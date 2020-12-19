from enum import Enum
class HeaderCodes(Enum):
    """
    Defines the various header values that we expect. If we get something that's not one of these
    then we have a problem.
    """
    STATS_BLOCK = 1
    HEADER = 4
    HEADER_W_ETS = 6
    HEADER_W_ESUM = 8
    HEADER_W_ESUM_ETS = 10
    HEADER_W_QDC = 12
    HEADER_W_QDC_ETS = 14
    HEADER_W_ESUM_QDC = 16
    HEADER_W_ESUM_QDC_ETS = 18


for x in [code for code in HeaderCodes if "ESUM" in code.name]:
    print(x)