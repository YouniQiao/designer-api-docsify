# X509CRL

Provides APIs for X.509 CRL operations.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cert-interface X509CRL--><!--Device-cert-interface X509CRL-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## getEncoded

```TypeScript
getEncoded(callback: AsyncCallback<EncodingBlob>): void
```

Obtains the serialized X.509 CRL data. This API uses an asynchronous callback to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getEncoded(callback: AsyncCallback<EncodingBlob>): void--><!--Device-X509CRL-getEncoded(callback: AsyncCallback<EncodingBlob>): void-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;EncodingBlob&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the serialized X.509 CRL data obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) | Runtime error. Possible causes: &lt;br&gt;1. Memory copy failed; &lt;br&gt;2. A null pointer occurs inside the system; &lt;br&gt;3. Failed to obtain the native object or convert parameters. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## getEncoded

```TypeScript
getEncoded(): Promise<EncodingBlob>
```

Obtains the serialized X.509 CRL data. This API uses a promise to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getEncoded(): Promise<EncodingBlob>--><!--Device-X509CRL-getEncoded(): Promise<EncodingBlob>-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;EncodingBlob&gt; | Promise used to return the serialized X.509 CRL data obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) | Runtime error. Possible causes: &lt;br&gt;1. Memory copy failed; &lt;br&gt;2. A null pointer occurs inside the system; &lt;br&gt;3. Failed to obtain the native object or convert parameters. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## getExtensions

```TypeScript
getExtensions(): DataBlob
```

Obtains the CRL extensions data in DER format.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getExtensions(): DataBlob--><!--Device-X509CRL-getExtensions(): DataBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | CRL extensions data in DER format obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) | Runtime error. Possible causes: &lt;br&gt;1. Memory copy failed; &lt;br&gt;2. A null pointer occurs inside the system; &lt;br&gt;3. Failed to obtain the native object or convert parameters. |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## getExtensionsObject

```TypeScript
getExtensionsObject(): CertExtension
```

Obtains the CRL extension object.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getExtensionsObject(): CertExtension--><!--Device-X509CRL-getExtensionsObject(): CertExtension-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [CertExtension](arkts-devicecertificate-cert-certextension-i.md) | CRL extensions object obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) | Runtime error. Possible causes: &lt;br&gt;1. Memory copy failed; &lt;br&gt;2. A null pointer occurs inside the system; &lt;br&gt;3. Failed to obtain the native object or convert parameters. |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## getIssuerName

```TypeScript
getIssuerName(): DataBlob
```

Obtains the issuer of the X.509 CRL.

> **NOTE：**
> 
> The obtained X.509 CRL issuer name contains a string terminator.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getIssuerName(): DataBlob--><!--Device-X509CRL-getIssuerName(): DataBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | Issuer of the X.509 CRL obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) | Runtime error. Possible causes: &lt;br&gt;1. Memory copy failed; &lt;br&gt;2. A null pointer occurs inside the system; &lt;br&gt;3. Failed to obtain the native object or convert parameters. |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## getIssuerName

```TypeScript
getIssuerName(encodingType: EncodingType): string
```

Obtains the issuer name of an X.509 CRL based on the encoding type.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-X509CRL-getIssuerName(encodingType: EncodingType): string--><!--Device-X509CRL-getIssuerName(encodingType: EncodingType): string-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| encodingType | [EncodingType](arkts-devicecertificate-cert-encodingtype-e.md) | Yes | Encoding type. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Issuer name of an X.509 CRL, separated by commas (,). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) | Runtime error. Possible causes: &lt;br&gt;1. Memory copy failed; &lt;br&gt;2. A null pointer occurs inside the system; &lt;br&gt;3. Failed to obtain the native object or convert parameters. |
| [19020003](../errorcode-cert.md#19020003-parameter-check-failure) | Parameter check failed. Possible causes: &lt;br&gt;1. The value of encodingType is not in the EncodingType enumeration range. |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## getIssuerX500DistinguishedName

```TypeScript
getIssuerX500DistinguishedName(): X500DistinguishedName
```

Obtains the distinguished name (DN) of the X.509 CRL issuer.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getIssuerX500DistinguishedName(): X500DistinguishedName--><!--Device-X509CRL-getIssuerX500DistinguishedName(): X500DistinguishedName-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [X500DistinguishedName](arkts-devicecertificate-cert-x500distinguishedname-i.md) | DN object obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) | Runtime error. Possible causes: &lt;br&gt;1. Memory copy failed; &lt;br&gt;2. A null pointer occurs inside the system; &lt;br&gt;3. Failed to obtain the native object or convert parameters. |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## getLastUpdate

```TypeScript
getLastUpdate(): string
```

Obtains the last update date of this X.509 CRL.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getLastUpdate(): string--><!--Device-X509CRL-getLastUpdate(): string-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| string | Last update date of the X.509 CRL, in an ASN.1 time format, specifically UTCTime or GeneralizedTime. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) | Runtime error. Possible causes: &lt;br&gt;1. Memory copy failed; &lt;br&gt;2. A null pointer occurs inside the system; &lt;br&gt;3. Failed to obtain the native object or convert parameters. |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## getNextUpdate

```TypeScript
getNextUpdate(): string
```

Obtains the next update date of this CRL.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getNextUpdate(): string--><!--Device-X509CRL-getNextUpdate(): string-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| string | Next update date of the CRL, in an ASN.1 time format, specifically UTCTime or GeneralizedTime. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) | Runtime error. Possible causes: &lt;br&gt;1. Memory copy failed; &lt;br&gt;2. A null pointer occurs inside the system; &lt;br&gt;3. Failed to obtain the native object or convert parameters. |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## getRevokedCert

```TypeScript
getRevokedCert(serialNumber: bigint): X509CRLEntry
```

Obtains the revoked certificate entry from the X.509 CRL based on the specified serial number.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getRevokedCert(serialNumber: bigint): X509CRLEntry--><!--Device-X509CRL-getRevokedCert(serialNumber: bigint): X509CRLEntry-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| serialNumber | bigint | Yes | Serial number of the certificate. |

**Return value:**

| Type | Description |
| --- | --- |
| [X509CRLEntry](arkts-devicecertificate-cert-x509crlentry-i.md) | Revoked certificate entry obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## getRevokedCertWithCert

```TypeScript
getRevokedCertWithCert(cert: X509Cert): X509CRLEntry
```

Obtains the revoked certificate entry from the X.509 CRL based on the specified certificate.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getRevokedCertWithCert(cert: X509Cert): X509CRLEntry--><!--Device-X509CRL-getRevokedCertWithCert(cert: X509Cert): X509CRLEntry-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cert | [X509Cert](../../apis-network-kit/arkts-apis/arkts-network-http-x509cert-t.md) | Yes | Certificate based on which the revoked certificate is obtained. |

**Return value:**

| Type | Description |
| --- | --- |
| [X509CRLEntry](arkts-devicecertificate-cert-x509crlentry-i.md) | Revoked certificate entry obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## getRevokedCerts

```TypeScript
getRevokedCerts(callback: AsyncCallback<Array<X509CRLEntry>>): void
```

Obtains all the revoked certificate entries from the X.509 CRL. This API uses an asynchronous callback to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getRevokedCerts(callback: AsyncCallback<Array<X509CRLEntry>>): void--><!--Device-X509CRL-getRevokedCerts(callback: AsyncCallback<Array<X509CRLEntry>>): void-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;X509CRLEntry&gt;&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the revoked certificate entries obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## getRevokedCerts

```TypeScript
getRevokedCerts(): Promise<Array<X509CRLEntry>>
```

Obtains all the revoked certificate entries from the X.509 CRL. This API uses a promise to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getRevokedCerts(): Promise<Array<X509CRLEntry>>--><!--Device-X509CRL-getRevokedCerts(): Promise<Array<X509CRLEntry>>-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;X509CRLEntry&gt;&gt; | Promise used to return the revoked certificate entries obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## getSignature

```TypeScript
getSignature(): DataBlob
```

Obtains the signature data of the X.509 CRL.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getSignature(): DataBlob--><!--Device-X509CRL-getSignature(): DataBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | Signature data of the X.509 CRL obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) | Runtime error. Possible causes: &lt;br&gt;1. Memory copy failed; &lt;br&gt;2. A null pointer occurs inside the system; &lt;br&gt;3. Failed to obtain the native object or convert parameters. |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## getSignatureAlgName

```TypeScript
getSignatureAlgName(): string
```

Obtains the signing algorithm of the X.509 CRL.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getSignatureAlgName(): string--><!--Device-X509CRL-getSignatureAlgName(): string-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| string | Signing algorithm obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) | Runtime error. Possible causes: &lt;br&gt;1. Memory copy failed; &lt;br&gt;2. A null pointer occurs inside the system; &lt;br&gt;3. Failed to obtain the native object or convert parameters. |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## getSignatureAlgOid

```TypeScript
getSignatureAlgOid(): string
```

Obtains the OID of the X.509 CRL signing algorithm. OIDs are allocated by the International Organization for Standardization (ISO).

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getSignatureAlgOid(): string--><!--Device-X509CRL-getSignatureAlgOid(): string-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| string | OID of the X.509 CRL signing algorithm obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) | Runtime error. Possible causes: &lt;br&gt;1. Memory copy failed; &lt;br&gt;2. A null pointer occurs inside the system; &lt;br&gt;3. Failed to obtain the native object or convert parameters. |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## getSignatureAlgParams

```TypeScript
getSignatureAlgParams(): DataBlob
```

Obtains the parameters of the X.509 CRL signing algorithm.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getSignatureAlgParams(): DataBlob--><!--Device-X509CRL-getSignatureAlgParams(): DataBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | Algorithm parameters obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) | Runtime error. Possible causes: &lt;br&gt;1. Memory copy failed; &lt;br&gt;2. A null pointer occurs inside the system; &lt;br&gt;3. Failed to obtain the native object or convert parameters. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | This operation is not supported. |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## getTBSInfo

```TypeScript
getTBSInfo(): DataBlob
```

Obtains the DER-encoded CRL information, that is, **tbsCertList** from this CRL.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getTBSInfo(): DataBlob--><!--Device-X509CRL-getTBSInfo(): DataBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | tbsCertList** information obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) | Runtime error. Possible causes: &lt;br&gt;1. Memory copy failed; &lt;br&gt;2. A null pointer occurs inside the system; &lt;br&gt;3. Failed to obtain the native object or convert parameters. |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## getType

```TypeScript
getType(): string
```

Obtains the CRL type.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getType(): string--><!--Device-X509CRL-getType(): string-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| string | CRL type obtained. |

## getVersion

ArkTS-Dyn:
```TypeScript
getVersion(): number
```

ArkTS-Sta:
```TypeScript
getVersion(): int
```

Obtains the version of the X.509 CRL.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-getVersion(): int--><!--Device-X509CRL-getVersion(): int-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Version of the X.509 CRL obtained. |

## hashCode

```TypeScript
hashCode(): Uint8Array
```

Obtains the hash value of the data in DER format.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-hashCode(): Uint8Array--><!--Device-X509CRL-hashCode(): Uint8Array-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | Hash value obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) | Runtime error. Possible causes: &lt;br&gt;1. Memory copy failed; &lt;br&gt;2. A null pointer occurs inside the system; &lt;br&gt;3. Failed to obtain the native object or convert parameters. |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## isRevoked

```TypeScript
isRevoked(cert: X509Cert): boolean
```

Checks whether an X.509 certificate is revoked.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-isRevoked(cert: X509Cert): boolean--><!--Device-X509CRL-isRevoked(cert: X509Cert): boolean-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cert | [X509Cert](../../apis-network-kit/arkts-apis/arkts-network-http-x509cert-t.md) | Yes | X.509 certificate to check. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the certificate is revoked. The value **true** indicates that the certificate is revoked, and **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |

## match

```TypeScript
match(param: X509CRLMatchParameters): boolean
```

Checks whether this CRL matches the specified parameters.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-match(param: X509CRLMatchParameters): boolean--><!--Device-X509CRL-match(param: X509CRLMatchParameters): boolean-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | [X509CRLMatchParameters](arkts-devicecertificate-cert-x509crlmatchparameters-i.md) | Yes | Parameters specified for matching the CRL. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the CRL matches the parameters specified; returns **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## toString

```TypeScript
toString(): string
```

Converts the object data into a string.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-toString(): string--><!--Device-X509CRL-toString(): string-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| Type | Description |
| --- | --- |
| string | String obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) | Runtime error. Possible causes: &lt;br&gt;1. Memory copy failed; &lt;br&gt;2. A null pointer occurs inside the system; &lt;br&gt;3. Failed to obtain the native object or convert parameters. |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## toString

```TypeScript
toString(encodingType: EncodingType): string
```

Converts this object into a string in the specified encoding format.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-X509CRL-toString(encodingType: EncodingType): string--><!--Device-X509CRL-toString(encodingType: EncodingType): string-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| encodingType | [EncodingType](arkts-devicecertificate-cert-encodingtype-e.md) | Yes | Encoding type. |

**Return value:**

| Type | Description |
| --- | --- |
| string | String obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) | Runtime error. Possible causes: &lt;br&gt;1. Memory copy failed; &lt;br&gt;2. A null pointer occurs inside the system; &lt;br&gt;3. Failed to obtain the native object or convert parameters. |
| [19020003](../errorcode-cert.md#19020003-parameter-check-failure) | Parameter check failed. Possible causes: &lt;br&gt;1. The value of encodingType is not in the EncodingType enumeration range. |
| [19020001](../errorcode-cert.md#19020001-memory-error) | Memory malloc failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## verify

```TypeScript
verify(key: cryptoFramework.PubKey, callback: AsyncCallback<void>): void
```

Verifies the signature of the X.509 CRL. The RSA algorithm is supported. This API uses an asynchronous callback to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-verify(key: cryptoFramework.PubKey, callback: AsyncCallback<void>): void--><!--Device-X509CRL-verify(key: cryptoFramework.PubKey, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | cryptoFramework.PubKey | Yes | Public key used for signature verification. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

## verify

```TypeScript
verify(key: cryptoFramework.PubKey): Promise<void>
```

Verifies the signature of the X.509 CRL. The RSA algorithm is supported. This API uses a promise to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRL-verify(key: cryptoFramework.PubKey): Promise<void>--><!--Device-X509CRL-verify(key: cryptoFramework.PubKey): Promise<void>-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | cryptoFramework.PubKey | Yes | Public key used for signature verification. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) | Crypto operation error. |

