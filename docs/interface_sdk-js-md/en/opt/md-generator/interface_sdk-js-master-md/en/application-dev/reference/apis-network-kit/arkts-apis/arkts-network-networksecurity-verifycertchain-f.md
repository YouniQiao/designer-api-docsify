# verifyCertChain

## Modules to Import

```TypeScript
import { networkSecurity } from '@kit.NetworkKit';
```

## verifyCertChain

```TypeScript
export function verifyCertChain(cert: CertBlob[], caCert?: CertBlob, hostname?: string): Promise<CertBlob[]>
```

Verifies the server certificate chain and returns a sorted chain.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-networkSecurity-export function verifyCertChain(cert: CertBlob[], caCert?: CertBlob, hostname?: string): Promise<CertBlob[]>--><!--Device-networkSecurity-export function verifyCertChain(cert: CertBlob[], caCert?: CertBlob, hostname?: string): Promise<CertBlob[]>-End-->

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
| [2305027](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-networkSecurity.md#2305027-untrusted-certificate) |
| [2305010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-networkSecurity.md#2305010-certificate-expired) |
| [2305009](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-networkSecurity.md#2305009-invalid-certificate) |
| [2305024](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-networkSecurity.md#2305024-invalid-ca) |
| 2305062 |
| [2305002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-networkSecurity.md#2305002-failed-to-obtain-the-issuer-certificate) |
| [2305018](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-networkSecurity.md#2305018-selfsigned-certificate) |
| [2305001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-networkSecurity.md#2305001-unspecified-error) |
| [2305007](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-networkSecurity.md#2305007-failed-to-sign-the-certificate) |
| [2305006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-networkSecurity.md#2305006-failed-to-decode-the-issuer-public-key) |
| [2305069](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-networkSecurity.md#2305069-invalid-certificate-verification-context) |
| [2305004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-networkSecurity.md#2305004-failed-to-decrypt-the-certificate-signature) |
