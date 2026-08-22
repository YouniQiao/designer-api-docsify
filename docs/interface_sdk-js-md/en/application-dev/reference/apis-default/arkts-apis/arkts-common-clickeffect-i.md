# ClickEffect

Defines the click effect.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface ClickEffect--><!--Device-unnamed-export declare interface ClickEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## level

```TypeScript
level: ClickEffectLevel
```

Set the click effect level.

**Type:** [ClickEffectLevel](../../apis-arkui/arkts-apis/arkts-arkui-clickeffectlevel-e.md)

**Default:** ClickEffectLevel.Light

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ClickEffect-level: ClickEffectLevel--><!--Device-ClickEffect-level: ClickEffectLevel-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
scale?: double
```

Set scale number. This default scale is same as the scale of click effect level.

<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br> This parameter works based on the setting of ClickEffectLevel. <br> If level is set to ClickEffectLevel.LIGHT, the default value is 0.90. <br> If level is set to ClickEffectLevel.MIDDLE or ClickEffectLevel.HEAVY, the default value is 0.95. <br> If level is set to undefined or null (both of which evaluate to ClickEffectLevel.LIGHT), the default value is 0.90. <br> If scale is set to undefined or null, the default zoom ratio for the set level will be used. </p>

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ClickEffect-scale?: double--><!--Device-ClickEffect-scale?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

