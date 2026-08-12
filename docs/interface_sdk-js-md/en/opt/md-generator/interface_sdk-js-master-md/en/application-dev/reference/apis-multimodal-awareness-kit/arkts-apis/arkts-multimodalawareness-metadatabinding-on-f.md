# on

## Modules to Import

```TypeScript
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
```

## on('operationSubmitMetadata')

```TypeScript
function on(type: 'operationSubmitMetadata', bundleName: string, callback: Callback<number>): void
```

Subscribes to a system event to obtain the encoded metadata. The application needs to register a callback to return the encoded metadata when the registered system event occurs.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-metadataBinding-function on(type: 'operationSubmitMetadata', bundleName: string, callback: Callback<int>): void--><!--Device-metadataBinding-function on(type: 'operationSubmitMetadata', bundleName: string, callback: Callback<int>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.MetadataBinding

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'operationSubmitMetadata' | Yes |
| bundleName | string | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [32100001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100001-file-creation-failed) |
| [32100004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100004-subscription-failed) |

## Examples

```TypeScript
import { metadataBinding } from '@kit.MultimodalAwarenessKit';

let bundleName: string = '';
try {
  metadataBinding.on('operationSubmitMetadata', bundleName, (event: number) => {
    if (event == 1) {
      console.info("The screenshot request is intercepted and the app link is obtained");
    }
  });
} catch (error) {
  console.error("register screenshot event error");
}
```
