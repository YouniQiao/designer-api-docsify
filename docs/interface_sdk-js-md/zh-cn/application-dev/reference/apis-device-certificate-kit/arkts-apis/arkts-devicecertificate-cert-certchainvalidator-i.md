# CertChainValidator

证书链校验器对象。

**起始版本：** 9

**系统能力：** SystemCapability.Security.Cert

## 导入模块

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## validate

```TypeScript
validate(certChain: CertChainData, callback: AsyncCallback<void>): void
```

表示校验X.509证书链。使用Callback异步回调。

由于端侧系统时间不可信，证书链校验不包含对证书有效时间的校验。如果需要检查证书的时间有效性，可使用X.509证书的 [checkValidityWithDate](arkts-devicecertificate-cert-x509cert-i.md#checkvaliditywithdate)方法进行检查。详见 [证书规格](../../../security/DeviceCertificateKit/certificate-framework-overview.md#证书规格)。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| certChain | [CertChainData](arkts-devicecertificate-cert-certchaindata-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

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

## validate

```TypeScript
validate(certChain: CertChainData): Promise<void>
```

表示校验X.509证书链。使用Promise方式返回结果。

由于端侧系统时间不可信，证书链校验不包含对证书有效时间的校验。如果需要检查证书的时间有效性，可使用X.509证书的 [checkValidityWithDate](arkts-devicecertificate-cert-x509cert-i.md#checkvaliditywithdate)方法进行检查。详见 [证书规格](../../../security/DeviceCertificateKit/certificate-framework-overview.md#证书规格)。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| certChain | [CertChainData](arkts-devicecertificate-cert-certchaindata-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

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

## validateCert

```TypeScript
validateCert(cert: X509Cert, params: CertValidationParams): Promise<CertValidationResult>
```

通过构建和验证证书链来验证证书。该接口使用Promise返回结果。

证书链构建过程遵循以下规则：
1. 信任锚来源：始终以信任证书列表（trustedCerts）作为信任锚源。仅当trustSystemCa设置为true时，才使用预配置证书作为信任锚源。
2. 颁发者搜索顺序：系统首先从信任锚来源中搜索颁发者，若未找到，则继续在非信任证书列表（untrustedCerts）中查找。在线下载的中间CA证书
属于非受信任证书。
3. 信任锚锁定：一旦在信任锚来源中找到颁发者，后续查找过程将不会再回至非信任证书，即后续证书必须来自信任锚来源。
4. 构建完成条件：若partialChain为false（默认值），则仅在找到根证书（自签名证书）时构建完成。若partialChain为true，则在首次在
信任锚来源中找到颁发者时构建完成。
5. 后续验证：证书链构建完成后，执行其他验证操作，如证书签名验证和证书吊销检查。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [cert](arkts-security-cert.md) | [X509Cert](../../apis-network-kit/arkts-apis/arkts-network-http-x509cert-t.md) | 是 |
| params | [CertValidationParams](arkts-devicecertificate-cert-certvalidationparams-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CertValidationResult](arkts-devicecertificate-cert-certvalidationresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19020003](../errorcode-cert.md#19020003-参数检查失败) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |
| [19030002](../errorcode-cert.md#19030002-证书签名验证错误) |
| [19030003](../errorcode-cert.md#19030003-证书尚未生效) |
| [19030004](../errorcode-cert.md#19030004-证书过期) |
| [19030005](../errorcode-cert.md#19030005-无法获取证书的颁发者) |
| [19030006](../errorcode-cert.md#19030006-证书的密钥用途不含证书签名) |
| [19030007](../errorcode-cert.md#19030007-证书的密钥用途不含数字签名) |
| [19030009](../errorcode-cert.md#19030009-证书不受信任) |
| [19030010](../errorcode-cert.md#19030010-证书已被吊销) |
| [19030011](../errorcode-cert.md#19030011-未知的关键扩展) |
| [19030012](../errorcode-cert.md#19030012-主机名不匹配) |
| [19030013](../errorcode-cert.md#19030013-邮箱地址不匹配) |
| [19030014](../errorcode-cert.md#19030014-密钥用途不匹配) |
| [19030015](../errorcode-cert.md#19030015-无法获取证书吊销列表) |
| [19030016](../errorcode-cert.md#19030016-证书吊销列表尚未生效) |
| [19030017](../errorcode-cert.md#19030017-证书吊销列表已过期) |
| [19030018](../errorcode-cert.md#19030018-证书吊销列表签名验证失败) |
| [19030019](../errorcode-cert.md#19030019-无法获取证书吊销列表颁发者) |
| [19030020](../errorcode-cert.md#19030020-无法获取在线证书状态协议ocsp响应) |
| [19030021](../errorcode-cert.md#19030021-无效的ocsp响应) |
| [19030022](../errorcode-cert.md#19030022-ocsp签名验证失败) |
| [19030023](../errorcode-cert.md#19030023-ocsp证书状态未知) |
| [19030024](../errorcode-cert.md#19030024-网络连接超时) |

## algorithm

```TypeScript
readonly algorithm: string
```

X.509证书链校验器算法名称。

**类型：** string

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert
