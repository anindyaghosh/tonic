import numpy as np


def drop_event_numpy(events, drop_probability=0.5, random_drop_probability=False):
    """
    Randomly drops events with drop_probability.

    Arguments:
    - events - ndarray of shape [num_events, num_event_channels]
    - drop_probability - probability of dropping out event
    - random_drop_probability - randomize the dropout probability between 0 and drop_probability

    Returns:
    - events - returns events that were not dropped
    """
    if random_drop_probability is True:
        drop_probability *= np.random.rand()

    length = events.shape[0]  # find the number of events
    nDrop = int(drop_probability * length + 0.5)
    ind = np.random.randint(0, length, size=nDrop)
    return np.delete(events, ind, axis=0)
