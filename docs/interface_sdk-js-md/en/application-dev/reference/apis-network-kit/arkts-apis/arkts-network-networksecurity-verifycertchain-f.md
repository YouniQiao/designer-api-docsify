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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-networkSecurity-export function verifyCertChain(cert: CertBlob[], caCert?: CertBlob, hostname?: string): Promise<CertBlob[]>--><!--Device-networkSecurity-export function verifyCertChain(cert: CertBlob[], caCert?: CertBlob, hostname?: string): Promise<CertBlob[]>-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cert | CertBlob[] | Yes | Certificate chain to be verified. |
| caCert | CertBlob | No | Incoming custom CA cert. |
| hostname | string | No | Hostname to be verified. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;CertBlob[]&gt; | Returns a promise that resolves to the sorted certificate chain (ordered from leaf to root) if verification succeeds. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2305027](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-networkSecurity.md#2305027-untrusted-certificate) | Certificate is untrusted. |
| [2305010](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-networkSecurity.md#2305010-certificate-expired) | Certificate has expired. |
| [2305009](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-networkSecurity.md#2305009-invalid-certificate) | Certificate is not yet valid. |
| [2305024](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-networkSecurity.md#2305024-invalid-ca) | Invalid certificate authority (CA). |
| 2305062 | Invalid hostname. |
| [2305002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-networkSecurity.md#2305002-failed-to-obtain-the-issuer-certificate) | Unable to get issuer certificate. |
| [2305018](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-networkSecurity.md#2305018-selfsigned-certificate) | Self-signed certificate. |
| [2305001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-networkSecurity.md#2305001-unspecified-error) | Unspecified error. |
| [2305007](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-networkSecurity.md#2305007-failed-to-sign-the-certificate) | Certificate signature failure. |
| [2305006](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-networkSecurity.md#2305006-failed-to-decode-the-issuer-public-key) | Unable to decode issuer public key. |
| [2305069](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-networkSecurity.md#2305069-invalid-certificate-verification-context) | Invalid certificate verification context. |
| [2305004](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-networkSecurity.md#2305004-failed-to-decrypt-the-certificate-signature) | Unable to decrypt certificate signature. |

