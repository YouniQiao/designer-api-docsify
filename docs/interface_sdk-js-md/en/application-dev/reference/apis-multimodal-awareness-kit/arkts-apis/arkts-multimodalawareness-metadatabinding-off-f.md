# off

## Modules to Import

```TypeScript
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
```

## off('operationSubmitMetadata')

```TypeScript
function off(type: 'operationSubmitMetadata', bundleName: string, callback?: Callback<int>): void
```

Unsubscribes from system events that are used to obtain the encoded metadata. The respective callback will be unregistered.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-metadataBinding-function off(type: 'operationSubmitMetadata', bundleName: string, callback?: Callback<int>): void--><!--Device-metadataBinding-function off(type: 'operationSubmitMetadata', bundleName: string, callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.MetadataBinding

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'operationSubmitMetadata' | Yes | Event type. This parameter has a fixed value of **operationSubmitMetadata**, indicating the system application's attempt to obtain the encoded metadata. |
| bundleName | string | Yes | Application bundle name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;int&gt; | No | Callback used to return the encoded metadata. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [32100001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100001-file-creation-failed) | Internal handling failed. |
| [32100005](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100005-unsubscription-failed) | Unsubscribe Failed. Possible causes: &lt;br&gt; 1. Abnormal system capability. &lt;br&gt; 2. IPC communication abnormality. |

## Examples

```TypeScript
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName: string = '';
try {
  metadataBinding.off('operationSubmitMetadata', bundleName, (event: number) => {
  });
} catch (error) {
  console.error("unsubscript screenshot event" + error);
}
```

