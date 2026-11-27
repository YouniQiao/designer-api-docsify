# pickForResult

## 导入模块

```TypeScript
import { colorPickerController, PickedColorInfo } from '@kit.ArkUI';
```

## pickForResult

```TypeScript
function pickForResult(x?: number, y?: number, showValue?: boolean): Promise<PickedColorInfo>
```

全局取色，支持SDR和HDR格式。屏幕上在指定初始位置出现取色环，并跟随用户手指或手写笔移动。当用户抬起手指或手写笔时，返回最后一次指向位置的颜色值。使用Promise异步回调。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-colorPickerController-function pickForResult(x?: number, y?: number, showValue?: boolean): Promise<PickedColorInfo>--><!--Device-colorPickerController-function pickForResult(x?: number, y?: number, showValue?: boolean): Promise<PickedColorInfo>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 否 | 颜色拾取器的初始x轴坐标。取值范围：0~屏幕的实际宽度，取值超出上限取屏幕的实际宽度。<br>单位为：像素（px）。默认值：100。 |
| y | number | 否 | 取色器初始位置的y轴坐标。取值范围：0~屏幕的实际高度，取值超出上限取屏幕的实际高度。<br>单位为：像素（px）。默认值：100。 |
| showValue | boolean | 否 | 是否显示RGB值。true：显示RGB值，false：不显示RGB值。<br>默认值：默认值：false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[PickedColorInfo](arkts-arkui-arkui-colorpickercontroller-pickedcolorinfo-i.md)&gt; | Promise对象，返回取色执行的结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [801](../../errorcode-universal.md#801-api功能在部分设备不支持) | Capability not supported on current device. |
