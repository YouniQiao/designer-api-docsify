# SliderTriggerChangeCallback

```TypeScript
export type SliderTriggerChangeCallback = (value: double, mode: SliderChangeMode) => void
```

Defines the callback type used in SliderConfiguration.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type SliderTriggerChangeCallback = (value: double, mode: SliderChangeMode) => void--><!--Device-unnamed-export type SliderTriggerChangeCallback = (value: double, mode: SliderChangeMode) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | Current progress. |
| mode | [SliderChangeMode](../arkts-components/arkts-arkui-sliderchangemode-e.md) | Yes | State triggered by the event. |

