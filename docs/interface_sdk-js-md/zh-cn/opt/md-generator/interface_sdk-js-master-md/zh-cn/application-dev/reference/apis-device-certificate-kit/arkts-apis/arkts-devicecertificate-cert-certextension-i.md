# CertExtension

提供操作X.509证书扩展的API。

**起始版本：** 23

**废弃版本：** -1

<!--Device-cert-interface CertExtension--><!--Device-cert-interface CertExtension-End-->

**系统能力：** SystemCapability.Security.Cert

## checkCA

```TypeScript
checkCA(): number
```

检查证书是否为CA证书。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CertExtension-checkCA(): int--><!--Device-CertExtension-checkCA(): int-End-->

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## 示例

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 证书扩展域段二进制数据，需业务自行赋值。
let extData = new Uint8Array([
  0x30, 0x40, 0x30, 0x0F, 0x06, 0x03, 0x55, 0x1D,
  0x13, 0x01, 0x01, 0xFF, 0x04, 0x05, 0x30, 0x03,
  0x01, 0x01, 0xFF, 0x30, 0x0E, 0x06, 0x03, 0x55,
  0x1D, 0x0F, 0x01, 0x01, 0xFF, 0x04, 0x04, 0x03,
  0x02, 0x01, 0xC6, 0x30, 0x1D, 0x06, 0x03, 0x55,
  0x1D, 0x0E, 0x04, 0x16, 0x04, 0x14, 0xE0, 0x8C,
  0x9B, 0xDB, 0x25, 0x49, 0xB3, 0xF1, 0x7C, 0x86,
  0xD6, 0xB2, 0x42, 0x87, 0x0B, 0xD0, 0x6B, 0xA0,
  0xD9, 0xE4
]);

let encodingBlob: cert.EncodingBlob = {
  data: extData,
  // 根据encodingData的格式进行赋值，仅支持FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_DER
};
cert.createCertExtension(encodingBlob, (error, certExt) => {
  if (error) {
    console.error(`createCertExtension failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createCertExtension result: success.');
    try {
      let res = certExt.checkCA();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`ext checkCA failed, errCode: ${e.code}, errMsg: ${e.message}`);
    }
  }
});
```

## getEncoded

```TypeScript
getEncoded(): EncodingBlob
```

获取证书扩展的序列化数据。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CertExtension-getEncoded(): EncodingBlob--><!--Device-CertExtension-getEncoded(): EncodingBlob-End-->

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| [EncodingBlob](arkts-devicecertificate-cert-encodingblob-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## 示例

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 证书扩展域段二进制数据，需业务自行赋值。
let extData = new Uint8Array([
  0x30, 0x40, 0x30, 0x0F, 0x06, 0x03, 0x55, 0x1D,
  0x13, 0x01, 0x01, 0xFF, 0x04, 0x05, 0x30, 0x03,
  0x01, 0x01, 0xFF, 0x30, 0x0E, 0x06, 0x03, 0x55,
  0x1D, 0x0F, 0x01, 0x01, 0xFF, 0x04, 0x04, 0x03,
  0x02, 0x01, 0xC6, 0x30, 0x1D, 0x06, 0x03, 0x55,
  0x1D, 0x0E, 0x04, 0x16, 0x04, 0x14, 0xE0, 0x8C,
  0x9B, 0xDB, 0x25, 0x49, 0xB3, 0xF1, 0x7C, 0x86,
  0xD6, 0xB2, 0x42, 0x87, 0x0B, 0xD0, 0x6B, 0xA0,
  0xD9, 0xE4
]);

let encodingBlob: cert.EncodingBlob = {
  data: extData,
  // 根据encodingData的格式进行赋值，仅支持FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_DER
};

cert.createCertExtension(encodingBlob, (error, certExt) => {
  if (error) {
    console.error(`createCertExtension failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createCertExtension result: success.');
    try {
      let extEncodedBlob = certExt.getEncoded();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`ext getEncoded failed, errCode: ${e.code}, errMsg: ${e.message}`);
    }
  }
});
```

## getEntry

```TypeScript
getEntry(valueType: ExtensionEntryType, oid: DataBlob): DataBlob
```

根据OID获取证书扩展项的值。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CertExtension-getEntry(valueType: ExtensionEntryType, oid: DataBlob): DataBlob--><!--Device-CertExtension-getEntry(valueType: ExtensionEntryType, oid: DataBlob): DataBlob-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [valueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-scanneroptionvalue-i.md) | [ExtensionEntryType](arkts-devicecertificate-cert-extensionentrytype-e.md) | 是 |
| oid | [DataBlob](arkts-devicecertificate-cert-datablob-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataBlob](arkts-devicecertificate-cert-datablob-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## 示例

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 证书扩展域段二进制数据，需业务自行赋值。
let extData = new Uint8Array([
  0x30, 0x40, 0x30, 0x0F, 0x06, 0x03, 0x55, 0x1D,
  0x13, 0x01, 0x01, 0xFF, 0x04, 0x05, 0x30, 0x03,
  0x01, 0x01, 0xFF, 0x30, 0x0E, 0x06, 0x03, 0x55,
  0x1D, 0x0F, 0x01, 0x01, 0xFF, 0x04, 0x04, 0x03,
  0x02, 0x01, 0xC6, 0x30, 0x1D, 0x06, 0x03, 0x55,
  0x1D, 0x0E, 0x04, 0x16, 0x04, 0x14, 0xE0, 0x8C,
  0x9B, 0xDB, 0x25, 0x49, 0xB3, 0xF1, 0x7C, 0x86,
  0xD6, 0xB2, 0x42, 0x87, 0x0B, 0xD0, 0x6B, 0xA0,
  0xD9, 0xE4
]);

let encodingBlob: cert.EncodingBlob = {
  data: extData,
  // 根据encodingData的格式进行赋值，仅支持FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_DER
};

cert.createCertExtension(encodingBlob, (error, certExt) => {
  if (error) {
    console.error(`createCertExtension failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createCertExtension result: success.');
    let oid = new Uint8Array([0x32, 0x2e, 0x35, 0x2e, 0x32, 0x39, 0x2e, 0x31, 0x35]);
    let oidBlob: cert.DataBlob = {
      data: oid
    }
    try {
      let entry = certExt.getEntry(cert.ExtensionEntryType.EXTENSION_ENTRY_TYPE_ENTRY, oidBlob);
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`ext getEntry failed, errCode: ${e.code}, errMsg: ${e.message}`);
    }
  }
});
```

## getOidList

```TypeScript
getOidList(valueType: ExtensionOidType): DataArray
```

获取证书扩展的OID列表。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CertExtension-getOidList(valueType: ExtensionOidType): DataArray--><!--Device-CertExtension-getOidList(valueType: ExtensionOidType): DataArray-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [valueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-scanneroptionvalue-i.md) | [ExtensionOidType](arkts-devicecertificate-cert-extensionoidtype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataArray](arkts-devicecertificate-cert-dataarray-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## 示例

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 证书扩展域段二进制数据，需业务自行赋值。
let extData = new Uint8Array([
  0x30, 0x40, 0x30, 0x0F, 0x06, 0x03, 0x55, 0x1D,
  0x13, 0x01, 0x01, 0xFF, 0x04, 0x05, 0x30, 0x03,
  0x01, 0x01, 0xFF, 0x30, 0x0E, 0x06, 0x03, 0x55,
  0x1D, 0x0F, 0x01, 0x01, 0xFF, 0x04, 0x04, 0x03,
  0x02, 0x01, 0xC6, 0x30, 0x1D, 0x06, 0x03, 0x55,
  0x1D, 0x0E, 0x04, 0x16, 0x04, 0x14, 0xE0, 0x8C,
  0x9B, 0xDB, 0x25, 0x49, 0xB3, 0xF1, 0x7C, 0x86,
  0xD6, 0xB2, 0x42, 0x87, 0x0B, 0xD0, 0x6B, 0xA0,
  0xD9, 0xE4
]);

let encodingBlob: cert.EncodingBlob = {
  data: extData,
  // 根据encodingData的格式进行赋值，仅支持FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_DER
};

cert.createCertExtension(encodingBlob, (error, certExt) => {
  if (error) {
    console.error(`createCertExtension failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createCertExtension result: success.');
    try {
      let oidList = certExt.getOidList(cert.ExtensionOidType.EXTENSION_OID_TYPE_ALL);
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`ext getOidList failed, errCode: ${e.code}, errMsg: ${e.message}`);
    }
  }
});
```

## hasUnsupportedCriticalExtension

```TypeScript
hasUnsupportedCriticalExtension(): boolean
```

判断是否存在不支持的关键扩展。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CertExtension-hasUnsupportedCriticalExtension(): boolean--><!--Device-CertExtension-hasUnsupportedCriticalExtension(): boolean-End-->

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## 示例

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let encodingData = new Uint8Array([
  0x30, 0x40, 0x30, 0x0F, 0x06, 0x03, 0x55, 0x1D,
  0x13, 0x01, 0x01, 0xFF, 0x04, 0x05, 0x30, 0x03,
  0x01, 0x01, 0xFF, 0x30, 0x0E, 0x06, 0x03, 0x55,
  0x1D, 0x0F, 0x01, 0x01, 0xFF, 0x04, 0x04, 0x03,
  0x02, 0x01, 0xC6, 0x30, 0x1D, 0x06, 0x03, 0x55,
  0x1D, 0x0E, 0x04, 0x16, 0x04, 0x14, 0xE0, 0x8C,
  0x9B, 0xDB, 0x25, 0x49, 0xB3, 0xF1, 0x7C, 0x86,
  0xD6, 0xB2, 0x42, 0x87, 0x0B, 0xD0, 0x6B, 0xA0,
  0xD9, 0xE4
]);
let encodingBlob: cert.EncodingBlob = {
  data: new Uint8Array(encodingData),
  encodingFormat: cert.EncodingFormat.FORMAT_DER
};

cert.createCertExtension(encodingBlob).then((extensionObj) => {
  console.info('createCertExtension result: success.');
  const result = extensionObj.hasUnsupportedCriticalExtension()
  console.info('has unsupported critical extension result =' + result);
}).catch((err: BusinessError) => {
  console.error(`createCertExtension failed, errCode: ${err.code}, errMsg: ${err.message}`);
});
```
