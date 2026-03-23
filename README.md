# Spacial Score topological indicator of molecular complexity

This tool computes the Spatial Score (SPS) and its size-normalized variant (nSPS), two empirical descriptors of molecular spatial complexity that extend common measures like Fsp3 and FCstereo by capturing molecular topology and three-dimensionality at a granular scale. The normalized score enables comparison across molecules of different sizes and differentiates natural products from synthetic compounds. Analyses of ChEMBL data show trends of increasing potency and selectivity with higher nSPS values.

This model was incorporated on 2026-01-20.Last packaged on 2026-01-20.

## Information
### Identifiers
- **Ersilia Identifier:** `eos12x7`
- **Slug:** `spacial-score-complexity`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Descriptor`, `Synthetic accessibility`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `2`
- **Output Consistency:** `Fixed`
- **Interpretation:** Spacial score calculated by RdKIT

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| sps_score | integer | high | Complexity score based on spacial features of the molecule |
| nsps_score | float | high | Normalized spacial score |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos12x7](https://hub.docker.com/r/ersiliaos/eos12x7)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos12x7.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos12x7.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `502`
- **Image Size (Mb):** `454.83`

**Computational Performance (seconds):**
- 10 inputs: `27.98`
- 100 inputs: `17.9`
- 10000 inputs: `35.4`

### References
- **Source Code**: [https://github.com/frog2000/Spacial-Score](https://github.com/frog2000/Spacial-Score)
- **Publication**: [https://pubs.acs.org/doi/10.1021/acs.jmedchem.3c00689](https://pubs.acs.org/doi/10.1021/acs.jmedchem.3c00689)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2023`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [BSD-3-Clause](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos12x7
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos12x7
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
