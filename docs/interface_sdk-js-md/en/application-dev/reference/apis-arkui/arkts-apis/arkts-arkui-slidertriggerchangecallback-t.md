# SliderTriggerChangeCallback

```TypeScript
export type SliderTriggerChangeCallback = (value: double, mode: SliderChangeMode) => void
```

定义SliderConfiguration中使用的回调类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type SliderTriggerChangeCallback = (value: double, mode: SliderChangeMode) => void--><!--Device-unnamed-export type SliderTriggerChangeCallback = (value: double, mode: SliderChangeMode) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | 设置当前的进度值。<br/>取值范围：[[min](../arkts-components/arkts-arkui-slideroptions-i.md/arkts-arkui-slideroptions-i.md)-[max](../arkts-components/arkts-arkui-slideroptions-i.md/arkts-arkui-slideroptions-i.md)] |
| mode | [SliderChangeMode](../arkts-components/arkts-arkui-sliderchangemode-e.md) | Yes | 设置事件触发的相关状态值。 |

