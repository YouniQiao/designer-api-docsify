# off

## Modules to Import

```TypeScript
import { metadataBinding } from 'kits/@kit.MultimodalAwarenessKit';
```

## off('operationSubmitMetadata')

```TypeScript
function off(type: 'operationSubmitMetadata', bundleName: string, callback?: Callback<number>): void
```

Unsubscribes from system events that are used to obtain the encoded metadata. The respective callback will be unregistered.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.MultimodalAwareness.MetadataBinding

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'operationSubmitMetadata' | Yes |
| bundleName | string | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [32100001](../errorcode-metadataBinding.md#32100001-file-creation-failed) |
| [32100005](../errorcode-metadataBinding.md#32100005-unsubscription-failed) |
