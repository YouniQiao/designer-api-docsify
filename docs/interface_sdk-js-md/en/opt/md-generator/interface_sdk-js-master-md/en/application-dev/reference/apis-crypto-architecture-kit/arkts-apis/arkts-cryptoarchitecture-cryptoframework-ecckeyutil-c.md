# ECCKeyUtil

Provides utilities for ECC key parameter generation and point conversion based on the specified elliptic curve.

**Since:** 11

<!--Device-cryptoFramework-class ECCKeyUtil--><!--Device-cryptoFramework-class ECCKeyUtil-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## convertPoint

```TypeScript
static convertPoint(curveName: string, encodedPoint: Uint8Array): Point
```

Converts the specified point data into a **Point** object based on the curve name (NID). Currently, compressed and uncompressed point data is supported.

> **NOTE：**
> 
> According to section 2.2 in RFC 5480:
> 1. The uncompressed point data is represented as **0x04**|x coordinate|y coordinate.
> 2. The compressed point data in the **Fp** field (the **F2m** field is not supported currently) is represented
> as follows: **0x03**|x coordinate (when the coordinate y is an odd number); **0x02**|x coordinate (when the
> coordinate y is an even number).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ECCKeyUtil-static convertPoint(curveName: string, encodedPoint: Uint8Array): Point--><!--Device-ECCKeyUtil-static convertPoint(curveName: string, encodedPoint: Uint8Array): Point-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| curveName | string | Yes |
| encodedPoint | Uint8Array | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Point](../../apis-test-kit/arkts-apis/arkts-test-uitest-point-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// Randomly generated uncompressed point data.
let pkData =
  new Uint8Array([4, 143, 39, 57, 249, 145, 50, 63, 222, 35, 70, 178, 121, 202, 154, 21, 146, 129, 75, 76, 63, 8, 195,
    157, 111, 40, 217, 215, 148, 120, 224, 205, 82, 83, 92, 185, 21, 211, 184, 5, 19, 114, 33, 86, 85, 228, 123, 242,
    206, 200, 98, 178, 184, 130, 35, 232, 45, 5, 202, 189, 11, 46, 163, 156, 152]);
let returnPoint = cryptoFramework.ECCKeyUtil.convertPoint('NID_brainpoolP256r1', pkData);
console.info('returnPoint: ' + returnPoint.x.toString(16));
```

## genECCCommonParamsSpec

```TypeScript
static genECCCommonParamsSpec(curveName: string): ECCCommonParamsSpec
```

Generates common parameters for an asymmetric key pair based on the specified name identifier (NID) of an elliptic curve. For details, see  
[ECC](../../../security/CryptoArchitectureKit/crypto-key-generation-conversion.md#ecc) and  
[SM2](../../../security/CryptoArchitectureKit/crypto-key-generation-conversion.md#sm2).

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ECCKeyUtil-static genECCCommonParamsSpec(curveName: string): ECCCommonParamsSpec--><!--Device-ECCKeyUtil-static genECCCommonParamsSpec(curveName: string): ECCCommonParamsSpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| curveName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ECCCommonParamsSpec](arkts-cryptoarchitecture-cryptoframework-ecccommonparamsspec-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let ECCCommonParamsSpec = cryptoFramework.ECCKeyUtil.genECCCommonParamsSpec('NID_brainpoolP160r1');
  console.info('genECCCommonParamsSpec result: success.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`genECCCommonParamsSpec failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```

## getEncodedPoint

```TypeScript
static getEncodedPoint(curveName: string, point: Point, format: string): Uint8Array
```

Obtains the point data in the specified format from a **Point** object. Currently, compressed and uncompressed point data is supported.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ECCKeyUtil-static getEncodedPoint(curveName: string, point: Point, format: string): Uint8Array--><!--Device-ECCKeyUtil-static getEncodedPoint(curveName: string, point: Point, format: string): Uint8Array-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| curveName | string | Yes |
| point | [Point](../../apis-test-kit/arkts-apis/arkts-test-uitest-point-i.md) | Yes |
| format | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17630001](../errorcode-crypto-framework.md#17630001-cryptographic-operation-error) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function doTest() {
  let generator = cryptoFramework.createAsyKeyGenerator('ECC_BrainPoolP256r1');
  let keyPair = await generator.generateKeyPair();
  let eccPkX = keyPair.pubKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_PK_X_BN);
  let eccPkY = keyPair.pubKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_PK_Y_BN);
  console.info('ECC_PK_X_BN 16: ' + eccPkX.toString(16));
  console.info('ECC_PK_Y_BN 16: ' + eccPkY.toString(16));
  // Place eccPkX.toString(16) in x and eccPkY.toString(16) in y.
  let returnPoint: cryptoFramework.Point = {
    x: BigInt('0x' + eccPkX.toString(16)),
    y: BigInt('0x' + eccPkY.toString(16))
  };
  let returnData = cryptoFramework.ECCKeyUtil.getEncodedPoint('NID_brainpoolP256r1', returnPoint, 'UNCOMPRESSED');
  console.info('returnData: ' + returnData);
}
```
