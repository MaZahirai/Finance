 Requirements

- Python 3.9
- matplotlib == 3.1.1
- numpy == 1.19.4
- pandas == 0.25.1
- scikit_learn == 0.21.3
- torch == 1.8.0


execute on command line 
py -3.9 -u main_informer.py --model informer --data XAUUSD_M15 --features S  --seq_len 96 --label_len 48 --pred_len 24 --e_layers 2 --d_layers 1 --attn prob --des 'Exp' --itr 5 --use_gpu True
