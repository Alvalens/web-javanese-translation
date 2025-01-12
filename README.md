# web-javanese-translation

![visitor badge](https://visitor-badge.laobi.icu/badge?page_id=transWJT)

Welcome to web-javanese-translation, a simple yet powerful translation website that leverages Python, Flask, and TensorFlow to translate text from Javanesse krama to ngoko using a Transformer algorithm. The model is provided as a Jupyter Notebook which you can experiment and train the model yourself.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white) ![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

## Features

* **Real-time Translation** : Instantly translate text from Krama to Ngoko.
* **Transformer Algorithm** : Utilizes a state-of-the-art Transformer model for high-quality translations.
* **Web Interface** : User-friendly web interface built with Flask.
* **Jupyter Notebook** : Model training and evaluation provided in a Jupyter Notebook for transparency and customization.

## Installation

Ensure you have Python version 3.10 and pip installed (windows). If not, you can install Python from [python.org](https://www.python.org/).

1. Clone the Repository

   ```powershell
   git clone "https://github.com/Alvalens/web-javanese-translation.git"
   ```
2. Navigate to project directory

   ```powershell
   cd web-javanese-translation
   ```
3. Create python virtual envirotment and activate it (optional)

   ```powershell
   python -m venv venv
   .venv\Scripts\activate
   ```
4. Install Dependency, also ensure you run notebook first cell  at `notebook/transformer_kr-ng.ipynb`

   ```
   pip install -r requirements.txt

   ```
5. Start the Flask development server, also before running the server train the model first

   ```powershell
   py app.py
   ```

## Contributing

Contributions are welcome! If you find any issues or have suggestions, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Special Thanks

**@Alvalens @[**atavada**](https://github.com/atavada)**
