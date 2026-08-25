# parsePkcs12

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## parsePkcs12

```TypeScript
function parsePkcs12(data: Uint8Array, config: Pkcs12ParsingConfig): Pkcs12Data
```

Parses P12.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | Uint8Array | Yes |
| config | [Pkcs12ParsingConfig](arkts-devicecertificate-cert-pkcs12parsingconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Pkcs12Data](arkts-devicecertificate-cert-pkcs12data-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |
| [19030008](../errorcode-cert.md#19030008-incorrect-private-key-password) |


## parsePkcs12

```TypeScript
function parsePkcs12(data: Uint8Array, password: string): Promise<Pkcs12Data>
```

Parses P12. This API uses a promise to return the result.

**Since:** 21

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | Uint8Array | Yes |
| password | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Pkcs12Data](arkts-devicecertificate-cert-pkcs12data-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020003](../errorcode-cert.md#19020003-parameter-check-failure) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |
| [19030008](../errorcode-cert.md#19030008-incorrect-private-key-password) |
