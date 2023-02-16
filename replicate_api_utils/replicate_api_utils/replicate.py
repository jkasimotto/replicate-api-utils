import os
import replicate
import yaml


class ReplicateAPI:
    def __init__(self, model_name, version_id):
        self.model_name = model_name
        self.version_id = version_id
        self.model = self.get_model(self.model_name)
        self.version = self.get_model_version(self.version_id)
        self.params = self.get_params()

    def get_model(self, model_name):
        self.model = replicate.models.get(model_name)
        return self.model

    def get_model_version(self, version_id):
        self.version = self.model.versions.get(version_id)
        return self.version
    
    def get_params(self):
        # Read config.yaml file in model_dir
        config_file = os.path.join(self.model_dir, "config.yaml")
        with open(config_file, "r") as f:
            self.params = yaml.safe_load(f)
        return self.params
    
    def predict(self):
        return self.version.predict(**self.params)

    @property
    def model_dir(self):
        # Replicate stores models in a directory structure like:
        # <account>/<model-name>
        return self.model_name.replace("-", "_").split("/")[-1]
