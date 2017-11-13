
import adsk.fusion


def component_histogram(c, hist):
    name = c.name
    if name not in hist:
        hist[name] = 0
    hist[name] += 1
