print("=" * 50)
print("🤖 AI Entertainment Recommendation System")
print("=" * 50)

print("\nChoose your interest:")
print("1. Movies")
print("2. Books")
print("3. Music")

choice = input("\nEnter your choice (1-3): ")

if choice == "1":

    print("\nMovie Genres:")
    print("Action, Comedy, Romance, Horror")

    genre = input("Enter genre: ").lower()

    if genre == "action":
        print("\nRecommended Movies:")
        print("- John Wick")
        print("- Avengers")
        print("- Mad Max")

    elif genre == "comedy":
        print("\nRecommended Movies:")
        print("- 3 Idiots")
        print("- Hera Pheri")
        print("- Dhamaal")

    elif genre == "romance":
        print("\nRecommended Movies:")
        print("- Titanic")
        print("- DDLJ")
        print("- The Notebook")

    elif genre == "horror":
        print("\nRecommended Movies:")
        print("- Conjuring")
        print("- Insidious")
        print("- Annabelle")

    else:
        print("Genre not found!")

elif choice == "2":

    print("\nBook Categories:")
    print("Programming, AI, Fiction")

    category = input("Enter category: ").lower()

    if category == "programming":
        print("\nRecommended Books:")
        print("- Clean Code")
        print("- Python Crash Course")
        print("- Head First Java")

    elif category == "ai":
        print("\nRecommended Books:")
        print("- Artificial Intelligence")
        print("- Hands-On Machine Learning")
        print("- Deep Learning")

    elif category == "fiction":
        print("\nRecommended Books:")
        print("- Harry Potter")
        print("- The Alchemist")
        print("- The Hobbit")

    else:
        print("Category not found!")

elif choice == "3":

    print("\nMusic Types:")
    print("Pop, Romantic, Classical")

    music = input("Enter type: ").lower()

    if music == "pop":
        print("\nRecommended Songs:")
        print("- Blinding Lights")
        print("- Shape of You")
        print("- Levitating")

    elif music == "romantic":
        print("\nRecommended Songs:")
        print("- Tum Hi Ho")
        print("- Kesariya")
        print("- Raataan Lambiyan")

    elif music == "classical":
        print("\nRecommended Songs:")
        print("- Fur Elise")
        print("- Moonlight Sonata")
        print("- Canon in D")

    else:
        print("Type not found!")

else:
    print("Invalid Choice!")

print("\nThank you for using the Recommendation System!")