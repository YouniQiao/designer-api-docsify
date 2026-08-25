# createCertCRLCollection

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## createCertCRLCollection

```TypeScript
function createCertCRLCollection(certs: Array<X509Cert>, crls?: Array<X509CRL>): CertCRLCollection
```

Creates an object for a collection of X.509 certificates and CRLs.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [certs](../../apis-universal-keystore-kit/arkts-apis/arkts-universalkeystore-security-cryptoextensionability-hukscryptoextensionresult-i.md) | Array & lt;X509Cert & gt; | Yes |
| [crls](arkts-devicecertificate-cert-x509certrevokedparams-i.md) | Array&lt;[X509CRL](arkts-devicecertificate-cert-x509crl-i.md)&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CertCRLCollection](arkts-devicecertificate-cert-certcrlcollection-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
