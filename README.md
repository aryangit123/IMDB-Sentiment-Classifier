# IMDb BERT Sentiment Classifier — Streamlit UI

## 1. Expected project structure

```text
imdb-bert-streamlit/
├── app.py
├── requirements.txt
├── .gitignore
└── imdb_bert/
    ├── config.json
    ├── model.safetensors (or pytorch_model.bin)
    ├── tokenizer_config.json
    ├── tokenizer.json
    └── vocab.txt
```

The `imdb_bert/` folder is created by the notebook's final save cell. It is not included in this starter bundle because it contains your trained model weights.

## 2. Install and run in VS Code (Windows PowerShell)

Open the folder in VS Code, then in its terminal run:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

If PowerShell blocks activation, you can run the environment's Python directly:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m streamlit run app.py
```

## 3. Save the model from your notebook

Run the notebook's training and save cells. The notebook currently has:

```python
SAVE_DIR = "./imdb_bert"
trainer.save_model(SAVE_DIR)
tokenizer.save_pretrained(SAVE_DIR)
```

Make sure this folder is in the same project directory as `app.py`, or set `MODEL_DIR` to the folder containing the saved model.

## 4. Important

- Train/fine-tune the model in the notebook; do not train it every time Streamlit starts.
- Keep the model folder out of Git if it is too large; use an appropriate model hosting/storage option for deployment.
- For Streamlit Community Cloud, the app must be able to access the model files. A large model folder may exceed repository or hosting limits.
