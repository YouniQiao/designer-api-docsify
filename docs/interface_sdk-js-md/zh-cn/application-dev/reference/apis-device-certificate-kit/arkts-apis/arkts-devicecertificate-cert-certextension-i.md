# CertExtension

提供操作X.509证书扩展的API。

**起始版本：** 10

**系统能力：** SystemCapability.Security.Cert

## 导入模块

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## checkCA

```TypeScript
checkCA(): number
```

检查证书是否为CA证书。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getEncoded

```TypeScript
getEncoded(): EncodingBlob
```

获取证书扩展的序列化数据。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| [EncodingBlob](arkts-devicecertificate-cert-encodingblob-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getEntry

```TypeScript
getEntry(valueType: ExtensionEntryType, oid: DataBlob): DataBlob
```

根据OID获取证书扩展项的值。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [valueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-scanneroptionvalue-i.md) | [ExtensionEntryType](arkts-devicecertificate-cert-extensionentrytype-e.md) | 是 |
| oid | [DataBlob](arkts-devicecertificate-cert-datablob-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataBlob](arkts-devicecertificate-cert-datablob-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## getOidList

```TypeScript
getOidList(valueType: ExtensionOidType): DataArray
```

获取证书扩展的OID列表。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [valueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-scanneroptionvalue-i.md) | [ExtensionOidType](arkts-devicecertificate-cert-extensionoidtype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataArray](arkts-devicecertificate-cert-dataarray-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## hasUnsupportedCriticalExtension

```TypeScript
hasUnsupportedCriticalExtension(): boolean
```

判断是否存在不支持的关键扩展。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |
