from omegaconf import DictConfig, OmegaConf
import hydra
import mlflow
@hydra.main(version_base=None, config_path="/home/user2/hydra-mlflow/hydra-mlflow/config/", config_name="config")
def my_app(cfg):
    mlflow.start_run()
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_artifact("./config/config.yaml")
    mlflow.end_run()  
    print(OmegaConf.to_yaml(cfg))

if __name__ == "__main__":
    my_app()