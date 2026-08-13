# buildX509CertChain

## Modules to Import

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
```

## buildX509CertChain

```TypeScript
function buildX509CertChain(param: CertChainBuildParameters): Promise<CertChainBuildResult>
```

Builds an X.509 certificate chain with a CertChainBuildParameters object. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-cert-function buildX509CertChain(param: CertChainBuildParameters): Promise<CertChainBuildResult>--><!--Device-cert-function buildX509CertChain(param: CertChainBuildParameters): Promise<CertChainBuildResult>-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | [CertChainBuildParameters](arkts-devicecertificate-cert-certchainbuildparameters-i.md) | Yes | Object used to build the certificate chain.&lt;br&gt; The value of **maxLength** in [CertChainBuildParameters](arkts-devicecertificate-cert-certchainbuildparameters-i.md#CertChainBuildParameters) must be less than the number of certificates in the certificate set. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[CertChainBuildResult](arkts-devicecertificate-cert-certchainbuildresult-i.md)&gt; | Promise used to return the **CertChainBuildResult** object created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) | Runtime error. Possible causes: &lt;br&gt;1. Memory copy failed; &lt;br&gt;2. A null pointer occurs inside the system; &lt;br&gt;3. Failed to obtain the native object or convert parameters. |
| [19030002](../errorcode-cert.md#19030002-certificate-signature-verification-failed) | The certificate signature verification failed. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [19030003](../errorcode-cert.md#19030003-certificate-has-not-taken-effect) | The certificate has not taken effect. |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |
| [19030006](../errorcode-cert.md#19030006-key-cannot-be-used-for-signing-a-certificate) | The key cannot be used for signing a certificate. |
| [19030007](../errorcode-cert.md#19030007-key-cannot-be-used-for-digital-signature) | The key cannot be used for a digital signature. |
| [19030004](../errorcode-cert.md#19030004-certificate-expired) | The certificate has expired. |
| [19030005](../errorcode-cert.md#19030005-failed-to-obtain-the-certificate-issuer) | Failed to obtain the certificate issuer. |

