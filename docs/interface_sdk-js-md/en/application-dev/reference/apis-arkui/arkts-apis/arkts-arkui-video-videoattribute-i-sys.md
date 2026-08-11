# VideoAttribute

Defines the Video attribute.

**Inheritance/Implementation:** VideoAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface VideoAttribute extends CommonMethod--><!--Device-unnamed-export declare interface VideoAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## surfaceBackgroundColor

```TypeScript
default surfaceBackgroundColor(color: ColorMetrics | undefined): this
```

Set background color of the surface holden by Video(only support Color.Black and Color.Transparent).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoAttribute-default surfaceBackgroundColor(color: ColorMetrics | undefined): this--><!--Device-VideoAttribute-default surfaceBackgroundColor(color: ColorMetrics | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [ColorMetrics](arkts-arkui-colormetrics-t.md) \| undefined | Yes | The surface background color. Default value is Color.Black, `undefined` means setting to the default value. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

