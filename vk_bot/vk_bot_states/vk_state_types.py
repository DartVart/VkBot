from enum import IntEnum


class VkStateTypes(IntEnum):
    INITIAL = 0
    WAITING_STATE = 1
    SELECT_UNIVERSITY_ONE_TIME_GETTING_NEWS = 2
    SELECT_TIME_FOR_ONE_TIME_GETTING_NEWS = 3
    SELECT_TOPIC_FOR_ONE_TIME_GETTING_NEWS = 4
    NEED_TO_SHOW_FOLLOWING_NEWS = 5
    ADD_TOPIC = 6
    SELECT_TIME_PERIOD = 7
    SELECT_TIME_OF_DAY = 8
    SELECT_DAY_OF_WEEK = 9
    SELECT_DAY_OF_MONTH = 10
    SUBSCRIPTION = 11
    UNSUBSCRIPTION = 12