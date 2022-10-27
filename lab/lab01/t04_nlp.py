from google.cloud import language


def get_text_sentiment(text):
    client = language.LanguageServiceClient()
    document = language.Document(
        content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    score = sentiment.score
    magnitude = sentiment.magnitude

    if score >= 0.6 and magnitude >= 1.0:
        return "Clearly Positive"
    elif score <= -0.6 and magnitude >= 1.0:
        return "Clearly Negative"
    elif -0.3 < score < 0.3:
        return "Mixed"
    else:
        return "Neutral"


def get_text_entities(text):
    client = language.LanguageServiceClient()
    document = language.Document(
        content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_entities(document=document)

    results = []
    for entity in response.entities:
        entity_dict = dict(
            name=entity.name,
            type=entity.type_.name,
            salience=f"{entity.salience:.1%}",
            wikipedia_url=entity.metadata.get("wikipedia_url", "-"),
            mid=entity.metadata.get("mid", "-"),
        )
        results.append(entity_dict)

    return results
