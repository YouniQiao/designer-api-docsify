# createImageCreator

## createImageCreator

```TypeScript
function createImageCreator(width: number, height: number, format: number, capacity: number): ImageCreator
```

通过宽、高、图片格式、容量创建ImageCreator实例。

由于图片占用内存较大，所以当ImageCreator实例使用完成后，应主动调用[release](arkts-image-image-imagecreator-i.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

> **说明：**
> 
> 从API version 9开始支持，从API version 11废弃，建议使用[createImageCreator](arkts-image-image-createimagecreator-f.md#createimagecreator)代替。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [image.createImageCreator](arkts-image-image-createimagecreator-f.md#createimagecreator)(size:

<!--Device-image-function createImageCreator(width: number, height: number, format: number, capacity: number): ImageCreator--><!--Device-image-function createImageCreator(width: number, height: number, format: number, capacity: number): ImageCreator-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| width | number | 是 |
| height | number | 是 |
| format | number | 是 |
| capacity | number | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageCreator](arkts-image-image-imagecreator-i.md) |

## 示例

```TypeScript
let creator: image.ImageCreator = image.createImageCreator(8192, 8192, image.ImageFormat.JPEG, 8);
```


## createImageCreator

```TypeScript
function createImageCreator(size: Size, format: ImageFormat, capacity: number): ImageCreator
```

通过图片大小、图片格式、容量创建ImageCreator实例。

由于图片占用内存较大，所以当ImageCreator实例使用完成后，应主动调用[release](arkts-image-image-imagecreator-i.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 11

<!--Device-image-function createImageCreator(size: Size, format: ImageFormat, capacity: int): ImageCreator--><!--Device-image-function createImageCreator(size: Size, format: ImageFormat, capacity: int): ImageCreator-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | [Size](../../apis-arkui/arkts-apis/arkts-arkui-window-size-i.md) | 是 |
| format | [ImageFormat](arkts-image-image-imageformat-e.md) | 是 |
| capacity | number | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageCreator](arkts-image-image-imagecreator-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

```TypeScript
let size: image.Size = {
  height: 8192,
  width: 8192
}
let creator: image.ImageCreator = image.createImageCreator(size, image.ImageFormat.JPEG, 8);
```
