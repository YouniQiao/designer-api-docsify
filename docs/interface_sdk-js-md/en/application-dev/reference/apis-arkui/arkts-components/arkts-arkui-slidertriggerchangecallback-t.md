# SliderTriggerChangeCallback

```TypeScript
declare type SliderTriggerChangeCallback = (value: number, mode: SliderChangeMode) => void
```

定义SliderConfiguration中使用的回调类型。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-declare type SliderTriggerChangeCallback = (value: number, mode: SliderChangeMode) => void--><!--Device-unnamed-declare type SliderTriggerChangeCallback = (value: number, mode: SliderChangeMode) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number | Yes | 设置当前进度值。<br/>取值范围：[[min](arkts-arkui-slideroptions-i.md)-[max](arkts-arkui-slideroptions-i.md)] |
| mode | [SliderChangeMode](arkts-arkui-sliderchangemode-e.md) | Yes | 设置事件触发的相关状态值。 |

