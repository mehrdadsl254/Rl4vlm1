# import sys
# sys.path.append("/home/mmd/RL4VLM/RL4VLM/LLaVA")
from llava.train.train import train

if __name__ == "__main__":
    train(attn_implementation="flash_attention_2")
