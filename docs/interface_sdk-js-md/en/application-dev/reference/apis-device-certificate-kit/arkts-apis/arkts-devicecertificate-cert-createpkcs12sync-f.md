# createPkcs12Sync

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## createPkcs12Sync

```TypeScript
function createPkcs12Sync(data: Pkcs12Data, config: Pkcs12CreationConfig): Uint8Array
```

Creates P12. This API returns the result synchronously.

**Since:** 21

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [Pkcs12Data](arkts-devicecertificate-cert-pkcs12data-i.md) | Yes |
| config | [Pkcs12CreationConfig](arkts-devicecertificate-cert-pkcs12creationconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020003](../errorcode-cert.md#19020003-parameter-check-failure) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |
