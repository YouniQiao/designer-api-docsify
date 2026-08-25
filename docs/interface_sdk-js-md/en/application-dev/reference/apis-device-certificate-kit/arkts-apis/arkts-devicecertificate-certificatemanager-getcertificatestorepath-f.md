# getCertificateStorePath

## Modules to Import

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## getCertificateStorePath

```TypeScript
function getCertificateStorePath(property: CertStoreProperty): string
```

Obtains the certificate storage path.

**Since:** 18

**System capability:** SystemCapability.Security.CertificateManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| property | [CertStoreProperty](arkts-devicecertificate-certificatemanager-certstoreproperty-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17500001](../errorcode-certManager.md#17500001-internal-error) |
| [17500009](../errorcode-certManager.md#17500009-specified-certificate-storage-path-not-supported) |
