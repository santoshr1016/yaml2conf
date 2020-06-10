import yaml
import pickle


def save_items(items):
    pickle_out = open("dict.pickle", "wb")
    pickle.dump(items, pickle_out)
    pickle_out.close()


with open('input.yaml') as stream:
    try:
        doc = yaml.load_all(stream, Loader=yaml.FullLoader)
        for items in doc:
            save_items(items)
    except yaml.YAMLError as exc:
        print(exc)


pickle_in = open("dict.pickle", "rb")
example_dict = pickle.load(pickle_in)
for key in example_dict.keys():
    print(key, example_dict.get(key))
