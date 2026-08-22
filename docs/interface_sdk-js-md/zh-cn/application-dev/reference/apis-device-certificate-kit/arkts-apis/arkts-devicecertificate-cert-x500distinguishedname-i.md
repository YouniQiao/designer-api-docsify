# X500DistinguishedName

提供X.500可分辨名称操作的API。

**起始版本：** 23

<!--Device-cert-interface X500DistinguishedName--><!--Device-cert-interface X500DistinguishedName-End-->

**系统能力：** SystemCapability.Security.Cert

## 导入模块

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { certificateManager } from '@kit.DeviceCertificateKit';
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
```

## getEncoded

```TypeScript
getEncoded(): EncodingBlob
```

获取X.500可分辨名称的DER编码数据。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-X500DistinguishedName-getEncoded(): EncodingBlob--><!--Device-X500DistinguishedName-getEncoded(): EncodingBlob-End-->

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [EncodingBlob](arkts-devicecertificate-cert-encodingblob-i.md) | X.500可分辨名称的DER编码数据。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) | Memory malloc failed. |
| [19020002](../errorcode-cert.md#19020002-运行时错误) | Runtime error. Possible causes: <br>1. Memory copy failed; <br>2. A null pointer occurs inside the system; <br>3. Failed to obtain the native object or convert parameters. |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) | Crypto operation error. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
  'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
  'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
  'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
  'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
  'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
  'Qw==\n' +
  '-----END CERTIFICATE-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Cert(encodingBlob, (error, x509Cert) => {
  if (error) {
    console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Cert result: success.');
    x509Cert.getEncoded((error, _data) => {
      if (error) {
        console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
      } else {
        console.info('getEncoded result: success.');
      }
    });
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}
function TestGetEncoded() {
  // 证书二进制数据，需业务自行赋值。
  let certData = '-----BEGIN CERTIFICATE-----\n' +
    'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
    'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
    'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
    'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
    'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
    'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
    'Qw==\n' +
    '-----END CERTIFICATE-----\n';

  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

  cert.createX509Cert(encodingBlob, (error, x509Cert) => {
    if (error) {
      console.error('createX509Cert failed, errCode: ' + error.code + ', errMsg: ' + error.message);
    } else {
      console.info('createX509Cert result: success.');
      if (x509Cert != undefined) {
        x509Cert.getEncoded((error, _data) => {
        if (error) {
          console.error('getEncoded failed, errCode: ' + error.code + ', errMsg: ' + error.message);
        } else {
          console.info('getEncoded result: success.');
        }
       });
      }
    }
  });
}
```

ArkTS-Dyn示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

// 证书二进制数据，需业务自行赋值。
let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIIBLzCB1QIUO/QDVJwZLIpeJyPjyTvE43xvE5cwCgYIKoZIzj0EAwIwGjEYMBYG\n' +
  'A1UEAwwPRXhhbXBsZSBSb290IENBMB4XDTIzMDkwNDExMjAxOVoXDTI2MDUzMDEx\n' +
  'MjAxOVowGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYI\n' +
  'KoZIzj0DAQcDQgAEHjG74yMIueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTa\n' +
  'tUsU0i/sePnrKglj2H8Abbx9PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEA\n' +
  '0ce/fvA4tckNZeB865aOApKXKlBjiRlaiuq5mEEqvNACIQDPD9WyC21MXqPBuRUf\n' +
  'BetUokslUfjT6+s/X4ByaxycAA==\n' +
  '-----END CERTIFICATE-----\n';

// 证书二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(certData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};
cert.createX509Cert(encodingBlob).then(x509Cert => {
  console.info('createX509Cert result: success.');
  x509Cert.getEncoded().then(_result => {
    console.info('getEncoded result: success.');
  }).catch((error: BusinessError) => {
    console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
  });
}).catch((error: BusinessError) => {
  console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@ohos.base';
// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}
async function TestGetEncoded() {
  // 证书二进制数据，需业务自行赋值。
  let certData = '-----BEGIN CERTIFICATE-----\n' +
    'MIIBLzCB1QIUO/QDVJwZLIpeJyPjyTvE43xvE5cwCgYIKoZIzj0EAwIwGjEYMBYG\n' +
    'A1UEAwwPRXhhbXBsZSBSb290IENBMB4XDTIzMDkwNDExMjAxOVoXDTI2MDUzMDEx\n' +
    'MjAxOVowGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYI\n' +
    'KoZIzj0DAQcDQgAEHjG74yMIueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTa\n' +
    'tUsU0i/sePnrKglj2H8Abbx9PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEA\n' +
    '0ce/fvA4tckNZeB865aOApKXKlBjiRlaiuq5mEEqvNACIQDPD9WyC21MXqPBuRUf\n' +
    'BetUokslUfjT6+s/X4ByaxycAA==\n' +
    '-----END CERTIFICATE-----\n';

  // 证书二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  try {
    let x509Cert = await cert.createX509Cert(encodingBlob);
    console.info('createX509Cert result: success.');
    try {
      await x509Cert.getEncoded();
      console.info('getEncoded result: success.');
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`getEncoded failed, ${e.code}, ${e.message}`);
    }
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509Cert failed, ${e.code}, ${e.message}`);
  }
}
```

ArkTS-Dyn示例：

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
      console.info('extEncodedBlob = ' + extEncodedBlob.data);
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      console.error(`ext getEncoded failed, errCode: ${e.code}, errMsg: ${e.message}`);
    }
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@ohos.base';

function TestGetEncoded() {
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
      console.error('createCertExtension failed, errCode: ' + error.code + ', errMsg: ' + error.message);
    } else {
      console.info('createCertExtension result: success.');
      if (certExt != undefined) {
        try {
          let extEncodedBlob = certExt.getEncoded();
          console.info('extEncodedBlob = ' + extEncodedBlob.data);
          console.info('getEncoded result: success.');
        } catch (err) {
          let e: BusinessError = err as BusinessError;
          console.error('ext getEncoded failed, errCode: ' + e.code + ', errMsg: ' + e.message);
        }
      }
    }
  });
}
```

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (error, x509Crl) => {
  if (error) {
    console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509Crl result: success.');
    x509Crl.getEncoded((error, _data) => {
      if (error) {
        console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
      } else {
        console.info('getEncoded result: success.');
      }
    });
  }
});
```

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob).then(x509Crl => {
  console.info('createX509Crl result: success.');
  x509Crl.getEncoded().then(_result => {
    console.info('getEncoded result: success.');
  }).catch((error: BusinessError) => {
    console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
  });
}).catch((error: BusinessError) => {
  console.error(`createX509Crl failed, errCode: ${error.code}, errMsg: ${error.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (error, x509CRL) => {
  if (error) {
    console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
  } else {
    console.info('createX509CRL result: success.');
    x509CRL.getEncoded((error, _data) => {
      if (error) {
        console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
      } else {
        console.info('getEncoded result: success.');
      }
    });
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function TestGetEncoded() {
  let crlData = '-----BEGIN X509 CRL-----\n' +
    'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
    'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
    'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
    'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
    '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
    'eavsH0Q3\n' +
    '-----END X509 CRL-----\n';

  // 证书吊销列表二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(crlData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

  cert.createX509CRL(encodingBlob, (error, x509CRL) => {
    if (error) {
      console.error('createX509CRL failed, errCode: ' + error.code + ', errMsg: ' + error.message);
    } else {
      if (x509CRL != undefined) {
        console.info('createX509CRL result: success.');
        x509CRL.getEncoded((error, _data) => {
          if (error) {
            console.error('getEncoded failed, errCode: ' + error.code + ', errMsg: ' + error.message);
          } else {
            console.info('getEncoded result: success.');
          }
        });
      }
    }
  });
}
```

ArkTS-Dyn示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

// 证书吊销列表二进制数据，需业务自行赋值。
let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob).then(x509CRL => {
  console.info('createX509CRL result: success.');
  x509CRL.getEncoded().then(_result => {
    console.info('getEncoded result: success.');
  }).catch((error: BusinessError) => {
    console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
  });
}).catch((error: BusinessError) => {
  console.error(`createX509CRL failed, errCode: ${error.code}, errMsg: ${error.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@ohos.base';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function TestGetEncoded() {
  let crlData = '-----BEGIN X509 CRL-----\n' +
    'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
    'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
    'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
    'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
    '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
    'eavsH0Q3\n' +
    '-----END X509 CRL-----\n';

  // 证书吊销列表二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(crlData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  try {
    let x509CRL = await cert.createX509CRL(encodingBlob);
    console.info('createX509CRL result: success.');
    let result = await x509CRL.getEncoded();
    console.info('result = ' + result.data);
    console.info('getEncoded result: success.');
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509CRL failed, ${e.code}, ${e.message}`);
  }
}
```

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (err, x509Crl) => {
  if (err) {
    console.error(`createX509Crl failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('create x509 crl result: success.');

    try {
      let serialNumber = 1000;
      let crlEntry = x509Crl.getRevokedCert(serialNumber);
      crlEntry.getEncoded((error, _data) => {
        if (error) {
          console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
        } else {
          console.info('getEncoded result: success.');
        }
      });
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getRevokedCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
    }
  }
});
```

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509Crl(encodingBlob, (err, x509Crl) => {
  if (err) {
    console.error(`createX509Crl failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('create x509 crl result: success.');

    try {
      let serialNumber = 1000;
      let crlEntry = x509Crl.getRevokedCert(serialNumber);
      crlEntry.getEncoded().then(_result => {
        console.info('getEncoded result: success.');
      }).catch((error: BusinessError) => {
        console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
      });
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getRevokedCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
    }
  }
});
```

ArkTS-Dyn示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (err, x509CRL) => {
  if (err) {
    console.error(`createX509CRL failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('create x509 CRL result: success.');

    try {
      let serialNumber = BigInt(1000);
      let crlEntry = x509CRL.getRevokedCert(serialNumber);
      crlEntry.getEncoded((error, _data) => {
        if (error) {
          console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
        } else {
          console.info('getEncoded result: success.');
        }
      });
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getRevokedCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
    }
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@ohos.base';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function TestGetEncoded() {
  let crlData = '-----BEGIN X509 CRL-----\n' +
    'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
    'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
    'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
    'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
    '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
    'eavsH0Q3\n' +
    '-----END X509 CRL-----\n';

  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(crlData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

  cert.createX509CRL(encodingBlob, (err, x509CRL) => {
    if (err) {
      console.error('createX509CRL failed, errCode: ' + err.code + ', errMsg: ' + err.message);
    } else {
      console.info('create x509 CRL result: success.');
      try {
        let serialNumber = BigInt(1000);
        if (x509CRL != undefined) {
          let crlEntry = x509CRL.getRevokedCert(serialNumber);
          crlEntry.getEncoded((error, _data) => {
            if (error) {
              console.error('getEncoded failed, errCode: ' + error.code + ', errMsg: ' + error.message);
            } else {
              console.info('getEncoded result: success.');
            }
          });
        }
      } catch (error) {
        let e: BusinessError = error as BusinessError;
        console.error('getRevokedCert failed, errCode: ' + e.code + ', errMsg: ' + e.message);
      }
    }
  });
}
```

ArkTS-Dyn示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

let crlData = '-----BEGIN X509 CRL-----\n' +
  'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
  'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
  'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
  'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
  '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
  'eavsH0Q3\n' +
  '-----END X509 CRL-----\n';

let encodingBlob: cert.EncodingBlob = {
  data: stringToUint8Array(crlData),
  // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};

cert.createX509CRL(encodingBlob, (err, x509CRL) => {
  if (err) {
    console.error(`createX509CRL failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('create x509 CRL result: success.');

    try {
      let serialNumber = BigInt(1000);
      let crlEntry = x509CRL.getRevokedCert(serialNumber);
      crlEntry.getEncoded().then(_result => {
        console.info('getEncoded result: success.');
      }).catch((error: BusinessError) => {
        console.error(`getEncoded failed, errCode: ${error.code}, errMsg: ${error.message}`);
      });
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getRevokedCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
    }
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@ohos.base';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function TestGetEncoded() {
  let crlData = '-----BEGIN X509 CRL-----\n' +
    'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
    'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
    'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
    'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
    '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
    'eavsH0Q3\n' +
    '-----END X509 CRL-----\n';

  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(crlData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  try {
    let x509CRL = await cert.createX509CRL(encodingBlob);
    let serialNumber = BigInt(1000);
    if (x509CRL != undefined) {
      let crlEntry = x509CRL.getRevokedCert(serialNumber);
      try {
        let result = await crlEntry.getEncoded();
        console.info('result = ' + result.data);
        console.info('getEncoded result: success.');
      } catch (err) {
        let e: BusinessError = err as BusinessError;
        console.error(`getEncoded failed, ${e.code}, ${e.message}`);
      }
    }
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error('getRevokedCert failed, errCode: ' + e.code + ', errMsg: ' + e.message);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let nameStr = '/CN=Example CA/OU=test cert/O=test/L=XA/ST=SX/C=CN/CN=RSA CA/CN=XTS';
async function getEncoded() {
  try {
    cert.createX500DistinguishedName(nameStr)
      .then((data) => {
        console.info('createX500DistinguishedName result: success.');
        let encodingBlobData = data.getEncoded();
        console.info('encodingBlobData = ' + encodingBlobData.data);
      })
      .catch((err: BusinessError) => {
        console.error(`createX500DistinguishedName failed, errCode: ${err.code}, errMsg: ${err.message}`);
      });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX500DistinguishedName failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@ohos.base';

let nameStr = '/CN=Example CA/OU=test cert/O=test/L=XA/ST=SX/C=CN/CN=RSA CA/CN=XTS';
async function getEncoded() {
  try {
    let data = await cert.createX500DistinguishedName(nameStr);
    console.info('createX500DistinguishedName result: success.');
    let encodingBlobData = data.getEncoded();
    console.info('getEncoded result: success.');
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error('createX500DistinguishedName catch, errCode: ' + e.code + ', errMsg: ' + e.message);
  }
}
```

## getName

```TypeScript
getName(): string
```

获取可分辨名的字符串。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-X500DistinguishedName-getName(): string--><!--Device-X500DistinguishedName-getName(): string-End-->

**系统能力：** SystemCapability.Security.Cert

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 可分辨名的字符串。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) | Memory malloc failed. |
| [19020002](../errorcode-cert.md#19020002-运行时错误) | Runtime error. Possible causes: <br>1. Memory copy failed; <br>2. A null pointer occurs inside the system; <br>3. Failed to obtain the native object or convert parameters. |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) | Crypto operation error. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let nameDer =
  new Uint8Array([48, 41, 49, 11, 48, 9, 6, 3, 85, 4, 3, 12, 2, 67, 65, 49, 13, 48, 11, 6, 3, 85, 4, 10, 12, 4, 116,
    101, 115, 116, 49, 11, 48, 9, 6, 3, 85, 4, 6, 19, 2, 67, 78]);

async function getName() {
  try {
    cert.createX500DistinguishedName(nameDer)
      .then((data) => {
        console.info('createX500DistinguishedName result: success.');
        console.info('createX500DistinguishedName getName: ' + data.getName());
      })
      .catch((err: BusinessError) => {
        console.error(`createX500DistinguishedName failed, errCode: ${err.code}, errMsg: ${err.message}`);
      });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX500DistinguishedName failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@ohos.base';

let nameDer =
  new Uint8Array([48, 41, 49, 11, 48, 9, 6, 3, 85, 4, 3, 12, 2, 67, 65, 49, 13, 48, 11, 6, 3, 85, 4, 10, 12, 4, 116,
    101, 115, 116, 49, 11, 48, 9, 6, 3, 85, 4, 6, 19, 2, 67, 78]);

async function getName() {
  try {
    let data = await cert.createX500DistinguishedName(nameDer);
    console.info('createX500DistinguishedName result: success.');
    console.info('createX500DistinguishedName getName: ' + data.getName());
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error('createX500DistinguishedName catch, errCode: ' + e.code + ', errMsg: ' + e.message);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let nameStr = '/CN=Example CA/OU=test cert/O=test/L=XA/ST=SX/C=CN/CN=RSA CA/CN=XTS';
async function getName() {
  try {
    cert.createX500DistinguishedName(nameStr)
      .then((data) => {
        console.info('createX500DistinguishedName result: success.');
        console.info('createX500DistinguishedName getName: ' + data.getName("CN"));
      })
      .catch((err: BusinessError) => {
        console.error(`createX500DistinguishedName failed, errCode: ${err.code}, errMsg: ${err.message}`);
      });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX500DistinguishedName failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@ohos.base';

let nameStr = '/CN=Example CA/OU=test cert/O=test/L=XA/ST=SX/C=CN/CN=RSA CA/CN=XTS';
async function getName() {
  try {
    let data = await cert.createX500DistinguishedName(nameStr);
    console.info('createX500DistinguishedName result: success.');
    console.info('createX500DistinguishedName getName: ' + data.getName("CN"));
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error('createX500DistinguishedName catch, errCode: ' + e.code + ', errMsg: ' + e.message);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let nameStr = '/CN=陕西@西安/OU=IT Department/O=ACME Inc./L=San Francisco/ST=California/C=US/CN=ALN C/CN=XTS';
async function getName() {
  try {
    cert.createX500DistinguishedName(nameStr)
      .then((data) => {
        console.info('createX500DistinguishedName result: success.');
        console.info('createX500DistinguishedName getName: ' + data.getName(cert.EncodingType.ENCODING_UTF8));
      })
      .catch((err: BusinessError) => {
        console.error(`createX500DistinguishedName failed, errCode: ${err.code}, errMsg: ${err.message}`);
      });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX500DistinguishedName failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@ohos.base';

let nameStr = '/CN=陕西@西安/OU=IT Department/O=ACME Inc./L=San Francisco/ST=California/C=US/CN=ALN C/CN=XTS';
async function getName() {
  try {
    let data = await cert.createX500DistinguishedName(nameStr);
    console.info('createX500DistinguishedName result: success.');
    console.info('createX500DistinguishedName getName: ' + data.getName(cert.EncodingType.ENCODING_UTF8));
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error('createX500DistinguishedName catch, errCode: ' + e.code + ', errMsg: ' + e.message);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let nameStr = '/CN=Example CA/OU=test cert/O=test/L=XA/ST=SX/C=CN/CN=RSA CA/CN=测试';
async function getName() {
  try {
    cert.createX500DistinguishedName(nameStr)
      .then((data) => {
        console.info('createX500DistinguishedName result: success.');
        console.info('createX500DistinguishedName getName: ' + data.getName("CN", cert.EncodingType.ENCODING_UTF8));
      })
      .catch((err: BusinessError) => {
        console.error(`createX500DistinguishedName failed, errCode: ${err.code}, errMsg: ${err.message}`);
      });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX500DistinguishedName failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let nameStr = '/CN=Example CA/OU=test cert/O=test/L=XA/ST=SX/C=CN/CN=RSA CA/CN=测试';
async function getName() {
  try {
    let data = await cert.createX500DistinguishedName(nameStr);
    console.info('createX500DistinguishedName result: success.');
    console.info('createX500DistinguishedName getName: ' + data.getName("CN", cert.EncodingType.ENCODING_UTF8));
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX500DistinguishedName failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
}
```

## getName

```TypeScript
getName(encodingType: EncodingType): string
```

根据指定编码格式获取可分辨名称的字符串。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-X500DistinguishedName-getName(encodingType: EncodingType): string--><!--Device-X500DistinguishedName-getName(encodingType: EncodingType): string-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encodingType | [EncodingType](arkts-devicecertificate-cert-encodingtype-e.md) | 是 | 表示编码格式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 表示可分辨名称的字符串，使用逗号分隔相对可分辨名称。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) | Memory malloc failed. |
| [19020002](../errorcode-cert.md#19020002-运行时错误) | Runtime error. Possible causes: <br>1. Memory copy failed; <br>2. A null pointer occurs inside the system; <br>3. Failed to obtain the native object or convert parameters. |
| [19020003](../errorcode-cert.md#19020003-参数检查失败) | Parameter check failed. Possible causes: <br>1. The value of encodingType is not in the EncodingType enumeration range. |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) | Crypto operation error. |

**示例**

参见 [getName](#getname)

## getName

```TypeScript
getName(type: string): Array<string>
```

按指定类型获取相对可分辨名称的字符串。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-X500DistinguishedName-getName(type: string): Array<string>--><!--Device-X500DistinguishedName-getName(type: string): Array<string>-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 指定类型的名称。如"CN"、"OU"等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;string&gt; | 相对可分辨名称的字符串数组。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [19020001](../errorcode-cert.md#19020001-内存错误) | Memory malloc failed. |
| [19020002](../errorcode-cert.md#19020002-运行时错误) | Runtime error. Possible causes: <br>1. Memory copy failed; <br>2. A null pointer occurs inside the system; <br>3. Failed to obtain the native object or convert parameters. |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) | Crypto operation error. |

**示例**

参见 [getName](#getname)

## getName

```TypeScript
getName(type: string, encodingType: EncodingType): Array<string>
```

根据指定类型和编码格式获取相对可分辨名称的字符串数组。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-X500DistinguishedName-getName(type: string, encodingType: EncodingType): Array<string>--><!--Device-X500DistinguishedName-getName(type: string, encodingType: EncodingType): Array<string>-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 指定类型的名称。如"CN"、"OU"等。 |
| encodingType | [EncodingType](arkts-devicecertificate-cert-encodingtype-e.md) | 是 | 表示编码格式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;string&gt; | 相对可分辨名称的字符串数组。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [19020001](../errorcode-cert.md#19020001-内存错误) | Memory malloc failed. |
| [19020002](../errorcode-cert.md#19020002-运行时错误) | Runtime error. Possible causes: <br>1. Memory copy failed; <br>2. A null pointer occurs inside the system; <br>3. Failed to obtain the native object or convert parameters. |
| [19020003](../errorcode-cert.md#19020003-参数检查失败) | Parameter check failed. Possible causes: <br>1. The value of encodingType is not in the EncodingType enumeration range. |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) | Crypto operation error. |

**示例**

参见 [getName](#getname)

