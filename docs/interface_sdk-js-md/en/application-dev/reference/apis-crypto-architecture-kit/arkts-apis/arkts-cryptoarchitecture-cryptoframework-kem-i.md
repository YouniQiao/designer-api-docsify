# Kem

密钥封装机制（KEM）接口，定义基于密钥封装机制进行密钥封装和解封装的方法。调用前，需通过  
[createKem(algNameId: KemAlgNameId): Kem](arkts-cryptoarchitecture-cryptoframework-createkem-f.md#createkem)方法创建一个Kem实例。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-cryptoFramework-interface Kem--><!--Device-cryptoFramework-interface Kem-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## decapsulate

```TypeScript
decapsulate(priKey: PriKey, wrappedKey: Uint8Array): Promise<Uint8Array>
```

密钥解封装操作。使用接收方的私钥，由接收方执行，从密文中解封装出共享密钥。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Kem-decapsulate(priKey: PriKey, wrappedKey: Uint8Array): Promise<Uint8Array>--><!--Device-Kem-decapsulate(priKey: PriKey, wrappedKey: Uint8Array): Promise<Uint8Array>-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| priKey | [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) | Yes | 接收方的私钥。 |
| wrappedKey | Uint8Array | Yes | KEM封装的密钥。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Uint8Array&gt; | Promise对象，返回共享密钥。 |

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
import { BusinessError } from '@kit.BasicServicesKit';

async function kemDecapsulate() {
  try {
    let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ML-KEM-768');
    let keyPair = await asyKeyGenerator.generateKeyPair();
    let kem = cryptoFramework.createKem(cryptoFramework.KemAlgNameId.ML_KEM_768);
    let encapResult = await kem.encapsulate(keyPair.pubKey, null);
    let sharedSecret = await kem.decapsulate(keyPair.priKey, encapResult.wrappedKey);
    console.info('decapsulate success');
    console.info('sharedSecret length: ' + sharedSecret.length);
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`decapsulate failed: errCode: ${e.code}, errMsg: ${e.message}`);
  }
}
```

## decapsulateSync

```TypeScript
decapsulateSync(priKey: PriKey, wrappedKey: Uint8Array): Uint8Array
```

密钥解封装操作。使用接收方的私钥，由接收方执行，从密文中解封装出共享密钥。

&lt;br&gt;&lt;br&gt;**说明：**&lt;br&gt;建议优先使用异步API，{@link decapsulate}。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。因此建议在子线程中调用同步API，以避免阻塞主线程。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Kem-decapsulateSync(priKey: PriKey, wrappedKey: Uint8Array): Uint8Array--><!--Device-Kem-decapsulateSync(priKey: PriKey, wrappedKey: Uint8Array): Uint8Array-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| priKey | [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) | Yes | 接收方的私钥。 |
| wrappedKey | Uint8Array | Yes | KEM封装的密钥。 |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | 共享密钥。 |

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
import { BusinessError } from '@kit.BasicServicesKit';

function kemDecapsulateSync() {
  try {
    let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ML-KEM-768');
    let keyPair = asyKeyGenerator.generateKeyPairSync();
    let kem = cryptoFramework.createKem(cryptoFramework.KemAlgNameId.ML_KEM_768);
    let encapResult = kem.encapsulateSync(keyPair.pubKey, null);
    let sharedSecret = kem.decapsulateSync(keyPair.priKey, encapResult.wrappedKey);
    console.info('decapsulateSync success');
    console.info('sharedSecret length: ' + sharedSecret.length);
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`decapsulateSync failed: errCode: ${e.code}, errMsg: ${e.message}`);
  }
}
```

## encapsulate

```TypeScript
encapsulate(pubKey: PubKey, ikme: Uint8Array | null): Promise<KemEncapResult>
```

密钥封装操作。使用接收方的公钥，由发送方执行，生成并封装一个共享密钥。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Kem-encapsulate(pubKey: PubKey, ikme: Uint8Array | null): Promise<KemEncapResult>--><!--Device-Kem-encapsulate(pubKey: PubKey, ikme: Uint8Array | null): Promise<KemEncapResult>-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pubKey | [PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md) | Yes | 接收方的公钥。 |
| ikme | Uint8Array \| null | Yes | 随机数种子，用于替代算法内部的随机数。对于ML-KEM算法，随机数种子是32字节。建议传null。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;KemEncapResult&gt; | Promise对象，返回KEM封装结果。 |

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
import { BusinessError } from '@kit.BasicServicesKit';

async function kemEncapsulate() {
  try {
    let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ML-KEM-768');
    let keyPair = await asyKeyGenerator.generateKeyPair();
    let kem = cryptoFramework.createKem(cryptoFramework.KemAlgNameId.ML_KEM_768);
    let encapResult = await kem.encapsulate(keyPair.pubKey, null);
    console.info('encapsulate success');
    console.info('sharedSecret length: ' + encapResult.sharedSecret.length);
    console.info('wrappedKey length: ' + encapResult.wrappedKey.length);
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`encapsulate failed: errCode: ${e.code}, errMsg: ${e.message}`);
  }
}
```

## encapsulateSync

```TypeScript
encapsulateSync(pubKey: PubKey, ikme: Uint8Array | null): KemEncapResult
```

密钥封装操作。使用接收方的公钥，由发送方执行，生成并封装一个共享密钥。

&lt;br&gt;&lt;br&gt;**说明：**&lt;br&gt;建议优先使用异步API，{@link encapsulate}。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。因此建议在子线程中调用同步API，以避免阻塞主线程。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Kem-encapsulateSync(pubKey: PubKey, ikme: Uint8Array | null): KemEncapResult--><!--Device-Kem-encapsulateSync(pubKey: PubKey, ikme: Uint8Array | null): KemEncapResult-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pubKey | [PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md) | Yes | 接收方的公钥。 |
| ikme | Uint8Array \| null | Yes | 随机数种子，用于替代算法内部的随机数。对于ML-KEM算法，随机数种子是32字节。建议传null。 |

**Return value:**

| Type | Description |
| --- | --- |
| [KemEncapResult](arkts-cryptoarchitecture-cryptoframework-kemencapresult-i.md) | KEM封装结果。 |

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
import { BusinessError } from '@kit.BasicServicesKit';

function kemEncapsulateSync() {
  try {
    let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ML-KEM-768');
    let keyPair = asyKeyGenerator.generateKeyPairSync();
    let kem = cryptoFramework.createKem(cryptoFramework.KemAlgNameId.ML_KEM_768);
    let encapResult = kem.encapsulateSync(keyPair.pubKey, null);
    console.info('encapsulateSync success');
    console.info('sharedSecret length: ' + encapResult.sharedSecret.length);
    console.info('wrappedKey length: ' + encapResult.wrappedKey.length);
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`encapsulateSync failed: errCode: ${e.code}, errMsg: ${e.message}`);
  }
}
```

