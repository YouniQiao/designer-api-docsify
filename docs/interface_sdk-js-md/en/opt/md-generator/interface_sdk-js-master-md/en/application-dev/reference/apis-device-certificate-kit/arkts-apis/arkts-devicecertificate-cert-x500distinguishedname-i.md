# X500DistinguishedName

Provides APIs for X.500 distinguished name operations.

**Since:** 12

<!--Device-cert-interface X500DistinguishedName--><!--Device-cert-interface X500DistinguishedName-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## getEncoded

```TypeScript
getEncoded(): EncodingBlob
```

Obtains the DER-encoded data of the X.500 Distinguished Name.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X500DistinguishedName-getEncoded(): EncodingBlob--><!--Device-X500DistinguishedName-getEncoded(): EncodingBlob-End-->

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [EncodingBlob](arkts-devicecertificate-cert-encodingblob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getName

```TypeScript
getName(): string
```

Obtains the DN in the form of a string.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X500DistinguishedName-getName(): string--><!--Device-X500DistinguishedName-getName(): string-End-->

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

## getName

```TypeScript
getName(encodingType: EncodingType): string
```

Obtains RDN strings based on the specified encoding format.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-X500DistinguishedName-getName(encodingType: EncodingType): string--><!--Device-X500DistinguishedName-getName(encodingType: EncodingType): string-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| encodingType | [EncodingType](arkts-devicecertificate-cert-encodingtype-e.md) | Yes |

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

## getName

```TypeScript
getName(type: string): Array<string>
```

Obtains relative distinguished name (RDN) strings of the specified type.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X500DistinguishedName-getName(type: string): Array<string>--><!--Device-X500DistinguishedName-getName(type: string): Array<string>-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getName

```TypeScript
getName(type: string, encodingType: EncodingType): Array<string>
```

Obtains an array of RDN strings based on the specified type and encoding format.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-X500DistinguishedName-getName(type: string, encodingType: EncodingType): Array<string>--><!--Device-X500DistinguishedName-getName(type: string, encodingType: EncodingType): Array<string>-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| encodingType | [EncodingType](arkts-devicecertificate-cert-encodingtype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19020003](../errorcode-cert.md#19020003-parameter-check-failure) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |
