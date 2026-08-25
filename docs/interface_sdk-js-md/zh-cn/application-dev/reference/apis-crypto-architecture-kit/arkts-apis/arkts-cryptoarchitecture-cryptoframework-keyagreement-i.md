# KeyAgreement

密钥协商接口，定义基于非对称密钥对生成共享密钥的方法。调用前，需通过 [createKeyAgreement(algName: string): KeyAgreement](arkts-cryptoarchitecture-cryptoframework-createkeyagreement-f.md)方法创建一个 KeyAgreement实例。

**起始版本：** 9

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.KeyAgreement
- API版本9-11：SystemCapability.Security.CryptoFramework

## 导入模块

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## generateSecret

```TypeScript
generateSecret(priKey: PriKey, pubKey: PubKey, callback: AsyncCallback<DataBlob>): void
```

基于传入的私钥与公钥进行密钥协商。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.KeyAgreement
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) | 是 |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DataBlob&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## generateSecret

```TypeScript
generateSecret(priKey: PriKey, pubKey: PubKey): Promise<DataBlob>
```

基于传入的私钥与公钥进行密钥协商。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.KeyAgreement
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) | 是 |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;DataBlob & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## generateSecretSync

```TypeScript
generateSecretSync(priKey: PriKey, pubKey: PubKey): DataBlob
```

基于传入的私钥与公钥进行密钥协商，通过同步返回共享密钥。

**说明：** 建议优先使用异步API，generateSecret。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。 因此建议在子线程中调用同步API，以避免阻塞主线程。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.KeyAgreement

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) | 是 |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## algName

```TypeScript
readonly algName: string
```

密钥协商的算法名称。

**类型：** string

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.KeyAgreement
- API版本9-11：SystemCapability.Security.CryptoFramework
