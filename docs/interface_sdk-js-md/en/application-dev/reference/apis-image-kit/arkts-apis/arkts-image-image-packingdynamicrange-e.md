# PackingDynamicRange

描述编码时期望的图像动态范围。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-image-enum PackingDynamicRange--><!--Device-image-enum PackingDynamicRange-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## AUTO

```TypeScript
AUTO = 0
```

自适应，根据[pixelmap](arkts-image-image-pixelmap-i.md)内容处理。即如果pixelmap本身为HDR，则会按照HDR内容进行编码；反之按照SDR内容编码。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-PackingDynamicRange-AUTO = 0--><!--Device-PackingDynamicRange-AUTO = 0-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## SDR

```TypeScript
SDR = 1
```

按照标准动态范围处理图片。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-PackingDynamicRange-SDR = 1--><!--Device-PackingDynamicRange-SDR = 1-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

