
class GroupsCreator(object):
    '''
    Collection of static methods to generate kids groups by age or mixed groups
    '''

    AGED_TYPE = 1
    MIXED_TYPE = 2

    @staticmethod
    def sort(participants):
        '''
        Sort a list of participants
        '''
        participants.sort(key=lambda participant: participant.dob, reverse=True)

    @staticmethod
    def by_age(participants, n_groups):
        '''
        Creates n_groups by age from the list of participants
        '''
        GroupsCreator.sort(participants)

        n_children = len(participants)/n_groups
        children_out = len(participants)%n_groups

        groups = []

        for index in range(n_groups):
            groups.append(participants[index*n_children:(index+1)*n_children])
        for j in range(children_out):
            groups[-1-j].append(participants[-1-j])
        return groups

    @staticmethod
    def mixed(participants, n_groups):
        '''
        Creates n_groups mixed groups from the list of participants
        '''
        GroupsCreator.sort(participants)
        n_children = len(participants)/n_groups
        children_out = len(participants)%n_groups
        groups = []
        for index in range(n_groups):
            groups.append([])
            for i in range(n_children):
                groups[index].append(participants[(i*n_groups)+ index])

        for j in range(children_out):
            groups[-1-j].append(participants[-1-j])

        return groups
