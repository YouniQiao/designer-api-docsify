# notifyMetadataBindingEvent (System API)

## Modules to Import

```TypeScript
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
```

## notifyMetadataBindingEvent

```TypeScript
function notifyMetadataBindingEvent(bundleName: string): Promise<string>
```

Transfers metadata to the application or service that calls the encoding API. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-metadataBinding-function notifyMetadataBindingEvent(bundleName: string): Promise<string>--><!--Device-metadataBinding-function notifyMetadataBindingEvent(bundleName: string): Promise<string>-End-->

**System capability:** SystemCapability.MultimodalAwareness.MetadataBinding

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [32100001](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100001-file-creation-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName: string = '';
metadataBinding.notifyMetadataBindingEvent(bundleName).then((appLink:string)=>{
  console.info("notify metadata:" + appLink);
}).catch((error: BusinessError) => {
  console.error("notify metadata error" + error);
});
```
