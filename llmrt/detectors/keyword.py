def detector(response, keywords):
    return any((keyword.lower() in response.lower()) for keyword in keywords)