# BlurStyleOptions

内容模糊选项。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare interface BlurStyleOptions--><!--Device-unnamed-declare interface BlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## adaptiveColor

```TypeScript
adaptiveColor?: AdaptiveColor
```

内容模糊效果使用的取色模式。

默认值：AdaptiveColor.DEFAULT

**Type:** [AdaptiveColor](../arkts-apis/arkts-arkui-common-adaptivecolor-e.md)

**Default:** AdaptiveColor.DEFAULT

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BlurStyleOptions-adaptiveColor?: AdaptiveColor--><!--Device-BlurStyleOptions-adaptiveColor?: AdaptiveColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## blurOptions

```TypeScript
blurOptions?: BlurOptions
```

灰阶模糊参数。

默认值：grayscale: [0,0]

**Type:** [BlurOptions](arkts-arkui-bluroptions-i.md)

**Default:** { grayScale: [0,0] }

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BlurStyleOptions-blurOptions?: BlurOptions--><!--Device-BlurStyleOptions-blurOptions?: BlurOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## colorMode

```TypeScript
colorMode?: ThemeColorMode
```

内容模糊效果使用的深浅色模式。

默认值：ThemeColorMode.SYSTEM

**Type:** [ThemeColorMode](arkts-arkui-themecolormode-e.md)

**Default:** ThemeColorMode.SYSTEM

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BlurStyleOptions-colorMode?: ThemeColorMode--><!--Device-BlurStyleOptions-colorMode?: ThemeColorMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
scale?: number
```

内容模糊效果程度。

默认值：1.0

取值范围：[0.0, 1.0]

1.0表示模糊程度最高。

0.0表示模糊程度最低。

**Type:** number

**Default:** 1.0

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BlurStyleOptions-scale?: number--><!--Device-BlurStyleOptions-scale?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

