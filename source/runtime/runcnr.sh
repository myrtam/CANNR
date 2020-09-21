# Run cannR build
export PYTHONPATH=$PYTHONPATH:../base_image/cannr/lib
python3 runcnr.py $1 context.json

# Example:
# ./runcnr.sh ../examples/project1/project.json
