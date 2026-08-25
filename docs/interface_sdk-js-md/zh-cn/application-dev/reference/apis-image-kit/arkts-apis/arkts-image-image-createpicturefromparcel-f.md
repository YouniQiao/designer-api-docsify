# createPictureFromParcel

## 导入模块

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createPictureFromParcel

```TypeScript
function createPictureFromParcel(sequence: rpc.MessageSequence): Picture
```

从MessageSequence中获取Picture。由于图片占用内存较大，所以当Picture对象使用完成后，应主动调用[release](arkts-image-image-picture-i.md#release)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成，且后续不再使用该对象。

**起始版本：** 13

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sequence | rpc.MessageSequence | 是 |

**返回值：**

| 类型 |
| --- |
| [Picture](arkts-image-image-picture-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [62980097](../errorcode-image.md#62980097-pixelmap序列化传输失败) |
