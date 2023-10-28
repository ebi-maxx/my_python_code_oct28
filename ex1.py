print("*-- WELCOME MAXX CINEMAS--*")
print("**jailer-200, jawaan-300,dd-180**")

movie_name=input("enter your movie name:")

if movie_name=="jailer" or movie_name=="jawaan" or movie_name=="dd":
    print(f"{movie_name} -> movie tickets is available")
    if movie_name=="jailer":
        one_jailer_ticket=200
        how_many=int(input(f"how many {movie_name} movie ticket you want:"))
        total_price=one_jailer_ticket*how_many
        print(f"your total ticket price is {total_price}")

    elif movie_name=="jawaan":
        one_jawaan_ticket=300
        how_many=int(input(f"how many {movie_name} movie ticket you want:"))
        total_price=one_jawaan_ticket*how_many
        print(f"your total ticket price is{total_price}")

    elif movie_name=="dd":
        one_dd_ticket=300
        how_many=int(input(f"how many {movie_name} movie ticket you want:"))
        total_price=one_dd_ticket*how_many
        print(f"your total ticket price is{total_price}")


else:
   print(f"sorry your {movie_name} movie is not running")
