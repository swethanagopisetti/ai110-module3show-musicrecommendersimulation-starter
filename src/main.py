"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    user_profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.4},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.9},
    }

    for profile_name, user_prefs in user_profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\nTop recommendations for {profile_name}:\n")
        if not recommendations:
            print("No recommendations found.")
            continue

        for rank, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"{rank}. {song['title']}")
            print(f"   Final score: {score:.2f}")
            print("   Reasons:")
            for reason in explanation.split(", "):
                print(f"   - {reason}")
            print()


if __name__ == "__main__":
    main()
