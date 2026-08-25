# Random

随机数接口，定义随机数生成的方法。调用前，需通过[createRandom](arkts-cryptoarchitecture-cryptoframework-createrandom-f.md)创建一个Random实例。

**起始版本：** 9

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Rand
- API版本9-11：SystemCapability.Security.CryptoFramework

## 导入模块

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## enableHardwareEntropy

```TypeScript
enableHardwareEntropy(): void
```

开启硬件熵源。将从TEE中获取安全随机数作为该随机数实例的熵源。

**起始版本：** 21

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Rand

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## generateRandom

```TypeScript
generateRandom(len: number, callback: AsyncCallback<DataBlob>): void
```

生成指定长度的随机数。使用callback异步回调。

**起始版本：** 9

**模型约束：** 
- API版本12+：此接口可在Stage模型和FA模型下使用。
- API版本9-11：此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Rand
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| len | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DataBlob&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## generateRandom

```TypeScript
generateRandom(len: number): Promise<DataBlob>
```

生成指定长度的随机数。使用promise异步回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Rand
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| len | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;DataBlob & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## generateRandomSync

```TypeScript
generateRandomSync(len: number): DataBlob
```

同步生成指定长度的随机数。

**说明：** 建议优先使用异步API，[generateRandom](#generaterandom)。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。 因此建议在子线程中调用同步API，以避免阻塞主线程。

**起始版本：** 10

**模型约束：** 
- API版本12+：此接口可在Stage模型和FA模型下使用。
- API版本10-11：此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Rand
- API版本10-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| len | number | 是 |

**返回值：**

| 类型 |
| --- |
| [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## setSeed

```TypeScript
setSeed(seed: DataBlob): void
```

设置指定的种子。

**起始版本：** 9

**模型约束：** 
- API版本12+：此接口可在Stage模型和FA模型下使用。
- API版本9-11：此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Rand
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| seed | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |

## algName

```TypeScript
readonly algName: string
```

代表当前使用的随机数生成算法，目前只支持"CTR_DRBG"。

**类型：** string

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Rand
- API版本10-11：SystemCapability.Security.CryptoFramework
