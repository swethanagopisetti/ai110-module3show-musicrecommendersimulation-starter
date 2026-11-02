from src.recommender import Song, UserProfile, Recommender, load_songs, recommend_songs, score_song


def test_score_song_returns_score_and_reasons_for_matches():
    score, reasons = score_song(
        {"genre": "pop", "mood": "happy", "energy": 0.8},
        {"genre": "pop", "mood": "happy", "energy": 0.6},
    )

    assert score == 3.8
    assert reasons == [
        "genre match (+2.0)",
        "mood match (+1.0)",
        "energy similarity (+0.80)",
    ]


def test_score_song_scores_energy_without_genre_or_mood_matches():
    score, reasons = score_song(
        {"genre": "pop", "mood": "happy", "energy": 0.8},
        {"genre": "rock", "mood": "sad", "energy": 0.8},
    )

    assert score == 1.0
    assert reasons == ["energy similarity (+1.00)"]


def test_recommend_songs_ranks_catalog_and_includes_explanations():
    preferred_song = {
        "title": "Preferred",
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
    }
    other_song = {
        "title": "Other",
        "genre": "rock",
        "mood": "sad",
        "energy": 0.4,
    }

    recommendations = recommend_songs(
        {"genre": "pop", "mood": "happy", "energy": 0.8},
        [other_song, preferred_song],
        k=1,
    )

    assert recommendations == [
        (
            preferred_song,
            4.0,
            "genre match (+2.0), mood match (+1.0), energy similarity (+1.00)",
        )
    ]


def test_recommend_songs_preserves_catalog_order_for_ties():
    songs = [
        {"title": "First", "genre": "rock", "mood": "sad", "energy": 0.8},
        {"title": "Second", "genre": "rock", "mood": "sad", "energy": 0.8},
    ]

    recommendations = recommend_songs(
        {"genre": "pop", "mood": "happy", "energy": 0.8},
        songs,
        k=2,
    )

    assert [song["title"] for song, _, _ in recommendations] == ["First", "Second"]


def make_small_recommender() -> Recommender:
    songs = [
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
        ),
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
        ),
    ]
    return Recommender(songs)


def test_recommend_returns_songs_sorted_by_score():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    # Starter expectation: the pop, happy, high energy song should score higher
    assert results[0].genre == "pop"
    assert results[0].mood == "happy"


def test_explain_recommendation_returns_non_empty_string():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""


def test_load_songs_converts_numeric_fields(tmp_path):
    csv_path = tmp_path / "songs.csv"
    csv_path.write_text(
        "id,title,artist,genre,mood,energy,tempo_bpm,valence,danceability,acousticness\n"
        "1,Test Song,Test Artist,pop,happy,0.82,118,0.84,0.79,0.18\n",
        encoding="utf-8",
    )

    songs = load_songs(str(csv_path))

    assert len(songs) == 1
    assert songs[0]["id"] == 1
    assert isinstance(songs[0]["id"], int)
    assert songs[0]["energy"] == 0.82
    assert isinstance(songs[0]["energy"], float)
    assert songs[0]["tempo_bpm"] == 118.0
    assert isinstance(songs[0]["tempo_bpm"], float)
