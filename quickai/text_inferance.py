from transformers import GPTNeoForCausalLM, GPT2Tokenizer, pipeline


def gpt_neo(prompt, model, max_length=100, temp=0.9):
    if model == "1.3B":
        model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")
        tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
    elif model == "2.7B":
        model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-2.7B")
        tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-2.7B")
    elif model == "125M":
        model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-125M")
        tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-125M")
    elif model == "350M":
        model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-350M")
        tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-350M")
    else:
        print("That is not a valid model")

    input_ids = tokenizer(prompt, return_tensors="pt").input_ids

    gen_tokens = model.generate(input_ids, do_sample=True, temperature=temp, max_length=max_length)
    gen_text = tokenizer.batch_decode(gen_tokens)[0]

    return gen_text


def sentiment_analysis(text, model="distilbert-base-uncased-finetuned-sst-2-english"):
    nlp = pipeline("sentiment-analysis", model=model)
    result = nlp(text)[0]
    return [result['label'], round(result['score'], 4)]


def q_and_a(context, question, model="distilbert-base-cased-distilled-squad"):
    nlp = pipeline("question-answering", model=model)
    result = nlp(question=question, context=context)
    return [result['answer'], round(result['score'], 4), result['start'], result['end']]


def mask_lang(text, model):
    nlp = pipeline("fill-mask")
    return nlp(f"HuggingFace is creating a {nlp.tokenizer.mask_token} that the community uses to solve NLP tasks.")


def ner(text, model="dbmdz/bert-large-cased-finetuned-conll03-english"):
    nlp = pipeline("ner", model=model)
    return nlp(text)


def summarization(text, length_max, length_min):
    summarizer = pipeline("summarization")
    return summarizer(text, max_length=length_max, min_length=length_min, do_sample=False)