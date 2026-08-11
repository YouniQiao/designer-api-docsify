# uninstallAllUserTrustedCertificate (System API)

## Modules to Import

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## uninstallAllUserTrustedCertificate

```TypeScript
function uninstallAllUserTrustedCertificate() : Promise<void>
```

Uninstalls all CA certificates trusted by the user. This API is called only by the certificate management application. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER and ohos.permission.ACCESS_USER_TRUSTED_CERT

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManager-function uninstallAllUserTrustedCertificate() : Promise<void>--><!--Device-certificateManager-function uninstallAllUserTrustedCertificate() : Promise<void>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17500001](../errorcode-certManager.md#17500001-internal-error) |

## Examples

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  certificateManager.uninstallAllUserTrustedCertificate().then(() => {
    console.info('Succeeded in uninstalling all user trusted certificates.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to uninstall all user trusted certificates. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to uninstall all user trusted certificates. Code: ${error.code}, message: ${error.message}`);
}
```
