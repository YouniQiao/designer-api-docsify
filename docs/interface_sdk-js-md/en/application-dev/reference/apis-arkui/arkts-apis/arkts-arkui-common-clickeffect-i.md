# ClickEffect

定义点击效果。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ClickEffect--><!--Device-unnamed-export declare interface ClickEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## level

```TypeScript
level: ClickEffectLevel
```

设置当前组件的点击回弹效果。

默认值：ClickEffectLevel.LIGHT

**说明：**

当level为undefined或者null时， ClickEffect采用ClickEffectLevel.LIGHT对应的回弹效果，缩放比参照scale说明。

**Type:** [ClickEffectLevel](arkts-arkui-clickeffectlevel-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ClickEffect-level: ClickEffectLevel--><!--Device-ClickEffect-level: ClickEffectLevel-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
scale?: double
```

回弹缩放比例，支持在设置ClickEffectLevel的基础上微调。

**说明：**

当level为ClickEffectLevel.LIGHT时，默认值：0.90 

当level为ClickEffectLevel.MIDDLE或者ClickEffectLevel.HEAVY时，默认值：0.95 

当level为undefined或者null时，level为ClickEffectLevel.LIGHT，默认值：0.90 

当scale为undefined或者null时，使用当前level对应的默认缩放比例。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ClickEffect-scale?: double--><!--Device-ClickEffect-scale?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

