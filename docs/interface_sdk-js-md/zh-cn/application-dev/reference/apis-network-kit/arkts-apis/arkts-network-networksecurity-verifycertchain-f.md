# verifyCertChain

## 导入模块

```TypeScript
import { networkSecurity } from 'kits/@kit.NetworkKit';
```

## verifyCertChain

```TypeScript
export function verifyCertChain(cert: CertBlob[], caCert?: CertBlob, hostname?: string): Promise<CertBlob[]>
```

验证服务器证书链并返回排序后的证书链。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cert | [CertBlob[]](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-certblob-i.md) | 是 |
| caCert | [CertBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-certblob-i.md) | 否 |
| [hostname](../../apis-arkts/arkts-apis/arkts-arkts-url-url-c.md) | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;CertBlob[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [2305001](../errorcode-net-networkSecurity.md#2305001-未定义的错误) |
| [2305002](../errorcode-net-networkSecurity.md#2305002-获取证书颁发者失败) |
| [2305004](../errorcode-net-networkSecurity.md#2305004-无法解密证书签名) |
| [2305006](../errorcode-net-networkSecurity.md#2305006-无法解码颁发者公钥) |
| [2305007](../errorcode-net-networkSecurity.md#2305007-证书签名失败) |
| [2305009](../errorcode-net-networkSecurity.md#2305009-证书尚未生效) |
| [2305010](../errorcode-net-networkSecurity.md#2305010-证书已过期) |
| [2305018](../errorcode-net-networkSecurity.md#2305018-自签名证书) |
| [2305024](../errorcode-net-networkSecurity.md#2305024-无效的证书颁发机构ca) |
| [2305027](../errorcode-net-networkSecurity.md#2305027-证书不可信) |
| [2305062](../errorcode-net-networkSecurity.md#2305062-主机名验证失败) |
| [2305069](../errorcode-net-networkSecurity.md#2305069-无效的证书验证上下文) |
