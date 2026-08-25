# CertExtension

Provides APIs for operating on certificate extensions.

**Since:** 10

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## checkCA

```TypeScript
checkCA(): number
```

Checks whether the certificate is a CA certificate.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getEncoded

```TypeScript
getEncoded(): EncodingBlob
```

Obtains the serialized data of the certificate extensions.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [EncodingBlob](arkts-devicecertificate-cert-encodingblob-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## getEntry

```TypeScript
getEntry(valueType: ExtensionEntryType, oid: DataBlob): DataBlob
```

Obtains the value of a specific certificate extension entry by OID.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [valueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-scanneroptionvalue-i.md) | [ExtensionEntryType](arkts-devicecertificate-cert-extensionentrytype-e.md) | Yes |
| oid | [DataBlob](arkts-devicecertificate-cert-datablob-i.md) | Yes |

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

## getOidList

```TypeScript
getOidList(valueType: ExtensionOidType): DataArray
```

Obtains the OIDs of the certificate extensions.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [valueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-scanneroptionvalue-i.md) | [ExtensionOidType](arkts-devicecertificate-cert-extensionoidtype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataArray](arkts-devicecertificate-cert-dataarray-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |

## hasUnsupportedCriticalExtension

```TypeScript
hasUnsupportedCriticalExtension(): boolean
```

Checks whether there is a critical extension that is not supported.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Security.Cert

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [19020001](../errorcode-cert.md#19020001-memory-error) |
| [19020002](../errorcode-cert.md#19020002-runtime-error) |
| [19030001](../errorcode-cert.md#19030001-crypto-operation-error) |
