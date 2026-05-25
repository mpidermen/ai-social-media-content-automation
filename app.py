def generate_caption(topic):
    return f"Nikmati {topic} terbaik hari ini! Jangan lewatkan promo spesial kami."

def generate_hashtag(topic):
    words = topic.lower().split()
    return " ".join([f"#{w}" for w in words]) + " #promo #viral #trending"

if __name__ == "__main__":
    topic = "kopi arabika"
    print("Caption:", generate_caption(topic))
    print("Hashtag:", generate_hashtag(topic))
