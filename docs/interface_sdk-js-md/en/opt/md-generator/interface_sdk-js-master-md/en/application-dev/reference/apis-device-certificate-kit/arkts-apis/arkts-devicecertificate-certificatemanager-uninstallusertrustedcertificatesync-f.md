# uninstallUserTrustedCertificateSync

## Modules to Import

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
```

## uninstallUserTrustedCertificateSync

```TypeScript
function uninstallUserTrustedCertificateSync(certUri: string): void
```

Uninstalls a user CA certificate.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_ENTERPRISE_USER_TRUSTED_CERT or ohos.permission.ACCESS_USER_TRUSTED_CERT

<!--Device-certificateManager-function uninstallUserTrustedCertificateSync(certUri: string): void--><!--Device-certificateManager-function uninstallUserTrustedCertificateSync(certUri: string): void-End-->

**System capability:** SystemCapability.Security.CertificateManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| certUri | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [17500002](../errorcode-certManager.md#17500002-certificate-not-exist) |
| [17500001](../errorcode-certManager.md#17500001-internal-error) |

## Examples

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';

let certUri: string = "test"; /* The service needs to use the certificate identifier to delete the certificate, which is not elaborated here. */
try {
  certificateManager.uninstallUserTrustedCertificateSync(certUri);
} catch (error) {
  console.error(`Failed to uninstall user trusted certificate. Code: ${error.code}, message: ${error.message}`);
}
```
