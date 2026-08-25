# AsyKeyGeneratorBySpec

指定密钥规格的非对称密钥生成器接口，定义根据指定密钥规格生成非对称密钥的方法。调用前，需通过 [createAsyKeyGeneratorBySpec](arkts-cryptoarchitecture-cryptoframework-createasykeygeneratorbyspec-f.md)方法创建一个AsyKeyGeneratorBySpec实例。

**起始版本：** 10

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本10-11：SystemCapability.Security.CryptoFramework

## 导入模块

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## generateKeyPair

```TypeScript
generateKeyPair(callback: AsyncCallback<KeyPair>): void
```

获取非对称密钥生成器生成的密钥。使用callback异步回调。

当使用[COMMON_PARAMS_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md)类型的密钥参数来创建密钥生成器时，可以得到随机生成的密钥对； 当使用[KEY_PAIR_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md)类型的密钥参数来创建密钥生成器时，可以得到各项数据与密钥参数一致的 密钥对。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本10-11：SystemCapability.Security.CryptoFramework

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

获取该非对称密钥生成器生成的密钥。使用Promise异步回调。

当使用[COMMON_PARAMS_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md)类型的密钥参数来创建密钥生成器时，可以得到随机生成的密钥对； 当使用[KEY_PAIR_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md)类型的密钥参数来创建密钥生成器时，可以得到各项数据与密钥参数一致的 密钥对。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本10-11：SystemCapability.Security.CryptoFramework

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

同步获取该非对称密钥生成器生成的密钥。

当使用[COMMON_PARAMS_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md)类型的密钥参数来创建密钥生成器时，可以得到随机生成的密钥对； 当使用[KEY_PAIR_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md)类型的密钥参数来创建密钥生成器时，可以得到各项数据与密钥参数一致的 密钥对。

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

## generatePriKey

```TypeScript
generatePriKey(callback: AsyncCallback<PriKey>): void
```

获取非对称密钥生成器生成的密钥。使用callback异步回调。

使用[PRIVATE_KEY_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md)类型密钥参数创建密钥生成器，生成指定私钥。使用 [KEY_PAIR_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md)类型密钥参数创建密钥生成器，从生成的密钥对中获取指定私钥。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本10-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## generatePriKey

```TypeScript
generatePriKey(): Promise<PriKey>
```

获取该非对称密钥生成器生成的私钥。使用Promise异步回调。

当使用[PRIVATE_KEY_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md)类型的密钥参数来创建密钥生成器时，可以得到指定的私钥；当使用 [KEY_PAIR_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md)类型的密钥参数来创建密钥生成器时，可以从生成的密钥对中获取指定的私钥。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本10-11：SystemCapability.Security.CryptoFramework

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## generatePriKeySync

```TypeScript
generatePriKeySync(): PriKey
```

使用该非对称密钥生成器生成私钥。该接口以同步方式返回结果。

当使用[PRIVATE_KEY_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md)类型的密钥参数来创建密钥生成器时，可以得到指定的私钥；当使用 [KEY_PAIR_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md)类型的密钥参数来创建密钥生成器时，可以从生成的密钥对中获取指定的私钥。

**说明：** 建议优先使用异步API，[generatePriKey](#generateprikey)。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。 因此建议在子线程中调用同步API，以避免阻塞主线程。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**返回值：**

| 类型 |
| --- |
| [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## generatePubKey

```TypeScript
generatePubKey(callback: AsyncCallback<PubKey>): void
```

获取非对称密钥生成器生成的公钥。使用callback异步回调。

当使用[PUBLIC_KEY_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md)类型的密钥参数来创建密钥生成器时，可以得到指定的公钥；当使用 [KEY_PAIR_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md)类型的密钥参数来创建密钥生成器时，可以从生成的密钥对中获取指定的公钥。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本10-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## generatePubKey

```TypeScript
generatePubKey(): Promise<PubKey>
```

获取该非对称密钥生成器生成的公钥。使用Promise异步回调。

当使用[PUBLIC_KEY_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md)类型的密钥参数来创建密钥生成器时，可以得到指定的公钥；当使用 [KEY_PAIR_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md)类型的密钥参数来创建密钥生成器时，可以从生成的密钥对中获取指定的公钥。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本10-11：SystemCapability.Security.CryptoFramework

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## generatePubKeySync

```TypeScript
generatePubKeySync(): PubKey
```

同步获取该非对称密钥生成器生成的公钥。

当使用[PUBLIC_KEY_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md)类型的密钥参数来创建密钥生成器时，可以得到指定的公钥；使用 [KEY_PAIR_SPEC](arkts-cryptoarchitecture-cryptoframework-asykeyspectype-e.md)类型的密钥参数时，可以从生成的密钥对中获取指定的公钥。

**说明：** 建议优先使用异步API，[generatePubKey](#generatepubkey)。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。 因此建议在子线程中调用同步API，以避免阻塞主线程。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**返回值：**

| 类型 |
| --- |
| [PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md) |

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

非对称密钥生成器的算法名。

**类型：** string

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.AsymKey
- API版本10-11：SystemCapability.Security.CryptoFramework
