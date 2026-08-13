# offOperationSubmitMetadata

## Modules to Import

```TypeScript
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
```

## offOperationSubmitMetadata

```TypeScript
function offOperationSubmitMetadata(bundleName: string, callback?: Callback<int>): void
```

Unsubscribes from system events that are used to obtain the encoded metadata.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-metadataBinding-function offOperationSubmitMetadata(bundleName: string, callback?: Callback<int>): void--><!--Device-metadataBinding-function offOperationSubmitMetadata(bundleName: string, callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.MetadataBinding

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Bundle name of a third-party application |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | No | Call back the screenshot event |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [32100001](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100001-file-creation-failed) | Internal handling failed. |
| [32100005](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100005-unsubscription-failed) | Unsubscribe Failed. Possible causes: &lt;br&gt;1. Abnormal system capability. &lt;br&gt;2. IPC communication abnormality. |

