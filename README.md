# Jatayu-ContentModeration

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

6) After succesfully installing pytesseract, set the tesseract path in the script. Add the following line in the [app.py](https://github.com/Slainteee/Jatayu-ContentModeration/blob/master/app.py) file(line 38)
```python
pytesseract.pytesseract.tesseract_cmd = <tesseract-path-here>
```
The Project is ready to run on your local machine💥💥



