import os
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dressCode.settings')

import django

django.setup()

from codeforgood.models import NewsArticle, VideoArticle, RoleModel, VisitedPagesCounter


def populate():
    # dummy News articles
    news = {"title": "News Article ",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            "picture": "cat.jpg"}
    for i in range(1, 10):
        n = NewsArticle.objects.get_or_create(title=news["title"] + str(i), description=news["description"],
                                              picture=news["picture"], date=timezone.now())[0]
        n.save()

    # Videos promoting joining tech
    videos = {"video1": {"title": "Careers in Tech: My name is Tess",
                         "description": "Meet Tess, a software engineer at Google.",
                         "url": "https://www.youtube.com/watch?v=RfbbDgx6l1g&list=PLzdnOPI1iJNfpWMZjEmumqVB09rXAVJRM",
                         "views": 20},
              "video2": {"title": "Careers in Tech: My name is Kinsley",
                         "description": "Meet Kinsley, a software engineer at Facebook.",
                         "url": "https://www.youtube.com/watch?v=suJZ9z426P0&list=PLzdnOPI1iJNfpWMZjEmumqVB09rXAVJRM&index=2",
                         "views": 20},
              "video3": {"title": "Careers in Tech: My name is Federico",
                         "description": "Meet Federico Gomez Suarez, a software engineer at Microsoft.",
                         "url": "https://www.youtube.com/watch?v=EUF2mad21jo&list=PLzdnOPI1iJNfpWMZjEmumqVB09rXAVJRM&index=3",
                         "views": 20},
              "video4": {"title": "Careers in Tech: My name is Brina",
                         "description": "Meet Brina Lee, a software engineer at Instagram.",
                         "url": "https://www.youtube.com/watch?v=t0-Z_LfGwUM&list=PLzdnOPI1iJNfpWMZjEmumqVB09rXAVJRM&index=4",
                         "views": 20},
              "video5": {"title": "Careers in Tech: My Name is Polina",
                         "description": "Meet Polina, a data scientist at Electronic Arts.",
                         "url": "",
                         "views": 20},
              "video6": {"title": "What is the Internet?",
                         "description": "What is the internet?  Short answer: a distributed packet-switched network.",
                         "url": "https://www.youtube.com/watch?v=Dxcc6ycZ73M&list=PLzdnOPI1iJNfMRZm5DDxco3UdsFegvuB7",
                         "views": 20},
              "video7": {"title": "The Internet: How Search Works",
                         "description": "Join John, Google's Chief of Search and AI, and Akshaya, from Microsoft Bing, to find out how search really works.",
                         "url": "https://www.youtube.com/watch?v=LVV_93mBfSU&list=PLzdnOPI1iJNfMRZm5DDxco3UdsFegvuB7&index=8",
                         "views": 20},
              "video8": {"title": "The Internet: Encryption & Public Keys",
                         "description": "Mia Epner, who works on security for a US national intelligence agency, explains how cryptography allows for the secure transfer of data online. ",
                         "url": "https://www.youtube.com/watch?v=ZghMPWGXexs&list=PLzdnOPI1iJNfMRZm5DDxco3UdsFegvuB7&index=6",
                         "views": 20}
              }
    for video in videos:
        v = VideoArticle.objects.get_or_create(title=videos[video]["title"], description=videos[video]["description"],
                                               url=videos[video]["url"], views=videos[video]["views"])[0]
        v.save()

    # Examples of rolemodels in tech
    rolemodels = {"rolemodel1": {"title": "Women Leaders in Tech Law: Sarita Venkat, Apple",
                                 "description": "Sarita Venkat, who was recently named director of IP transactions at Apple, co-created and co-hosts the “Heels of Justice” podcast, which celebrates other trailblazing women in law. Venkat’s work on the podcast earned her a spot as one of 21 Women Leaders in Tech Law as part of The Recorder’s California Leaders in Tech Law and Innovation Awards.",
                                 "picture": "saritavenkat.jpg",
                                 "url": "https://www.law.com/therecorder/2019/10/25/women-leaders-in-tech-law-sarita-venkat-apple/?slreturn=20190926143151",
                                 "gender": "Female",
                                 "ethnicity": "White",
                                 "position": "Software Developer"},

                  "rolemodel2": {"title": "Women Leaders in Tech Law: Andrea Lobato, Eaze Technologies",
                                 "description": "Andrea Lobato, the chief risk officer of Eaze Technologies and an alum of Lyft’s regulatory compliance program, has helped create the single largest marketplace and tech platform for the legal access to cannabis products in California, if not the entire United States.",
                                 "picture": "lobatoandrea.jpg",
                                 "url": "https://www.law.com/therecorder/2019/10/26/women-leaders-in-tech-law-andrea-lobato-eaze-technologies/",
                                 "gender": "Female",
                                 "ethnicity": "White",
                                 "position": "Software Developer"},
                  "rolemodel3": {
                      "title": "App developer and former Victoria's Secret model inspires Perth women in tech",
                      "description": "Lyndsey Scott has had a career as an internationally acclaimed model, working for brands such as Victoria's Secret and Gucci, but she has always had a burning passion for computer programming.",
                      "picture": "lyndseyscott.jpg",
                      "url": "https://www.brisbanetimes.com.au/national/western-australia/app-developer-and-former-victoria-s-secret-model-inspires-perth-women-in-tech-20191025-p534cb.html",
                      "gender": "Female",
                      "ethnicity": "White",
                      "position": "Software Developer"},
                  "rolemodel4": {"title": "Susan Wojcicki",
                                 "description": "Susan Wojcicki grew up surrounded by Stem: her father was a physics professor at Stanford University and, as a child, she lived on campus with famous mathematicians as neighbours. She joined Google the year after it was founded and has been behind many of the search engine’s most defining features, including creating the first ever Google Doodle. She became head of YouTube last year, after it was bought by Google in 2006.",
                                 "picture": "susanwojcicki.jpeg",
                                 "url": "https://www.theguardian.com/guardian-professional/women-leadership-blog/gallery/2015/jun/22/10-of-the-best-female-role-models-in-tech-in-pictures",
                                 "gender": "Female",
                                 "ethnicity": "White",
                                 "position": "Software Developer"},
                  "rolemodel5": {"title": "Belinda Parmar",
                                 "description": "One of the UK’s leading campaigners to get more women into tech, Belinda Parmar is the founder of Little Miss Geek and chief executive of Lady Geek. She was awarded an OBE for services to women in technology in 2014 following campaigns like Her In Hero which brought in support from senior politicians. She has explained her campaigning, saying: “Diversity is important in any industry, but is especially relevant when it comes to technology. Tech is the way that world talks to each other.”",
                                 "picture": "belindaparmar.jpeg",
                                 "url": "https://www.theguardian.com/guardian-professional/women-leadership-blog/gallery/2015/jun/22/10-of-the-best-female-role-models-in-tech-in-pictures",
                                 "gender": "Female",
                                 "ethnicity": "White",
                                 "position": "Software Developer"},
                  "rolemodel6": {"title": "Sheryl Sandberg",
                                 "description": "As chief operating officer of Facebook, Sheryl Sandberg is one of the world’s most high-profile women in the tech sector. After an economics degree and a stint at Google, she was hired by Facebook in 2008 and later became the first woman on the company’s board. She has also been a champion of gender equality – in her book about women in work, Lean In, she writes: “We stand on the shoulders of the women who came before us, women who had to fight for the rights that we now take for granted.”",
                                 "picture": "sherylsandberg.jpg",
                                 "url": "https://www.theguardian.com/guardian-professional/women-leadership-blog/gallery/2015/jun/22/10-of-the-best-female-role-models-in-tech-in-pictures",
                                 "gender": "Female",
                                 "ethnicity": "White",
                                 "position": "Software Developer"}
                  }

    for rolemodel in rolemodels:
        r = RoleModel.objects.get_or_create(title=rolemodels[rolemodel]["title"],
                                            description=rolemodels[rolemodel]["description"],
                                            picture=rolemodels[rolemodel]["picture"],
                                            url=rolemodels[rolemodel]["url"],
                                            gender=rolemodels[rolemodel]["gender"],
                                            ethnicity=rolemodels[rolemodel]["ethnicity"],
                                            position=rolemodels[rolemodel]["position"])[0]
        r.save()

    # Initialize dummy views for each page
    vpc = VisitedPagesCounter.objects.create(home_views=0,
                                             careers_views=0,
                                             contact_views=0,
                                             meet_your_hero_views=0,
                                             news_views=0,
                                             videos_views=0,)
    vpc.save()


if __name__ == '__main__':
    print("Starting codeforgood population script..")
    populate()
