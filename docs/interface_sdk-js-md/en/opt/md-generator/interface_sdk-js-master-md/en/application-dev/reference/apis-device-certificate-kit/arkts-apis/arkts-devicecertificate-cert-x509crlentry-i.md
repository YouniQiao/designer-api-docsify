# X509CRLEntry

Provides APIs for operating on a revoked certificate entry in a CRL.

**Since:** 11

<!--Device-cert-interface X509CRLEntry--><!--Device-cert-interface X509CRLEntry-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
```

## getCertIssuer

```TypeScript
getCertIssuer(): DataBlob
```

Obtains the issuer name of the revoked certificate.

> **NOTE：**
> 
> The obtained issuer name of this revoked certificate contains a string terminator.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLEntry-getCertIssuer(): DataBlob--><!--Device-X509CRLEntry-getCertIssuer(): DataBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020002-runtime-error) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [19020001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020001-memory-error) |
| [19030001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030001-crypto-operation-error) |

## getCertIssuer

```TypeScript
getCertIssuer(encodingType: EncodingType): string
```

Obtains the issuer name of the revoked certificate based on the encoding type.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-X509CRLEntry-getCertIssuer(encodingType: EncodingType): string--><!--Device-X509CRLEntry-getCertIssuer(encodingType: EncodingType): string-End-->

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
| [19020002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020002-runtime-error) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [19020003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020003-parameter-check-failure) |
| [19020001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020001-memory-error) |
| [19030001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030001-crypto-operation-error) |

## getCertIssuerX500DistinguishedName

```TypeScript
getCertIssuerX500DistinguishedName(): X500DistinguishedName
```

Obtains the distinguished name (DN) of the issuer of the revoked certificate.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLEntry-getCertIssuerX500DistinguishedName(): X500DistinguishedName--><!--Device-X509CRLEntry-getCertIssuerX500DistinguishedName(): X500DistinguishedName-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [X500DistinguishedName](arkts-devicecertificate-cert-x500distinguishedname-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020002-runtime-error) |
| [19020001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020001-memory-error) |
| [19030001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030001-crypto-operation-error) |

## getEncoded

```TypeScript
getEncoded(callback: AsyncCallback<EncodingBlob>): void
```

Obtains the serialized data of this revoked certificate entry. This API uses an asynchronous callback to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLEntry-getEncoded(callback: AsyncCallback<EncodingBlob>): void--><!--Device-X509CRLEntry-getEncoded(callback: AsyncCallback<EncodingBlob>): void-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[EncodingBlob](arkts-devicecertificate-cert-encodingblob-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020002-runtime-error) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [19020001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020001-memory-error) |
| [19030001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030001-crypto-operation-error) |

## getEncoded

```TypeScript
getEncoded(): Promise<EncodingBlob>
```

Obtains the serialized data of this revoked certificate entry. This API uses a promise to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLEntry-getEncoded(): Promise<EncodingBlob>--><!--Device-X509CRLEntry-getEncoded(): Promise<EncodingBlob>-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[EncodingBlob](arkts-devicecertificate-cert-encodingblob-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020002-runtime-error) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [19020001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020001-memory-error) |
| [19030001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030001-crypto-operation-error) |

## getExtensions

```TypeScript
getExtensions(): DataBlob
```

Obtains the CRL entry extensions in DER format.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLEntry-getExtensions(): DataBlob--><!--Device-X509CRLEntry-getExtensions(): DataBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataBlob](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-datablob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020002-runtime-error) |
| [19020001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020001-memory-error) |
| [19030001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030001-crypto-operation-error) |

## getExtensionsObject

```TypeScript
getExtensionsObject(): CertExtension
```

Obtains the CRL entry extension object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLEntry-getExtensionsObject(): CertExtension--><!--Device-X509CRLEntry-getExtensionsObject(): CertExtension-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CertExtension](arkts-devicecertificate-cert-certextension-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020002-runtime-error) |
| [19020001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020001-memory-error) |
| [19030001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030001-crypto-operation-error) |

## getRevocationDate

```TypeScript
getRevocationDate(): string
```

Obtains the certificate's revocation date.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLEntry-getRevocationDate(): string--><!--Device-X509CRLEntry-getRevocationDate(): string-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020002-runtime-error) |
| [19020001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020001-memory-error) |
| [19030001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030001-crypto-operation-error) |

## getSerialNumber

```TypeScript
getSerialNumber(): bigint
```

Obtains the serial number of this revoked certificate.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLEntry-getSerialNumber(): bigint--><!--Device-X509CRLEntry-getSerialNumber(): bigint-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| bigint |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020002-runtime-error) |
| [19020001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020001-memory-error) |
| [19030001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030001-crypto-operation-error) |

## hasExtensions

```TypeScript
hasExtensions(): boolean
```

Checks whether this CRL entry has extensions.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLEntry-hasExtensions(): boolean--><!--Device-X509CRLEntry-hasExtensions(): boolean-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020002-runtime-error) |
| [19020001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020001-memory-error) |
| [19030001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030001-crypto-operation-error) |

## hashCode

```TypeScript
hashCode(): Uint8Array
```

Obtains the hash value of the data in DER format.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLEntry-hashCode(): Uint8Array--><!--Device-X509CRLEntry-hashCode(): Uint8Array-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020002-runtime-error) |
| [19020001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020001-memory-error) |
| [19030001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030001-crypto-operation-error) |

## toString

```TypeScript
toString(): string
```

Converts the object data into a string.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLEntry-toString(): string--><!--Device-X509CRLEntry-toString(): string-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020002-runtime-error) |
| [19020001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19020001-memory-error) |
| [19030001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-device-certificate-kit/errorcode-cert.md#19030001-crypto-operation-error) |
