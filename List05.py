def main(n1, n2):
    """
    You are given a list called numbers1 and numbers2.
    Delete the last item in the first list and add that deleted item to the beginning of the 
    second list.
    Merge the first list into the second and return.
    Args:
        numbers1(list): parameter
        numbers2(list): parameter
    Returns:
        list: return answer
    """
    x = n1.pop()
    n2.insert(0, x)
    n1.extend(n2)   
    return n1