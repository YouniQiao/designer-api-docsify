# SM2CryptoUtil

Provides APIs for SM2 cryptographic operations.

**Since:** 23

**Deprecated since:** -1

<!--Device-cryptoFramework-class SM2CryptoUtil--><!--Device-cryptoFramework-class SM2CryptoUtil-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

## Modules to Import

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

## genCipherTextBySpec

```TypeScript
static genCipherTextBySpec(spec: SM2CipherTextSpec, mode?: string): DataBlob
```

Generates SM2 ciphertext in ASN.1 format.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SM2CryptoUtil-static genCipherTextBySpec(spec: SM2CipherTextSpec, mode?: string): DataBlob--><!--Device-SM2CryptoUtil-static genCipherTextBySpec(spec: SM2CipherTextSpec, mode?: string): DataBlob-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| spec | [SM2CipherTextSpec](arkts-cryptoarchitecture-cryptoframework-sm2ciphertextspec-i.md) | Yes |
| mode | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## getCipherTextSpec

```TypeScript
static getCipherTextSpec(cipherText: DataBlob, mode?: string): SM2CipherTextSpec
```

Obtains SM2 ciphertext parameters from the SM2 ciphertext in ASN.1 format.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SM2CryptoUtil-static getCipherTextSpec(cipherText: DataBlob, mode?: string): SM2CipherTextSpec--><!--Device-SM2CryptoUtil-static getCipherTextSpec(cipherText: DataBlob, mode?: string): SM2CipherTextSpec-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cipherText | [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | Yes |
| mode | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SM2CipherTextSpec](arkts-cryptoarchitecture-cryptoframework-sm2ciphertextspec-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |
