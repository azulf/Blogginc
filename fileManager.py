import os 
import json

def save_article_json(article):
    data = {
        "id" : article['id'],
        "title" : article['title'],
        "content" : article['content'],
    }

    # simpan ke file per artikel
    os.makedirs('articles', exist_ok=True)
    with open(f'articles/{article["id"]}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def load_all_articles():
    articles = []
    for filename in os.listdir('articles'):
        if filename.endswith('.json'):
            with open(os.path.join('articles', filename), 'r', encoding='utf-8') as f:
                article = json.load(f)
                articles.append(article)
    return articles

def generate_id():
    # Generate ID for new article
    for i in range (1, 1000):
        if not os.path.exists(f'articles/{i}.json'):
            return i
        
def delete_article(article_id):
    try :
        os.remove(f'articles/{article_id}.json')
    except FileNotFoundError:
        print(f"File {article_id}.json not found.")