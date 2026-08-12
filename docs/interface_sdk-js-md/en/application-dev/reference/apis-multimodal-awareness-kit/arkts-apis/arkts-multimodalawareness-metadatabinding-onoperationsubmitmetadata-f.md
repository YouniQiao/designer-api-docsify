# onOperationSubmitMetadata

## Modules to Import

```TypeScript
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
```

## onOperationSubmitMetadata

```TypeScript
function onOperationSubmitMetadata(bundleName: string, callback: Callback<int>): void
```

Subscribes to a system event to obtain the encoded metadata.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-metadataBinding-function onOperationSubmitMetadata(bundleName: string, callback: Callback<int>): void--><!--Device-metadataBinding-function onOperationSubmitMetadata(bundleName: string, callback: Callback<int>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.MetadataBinding

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Bundle name of a third-party application |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;int&gt; | Yes | Call back the screenshot event |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [32100001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100001-file-creation-failed) | Internal handling failed. |
| [32100004](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100004-subscription-failed) | Subscribe Failed. Possible causes: &lt;br&gt;1. Abnormal system capability. &lt;br&gt;2. IPC communication abnormality. &lt;br&gt;3. Algorithm loading exception. |

