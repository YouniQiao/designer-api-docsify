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

Animation curve.&lt;br&gt;You are advised to specify the curve using the **Curve** or  
** ICurve** type.&lt;br&gt;For the string type, this parameter indicates an animation interpolation curve. For available values, see the **curve** parameter in AnimateParam.&lt;br&gt;Default value: **Curve.Linear**.

**Type:** [Curve](arkts-arkui-curve-e.md) \| string \| ICurve

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

Animation duration.&lt;br&gt;Default value: **1000**.&lt;br&gt;Unit: ms.&lt;br&gt;Value range: [0, +∞).

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

**Type:** [MotionPathOptions](arkts-arkui-common-motionpathoptions-i.md)

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

**Type:** [SharedTransitionEffectType](arkts-arkui-sharedtransitioneffecttype-e.md)

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

