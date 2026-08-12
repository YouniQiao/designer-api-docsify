# setCertificateStatus (System API)

## Modules to Import

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
```

## setCertificateStatus

```TypeScript
function setCertificateStatus(certUri: string, certType: CertType, enabled: boolean) : Promise<void>
```

Sets the status of a CA certificate. Currently, only the status of a user's CA certificate can be set. This API is called only by the certificate management application. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER and ohos.permission.ACCESS_USER_TRUSTED_CERT

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManager-function setCertificateStatus(certUri: string, certType: CertType, enabled: boolean) : Promise<void>--><!--Device-certificateManager-function setCertificateStatus(certUri: string, certType: CertType, enabled: boolean) : Promise<void>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| certUri | string | Yes | Unique identifier of the certificate. Currently, only user CA certificates are supported. |
| certType | CertType | Yes | Certificate type. Currently, only the status of user CA certificates ( **CA_CERT_USER**) can be set. |
| enabled | boolean | Yes | Whether the certificate is enabled. **true**: enabled; **false**: disabled. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter verification failed. &lt;br&gt;Possible causes: the URI is null or the URI format is wrong, &lt;br&gt; the certType's value is invalid or not supported. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. &lt;br&gt;The application does not have the permission required to call the API. |
| [17500002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-device-certificate-kit/errorcode-certManager.md#17500002-certificate-not-exist) | The certificate does not exist. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [17500001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-device-certificate-kit/errorcode-certManager.md#17500001-internal-error) | Internal error. Possible causes: 1. IPC communication failed; &lt;br&gt;2. Memory operation error; 3. File operation error. Please try again. |

## Examples

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let certUri: string = 'test'; /* Unique identifier of the user CA certificate. */
try {
  /* Set the user CA certificate status to enabled. */
  certificateManager.setCertificateStatus(certUri, certificateManager.CertType.CA_CERT_USER, true).then(() => {
    console.info('Succeeded in setting certificate status.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set certificate status. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error: BusinessError) {
  console.error(`Failed to set certificate status. Code: ${error.code}, message: ${error.message}`);
}
```

