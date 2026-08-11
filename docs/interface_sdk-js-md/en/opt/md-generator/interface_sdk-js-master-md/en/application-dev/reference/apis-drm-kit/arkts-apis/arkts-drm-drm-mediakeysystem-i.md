# MediaKeySystem

Manages and record MediaKeySessions. Before calling an MediaKeySystem method, we must use getMediaKeySystem to get a MediaKeySystem instance, then we can call functions.

**Since:** 14

<!--Device-drm-interface MediaKeySystem--><!--Device-drm-interface MediaKeySystem-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

## Modules to Import

```TypeScript
import { drm } from 'kits/@kit.DrmKit';
```

## clearOfflineMediaKeys

```TypeScript
clearOfflineMediaKeys(mediaKeyId: Uint8Array): void
```

Remove media keys corresponding to the mediaKeyId.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-clearOfflineMediaKeys(mediaKeyId: Uint8Array): void--><!--Device-MediaKeySystem-clearOfflineMediaKeys(mediaKeyId: Uint8Array): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mediaKeyId | Uint8Array | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## createMediaKeySession

```TypeScript
createMediaKeySession(level: ContentProtectionLevel): MediaKeySession
```

Create a MediaKeySession instance with level.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-createMediaKeySession(level: ContentProtectionLevel): MediaKeySession--><!--Device-MediaKeySystem-createMediaKeySession(level: ContentProtectionLevel): MediaKeySession-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| level | [ContentProtectionLevel](arkts-drm-drm-contentprotectionlevel-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MediaKeySession](arkts-drm-drm-mediakeysession-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [24700104](../errorcode-drm.md#24700104-too-many-mediakeysession-instances) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## createMediaKeySession

```TypeScript
createMediaKeySession(): MediaKeySession
```

Create a MediaKeySession instance.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-createMediaKeySession(): MediaKeySession--><!--Device-MediaKeySystem-createMediaKeySession(): MediaKeySession-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MediaKeySession](arkts-drm-drm-mediakeysession-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [24700104](../errorcode-drm.md#24700104-too-many-mediakeysession-instances) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## destroy

```TypeScript
destroy(): void
```

Release the resource before the MediaKeySystem gonna be unused.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-destroy(): void--><!--Device-MediaKeySystem-destroy(): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Error codes:**

| Error Code ID |
| --- |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## generateKeySystemRequest

```TypeScript
generateKeySystemRequest(): Promise<ProvisionRequest>
```

Generate a media key system provision request.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-generateKeySystemRequest(): Promise<ProvisionRequest>--><!--Device-MediaKeySystem-generateKeySystemRequest(): Promise<ProvisionRequest>-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ProvisionRequest&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## getCertificateStatus

```TypeScript
getCertificateStatus(): CertificateStatus
```

Get certificate status of the MediaKeySystem.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-getCertificateStatus(): CertificateStatus--><!--Device-MediaKeySystem-getCertificateStatus(): CertificateStatus-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CertificateStatus](arkts-drm-drm-certificatestatus-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## getConfigurationByteArray

```TypeScript
getConfigurationByteArray(configName: string): Uint8Array
```

Get the specified configuration.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-getConfigurationByteArray(configName: string): Uint8Array--><!--Device-MediaKeySystem-getConfigurationByteArray(configName: string): Uint8Array-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| configName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## getConfigurationString

```TypeScript
getConfigurationString(configName: string): string
```

Get the specified configuration.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-getConfigurationString(configName: string): string--><!--Device-MediaKeySystem-getConfigurationString(configName: string): string-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| configName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## getMaxContentProtectionLevel

```TypeScript
getMaxContentProtectionLevel(): ContentProtectionLevel
```

Get max content protection level the device supports.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-getMaxContentProtectionLevel(): ContentProtectionLevel--><!--Device-MediaKeySystem-getMaxContentProtectionLevel(): ContentProtectionLevel-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ContentProtectionLevel](arkts-drm-drm-contentprotectionlevel-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## getOfflineMediaKeyIds

```TypeScript
getOfflineMediaKeyIds(): Uint8Array[]
```

Get the list of offline MediaKeyIds.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-getOfflineMediaKeyIds(): Uint8Array[]--><!--Device-MediaKeySystem-getOfflineMediaKeyIds(): Uint8Array[]-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array[] |

**Error codes:**

| Error Code ID |
| --- |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## getOfflineMediaKeyStatus

```TypeScript
getOfflineMediaKeyStatus(mediaKeyId: Uint8Array): OfflineMediaKeyStatus
```

Get offline media key status corresponding to the mediaKeyId.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-getOfflineMediaKeyStatus(mediaKeyId: Uint8Array): OfflineMediaKeyStatus--><!--Device-MediaKeySystem-getOfflineMediaKeyStatus(mediaKeyId: Uint8Array): OfflineMediaKeyStatus-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mediaKeyId | Uint8Array | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [OfflineMediaKeyStatus](arkts-drm-drm-offlinemediakeystatus-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## getStatistics

```TypeScript
getStatistics(): StatisticKeyValue[]
```

Get performance statistics information.That includes currentSessionNum, version, decryptNumber,and errorDecryptNumber.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-getStatistics(): StatisticKeyValue[]--><!--Device-MediaKeySystem-getStatistics(): StatisticKeyValue[]-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [StatisticKeyValue](arkts-drm-drm-statistickeyvalue-i.md)[] |

**Error codes:**

| Error Code ID |
| --- |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## off('keySystemRequired')

```TypeScript
off(type: 'keySystemRequired', callback?: (eventInfo: EventInfo) => void): void
```

Unregister keySystemRequired events.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-off(type: 'keySystemRequired', callback?: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySystem-off(type: 'keySystemRequired', callback?: (eventInfo: EventInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keySystemRequired' | Yes |
| callback | (eventInfo: EventInfo) =&gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## on('keySystemRequired')

```TypeScript
on(type: 'keySystemRequired', callback: (eventInfo: EventInfo) => void): void
```

Register keySystemRequired events.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-on(type: 'keySystemRequired', callback: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySystem-on(type: 'keySystemRequired', callback: (eventInfo: EventInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keySystemRequired' | Yes |
| callback | (eventInfo: EventInfo) =&gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## processKeySystemResponse

```TypeScript
processKeySystemResponse(response: Uint8Array): Promise<void>
```

Process the response corresponding the key system request obtained by the application.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-processKeySystemResponse(response: Uint8Array): Promise<void>--><!--Device-MediaKeySystem-processKeySystemResponse(response: Uint8Array): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| response | Uint8Array | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## setConfigurationByteArray

```TypeScript
setConfigurationByteArray(configName: string, value: Uint8Array): void
```

Set the specified configuration.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-setConfigurationByteArray(configName: string, value: Uint8Array): void--><!--Device-MediaKeySystem-setConfigurationByteArray(configName: string, value: Uint8Array): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| configName | string | Yes |
| value | Uint8Array | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## setConfigurationString

```TypeScript
setConfigurationString(configName: string, value: string): void
```

Set the specified configuration.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-setConfigurationString(configName: string, value: string): void--><!--Device-MediaKeySystem-setConfigurationString(configName: string, value: string): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| configName | string | Yes |
| value | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |
