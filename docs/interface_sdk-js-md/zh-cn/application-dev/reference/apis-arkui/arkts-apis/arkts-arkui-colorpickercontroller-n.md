# colorPickerController

```TypeScript
declare namespace colorPickerController
```

**colorPickerController**模块提供全局取色能力。应用程序调用[pickForResult](arkts-arkui-colorpickercontroller-pickforresult-f.md)启动取色流程后，屏幕上在指定初始位置出现取色环，并跟随用户手指或手写笔移动。当用户抬起手指或手写笔时，返回最后一次指向位置的颜色值。

本接口同时支持SDR和HDR色彩格式。当取色像素为HDR内容时，返回的[brightness](arkts-arkui-arkui-colorpickercontroller-pickedcolorinfo-i.md#brightness)可用。

> **说明：** 
> 
> -仅支持触摸屏/手写笔设备。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace colorPickerController--><!--Device-unnamed-declare namespace colorPickerController-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { colorPickerController, PickedColorInfo } from '@kit.ArkUI';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [pickForResult](arkts-arkui-colorpickercontroller-pickforresult-f.md#pickforresult-1) | 全局取色，支持SDR和HDR格式。屏幕上在指定初始位置出现取色环，并跟随用户手指或手写笔移动。当用户抬起手指或手写笔时，返回最后一次指向位置的颜色值。使用Promise异步回调。 |
