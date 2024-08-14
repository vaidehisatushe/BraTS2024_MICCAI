"""MLCube handler file"""
import typer
from generate_segmentation_infer import infer as infer_mri

app = typer.Typer()


@app.command("infer")
def infer(
    data_path: str = typer.Option(..., "--data_path"),
    parameters_file: str = typer.Option(None, "--parameters_file"),
    output_path: str = typer.Option(..., "--output_path"),
    # Provide additional parameters as described in the mlcube.yaml file
    # e.g. model weights:
    weights: str = typer.Option(..., "--additional_files/brain_segmentation_model.h5"),
):
    # Modify the infer command as needed
    infer_mri(data_path, output_path)


@app.command("hotfix")
def hotfix():
    # NOOP command for typer to behave correctly. DO NOT REMOVE OR MODIFY
    pass


if __name__ == "__main__":
    app()
   