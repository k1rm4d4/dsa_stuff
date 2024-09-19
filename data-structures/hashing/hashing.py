def hash_remainder(item_value: int, table_size: int) -> int:
    hash_value = item_value % table_size
    return hash_value


# hashing realted fn:
def mid_square(num):
    sq = num**2
    sqstr = str(sq)
    mid_n = len(sqstr) // 2
    # print(sq, " mid n: ", mid_n)
    # print(sqstr[mid_n - 1 : mid_n + 1])
    return int(sqstr[mid_n - 1 : mid_n + 1])


def hash_str(word, table_size):
    """Return remainder of sum of string char value divided by table_size

    :param word: _description_
    :type word: _type_
    :param table_size: _description_
    :type table_size: _type_
    :return: _description_
    :rtype: _type_
    """
    str_sum = 0
    for c in word:
        str_sum += ord(c)
    print(str_sum)
    return str_sum % table_size


def hash_str_weighted(word, table_size):
    """Return remainder of sum of weighted string char value divided by table_size

        sum += ord(char) * pos of char from left

    :param word: _description_
    :type word: _type_
    :param table_size: _description_
    :type table_size: _type_
    :return: _description_
    :rtype: _type_
    """
    str_sum = 0
    weight = 1
    for c in word:
        str_sum += ord(c) * weight
        weight += 1
    print(str_sum)
    return str_sum % table_size


# collision resolution
def open_addr():
    pass


def get_hasht_linear_probing(num_list, table_size):
    table_hash = [None for _ in range(table_size)]
    
    for n in num_list:
        idx = n % table_size
        org_hash = idx
        while table_hash[idx] is not None:
            idx += 1
        print(n, " hash:: ", org_hash, " idx:: ", idx)
        table_hash[idx] = n
    return table_hash



# util
def load_factor(hash_table):
    size = len(hash_table)
    occupy_count = 0
    for item in hash_table:
        if item is not None:
            occupy_count += 1
    if size != 0:
        return occupy_count / size


# hasht = [None for _ in range(20)]
# for n in range(20):
#     if n % 7 == 0:
#         hasht[n] = n


if __name__ == "__main__":
    # print(hasht)
    # print(load_factor(hasht))
    # mid_square(234)
    print(hash_str("apple", 9))
    print(hash_str_weighted("apple", 9))
    print(get_hasht_linear_probing([113, 117, 97, 100, 114, 108, 116, 105, 99], 11))
