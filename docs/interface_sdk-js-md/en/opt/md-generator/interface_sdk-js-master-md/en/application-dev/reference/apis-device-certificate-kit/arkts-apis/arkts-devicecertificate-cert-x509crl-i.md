# X509CRL

Provides APIs for X.509 CRL operations.

**Since:** 23

**Deprecated since:** -1

<!--Device-cert-interface X509CRL--><!--Device-cert-interface X509CRL-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
```

## getEncoded

```TypeScript
getEncoded(callback: AsyncCallback<EncodingBlob>): void
```

Obtains the serialized X.509 CRL data. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getEncoded(callback: AsyncCallback<EncodingBlob>): void--><!--Device-X509CRL-getEncoded(callback: AsyncCallback<EncodingBlob>): void-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[EncodingBlob](arkts-devicecertificate-cert-encodingblob-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getEncoded

```TypeScript
getEncoded(): Promise<EncodingBlob>
```

Obtains the serialized X.509 CRL data. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getEncoded(): Promise<EncodingBlob>--><!--Device-X509CRL-getEncoded(): Promise<EncodingBlob>-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[EncodingBlob](arkts-devicecertificate-cert-encodingblob-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getExtensions

```TypeScript
getExtensions(): DataBlob
```

Obtains the CRL extensions data in DER format.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getExtensions(): DataBlob--><!--Device-X509CRL-getExtensions(): DataBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getExtensionsObject

```TypeScript
getExtensionsObject(): CertExtension
```

Obtains the CRL extension object.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-X509CRL-getExtensionsObject(): CertExtension--><!--Device-X509CRL-getExtensionsObject(): CertExtension-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CertExtension](arkts-devicecertificate-cert-certextension-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getIssuerName

```TypeScript
getIssuerName(): DataBlob
```

Obtains the issuer of the X.509 CRL. > **NOTE：**> > The obtained X.509 CRL issuer name contains a string terminator.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getIssuerName(): DataBlob--><!--Device-X509CRL-getIssuerName(): DataBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getIssuerName

```TypeScript
getIssuerName(encodingType: EncodingType): string
```

Obtains the issuer name of an X.509 CRL based on the encoding type.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-X509CRL-getIssuerName(encodingType: EncodingType): string--><!--Device-X509CRL-getIssuerName(encodingType: EncodingType): string-End-->

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
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020003](../errorcode-cert.md#19020003-parameter-check-failure) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getIssuerX500DistinguishedName

```TypeScript
getIssuerX500DistinguishedName(): X500DistinguishedName
```

Obtains the distinguished name (DN) of the X.509 CRL issuer.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-X509CRL-getIssuerX500DistinguishedName(): X500DistinguishedName--><!--Device-X509CRL-getIssuerX500DistinguishedName(): X500DistinguishedName-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [X500DistinguishedName](arkts-devicecertificate-cert-x500distinguishedname-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getLastUpdate

```TypeScript
getLastUpdate(): string
```

Obtains the last update date of this X.509 CRL.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getLastUpdate(): string--><!--Device-X509CRL-getLastUpdate(): string-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getNextUpdate

```TypeScript
getNextUpdate(): string
```

Obtains the next update date of this CRL.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getNextUpdate(): string--><!--Device-X509CRL-getNextUpdate(): string-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getRevokedCert

```TypeScript
getRevokedCert(serialNumber: bigint): X509CRLEntry
```

Obtains the revoked certificate entry from the X.509 CRL based on the specified serial number.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getRevokedCert(serialNumber: bigint): X509CRLEntry--><!--Device-X509CRL-getRevokedCert(serialNumber: bigint): X509CRLEntry-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| serialNumber | bigint | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [X509CRLEntry](arkts-devicecertificate-cert-x509crlentry-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getRevokedCertWithCert

```TypeScript
getRevokedCertWithCert(cert: X509Cert): X509CRLEntry
```

Obtains the revoked certificate entry from the X.509 CRL based on the specified certificate.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getRevokedCertWithCert(cert: X509Cert): X509CRLEntry--><!--Device-X509CRL-getRevokedCertWithCert(cert: X509Cert): X509CRLEntry-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [cert](arkts-security-cert.md) | [X509Cert](../../apis-network-kit/arkts-apis/arkts-network-http-x509cert-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [X509CRLEntry](arkts-devicecertificate-cert-x509crlentry-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getRevokedCerts

```TypeScript
getRevokedCerts(callback: AsyncCallback<Array<X509CRLEntry>>): void
```

Obtains all the revoked certificate entries from the X.509 CRL. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getRevokedCerts(callback: AsyncCallback<Array<X509CRLEntry>>): void--><!--Device-X509CRL-getRevokedCerts(callback: AsyncCallback<Array<X509CRLEntry>>): void-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[X509CRLEntry](arkts-devicecertificate-cert-x509crlentry-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getRevokedCerts

```TypeScript
getRevokedCerts(): Promise<Array<X509CRLEntry>>
```

Obtains all the revoked certificate entries from the X.509 CRL. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getRevokedCerts(): Promise<Array<X509CRLEntry>>--><!--Device-X509CRL-getRevokedCerts(): Promise<Array<X509CRLEntry>>-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[X509CRLEntry](arkts-devicecertificate-cert-x509crlentry-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getSignature

```TypeScript
getSignature(): DataBlob
```

Obtains the signature data of the X.509 CRL.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getSignature(): DataBlob--><!--Device-X509CRL-getSignature(): DataBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getSignatureAlgName

```TypeScript
getSignatureAlgName(): string
```

Obtains the signing algorithm of the X.509 CRL.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getSignatureAlgName(): string--><!--Device-X509CRL-getSignatureAlgName(): string-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getSignatureAlgOid

```TypeScript
getSignatureAlgOid(): string
```

Obtains the OID of the X.509 CRL signing algorithm. OIDs are allocated by the International Organization for Standardization (ISO).

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getSignatureAlgOid(): string--><!--Device-X509CRL-getSignatureAlgOid(): string-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getSignatureAlgParams

```TypeScript
getSignatureAlgParams(): DataBlob
```

Obtains the parameters of the X.509 CRL signing algorithm.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getSignatureAlgParams(): DataBlob--><!--Device-X509CRL-getSignatureAlgParams(): DataBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getTBSInfo

```TypeScript
getTBSInfo(): DataBlob
```

Obtains the DER-encoded CRL information, that is, **tbsCertList** from this CRL.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getTBSInfo(): DataBlob--><!--Device-X509CRL-getTBSInfo(): DataBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getType

```TypeScript
getType(): string
```

Obtains the CRL type.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getType(): string--><!--Device-X509CRL-getType(): string-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getVersion

```TypeScript
getVersion(): number
```

Obtains the version of the X.509 CRL.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getVersion(): int--><!--Device-X509CRL-getVersion(): int-End-->

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

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-X509CRL-hashCode(): Uint8Array--><!--Device-X509CRL-hashCode(): Uint8Array-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## isRevoked

```TypeScript
isRevoked(cert: X509Cert): boolean
```

Checks whether an X.509 certificate is revoked.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-isRevoked(cert: X509Cert): boolean--><!--Device-X509CRL-isRevoked(cert: X509Cert): boolean-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [cert](arkts-security-cert.md) | [X509Cert](../../apis-network-kit/arkts-apis/arkts-network-http-x509cert-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## match

```TypeScript
match(param: X509CRLMatchParameters): boolean
```

Checks whether this CRL matches the specified parameters.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-match(param: X509CRLMatchParameters): boolean--><!--Device-X509CRL-match(param: X509CRLMatchParameters): boolean-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| param | [X509CRLMatchParameters](arkts-devicecertificate-cert-x509crlmatchparameters-i.md) | Yes |

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

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-X509CRL-toString(): string--><!--Device-X509CRL-toString(): string-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## toString

```TypeScript
toString(encodingType: EncodingType): string
```

Converts this object into a string in the specified encoding format.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-X509CRL-toString(encodingType: EncodingType): string--><!--Device-X509CRL-toString(encodingType: EncodingType): string-End-->

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
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020003](../errorcode-cert.md#19020003-parameter-check-failure) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## verify

```TypeScript
verify(key: cryptoFramework.PubKey, callback: AsyncCallback<void>): void
```

Verifies the signature of the X.509 CRL. The RSA algorithm is supported. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-verify(key: cryptoFramework.PubKey, callback: AsyncCallback<void>): void--><!--Device-X509CRL-verify(key: cryptoFramework.PubKey, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | cryptoFramework.PubKey | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## verify

```TypeScript
verify(key: cryptoFramework.PubKey): Promise<void>
```

Verifies the signature of the X.509 CRL. The RSA algorithm is supported. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-verify(key: cryptoFramework.PubKey): Promise<void>--><!--Device-X509CRL-verify(key: cryptoFramework.PubKey): Promise<void>-End-->

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
