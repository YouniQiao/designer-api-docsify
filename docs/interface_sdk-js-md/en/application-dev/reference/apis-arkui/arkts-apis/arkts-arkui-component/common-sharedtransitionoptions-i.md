# sharedTransitionOptions

Defines the shard transition function params.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface sharedTransitionOptions--><!--Device-unnamed-export declare interface sharedTransitionOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## curve

```TypeScript
curve?: Curve | string | ICurve
```

Animation curve.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_You are advised to specify the curve using the **Curve** or  
** ICurve** type.\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_For the string type, this parameter indicates an animation interpolation curve. For available values, see the **curve** parameter in AnimateParam.\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_Default value: **Curve.Linear**.

**Type:** Curve \| string \| ICurve

**Default:** 1000

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-sharedTransitionOptions-curve?: Curve | string | ICurve--><!--Device-sharedTransitionOptions-curve?: Curve | string | ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## delay

```TypeScript
delay?: int
```

Animation delay time, in ms.

**Type:** int

**Default:** 0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-sharedTransitionOptions-delay?: int--><!--Device-sharedTransitionOptions-delay?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration?: int
```

Animation duration.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Default value: **1000**.\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_Unit: ms.\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_Value range: [0, +∞).

**Type:** int

**Default:** 1000

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-sharedTransitionOptions-duration?: int--><!--Device-sharedTransitionOptions-duration?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## motionPath

```TypeScript
motionPath?: MotionPathOptions
```

The motion path info.

**Type:** MotionPathOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-sharedTransitionOptions-motionPath?: MotionPathOptions--><!--Device-sharedTransitionOptions-motionPath?: MotionPathOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type?: SharedTransitionEffectType
```

the animate type.

**Type:** SharedTransitionEffectType

**Default:** SharedTransitionEffectType.Exchange

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-sharedTransitionOptions-type?: SharedTransitionEffectType--><!--Device-sharedTransitionOptions-type?: SharedTransitionEffectType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## zIndex

```TypeScript
zIndex?: int
```

Z index info.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-sharedTransitionOptions-zIndex?: int--><!--Device-sharedTransitionOptions-zIndex?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

