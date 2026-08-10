# certVerification

## 导入模块

```TypeScript
import { networkSecurity } from 'kits/@kit.NetworkKit';
```

## certVerification

```TypeScript
export function certVerification(cert: CertBlob, caCert?: CertBlob): Promise<int>
```

Certificate verification to the server.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-networkSecurity-export function certVerification(cert: CertBlob, caCert?: CertBlob): Promise<int>--><!--Device-networkSecurity-export function certVerification(cert: CertBlob, caCert?: CertBlob): Promise<int>-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cert | [CertBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-certblob-i.md) | 是 | Certificates to be verified. |
| caCert | [CertBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-certblob-i.md) | 否 | Incoming custom CA cert. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | The promise returned by the function. Number equals 0 if verify of certification from server succeed, else verify failed. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2305027 | Certificate is untrusted. |
| 2305024 | Invalid certificate authority (CA). |
| 2305003 | Unable to get certificate revocation list (CRL). |
| 2305002 | Unable to get issuer certificate. |
| 2305001 | Unspecified error. |
| 2305007 | Certificate signature failure. |
| 2305006 | Unable to decode issuer public key. |
| 2305005 | Unable to decrypt CRL signature. |
| 2305069 | Invalid certificate verification context. |
| 2305004 | Unable to decrypt certificate signature. |
| 2305011 | CRL is not yet valid. |
| 401 | Parameter error. |
| 2305010 | Certificate has expired. |
| 2305009 | Certificate is not yet valid. |
| 2305008 | CRL signature failure. |
| 2305012 | CRL has expired. |
| 2305018 | Self-signed certificate. |
| 2305023 | Certificate has been revoked. |

## 示例

```TypeScript
import { networkSecurity } from '@kit.NetworkKit';

// Define certificate blobs
const cert:networkSecurity.CertBlob = {
  type: networkSecurity.CertType.CERT_TYPE_PEM,
  data: '-----BEGIN CERTIFICATE-----\n... (certificate data) ...\n-----END CERTIFICATE-----',
};

const caCert:networkSecurity.CertBlob = {
  type: networkSecurity.CertType.CERT_TYPE_PEM,
  data: '-----BEGIN CERTIFICATE-----\n... (CA certificate data) ...\n-----END CERTIFICATE-----',
};

// Perform asynchronous certificate verification
networkSecurity.certVerification(cert, caCert)
  .then((result) => {
    console.info('Certificate verification result:', result);
  })
  .catch((error: BusinessError) => {
    console.error('Certificate verification failed:', error);
  });
```

