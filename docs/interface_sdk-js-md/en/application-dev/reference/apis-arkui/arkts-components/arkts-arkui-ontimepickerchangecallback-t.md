# OnTimePickerChangeCallback

```TypeScript
declare type OnTimePickerChangeCallback = (result: TimePickerResult) => void
```

选择时间时触发该事件。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type OnTimePickerChangeCallback = (result: TimePickerResult) => void--><!--Device-unnamed-declare type OnTimePickerChangeCallback = (result: TimePickerResult) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | [TimePickerResult](../arkts-apis/arkts-arkui-timepicker-timepickerresult-i.md) | Yes | 选中的时间结果，hour取值0-23，与展示制式无关。 |

