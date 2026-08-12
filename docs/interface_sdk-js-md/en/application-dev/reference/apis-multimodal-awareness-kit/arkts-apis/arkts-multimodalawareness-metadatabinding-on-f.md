# on

## Modules to Import

```TypeScript
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
```

## on('operationSubmitMetadata')

```TypeScript
function on(type: 'operationSubmitMetadata', bundleName: string, callback: Callback<int>): void
```

Subscribes to a system event to obtain the encoded metadata. The application needs to register a callback to return the encoded metadata when the registered system event occurs.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-metadataBinding-function on(type: 'operationSubmitMetadata', bundleName: string, callback: Callback<int>): void--><!--Device-metadataBinding-function on(type: 'operationSubmitMetadata', bundleName: string, callback: Callback<int>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.MetadataBinding

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'operationSubmitMetadata' | Yes | Event type. This parameter has a fixed value of **operationSubmitMetadata**, indicating the system application's attempt to obtain the encoded metadata. |
| bundleName | string | Yes | Application bundle name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;int&gt; | Yes | Callback used to return the encoded metadata. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [32100001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100001-file-creation-failed) | Internal handling failed. |
| [32100004](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100004-subscription-failed) | Subscribe Failed. Possible causes: &lt;br&gt;1. Abnormal system capability. &lt;br&gt;2. IPC communication abnormality. &lt;br&gt;3. Algorithm loading exception. |

## Examples

```TypeScript
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
import { BusinessError } from '@kit.BasicServicesKit';

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

