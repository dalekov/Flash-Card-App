# Flashy 🌟 - A Flashcard App

Flashy is a simple and interactive flashcard application built with Python and Tkinter. The app helps users learn new languages by displaying flashcards with words in Spanish and their English translations. Users can mark words they know, allowing the app to focus on words that still need practice. 📚

## Features ✨

- Randomly displays flashcards with Spanish words. 🇪🇸
- Flips the card to show the English translation after a set time. 🇬🇧
- Allows users to mark words as known, removing them from the study list. ✅
- Saves progress in a CSV file for future sessions. 💾

## Technologies Used ⚙️

- Python 🐍
- Tkinter (for the GUI) 🖥️
- Pandas (for data handling) 📊

## Installation 🚀

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/flashy.git
   cd flashy
2. **Install depedencies**
   ```bash
   pip install pandas
3. **Prepare the data:**
   - Create a folder named data.
   - Place your spanish_words.csv file inside the data folder. This file should contain the Spanish words and their English translations.
4. **Run the application:**
   ```bash
   python main.py

## Usage
- Upon launching, the app will display a random Spanish word.
- The card will flip after 3 seconds to show the English translation.
- If you know the word, click the "Right" button to mark it as known.
- If you don't know the word, click the "Wrong" button to see the next card.
