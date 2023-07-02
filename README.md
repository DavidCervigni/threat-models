# threat-models
threat models structured in YAML and report generation integration


## Generate the report using r3-threat-modeling-tool

**First time python tool installation**
```bash
#requires python and pip
pip install git+https://github.com/corda/threat-model-tool.git
```

**Generate the MD and HTML report from YAML threat model**

```bash
ROOT_YAML_PATH="OAuth 2.0/OAuth2.0.yaml"
BUILD_DIR="build"
ASSETS_PATH="OAuth 2.0/assets"
python -m r3threatmodeling.report_generator \
--rootTMYaml ${ROOT_YAML_PATH} \
--TMID OAuth2 \
--outputDir ${BUILD_DIR} \
--template TM_templateFull \
--assetDir ${ASSETS_PATH}
```

**Use BSYNC server to view the report on a browser**

```bash
cd $BUILD_DIR
sh bsync.sh 
```

## Example MD report

 - [OAuth 2.0](report-examples/OAuth%202.0%20build/OAuth2.md)
