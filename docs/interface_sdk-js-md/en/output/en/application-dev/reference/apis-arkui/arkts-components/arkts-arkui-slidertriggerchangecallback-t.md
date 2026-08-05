# SliderTriggerChangeCallback

```TypeScript
declare type SliderTriggerChangeCallback = (value: number, mode: SliderChangeMode) => void
```

Defines the callback type used in **SliderConfiguration**.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-declare type SliderTriggerChangeCallback = (value: number, mode: SliderChangeMode) => void--><!--Device-unnamed-declare type SliderTriggerChangeCallback = (value: number, mode: SliderChangeMode) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number | Yes | Current progress.\_\_\_HTML\_TAG\_USD\_2\_\_\_Value range: [[min]\_\_\_JSDOC\_LINK\_USD\_0\_\_\_, [max]\_\_\_JSDOC\_LINK\_USD\_1\_\_\_]  |
| mode | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | State triggered by the event.  |

