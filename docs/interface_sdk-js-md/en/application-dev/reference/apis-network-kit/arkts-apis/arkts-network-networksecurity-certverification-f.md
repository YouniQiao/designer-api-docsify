# certVerification

## Modules to Import

```TypeScript
import { networkSecurity } from 'kits/@kit.NetworkKit';
```

## certVerification

```TypeScript
export function certVerification(cert: CertBlob, caCert?: CertBlob): Promise<int>
```

Certificate verification to the server.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-networkSecurity-export function certVerification(cert: CertBlob, caCert?: CertBlob): Promise<int>--><!--Device-networkSecurity-export function certVerification(cert: CertBlob, caCert?: CertBlob): Promise<int>-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cert | [CertBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-certblob-i.md) | Yes | Certificates to be verified. |
| caCert | [CertBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-certblob-i.md) | No | Incoming custom CA cert. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | The promise returned by the function. Number equals 0 if verify of certification from server succeed, else verify failed. |

**Error codes:**

| Error Code ID | Error Message |
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

## Examples

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

