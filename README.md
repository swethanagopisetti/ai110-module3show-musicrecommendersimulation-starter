# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Real-world music recommendations combine signals such as listening behavior, song characteristics, and user feedback to predict what someone may enjoy next. This recommender uses a simpler content-based approach: it prioritizes matching a user's preferred genre and mood, then scores songs by how closely numerical features such as energy fit the user's target.

---

## How The System Works

The simulation's data objects use these fields:

- **`Song`:** ID, title, artist, genre, mood, energy, tempo (BPM), valence, danceability, and acousticness.
- **`UserProfile`:** favorite genre, favorite mood, target energy, and whether the user likes acoustic music.

The example taste profile used for comparisons is:

```python
user_profile = {
    "genre": "pop",
    "mood": "happy",
    "energy": 0.8,
}
```

It represents a listener looking for happy pop with energy close to 0.8 on a 0–1 scale.

### Data Flow

```text
INPUT: User preferences (genre, mood, target energy)
                 │
                 ▼
PROCESS: Loop through every song in songs.csv
  +2.0 points for a genre match
  +1.0 point for a mood match
  + energy similarity: 1 - abs(song energy - target energy)
                 │
                 ▼
OUTPUT: Sort songs by score and return the top K recommendations
```

### Algorithm Recipe

For each song, calculate:

```text
genre_points = 2.0 if song genre matches the user's genre, otherwise 0
mood_points = 1.0 if song mood matches the user's mood, otherwise 0
energy_similarity = 1 - abs(song energy - target energy)
total_score = genre_points + mood_points + energy_similarity
```

Energy and target energy are on a 0–1 scale, so energy similarity contributes between 0 and 1 point. Rank songs by total score, highest first, and return the top `k`; preserve catalog order for ties.

The maximum score is 4.0 points. Genre carries twice the weight of mood, while energy closeness can contribute up to 1.0 point. Other song fields, such as tempo, valence, danceability, and acousticness, are not scored until the profile includes corresponding targets.

### Potential Biases

Because a genre match is worth twice as much as a mood match, the ranking may favor a genre-matching song over one that better fits the user's mood. The small catalog may also underrepresent some genres and moods, limiting which songs can be recommended.

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

```
% python3 src/main.py
Loaded songs: 18

Top recommendations:

1. Sunrise City
   Final score: 3.98
   Reasons:
   - genre match (+2.0)
   - mood match (+1.0)
   - energy similarity (+0.98)

2. Gym Hero
   Final score: 2.87
   Reasons:
   - genre match (+2.0)
   - energy similarity (+0.87)

3. Rooftop Lights
   Final score: 1.96
   Reasons:
   - mood match (+1.0)
   - energy similarity (+0.96)

4. Night Drive Loop
   Final score: 0.95
   Reasons:
   - energy similarity (+0.95)

5. Neon Carnival
   Final score: 0.93
   Reasons:
   - energy similarity (+0.93)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this
