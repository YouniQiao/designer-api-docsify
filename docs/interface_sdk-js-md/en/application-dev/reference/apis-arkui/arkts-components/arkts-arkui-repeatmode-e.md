# RepeatMode

用于设置被切割的图片在边框上的重复方式。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare enum RepeatMode--><!--Device-unnamed-declare enum RepeatMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Repeat

```TypeScript
Repeat = 0
```

被切割的图片会重复铺平在图片边框上，超出部分会被剪裁。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-RepeatMode-Repeat = 0--><!--Device-RepeatMode-Repeat = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Stretch

```TypeScript
Stretch = 1
```

被切割的图片会以拉伸填充的方式铺满图片边框。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-RepeatMode-Stretch = 1--><!--Device-RepeatMode-Stretch = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Round

```TypeScript
Round = 2
```

被切割的图片会以整数次平铺在图片边框上，无法以整数次平铺时会压缩图片。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-RepeatMode-Round = 2--><!--Device-RepeatMode-Round = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Space

```TypeScript
Space = 3
```

被切割的图片会以整数次平铺在图片边框上，无法以整数次平铺时会以空白填充。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-RepeatMode-Space = 3--><!--Device-RepeatMode-Space = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

