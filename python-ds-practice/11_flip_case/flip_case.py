def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    new_phrase = [] 
    for to_swap in phrase:
        if to_swap.isupper():
            new_phrase.append(to_swap.lower())
        elif to_swap.islower():
            new_phrase.append(to_swap.upper())
        else:
            new_phrase.append(to_swap)
    print ("".join(new_phrase))
