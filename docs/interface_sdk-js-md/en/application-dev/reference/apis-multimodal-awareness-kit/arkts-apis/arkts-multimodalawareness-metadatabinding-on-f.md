# on

## Modules to Import

```TypeScript
import { metadataBinding } from 'kits/@kit.MultimodalAwarenessKit';
```

## on('operationSubmitMetadata')

```TypeScript
function on(type: 'operationSubmitMetadata', bundleName: string, callback: Callback<number>): void
```

Subscribes to a system event to obtain the encoded metadata. The application needs to register a callback to return the encoded metadata when the registered system event occurs.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.MultimodalAwareness.MetadataBinding

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'operationSubmitMetadata' | Yes |
| bundleName | string | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [32100001](../errorcode-metadataBinding.md#32100001-file-creation-failed) |
| [32100004](../errorcode-metadataBinding.md#32100004-subscription-failed) |
