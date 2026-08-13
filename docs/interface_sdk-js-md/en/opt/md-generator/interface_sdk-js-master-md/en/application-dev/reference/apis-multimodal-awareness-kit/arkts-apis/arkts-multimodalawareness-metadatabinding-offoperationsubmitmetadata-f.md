# offOperationSubmitMetadata

## Modules to Import

```TypeScript
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
```

## offOperationSubmitMetadata

```TypeScript
function offOperationSubmitMetadata(bundleName: string, callback?: Callback<number>): void
```

Unsubscribes from system events that are used to obtain the encoded metadata.

**Since:** 23

**Deprecated since:** -1

<!--Device-metadataBinding-function offOperationSubmitMetadata(bundleName: string, callback?: Callback<int>): void--><!--Device-metadataBinding-function offOperationSubmitMetadata(bundleName: string, callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.MetadataBinding

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [32100001](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100001-file-creation-failed) |
| [32100005](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100005-unsubscription-failed) |
