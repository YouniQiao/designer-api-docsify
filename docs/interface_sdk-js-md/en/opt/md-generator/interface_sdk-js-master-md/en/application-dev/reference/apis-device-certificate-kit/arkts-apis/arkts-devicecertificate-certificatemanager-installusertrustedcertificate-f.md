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

**Required permissions:** ohos.permission.ACCESS_ENTERPRISE_USER_TRUSTED_CERT or ohos.permission.ACCESS_USER_TRUSTED_CERT

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManager-function installUserTrustedCertificate(certificate: CertBlob) : Promise<CMResult>--><!--Device-certificateManager-function installUserTrustedCertificate(certificate: CertBlob) : Promise<CMResult>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| certificate | [CertBlob](arkts-devicecertificate-certificatemanager-certblob-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[CMResult](arkts-devicecertificate-certificatemanager-cmresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17500003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-certManager.md#17500003-invalid-certificate-or-credential) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [17500001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-certManager.md#17500001-internal-error) |
| [17500007](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-certManager.md#17500007-device-in-advanced-security-mode) |
| [17500004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-certManager.md#17500004-the-number-of-certificates-or-credentials-reaches-the-limit) |

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
  certificateManager.installUserTrustedCertificate(certBlob).then((cmResult) => {
    let uri: string = cmResult.uri ?? '';
    console.info('Succeeded in installing user trusted certificate.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to install user trusted certificate. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to install user trusted certificate. Code: ${error.code}, message: ${error.message}`);
}
```
