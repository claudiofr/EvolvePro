from evolvepro.src.process import process_dataset

process_dataset(
    file_path="data/dms/activity/Source.xlsx",
    dataset_name="brenan",
    wt_fasta_path="data/dms/wt_fasta/brenan_WT.fasta",
    activity_column="DMS_SCH",
    cutoff_value=2.5,
    output_dir="output/dms",
    sheet_name="MAPK1",
    cutoff_rule="greater_than",
    cutoff_percentiles=[90, 95],
)
