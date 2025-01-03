import rustworkx as rx
from rustworkx.visualization import mpl_draw as draw_graph
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.converters import QuadraticProgramToQubo
from qiskit.quantum_info import SparsePauliOp
from qiskit.circuit.library import QAOAAnsatz
from qiskit_algorithms.optimizers import COBYLA
from qiskit.primitives import Estimator
from qiskit.primitives import Sampler
from qiskit_algorithms import QAOA
from qiskit_aer import Aer

graph = rx.PyGraph()
node_names = ["Chris", "James", "Charlie", "Samantha", "John"]

user_data = {}
for user in node_names:
    node_index = graph.add_node(user)
    user_data[user] = {"index": node_index, "friends": []}

for user in node_names:
    user_data[user]["messages"] = []

friends = [
    ("Chris", "Charlie"),
    ("Samantha", "John"),
    ("James", "John"),
    ("Charlie", "James"),
    ("Chris", "John"),
]

for user1, user2 in friends:
    user1_index = user_data[user1]["index"]
    user2_index = user_data[user2]["index"]

    if not graph.has_edge(user1_index, user2_index):
        graph.add_edge(user1_index, user2_index, 1.0)
        user_data[user1]["friends"].append(user2)
        user_data[user2]["friends"].append(user1)

admin_code = '0'

def add_user(name):
    if name in node_names:
        print(f"User '{name}' already exists!")
        return
    
    # Add the user to the graph
    node_index = graph.add_node(name)
    node_names.append(name)
    print(f"User '{name}' added successfully!")
    return node_index

def login_user(name):
    if name in node_names:
        print(f"Welcome back, {name}!")
        return True
    else:
        print(f"User '{name}' does not exist. Please create an account first.")
        return False

def add_friendship(user_name, friend_name):
    if user_name not in node_names or friend_name not in node_names:
        print(f"Both users must exist in the graph to create a friendship.")
        return
    
    user_index = user_data[user_name]["index"]
    friend_index = user_data[friend_name]["index"]

    if graph.has_edge(user_index, friend_index):
        print(f"'{user_name}' and '{friend_name}' are already friends!")
        return

    graph.add_edge(user_index, friend_index, 1.0)
    user_data[user_name]["friends"].append(friend_name)
    user_data[friend_name]["friends"].append(user_name)
    print(f"Friendship added between '{user_name}' and '{friend_name}'!")

def send_message(sender, receiver, message):
    if receiver not in node_names:
        print(f"User '{receiver}' does not exist!")
        return

    user_data[receiver]["messages"].append(f"From {sender}: {message}")

def view_messages(name):
    messages = user_data[name]["messages"]
    if messages:
        print(f"\n{name}'s Messages:")
        for msg in messages:
            print(f"- {msg}")
    else:
        print(f"\nYou have no messages.")

def qaoa_min_vertex_cover():
    qp = QuadraticProgram()

    for indx, name in enumerate(node_names):
        qp.binary_var(name=f"x_{indx}")

    qp.minimize(linear={f"x_{i}": 1 for i in range(len(node_names))})

    for u, v in graph.edge_list():
        qp.linear_constraint(linear={f"x_{u}": 1, f"x_{v}": 1}, sense='>=', rhs=1, name=f"edge_{u}_{v}")

    qubo_converter = QuadraticProgramToQubo()
    qubo = qubo_converter.convert(qp)

    backend = Aer.get_backend('aer_simulator_statevector')
    optimizer = COBYLA()

    sampler = Sampler()
    qaoa = QAOA(optimizer=optimizer, sampler=sampler, reps=2)

    meo = MinimumEigenOptimizer(qaoa)
    result = meo.solve(qubo)

    min_vertex_cover = [node_names[i] for i in range(len(node_names)) if result.x[i] == 1]

    print("\nMost Influential Accounts:", min_vertex_cover)
    print("Number of Influential Accounts:", result.fval)

    return min_vertex_cover

def admin_panel():
        while True:
            print("\nAdmin Panel:")
            print("1. See Most Influential Accounts")
            print("2. Send Message to User")
            print("3. Exit Admin Panel")
            choice = input("Choose an option: ")
            
            if choice == "1":

                qaoa_min_vertex_cover()

            elif choice == "2":

                receiver = input("Enter recipient's name: ")
                message = input("Enter your message: ")
                send_message("Admin", receiver, message)

            elif choice == "3":

                print("Exiting Admin Panel...")
                break

            else:

                print("Invalid choice! Please try again.")

print("Welcome to the social network graph!")
while True:
    print("\nMenu:")
    print("1. Add a new user")
    print("2. Login")
    print("3. Admin Panel")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":

        name = input("Enter the new user's name: ")
        add_user(name)

    elif choice == "2":

        name = input("Enter user name: ")

        if login_user(name):
            print(f"Logged in as {name}.")
            while True:
                print("\n1. Add a friend")
                print("2. Send a message to a friend")
                print("3. Send a message to all friends")
                print("4. View messages")
                print("5. Logout")
                sub_choice = input("Choose option: ")
                
                if sub_choice == "1":

                    friend_name = input("Enter friend's name: ")
                    add_friendship(name, friend_name)

                elif sub_choice == "2":

                    friend_name = input("Enter friend's name: ")

                    if friend_name in user_data[name]["friends"]:
                        message = input("Enter your message: ")
                        send_message(name, friend_name, message)
                    else:
                        print(f"{friend_name} isn't your friend!")

                elif sub_choice == "3":

                    message = input("Enter the message: ")
                    for friend in user_data[name]["friends"]:
                        user_data[friend]["messages"].append(f"From {name}: {message}")
                    print(f"Message sent to all friends!")


                elif sub_choice == "4":

                    view_messages(name)

                elif sub_choice == "5":

                    print(f"Logged out.")
                    break

                else:

                    print("Invalid choice! Please try again.")

    elif choice == "3":

        code = input("Enter admin login code: ")
        if code == admin_code:
            admin_panel()
        else:
            print("Incorrect admin code!")

    elif choice == "4":

        print("Exiting the program.")
        exit()

    else:

        print("Invalid choice! Please try again.")