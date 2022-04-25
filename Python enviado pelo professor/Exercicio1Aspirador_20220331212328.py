import UninformedSearch_20220324212440
import enum

class Positions(enum.Enum):
    ROOM1 = 'room1'
    ROOM2 = 'room2'
    ROOM3 = 'room3'

class States(enum.Enum):
        DIRTY = 'dirty'
        CLEAN = 'clean'

class Actions(enum.Enum):
    GOTOROOM1 = 'go-to-room-1'
    GOTOROOM2 = 'go-to-room-2'
    GOTOROOM3 = 'go-to-room-3'
    CLEAR = 'clear-room'


class VacuumCleanerWorld:
    def __init__(self, vacuumPosition, room1State, room2State, room3State):
        self.vacuumPosition = vacuumPosition
        self.room1State = room1State
        self.room2State = room2State
        self.room3State = room3State

    def getActions(self):
        lists = []

        if self.vacuumPosition == Positions.ROOM1:
            if self.room1State == States.DIRTY:
                lists.append(Actions.CLEAR)

            lists.append(Actions.GOTOROOM2)

        elif self.vacuumPosition == Positions.ROOM2:
            if self.room2State == States.DIRTY:
                lists.append(Actions.CLEAR)
            
            lists.append(Actions.GOTOROOM1)
            lists.append(Actions.GOTOROOM3)

        else:
            if self.room3State == States.DIRTY:
                lists.append(Actions.CLEAR)

            lists.append(Actions.GOTOROOM2)

        return lists

    def doAction(self, action):
        state = self.clone()

        if action == Actions.GOTOROOM1:
            state.vacuumPosition = Positions.ROOM1
        elif action == Actions.GOTOROOM2:
            state.vacuumPosition = Positions.ROOM2
        elif action == Actions.GOTOROOM3:
            state.vacuumPosition = Positions.ROOM3
        elif action == Actions.CLEAR:
            if self.vacuumPosition == Positions.ROOM1:
                state.room1State = States.CLEAN
            elif self.vacuumPosition == Positions.ROOM2:
                state.room2State = States.CLEAN
            else:
                state.room3State = States.CLEAN

        return state

    def equals(self, o):
        return o.vacuumPosition == self.vacuumPosition and o.room1State == self.room1State and o.room2State == self.room2State and o.room3State == self.room3State

    def clone(self):
        return VacuumCleanerWorld(
            self.vacuumPosition,
            self.room1State,
            self.room2State,
            self.room3State
        )

    def toString(self):
        return [f'{self.vacuumPosition}', f'{self.room1State}', f'{self.room2State}', f'{self.room3State}']

initial = VacuumCleanerWorld(Positions.ROOM1, States.DIRTY, States.DIRTY, States.DIRTY)
finals = [
    VacuumCleanerWorld(Positions.ROOM1, States.CLEAN, States.CLEAN, States.CLEAN),
    VacuumCleanerWorld(Positions.ROOM2, States.CLEAN, States.CLEAN, States.CLEAN),
    VacuumCleanerWorld(Positions.ROOM3, States.CLEAN, States.CLEAN, States.CLEAN)
]

problem = UninformedSearch_20220324212440.UninformedSearch(initial, finals)
result = problem.search()

if result:
    for res in result:
        print(res)