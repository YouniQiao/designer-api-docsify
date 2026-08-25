# Verify

验签接口，定义基于公钥对签名数据进行验签的方法。调用前，需通过 [createVerify(algName: string): Verify](arkts-cryptoarchitecture-cryptoframework-createverify-f.md)方法创建一个Verify实例。按序调用Verify实例中 的init、update（可选）、verify方法完成验签操作。验签操作的示例代码详见 [签名验签开发指导](../../../security/CryptoArchitectureKit/crypto-rsa-sign-sig-verify.md)。

Verify实例不支持重复初始化，当业务方需要使用新密钥验签时，需要重新创建新Verify实例并调用init初始化。

业务方使用时，在createVerify时确定验签的模式，调用init接口设置密钥。

当被签名的消息较短时，可在init初始化后，（无需update）直接调用verify接口传入被签名的消息和签名（signatureData）进行验签。

当被签名的消息较长时，可通过update接口分段传入被签名的消息，最后调用verify接口对消息全文进行验签。verify接口的data入参在API 10之前只 支持DataBlob， API 10之后增加支持null。业务方可在循环中调用update接口，循环结束后调用verify传入签名（signatureData）进行验签。

当使用DSA算法进行验签，并设置了摘要算法为NoHash时，则不支持update操作，update接口会返回错误码ERR_CRYPTO_OPERATION。

**起始版本：** 9

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Signature
- API版本9-11：SystemCapability.Security.CryptoFramework

## 导入模块

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## getVerifySpec

```TypeScript
getVerifySpec(itemType: SignSpecItem): string | number
```

获取验签参数。当前只支持RSA算法。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Signature
- API版本10-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| itemType | [SignSpecItem](arkts-cryptoarchitecture-cryptoframework-signspecitem-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| string \| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## init

```TypeScript
init(pubKey: PubKey, callback: AsyncCallback<void>): void
```

传入公钥初始化Verify实例。使用callback异步回调。init、update、verify为三段式接口，需要成组使用。其中init和verify必选，update 可选。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Signature
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## init

```TypeScript
init(pubKey: PubKey): Promise<void>
```

传入公钥初始化Verify实例。使用Promise异步回调。init、update、verify为三段式接口，需要成组使用。其中init和verify必选，update 可选。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Signature
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## initSync

```TypeScript
initSync(pubKey: PubKey): void
```

传入公钥初始化Verify实例，通过同步方式获取结果。initSync、updateSync、verifySync为三段式接口，需要成组使用。其中initSync和 verifySync必选，updateSync可选。

**说明：** 建议优先使用异步API，init。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。 因此建议在子线程中调用同步API，以避免阻塞主线程。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pubKey](arkts-cryptoarchitecture-cryptoframework-keypair-i.md) | [PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## recover

```TypeScript
recover(signatureData: DataBlob): Promise<DataBlob | null>
```

对数据进行签名恢复原始数据。使用Promise异步回调。

> **说明：**&gt;
> - 目前仅RSA支持。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| signatureData | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;DataBlob \ | null & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620004](../errorcode-crypto-framework.md#17620004-无效的函数调用) |

## recoverSync

```TypeScript
recoverSync(signatureData: DataBlob): DataBlob | null
```

对数据进行签名恢复原始数据。

> **说明：**&gt;
> - 目前仅RSA支持。

**说明：** 建议优先使用异步API，[recover](#recover)。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。 因此建议在子线程中调用同步API，以避免阻塞主线程。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| signatureData | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| DataBlob \| null |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620004](../errorcode-crypto-framework.md#17620004-无效的函数调用) |

## setVerifySpec

```TypeScript
setVerifySpec(itemType: SignSpecItem, itemValue: number): void
```

设置验签参数。常用的验签参数直接通过[createVerify](arkts-cryptoarchitecture-cryptoframework-createverify-f.md) 来指定，剩余参数通过本接口指定。

支持RSA算法和SM2算法，从API version 11开始，支持SM2算法设置签名验证参数。

验签的参数应当与签名的参数保持一致。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Signature
- API版本10-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| itemType | [SignSpecItem](arkts-cryptoarchitecture-cryptoframework-signspecitem-e.md) | 是 |
| itemValue | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## setVerifySpec

```TypeScript
setVerifySpec(itemType: SignSpecItem, itemValue: number | Uint8Array): void
```

设置签名验证参数。

当前仅支持RSA算法中的PSS_SALT_LEN和SM2签名验证中的USER_ID。

验签的参数应当与签名的参数保持一致。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Signature
- API版本11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| itemType | [SignSpecItem](arkts-cryptoarchitecture-cryptoframework-signspecitem-e.md) | 是 |
| itemValue | number \| Uint8Array | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |
| [17620004](../errorcode-crypto-framework.md#17620004-无效的函数调用) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## setVerifySpec

```TypeScript
setVerifySpec(itemType: SignSpecItem, itemValue: number | Uint8Array | boolean): void
```

设置签名验证参数。

当前仅支持RSA算法中的PSS_SALT_LEN，SM2算法中的USER_ID以及ML-DSA算法中的ML_DSA_DETERMINISTIC、ML_DSA_MU和ML_DSA_CONTEXT。

验签的参数应当与签名的参数保持一致。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| itemType | [SignSpecItem](arkts-cryptoarchitecture-cryptoframework-signspecitem-e.md) | 是 |
| itemValue | number \| Uint8Array \| boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |
| [17620004](../errorcode-crypto-framework.md#17620004-无效的函数调用) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |

## update

```TypeScript
update(data: DataBlob, callback: AsyncCallback<void>): void
```

追加待验签数据，使用callback异步回调完成更新。

必须在对[Verify](#verify)实例使用[init](#init)或 [initSync](#initsync)初始化后，才能使用本函数。

> **说明：**&gt;
> 根据数据量，可以不调用update（即[init](#init)
> 完成后直接调用
> [verify](#verify)
> ）或多次调用update。&gt;
> 算法库目前没有对update（单次或累计）的数据量设置大小限制，建议对于大数据量的验签操作，采用多次update的方式传入数据，避免一次性申请
> 过大内存。&gt;
> 验签使用多次update操作的示例代码详见
> [使用RSA密钥对分段签名验签](../../../security/CryptoArchitectureKit/crypto-rsa-sign-sig-verify.md)
> ，其余算法操作类似。&gt;
> OnlyVerify模式下，不支持update操作，直接使用verify传入数据即可。&gt;
> 当使用DSA算法进行验签，并设置了摘要算法为NoHash时，则不支持update操作，update接口会返回错误码ERR_CRYPTO_OPERATION。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Signature
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620004](../errorcode-crypto-framework.md#17620004-无效的函数调用) |

## update

```TypeScript
update(data: DataBlob): Promise<void>
```

追加待验签数据，使用Promise异步回调完成更新。

必须在对[Verify](#verify)实例使用[init()](#init)初始化后，才能使 用本函数。

> **说明：**&gt;
> 根据数据量，可以不调用update（即[init](#init)完成后直接调用
> [verify](#verify)）或多次调用update。&gt;
> 算法库目前没有对update（单次或累计）的数据量设置大小限制，建议对于大数据量的验签操作，采用多次update的方式传入数据，避免一次性申请
> 过大内存。&gt;
> 验签使用多次update操作的示例代码详见
> [使用RSA密钥对分段签名验签](../../../security/CryptoArchitectureKit/crypto-rsa-sign-sig-verify.md)
> ，其余算法操作类似。&gt;
> OnlyVerify模式下，不支持update操作，直接使用verify传入数据即可。&gt;
> 当使用DSA算法进行验签，并设置了摘要算法为NoHash时，则不支持update操作，update接口会返回错误码ERR_CRYPTO_OPERATION。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Signature
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620004](../errorcode-crypto-framework.md#17620004-无效的函数调用) |

## updateSync

```TypeScript
updateSync(data: DataBlob): void
```

追加待验签数据，通过同步方式完成更新。

必须在对[Verify](#verify)实例使用[initSync()](#initsync)初始化后，才 能使用本函数。

> **说明：**&gt;
> 根据数据量，可以不调用updateSync（即[initSync](#initsync)完成后直接调用
> [verifySync](#verifysync)）或多次调用updateSync。&gt;
> 算法库目前没有对updateSync（单次或累计）的数据量设置大小限制，建议对于大数据量的验签操作，采用多次updateSync的方式传入数据，避免
> 一次性申请过大内存。&gt;
> 验签使用多次updateSync操作的示例代码详见
> [使用RSA密钥对分段签名验签](../../../security/CryptoArchitectureKit/crypto-rsa-sign-sig-verify.md)，
> 其余算法操作类似。&gt;
> OnlyVerify模式下，不支持updateSync操作，需要直接使用verifySync传入数据。&gt;
> 当使用DSA算法进行验签，并设置了摘要算法为NoHash时，则不支持updateSync操作，updateSync接口会返回错误码ERR_CRYPTO_OPERATION。

**说明：** 建议优先使用异步API，update。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。 因此建议在子线程中调用同步API，以避免阻塞主线程。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620004](../errorcode-crypto-framework.md#17620004-无效的函数调用) |

## verify

```TypeScript
verify(data: DataBlob, signatureData: DataBlob, callback: AsyncCallback<boolean>): void
```

对数据进行验签，包含update的数据。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Signature
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |
| signatureData | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## verify

```TypeScript
verify(data: DataBlob | null, signatureData: DataBlob, callback: AsyncCallback<boolean>): void
```

对数据进行验签。使用callback异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Signature
- API版本10-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | DataBlob \| null | 是 |
| signatureData | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## verify

```TypeScript
verify(data: DataBlob, signatureData: DataBlob): Promise<boolean>
```

对数据进行验签，包含update的数据。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Signature
- API版本9-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |
| signatureData | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## verify

```TypeScript
verify(data: DataBlob | null, signatureData: DataBlob): Promise<boolean>
```

对数据进行验签。使用Promise异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Signature
- API版本10-11：SystemCapability.Security.CryptoFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | DataBlob \| null | 是 |
| signatureData | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## verifySync

```TypeScript
verifySync(data: DataBlob | null, signatureData: DataBlob): boolean
```

对数据进行验签，通过同步方式返回验签结果。

**说明：** 建议优先使用异步API，[verify](#verify)。同步API可能因系统繁忙、高负载等原因耗时较长而阻塞主线程。 因此建议在子线程中调用同步API，以避免阻塞主线程。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | DataBlob \| null | 是 |
| signatureData | [DataBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-datablob-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |

## algName

```TypeScript
readonly algName: string
```

验签指定的算法名称。

**类型：** string

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** 
- API版本12+：SystemCapability.Security.CryptoFramework.Signature
- API版本9-11：SystemCapability.Security.CryptoFramework
