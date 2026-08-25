# AsyKeyGenerator

非对称密钥生成器接口，定义生成非对称密钥的方法。调用前，需通过 [createAsyKeyGenerator](arkts-cryptoarchitecture-cryptoframework-createasykeygenerator-f.md)方法创建一个AsyKeyGenerator实例。

**起始版本：** 9

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本9-11：SystemCapability.Security.CryptoFramework

## 导入模块

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## convertKey

```TypeScript
convertKey(pubKey: DataBlob, priKey: DataBlob, callback: AsyncCallback<KeyPair>): void
```

将非对称密钥数据转换为密钥对对象。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## convertKey

```TypeScript
convertKey(pubKey: DataBlob | null, priKey: DataBlob | null, callback: AsyncCallback<KeyPair>): void
```

获取指定数据生成非对称密钥。使用callback异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本10-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | DataBlob \| null | 是 |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | DataBlob \| null | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## convertKey

```TypeScript
convertKey(pubKey: DataBlob, priKey: DataBlob): Promise<KeyPair>
```

将非对称密钥数据转换为密钥对对象。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## convertKey

```TypeScript
convertKey(pubKey: DataBlob | null, priKey: DataBlob | null): Promise<KeyPair>
```

获取指定数据生成非对称密钥。使用Promise异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本10-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | DataBlob \| null | 是 |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | DataBlob \| null | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## convertKeySync

```TypeScript
convertKeySync(pubKey: DataBlob | null, priKey: DataBlob | null): KeyPair
```

同步获取指定数据生成非对称密钥。

**说明：** 建议优先使用异步API，convertKey。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。 因此建议在子线程中调用同步API，以避免阻塞主线程。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | DataBlob \| null | 是 |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | DataBlob \| null | 是 |

**返回值：**

| 类型 |
| --- |
| [KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## convertPemKey

```TypeScript
convertPemKey(pubKey: string | null, priKey: string | null): Promise<KeyPair>
```

获取指定数据生成非对称密钥。使用Promise异步回调。

> **说明：**&gt;
> 1. 使用convertPemKey()将外部字符串转换为Crypto框架定义的非对称密钥对象时，公钥需满足ASN.1语法、X.509规范和PEM编码格式，私钥需
> 满足ASN.1语法、PKCS#8规范和PEM编码格式。
> 2. 在convertPemKey()中，可以只传入pubKey或priKey中的一个，也可以两个都传入。如果只传入其中一个，返回的KeyPair实例中只包含从传
> 入数据转换而来的密钥。
> 3. 使用convertPemKey将外部字符串转换为Crypto框架定义的非对称密钥对象时，系统不会校验生成的密钥对象规格是否与为非对称密钥生成器指
> 定的密钥规格相同。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | string \| null | 是 |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | string \| null | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## convertPemKey

```TypeScript
convertPemKey(pubKey: string | null, priKey: string | null, password: string): Promise<KeyPair>
```

获取指定数据生成非对称密钥。支持加密的私钥，同步传入私钥口令解密私钥。使用Promise异步回调。

> **说明：**&gt;
> 1. 使用convertPemKey()将外部字符串转换为Crypto框架定义的非对称密钥对象时，公钥需满足ASN.1语法、X.509规范和PEM编码格式，私钥需
> 满足ASN.1语法、PKCS#8规范和PEM编码格式。
> 2. 在convertPemKey()中，可以只传入pubKey或priKey中的一个，也可以两个都传入。如果只传入其中一个，返回的KeyPair实例中只包含从传
> 入数据转换而来的密钥。
> 3. 使用convertPemKey将外部字符串转换为Crypto框架定义的非对称密钥对象时，系统不会校验生成的密钥对象规格是否与为非对称密钥生成器指
> 定的密钥规格相同。
> 4. 如果传入了password参数，可用于解密加密的私钥。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | string \| null | 是 |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | string \| null | 是 |
| password | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## convertPemKeySync

```TypeScript
convertPemKeySync(pubKey: string | null, priKey: string | null): KeyPair
```

同步获取指定数据，生成非对称密钥。

> **说明：**
> convertPemKeySync接口与convertPemKey接口注意事项相同，见
> [convertPemKey](#convertpemkey)
> 接口说明。

**说明：** 建议优先使用异步API，[convertPemKey](#convertpemkey)。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。 因此建议在子线程中调用同步API，以避免阻塞主线程。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | string \| null | 是 |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | string \| null | 是 |

**返回值：**

| 类型 |
| --- |
| [KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## convertPemKeySync

```TypeScript
convertPemKeySync(pubKey: string | null, priKey: string | null, password: string): KeyPair
```

获取指定数据生成非对称密钥。支持加密的私钥，同步传入私钥口令解密私钥。

> **说明：**
> convertPemKeySync接口与convertPemKey接口注意事项相同，见
> [convertPemKey](#convertpemkey)
> 接口说明。

**说明：** 建议优先使用异步API，[convertPemKey](#convertpemkey)。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。 因此建议在子线程中调用同步API，以避免阻塞主线程。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | string \| null | 是 |
| [priKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | string \| null | 是 |
| password | string | 是 |

**返回值：**

| 类型 |
| --- |
| [KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## generateKeyPair

```TypeScript
generateKeyPair(callback: AsyncCallback<KeyPair>): void
```

获取非对称密钥生成器随机生成的密钥。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## generateKeyPair

```TypeScript
generateKeyPair(): Promise<KeyPair>
```

获取非对称密钥生成器随机生成的密钥。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本9-11：SystemCapability.Security.CryptoFramework

**返回值：**

| 类型 |
| --- |
| Promise&lt;[KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## generateKeyPairSync

```TypeScript
generateKeyPairSync(): KeyPair
```

同步获取非对称密钥生成器随机生成的密钥。

**说明：** 建议优先使用异步API，generateKeyPair。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。 因此建议在子线程中调用同步API，以避免阻塞主线程。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**返回值：**

| 类型 |
| --- |
| [KeyPair](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) |

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

非对称密钥生成器指定的算法名称。

**类型：** string

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本9-11：SystemCapability.Security.CryptoFramework
