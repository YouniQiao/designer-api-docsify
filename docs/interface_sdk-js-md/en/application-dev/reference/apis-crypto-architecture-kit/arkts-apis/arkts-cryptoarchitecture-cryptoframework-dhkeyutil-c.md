# DHKeyUtil

Generates common parameters for a DH key based on the prime **p** length and the private key length.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-class DHKeyUtil--><!--Device-cryptoFramework-class DHKeyUtil-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

## genDHCommonParamsSpec

ArkTS-Dyn:
```TypeScript
static genDHCommonParamsSpec(pLen: number, skLen?: number): DHCommonParamsSpec
```

ArkTS-Sta:
```TypeScript
static genDHCommonParamsSpec(pLen: int, skLen?: int): DHCommonParamsSpec
```

Generates common parameters for a DH key based on the prime **p** length and the private key length, in bits. For details, see [DH](../../../security/CryptoArchitectureKit/crypto-key-generation-conversion.md#dh).

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DHKeyUtil-static genDHCommonParamsSpec(pLen: int, skLen?: int): DHCommonParamsSpec--><!--Device-DHKeyUtil-static genDHCommonParamsSpec(pLen: int, skLen?: int): DHCommonParamsSpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pLen | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Length of the prime **p**, in bits. |
| skLen | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | Maximum length of the generated DH private key, in bits. The default value is **0**.&lt;br&gt; When this parameter is set to **0**, the maximum length of the generated DH private key is as follows:&lt;br&gt; ffdhe2048: 255 bits.&lt;br&gt;ffdhe3072: 275 bits.&lt;br&gt;ffdhe4096: 325 bits.&lt;br&gt;ffdhe6144: 375 bits.&lt;br&gt;ffdhe8192: 400 bits. |

**Return value:**

| Type | Description |
| --- | --- |
| [DHCommonParamsSpec](arkts-cryptoarchitecture-cryptoframework-dhcommonparamsspec-i.md) | DH common parameters generated. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | This operation is not supported. |
| [17630001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17630001-cryptographic-operation-error) | Crypto operation error. |
| [17620001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |

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

