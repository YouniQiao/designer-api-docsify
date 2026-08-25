# X509CertChain

Provides APIs for managing the X.509 certificate chain.

**Since:** 11

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## getCertList

```TypeScript
getCertList(): Array<X509Cert>
```

Obtains the X.509 certificate list.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;X509Cert & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## hashCode

```TypeScript
hashCode(): Uint8Array
```

Obtains the hash value of the data in DER format.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## toString

```TypeScript
toString(): string
```

Converts the object data into a string.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## validate

```TypeScript
validate(param: CertChainValidationParameters): Promise<CertChainValidationResult>
```

Validates a certificate chain. This API uses a promise to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| param | [CertChainValidationParameters](arkts-devicecertificate-cert-certchainvalidationparameters-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[CertChainValidationResult](arkts-devicecertificate-cert-certchainvalidationresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |
| [19030002](../errorcode-cert.md#19030002-certificate-signature-verification-failed) |
| [19030003](../errorcode-cert.md#19030003-certificate-has-not-taken-effect) |
| [19030004](../errorcode-cert.md#19030004-certificate-expired) |
| [19030005](../errorcode-cert.md#19030005-failed-to-obtain-the-certificate-issuer) |
| [19030006](../errorcode-cert.md#19030006-key-cannot-be-used-for-signing-a-certificate) |
| [19030007](../errorcode-cert.md#19030007-key-cannot-be-used-for-digital-signature) |

## validate

```TypeScript
validate(param: CertChainValidationParameters, callback: AsyncCallback<CertChainValidationResult>): void
```

Validates a certificate chain. This API uses an asynchronous callback to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| param | [CertChainValidationParameters](arkts-devicecertificate-cert-certchainvalidationparameters-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CertChainValidationResult](arkts-devicecertificate-cert-certchainvalidationresult-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |
| [19030002](../errorcode-cert.md#19030002-certificate-signature-verification-failed) |
| [19030003](../errorcode-cert.md#19030003-certificate-has-not-taken-effect) |
| [19030004](../errorcode-cert.md#19030004-certificate-expired) |
| [19030005](../errorcode-cert.md#19030005-failed-to-obtain-the-certificate-issuer) |
| [19030006](../errorcode-cert.md#19030006-key-cannot-be-used-for-signing-a-certificate) |
| [19030007](../errorcode-cert.md#19030007-key-cannot-be-used-for-digital-signature) |
