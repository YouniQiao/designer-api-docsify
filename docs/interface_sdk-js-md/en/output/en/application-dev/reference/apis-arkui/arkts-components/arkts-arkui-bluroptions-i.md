# BlurOptions

Grayscale blur parameters.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare interface BlurOptions--><!--Device-unnamed-declare interface BlurOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## grayscale

```TypeScript
grayscale: [number, number]
```

Grayscale blur, with two parameters in the value range of [0, 127]. The color gradation of the black and white in the image is adjusted to create different shades of gray. The first parameter indicates the brightness of the black color, and the second parameter indicates the darkness of the white color. A larger value indicates a more obvious adjustment effect (the black and white colors become grayer). The valid value range is 0–127. For example, if the value specified is (20,20), the RGB value \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ is converted to [20, 20, 20], RGB value \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_ is converted to \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_, and the color pixels remain unchanged.

**Type:** [number, number]

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BlurOptions-grayscale: [number, number]--><!--Device-BlurOptions-grayscale: [number, number]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

