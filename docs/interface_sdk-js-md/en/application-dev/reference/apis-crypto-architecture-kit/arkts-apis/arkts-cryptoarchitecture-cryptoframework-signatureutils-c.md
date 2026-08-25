# SignatureUtils

Provides utilities for converting ECC/SM2 signature data.

**Since:** 20

**System capability:** SystemCapability.Security.CryptoFramework.Signature

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## genEccSignature

```TypeScript
static genEccSignature(spec: EccSignatureSpec): Uint8Array
```

Converts an ECC/SM2 signature (r, s) to the ASN.1 DER encoding.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Security.CryptoFramework.Signature

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| spec | [EccSignatureSpec](arkts-cryptoarchitecture-cryptoframework-eccsignaturespec-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Error codes:**

| Error Code ID |
| --- |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |

## genEccSignatureSpec

```TypeScript
static genEccSignatureSpec(data: Uint8Array): EccSignatureSpec
```

Generates r and s from the ECC/SM2 signature data in ASN.1 DER encoding.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Security.CryptoFramework.Signature

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | Uint8Array | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [EccSignatureSpec](arkts-cryptoarchitecture-cryptoframework-eccsignaturespec-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
| [17620002](../errorcode-crypto-framework.md#17620002-failed-to-obtain-the-native-object-or-convert-parameters) |
| [17620003](../errorcode-crypto-framework.md#17620003-parameter-check-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
