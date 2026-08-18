# removeGrantedPublicCertificate (System API)

## Modules to Import

```TypeScript
```

## removeGrantedPublicCertificate

```TypeScript
function removeGrantedPublicCertificate(keyUri: string, clientAppUid: number) : Promise<void>
```

Removes the permission for an application to use the public credentials of a user. This API is called only by the certificate management application. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER and ohos.permission.ACCESS_CERT_MANAGER_INTERNAL

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManager-function removeGrantedPublicCertificate(keyUri: string, clientAppUid: int) : Promise<void>--><!--Device-certificateManager-function removeGrantedPublicCertificate(keyUri: string, clientAppUid: int) : Promise<void>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyUri | string | Yes |
| clientAppUid | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [17500002](../errorcode-certManager.md#17500002-certificate-not-exist) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17500001](../errorcode-certManager.md#17500001-internal-error) |

**Examples**

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let keyUri: string = 'test'; /* Unique identifier of the user public credential. */
let clientAppUid: number = 1001; /* Application UID */
try {
  certificateManager.removeGrantedPublicCertificate(keyUri, clientAppUid).then(() => {
    console.info('Succeeded in removing granted public certificate.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to remove granted public certificate. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to remove granted public certificate. Code: ${error.code}, message: ${error.message}`);
}
```
