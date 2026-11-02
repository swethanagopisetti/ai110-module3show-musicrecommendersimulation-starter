# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

Give your model a short, descriptive name.
Example: **VibeFinder 1.0**

---

## 2. Intended Use

Describe what your recommender is designed to do and who it is for.

Prompts:

- What kind of recommendations does it generate
- What assumptions does it make about the user
- Is this for real users or classroom exploration

---

## 3. How the Model Works

For each song, the recommender compares its genre and mood with the listener's
preferences. A matching genre adds 2 points, and a matching mood adds 1 point.
It also gives up to 1 point for energy: the closer the song's energy is to the
listener's target energy, the more points it receives.

The recommender adds these points to get a total score, then sorts the songs
from highest to lowest and returns the top results. If scores are tied, songs
stay in their original catalog order. In this version, genre, mood, and energy
are the only features that affect the score; other details such as tempo and
acousticness are not considered.

---

## 4. Data

Describe the dataset the model uses.

Prompts:

- How many songs are in the catalog
- What genres or moods are represented
- Did you add or remove data
- Are there parts of musical taste missing in the dataset

---

## 5. Strengths

Where does your system seem to work well

Prompts:

- User types for which it gives reasonable results
- Any patterns you think your scoring captures correctly
- Cases where the recommendations matched your intuition

---

## 6. Limitations and Bias

Where the system struggles or behaves unfairly.

Prompts:

- Features it does not consider
- Genres or moods that are underrepresented
- Cases where the system overfits to one preference
- Ways the scoring might unintentionally favor some users

In my experiments, the High-Energy Pop profile ranked Gym Hero first, even
though its mood is intense rather than happy. Its pop genre match and energy
close to the 0.9 target earn it a high score; mood does not affect ranking
because mood scoring is disabled. The 2-point genre match can outweigh a closer
energy fit, and exact genre matching treats related labels such as "pop" and
"indie pop" as different. As a result, listeners whose preferences do not
match the catalog's exact genre labels may get less relevant recommendations.

---

## 7. Evaluation

I tested the top five recommendations for High-Energy Pop (pop, energy 0.9),
Chill Lofi (lofi, energy 0.4), and Deep Intense Rock (rock, energy 0.9). I
expected the preferred genre and energy level to influence the results, and
they did. What surprised me was that Gym Hero, an intense pop song, ranked
first for High-Energy Pop and second for Deep Intense Rock: its high energy
suits both, and the system does not currently use mood to tell "happy" and
"intense" apart.

- **High-Energy Pop vs. Chill Lofi:** High-Energy Pop puts Gym Hero and Sunrise
  City at the top, while Chill Lofi puts Focus Flow, Midnight Coding, and
  Library Rain first. That makes sense because the first profile rewards pop
  and energy near 0.9, while the second rewards lofi and energy near 0.4.
- **High-Energy Pop vs. Deep Intense Rock:** Both profiles prefer high energy,
  so energetic songs such as Gym Hero and Storm Runner appear near the top for
  both. Gym Hero leads for Pop because it matches pop; Storm Runner leads for
  Rock because it matches rock. The happy/intense mood difference does not
  change the ranking because mood is not scored.
- **Chill Lofi vs. Deep Intense Rock:** Chill Lofi favors lower-energy lofi
  songs, while Deep Intense Rock favors high-energy rock, led by Storm Runner.
  Gym Hero still appears second for Rock because its energy is close to the
  target, even though its genre is pop. This shows how the genre bonus and
  energy score combine in the results.

---

## 8. Future Work

Ideas for how you would improve the model next.

Prompts:

- Additional features or preferences
- Better ways to explain recommendations
- Improving diversity among the top results
- Handling more complex user tastes

---

## 9. Personal Reflection

A few sentences about your experience.

Prompts:

- What you learned about recommender systems
- Something unexpected or interesting you discovered
- How this changed the way you think about music recommendation apps

---

# Completed Model Card

## 1. Model Name

**VibeMixer 1.0**

## 2. Goal / Task

VibeMixer suggests songs from a small catalog. It ranks songs based on a
listener's preferred genre and energy level.

## 3. Data Used

The catalog has 18 songs. Each song has a title, artist, genre, mood, energy,
tempo, valence, danceability, and acousticness. The current scorer uses only
genre and energy. This small sample does not cover every artist, genre, or
listener.

## 4. Algorithm Summary

A song gets 2 points if its genre exactly matches the listener's genre. It can
also get up to 1 point for having energy close to the listener's target. The
system adds these points, then shows the five highest-scoring songs. Mood is
not part of the score right now.

## 5. Observed Behavior / Biases

Gym Hero appears near the top for both High-Energy Pop and Deep Intense Rock.
It is a high-energy pop song, so it gets points for pop listeners and its
energy is also close to the rock listener's target. The system ignores mood,
so it cannot tell that Gym Hero is intense rather than happy. Genre is worth
more than energy, and exact genre matching can miss related labels like "pop"
and "indie pop."

## 6. Evaluation Process

I tested the top five results for High-Energy Pop (pop, energy 0.9), Chill Lofi
(lofi, energy 0.4), and Deep Intense Rock (rock, energy 0.9). Chill Lofi
ranked Focus Flow, Midnight Coding, and Library Rain highest. High-Energy Pop
ranked Gym Hero and Sunrise City highest, while Deep Intense Rock ranked Storm
Runner first and Gym Hero second. Pop and Rock share the high-energy target, so
some energetic songs show up for both; the genre match changes which song
leads. Chill Lofi has a lower energy target and a different genre, so its
results shift to quieter lofi songs. I was surprised that Gym Hero ranks first
for High-Energy Pop even though its mood is intense, because mood is not scored.

## 7. Intended Use and Non-Intended Use

This project is for learning how a simple music recommender scores and ranks
songs. It is not designed for real-world personalization or for making
important decisions. Its small catalog and limited scoring rules may produce
poor or repetitive recommendations.

## 8. Ideas for Improvement

- Use mood in the score so happy and intense preferences can differ.
- Add more songs and use tempo, valence, danceability, and acousticness.
- Add genre variety so recommendations are not too repetitive.
