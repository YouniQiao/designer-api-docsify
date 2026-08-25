# Md

消息摘要接口，定义计算消息摘要的方法。调用前，需通过[createMd](arkts-cryptoarchitecture-cryptoframework-createmd-f.md)方法创建一个Md实例。

**起始版本：** 9

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.MessageDigest
- API版本9-11：SystemCapability.Security.CryptoFramework

## 导入模块

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## digest

```TypeScript
digest(callback: AsyncCallback<DataBlob>): void
```

返回Md的计算结果。使用callback异步回调。

**起始版本：** 9

**模型约束：** 
- API版本12+：此接口可在Stage模型和FA模型下使用。
- API版本9-11：此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.MessageDigest
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DataBlob&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## digest

```TypeScript
digest(): Promise<DataBlob>
```

生成消息摘要。使用Promise异步回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.MessageDigest
- API版本9-11：SystemCapability.Security.CryptoFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;DataBlob & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## digestSync

```TypeScript
digestSync(): DataBlob
```

生成消息摘要，通过同步方式返回摘要计算结果。

**说明：** 建议优先使用异步API，[digest](#digest)。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。 因此建议在子线程中调用同步API，以避免阻塞主线程。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.MessageDigest

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

## getMdLength

```TypeScript
getMdLength(): number
```

获取消息摘要的字节长度，单位为字节。

**起始版本：** 9

**模型约束：** 
- API版本12+：此接口可在Stage模型和FA模型下使用。
- API版本9-11：此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.MessageDigest
- API版本9-11：SystemCapability.Security.CryptoFramework

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## update

```TypeScript
update(input: DataBlob, callback: AsyncCallback<void>): void
```

传入消息进行Md更新摘要状态。使用callback异步回调。update和digest为两段式接口，需要成组使用。其中digest必选，update可选。

> **说明：**&gt;
> Md算法多次调用update更新的代码示例详见开发指导
> [分段摘要算法](../../../security/CryptoArchitectureKit/crypto-generate-message-digest.md#分段摘要算法)。

**起始版本：** 9

**模型约束：** 
- API版本12+：此接口可在Stage模型和FA模型下使用。
- API版本9-11：此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.MessageDigest
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| input | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## update

```TypeScript
update(input: DataBlob): Promise<void>
```

传入消息进行Md更新摘要状态。使用Promise异步回调。update和digest为两段式接口，需要成组使用。其中digest必选，update可选。

> **说明：**&gt;
> Md算法多次调用update更新的代码示例详见开发指导
> [分段摘要算法](../../../security/CryptoArchitectureKit/crypto-generate-message-digest.md#分段摘要算法)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.MessageDigest
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| input | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## updateSync

```TypeScript
updateSync(input: DataBlob): void
```

传入消息进行Md更新摘要状态，通过同步方式更新。updateSync和digestSync为两段式接口，需要成组使用。其中digestSync必选， updateSync可选。

> **说明：**&gt;
> Md算法多次调用updateSync更新的代码示例详见开发指导
> [分段摘要算法](../../../security/CryptoArchitectureKit/crypto-generate-message-digest.md#分段摘要算法)。

**说明：** 建议优先使用异步API，update。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。 因此建议在子线程中调用同步API，以避免阻塞主线程。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.MessageDigest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| input | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## algName

```TypeScript
readonly algName: string
```

代表指定的摘要算法名。

**类型：** string

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.MessageDigest
- API版本9-11：SystemCapability.Security.CryptoFramework
