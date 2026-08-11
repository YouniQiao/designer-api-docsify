# installSystemAppCertificate (System API)

## Modules to Import

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## installSystemAppCertificate

```TypeScript
function installSystemAppCertificate(keystore: Uint8Array, keystorePwd: string): Promise<CMResult>
```

Installs the system application credential. This API is called only by the certificate management application. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER and ohos.permission.ACCESS_SYSTEM_APP_CERT

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManager-function installSystemAppCertificate(keystore: Uint8Array, keystorePwd: string): Promise<CMResult>--><!--Device-certificateManager-function installSystemAppCertificate(keystore: Uint8Array, keystorePwd: string): Promise<CMResult>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keystore | Uint8Array | Yes |
| keystorePwd | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;CMResult&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17500008](../errorcode-certManager.md#17500008-incorrect-password) |
| [17500003](../errorcode-certManager.md#17500003-invalid-certificate-or-credential) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17500001](../errorcode-certManager.md#17500001-internal-error) |
| [17500004](../errorcode-certManager.md#17500004-the-number-of-certificates-or-credentials-reaches-the-limit) |

## Examples

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

/* The data of the credential to be installed must be assigned based on the service. The data in this example is not the real credential data. */
let keystore: Uint8Array = new Uint8Array([
    0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01,
]);
let keystorePwd: string = "123456";
try {
  certificateManager.installSystemAppCertificate(keystore, keystorePwd).then((cmResult: certificateManager.CMResult) => {
    let uri: string = (cmResult?.uri == undefined) ? '' : cmResult.uri;
    console.info('Succeeded in installing system app certificate.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to install system app certificate. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to install system app certificate. Code: ${error.code}, message: ${error.message}`);
}
```
