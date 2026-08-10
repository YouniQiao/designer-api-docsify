# SymKeyGenerator

对称密钥生成器接口，定义生成对称密钥的方法。调用前，需通过  
[createSymKeyGenerator](arkts-cryptoarchitecture-cryptoframework-createsymkeygenerator-f.md#createsymkeygenerator)方法创建一个SymKeyGenerator实例。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface SymKeyGenerator--><!--Device-cryptoFramework-interface SymKeyGenerator-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.SymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## convertKey

```TypeScript
convertKey(key: DataBlob, callback: AsyncCallback<SymKey>): void
```

将指定数据转换为对称密钥。使用callback异步回调。

> **说明：**
> 
> 对于HMAC算法的对称密钥，如果已经在创建对称密钥生成器时指定了具体哈希算法（如指定"HMAC|SHA256"），则需要传入与哈希长度一致的二进制
> 密钥数据（如传入SHA256对应256位的密钥数据）。

如果在创建对称密钥生成器时没有指定具体哈希算法，如仅指定"HMAC"，则支持传入长度在[1,4096]范围内（单位为bytes）的任意二进制密钥数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SymKeyGenerator-convertKey(key: DataBlob, callback: AsyncCallback<SymKey>): void--><!--Device-SymKeyGenerator-convertKey(key: DataBlob, callback: AsyncCallback<SymKey>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.SymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | Yes | 指定的对称密钥材料。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SymKey&gt; | Yes | 回调函数。当生成对称密钥成功时，err为undefined，data为获取到的SymKey；否则为 错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 非法入参。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数验证失败。 |
| 17620001 | 内存操作失败。 |
| 17620003 | 参数检查失败。<br>**Applicable version:** 26.0.0 and later |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function genKeyMaterialBlob(): cryptoFramework.DataBlob {
  let arr = [
    0xba, 0x3d, 0xc2, 0x71, 0x21, 0x1e, 0x30, 0x56,
    0xad, 0x47, 0xfc, 0x5a, 0x46, 0x39, 0xee, 0x7c,
    0xba, 0x3b, 0xc2, 0x71, 0xab, 0xa0, 0x30, 0x72]; // keyLen = 192 (24 bytes)
  let keyMaterial = new Uint8Array(arr);
  return { data: keyMaterial };
}

function testConvertKey() {
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
  let keyMaterialBlob = genKeyMaterialBlob();
  symKeyGenerator.convertKey(keyMaterialBlob, (err, symKey) => {
    console.info('Convert symKey result: success, algName: ' + symKey.algName);
  });
}
```

## convertKey

```TypeScript
convertKey(key: DataBlob): Promise<SymKey>
```

将指定数据转换为对称密钥。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SymKeyGenerator-convertKey(key: DataBlob): Promise<SymKey>--><!--Device-SymKeyGenerator-convertKey(key: DataBlob): Promise<SymKey>-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.SymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | Yes | 指定的密钥材料数据。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;SymKey&gt; | Promise对象，返回对称密钥SymKey。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 非法入参。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数验证失败。 |
| 17620001 | 内存操作失败。 |
| 17620003 | 参数检查失败。<br>**Applicable version:** 26.0.0 and later |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

function genKeyMaterialBlob(): cryptoFramework.DataBlob {
  let arr = [
    0xba, 0x3d, 0xc2, 0x71, 0x21, 0x1e, 0x30, 0x56,
    0xad, 0x47, 0xfc, 0x5a, 0x46, 0x39, 0xee, 0x7c,
    0xba, 0x3b, 0xc2, 0x71, 0xab, 0xa0, 0x30, 0x72]; // keyLen = 192 (24 bytes)
  let keyMaterial = new Uint8Array(arr);
  return { data: keyMaterial };
}

function testConvertKey() {
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
  let keyMaterialBlob = genKeyMaterialBlob();
  symKeyGenerator.convertKey(keyMaterialBlob)
    .then(symKey => {
      console.info('Convert symKey result: success, algName: ' + symKey.algName);
    }).catch((error: BusinessError) => {
      console.error(`Convert symKey failed, ${error.code}, ${error.message}`);
    });
}
```

## convertKeySync

```TypeScript
convertKeySync(key: DataBlob): SymKey
```

将指定数据转换为对称密钥。

> **说明：**
> 
> 对于HMAC算法的对称密钥，如果在创建对称密钥生成器时指定了具体哈希算法（如"HMAC|SHA256"），则需要传入与哈希长度一致的二进制密钥数据
> （如传入SHA256对应的256位密钥数据）。如果在创建对称密钥生成器时未指定具体哈希算法，如仅指定"HMAC"，则支持传入长度在1到4096字节范围
> 内的任意二进制密钥数据。

&lt;br&gt;&lt;br&gt;**说明：**&lt;br&gt;建议优先使用异步API，{@link convertKey}。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。因此建议在子线程中调用同步API，以避免阻塞主线程。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SymKeyGenerator-convertKeySync(key: DataBlob): SymKey--><!--Device-SymKeyGenerator-convertKeySync(key: DataBlob): SymKey-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Key.SymKey

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | Yes | 指定的对称密钥材料。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SymKey](arkts-cryptoarchitecture-cryptoframework-symkey-i.md) | 对称密钥。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 非法入参。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数验证失败。 |
| 17620001 | 内存操作失败。 |
| 17620003 | 参数检查失败。<br>**Applicable version:** 26.0.0 and later |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function testConvertKeySync() {
  // The symmetric key length is 64 bytes (512 bits).
  let keyMessage = '87654321abcdefgh87654321abcdefgh87654321abcdefgh87654321abcdefgh';
  let keyBlob: cryptoFramework.DataBlob = {
    data : new Uint8Array(buffer.from(keyMessage, 'utf-8').buffer)
  }
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('HMAC');
  let key = symKeyGenerator.convertKeySync(keyBlob);
  let encodedKey = key.getEncoded();
  console.info('key encoded data: ' + encodedKey.data);
}
```

## generateSymKey

```TypeScript
generateSymKey(callback: AsyncCallback<SymKey>): void
```

获取对称密钥生成器随机生成的密钥。使用callback异步回调。

&lt;br&gt;目前使用OpenSSL的RAND_priv_bytes()作为底层能力生成随机密钥。

> **说明：**
> 
> 对于HMAC算法的对称密钥，如果在创建对称密钥生成器时指定了具体哈希算法（如"HMAC|SHA256"），则会随机生成与哈希长度一致的二进制密钥
> 数据（如256位的密钥数据）。如果未指定具体哈希算法，如仅指定"HMAC"，则不支持随机生成对称密钥数据，可通过
> [convertKey](arkts-cryptoarchitecture-cryptoframework-symkeygenerator-i.md#convertkey)
> 方式生成对称密钥数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SymKeyGenerator-generateSymKey(callback: AsyncCallback<SymKey>): void--><!--Device-SymKeyGenerator-generateSymKey(callback: AsyncCallback<SymKey>): void-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.SymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SymKey&gt; | Yes | 回调函数。当生成对称密钥成功时，err为undefined，data为获取到的SymKey；否则为 错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17620004 | 无效的函数调用。<br>**Applicable version:** 26.0.0 and later |
| 17620001 | 内存操作失败。 |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let symKeyGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
  symKeyGenerator.generateSymKey((err, symKey) => {
    console.info('Generate symKey result: success, algName: ' + symKey.algName);
  });
```

## generateSymKey

```TypeScript
generateSymKey(): Promise<SymKey>
```

获取该对称密钥生成器随机生成的密钥。使用Promise异步回调。

&lt;br&gt;目前使用OpenSSL的RAND_priv_bytes()作为底层能力生成随机密钥。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SymKeyGenerator-generateSymKey(): Promise<SymKey>--><!--Device-SymKeyGenerator-generateSymKey(): Promise<SymKey>-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.SymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;SymKey&gt; | Promise对象，返回对称密钥SymKey。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17620004 | 无效的函数调用。<br>**Applicable version:** 26.0.0 and later |
| 17620001 | 内存操作失败。 |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  symKeyGenerator.generateSymKey()
    .then(symKey => {
      console.info('Generate symKey result: success, algName: ' + symKey.algName);
    }).catch((error: BusinessError) => {
      console.error(`Generate symKey failed, ${error.code}, ${error.message}`);
    });
```

## generateSymKeySync

```TypeScript
generateSymKeySync(): SymKey
```

同步获取对称密钥生成器随机生成的密钥。

&lt;br&gt;目前使用OpenSSL的RAND_priv_bytes()作为底层能力生成随机密钥。

> **说明：**
> 
> 对于HMAC算法的对称密钥，如果已经在创建对称密钥生成器时指定了具体哈希算法（如指定"HMAC|SHA256"），则会随机生成与哈希长度一致的
> 二进制密钥数据（如指定"HMAC|SHA256"会随机生成256位的密钥数据）。

如果在创建对称密钥生成器时没有指定具体哈希算法，如仅指定"HMAC"，则不支持随机生成对称密钥数据，可通过  
[convertKeySync](arkts-cryptoarchitecture-cryptoframework-symkeygenerator-i.md#convertkeysync)方式生成对称密钥数据。

&lt;br&gt;&lt;br&gt;**说明：**&lt;br&gt;建议优先使用异步API，{@link generateSymKey}。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。因此建议在子线程中调用同步API，以避免阻塞主线程。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SymKeyGenerator-generateSymKeySync(): SymKey--><!--Device-SymKeyGenerator-generateSymKeySync(): SymKey-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Key.SymKey

**Return value:**

| Type | Description |
| --- | --- |
| [SymKey](arkts-cryptoarchitecture-cryptoframework-symkey-i.md) | 返回对称密钥SymKey。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17620004 | 无效的函数调用。<br>**Applicable version:** 26.0.0 and later |
| 17620001 | 内存操作失败。 |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function testGenerateSymKeySync() {
  // Create a SymKeyGenerator instance.
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES256');
  // Use SymKeyGenerator to randomly generate a symmetric key.
  let key = symKeyGenerator.generateSymKeySync();
  let encodedKey = key.getEncoded();
  console.info('key hex:' + encodedKey.data);
}
```

## algName

```TypeScript
readonly algName: string
```

对称密钥生成器指定的算法名称。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SymKeyGenerator-readonly algName: string--><!--Device-SymKeyGenerator-readonly algName: string-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.SymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

