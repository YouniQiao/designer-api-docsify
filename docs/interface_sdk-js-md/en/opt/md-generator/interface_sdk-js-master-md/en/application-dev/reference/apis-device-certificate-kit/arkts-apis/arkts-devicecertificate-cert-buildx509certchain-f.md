# buildX509CertChain

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## buildX509CertChain

```TypeScript
function buildX509CertChain(param: CertChainBuildParameters): Promise<CertChainBuildResult>
```

Builds an X.509 certificate chain with a CertChainBuildParameters object. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-cert-function buildX509CertChain(param: CertChainBuildParameters): Promise<CertChainBuildResult>--><!--Device-cert-function buildX509CertChain(param: CertChainBuildParameters): Promise<CertChainBuildResult>-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| param | [CertChainBuildParameters](arkts-devicecertificate-cert-certchainbuildparameters-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;CertChainBuildResult&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030002](../errorcode-cert.md#19030002-certificate-signature-verification-failed) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [19030003](../errorcode-cert.md#19030003-certificate-has-not-taken-effect) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |
| [19030006](../errorcode-cert.md#19030006-key-cannot-be-used-for-signing-a-certificate) |
| [19030007](../errorcode-cert.md#19030007-key-cannot-be-used-for-digital-signature) |
| [19030004](../errorcode-cert.md#19030004-certificate-expired) |
| [19030005](../errorcode-cert.md#19030005-failed-to-obtain-the-certificate-issuer) |
