# codex-test

## STM32 + 探針量測 PCB 銅箔厚度

這個 repo 包含一份可落地的系統開發指南（繁體中文）與厚度計算工具：

- 系統指南：`docs/stm32_pcb_copper_thickness_system_guide_zh-TW.md`
- 商用化產品藍圖：`docs/stm32_copper_thickness_product_blueprint_zh-TW.md`
- 計算工具：`tools/copper_thickness_calc.py`
- 測試：`tests/test_copper_thickness_calc.py`
- 完整流程章節：`docs/stm32_pcb_copper_thickness_system_guide_zh-TW.md` 的「## 11. 完整系統架構流程」

## 在 STM32 上可以用 Python 嗎？

- 可以用 **MicroPython/CircuitPython** 做原型。  
- 但若是高精度量測（毫歐級電阻 + ADC + 定時採樣），正式版通常建議使用 **STM32 HAL/C**。  
- 建議分工：STM32 端跑 C 做即時量測，PC 端跑 Python 做校正與資料分析。
