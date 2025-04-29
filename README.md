# Project: Reservoir & Dam Control Automation and M&A Text Analysis

This repository contains implementations for two primary domains:

1. **Reservoir and Dam Operation Automation** using Reinforcement Learning and Q-Learning.
2. **Merger & Acquisition (M&A) Press Release Text Analysis** using NLP techniques (word frequency, sentiment analysis, word clouds).

---

## Repository Structure
```
.
├── reservoir_operation_rl.ipynb        # Colab notebook: PPO for reservoir operation control
├── dam_qlearning_and_shadow.py         # Python script: Q-Learning + shadow learning for Hirakud Dam
├── deal_synopsis_word_frequency.py     # Word frequency analysis on "Deal Synopsis" column
├── mna_sentiment_analysis_t5.py        # T5-based sentiment analysis for M&A press releases
├── deal_synopsis_frequency_analysis.py # Interactive frequency analysis by row/industry filters
├── deal_synopsis_wordcloud.py          # Word cloud generator for Deal Synopsis by various filters
├── cell_wordcloud_generator.py         # Word cloud generator for any cell (row, column)
├── requirements.txt                    # Pinned dependencies for all scripts/notebooks
├── README.md                           # This file
└── reservoir_results.png               # Sample output plot from PPO notebook
```  

---

## Requirements
- Python 3.7+
- Jupyter / Colab (for `.ipynb`)
- Install dependencies via:
  ```bash
  pip install -r requirements.txt
  ```

**Key Dependencies**:
```
pandas
numpy
matplotlib
gym==0.21.0
stable-baselines3
shimmy>=2.0
pywr
transformers
datasets
wordcloud
Pillow
```  

---

## 1. Reservoir Operation with PPO

**File:** `reservoir_operation_rl.ipynb`  
**Description:** Train a PPO agent to manage reservoir releases given constant inflow.  
**Usage:** Open in Colab & run all cells.  

**Core Functions:**
- `ReservoirEnv`: custom Gym environment
- `train_model()`: trains PPO for 10k timesteps
- `evaluate_model()`: runs a test simulation, plots storage, actions, inflow, reward

---

## 2. Hirakud Dam Control: Q-Learning & Shadow Learning

**File:** `dam_qlearning_and_shadow.py`  
**Description:** Tabular Q-learning agent refines discharge decisions; shadow-learning phase incorporates user feedback.  
**Usage:**
```bash
python dam_qlearning_and_shadow.py
```  

**Phases:**
1. **Training Phase**: agent self-explores.
2. **Shadow Learning**: user inputs discharge & impact scores.
3. **Plots**: reward trends & inflow patterns.

---

## 3. Word Frequency Analysis

**File:** `deal_synopsis_word_frequency.py`  
**Description:** Static script to compute top N word counts in the "Deal Synopsis" column.  

**File:** `deal_synopsis_frequency_analysis.py`  
**Description:** Interactive CLI: filter by row number or macro industry, show top words & frequencies.

---

## 4. M&A Sentiment Analysis with T5

**File:** `mna_sentiment_analysis_t5.py`  
**Description:** Uses a pre-trained T5 model to perform conditional generation for sentiment classification or summarization of press releases.

---

## 5. Word Cloud Visualizations

**File:** `deal_synopsis_wordcloud.py`  
**Description:** Generate word clouds filtered by row index, Acquiror Macro Industry, or Target Macro Industry.

**File:** `cell_wordcloud_generator.py`  
**Description:** General-purpose word cloud generator for any specific DataFrame cell (given row & column).

---

## Usage & Examples
1. **Text Analysis**:
   ```bash
   python deal_synopsis_word_frequency.py
   python deal_synopsis_frequency_analysis.py
   python deal_synopsis_wordcloud.py
   python cell_wordcloud_generator.py
   ```
2. **Sentiment**:
   ```bash
   python mna_sentiment_analysis_t5.py
   ```
3. **RL & Q‑Learning**: use `.ipynb` or run script as described above.

Ensure `train.csv` (with columns like "Deal Synopsis", "Acquiror Macro Industry", "Target Macro Industry") is placed in the data path expected by scripts or update code paths accordingly.

---

## Customization
- Update constants (e.g., `NUM_DAYS`, `ACTIONS`, `STATE_BINS`) in RL/Q‑Learning scripts.
- Extend `stop_words` sets or NLP parameters for text analysis.
- Adjust T5 training arguments or model selection in `mna_sentiment_analysis_t5.py`.

---

## License
This project is MIT-licensed—feel free to adapt and extend.

