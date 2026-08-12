# createSymKeyGenerator

## Modules to Import

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

## createSymKeyGenerator

```TypeScript
function createSymKeyGenerator(algName: string): SymKeyGenerator
```

Creates a symmetric key generator instance with the specified algorithm.

&lt;br&gt;For details about the supported specifications, see  
[Symmetric Key Generation and Conversion Specifications](../../../security/CryptoArchitectureKit/crypto-key-generation-conversion.md).

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-cryptoFramework-function createSymKeyGenerator(algName: string): SymKeyGenerator--><!--Device-cryptoFramework-function createSymKeyGenerator(algName: string): SymKeyGenerator-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.SymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| algName | string | Yes | Algorithm to be used by the **symKeyGenerator** instance.&lt;br&gt;For details, see **String Parameter** in [Symmetric Key Generation and Conversion Specifications](../../../security/CryptoArchitectureKit/crypto-key-generation-conversion.md) . |

**Return value:**

| Type | Description |
| --- | --- |
| [SymKeyGenerator](arkts-cryptoarchitecture-cryptoframework-symkeygenerator-i.md) | Returns the **SymKeyGenerator** instance corresponding to the specified algorithm. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | This operation is not supported. |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let symKeyGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
```

