# createImageCreator

## 导入模块

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createImageCreator

```TypeScript
function createImageCreator(width: number, height: number, format: number, capacity: number): ImageCreator
```

通过宽、高、图片格式、容量创建ImageCreator实例。由于图片占用内存较大，所以当ImageCreator实例使用完成后，应主动调用[release](arkts-image-image-imagecreator-i.md#release)方法 及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

> **说明：**&gt;
> 从API version 9开始支持，从API version 11废弃，建议使用[createImageCreator](#createimagecreator)代替。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [createImageCreator](#createimagecreator)(size: Size, format: ImageFormat, capacity: int)

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


## createImageCreator

```TypeScript
function createImageCreator(size: Size, format: ImageFormat, capacity: number): ImageCreator
```

通过图片大小、图片格式、容量创建ImageCreator实例。由于图片占用内存较大，所以当ImageCreator实例使用完成后，应主动调用[release](arkts-image-image-imagecreator-i.md#release)方法 及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | Size | 是 |
| format | [ImageFormat](arkts-image-image-imageformat-e.md) | 是 |
| capacity | number | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageCreator](arkts-image-image-imagecreator-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
