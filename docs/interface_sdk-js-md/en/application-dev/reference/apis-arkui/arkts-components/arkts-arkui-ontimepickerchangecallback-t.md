# OnTimePickerChangeCallback

```TypeScript
declare type OnTimePickerChangeCallback = (result: TimePickerResult) => void
```

Triggered when a time is selected.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type OnTimePickerChangeCallback = (result: TimePickerResult) => void--><!--Device-unnamed-declare type OnTimePickerChangeCallback = (result: TimePickerResult) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | [TimePickerResult](arkts-arkui-timepickerresult-i.md) | Yes | Time in 24-hour format. |

