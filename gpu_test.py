import torch
# 检查基础信息
print("PyTorch版本:", torch.__version__)          # 应为 2.x+cu118 格式（含CUDA标识）
print("CUDA是否可用:", torch.cuda.is_available())  # 需返回 True
print("当前GPU设备:", torch.cuda.get_device_name(0))  # 显示显卡型号