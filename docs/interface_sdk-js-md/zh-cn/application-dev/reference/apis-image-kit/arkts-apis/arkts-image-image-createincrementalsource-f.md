# CreateIncrementalSource

## 导入模块

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## CreateIncrementalSource

```TypeScript
function CreateIncrementalSource(buf: ArrayBuffer): ImageSource
```

通过缓冲区以增量的方式创建ImageSource实例，IncrementalSource不支持读写Exif信息。由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](arkts-image-image-imagesource-i.md#release)方法及时 释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。以增量方式创建的ImageSource实例，仅支持使用以下功能，同步、异步callback、异步Promise均支持。  
- 获取图片信息：指定序号-[getImageInfo](arkts-image-image-imagesource-i.md#getimageinfo)、  
直接获取-[getImageInfo](arkts-image-image-imagesource-i.md#getimageinfo)  
- 获取图片中给定索引处图像的指定属性键的值：  
[getImageProperty](arkts-image-image-imagesource-i.md#getimageproperty)  
- 批量获取图片中的指定属性键的值：[getImageProperties](arkts-image-image-imagesource-i.md#getimageproperties)  
- 更新增量数据：  
[updateData](arkts-image-image-imagesource-i.md#updatedata)  
- 创建PixelMap对象：通过图片解码参数创建-[createPixelMap](arkts-image-image-createpixelmap-f.md)、通过默认参数创建-  
[createPixelMap](arkts-image-image-createpixelmap-f.md) 、通过图片解码参数-[createPixelMap](arkts-image-image-createpixelmap-f.md)  
- 释放ImageSource实例：[release](arkts-image-image-imagesource-i.md#release)

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |


## CreateIncrementalSource

```TypeScript
function CreateIncrementalSource(buf: ArrayBuffer, options?: SourceOptions): ImageSource
```

通过缓冲区以增量的方式创建ImageSource实例，IncrementalSource不支持读写Exif信息。此接口支持的功能与[CreateIncrementalSource(buf: ArrayBuffer): ImageSource](#createincrementalsource)所生成的实例支持的功能相 同。由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](arkts-image-image-imagesource-i.md#release)方法及时 释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | ArrayBuffer | 是 |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |
