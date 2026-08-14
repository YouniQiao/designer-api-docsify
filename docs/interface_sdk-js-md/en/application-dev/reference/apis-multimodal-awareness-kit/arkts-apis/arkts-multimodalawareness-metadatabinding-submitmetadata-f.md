# submitMetadata

## Modules to Import

```TypeScript
import { metadataBinding } from 'metadataBinding';
```

## submitMetadata

```TypeScript
function submitMetadata(metadata: string): void
```

Transfers the metadata to be encoded to the MSDP. The MSDP determines whether to transfer the metadata to the system application or service that calls the encoding API.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-metadataBinding-function submitMetadata(metadata: string): void--><!--Device-metadataBinding-function submitMetadata(metadata: string): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.MetadataBinding

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| metadata | string | Yes | Metadata to be encoded. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [32100001](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100001-file-creation-failed) | Internal handling failed. |

## Examples

```TypeScript
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
import { BusinessError } from '@kit.BasicServicesKit';

let metadata: string = "";
try {
  metadataBinding.submitMetadata(metadata);
} catch (error) {
  console.error("submit metadata error" + error);
}
```

