from openai import OpenAI

client = OpenAI()

def get_context():

    docs = open("ritual_docs.txt").read()
    dataset = open("dataset_qa.txt").read()

    context = docs + "\n" + dataset

    return context