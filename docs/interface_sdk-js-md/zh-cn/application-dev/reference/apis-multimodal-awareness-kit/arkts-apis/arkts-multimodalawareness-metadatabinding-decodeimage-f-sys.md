# decodeImage（系统接口）

## 导入模块

```TypeScript
import { metadataBinding } from 'kits/@kit.MultimodalAwarenessKit';
```

## decodeImage

```TypeScript
function decodeImage(encodedImage: image.PixelMap): Promise<string>
```

解析图片中携带的信息。通过对应的解码算法从图片中提取嵌入的metadata信息。使用Promise异步回调。

**起始版本：** 18

**系统能力：** SystemCapability.MultimodalAwareness.MetadataBinding

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| encodedImage | image.PixelMap | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [32100001](../errorcode-metadataBinding.md#32100001-文件创建失败) |
| [32100003](../errorcode-metadataBinding.md#32100003-解码程序执行失败) |
