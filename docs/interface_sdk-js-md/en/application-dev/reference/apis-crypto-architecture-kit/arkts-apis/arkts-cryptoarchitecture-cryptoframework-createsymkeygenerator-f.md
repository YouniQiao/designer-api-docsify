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

For details about the supported specifications, see Symmetric Key Generation and Conversion Specifications.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.SymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| algName | string | Yes | Algorithm to be used by the **symKeyGenerator** instance.For details, see **String Parameter** in Symmetric Key Generation and Conversion Specifications. |

**Return value:**

| Type | Description |
| --- | --- |
| [SymKeyGenerator](arkts-cryptoarchitecture-cryptoframework-symkeygenerator-i.md) | Returns the **SymKeyGenerator** instance corresponding to the specified algorithm. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | This operation is not supported. |

**Examples**

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let symKeyGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
```
