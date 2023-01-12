import concurrent.futures
import requests_cache
import time
from collections import Counter
from flask import Flask, request, render_template
import recipe_scrapers

app = Flask(__name__)

# Creating cache for the requests
# Setting expire_after to None will store the cache indefinitely
# unless it is manually deleted
requests_cache.install_cache("recipe_cache", expire_after=None)

# Delay time in seconds between requests
DELAY_TIME = 1

def scrape_recipe(ingredient):
    scraper = recipe_scrapers.scrape_me("http://www.food.com/search?q="+ingredient)
    if scraper is not None:
        title = scraper.title()
        ingredients = scraper.ingredients()
        rating = scraper.rating()
        total_time = scraper.total_time()
        review_count = scraper.review_count()
        time.sleep(DELAY_TIME)
        return (title, ingredients, rating, total_time, review_count)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ingredients = request.form["ingredients"]
        ingredients_list = ingredients.strip().split(",")
        if not ingredients_list or ingredients_list[0] == "":
            return render_template("index.html", error="Please enter valid ingredients")

        # Create a thread pool with `concurrent.futures.ThreadPoolExecutor()`
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Use the `executor.map()` function to execute the `scrape_recipe()` function for each ingredient concurrently
            recipe_options = list(executor.map(scrape_recipe, ingredients_list))

        recipe_options = sorted(recipe_options, key=lambda x: (len(set(ingredients_list).intersection(set(x[1])) , x[2], x[3], x[4])),)
        return render_template("result.html", recipe_options=recipe_options)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
