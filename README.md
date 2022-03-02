# Visualization SQripts

Extents the [QuTiP Framework](https://qutip.org/) by a more convenient wrapper which allows for adding vectors, drawing angles and squishing the sphere (coherent noise artefacts).

## Install

Install the requirements from 'requirements.txt'.

By now, there is an issue with matplotlib-3.5.x which is why matplotlib-3.4.3 is required.

## Usage

Either use the provided launch scripts or run
```bash
python circuit.py
python blochSphere.py
```
directly from the command line.

The output will be saved to the './out/' folder, which can be changed by providing a 'savePath' argument when instantiating the blochSphere class or when calling the saveDefault method.



*Please excuse any scetchy python code.. certain deadlines should be respected*