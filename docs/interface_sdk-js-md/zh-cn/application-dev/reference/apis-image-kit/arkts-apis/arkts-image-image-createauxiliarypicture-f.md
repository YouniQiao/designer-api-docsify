# createAuxiliaryPicture

## 导入模块

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createAuxiliaryPicture

```TypeScript
function createAuxiliaryPicture(buffer: ArrayBuffer, size: Size, type: AuxiliaryPictureType): AuxiliaryPicture
```

通过ArrayBuffer图片数据、辅助图尺寸、辅助图类型创建AuxiliaryPicture实例。该接口仅支持传入BGRA的连续像素数据，会创建出RGBA的辅助图。由于图片占用内存较大，所以当AuxiliaryPicture实例使用完成后，应主动调用[release](arkts-image-image-auxiliarypicture-i.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法 均执行完成，且后续不再使用该实例。

**起始版本：** 13

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer | 是 |
| size | Size | 是 |
| type | [AuxiliaryPictureType](arkts-image-image-auxiliarypicturetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [AuxiliaryPicture](arkts-image-image-auxiliarypicture-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
