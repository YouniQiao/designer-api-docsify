# off

## Modules to Import

```TypeScript
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
```

## off('operationSubmitMetadata')

```TypeScript
function off(type: 'operationSubmitMetadata', bundleName: string, callback?: Callback<number>): void
```

Unsubscribes from system events that are used to obtain the encoded metadata. The respective callback will be unregistered.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-metadataBinding-function off(type: 'operationSubmitMetadata', bundleName: string, callback?: Callback<int>): void--><!--Device-metadataBinding-function off(type: 'operationSubmitMetadata', bundleName: string, callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.MetadataBinding

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'operationSubmitMetadata' | Yes |
| bundleName | string | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [32100001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100001-file-creation-failed) |
| [32100005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100005-unsubscription-failed) |

## Examples

```TypeScript
import { metadataBinding } from '@kit.MultimodalAwarenessKit';

let bundleName: string = '';
try {
  metadataBinding.off('operationSubmitMetadata', bundleName, (event: number) => {
  });
} catch (error) {
  console.error("unsubscript screenshot event" + error);
}
```
