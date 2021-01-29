# Jatayu-ContentModeration

## Content Moderation for Online Chat Application

In today's world, it is a well known fact the internet and social media can be used to influence opinions and spread hate. Although the platform is not to blame, popular brands like facebook lose customers and their usage statistics go down because many people find some content offensive or inappropriate. In the recent past, people have been very vocal about their opinions, and have been posting offendable posts. This has caused social unrest and even riots between various sections of the society.

User generated contents contains different types of opinions and expressions through written texts, images or videos. And such contents may also contain objectionable visuals or which is not favorable for many people viewing such contents.

## Why Content Moderation is important
Moderating the content on social media websites is important, as now such platforms are used to promote the business, products and brands and such spam contents can disappoint other customers and discourage them to either stay away from such platforms or minimize the use of social media sites.

## Our Solution
Our idea is to develop a filter which can be embedded in any chat system or social media to prevent cyberbullying, hate spread, obscenity etc.

We have came up with a AI based Content Moderation model which is deployed as an [API](https://github.com/Slainteee/Jatayu-ContentModeration/blob/master/app.py) and it can be easily used in any Web [(demo)](https://github.com/Slainteee/Jatayu-ContentModeration/tree/master/Web-Frontend) or Mobile [(demo)](https://github.com/Slainteee/Jatayu-ContentModeration/tree/master/App) based platforms.

## Process Flow
For the image data, we are checking for any inappropriate text in the image or whether the image contains violence. The API checks the same for audio and video data aswell . Apart from images and videos of violence, It will also check for sexual or nudity related contents like, sexual activities, pornography, offensive signs, stripped images of people, especially females with revealing dresses and erotic gestures that are against the community of the chat platforms. In case of text data, along with checking for hatefull speech , the API will even check for any malicious links in the text in order to prevent cyberattacks such as phishing attacks. It will also check for spam messages/mails with circulates in online chat plaforms in the form of fake advertisements,self promotion etc.

