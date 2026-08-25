# certVerificationSync

## 导入模块

```TypeScript
import { networkSecurity } from 'kits/@kit.NetworkKit';
```

## certVerificationSync

```TypeScript
export function certVerificationSync(cert: CertBlob, caCert?: CertBlob): number
```

系统将使用证书管理中的预置CA证书和用户安装的CA证书来校验应用传入的证书，使用同步方式返回。

**起始版本：** 11

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cert | [CertBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-certblob-i.md) | 是 |
| caCert | [CertBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-certblob-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2305001](../errorcode-net-networkSecurity.md#2305001-未定义的错误) |
| [2305002](../errorcode-net-networkSecurity.md#2305002-获取证书颁发者失败) |
| [2305003](../errorcode-net-networkSecurity.md#2305003-获取证书吊销列表失败) |
| [2305004](../errorcode-net-networkSecurity.md#2305004-无法解密证书签名) |
| [2305005](../errorcode-net-networkSecurity.md#2305005-无法解密证书吊销列表签名) |
| [2305006](../errorcode-net-networkSecurity.md#2305006-无法解码颁发者公钥) |
| [2305007](../errorcode-net-networkSecurity.md#2305007-证书签名失败) |
| [2305008](../errorcode-net-networkSecurity.md#2305008-证书吊销列表签名失败) |
| [2305009](../errorcode-net-networkSecurity.md#2305009-证书尚未生效) |
| [2305010](../errorcode-net-networkSecurity.md#2305010-证书已过期) |
| [2305011](../errorcode-net-networkSecurity.md#2305011-crl尚未生效) |
| [2305012](../errorcode-net-networkSecurity.md#2305012-crl已过期) |
| [2305023](../errorcode-net-networkSecurity.md#2305023-证书已被吊销) |
| [2305024](../errorcode-net-networkSecurity.md#2305024-无效的证书颁发机构ca) |
| [2305027](../errorcode-net-networkSecurity.md#2305027-证书不可信) |
| [2305018](../errorcode-net-networkSecurity.md#2305018-自签名证书) |
| [2305069](../errorcode-net-networkSecurity.md#2305069-无效的证书验证上下文) |
