# installUserTrustedCertificate

## Modules to Import

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
```

## installUserTrustedCertificate

```TypeScript
function installUserTrustedCertificate(certificate: CertBlob) : Promise<CMResult>
```

Install the user CA certificate. Use Promise asynchronous callback.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_ENTERPRISE_USER_TRUSTED_CERT or ohos.permission.ACCESS_USER_TRUSTED_CERT

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManager-function installUserTrustedCertificate(certificate: CertBlob) : Promise<CMResult>--><!--Device-certificateManager-function installUserTrustedCertificate(certificate: CertBlob) : Promise<CMResult>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| certificate | CertBlob | Yes | Certificate information. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[CMResult](arkts-devicecertificate-certificatemanager-cmresult-i.md)&gt; | Promise used to return the operation result, that is, **uri** in the [CMResult]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter verification failed. Possible causes: &lt;br&gt;the certData parameter is empty or exceeds the maximum length . |
| [17500003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-device-certificate-kit/errorcode-certManager.md#17500003-invalid-certificate-or-credential) | Indicates that the certificate is in an invalid format. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. &lt;br&gt;The application does not have the permission required to call the API. |
| [17500001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-device-certificate-kit/errorcode-certManager.md#17500001-internal-error) | Internal error. Possible causes: 1. IPC communication failed; &lt;br&gt;2. Memory operation error; 3. File operation error. Please try again. |
| [17500007](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-device-certificate-kit/errorcode-certManager.md#17500007-device-in-advanced-security-mode) | Indicates that the device enters advanced security mode. &lt;br&gt;In this mode, the user CA certificate cannot be installed. |
| [17500004](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-device-certificate-kit/errorcode-certManager.md#17500004-the-number-of-certificates-or-credentials-reaches-the-limit) | Indicates that the number of certificates reaches the maximum allowed. |

## Examples

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

/* The CA certificate data must be assigned by the service. In this example, the data is not CA certificate data. */
let certData: Uint8Array = new Uint8Array([
    0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01,
]);
try {
    let certBlob: certificateManager.CertBlob = {
        certData: certData,
        certFormat: certificateManager.CertFileFormat.PEM_DER,
        certScope: certificateManager.CertScope.CURRENT_USER
    };
    certificateManager.installUserTrustedCertificate(certBlob).then((cmResult: certificateManager.CMResult) => {
        let uri: string = (cmResult?.uri == undefined) ? '' : cmResult.uri;
        console.info('Succeeded in installing user trusted certificate.');
    }).catch((err: BusinessError) => {
        console.error(`Failed to install user trusted certificate. Code: ${err.code}, message: ${err.message}`);
    })
} catch (error: BusinessError) {
    console.error(`Failed to install user trusted certificate. Code: ${error.code}, message: ${error.message}`);
}
```

