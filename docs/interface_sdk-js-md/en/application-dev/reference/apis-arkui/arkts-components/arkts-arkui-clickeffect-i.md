# ClickEffect

定义点击效果。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface ClickEffect--><!--Device-unnamed-declare interface ClickEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## level

```TypeScript
level: ClickEffectLevel
```

设置当前组件的点击回弹效果。

默认值：ClickEffectLevel.LIGHT

**说明：**

当level为undefined或者null时， ClickEffect采用ClickEffectLevel.LIGHT对应的回弹效果，缩放比参照scale说明。

**Type:** [ClickEffectLevel](../arkts-apis/arkts-arkui-clickeffectlevel-e.md)

**Default:** ClickEffectLevel.LIGHT

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ClickEffect-level: ClickEffectLevel--><!--Device-ClickEffect-level: ClickEffectLevel-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
scale?: number
```

回弹缩放比例，支持在设置ClickEffectLevel的基础上微调。

**说明：**

当level为ClickEffectLevel.LIGHT时，默认值：0.90 

当level为ClickEffectLevel.MIDDLE或者ClickEffectLevel.HEAVY时，默认值：0.95 

当level为undefined或者null时，level为ClickEffectLevel.LIGHT，默认值：0.90 

当scale为undefined或者null时，使用当前level对应的默认缩放比例。

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ClickEffect-scale?: number--><!--Device-ClickEffect-scale?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

