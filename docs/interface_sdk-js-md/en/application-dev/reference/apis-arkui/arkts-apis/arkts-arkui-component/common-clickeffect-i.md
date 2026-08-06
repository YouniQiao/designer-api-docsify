# ClickEffect

Defines the click effect.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ClickEffect--><!--Device-unnamed-export declare interface ClickEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## level

```TypeScript
level: ClickEffectLevel
```

Set the click effect level.

**Type:** ClickEffectLevel

**Default:** ClickEffectLevel.Light

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ClickEffect-level: ClickEffectLevel--><!--Device-ClickEffect-level: ClickEffectLevel-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
scale?: double
```

Set scale number.This default scale is same as the scale of click effect level.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_:\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_ This parameter works based on the setting of ClickEffectLevel.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_ If level is set to ClickEffectLevel.LIGHT, the default value is 0.90.\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_ If level is set to ClickEffectLevel.MIDDLE or ClickEffectLevel.HEAVY, the default value is 0.95.\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_ If level is set to undefined or null (both of which evaluate to ClickEffectLevel.LIGHT), the default value is 0.90.\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_ If scale is set to undefined or null, the default zoom ratio for the set level will be used.\_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ClickEffect-scale?: double--><!--Device-ClickEffect-scale?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

