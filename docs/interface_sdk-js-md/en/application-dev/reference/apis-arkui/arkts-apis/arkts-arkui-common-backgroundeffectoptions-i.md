# BackgroundEffectOptions

背景效果参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface BackgroundEffectOptions--><!--Device-unnamed-export declare interface BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## adaptiveColor

```TypeScript
adaptiveColor?: AdaptiveColor
```

背景模糊效果使用的取色模式，默认为DEFAULT。使用AVERAGE时color必须带有透明度，取色模式才生效。

**Type:** [AdaptiveColor](arkts-arkui-common-adaptivecolor-e.md)

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

灰阶模糊参数，默认为[0,0]。

**Type:** [BlurOptions](../arkts-components/arkts-arkui-bluroptions-i.md)

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

亮度，取值范围：[0, +∞)，默认为1。推荐取值范围：[0, 2]。

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

颜色，默认透明色。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

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

模糊不生效时使用的背景色。该参数需配合policy参数使用。当policy使模糊失效时，控件模糊效果会被移除，如果设置了inactiveColor会使用inactiveColor作为控件背景色。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

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

模糊激活策略。

默认值：BlurStyleActivePolicy.ALWAYS_ACTIVE

**Type:** [BlurStyleActivePolicy](../arkts-components/arkts-arkui-blurstyleactivepolicy-e.md)

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

模糊半径，取值范围：[0, +∞)，默认为0。

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

饱和度，取值范围：[0, +∞)，默认为1。推荐取值范围：[0, 50]。

**Type:** double

**Default:** 1

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundEffectOptions-saturation?: double--><!--Device-BackgroundEffectOptions-saturation?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

