"""Smoke tests to verify environment."""
import pytest

def test_pytorch_available():
    import torch
    assert torch.__version__

def test_numpy_available():
    import numpy as np
    assert np.__version__

def test_basic_tensor():
    import torch
    x = torch.randn(2, 3)
    assert x.shape == (2, 3)
