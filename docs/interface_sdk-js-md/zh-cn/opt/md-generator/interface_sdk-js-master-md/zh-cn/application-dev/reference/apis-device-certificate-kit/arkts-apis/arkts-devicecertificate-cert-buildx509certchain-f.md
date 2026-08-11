# buildX509CertChain

## buildX509CertChain

```TypeScript
function buildX509CertChain(param: CertChainBuildParameters): Promise<CertChainBuildResult>
```

表示使用CertChainBuildParameters对象方式创建X.509证书链对象。使用Promise方式返回结果。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-cert-function buildX509CertChain(param: CertChainBuildParameters): Promise<CertChainBuildResult>--><!--Device-cert-function buildX509CertChain(param: CertChainBuildParameters): Promise<CertChainBuildResult>-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| param | [CertChainBuildParameters](arkts-devicecertificate-cert-certchainbuildparameters-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;CertChainBuildResult&gt; |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030002](../errorcode-cert.md#19030002-证书签名验证错误) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [19030003](../errorcode-cert.md#19030003-证书尚未生效) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |
| [19030006](../errorcode-cert.md#19030006-证书的密钥用途不含证书签名) |
| [19030007](../errorcode-cert.md#19030007-证书的密钥用途不含数字签名) |
| [19030004](../errorcode-cert.md#19030004-证书过期) |
| [19030005](../errorcode-cert.md#19030005-无法获取证书的颁发者) |
