# ...
from simulator.components.MyComponent import MyComponent
from simulator.components.MyOtherComponent import MyOtherComponent
# ...

class MySystem(esper.Processor):
    def __init__(self, args):
        super().__init__()
        # initialize system

    def process(self, kwargs: SystemArgs) -> None:
        # Iterate over components the system is interested in
        for ent, (my_comp, my_other_comp) in \
            self.world.get_components(MyComponent, MyOtherComponent):
            # Does stuff
            # ...
