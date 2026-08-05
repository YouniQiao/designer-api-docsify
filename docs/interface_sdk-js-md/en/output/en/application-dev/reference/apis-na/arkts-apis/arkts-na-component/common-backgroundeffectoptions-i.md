# BackgroundEffectOptions

Defines the options of BackgroundEffect

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface BackgroundEffectOptions--><!--Device-unnamed-export declare interface BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## adaptiveColor

```TypeScript
adaptiveColor?: AdaptiveColor
```

Define the adaptiveColor of BackgroundEffect.

**Type:** AdaptiveColor

**Default:** AdaptiveColor.DEFAULT

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundEffectOptions-adaptiveColor?: AdaptiveColor--><!--Device-BackgroundEffectOptions-adaptiveColor?: AdaptiveColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## blurOptions

```TypeScript
blurOptions?: BlurOptions
```

Define the blurOptions of BackgroundEffect.

**Type:** BlurOptions

**Default:** { grayScale: [0,0] }

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundEffectOptions-blurOptions?: BlurOptions--><!--Device-BackgroundEffectOptions-blurOptions?: BlurOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## brightness

```TypeScript
brightness?: double
```

Brightness. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Value range: [0, +∞). \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_Default value: **1** Recommended value range: [0, 2].

**Type:** double

**Default:** 1

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundEffectOptions-brightness?: double--><!--Device-BackgroundEffectOptions-brightness?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color?: ResourceColor
```

Color.

**Type:** ResourceColor

**Default:** Color.Transparent

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundEffectOptions-color?: ResourceColor--><!--Device-BackgroundEffectOptions-color?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## inactiveColor

```TypeScript
inactiveColor?: ResourceColor
```

Color of the background effect when the window is not focused.

**Type:** ResourceColor

**Default:** Color.Transparent

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundEffectOptions-inactiveColor?: ResourceColor--><!--Device-BackgroundEffectOptions-inactiveColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## policy

```TypeScript
policy?: BlurStyleActivePolicy
```

Defines the policy for activating the blur style.

**Type:** BlurStyleActivePolicy

**Default:** BlurStyleActivePolicy.ALWAYS_ACTIVE

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundEffectOptions-policy?: BlurStyleActivePolicy--><!--Device-BackgroundEffectOptions-policy?: BlurStyleActivePolicy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## radius

```TypeScript
radius: double | undefined
```

Blur radius. Undefined value means 0. Value range: [0, +∞). Default value: **0**.

**Type:** double \| undefined

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundEffectOptions-radius: double | undefined--><!--Device-BackgroundEffectOptions-radius: double | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## saturation

```TypeScript
saturation?: double
```

Saturation. Value range: [0, +∞). Recommended value range: [0, 50].

**Type:** double

**Default:** 1

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundEffectOptions-saturation?: double--><!--Device-BackgroundEffectOptions-saturation?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

