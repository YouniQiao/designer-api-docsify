# KeyAgreement

密钥协商接口，定义基于非对称密钥对生成共享密钥的方法。调用前，需通过  
[createKeyAgreement(algName: string): KeyAgreement](arkts-cryptoarchitecture-cryptoframework-createkeyagreement-f.md#createkeyagreement)方法创建一个KeyAgreement实例。

**起始版本：** 9

<!--Device-cryptoFramework-interface KeyAgreement--><!--Device-cryptoFramework-interface KeyAgreement-End-->

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.KeyAgreement
- API版本9-11：SystemCapability.Security.CryptoFramework

## generateSecret

```TypeScript
generateSecret(priKey: PriKey, pubKey: PubKey, callback: AsyncCallback<DataBlob>): void
```

基于传入的私钥与公钥进行密钥协商。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-KeyAgreement-generateSecret(priKey: PriKey, pubKey: PubKey, callback: AsyncCallback<DataBlob>): void--><!--Device-KeyAgreement-generateSecret(priKey: PriKey, pubKey: PubKey, callback: AsyncCallback<DataBlob>): void-End-->

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.KeyAgreement
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| priKey | [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) | 是 |
| pubKey | [PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DataBlob&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |

## generateSecret

```TypeScript
generateSecret(priKey: PriKey, pubKey: PubKey): Promise<DataBlob>
```

基于传入的私钥与公钥进行密钥协商。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-KeyAgreement-generateSecret(priKey: PriKey, pubKey: PubKey): Promise<DataBlob>--><!--Device-KeyAgreement-generateSecret(priKey: PriKey, pubKey: PubKey): Promise<DataBlob>-End-->

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.KeyAgreement
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| priKey | [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) | 是 |
| pubKey | [PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;DataBlob&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |

## generateSecretSync

```TypeScript
generateSecretSync(priKey: PriKey, pubKey: PubKey): DataBlob
```

基于传入的私钥与公钥进行密钥协商，通过同步返回共享密钥。

&lt;br&gt;&lt;br&gt;**说明：**&lt;br&gt;建议优先使用异步API，{@link generateSecret}。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。因此建议在子线程中调用同步API，以避免阻塞主线程。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-KeyAgreement-generateSecretSync(priKey: PriKey, pubKey: PubKey): DataBlob--><!--Device-KeyAgreement-generateSecretSync(priKey: PriKey, pubKey: PubKey): DataBlob-End-->

**系统能力：** SystemCapability.Security.CryptoFramework.KeyAgreement

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| priKey | [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) | 是 |
| pubKey | [PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |

## 示例

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function testGenerateSecret() {
  let eccGen = cryptoFramework.createAsyKeyGenerator('ECC256');
  let globalKeyPair = await eccGen.generateKeyPair();
  let keyAgreement = cryptoFramework.createKeyAgreement('ECC256');
  keyAgreement.generateSecret(globalKeyPair.priKey, globalKeyPair.pubKey, (err, secret) => {
    if (err) {
      console.error(`keyAgreement failed, errCode: ${err.code}, errMsg: ${err.message}`);
      return;
    }
    console.info('keyAgreement output = ' + secret.data);
  });
}
```

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function testGenerateSecret() {
  let eccGen = cryptoFramework.createAsyKeyGenerator('ECC256');
  let globalKeyPair = await eccGen.generateKeyPair();
  let keyAgreement = cryptoFramework.createKeyAgreement('ECC256');
  let keyAgreementPromise = keyAgreement.generateSecret(globalKeyPair.priKey, globalKeyPair.pubKey);
  keyAgreementPromise.then(secret => {
    console.info('keyAgreement output = ' + secret.data);
  }).catch((error: BusinessError) => {
    console.error(`keyAgreement failed: errCode: ${error.code}, errMsg: ${error.message}`);
  });
}
```

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function testGenerateSecretSync() {
  let eccGen = cryptoFramework.createAsyKeyGenerator('ECC256');
  let globalKeyPair = await eccGen.generateKeyPair();
  let keyAgreement = cryptoFramework.createKeyAgreement('ECC256');
  let secret = keyAgreement.generateSecretSync(globalKeyPair.priKey, globalKeyPair.pubKey);
  console.info('[Sync]keyAgreement output = ' + secret.data);
}
```

## algName

```TypeScript
readonly algName: string
```

密钥协商的算法名称。

**类型：** string

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-KeyAgreement-readonly algName: string--><!--Device-KeyAgreement-readonly algName: string-End-->

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.KeyAgreement
- API版本9-11：SystemCapability.Security.CryptoFramework
