import requests

print("=" * 60)
print("LAB 17: WORKING WITH APIS")
print("=" * 60)

# ============================================================
# PART 1: CONSUMING PUBLIC API
# ============================================================
print("\n1. CONSUMING PUBLIC API")
print("-" * 40)

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    print(f"Received {len(users)} users:")
    for user in users[:3]:
        print(f"  • {user['name']} - {user['email']}")
else:
    print(f"Error: {response.status_code}")

# ============================================================
# PART 2: API WITH PARAMETERS
# ============================================================
print("\n2. API WITH PARAMETERS")
print("-" * 40)

url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1, "_limit": 3}
response = requests.get(url, params=params)

print(f"URL: {response.url}")
if response.status_code == 200:
    posts = response.json()
    print(f"Found {len(posts)} posts for user 1:")
    for post in posts:
        print(f"  • {post['title'][:30]}...")

# ============================================================
# PART 3: LOCAL DATABASE
# ============================================================
print("\n3. LOCAL DATABASE")
print("-" * 40)

movies = [
    {"id": 1, "title": "Inception", "year": 2010, "director": "Nolan", "rating": 8.8},
    {"id": 2, "title": "The Matrix", "year": 1999, "director": "Wachowski", "rating": 8.7},
    {"id": 3, "title": "The Godfather", "year": 1972, "director": "Coppola", "rating": 9.2}
]

print("Movies database:")
for m in movies:
    print(f"  [{m['id']}] {m['title']} ({m['year']}) - {m['rating']}/10")

# ============================================================
# PART 4: API ENDPOINTS SIMULATION
# ============================================================
print("\n4. API ENDPOINTS SIMULATION")
print("-" * 40)

def get_movie(id):
    for m in movies:
        if m["id"] == id:
            return {"status": "ok", "data": m}
    return {"status": "error", "message": "Not found"}, 404

def filter_movies(director=None, min_rating=None):
    results = movies.copy()
    if director:
        results = [m for m in results if director.lower() in m["director"].lower()]
    if min_rating:
        results = [m for m in results if m["rating"] >= min_rating]
    return {"status": "ok", "count": len(results), "data": results}

print("▶ GET /movies/2")
result = get_movie(2)
if isinstance(result, tuple):
    print(f"  {result[0]['message']}")
else:
    print(f"  Found: {result['data']['title']}")

print("\n▶ GET /movies?director=nolan")
result = filter_movies(director="nolan")
print(f"  Found: {result['count']}")
for m in result['data']:
    print(f"    • {m['title']}")

print("\n▶ GET /movies?min_rating=9.0")
result = filter_movies(min_rating=9.0)
print(f"  Found: {result['count']}")
for m in result['data']:
    print(f"    • {m['title']} - {m['rating']}")

print("\n▶ GET /movies/99 (not found)")
result = get_movie(99)
if isinstance(result, tuple):
    print(f"  {result[0]['message']} (404)")

# ============================================================
# PART 5: POST REQUEST
# ============================================================
print("\n5. POST REQUEST")
print("-" * 40)

new_movie = {"title": "Interstellar", "year": 2014, "director": "Nolan", "rating": 8.6}
new_id = max([m["id"] for m in movies]) + 1
new_movie["id"] = new_id
movies.append(new_movie)
print(f"Added movie: {new_movie['title']} (ID: {new_id})")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("✓ GET requests with parameters")
print("✓ JSON response handling")
print("✓ Status codes (200, 404)")
print("✓ Local database")
print("✓ Data filtering")
print("✓ POST requests")

print("\n" + "=" * 60)
print("LAB WORK COMPLETED")
print("=" * 60)