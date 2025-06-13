import requests
import csv

"""
fetching posts from JSONPlaceholder
"""


def fetch_and_print_posts():
    """using request.get() for the JSONplaceholder and try to fetch from posts"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    """if request is sueccfull, 200 will be printed"""
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        """if the request is successful, fetch the posts from JSONplaceholder"""

        posts = response.json()
        """iterating through the posts to print only the titles"""
        for post in posts:
            print(post["title"])

def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        """we want to extract json, so first turn the data to json
        using .json"""

        """reading the data, under the hood, it does json.loads(response.text)"""
        raw_data = response.json()
        """now, we are structuring a CSV file"""

        """opening CSV file"""
        with open("posts.csv", 'w', newline="") as csvf:
            my_file = csv.DictWriter(csvf, fieldnames=["id", "title", "body"], extrasaction='ignore' )
            my_file.writeheader()
            my_file.writerows(raw_data)
            """a different method for this method. which is to first structure
            the data that we need, (i.e id, title and body). we had to put
            (extrasaction='ignore') in the dictwriter argument to ignore
            other dicionary attributes. below is the alternatve solution 
                        
                        filtered = [
                { "id":  p["id"],
                "title":p["title"],
                "body": p["body"] }
                for p in raw
]
""" 
fetch_and_save_posts()

        
        
