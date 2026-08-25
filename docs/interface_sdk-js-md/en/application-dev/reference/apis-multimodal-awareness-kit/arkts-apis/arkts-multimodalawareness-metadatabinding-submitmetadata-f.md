# submitMetadata

## Modules to Import

```TypeScript
import { metadataBinding } from 'kits/@kit.MultimodalAwarenessKit';
```

## submitMetadata

```TypeScript
function submitMetadata(metadata: string): void
```

Transfers the metadata to be encoded to the MSDP. The MSDP determines whether to transfer the metadata to the system application or service that calls the encoding API.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.MultimodalAwareness.MetadataBinding

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| metadata | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [32100001](../errorcode-metadataBinding.md#32100001-file-creation-failed) |
