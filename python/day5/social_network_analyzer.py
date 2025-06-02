def social_network_analyzer():
    """
    Analyze a social network represented as friendships:
    1. Store friendship relationships - using what variable type?
    2. Find mutual friends between two people
    3. Suggest friends (friends of friends who aren't already friends)
    4. Find the most popular person (most connections)

    Input format:
    - First line: number of friendship pairs
    - Each line: two names representing a friendship

    Example input:
    6
    Alice Bob
    Alice Charlie
    Bob David
    Charlie David
    David Eve
    Eve Frank

    Expected operations:
    - Find mutual friends of Alice and David
    - Suggest friends for Alice
    - Find person with most friends
    """
    # the list of set
    relationship_dict = {}
    pair_list = []
    num_of_pairs = int(input("number of friendship pairs: "))
    for i in range(num_of_pairs):
        str_input_pair = input()
        pair_list.append(str_input_pair.strip().split())
    # print(pair_list)
    for pair in pair_list:
        # print(pair)
        relationship_dict.setdefault(pair[0], set()).add(pair[1])
        relationship_dict.setdefault(pair[1], set()).add(pair[0])

    mutual_friend_dict = {}
    keys = list(relationship_dict.keys())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            person1, person2 = keys[i], keys[j]
            mutual_friend = relationship_dict[person1] & relationship_dict[person2]
            if mutual_friend:
                mutual_friend_dict.setdefault((person1, person2), mutual_friend)

    # print(mutual_friend_dict)

    # 3.
    keys_list_relation = list(relationship_dict.keys())
    recommand_dict = {}
    for i in range(len(keys_list_relation)):
        current_person = keys_list_relation[i]
        friends_of_friends_real = set()
        for friend in relationship_dict[current_person]:
            # specific friend friendlist
            friends_of_friends = relationship_dict[friend]
            friends_of_friends_real.update(friends_of_friends)
        friends_of_friends_real.discard(current_person)
        recommand_set = friends_of_friends_real - relationship_dict[current_person]

        if recommand_set:
            recommand_dict.setdefault(current_person, set()).update(recommand_set)

    # 4. Find the most popular person (most connections)
    most_popular_person = max(relationship_dict.items(), key=lambda x: len(x[1]))

    print("=== SOCIAL NETWORK ANALYSIS ===")
    print(f"\n1. Friendship Network:")
    for person, friends in relationship_dict.items():
        print(f"   {person}: {friends}")

    print(f"\n2. Mutual Friends:")
    for (person1, person2), mutual in mutual_friend_dict.items():
        print(f"   {person1} & {person2}: {mutual}")

    print(f"\n3. Friend Recommendations:")
    for person, recommendations in recommand_dict.items():
        print(f"   {person}: {recommendations}")

    print(f"\n4. Most Popular Person:")
    print(f"   {most_popular_person[0]} with {len(most_popular_person[1])} friends: {most_popular_person[1]}")


social_network_analyzer()
