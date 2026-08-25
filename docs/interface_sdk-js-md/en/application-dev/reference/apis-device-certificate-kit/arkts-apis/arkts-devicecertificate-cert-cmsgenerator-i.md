# CmsGenerator

Provides APIs for generating the messages in CMS format.

> **NOTE：**&gt;
> PKCS #7 is a standard syntax for storing signed or encrypted data. CMS is an extension of PKCS #7. PKCS #7
> supports data types including data, signed data, enveloped data, signed and enveloped data, digested
> data, and encrypted data. It is often used to protect data integrity and confidentiality.

**Since:** 18

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## addCert

```TypeScript
addCert(cert: X509Cert): void
```

Adds a CMS certificate of the **SIGNED_DATA** content type, for example, the issuer certificate of a signing certificate.

If the **addSigner** API is not called and only the certificate is added, the generated CMS signed data contains only the certificate.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [cert](arkts-security-cert.md) | [X509Cert](../../apis-network-kit/arkts-apis/arkts-network-http-x509cert-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## addRecipientInfo

```TypeScript
addRecipientInfo(recipientInfo: CmsRecipientInfo): Promise<void>
```

Adds recipient information to a CMS with the content type of **ENVELOPED_DATA**. This API uses a promise to return the result.

At least one recipient needs to be set.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| recipientInfo | [CmsRecipientInfo](arkts-devicecertificate-cert-cmsrecipientinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020003](../errorcode-cert.md#19020003-parameter-check-failure) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## addSigner

```TypeScript
addSigner(cert: X509Cert, keyInfo: PrivateKeyInfo, config: CmsSignerConfig): void
```

Adds signer information to the CMS whose content type is **SIGNED_DATA**.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [cert](arkts-security-cert.md) | [X509Cert](../../apis-network-kit/arkts-apis/arkts-network-http-x509cert-t.md) | Yes |
| [keyInfo](arkts-devicecertificate-cert-cmsenvelopeddecryptionconfig-i.md) | [PrivateKeyInfo](arkts-devicecertificate-cert-privatekeyinfo-i.md) | Yes |
| config | [CmsSignerConfig](arkts-devicecertificate-cert-cmssignerconfig-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |
| [19030008](../errorcode-cert.md#19030008-incorrect-private-key-password) |

## doFinal

```TypeScript
doFinal(data: Uint8Array, options?: CmsGeneratorOptions): Promise<Uint8Array | string>
```

Obtains the CMS message, for example, the CMS signed data or CMS enveloped data. This API uses a promise to return the result.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | Uint8Array | Yes |
| options | [CmsGeneratorOptions](arkts-devicecertificate-cert-cmsgeneratoroptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Uint8Array \ | string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## doFinalSync

```TypeScript
doFinalSync(data: Uint8Array, options?: CmsGeneratorOptions): Uint8Array | string
```

Obtains the CMS message, for example, the CMS signed data or CMS enveloped data. This API returns the result synchronously.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | Uint8Array | Yes |
| options | [CmsGeneratorOptions](arkts-devicecertificate-cert-cmsgeneratoroptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array \| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getEncryptedContentData

```TypeScript
getEncryptedContentData(): Promise<Uint8Array>
```

Obtains the encrypted content data of the CMS whose content type is **ENVELOPED_DATA**. This API uses a promise to return the result.

Obtains the encrypted content data if the **CmsGenerator** of the **ENVELOPED_DATA** type is created and data separation is used to generate detached CMS enveloped data.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Uint8Array & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## setRecipientEncryptionAlgorithm

```TypeScript
setRecipientEncryptionAlgorithm(algorithm: CmsRecipientEncryptionAlgorithm): void
```

Sets the encryption algorithm for the CMS whose content type is **ENVELOPED_DATA**.

This method should be called immediately after the **CmsGenerator** of the **ENVELOPED_DATA** type is created. If this method is not called, AES_256_GCM is used as the encryption algorithm by default.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [algorithm](arkts-devicecertificate-cert-certchainvalidator-i.md) | [CmsRecipientEncryptionAlgorithm](arkts-devicecertificate-cert-cmsrecipientencryptionalgorithm-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020003](../errorcode-cert.md#19020003-parameter-check-failure) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |
