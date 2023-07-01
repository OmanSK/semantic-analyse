# semantic-analyse
![Hugginface](https://img.shields.io/badge/Hugginface-bfb40f?style=for-the-badge)
![Pytorch](https://img.shields.io/badge/Pytorch-bfb40f?style=for-the-badge&logo=pytorch&logoColor=4d4c43)
![ONNX](https://img.shields.io/badge/ONNX-bfb40f?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-bfb40f?style=for-the-badge&logo=Streamlit&logoColor=5b5840)

<br />
<div align="center">
  
  <h3 align="center">Бинарный классификатор тестов</h3>
  <img src="https://storage.googleapis.com/lds-media/images/sigmoid-function.width-1200.png" alt="Logo" width="160" height="99">

  <p align="center">
    BERT-Transformer
  </p>
</div>

### О проекте

Классификатор на архитектуре BERT был переобучен под цели бинарной классификации, выдавая метку класса и процент уверенности в своем ответе.  Эта вероятность будет переведена в рейтинг от 1 до 10.
Всего в обеих выборках было 50 тысяч комментариев, по 25к на трейн и тест. Классы в трейне и тесте были сбалансированы близко к соотношению 50/50. В качестве метрики была выбрана <b>Accuracy</b>, 
т.к. в случае сбалансированных классов она хорошо отражает "способности" модели. После 3-й эпохи обучения метрика составила 92%, она лишь незначительно возросла после 2-й эпохи.</br>
<p>Confusion Matrix: ложноположительных ответов - 1009 (4%), ложноотрицательных - 951 (3.8%).</p>

Что было сделано:
* Исправлена предобученная модель под цели конкретной задачи;
* Модель из Pytorch + Hugginface была переведена в ONNX-формат
* Реализовано и задеплоено простое онлайн-приложение средствами библиотеки и сервиса Streamlit
