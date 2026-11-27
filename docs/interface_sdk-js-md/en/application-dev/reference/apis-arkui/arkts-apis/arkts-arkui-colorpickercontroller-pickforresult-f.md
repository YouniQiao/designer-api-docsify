# pickForResult

## Modules to Import

```TypeScript
import { colorPickerController, PickedColorInfo } from '@kit.ArkUI';
```

## pickForResult

```TypeScript
function pickForResult(x?: number, y?: number, showValue?: boolean): Promise<PickedColorInfo>
```

Picks color globally, supporting both SDR and HDR formats. A color ring appears on the screen at the specified initial position and follows the user's finger or stylus movement. When the user lifts the finger or stylus, the color of the last pointing position is returned. Uses Promise for asynchronous callback.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-colorPickerController-function pickForResult(x?: number, y?: number, showValue?: boolean): Promise<PickedColorInfo>--><!--Device-colorPickerController-function pickForResult(x?: number, y?: number, showValue?: boolean): Promise<PickedColorInfo>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | number | No | Initial x-axis coordinate of the color picker. Value range: 0 to actual screen width. If the value exceeds the upper limit, the actual screen width is used. <br>Unit: px. Default value: 100. |
| y | number | No | Initial y-axis coordinate of the color picker. Value range: 0 to actual screen height. If the value exceeds the upper limit, the actual screen height is used. <br>Unit: px. Default value: 100. |
| showValue | boolean | No | Whether to display RGB values in real time. true: display; false: do not display. <br>Default value: false. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[PickedColorInfo](arkts-arkui-arkui-colorpickercontroller-pickedcolorinfo-i.md)&gt; | Promise used to return the color picking result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported on current device. |
