import yaml
import pickle

YAML_FILE = "./resources/input.yaml"
PICKLE_FILE = "./resources/dict.pickle"


class SaveYaml(object):
    def __init__(self):
        pass

    def save_items(self):
        with open(YAML_FILE) as stream:
            try:
                doc = yaml.load_all(stream, Loader=yaml.FullLoader)
                pickle_out = open(PICKLE_FILE, "wb")
                for items in doc:
                    pickle.dump(items, pickle_out)
                pickle_out.close()
            except yaml.YAMLError as exc:
                print(exc)

    def load_yaml(self):
        pickle_in = open(PICKLE_FILE, "rb")
        yaml_dict = pickle.load(pickle_in)
        return yaml_dict





# pickle_in = open(PICKLE_FILE, "rb")
# example_dict = pickle.load(pickle_in)
# for key in example_dict.keys():
#     print(key, example_dict.get(key))
