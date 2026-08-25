# SignatureUtils

用于ECC/SM2签名数据转换的工具类。

**起始版本：** 20

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

## 导入模块

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## genEccSignature

```TypeScript
static genEccSignature(spec: EccSignatureSpec): Uint8Array
```

将（r、s）的ECC/SM2签名数据转换为ASN.1 DER编码。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| spec | [EccSignatureSpec](arkts-cryptoarchitecture-cryptoframework-eccsignaturespec-i.md) | 是 |

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

## genEccSignatureSpec

```TypeScript
static genEccSignatureSpec(data: Uint8Array): EccSignatureSpec
```

从ASN.1 DER编码的ECC/SM2签名数据获取r和s。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| [EccSignatureSpec](arkts-cryptoarchitecture-cryptoframework-eccsignaturespec-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [17620001](../errorcode-crypto-framework.md#17620001-内存操作失败) |
| [17620002](../errorcode-crypto-framework.md#17620002-获取native对象失败或参数转换失败) |
| [17620003](../errorcode-crypto-framework.md#17620003-参数检查失败) |
| [17630001](../errorcode-crypto-framework.md#17630001-密码操作错误) |
