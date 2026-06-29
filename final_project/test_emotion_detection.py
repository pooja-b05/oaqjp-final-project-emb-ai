from EmotionDetection.emotion_detection import emotion_detector

def test_emotions():
    test_cases = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }

    for text, expected in test_cases.items():
        result = emotion_detector(text)
        detected = result["dominant_emotion"]

        print(f"Text: {text}")
        print(f"Expected: {expected}, Detected: {detected}")
        print("")

        # Assertion check
        assert detected == expected

    print("✅ All unit tests passed!")

# Execute tests
if __name__ == "__main__":
    test_emotions()