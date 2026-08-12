# createTrustAnchorsWithKeyStore

## createTrustAnchorsWithKeyStore

```TypeScript
function createTrustAnchorsWithKeyStore(keystore: Uint8Array, pwd: string): Promise<Array<X509TrustAnchor>>
```

表示从P12中读取ca证书来构造[TrustAnchor](arkts-devicecertificate-cert-x509trustanchor-i.md#X509TrustAnchor)对象数组。使用Promise方式返回结果。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

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
| [19020002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020002-运行时错误) |
| [19030002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030002-证书签名验证错误) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [19030003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030003-证书尚未生效) |
| [19020001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020001-内存错误) |
| [19030001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030001-调用三方算法库api出错) |
| [19030006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030006-证书的密钥用途不含证书签名) |
| [19030007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030007-证书的密钥用途不含数字签名) |
| [19030004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030004-证书过期) |
| [19030005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030005-无法获取证书的颁发者) |
