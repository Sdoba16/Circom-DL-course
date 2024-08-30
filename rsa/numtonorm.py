import json

signature = 41221598203604396207904179361764910846452317904468256730587511496301851427121262796061175954223113696542077310748928363966903930879136190914203051330221700694524002661550197320997589062458310298450254828410616789537693484368833525794600589724738706424280571497409988883651471758345091192064409121489008085239
pubkey = 101033296424143946671973446865162996263494748727837572666022791892593902158428236164150382105844438383436324990679960206564209815556803195335701638444637046837498348091551051068794859349593922616106567084821758165667859307167433276589441423874469333460024274126878115431804473693383337837487939994514294221581

hui = 24486213345066591544654211573410221891694396565083916679084610715200748926922
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

def jsonify_and_save(signature, pubkey, hui, filename='inputs.json'):
    data = {
        "signature": bigint_to_array(64, 16, signature),
        "pubkey":    bigint_to_array(64, 16, pubkey),
        "message": bigint_to_array(64, 16, hui)
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
jsonify_and_save(signature, pubkey, hui)