#!/usr/bin/python3
"""Module for handling API requests and data processing"""
import requests
import csv


def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print their titles"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """Fetch posts and save them to a CSV file"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        # Create a list of dictionaries with only required fields
        formatted_posts = [
            {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            for post in posts
        ]

        # Write to CSV file
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(formatted_posts)


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
