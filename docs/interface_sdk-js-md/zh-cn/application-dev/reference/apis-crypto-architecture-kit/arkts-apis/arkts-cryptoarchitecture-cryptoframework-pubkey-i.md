# PubKey

公钥，是[Key](arkts-cryptoarchitecture-cryptoframework-key-i.md)的子类，在非对称加密、签名验证、密钥协商时需要将其对象作为输入使用。

公钥可以通过非对称密钥生成器[AsyKeyGenerator](arkts-cryptoarchitecture-cryptoframework-asykeygenerator-i.md)、 [AsyKeyGeneratorBySpec](arkts-cryptoarchitecture-cryptoframework-asykeygeneratorbyspec-i.md)来生成。

**继承/实现关系：** PubKey extends [Key](arkts-cryptoarchitecture-cryptoframework-key-i.md)

**起始版本：** 9

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本9-11：SystemCapability.Security.CryptoFramework

## 导入模块

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## getAsyKeySpec

```TypeScript
getAsyKeySpec(itemType: AsyKeySpecItem): bigint | string | number
```

获取密钥参数。此API以同步方式返回结果。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本10-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| itemType | [AsyKeySpecItem](arkts-cryptoarchitecture-cryptoframework-asykeyspecitem-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| bigint \| string \| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## getEncodedDer

```TypeScript
getEncodedDer(format: string): DataBlob
```

支持根据指定的密钥格式（如规范、压缩状态等），获取符合ASN.1语法和DER编码的公钥数据。

> **说明：**&gt;
> 本接口和[Key.getEncoded()](arkts-cryptoarchitecture-cryptoframework-key-i.md#getencoded)的区别是：
> 1. 本接口可以指定获取密钥数据的格式。
> 2. [Key.getEncoded()](arkts-cryptoarchitecture-cryptoframework-key-i.md#getencoded)不支持指定获取密钥数据的格式。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| format | string | 是 | 用于指定当前密钥格式。支持EC密钥，format取值支持"X509\|COMPRESSED"和"X509\|

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
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## getEncodedPem

```TypeScript
getEncodedPem(format: string): string
```

获取PEM编码的密钥数据。此API以同步方式返回结果。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| format | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## getKeyData

```TypeScript
getKeyData(itemType: AsyKeyDataItem): Promise<Uint8Array>
```

获取指定的密钥数据类型对应的公钥数据。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| itemType | [AsyKeyDataItem](arkts-cryptoarchitecture-cryptoframework-asykeydataitem-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Uint8Array & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## getKeyDataSync

```TypeScript
getKeyDataSync(itemType: AsyKeyDataItem): Uint8Array
```

获取指定的密钥数据类型对应的公钥数据。此API以同步方式返回结果。

**说明：** 建议优先使用异步API，getKeyData。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。 因此建议在子线程中调用同步API，以避免阻塞主线程。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| itemType | [AsyKeyDataItem](arkts-cryptoarchitecture-cryptoframework-asykeydataitem-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Uint8Array |

**错误码：**

| 错误码ID |
| --- |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
