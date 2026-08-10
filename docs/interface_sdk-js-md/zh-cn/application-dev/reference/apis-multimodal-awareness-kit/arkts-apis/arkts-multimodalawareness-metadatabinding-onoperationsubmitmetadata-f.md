# onOperationSubmitMetadata

## 导入模块

```TypeScript
import { metadataBinding } from 'kits/@kit.MultimodalAwarenessKit';
```

## onOperationSubmitMetadata

```TypeScript
function onOperationSubmitMetadata(bundleName: string, callback: Callback<int>): void
```

Subscribes to a system event to obtain the encoded metadata.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-metadataBinding-function onOperationSubmitMetadata(bundleName: string, callback: Callback<int>): void--><!--Device-metadataBinding-function onOperationSubmitMetadata(bundleName: string, callback: Callback<int>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.MetadataBinding

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | Bundle name of a third-party application |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 是 | Call back the screenshot event |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 32100001 | Internal handling failed. |
| 32100004 | Subscribe Failed. Possible causes: &lt;br&gt;1. Abnormal system capability. &lt;br&gt;2. IPC communication abnormality. &lt;br&gt;3. Algorithm loading exception. |

