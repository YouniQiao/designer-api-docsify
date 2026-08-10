# decodeImage（系统接口）

## 导入模块

```TypeScript
import { metadataBinding } from 'kits/@kit.MultimodalAwarenessKit';
```

## decodeImage

```TypeScript
function decodeImage(encodedImage: image.PixelMap): Promise<string>
```

Decodes the information carried in the image. This API uses a promise to return the result.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-metadataBinding-function decodeImage(encodedImage: image.PixelMap): Promise<string>--><!--Device-metadataBinding-function decodeImage(encodedImage: image.PixelMap): Promise<string>-End-->

**系统能力：** SystemCapability.MultimodalAwareness.MetadataBinding

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encodedImage | image.PixelMap | 是 | Image with metadata encoded. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise object, which is used to return the encoded metadata of the image. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 32100001 | Internal handling failed. |
| 202 | Permission check failed. A non-system application uses the system API. |
| 32100003 | Decode process fail. Possible causes: &lt;br&gt;1. Image is not an encoded Image. &lt;br&gt;2. Image destroyed, decoding failed. |

## 示例

```TypeScript
import { image } from '@kit.ImageKit';
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
import { BusinessError } from '@kit.BasicServicesKit';

// encodedImage需通过encodeImage接口处理后的图片获取。
let encodedImage: image.PixelMap | undefined = undefined;
let captureMetadata: string = "";
metadataBinding.decodeImage(encodedImage).then((metadata: string) => {
  // 将从图片解析出的元数据信息保存到captureMetadata变量，供后续使用
  captureMetadata = metadata;
}).catch((error: BusinessError) => {
  console.error(`Failed to decode image. Code: ${error.code}, message: ${error.message}`);
});
```

