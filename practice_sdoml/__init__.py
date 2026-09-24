"""
.. include:: ../README.md
"""

from practice_sdoml import plots
from practice_sdoml import modeling

from practice_sdoml.dataset import DiabetesDataset, get_dataloader
from practice_sdoml.modeling.model import SimpleNet
from practice_sdoml.modeling.train import train

__all__ = [
    "config",
    "dataset",
    "features",
    "plots",
    "modeling",
    "DiabetesDataset",
    "get_dataloader",
    "SimpleNet",
    "train",
]

__version__ = "0.1.0"
