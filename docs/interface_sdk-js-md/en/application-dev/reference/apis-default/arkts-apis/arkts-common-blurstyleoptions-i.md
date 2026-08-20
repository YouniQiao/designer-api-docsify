# BlurStyleOptions

Defines the options of blurStyle

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface BlurStyleOptions--><!--Device-unnamed-export declare interface BlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## adaptiveColor

```TypeScript
adaptiveColor?: AdaptiveColor
```

Adaptive color mode. <br>Default value: **AdaptiveColor.DEFAULT**.

**Type:** [AdaptiveColor](arkts-common-adaptivecolor-e.md)

**Default:** AdaptiveColor.DEFAULT

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BlurStyleOptions-adaptiveColor?: AdaptiveColor--><!--Device-BlurStyleOptions-adaptiveColor?: AdaptiveColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## blurOptions

```TypeScript
blurOptions?: BlurOptions
```

Defines the options of blur

**Type:** [BlurOptions](arkts-common-bluroptions-i.md)

**Default:** { grayScale: [0,0] }

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BlurStyleOptions-blurOptions?: BlurOptions--><!--Device-BlurStyleOptions-blurOptions?: BlurOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## colorMode

```TypeScript
colorMode?: ThemeColorMode
```

Color mode used for the foreground blur. <br>Default value: **ThemeColorMode.SYSTEM**.

**Type:** [ThemeColorMode](arkts-common-themecolormode-e.md)

**Default:** ThemeColorMode.SYSTEM

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BlurStyleOptions-colorMode?: ThemeColorMode--><!--Device-BlurStyleOptions-colorMode?: ThemeColorMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
scale?: double
```

Foreground blur scale. <br>Default value: **1.0**. <br>Value range: [0.0, 1.0].

**Type:** double

**Default:** 1.0

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BlurStyleOptions-scale?: double--><!--Device-BlurStyleOptions-scale?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

