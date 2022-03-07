# pylint:disable=line-too-long                                 # Allows for longer line length inside a Parametrization
"""Copyright (c) 2022 VIKTOR B.V.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

VIKTOR B.V. PROVIDES THIS SOFTWARE ON AN "AS IS" BASIS, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from viktor.parametrization import NumberField
from viktor.parametrization import Parametrization
from viktor.parametrization import Step


class BridgeParametrization(Parametrization):
    """Defines the input fields in left-side of the web UI in the Sample entity (Editor)."""
    bridge_layout = Step("Defining bridge layout", views='visualize_bridge_layout')
    bridge_layout.width = NumberField("Width", default=20, suffix='m')
    bridge_layout.length = NumberField("Length", default=100, suffix='m')
    bridge_layout.height = NumberField("height", default=10, suffix='m')
    bridge_layout.deck_thickness = NumberField("Deck thickness", default=2, suffix='m')
    bridge_layout.support_amount = NumberField("Number of supports", default=1, suffix='m')

    bridge_foundations = Step("Defining bridge foundations", views='visualize_bridge_foundations')
    bridge_foundations.pile_length = NumberField("Pile length", default=10, suffix='m')
    bridge_foundations.pile_angle = NumberField("Pile angle", default=10, suffix='°')
    bridge_foundations.pile_thickness = NumberField("Pile width", default=2000, suffix='mm')
