from pyAgrum import BayesNet
import pyAgrum as gum
import pyAgrum.lib.notebook as gnb
from IPython.display import Image
import pydotplus
from IPython.display import display
from ipywidgets import widgets, HBox, Layout

lyt = layout={'border-collapse': 'collapse', 'border-spacing': '0px'}

def display_bn(bn: BayesNet):
    return Image(pydotplus.graph_from_dot_data(bn.toDot()).create_png())


def display_tables(bn: BayesNet, row_length = -1):
    buffer = []
    if row_length != -1:
        for i, n in enumerate(bn.nodes()):
            buffer.append(n)
            if i % 3 == 0 and i != 0:
                display(HBox([widgets.HTML(gnb.getPotential(bn.cpt(node)), layout=lyt) for node in buffer]))
                buffer = []
    else:
        display(HBox([widgets.HTML(gnb.getPotential(bn.cpt(node)), layout=lyt) for node in bn.nodes()]))


BayesNet.display = display_bn
BayesNet.display_tables = display_tables