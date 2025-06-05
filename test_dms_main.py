import sys
from scripts.dms.dms_main import main

sys.argv = [
    "dms_main.py",
    "--dataset_name",
    "brenan1",
    "--experiment_name",
    "esm2_8M_optimal",
    "--model_name",
    "esm2_t6_8M_UR50D",
    "--embeddings_path",
    "output/plm/esm",
    "--labels_path",
    "output/dms",
    "--num_simulations",
    # "10",
    "1",
    "--num_iterations",
    # "10",
    "3",
    "--measured_var",
    "activity",
    "--learning_strategies",
    "topn",
    "--num_mutants_per_round",
    "16",
    "--num_final_round_mutants",
    "16",
    "--first_round_strategies",
    "random",
    "--embedding_types",
    "embeddings",
    "--regression_types",
    "randomforest",
    "--embeddings_file_type",
    "csv",
    "--output_dir",
    "output/dms_results"
]

main()
