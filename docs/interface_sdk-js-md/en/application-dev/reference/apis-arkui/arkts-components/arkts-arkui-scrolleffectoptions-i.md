# ScrollEffectOptions

定义标题栏的滑动模糊效果选项。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-unnamed-declare interface ScrollEffectOptions--><!--Device-unnamed-declare interface ScrollEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## blurEffectiveEndOffset

```TypeScript
blurEffectiveEndOffset?: LengthMetrics
```

达到标题栏最终模糊样式的最大滑动距离。当用户滑动距离达到该值时，模糊效果达到最终状态。默认值： 8vp。

**Type:** [LengthMetrics](../arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ScrollEffectOptions-blurEffectiveEndOffset?: LengthMetrics--><!--Device-ScrollEffectOptions-blurEffectiveEndOffset?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## blurEffectiveStartOffset

```TypeScript
blurEffectiveStartOffset?: LengthMetrics
```

启用标题栏滚动模糊效果的最小滑动距离。当用户滑动距离超过该值时，开始应用模糊效果。默认值： 0vp。

**Type:** [LengthMetrics](../arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ScrollEffectOptions-blurEffectiveStartOffset?: LengthMetrics--><!--Device-ScrollEffectOptions-blurEffectiveStartOffset?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scrollEffectType

```TypeScript
scrollEffectType?: ScrollEffectType
```

标题栏滚动模糊效果类型。默认值： ScrollEffectType.COMMON_BLUR。

**Type:** [ScrollEffectType](../arkts-apis/arkts-arkui-navigation-scrolleffecttype-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ScrollEffectOptions-scrollEffectType?: ScrollEffectType--><!--Device-ScrollEffectOptions-scrollEffectType?: ScrollEffectType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

