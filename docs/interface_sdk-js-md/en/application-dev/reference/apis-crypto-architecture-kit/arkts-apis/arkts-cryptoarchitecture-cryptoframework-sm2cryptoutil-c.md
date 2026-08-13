# SM2CryptoUtil

Provides APIs for SM2 cryptographic operations.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

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

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SM2CryptoUtil-static genCipherTextBySpec(spec: SM2CipherTextSpec, mode?: string): DataBlob--><!--Device-SM2CryptoUtil-static genCipherTextBySpec(spec: SM2CipherTextSpec, mode?: string): DataBlob-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| spec | [SM2CipherTextSpec](arkts-cryptoarchitecture-cryptoframework-sm2ciphertextspec-i.md) | Yes | SM2 ciphertext parameters. |
| mode | string | No | Order of the SM2 parameters in the ciphertext. Currently, only C1C3C2 is supported. If this parameter is left empty or is an empty string, the default value is used. |

**Return value:**

| Type | Description |
| --- | --- |
| DataBlob | SM2 ciphertext in ASN.1 format. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |

## getCipherTextSpec

```TypeScript
static getCipherTextSpec(cipherText: DataBlob, mode?: string): SM2CipherTextSpec
```

Obtains SM2 ciphertext parameters from the SM2 ciphertext in ASN.1 format.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SM2CryptoUtil-static getCipherTextSpec(cipherText: DataBlob, mode?: string): SM2CipherTextSpec--><!--Device-SM2CryptoUtil-static getCipherTextSpec(cipherText: DataBlob, mode?: string): SM2CipherTextSpec-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cipherText | DataBlob | Yes | SM2 ciphertext in ASN.1 format. |
| mode | string | No | Order of the SM2 parameters in the ciphertext. Currently, only C1C3C2 is supported. If this parameter is left empty or is an empty string, the default value is used. |

**Return value:**

| Type | Description |
| --- | --- |
| [SM2CipherTextSpec](arkts-cryptoarchitecture-cryptoframework-sm2ciphertextspec-i.md) | SM2 ciphertext parameters obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |

