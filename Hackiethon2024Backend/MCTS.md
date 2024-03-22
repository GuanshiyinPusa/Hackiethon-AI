# MCTS -- Markov Chain Tree Search

## Integration with Game Logic
- State presentation: state of the player and enemy
- Action presentation: action of the player and enemy
- Simulations: simulate the game to the end
- Reward: reward of the player and enemy

```
def MCTS(root_state):
    root_node = Node(state=root_state)

    for _ in range(number_of_iterations):
        node = root_node
        state = deepcopy(root_state)

        # Selection
        while node.children:
            node = node.select_child()
            state.perform_action(node.action)

        # Expansion
        if not state.is_terminal():
            actions = state.available_actions()
            for action in actions:
                new_state = deepcopy(state)
                new_state.perform_action(action)
                node.add_child(action=action, state=new_state)

        # Simulation
        simulation_state = deepcopy(state)
        while not simulation_state.is_terminal():
            simulation_action = choose_random(simulation_state.available_actions())
            simulation_state.perform_action(simulation_action)

        # Backpropagation
        while node is not None:
            node.update(simulation_state.get_reward())
            node = node.parent

    # Choose the best action
    best_child = root_node.get_best_child()
    return best_child.action

class Node:
    def __init__(self, action=None, parent=None, state=None):
        self.action = action
        self.parent = parent
        self.children = []
        self.wins = 0
        self.visits = 0
        self.state = state

    def select_child(self):
        # Select a child node using a strategy like UCB1
        pass

    def add_child(self, action, state):
        # Add a new child node for the given action and state
        pass

    def update(self, reward):
        # Update this node's data with the simulation's result
        pass

    def get_best_child(self):
        # Return the child with the best performance
        pass

def choose_random(actions):
    # Randomly choose an action from the available ones
    pass

```
