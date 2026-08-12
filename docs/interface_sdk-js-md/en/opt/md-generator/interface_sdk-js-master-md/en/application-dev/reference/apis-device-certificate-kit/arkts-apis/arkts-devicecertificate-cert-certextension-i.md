# CertExtension

Provides APIs for operating on certificate extensions.

**Since:** 10

<!--Device-cert-interface CertExtension--><!--Device-cert-interface CertExtension-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
```

## checkCA

```TypeScript
checkCA(): number
```

Checks whether the certificate is a CA certificate.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertExtension-checkCA(): int--><!--Device-CertExtension-checkCA(): int-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020002-runtime-error) |
| [19020001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020001-memory-error) |
| [19030001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030001-crypto-operation-error) |

## Examples

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Binary data of the certificate extension, which needs to be set to match your case.
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
  // Assign a value based on the encodingData format. Currently, only FORMAT_DER is supported.
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

Obtains the serialized data of the certificate extensions.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertExtension-getEncoded(): EncodingBlob--><!--Device-CertExtension-getEncoded(): EncodingBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [EncodingBlob](arkts-devicecertificate-cert-encodingblob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020002-runtime-error) |
| [19020001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020001-memory-error) |
| [19030001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030001-crypto-operation-error) |

## Examples

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Binary data of the certificate extension, which needs to be set to match your case.
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
  // Assign a value based on the encodingData format. Currently, only FORMAT_DER is supported.
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

Obtains the value of a specific certificate extension entry by OID.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertExtension-getEntry(valueType: ExtensionEntryType, oid: DataBlob): DataBlob--><!--Device-CertExtension-getEntry(valueType: ExtensionEntryType, oid: DataBlob): DataBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [valueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-scanneroptionvalue-i.md) | [ExtensionEntryType](arkts-devicecertificate-cert-extensionentrytype-e.md) | Yes |
| oid | [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020002-runtime-error) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [19020001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020001-memory-error) |
| [19030001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030001-crypto-operation-error) |

## Examples

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Binary data of the certificate extension, which needs to be set to match your case.
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
  // Assign a value based on the encodingData format. Currently, only FORMAT_DER is supported.
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

Obtains the OIDs of the certificate extensions.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertExtension-getOidList(valueType: ExtensionOidType): DataArray--><!--Device-CertExtension-getOidList(valueType: ExtensionOidType): DataArray-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [valueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-scanneroptionvalue-i.md) | [ExtensionOidType](arkts-devicecertificate-cert-extensionoidtype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataArray](arkts-devicecertificate-cert-dataarray-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020002-runtime-error) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [19020001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020001-memory-error) |
| [19030001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030001-crypto-operation-error) |

## Examples

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Binary data of the certificate extension, which needs to be set to match your case.
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
  // Assign a value based on the encodingData format. Currently, only FORMAT_DER is supported.
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

Checks whether there is a critical extension that is not supported.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertExtension-hasUnsupportedCriticalExtension(): boolean--><!--Device-CertExtension-hasUnsupportedCriticalExtension(): boolean-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020002-runtime-error) |
| [19020001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020001-memory-error) |
| [19030001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030001-crypto-operation-error) |

## Examples

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
