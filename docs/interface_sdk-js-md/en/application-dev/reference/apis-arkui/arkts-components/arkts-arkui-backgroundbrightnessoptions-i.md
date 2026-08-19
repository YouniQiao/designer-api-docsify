# BackgroundBrightnessOptions

Provides background brightness options. &gt; **NOTE：**&gt; &gt; The brightness (gray scale value) of each pixel in the component background content is calculated using the &gt; following formula: &gt; &gt; Y = (0.299R + 0.587G + 0.114B) / 255.0, where **R**, **G**, and **B** represent red, green, and blue channel &gt; values of the pixel, respectively, and **Y** is the gray scale value. This formula normalizes the gray scale value &gt; to a range of 0 to 1. &gt; &gt; The formula for calculating the increase in brightness for each pixel is as follows: ΔY = -rate * Y + &gt; lightUpDegree. For example, when rate = 0.5 and lightUpDegree = 0.5, for a pixel with a gray scale value of 0.2, &gt; the increase in brightness is -0.5 * 0.2 + 0.5 = 0.4. For a pixel with a gray scale value of 1, the increase in &gt; brightness is -0.5 * 1 + 0.5 = 0.

**Since:** 12

<!--Device-unnamed-declare interface BackgroundBrightnessOptions--><!--Device-unnamed-declare interface BackgroundBrightnessOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## lightUpDegree

```TypeScript
lightUpDegree: number
```

Light up degree. A greater degree indicates a greater increase in brightness. Default value: **0.0** Value range: [-1.0, 1.0]

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BackgroundBrightnessOptions-lightUpDegree: number--><!--Device-BackgroundBrightnessOptions-lightUpDegree: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rate

```TypeScript
rate: number
```

Brightness change rate. A higher rate means that brightness decreases more quickly. If **rate** is set to **0**, **lightUpDegree** will not take effect, meaning no brightening effect will occur. Default value: **0.0** Value range: (0.0, +∞)

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BackgroundBrightnessOptions-rate: number--><!--Device-BackgroundBrightnessOptions-rate: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

