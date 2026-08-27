# DHKeyUtil

Generates common parameters for a DH key based on the prime **p** length and the private key length.

**Since:** 11

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

## genDHCommonParamsSpec

```TypeScript
static genDHCommonParamsSpec(pLen: number, skLen?: number): DHCommonParamsSpec
```

Generates common parameters for a DH key based on the prime **p** length and the private key length, in bits. For details, see DH.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pLen | number | Yes | Length of the prime **p**, in bits. |
| skLen | number | No | Maximum length of the generated DH private key, in bits. The default value is **0**.When this parameter is set to **0**, the maximum length of the generated DH private key is as follows:ffdhe2048: 255 bits.ffdhe3072: 275 bits.ffdhe4096: 325 bits.ffdhe6144: 375 bits.ffdhe8192: 400 bits. |

**Return value:**

| Type | Description |
| --- | --- |
| [DHCommonParamsSpec](arkts-cryptoarchitecture-cryptoframework-dhcommonparamsspec-i.md) | DH common parameters generated. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | This operation is not supported. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |

**Examples**

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let DHCommonParamsSpec = cryptoFramework.DHKeyUtil.genDHCommonParamsSpec(2048);
  console.info('genDHCommonParamsSpec result: success.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`genDHCommonParamsSpec failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```
