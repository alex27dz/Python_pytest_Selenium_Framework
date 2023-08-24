from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    name = "Alex Dezho Inc."
    social_media = {
        'Twitter': 'https://twitter.com/',
        'LinkedIn': 'https://www.linkedin.com/',
        'GitHub': 'https://github.com/',
    }
    bio = "Hello, I'm Alex Dezho! I'm a software engineer and data scientist based in [your location]. I have [number] years of experience in [your areas of expertise]. In my free time, I enjoy [your hobbies/interests]."
    email = "your_email_address@gmail.com"
    publications = [
        {
            'title': 'Publication Title 1',
            'date': 'Publication Date 1',
            'link': 'Publication Link 1',
        },
        {
            'title': 'Publication Title 2',
            'date': 'Publication Date 2',
            'link': 'Publication Link 2',
        },
        {
            'title': 'Publication Title 3',
            'date': 'Publication Date 3',
            'link': 'Publication Link 3',
        },
    ]
    return render_template('home.html', name=name, social_media=social_media, bio=bio, email=email, publications=publications)

if __name__ == '__main__':
    app.run(debug=True)
