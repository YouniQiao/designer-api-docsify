# PositionArea

表示图片指定区域内的数据。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-image-interface PositionArea--><!--Device-image-interface PositionArea-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## offset

```TypeScript
offset: int
```

偏移量。单位：字节（Byte）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PositionArea-offset: int--><!--Device-PositionArea-offset: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## pixels

```TypeScript
pixels: ArrayBuffer
```

像素数据缓冲区。仅支持BGRA_8888格式的像素数据。

**Type:** ArrayBuffer

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PositionArea-pixels: ArrayBuffer--><!--Device-PositionArea-pixels: ArrayBuffer-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## region

```TypeScript
region: Region
```

区域信息，用于按区域进行图像数据的读写。写入的区域宽度加X坐标不能大于原图的宽度，写入的区域高度加Y坐标不能大于原图的高度。

**Type:** [Region](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-drawing-region-c.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PositionArea-region: Region--><!--Device-PositionArea-region: Region-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## stride

```TypeScript
stride: int
```

跨距，内存中每行像素所占的空间。单位：字节（Byte）。stride >= region.size.width * 4，不满足时数据读取异常。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PositionArea-stride: int--><!--Device-PositionArea-stride: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

