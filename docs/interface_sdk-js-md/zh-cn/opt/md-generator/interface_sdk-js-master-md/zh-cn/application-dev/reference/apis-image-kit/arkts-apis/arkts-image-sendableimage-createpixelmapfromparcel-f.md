# createPixelMapFromParcel

## createPixelMapFromParcel

```TypeScript
function createPixelMapFromParcel(sequence: rpc.MessageSequence): PixelMap
```

Creates a PixelMap object based on MessageSequence parameter.

**起始版本：** 12

**废弃版本：** -1

<!--Device-sendableImage-function createPixelMapFromParcel(sequence: rpc.MessageSequence): PixelMap--><!--Device-sendableImage-function createPixelMapFromParcel(sequence: rpc.MessageSequence): PixelMap-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sequence | rpc.MessageSequence | 是 |

**返回值：**

| 类型 |
| --- |
| [PixelMap](../../apis-na/arkts-apis/arkts-na-pixelmap-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [62980097](../errorcode-image.md#62980097-pixelmap序列化传输失败) |
| [62980177](../errorcode-image.md#62980177-api环境异常) |
| [62980096](../errorcode-image.md#62980096-操作失败) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980179](../errorcode-image.md#62980179-缓冲区大小异常) |
| [62980178](../errorcode-image.md#62980178-pixelmap创建失败) |
| [62980180](../errorcode-image.md#62980180-文件描述符映射失败) |
| [62980246](../errorcode-image.md#62980246-读取pixelmap失败) |
| [62980105](../errorcode-image.md#62980105-图片获取数据错误) |

## 示例

```TypeScript
// EntryAbility.ets
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MySequence implements rpc.Parcelable {
  pixel_map: sendableImage.PixelMap;
  constructor(conPixelmap: sendableImage.PixelMap) {
    this.pixel_map = conPixelmap;
  }
  marshalling(messageSequence: rpc.MessageSequence) {
    this.pixel_map.marshalling(messageSequence);
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence) {
    try {
      this.pixel_map = sendableImage.createPixelMapFromParcel(messageSequence);
    } catch(e) {
      let error = e as BusinessError;
      console.error(`Failed to create a PixelMap from a parcel. Code: ${error.code}, message: ${error.message}.`);
      return false;
    }
    return true;
  }
}
async function CreatePixelMapFromParcel() {
  const color: ArrayBuffer = new ArrayBuffer(96);
  let bufferArr: Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr[i] = 0x80;
  }
  let opts: image.InitializationOptions = {
    editable: true,
    pixelFormat: 4,
    size: { height: 4, width: 6 },
    alphaType: 3
  }
  let pixelMap: sendableImage.PixelMap | undefined = undefined;
  await sendableImage.createPixelMap(color, opts).then((srcPixelMap: sendableImage.PixelMap) => {
    pixelMap = srcPixelMap;
  })
  if (pixelMap != undefined) {
    // 序列化。
    let parcelable: MySequence = new MySequence(pixelMap);
    let data: rpc.MessageSequence = rpc.MessageSequence.create();
    data.writeParcelable(parcelable);

    // 反序列化rpc获取到data。
    let ret: MySequence = new MySequence(pixelMap);
    data.readParcelable(ret);

    // 获取到PixelMap。
    let newPixelMap = ret.pixel_map;
  }
}
```
