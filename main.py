from story_engine import StoryEngine


def main():
    print("=== NEON CIRCUIT STORY ENGINE ===\n")
    engine = StoryEngine()

    character_name = input("Enter character name: ").strip()
    car_type = input("Enter car type: ").strip()

    print("\nGenerating your story...\n")

    try:
        story = engine.generate_story(character_name, car_type)
        print(story)
    except ValueError as e:
        print(f"Input error: {e}")
    except RuntimeError as e:
        print(f"Generation error: {e}")


if __name__ == "__main__":
    main()