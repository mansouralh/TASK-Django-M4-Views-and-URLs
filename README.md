# Task

We will be displaying our shiny new pokemons on our website!

## Setup

1. Fork and clone [this repository](https://github.com/JoinCODED/TASK-Django-M4-Views-and-URLs).
2. Create a `virtual environment`, and activate it.
3. Install the requirements using `pip install -r dev-requirements.txt`.
4. Run migrations using `python manage.py migrate`.
5. Create an admin user using `python manage createsuperuser`.
6. Run the server using `python manage.py runserver`.
7. Go to the admin panel and create several pokemons.

## Detail View

1. Go to `views.py`, and create a detail view for your pokemons.
   - Call the function `get_pokemon`.
   - The function will receive a `request`, a `pokemon_id`, and return an `HttpResponse`.
   - The function should use the `pokemon_id` received from the parameters to fetch the `Pokemon` from the database.
   - The `HttpResponse` should contain a [multi-line](https://www.programiz.com/python-programming/examples/multiline-string) string, that is also an [f-string](https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python), which displays the details of our pokemon.
2. Go to `urls.py` and create a path for our pokemon detail view.
   - Import our `get_pokemon` view.
   - Add a `path` that is starts with `/pokemons` and contains an id in its path
3. Go to `/pokemons/YOUR_ID` and verify that you can see your pokemon.
4. Commit and push your code.
