# createTrustAnchorsWithKeyStore

## createTrustAnchorsWithKeyStore

```TypeScript
function createTrustAnchorsWithKeyStore(keystore: Uint8Array, pwd: string): Promise<Array<X509TrustAnchor>>
```

表示从P12中读取ca证书来构造[TrustAnchor](arkts-devicecertificate-cert-x509trustanchor-i.md#X509TrustAnchor)对象数组。使用Promise方式返回结果。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-cert-function createTrustAnchorsWithKeyStore(keystore: Uint8Array, pwd: string): Promise<Array<X509TrustAnchor>>--><!--Device-cert-function createTrustAnchorsWithKeyStore(keystore: Uint8Array, pwd: string): Promise<Array<X509TrustAnchor>>-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keystore | Uint8Array | 是 |
| pwd | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[X509TrustAnchor](arkts-devicecertificate-cert-x509trustanchor-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030002](../errorcode-cert.md#19030002-证书签名验证错误) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19030003](../errorcode-cert.md#19030003-证书尚未生效) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |
| [19030006](../errorcode-cert.md#19030006-证书的密钥用途不含证书签名) |
| [19030007](../errorcode-cert.md#19030007-证书的密钥用途不含数字签名) |
| [19030004](../errorcode-cert.md#19030004-证书过期) |
| [19030005](../errorcode-cert.md#19030005-无法获取证书的颁发者) |
