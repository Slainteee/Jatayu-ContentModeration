# Jatayu-ContentModeration
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

## Content Moderation for Online Chat Application

In today's world, it is a well known fact the internet and social media can be used to influence opinions and spread hate. Although the platform is not to blame, popular brands like facebook lose customers and their usage statistics go down because many people find some content offensive or inappropriate. In the recent past, people have been very vocal about their opinions, and have been posting offendable posts. This has caused social unrest and even riots between various sections of the society.

User generated contents contains different types of opinions and expressions through written texts, images or videos. And such contents may also contain objectionable visuals or which is not favorable for many people viewing such contents.

## Why Content Moderation is important
Moderating the content on social media websites is important, as now such platforms are used to promote the business, products and brands and such spam contents can disappoint other customers and discourage them to either stay away from such platforms or minimize the use of social media sites.

## The Solution
The idea is to develop a filter which can be embedded in any chat system or social media to prevent cyberbullying, hate spread, obscenity etc.

We have came up with a AI based Content Moderation model which is deployed as an API and it can be easily used in any Web or Mobile based platforms.

## Process Flow
For the image data, we are checking for any inappropriate text in the image or whether the image contains violence. The API checks the same for audio and video data aswell . Apart from images and videos of violence, It will also check for sexual or nudity related contents like, sexual activities, pornography, offensive signs, stripped images of people, especially females with revealing dresses and erotic gestures that are against the community of the chat platforms. In case of text data, along with checking for hatefull speech , the API will even check for any malicious links in the text in order to prevent cyberattacks such as phishing attacks. It will also check for spam messages/mails with circulates in online chat plaforms in the form of fake advertisements,self promotion etc.

## Architecture Diagram
![picture alt](https://github.com/Slainteee/Jatayu-ContentModeration/blob/master/documents/architecture.png)

## Tech Stack
![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)
![](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)
![](https://img.shields.io/badge/conda-342B029.svg?&style=for-the-badge&logo=anaconda&logoColor=white)
![](https://img.shields.io/badge/sublime_text-%23575757.svg?&style=for-the-badge&logo=sublime-text&logoColor=important)
1. Languages : Python. We will use Python basically for everything, from Modeling to ETL
2. AI/ML : Pytorch/Tensorflow(for most Deep Learning Tasks) and Scikit-Learn(Our go-to for most Non DL Tasks
3. NLP : NLTK/spaCy for extracting features from the text data.
4. OCR : For extracting Text from images, We rely on Tesseract OCR Engine.
5. Speech Recognition : Analysing Audio input can be achieved through Speech to text Conversion. We have used Sphinx/Google Speech Recognition for the same.
6. Version Control : Github is the best choice for any group project for code control and tracking.
7. Additional Libraries: Pandas, Numpy, MatplotLib
8. Google Colab for GPU support.
9. Project Management: We used Notion and We find ourself using Notion for more than just project management and tracking. We were able to keep track of what Our Team Members do on a daily basis, make sure that we allocate time efficiently, and track what everyone on the team is up to.

## Installation Guide
* For Windows

1) CLone the Repo.
```
git clone https://github.com/Slainteee/Jatayu-ContentModeration.git
```
2) Change the working directory.
```
cd Jatayu-ContentModeration
```
3) Create and activate Virtual Environment ([Conda](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/) is preferred).
4) Install the required packages.
```
pip install -r requirements.txt
```
5) Install OCR Engine: The project uses pytesseract OCR engine. To install pytesseract, Follow [this](https://stackoverflow.com/a/53672281)

6) After succesfully installing pytesseract, set the tesseract path in the script. Add the following line in the [app.py](https://github.com/Slainteee/Jatayu-ContentModeration/blob/master/app.py)
```python
pytesseract.pytesseract.tesseract_cmd = <tesseract-path-here>
```
The Project is ready to run on your local machine💥💥

## To Run
* For Windows

1) Open 2 tabs of Command prompt
2) Change the working directory
```
cd Jatayu-ContentModeration
```
3) Activate virtual Environment([Conda](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/) is preferred).
4) In first CMD tab
```
python app.py
```
It will start the API server.
5) In second CMD tab, change the directory to run the UI sample
```
cd Web-Frontend
```
6) Create a folder named upload inside the static folder
```
cd static && mkdir uploads
```
7) Return to the Web-Frontend Directory
```
cd ..
```
8) Execute the server.py to start flask web server
```
python server.py
```
9) Flask server will run on host='127.0.0.1' and port=1025
10) Open any web browser(Chrome preferred) and type ```127.0.0.1:1025``` to see the live demo

## Tests

Testing will ensure that the api is working as expected. The project uses [pytest]() as a test framework. After setting up the basic test structure, pytest makes it really easy to write and provides a lot of flexibility for running the tests.

To Run the tests:

1) Navigate to the project directory
```
cd Jatayu-ContentModeration
```
2) Activate virtual Environment
3) Run the test script
```
python test.py
```

Wanna know a secret, You can add more tests 😊😊. So go ahead and create a pull request🎉🎉

## To Contribute

“No one and nothing is perfect, or we wouldn't have uniqueness.” <-- Random quote from google. You can find more [here](https://parade.com/937586/parade/life-quotes/) -->. 
“No matter how good you get you can always get better, and that's the exciting part.” <- Another one 😅😅->. To Contribute to the project and make it better, follow the [contributing guidelines](https://github.com/Slainteee/Jatayu-ContentModeration/blob/master/CONTRIBUTING.md) for project specific details.

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://www.linkedin.com/in/khushhalreddy"><img src="https://avatars.githubusercontent.com/u/58569950?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Khushhal Reddy</b></sub></a><br /><a href="#infra-KKhushhalR2405" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/Slainteee/Jatayu-ContentModeration/commits?author=KKhushhalR2405" title="Tests">⚠️</a> <a href="https://github.com/Slainteee/Jatayu-ContentModeration/commits?author=KKhushhalR2405" title="Code">💻</a></td>
    <td align="center"><a href="http://www.linkedin.com/in/ranjan-panda"><img src="https://avatars.githubusercontent.com/u/69582038?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ranjan Panda</b></sub></a><br /><a href="#plugin-ranjan-panda" title="Plugin/utility libraries">🔌</a></td>
    <td align="center"><a href="https://github.com/Aryamaan777"><img src="https://avatars.githubusercontent.com/u/63562112?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Aryamaan Srivastava</b></sub></a><br /><a href="#data-Aryamaan777" title="Data">🔣</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
