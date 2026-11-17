# PositionArea

```TypeScript
interface PositionArea
```

表示图片指定区域内的数据。

**起始版本：** 7

<!--Device-image-interface PositionArea--><!--Device-image-interface PositionArea-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## 导入模块

```TypeScript
import { image } from '@kit.ImageKit';
```

## offset

```TypeScript
offset: number
```

`pixels`缓冲区内第一个像素的字节偏移量，即区域像素数据在缓冲区中的起始位置。<br>读写区域数据时，从`pixels[offset]`处开始读取或写入。<br>单位：字节（Byte）。

**类型：** number

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PositionArea-offset: int--><!--Device-PositionArea-offset: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## pixels

```TypeScript
pixels: ArrayBuffer
```

区域像素数据缓冲区。

**类型：** ArrayBuffer

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PositionArea-pixels: ArrayBuffer--><!--Device-PositionArea-pixels: ArrayBuffer-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## region

```TypeScript
region: Region
```

区域信息，用于按区域进行图像数据的读写。<br>指定区域的宽度加X坐标不能大于原图的宽度。<br>指定区域的高度加Y坐标不能大于原图的高度。

**类型：** [Region](arkts-image-image-region-i.md)

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PositionArea-region: Region--><!--Device-PositionArea-region: Region-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## stride

```TypeScript
stride: number
```

跨距，内存中每行像素（含行末填充字节）所占的空间。单位：字节（Byte）。

**类型：** number

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-PositionArea-stride: int--><!--Device-PositionArea-stride: int-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core
