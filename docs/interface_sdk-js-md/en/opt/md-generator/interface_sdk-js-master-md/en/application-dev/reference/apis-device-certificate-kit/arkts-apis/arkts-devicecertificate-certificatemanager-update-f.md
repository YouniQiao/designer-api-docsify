# update

## Modules to Import

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
```

## update

```TypeScript
function update(handle: Uint8Array, data: Uint8Array, callback: AsyncCallback<void>): void
```

Updates the data for the signing or signature verification operation. It needs to be invoked after the init operation to transfer the data to be signed and verified. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

<!--Device-certificateManager-function update(handle: Uint8Array, data: Uint8Array, callback: AsyncCallback<void>): void--><!--Device-certificateManager-function update(handle: Uint8Array, data: Uint8Array, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Security.CertificateManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handle | Uint8Array | Yes |
| data | Uint8Array | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [17500001](../errorcode-certManager.md#17500001-internal-error) |

## Examples

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';

/* cmHandle is the value returned by init(). The value here is only an example. */
let cmHandle: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
let srcData: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
try {
  certificateManager.update(cmHandle, srcData, (err, result) => {
    if (err != null) {
      console.error(`Failed to update. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info('Succeeded in updating.');
    }
  });
} catch (error) {
  console.error(`Failed to update. Code: ${error.code}, message: ${error.message}`);
}
```


## update

```TypeScript
function update(handle: Uint8Array, data: Uint8Array): Promise<void>
```

Updates the data for the signing or signature verification operation. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

<!--Device-certificateManager-function update(handle: Uint8Array, data: Uint8Array): Promise<void>--><!--Device-certificateManager-function update(handle: Uint8Array, data: Uint8Array): Promise<void>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handle | Uint8Array | Yes |
| data | Uint8Array | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [17500001](../errorcode-certManager.md#17500001-internal-error) |

## Examples

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

/* cmHandle is the value returned by init(). The value here is only an example. */
let cmHandle: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
let srcData: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
try {
  certificateManager.update(cmHandle, srcData).then((result) => {
    console.info('Succeeded in updating.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to update. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to update. Code: ${error.code}, message: ${error.message}`);
}
```
