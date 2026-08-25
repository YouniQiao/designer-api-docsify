# createCertChainValidator

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## createCertChainValidator

```TypeScript
function createCertChainValidator(algorithm: string): CertChainValidator
```

Creates a **CertChainValidator** object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [algorithm](arkts-devicecertificate-cert-certchainvalidator-i.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CertChainValidator](arkts-devicecertificate-cert-certchainvalidator-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |
