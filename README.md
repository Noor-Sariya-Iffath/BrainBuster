# BrainBuster

A Python command-line quiz app that fetches random multiple-choice trivia questions from the Open Trivia Database (OpenTDB). Users can answer questions, track their score, and exit anytime by typing 'exit'.

## Features

- Fetches random trivia questions from the OpenTDB API.  
- Supports multiple categories and difficulty levels.  
- Provides multiple-choice options and tracks score.  
- Exit the quiz anytime by typing 'exit'.

## Requirements

- Python 3.x  
- requests library (install with `pip install requests`)

## Customization

- **Category & Difficulty**: Change the category and difficulty by modifying the `fetch_questions()` parameters.  
- **Number of Questions**: Adjust the number of questions by changing the `amount` parameter.
