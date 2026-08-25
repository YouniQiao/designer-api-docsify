# X509Cert

Provides APIs for X.509 certificate operations.

**Since:** 9

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## checkValidityWithDate

```TypeScript
checkValidityWithDate(date: string): void
```

Checks the validity period of this X.509 certificate.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| date | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |
| [19030003](../errorcode-cert.md#19030003-certificate-has-not-taken-effect) |
| [19030004](../errorcode-cert.md#19030004-certificate-expired) |

## getBasicConstraints

```TypeScript
getBasicConstraints(): number
```

Obtains the basic constraints of this X.509 certificate.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getCertSerialNumber

```TypeScript
getCertSerialNumber(): bigint
```

Obtains the X.509 certificate serial number.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| bigint |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |

## getCRLDistributionPoint

```TypeScript
getCRLDistributionPoint(): DataArray
```

Obtains the CRL distribution points of this X.509 certificate.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataArray](arkts-devicecertificate-cert-dataarray-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getEncoded

```TypeScript
getEncoded(callback: AsyncCallback<EncodingBlob>): void
```

Obtains the serialized X.509 certificate data. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[EncodingBlob](arkts-devicecertificate-cert-encodingblob-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getEncoded

```TypeScript
getEncoded(): Promise<EncodingBlob>
```

Obtains the serialized X.509 certificate data. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[EncodingBlob](arkts-devicecertificate-cert-encodingblob-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getExtensionsObject

```TypeScript
getExtensionsObject(): CertExtension
```

Obtains the certificate extension object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CertExtension](arkts-devicecertificate-cert-certextension-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getExtKeyUsage

```TypeScript
getExtKeyUsage(): DataArray
```

Obtains the usage of the extended key of this X.509 certificate.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataArray](arkts-devicecertificate-cert-dataarray-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getIssuerAltNames

```TypeScript
getIssuerAltNames(): DataArray
```

Obtains the Issuer Alternative Names (IANs) of this X.509 certificate.

> **NOTE：**&gt;
> The obtained IANs contain a string terminator.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataArray](arkts-devicecertificate-cert-dataarray-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getIssuerName

```TypeScript
getIssuerName(): DataBlob
```

Obtains the issuer name of this X.509 certificate.

> **NOTE：**&gt;
> - The obtained X.509 certificate issuer name ends with a NUL terminator (value 0). Determine whether to remove
> this terminator based on your business requirements.
> - The obtained certificate issuer name is ASCII-encoded. When converted to a string, it is a distinguished name
> string that starts with a slash (/) and uses slashes (/) to separate relative distinguished names.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataBlob](arkts-devicecertificate-cert-datablob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getIssuerName

```TypeScript
getIssuerName(encodingType: EncodingType): string
```

Obtains the issuer name of this X.509 certificate based on the encoding type.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [encodingType](../../apis-audio-kit/arkts-apis/arkts-audio-audio-audiostreaminfo-i.md) | [EncodingType](arkts-devicecertificate-cert-encodingtype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020003](../errorcode-cert.md#19020003-parameter-check-failure) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getIssuerX500DistinguishedName

```TypeScript
getIssuerX500DistinguishedName(): X500DistinguishedName
```

Obtains the X.500 distinguished name object of the X.509 certificate issuer.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [X500DistinguishedName](arkts-devicecertificate-cert-x500distinguishedname-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getItem

```TypeScript
getItem(itemType: CertItemType): DataBlob
```

Obtains the fields in the X.509 certificate.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [itemType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-iteminfo-c.md) | [CertItemType](arkts-devicecertificate-cert-certitemtype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataBlob](arkts-devicecertificate-cert-datablob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getKeyUsage

```TypeScript
getKeyUsage(): DataBlob
```

Obtains the key usage of this X.509 certificate.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataBlob](arkts-devicecertificate-cert-datablob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getNotAfterTime

```TypeScript
getNotAfterTime(): string
```

Obtains the expiration time of this X.509 certificate.

**Since:** 9

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

## getNotBeforeTime

```TypeScript
getNotBeforeTime(): string
```

Obtains the start time of this X.509 certificate.

**Since:** 9

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

## getPublicKey

```TypeScript
getPublicKey(): cryptoFramework.PubKey
```

Obtains the public key of this X.509 certificate.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| cryptoFramework.PubKey |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getSerialNumber

```TypeScript
getSerialNumber(): number
```

Obtains the X.509 certificate serial number.

> **NOTE：**&gt;
> This API is supported since API version 9 and deprecated since API version 10. Use
> [X509Cert.getCertSerialNumber()](#getcertserialnumber) instead.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [getCertSerialNumber](#getcertserialnumber)

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getSignature

```TypeScript
getSignature(): DataBlob
```

Obtains the signature data of this X.509 certificate.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataBlob](arkts-devicecertificate-cert-datablob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getSignatureAlgName

```TypeScript
getSignatureAlgName(): string
```

Obtains the signing algorithm of this X.509 certificate.

**Since:** 9

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

## getSignatureAlgOid

```TypeScript
getSignatureAlgOid(): string
```

Obtains the object identifier (OID) of the X.509 certificate signing algorithm. OIDs are allocated by the International Organization for Standardization (ISO).

**Since:** 9

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

## getSignatureAlgParams

```TypeScript
getSignatureAlgParams(): DataBlob
```

Obtains the signing algorithm parameters of this X.509 certificate.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataBlob](arkts-devicecertificate-cert-datablob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getSubjectAltNames

```TypeScript
getSubjectAltNames(): DataArray
```

Obtains the Subject Alternative Names (SANs) of this X.509 certificate.

> **NOTE：**&gt;
> The obtained SANs contain a string terminator.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataArray](arkts-devicecertificate-cert-dataarray-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getSubjectName

```TypeScript
getSubjectName(encodingType?: EncodingType): DataBlob
```

Obtains the subject name of this X.509 certificate.

> **NOTE：**&gt;
> - If the encodingType parameter is not set, the obtained certificate subject name ends with a
> NUL terminator (value 0). Determine whether to remove this terminator based on your business requirements.
> - If the encodingType parameter is not set, the obtained certificate subject name is ASCII-encoded. When
> converted to a string, it is a distinguished name string that starts with a slash (/) and uses slashes (/) to
> separate relative distinguished names.
> - It is recommended to set the encodingType parameter to EncodingType.ENCODING_UTF8. The obtained certificate
> subject name is a distinguished name string that uses commas (,) to separate relative distinguished names.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [encodingType](../../apis-audio-kit/arkts-apis/arkts-audio-audio-audiostreaminfo-i.md) | [EncodingType](arkts-devicecertificate-cert-encodingtype-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataBlob](arkts-devicecertificate-cert-datablob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getSubjectX500DistinguishedName

```TypeScript
getSubjectX500DistinguishedName(): X500DistinguishedName
```

Obtains the X.500 distinguished name object of the X.509 certificate subject.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [X500DistinguishedName](arkts-devicecertificate-cert-x500distinguishedname-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getVersion

```TypeScript
getVersion(): number
```

Obtains the X.509 certificate version.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

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

## match

```TypeScript
match(param: X509CertMatchParameters): boolean
```

Checks whether this certificate matches the specified parameters.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| param | [X509CertMatchParameters](arkts-devicecertificate-cert-x509certmatchparameters-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
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

## toString

```TypeScript
toString(encodingType: EncodingType): string
```

Converts this object into a string in the specified encoding format.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [encodingType](../../apis-audio-kit/arkts-apis/arkts-audio-audio-audiostreaminfo-i.md) | [EncodingType](arkts-devicecertificate-cert-encodingtype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020003](../errorcode-cert.md#19020003-parameter-check-failure) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## verify

```TypeScript
verify(key: cryptoFramework.PubKey, callback: AsyncCallback<void>): void
```

Verifies the certificate signature. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | cryptoFramework.PubKey | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## verify

```TypeScript
verify(key: cryptoFramework.PubKey): Promise<void>
```

Verifies the certificate signature. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | cryptoFramework.PubKey | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |
