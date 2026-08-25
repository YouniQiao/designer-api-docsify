# installUserTrustedCertificateSync

## Modules to Import

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## installUserTrustedCertificateSync

```TypeScript
function installUserTrustedCertificateSync(cert: Uint8Array, certScope: CertScope): CMResult
```

Installs a user CA certificate.

**Since:** 18

**Required permissions:** ohos.permission.ACCESS_ENTERPRISE_USER_TRUSTED_CERT or ohos.permission.ACCESS_USER_TRUSTED_CERT

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17500001](../errorcode-certManager.md#17500001-internal-error) |
| [17500003](../errorcode-certManager.md#17500003-invalid-certificate-or-credential) |
| [17500004](../errorcode-certManager.md#17500004-the-number-of-certificates-or-credentials-reaches-the-limit) |
| [17500007](../errorcode-certManager.md#17500007-device-in-advanced-security-mode) |
