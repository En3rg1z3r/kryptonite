# Python program to create Blockchain
import json,os,hashlib,flask
global block;block={}

def block_chain_file():
    with open ("block_chain","r") as f:
        return (json.load(f))

#proof= nounce ! 

    

def create_block(LastName,FirstName,University,Degree,Date,proof,previous_hash):
    global block
    
    with open ("block_chain","r") as f:
        tmpdata2=json.load(f)
        print(len(tmpdata2["blockchain"]))
    
    block= {
    "index":len(tmpdata2["blockchain"]),  
    "Last Name" : LastName,
    "First Name" : FirstName ,
    "University" :University,
    "Degree" : Degree ,
    "Date Conferred" : Date,
    "proof":proof,
    "previous_hash":previous_hash
    }

   

def previous_block():
    chain=block_chain_file()
    return chain["blockchain"][-1]

def hash(block):
    encoded_block = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(encoded_block).hexdigest()



def proof_of_work(previous_proof):
    new_proof = 1
    check_proof = False
         
    while check_proof is False:
        hash_operation = hashlib.sha256(
        str(new_proof**2 - previous_proof**2).encode()).hexdigest()
        if hash_operation[:5] == '00000':
            check_proof = True
        else:
            new_proof += 1
                 
    return new_proof


def chain_valid(chain):
    previous_block = chain[0]
    block_index = 1
    
    #parcourir la liste des blocks
    while block_index < len(chain):
        block = chain[block_index]
        #verifier si le hash du block precedent est different du hash li raho fel bloc 
        if block['previous_hash'] != hash(previous_block):
             return False

        #2eme verification : par rapport l nounce    

        previous_proof = previous_block['proof']
        proof = block['proof'] 
        hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()).hexdigest()
             
        if hash_operation[:5] != '00000':
                return False
        previous_block = block
        block_index += 1
         
        return True
 
def previous_proof():
    prev_block=previous_block()
    return prev_block["proof"]

#miner click button to mine
def mine():
    print("ok")
    block["proof"]=proof_of_work(previous_proof())
    block["previous_hash"]=hash(previous_block())
    
    chain=block_chain_file()
    chain["blockchain"].append(block)

    with open ("block_chain","w") as f:
        json.dump(chain,f,indent=4)




