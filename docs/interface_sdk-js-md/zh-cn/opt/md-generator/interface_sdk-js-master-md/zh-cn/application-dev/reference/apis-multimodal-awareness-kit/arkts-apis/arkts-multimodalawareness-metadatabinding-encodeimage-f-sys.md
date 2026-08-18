# encodeImage（系统接口）

## 导入模块

```TypeScript
```

## encodeImage

```TypeScript
function encodeImage(srcImage: image.PixelMap, metadata: string): Promise<image.PixelMap>
```

在图片中加入信息。通过特定的编码算法将metadata信息嵌入到图片中，编码过程对图片的视觉呈现影响极小，嵌入的信息可通过decodeImage接口解析。可用于防伪、版权保护等场景。 <br>使用Promise异步回调。

**起始版本：** 23

<!--Device-metadataBinding-function encodeImage(srcImage: image.PixelMap, metadata: string): Promise<image.PixelMap>--><!--Device-metadataBinding-function encodeImage(srcImage: image.PixelMap, metadata: string): Promise<image.PixelMap>-End-->

**系统能力：** SystemCapability.MultimodalAwareness.MetadataBinding

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| srcImage | image.PixelMap | 是 |
| metadata | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [32100001](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100001-文件创建失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [32100002](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100002-编码程序执行失败) |

**示例**

```TypeScript
import { image } from '@kit.ImageKit';
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
import { BusinessError } from '@kit.BasicServicesKit';

let encodedImage: image.PixelMap | undefined = undefined;
let metadata: string = '';
// srcImage需通过image内的接口获取有效的PixelMap对象
let srcImage: image.PixelMap | undefined = undefined;
metadataBinding.encodeImage(srcImage, metadata).then((pixelMap: image.PixelMap) => {
  encodedImage = pixelMap;
}).catch((error: BusinessError) => {
  console.error(`Failed to encode image. Code: ${error.code}, message: ${error.message}`);
});
```
