from probeinterface import get_probe
from probeinterface.wiring import wire_probe
from probeinterface.plotting import plot_probe

import matplotlib.pyplot as plt
import numpy as np

import pytest

def test_wire_probe():
    
    manufacturer = 'neuronexus'
    probe_name = 'A1x32-Poly3-10mm-50-177'
    probe = get_probe(manufacturer, probe_name)
    
    probe.wiring_to_device('H32>RDH')
    
    plot_probe(probe, with_channel_index=True)


if __name__ == '__main__':
    test_wire_probe()
    
    plt.show()
