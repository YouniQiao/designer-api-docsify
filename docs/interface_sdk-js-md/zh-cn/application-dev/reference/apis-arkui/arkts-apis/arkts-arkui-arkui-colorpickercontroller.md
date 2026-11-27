# @ohos.arkui.colorPickerController

**colorPickerController**模块提供全局取色能力。应用程序调用[pickForResult](arkts-arkui-colorpickercontroller-pickforresult-f.md)启动取色流程后，屏幕上在指定初始位置出现取色环，并跟随用户手指或手写笔移动。当用户抬起手指或手写笔时，返回最后一次指向位置的颜色值。

本接口同时支持SDR和HDR色彩格式。当取色像素为HDR内容时，返回的[brightness](arkts-arkui-arkui-colorpickercontroller-pickedcolorinfo-i.md#brightness)可用。

> **说明：** 
> 
> -仅支持触摸屏/手写笔设备。

## 导入模块

```TypeScript
import { colorPickerController, PickedColorInfo } from '@kit.ArkUI';
```

## 汇总

### 命名空间

| 名称 | 说明 |
| --- | --- |
| [colorPickerController](arkts-arkui-colorpickercontroller-n.md) | **colorPickerController**模块提供全局取色能力。应用程序调用[pickForResult](arkts-arkui-colorpickercontroller-pickforresult-f.md)启动取色流程后，屏幕上在指定初始位置出现取色环，并跟随用户手指或手写笔移动。当用户抬起手指或手写笔时，返回最后一次指向位置的颜色值。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [PickedColorInfo](arkts-arkui-arkui-colorpickercontroller-pickedcolorinfo-i.md) | 全局取色结果对象，包含取色的基本信息。 |
