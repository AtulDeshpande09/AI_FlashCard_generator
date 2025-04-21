from flask import Flask, request, render_template, redirect
import genanki
import os

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag, ne_chunk
from nltk.tree import Tree

app = Flask(__name__)


flashcards = [] 

def extract_named_entities(text):
    entities = []
    sentences = sent_tokenize(text)

    for sentence in sentences:
        words = word_tokenize(sentence)
        tags = pos_tag(words)
        chunks = ne_chunk(tags)

        entity_name = ""

        for chunk in chunks:
            if isinstance(chunk, Tree): 
                entity = " ".join(c[0] for c in chunk) 
                
                if entity_name:
                    entity_name += " " + entity
                else:
                    entity_name = entity
                
                entities.append((entity_name, sentence))
                entity_name = ""

    return entities


def generate_flashcards(text):
    entities = extract_named_entities(text)
    flashcards = []
    seen_sentences = set()

    for entity, sentence in entities:
        if entity in sentence:
            blank_sentence = sentence.replace(entity, "_____", 1)
            sentence_without_entity = sentence.replace(entity, "").strip()
            
            if sentence_without_entity not in seen_sentences: 
                seen_sentences.add(sentence_without_entity)
                flashcards.append((blank_sentence, entity))

    return flashcards




@app.route("/", methods=["GET", "POST"])
def index():
    global flashcards

    if request.method == "POST":
        text = request.form["text"]
        print("Input received!!")
        flashcards = generate_flashcards(text)
        return render_template("flashcard.html" , flashcards=flashcards)

    return render_template("index.html")

"""
@app.route("/flashcards")
def flashcard_page():
    return render_template("flashcards.html", flashcards=flashcards)
"""

@app.route("/flashcards/data")
def get_flashcards():
    return jsonify({"flashcards": flashcards})



@app.route("/download")
def download_flashcards():
    if not flashcards:
        return "No flashcards to download."

    deck = genanki.Deck(2059400110, "Generated Flashcards")
    model = genanki.Model(
        1607392319,
        "Simple Model",
        fields=[{"name": "Question"}, {"name": "Answer"}],
        templates=[
            {"name": "Card 1", "qfmt": "{{Question}}", "afmt": "{{FrontSide}}<hr id='answer'>{{Answer}}"},
        ],
    )

    for q, a in flashcards:
        note = genanki.Note(model=model, fields=[q, a])
        deck.add_note(note)

    package = genanki.Package(deck)
    package.write_to_file("flashcards.apkg")

    return send_file("flashcards.apkg", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
