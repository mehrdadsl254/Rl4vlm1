TOKENIZERS_PARALLELISM=false CUDA_VISIBLE_DEVICES="0" accelerate launch --config_file config_zero2.yaml --main_process_port 29380 /home/mmd/RL4VLM/RL4VLM/VLM_PPO/main_test.py \
    --env-name gym_cards/Points24-v0 \
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
    --model-path /home/mmd/LLaVA/checkpoints/llava-point24_7b-lora \
    --use-lora \
    --train-vision all \
    # --wandb-project you_wandb_proj \
    # --wandb-run you_wandb_run \
    # --use-wandb \
    # --q4
