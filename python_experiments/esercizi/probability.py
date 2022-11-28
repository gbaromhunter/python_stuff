sample_space = {'Heads', 'Tails'}
probability_heads = 1 / len(sample_space)


def is_heads_or_tails(outcome): return outcome in {'Heads', 'Tails'}


def is_neither(outcome): return not is_heads_or_tails(outcome)


def is_heads(outcome): return outcome == 'Heads'


def is_tails(outcome): return outcome == 'Tails'


def get_matching_event(event_condition, sample_space):
    return set([outcome for outcome in sample_space
                if event_condition(outcome)])


event_conditions = [is_heads_or_tails, is_heads, is_tails, is_neither]
for event_condition in event_conditions:
    print(f"Event Condition: {event_condition.__name__}")
    event = get_matching_event(event_condition, sample_space)
    print(f'Event: {event}\n')


def compute_probability(event_condition, generic_sample_space):
    event = get_matching_event(event_condition, generic_sample_space)
    return len(event) / len(generic_sample_space)


weighted_sample_space = {'Heads': 4, 'Tails': 2}

sample_space_size = sum(weighted_sample_space.values())

event = get_matching_event(is_heads_or_tails, weighted_sample_space)
event_size = sum(weighted_sample_space[outcome] for outcome in event)


def compute_event_probability(event_condition, generic_sample_space):
    event = get_matching_event(event_condition, generic_sample_space)
    if type(generic_sample_space) == type(set()):
        return len(event) / len(generic_sample_space)
    event_size = sum(generic_sample_space[outcome]
                     for outcome in event)
    return event_size / sum(generic_sample_space.values())


possible_children = ['Boy', 'Girl']
sample_space = set()
for child1 in possible_children:
    for child2 in possible_children:
        for child3 in possible_children:
            for child4 in possible_children:
                outcome = (child1, child2, child3, child4)
    sample_space.add(outcome)

from itertools import product

all_combinations = product(*(4 * [possible_children]))

sample_space_efficient = set(product(possible_children, repeat=4))


def has_two_boys(outcome): return len([child for child in outcome
                                       if child == 'Boy']) == 2


prob = compute_event_probability(has_two_boys, sample_space_efficient)
print(f"Probability of 2 boys is {prob}")
