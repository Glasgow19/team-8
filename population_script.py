import os
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dressCode.settings')

import django

django.setup()

from codeforgood.models import NewsArticle, VideoArticle, RoleModel, VisitedPagesCounter
from django.contrib.auth.models import User



def create_superuser(username, password):
    superuser = User.objects.get_or_create(username=username)[0]
    superuser.set_password(password)
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.save()
    return superuser


def populate():
    # Superuser is used to create the initial categories
    superuser = create_superuser("admin", "root")

    # dummy News articles
    news = {"article1": {"title": "The Week in Tech: Google’s Quantum Leap",
                         "description": "The company can run esoteric calculations on exotic new hardware faster than is possible on a supercomputer. It’s an achievement of little practical use, but still important.",
                         "picture": "googlequantum.jpg",
                         "url": "https://www.nytimes.com/2019/10/25/technology/google-quantum.html",
                         "views": 20},
            "article2": {"title": "Monday briefing: The first all-women spacewalk crew has repaired the  ISS",
                         "description": "Nasa's Christina Koch and Jessica Meir replaced a power control unit and made history, Malicious apps could use Amazon Alexa and Google Home to eavesdrop.",
                         "picture": "spacewalk.jpg",
                         "url": "https://www.wired.co.uk/article/wired-awake-211019",
                         "views": 20},
            "article3": {"title": "Smart gumshields are monitoring rugby concussions",
                         "description": "Concussions have become a growing issue in contact sports. New on-field technology is helping to understand the consequences",
                         "picture": "rugby.jpg",
                         "url": "https://www.wired.co.uk/article/rugby-concussion-opro-mouthguard",
                         "views": 20},
            "article4": {"title": "Migrating eagles racked up a huge cellular bill",
                         "description": "Migrating eagles with tracking beacons that send texts reportedly accrued roaming charges so high that scientists had to take out a loan to pay for them, as well as attempt to raise money from a crowdfunding campaign — because some of the birds made unexpected detours (via BBC).",
                         "picture": "eagle.jpg",
                         "url": "https://www.theverge.com/2019/10/25/20933022/migrating-eagles-scientific-research-major-data-roaming-charges-sms-russia-iran-kazakhstan",
                         "views": 20},
            "article5": {"title": "THE STATE OF AI IN 2019",
                         "description": "It’s a common psychological phenomenon: repeat any word enough times, and it eventually loses all meaning, disintegrating like soggy tissue into phonetic nothingness. For many of us, the phrase “artificial intelligence” fell apart in this way a long time ago. AI is everywhere in tech right now, said to be powering everything from your TV to your toothbrush, but never have the words themselves meant less.",
                         "picture": "aintel.jpg",
                         "url": "https://www.theverge.com/2019/1/28/18197520/ai-artificial-intelligence-machine-learning-computational-science",
                         "views": 20},
            "article6": {"title": "Samsung announces more powerful Exynos processor",
                         "description": "Just shy of two months after announcing the Exynos 980, Samsung has announced a new chipset, the Exynos 990. The new processor is built on Samsung’s 7nm process, and includes a Mali-G77 GPU that increases graphical performance or power efficiency compared to Samsung’s previous chip by up to 20 percent as well as an octa-core CPU that should be 20 percent faster.",
                         "picture": "samsungchip.jpg",
                         "url": "https://www.theverge.com/2019/10/24/20930060/samsung-exynos-990-chipset-features-specs-performance-cameras-display",
                         "views": 20}
            }
    for article in news:
        n = NewsArticle.objects.get_or_create(title=news[article]["title"], description=news[article]["description"],
                                              picture=news[article]["picture"], url=news[article]["url"],
                                              views=news[article]["views"])[0]
        n.save()

    # Videos promoting joining tech
    videos = {"video1": {"title": "Careers in Tech: My name is Tess",
                         "description": "Meet Tess, a software engineer at Google.",
                         "url": "https://www.youtube.com/embed/RfbbDgx6l1g",
                         "views": 20},
              "video2": {"title": "Careers in Tech: My name is Kinsley",
                         "description": "Meet Kinsley, a software engineer at Facebook.",
                         "url": "https://www.youtube.com/embed/suJZ9z426P0",
                         "views": 20},
              "video3": {"title": "Careers in Tech: My name is Federico",
                         "description": "Meet Federico Gomez Suarez, a software engineer at Microsoft.",
                         "url": "https://www.youtube.com/embed/EUF2mad21jo",
                         "views": 20},
              "video4": {"title": "Careers in Tech: My name is Brina",
                         "description": "Meet Brina Lee, a software engineer at Instagram.",
                         "url": "https://www.youtube.com/embed/t0-Z_LfGwUM",
                         "views": 20},
              "video5": {"title": "Careers in Tech: My Name is Polina",
                         "description": "Meet Polina, a data scientist at Electronic Arts.",
                         "url": "https://www.youtube.com/embed/tTSEFaYjV30",
                         "views": 20},
              "video6": {"title": "What is the Internet?",
                         "description": "What is the internet?  Short answer: a distributed packet-switched network.",
                         "url": "https://www.youtube.com/embed/Dxcc6ycZ73M",
                         "views": 20},
              "video7": {"title": "The Internet: How Search Works",
                         "description": "Join John, Google's Chief of Search and AI, and Akshaya, from Microsoft Bing, to find out how search really works.",
                         "url": "https://www.youtube.com/embed/LVV_93mBfSU",
                         "views": 20},
              "video8": {"title": "The Internet: Encryption & Public Keys",
                         "description": "Mia Epner, who works on security for a US national intelligence agency, explains how cryptography allows for the secure transfer of data online. ",
                         "url": "https://www.youtube.com/embed/ZghMPWGXexs",
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
                                 "ethnicity": "Mixed",
                                 "position": "Software Developer"},
                  "rolemodel3": {
                      "title": "App developer and former Victoria's Secret model inspires Perth women in tech",
                      "description": "Lyndsey Scott has had a career as an internationally acclaimed model, working for brands such as Victoria's Secret and Gucci, but she has always had a burning passion for computer programming.",
                      "picture": "lyndseyscott.jpg",
                      "url": "https://www.brisbanetimes.com.au/national/western-australia/app-developer-and-former-victoria-s-secret-model-inspires-perth-women-in-tech-20191025-p534cb.html",
                      "gender": "Female",
                      "ethnicity": "Mixed",
                      "position": "Software Developer"},
                  "rolemodel4": {"title": "Susan Wojcicki",
                                 "description": "Susan Wojcicki grew up surrounded by Stem: her father was a physics professor at Stanford University and, as a child, she lived on campus with famous mathematicians as neighbours. She joined Google the year after it was founded and has been behind many of the search engine’s most defining features, including creating the first ever Google Doodle. She became head of YouTube last year, after it was bought by Google in 2006.",
                                 "picture": "susanwojcicki.jpeg",
                                 "url": "https://www.theguardian.com/guardian-professional/women-leadership-blog/gallery/2015/jun/22/10-of-the-best-female-role-models-in-tech-in-pictures",
                                 "gender": "Female",
                                 "ethnicity": "Mixed",
                                 "position": "Software Developer"},
                  "rolemodel5": {"title": "Belinda Parmar",
                                 "description": "One of the UK’s leading campaigners to get more women into tech, Belinda Parmar is the founder of Little Miss Geek and chief executive of Lady Geek. She was awarded an OBE for services to women in technology in 2014 following campaigns like Her In Hero which brought in support from senior politicians. She has explained her campaigning, saying: “Diversity is important in any industry, but is especially relevant when it comes to technology. Tech is the way that world talks to each other.”",
                                 "picture": "belindaparmar.jpeg",
                                 "url": "https://www.theguardian.com/guardian-professional/women-leadership-blog/gallery/2015/jun/22/10-of-the-best-female-role-models-in-tech-in-pictures",
                                 "gender": "Female",
                                 "ethnicity": "African",
                                 "position": "Software Developer"},
                  "rolemodel6": {"title": "Sheryl Sandberg",
                                 "description": "As chief operating officer of Facebook, Sheryl Sandberg is one of the world’s most high-profile women in the tech sector. After an economics degree and a stint at Google, she was hired by Facebook in 2008 and later became the first woman on the company’s board. She has also been a champion of gender equality – in her book about women in work, Lean In, she writes: “We stand on the shoulders of the women who came before us, women who had to fight for the rights that we now take for granted.”",
                                 "picture": "sherylsandberg.jpg",
                                 "url": "https://www.theguardian.com/guardian-professional/women-leadership-blog/gallery/2015/jun/22/10-of-the-best-female-role-models-in-tech-in-pictures",
                                 "gender": "Female",
                                 "ethnicity": "African",
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
    vpc = VisitedPagesCounter.objects.get_or_create(pk=0)[0]
    vpc.home_views = 0
    vpc.careers_views = 0
    vpc.contact_views = 0
    vpc.meet_your_hero_views = 0
    vpc.news_views = 0
    vpc.videos_views = 0
    vpc.play_views = 0
    vpc.save()


if __name__ == '__main__':
    print("Starting codeforgood population script..")
    populate()
