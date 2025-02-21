from BTrees._OOBTree import OOBTree
import csv
import timeit
import random


filename = "/Users/gregorykucherkov/Documents/2024/IT/Tier_10_Design_Algorithms/topic_3/HW/task_2/csv/generated_items_data.csv"


def add_item_to_dict(filename):
    store = {}
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            store[row["ID"]] = {
                "name": row["Name"],
                "category": row["Category"],
                "price": row["Price"],
            }

    return store


# classic way to store ID's as keys
# def add_item_to_tree(filename):
#     ob_tree = OOBTree()
#     with open(filename, "r") as csvfile:
#         reader = csv.DictReader(csvfile)

#         for row in reader:
#             ob_tree.update(
#                 {
#                     row["ID"]: {
#                         "name": row["Name"],
#                         "category": row["Category"],
#                         "price": float(row["Price"]),
#                     }
#                 }
#             )

#     return ob_tree


# altrenative way to store prices as ID, in order to utilize BTree search
def add_item_to_tree(filename):
    ob_tree = OOBTree()
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            ob_tree.update(
                {
                    float(row["Price"]): {
                        "name": row["Name"],
                        "category": row["Category"],
                        "ID": row["ID"],
                    }
                }
            )

    return ob_tree


def range_query_dict(store, min_price, max_price):
    result = []
    for product_id, product in store.items():
        price = float(product["price"])

        if min_price <= price <= max_price:
            result.append(
                {
                    "ID": product_id,
                    "name": product["name"],
                    "category": product["category"],
                    "price": product["price"],
                }
            )
    return result


def range_query_tree(tree, min_price, max_price):
    result = []

    for product_id, product in tree.items(
        min_price, max_price
    ):  # we can make much faster search if store prices as id's

        result.append(
            {
                "ID": product["ID"],
                "name": product["name"],
                "category": product["category"],
                "price": product_id,
            }
        )
    return result


if __name__ == "__main__":
    dict_store = add_item_to_dict(filename)
    tree_store = add_item_to_tree(filename)

    min_price = random.randint(10, 200)
    max_price = random.randint(min_price, 500)

    dict_time = timeit.timeit(
        stmt=lambda: range_query_dict(dict_store, min_price, max_price),
        number=100,
    )
    print(f"Total range_query time for Dict: {dict_time:.8f} seconds")

    tree_time = timeit.timeit(
        stmt=lambda: range_query_tree(tree_store, min_price, max_price),
        number=100,
    )
    print(f"Total range_query time for OOBTree: {tree_time:.8f} seconds")

    """
    The output shows efficiency of BTree's, but only if utilize search by ID's, so, in order to use this feature, I make prices ID's, otherwise it even slower then dict's.
    With this implementation we can get the following results:

    Total range_query time for Dict: 1.39537279 seconds
    Total range_query time for OOBTree: 0.36236483 seconds

    The difference is significant.
    """
