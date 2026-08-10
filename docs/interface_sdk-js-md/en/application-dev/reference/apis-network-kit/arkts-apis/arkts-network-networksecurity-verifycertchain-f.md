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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-networkSecurity-export function verifyCertChain(cert: CertBlob[], caCert?: CertBlob, hostname?: string): Promise<CertBlob[]>--><!--Device-networkSecurity-export function verifyCertChain(cert: CertBlob[], caCert?: CertBlob, hostname?: string): Promise<CertBlob[]>-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cert | [CertBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-certblob-i.md)[] | Yes | Certificate chain to be verified. |
| caCert | [CertBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-certblob-i.md) | No | Incoming custom CA cert. |
| hostname | string | No | Hostname to be verified. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;CertBlob[]&gt; | Returns a promise that resolves to the sorted certificate chain (ordered from leaf to root) if verification succeeds. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 2305027 | Certificate is untrusted. |
| 2305010 | Certificate has expired. |
| 2305009 | Certificate is not yet valid. |
| 2305024 | Invalid certificate authority (CA). |
| 2305062 | Invalid hostname. |
| 2305002 | Unable to get issuer certificate. |
| 2305018 | Self-signed certificate. |
| 2305001 | Unspecified error. |
| 2305007 | Certificate signature failure. |
| 2305006 | Unable to decode issuer public key. |
| 2305069 | Invalid certificate verification context. |
| 2305004 | Unable to decrypt certificate signature. |

