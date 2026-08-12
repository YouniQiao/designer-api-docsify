# uninstallAllUserTrustedCertificate (System API)

## Modules to Import

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
```

## uninstallAllUserTrustedCertificate

```TypeScript
function uninstallAllUserTrustedCertificate() : Promise<void>
```

Uninstalls all CA certificates trusted by the user. This API is called only by the certificate management application. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER and ohos.permission.ACCESS_USER_TRUSTED_CERT

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManager-function uninstallAllUserTrustedCertificate() : Promise<void>--><!--Device-certificateManager-function uninstallAllUserTrustedCertificate() : Promise<void>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. &lt;br&gt;The application does not have the permission required to call the API. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [17500001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-device-certificate-kit/errorcode-certManager.md#17500001-internal-error) | Internal error. Possible causes: 1. IPC communication failed; &lt;br&gt;2. Memory operation error; 3. File operation error. Please try again. |

## Examples

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  certificateManager.uninstallAllUserTrustedCertificate().then(() => {
    console.info('Succeeded in uninstalling all user trusted certificates.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to uninstall all user trusted certificates. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error: BusinessError) {
  console.error(`Failed to uninstall all user trusted certificates. Code: ${error.code}, message: ${error.message}`);
}
```

