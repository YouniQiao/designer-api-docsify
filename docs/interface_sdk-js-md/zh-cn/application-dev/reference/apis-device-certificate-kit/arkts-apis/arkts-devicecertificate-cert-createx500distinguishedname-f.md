# createX500DistinguishedName

## 导入模块

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## createX500DistinguishedName

```TypeScript
function createX500DistinguishedName(nameStr: string): Promise<X500DistinguishedName>
```

表示使用字符串格式的名称创建X500DistinguishedName对象。使用Promise方式返回结果。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| nameStr | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[X500DistinguishedName](arkts-devicecertificate-cert-x500distinguishedname-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |
| [19030002](../errorcode-cert.md#19030002-证书签名验证错误) |
| [19030003](../errorcode-cert.md#19030003-证书尚未生效) |
| [19030004](../errorcode-cert.md#19030004-证书过期) |
| [19030005](../errorcode-cert.md#19030005-无法获取证书的颁发者) |
| [19030006](../errorcode-cert.md#19030006-证书的密钥用途不含证书签名) |
| [19030007](../errorcode-cert.md#19030007-证书的密钥用途不含数字签名) |


## createX500DistinguishedName

```TypeScript
function createX500DistinguishedName(nameDer: Uint8Array): Promise<X500DistinguishedName>
```

表示使用DER格式的名称创建X500DistinguishedName对象。使用Promise方式返回结果。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| nameDer | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[X500DistinguishedName](arkts-devicecertificate-cert-x500distinguishedname-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |
| [19030002](../errorcode-cert.md#19030002-证书签名验证错误) |
| [19030003](../errorcode-cert.md#19030003-证书尚未生效) |
| [19030004](../errorcode-cert.md#19030004-证书过期) |
| [19030005](../errorcode-cert.md#19030005-无法获取证书的颁发者) |
| [19030006](../errorcode-cert.md#19030006-证书的密钥用途不含证书签名) |
| [19030007](../errorcode-cert.md#19030007-证书的密钥用途不含数字签名) |
