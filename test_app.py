from app import generate_caption, generate_hashtag

def test_generate_caption():
    result = generate_caption("kopi")
    assert "kopi" in result
    print("✅ test_generate_caption PASSED")

def test_generate_hashtag():
    result = generate_hashtag("kopi susu")
    assert "#kopi" in result
    assert "#susu" in result
    print("✅ test_generate_hashtag PASSED")

if __name__ == "__main__":
    test_generate_caption()
    test_generate_hashtag()
