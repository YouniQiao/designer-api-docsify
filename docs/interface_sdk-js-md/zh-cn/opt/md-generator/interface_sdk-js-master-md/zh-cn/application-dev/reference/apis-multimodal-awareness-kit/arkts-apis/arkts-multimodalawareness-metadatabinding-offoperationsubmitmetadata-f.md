# offOperationSubmitMetadata

## 导入模块

```TypeScript
```

## offOperationSubmitMetadata

```TypeScript
function offOperationSubmitMetadata(bundleName: string, callback?: Callback<number>): void
```

取消订阅系统获取编码内容的事件。

**起始版本：** 23

<!--Device-metadataBinding-function offOperationSubmitMetadata(bundleName: string, callback?: Callback<int>): void--><!--Device-metadataBinding-function offOperationSubmitMetadata(bundleName: string, callback?: Callback<int>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.MetadataBinding

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [32100001](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100001-文件创建失败) |
| [32100005](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100005-取消订阅失败) |
