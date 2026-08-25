# verifyCertChain

## Modules to Import

```TypeScript
import { networkSecurity } from 'kits/@kit.NetworkKit';
```

## verifyCertChain

```TypeScript
export function verifyCertChain(cert: CertBlob[], caCert?: CertBlob, hostname?: string): Promise<CertBlob[]>
```

Verifies the server certificate chain and returns a sorted chain.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cert | [CertBlob[]](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-certblob-i.md) | Yes |
| caCert | [CertBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-certblob-i.md) | No |
| [hostname](../../apis-arkts/arkts-apis/arkts-arkts-url-url-c.md) | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;CertBlob[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2305001](../errorcode-net-networkSecurity.md#2305001-unspecified-error) |
| [2305002](../errorcode-net-networkSecurity.md#2305002-failed-to-obtain-the-issuer-certificate) |
| [2305004](../errorcode-net-networkSecurity.md#2305004-failed-to-decrypt-the-certificate-signature) |
| [2305006](../errorcode-net-networkSecurity.md#2305006-failed-to-decode-the-issuer-public-key) |
| [2305007](../errorcode-net-networkSecurity.md#2305007-failed-to-sign-the-certificate) |
| [2305009](../errorcode-net-networkSecurity.md#2305009-invalid-certificate) |
| [2305010](../errorcode-net-networkSecurity.md#2305010-certificate-expired) |
| [2305018](../errorcode-net-networkSecurity.md#2305018-self-signed-certificate) |
| [2305024](../errorcode-net-networkSecurity.md#2305024-invalid-ca) |
| [2305027](../errorcode-net-networkSecurity.md#2305027-untrusted-certificate) |
| 2305062 |
| [2305069](../errorcode-net-networkSecurity.md#2305069-invalid-certificate-verification-context) |
