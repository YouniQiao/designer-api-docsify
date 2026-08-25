# createAVMetadataExtractor

## 导入模块

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createAVMetadataExtractor

```TypeScript
function createAVMetadataExtractor(): Promise<AVMetadataExtractor>
```

创建AVMetadataExtractor实例。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AVMetadataExtractor](arkts-media-media-avmetadataextractor-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400101](../errorcode-media.md#5400101-内存分配失败) |


## createAVMetadataExtractor

```TypeScript
function createAVMetadataExtractor(callback: AsyncCallback<AVMetadataExtractor>): void
```

创建AVMetadataExtractor实例。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVMetadataExtractor](arkts-media-media-avmetadataextractor-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [5400101](../errorcode-media.md#5400101-内存分配失败) |
