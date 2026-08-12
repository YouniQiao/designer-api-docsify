# installUserTrustedCertificateSync

## Modules to Import

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
```

## installUserTrustedCertificateSync

```TypeScript
function installUserTrustedCertificateSync(cert: Uint8Array, certScope: CertScope): CMResult
```

Installs a user CA certificate.

**Since:** 18

**Required permissions:** ohos.permission.ACCESS_ENTERPRISE_USER_TRUSTED_CERT or ohos.permission.ACCESS_USER_TRUSTED_CERT

<!--Device-certificateManager-function installUserTrustedCertificateSync(cert: Uint8Array, certScope: CertScope): CMResult--><!--Device-certificateManager-function installUserTrustedCertificateSync(cert: Uint8Array, certScope: CertScope): CMResult-End-->

**System capability:** SystemCapability.Security.CertificateManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cert | Uint8Array | Yes |
| certScope | [CertScope](arkts-devicecertificate-certificatemanager-certscope-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CMResult](arkts-devicecertificate-certificatemanager-cmresult-i.md) |

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

/* The CA certificate data must be assigned by the service. In this example, the data is not CA certificate data. */
let certData: Uint8Array = new Uint8Array([
  0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01,
]);
try {
  let result: certificateManager.CMResult = certificateManager.installUserTrustedCertificateSync(certData, certificateManager.CertScope.CURRENT_USER);
  let certUri = result.uri;
  if (certUri === undefined) {
    console.error("The result of install user trusted certificate is undefined.");
  } else {
    console.info("Succeeded to install user trusted certificate.");
  }
} catch (error) {
  console.error(`Failed to install user trusted certificate. Code: ${error.code}, message: ${error.message}`);
}
```
