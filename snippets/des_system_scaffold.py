
MyEventPayload = NamedTuple('myPayload', [('ent', int), ('info', str)])
MyEventTag = 'MyEvent'

def process(kwargs: SystemArgs):
    event_store: FilterStore = kwargs.get('EVENT_STORE', None)
    # Initialize other variables
    while True:
        # Activates process when event arrives
        ev = yield event_store.get(lambda e: e.type == MyEventTag)
        # Do stuff
        # ...
