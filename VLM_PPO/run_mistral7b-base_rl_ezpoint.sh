TOKENIZERS_PARALLELISM=false CUDA_VISIBLE_DEVICES="0" accelerate launch --config_file ./scripts/config_zero2.yaml --main_process_port 29380 ./main.py \
    --env-name gym_cards/EZPoints-v0 \
    --init-lr 1e-5 \
    --end-lr 1e-9 \
    --lr_max_steps 25 \
    --eval-num-per-episode 200 \
    --num-env-steps 15000 \
    --num-steps 1024 \
    --grad-accum-steps 128 \
    --max-new-tokens 256 \
    --thought-prob-coef 0.5 \
    --use-gae \
    --seed 1 \
    --temperature 0.2 \
    --ppo-epoch 4 \
    --mini-batch-size 1 \
    --model-path liuhaotian/llava-v1.6-mistral-7b \
    --use-lora \
    --train-vision all \
    # --q8
    # --wandb-project you_wandb_proj \
    # --wandb-run you_wandb_run \
    # --use-wandb \
    # --q4
    # --model-path //home/mmd/LLaVA/checkpoints/llava-ezpoint_7b-lora \
    # liuhaotian/llava-v1.5-7b   ,   liuhaotian/llava-v1.6-mistral-7b 
