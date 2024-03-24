#!usr/bin/env python3
"""
python3 makepyproject.py    
"""
import json
import os
import jinja2
import jjcli
from glob import glob

def main():    
    modes = glob("*.py")
    if len(modes) >= 1:
        name = modes[0].replace(".py","")
    else:
        name = input("Modulo?")

    version = jjcli.qx(f"grep __version__ '{name}'.py")
    if version == "":
        version = "0.0.1"

    
    metadata_path = str(os.path.expanduser("~/.METADATA.json"))
    file = open(metadata_path, 'r')
    data = json.load(file)
    autor = data["Username"]
    email = data["Email"]

    pp = jinja2.Template('''

    [build-system]
    requires = ["flit_core >=3.2,<4"]
    build-backend = "flit_core.buildapi"

    [project]
    name = "{{name}}"
    authors = [
        {name = "{{autor}}", email = "{{email}}"},
    ]
    version = "{{version}}"
    readme = "README.md"
    classifiers = [
        "License :: OSI Approved :: MIT License",
    ]
    requires-python = ">=3.8"
    dynamic = ["description"]

    dependencies = [
        "jjcli",
        "jinja2"
    ]

    [project.scripts]
    {{name}} = "{{name}}:main"

    ''')
    
    print(pp.render({"version":version,"name":name,"autor":autor,"email":email}))

    with open("pyproject.toml", "w") as out:
        out.write(pp.render({"version":version,"name":name,"autor":autor,"email":email}))

    print(out)


if __name__ == "__main__":
    main()