# certVerification

## Modules to Import

```TypeScript
import { networkSecurity } from '@kit.NetworkKit';
```

## certVerification

```TypeScript
export function certVerification(cert: CertBlob, caCert?: CertBlob): Promise<int>
```

Verifies the certificate passed by the application using the preset CA certificate and the CA certificate installed by the user in the certificate management. This API uses a promise to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cert | [CertBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-certblob-i.md) | Yes |
| caCert | [CertBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-certblob-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| ArkTS-Dyn: Promise & lt;number & gt;<br>ArkTS-Sta：Promise & lt;int & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2305001](../errorcode-net-networkSecurity.md#2305001-unspecified-error) |
| [2305002](../errorcode-net-networkSecurity.md#2305002-failed-to-obtain-the-issuer-certificate) |
| [2305003](../errorcode-net-networkSecurity.md#2305003-failed-to-obtain-the-certificate-revocation-list) |
| [2305004](../errorcode-net-networkSecurity.md#2305004-failed-to-decrypt-the-certificate-signature) |
| [2305005](../errorcode-net-networkSecurity.md#2305005-failed-to-decrypt-the-crl-signature) |
| [2305006](../errorcode-net-networkSecurity.md#2305006-failed-to-decode-the-issuer-public-key) |
| [2305007](../errorcode-net-networkSecurity.md#2305007-failed-to-sign-the-certificate) |
| [2305008](../errorcode-net-networkSecurity.md#2305008-failed-to-sign-the-crl) |
| [2305009](../errorcode-net-networkSecurity.md#2305009-invalid-certificate) |
| [2305010](../errorcode-net-networkSecurity.md#2305010-certificate-expired) |
| [2305011](../errorcode-net-networkSecurity.md#2305011-invalid-crl) |
| [2305012](../errorcode-net-networkSecurity.md#2305012-crl-expired) |
| [2305023](../errorcode-net-networkSecurity.md#2305023-certificate-revoked) |
| [2305024](../errorcode-net-networkSecurity.md#2305024-invalid-ca) |
| [2305027](../errorcode-net-networkSecurity.md#2305027-untrusted-certificate) |
| [2305018](../errorcode-net-networkSecurity.md#2305018-self-signed-certificate) |
| [2305069](../errorcode-net-networkSecurity.md#2305069-invalid-certificate-verification-context) |

**Examples**

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
