import hashlib
import json
import os

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update((str(self.index) + 
                   str(self.timestamp) + 
                   str(self.data) + 
                   str(self.previous_hash)).encode())
        return sha.hexdigest()
    
def create_genesis_block():
    return Block(0, "01/01/2017", "Genesis Block", "0")

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = "some_timestamp"
    this_data = "some_data"
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

num_of_blocks_to_add = 20

for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print("Block #{} has been added to the blockchain!".format(block_to_add.index))
    print("Hash: {}\n".format(block_to_add.hash))

class CLI:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        
    def display_menu(self):
        print("1. Add new image to blockchain")
        print("2. Display blockchain")
        print("3. Validate blockchain")
        print("4. Exit")
        
    def add_image(self):
        image_path = input("Enter the path of the image: ")
        if os.path.isfile(image_path):
            self.blockchain.add_block(image_path)
            print("Image added to blockchain")
        else:
            print("Invalid image path")
        
    def display_blockchain(self):
        for i, block in enumerate(self.blockchain.chain):
            print("Block {}".format(i))
            print("Timestamp: {}".format(block.timestamp))
            print("Image: {}".format(block.image))
            print("Hash: {}".format(block.hash))
            print("Previous Hash: {}".format(block.previous_hash))
            print()
            
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_image()
            elif choice == "2":
                self.display_blockchain()
            elif choice == "3":
                if self.blockchain.is_valid():
                    print("Blockchain is valid")
                else:
                    print("Blockchain is invalid")
            elif choice == "4":
                break
            else:
                print("Invalid choice")

# Test the CLI
bc = Blockchain()
cli = CLI(bc)
cli.run()
