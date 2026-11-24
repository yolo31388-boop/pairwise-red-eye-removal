# pairwise-red-eye-removal

## 领域

游戏、图形与多媒体

## 主题

红眼去除

## 说明

全分辨率检测、色度蒙版与保留高光。

初始状态下 `imaging/red_eye_removal.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
