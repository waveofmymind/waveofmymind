import feedparser

blog_rss_url = "https://waveofmymind.github.io/feed.xml"
rss_feed = feedparser.parse(blog_rss_url)

MAX_POST_NUM = 5

latest_blog_post_list = "## 📄 Blog <br>\n"

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"- [{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"

markdown_text = """

### 🌊 waveofmymind
> 

- I am currently working on **a variety of problems and solving them**.

  - 👀 studying - Kotlin, Spring Boot
  - 🎯 focusing - Event Driven Architecture with Kafka, k8s
<!--   - enjoyed learning - Spring Boot -->
---


![Kotlin](https://img.shields.io/badge/Kotlin-B75EA4?style=for-the-badge&logo=kotlin&logoColor=F6891F)
![Java](https://img.shields.io/badge/JAVA-007396?style=for-the-badge&logo=java&logoColor=white)

![Spring](https://img.shields.io/badge/Spring-6DB33F?style=for-the-badge&logo=spring&logoColor=white)

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=fff) ![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white)

![Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)

![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=waveofmymind&show_icons=true&theme=dark)

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fwaveofmymind&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w') as f:
    f.write(readme_text)
