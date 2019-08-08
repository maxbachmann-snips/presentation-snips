import io
import json

from snips_nlu import SnipsNLUEngine
#from snips_nlu.dataset.dataset import Dataset
from snips_nlu.default_configs import CONFIG_EN

engine = SnipsNLUEngine(config=CONFIG_EN)

#dataset = Dataset.from_yaml_files("en", ["dataset.yaml"]).json

with io.open("dataset.json") as f:
    dataset = json.load(f)

engine.fit(dataset)
print("Training finished")
parsing = engine.parse(u"Hey, lights on in the lounge !")
print(json.dumps(parsing, indent=2))
