# DHKeyUtil

Generates common parameters for a DH key based on the prime **p** length and the private key length.

**Since:** 11

<!--Device-cryptoFramework-class DHKeyUtil--><!--Device-cryptoFramework-class DHKeyUtil-End-->

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

Generates common parameters for a DH key based on the prime **p** length and the private key length, in bits. For details, see [DH](../../../security/CryptoArchitectureKit/crypto-key-generation-conversion.md#dh).

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DHKeyUtil-static genDHCommonParamsSpec(pLen: int, skLen?: int): DHCommonParamsSpec--><!--Device-DHKeyUtil-static genDHCommonParamsSpec(pLen: int, skLen?: int): DHCommonParamsSpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pLen | number | Yes |
| skLen | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DHCommonParamsSpec](arkts-cryptoarchitecture-cryptoframework-dhcommonparamsspec-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [17630001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## Examples

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
