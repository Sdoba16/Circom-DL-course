import json
import sys
from hashlib import sha3_256

signature = 0x8a39bcd56fc065b517e801beeaefa259cc857546ec568fd4b7982a1f7dc2a07e91df8d865b226868a6951f74e1c1310fa093a7bb242cdfb48ac5251ea349f43c
R = 108607064596551879580190606910245687803607295064141551927605737287325610911759
S = 73791001770378044883749956175832052998232581925633570497458784569540878807131
pubkeyX = 33886286099813419182054595252042348742146950914608322024530631065951421850289
pubkeyY = 9529752953487881233694078263953407116222499632359298014255097182349749987176
hui = 103318048148376957923607078689899464500752411597387986125144636642406244063093
def bigint_to_array(n, k, x):
    # Initialize mod to 1 (Python's int can handle arbitrarily large numbers)
    mod = 1
    for idx in range(n):
        mod *= 2

    # Initialize the return list
    ret = []
    x_temp = x
    for idx in range(k):
        # Append x_temp mod mod to the list
        ret.append(str(x_temp % mod))
        # Divide x_temp by mod for the next iteration
        x_temp //= mod  # Use integer division in Python

    return ret

def jsonify_and_save(R, S, pubkeyX, pubkeyY, hui, filename='inputs.json'):
    data = {
        "R": bigint_to_array(64, 4, R),
        "S": bigint_to_array(64, 4, S),
        "PubKey":    [bigint_to_array(64, 4, pubkeyX), bigint_to_array(64, 4, pubkeyY)],
        "msghash": bigint_to_array(64, 4, hui)
    }
    
    # Convert the data to a JSON string
    json_data = json.dumps(data, indent=2)
    
    # Save the JSON string to a file
    with open(filename, 'w') as f:
        f.write(json_data)

    print(f'Data has been saved to {filename}')
#print(bigint_to_array(64, 32, signature),)
#print(bigint_to_array(64, 32, pubkey))
#print(bigint_to_array(64, 32, pubkey))
jsonify_and_save(R, S, pubkeyX, pubkeyY, hui)
message="hui"

if (len(sys.argv)>1):
        message=str(sys.argv[1])
print(message.encode())