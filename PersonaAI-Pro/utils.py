# Example mapping for MCQ options

MCQ_MAP = {
    "calm": 1,
    "neutral": 2,
    "aggressive": 3,
    "analytical": 4,
    "emotional": 5
}

def convert_mcq_to_vector(answers):
    """
    answers: list of string MCQ responses
    returns: numeric vector
    """
    return [MCQ_MAP.get(ans, 0) for ans in answers]



