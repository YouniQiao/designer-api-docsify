# PubKey

公钥，是[Key](arkts-cryptoarchitecture-cryptoframework-key-i.md)的子类，在非对称加密、签名验证、密钥协商时需要将其对象作为输入使用。

&lt;br&gt;公钥可以通过非对称密钥生成器[AsyKeyGenerator](arkts-cryptoarchitecture-cryptoframework-asykeygenerator-i.md)、  
[AsyKeyGeneratorBySpec](arkts-cryptoarchitecture-cryptoframework-asykeygeneratorbyspec-i.md)来生成。

**Inheritance/Implementation:** PubKey extends [Key](arkts-cryptoarchitecture-cryptoframework-key-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface PubKey extends Key--><!--Device-cryptoFramework-interface PubKey extends Key-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## getAsyKeySpec

ArkTS-Dyn:
```TypeScript
getAsyKeySpec(itemType: AsyKeySpecItem): bigint | string | number
```

ArkTS-Sta:
```TypeScript
getAsyKeySpec(itemType: AsyKeySpecItem): bigint | string | int
```

获取密钥参数。此API以同步方式返回结果。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PubKey-getAsyKeySpec(itemType: AsyKeySpecItem): bigint | string | int--><!--Device-PubKey-getAsyKeySpec(itemType: AsyKeySpecItem): bigint | string | int-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| itemType | [AsyKeySpecItem](arkts-cryptoarchitecture-cryptoframework-asykeyspecitem-e.md) | Yes | 指定的密钥参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| bigint | 获取的密钥参数内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 非法入参。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数验证失败。 |
| 801 | 该操作不支持。<br>**Applicable version:** 12 and later |
| 17630001 | 密码操作错误。 |
| 17620001 | 内存操作失败。 |
| 17620003 | 参数检查失败。<br>**Applicable version:** 26.0.0 and later |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// Construct the EccCommonSpec struct, which defines the common parameters of the ECC public and private keys.
function genEccCommonSpec(): cryptoFramework.ECCCommonParamsSpec {
  let fieldFp: cryptoFramework.ECFieldFp = {
    fieldType: 'Fp',
    p: BigInt('0xffffffffffffffffffffffffffffffff000000000000000000000001')
  }
  let G: cryptoFramework.Point = {
    x: BigInt('0xb70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21'),
    y: BigInt('0xbd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34')
  }
  let eccCommonSpec: cryptoFramework.ECCCommonParamsSpec = {
    algName: 'ECC',
    specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC,
    field: fieldFp,
    a: BigInt('0xfffffffffffffffffffffffffffffffefffffffffffffffffffffffe'),
    b: BigInt('0xb4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4'),
    g: G,
    n: BigInt('0xffffffffffffffffffffffffffff16a2e0b8f03e13dd29455c5c2a3d'),
    h: 1
  }
  return eccCommonSpec;
}

async function testgetAsyKeySpec() {
  let commKeySpec = genEccCommonSpec(); // Construct the EccCommonSpec object.
  let generatorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(commKeySpec); // Create an AsyKeyGenerator instance based on the EccCommonSpec object.
  let keyPair = await generatorBySpec.generateKeyPair();
  let key = keyPair.pubKey;
  let p = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_FP_P_BN);
  console.info('ecc item --- p: ' + p.toString(16));
}
```

## getEncodedDer

```TypeScript
getEncodedDer(format: string): DataBlob
```

支持根据指定的密钥格式（如规范、压缩状态等），获取符合ASN.1语法和DER编码的公钥数据。

> **说明：**
> 
> 本接口和[Key.getEncoded()](arkts-cryptoarchitecture-cryptoframework-key-i.md#getencoded)的区别是：
> 1. 本接口可以指定获取密钥数据的格式。
> 2. [Key.getEncoded()](arkts-cryptoarchitecture-cryptoframework-key-i.md#getencoded)不支持指定获取密钥数据的格式。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PubKey-getEncodedDer(format: string): DataBlob--><!--Device-PubKey-getEncodedDer(format: string): DataBlob-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| format | string | Yes | 用于指定当前密钥格式。支持EC密钥，format取值支持"X509\|COMPRESSED"和"X509\|UNCOMPRESSED"。 &lt;br&gt;从API版本26.0.0开始，支持RSA密钥，format取值支持"PKCS1"和"X509"。 &lt;br&gt;从API版本26.0.0开始，支持ML-DSA和ML-KEM密钥，format取值支持"X509"。 |

**Return value:**

| Type | Description |
| --- | --- |
| [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | DER编码的公钥数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 非法入参。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数验证失败。 |
| 17630001 | 密码操作错误。 |
| 17620001 | 内存操作失败。 |
| 17620003 | 参数检查失败。<br>**Applicable version:** 26.0.0 and later |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function testGetEncodedDer() {
  let pkData = new Uint8Array([48, 90, 48, 20, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 9, 43, 36, 3, 3, 2, 8, 1, 1, 7, 3, 66, 0, 4, 143, 39, 57, 249, 145, 50, 63, 222, 35, 70, 178, 121, 202, 154, 21, 146, 129, 75, 76, 63, 8, 195, 157, 111, 40, 217, 215, 148, 120, 224, 205, 82, 83, 92, 185, 21, 211, 184, 5, 19, 114, 33, 86, 85, 228, 123, 242, 206, 200, 98, 178, 184, 130, 35, 232, 45, 5, 202, 189, 11, 46, 163, 156, 152]);
  let pubKeyBlob: cryptoFramework.DataBlob = { data: pkData };
  let generator = cryptoFramework.createAsyKeyGenerator('ECC_BrainPoolP256r1');
  let keyPair = await generator.convertKey(pubKeyBlob, null);
  let key = keyPair.pubKey;
  let returnBlob = key.getEncodedDer('X509|UNCOMPRESSED');
  console.info('returnBlob data: ' + returnBlob.data);
}
```

## getEncodedPem

```TypeScript
getEncodedPem(format: string): string
```

获取PEM编码的密钥数据。此API以同步方式返回结果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PubKey-getEncodedPem(format: string): string--><!--Device-PubKey-getEncodedPem(format: string): string-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| format | string | Yes | 指定的获取密钥字符串的编码格式。支持RSA密钥，format取值支持"X509"或"PKCS1"。 &lt;br&gt;自API版本26.0.0起，支持EC、ML-DSA和ML-KEM密钥，format取值支持"X509"。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | PEM编码的公钥数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 非法入参。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数验证失败。 |
| 17630001 | 密码操作错误。 |
| 17620001 | 内存操作失败。 |
| 17620003 | 参数检查失败。<br>**Applicable version:** 26.0.0 and later |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let publicPkcs1Str1024: string =
  '-----BEGIN RSA PUBLIC KEY-----\n'
    + 'MIGJAoGBALAg3eavbX433pOjGdWdpL7HIr1w1EAeIcaCtuMfDpECPdX6X5ZjrwiE\n'
    + 'h7cO51WXMT2gyN45DCQySr/8cLE2UiUVHo7qlrSatdLA9ETtgob3sJ4qTaBg5Lxg\n'
    + 'SHy2gC+bvEpuIuRe64yXGuM/aP+ZvmIj9QBIVI9mJD8jLEOvQBBpAgMBAAE=\n'
    + '-----END RSA PUBLIC KEY-----\n';

function TestPubKeyPkcs1ToX509BySync1024() {
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let keyPair = rsaGenerator.convertPemKeySync(publicPkcs1Str1024, null);
  let pubPemKey = keyPair.pubKey;
  let pubString = pubPemKey.getEncodedPem('X509');
  console.info('[sync]TestPubKeyPkcs1ToX509BySync1024 pubString output = ' + pubString);
}
```

## getKeyData

```TypeScript
getKeyData(itemType: AsyKeyDataItem): Promise<Uint8Array>
```

获取指定的密钥数据类型对应的公钥数据。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-PubKey-getKeyData(itemType: AsyKeyDataItem): Promise<Uint8Array>--><!--Device-PubKey-getKeyData(itemType: AsyKeyDataItem): Promise<Uint8Array>-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| itemType | [AsyKeyDataItem](arkts-cryptoarchitecture-cryptoframework-asykeydataitem-e.md) | Yes | 指定密钥数据项类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Uint8Array&gt; | Promise对象，返回指定密钥数据项类型的公钥数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17630001 | 密码操作错误。 |
| 17620001 | 内存操作失败。 |
| 17620002 | 获取Native对象失败或参数转换失败。 |
| 17620003 | 参数检查失败。 |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function eccGetKeyDataTest() {
  let eccGenerator = cryptoFramework.createAsyKeyGenerator('ECC_BrainPoolP256r1');
  let keyPair = await eccGenerator.generateKeyPair();
  let returnBlob = await keyPair.pubKey.getKeyData(cryptoFramework.AsyKeyDataItem.EC_PUBLIC_X_Y);
  console.info('EC_PUBLIC_X_Y data: ' + returnBlob);
}
```

## getKeyDataSync

```TypeScript
getKeyDataSync(itemType: AsyKeyDataItem): Uint8Array
```

获取指定的密钥数据类型对应的公钥数据。此API以同步方式返回结果。

&lt;br&gt;&lt;br&gt;**说明：**&lt;br&gt;建议优先使用异步API，{@link getKeyData}。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。因此建议在子线程中调用同步API，以避免阻塞主线程。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-PubKey-getKeyDataSync(itemType: AsyKeyDataItem): Uint8Array--><!--Device-PubKey-getKeyDataSync(itemType: AsyKeyDataItem): Uint8Array-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| itemType | [AsyKeyDataItem](arkts-cryptoarchitecture-cryptoframework-asykeydataitem-e.md) | Yes | 指定密钥数据项类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | 返回指定密钥数据项类型的公钥数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17630001 | 密码操作错误。 |
| 17620001 | 内存操作失败。 |
| 17620002 | 获取Native对象失败或参数转换失败。 |
| 17620003 | 参数检查失败。 |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function eccGetKeyDataTest() {
  let eccGenerator = cryptoFramework.createAsyKeyGenerator('ECC_BrainPoolP256r1');
  let keyPair = eccGenerator.generateKeyPairSync();
  let returnBlob = keyPair.pubKey.getKeyDataSync(cryptoFramework.AsyKeyDataItem.EC_PUBLIC_X_Y);
  console.info('EC_PUBLIC_X_Y data: ' + returnBlob);
}
```

