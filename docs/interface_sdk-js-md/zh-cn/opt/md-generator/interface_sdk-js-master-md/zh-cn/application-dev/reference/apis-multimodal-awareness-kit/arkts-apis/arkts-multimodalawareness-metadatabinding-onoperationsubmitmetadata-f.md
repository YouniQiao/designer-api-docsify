# onOperationSubmitMetadata

## onOperationSubmitMetadata

```TypeScript
function onOperationSubmitMetadata(bundleName: string, callback: Callback<number>): void
```

订阅系统获取编码内容的事件。

**起始版本：** 23

**废弃版本：** -1

<!--Device-metadataBinding-function onOperationSubmitMetadata(bundleName: string, callback: Callback<int>): void--><!--Device-metadataBinding-function onOperationSubmitMetadata(bundleName: string, callback: Callback<int>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.MetadataBinding

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [32100001](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100001-文件创建失败) |
| [32100004](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100004-订阅失败) |
