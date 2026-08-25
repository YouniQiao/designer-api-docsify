# SymKeyGenerator

对称密钥生成器接口，定义生成对称密钥的方法。调用前，需通过 [createSymKeyGenerator](arkts-cryptoarchitecture-cryptoframework-createsymkeygenerator-f.md)方法创建一个SymKeyGenerator实例。

**起始版本：** 9

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.SymKey
- API版本9-11：SystemCapability.Security.CryptoFramework

## 导入模块

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## convertKey

```TypeScript
convertKey(key: DataBlob, callback: AsyncCallback<SymKey>): void
```

将指定数据转换为对称密钥。使用callback异步回调。

> **说明：**&gt;
> 对于HMAC算法的对称密钥，如果已经在创建对称密钥生成器时指定了具体哈希算法（如指定"HMAC|SHA256"），则需要传入与哈希长度一致的二进制
> 密钥数据（如传入SHA256对应256位的密钥数据）。
如果在创建对称密钥生成器时没有指定具体哈希算法，如仅指定"HMAC"，则支持传入长度在[1,4096]范围内（单位为bytes）的任意二进制密钥数据。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.SymKey
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SymKey](arkts-cryptoarchitecture-cryptoframework-symkey-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## convertKey

```TypeScript
convertKey(key: DataBlob): Promise<SymKey>
```

将指定数据转换为对称密钥。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.SymKey
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[SymKey](arkts-cryptoarchitecture-cryptoframework-symkey-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## convertKeySync

```TypeScript
convertKeySync(key: DataBlob): SymKey
```

将指定数据转换为对称密钥。

> **说明：**&gt;
> 对于HMAC算法的对称密钥，如果在创建对称密钥生成器时指定了具体哈希算法（如"HMAC|SHA256"），则需要传入与哈希长度一致的二进制密钥数据&gt;（如传入SHA256对应的256位密钥数据）。如果在创建对称密钥生成器时未指定具体哈希算法，如仅指定"HMAC"，则支持传入长度在1到4096字节范围
> 内的任意二进制密钥数据。

**说明：** 建议优先使用异步API，convertKey。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。 因此建议在子线程中调用同步API，以避免阻塞主线程。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.SymKey

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [SymKey](arkts-cryptoarchitecture-cryptoframework-symkey-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## generateSymKey

```TypeScript
generateSymKey(callback: AsyncCallback<SymKey>): void
```

获取对称密钥生成器随机生成的密钥。使用callback异步回调。

目前使用OpenSSL的RAND_priv_bytes()作为底层能力生成随机密钥。

> **说明：**&gt;
> 对于HMAC算法的对称密钥，如果在创建对称密钥生成器时指定了具体哈希算法（如"HMAC|SHA256"），则会随机生成与哈希长度一致的二进制密钥
> 数据（如256位的密钥数据）。如果未指定具体哈希算法，如仅指定"HMAC"，则不支持随机生成对称密钥数据，可通过
> [convertKey](#convertkey)
> 方式生成对称密钥数据。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.SymKey
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SymKey](arkts-cryptoarchitecture-cryptoframework-symkey-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620004](../errorcode-crypto-framework.md#17620004-无效的函数调用) |

## generateSymKey

```TypeScript
generateSymKey(): Promise<SymKey>
```

获取该对称密钥生成器随机生成的密钥。使用Promise异步回调。

目前使用OpenSSL的RAND_priv_bytes()作为底层能力生成随机密钥。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.SymKey
- API版本9-11：SystemCapability.Security.CryptoFramework

**返回值：**

| 类型 |
| --- |
| Promise&lt;[SymKey](arkts-cryptoarchitecture-cryptoframework-symkey-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620004](../errorcode-crypto-framework.md#17620004-无效的函数调用) |

## generateSymKeySync

```TypeScript
generateSymKeySync(): SymKey
```

同步获取对称密钥生成器随机生成的密钥。

目前使用OpenSSL的RAND_priv_bytes()作为底层能力生成随机密钥。

> **说明：**&gt;
> 对于HMAC算法的对称密钥，如果已经在创建对称密钥生成器时指定了具体哈希算法（如指定"HMAC|SHA256"），则会随机生成与哈希长度一致的
> 二进制密钥数据（如指定"HMAC|SHA256"会随机生成256位的密钥数据）。
如果在创建对称密钥生成器时没有指定具体哈希算法，如仅指定"HMAC"，则不支持随机生成对称密钥数据，可通过 [convertKeySync](#convertkeysync)方式生成对称密钥数据。

**说明：** 建议优先使用异步API，[generateSymKey](#generatesymkey)。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。 因此建议在子线程中调用同步API，以避免阻塞主线程。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.SymKey

**返回值：**

| 类型 |
| --- |
| [SymKey](arkts-cryptoarchitecture-cryptoframework-symkey-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620004](../errorcode-crypto-framework.md#17620004-无效的函数调用) |

## algName

```TypeScript
readonly algName: string
```

对称密钥生成器指定的算法名称。

**类型：** string

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Key.SymKey
- API版本9-11：SystemCapability.Security.CryptoFramework
