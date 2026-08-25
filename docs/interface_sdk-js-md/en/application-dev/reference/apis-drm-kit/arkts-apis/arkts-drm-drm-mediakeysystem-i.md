# MediaKeySystem

MediaKeySystem manages MediaKeySystem instances, handles device certificate (DRM certificate) requests and processing, creates sessions, manages offline media keys, obtains DRM metrics, and obtain device configurations. Before calling any API in MediaKeySystem, you must use [createMediaKeySystem](arkts-drm-drm-createmediakeysystem-f.md) to create a MediaKeySystem instance.

**Since:** 11

**System capability:** SystemCapability.Multimedia.Drm.Core

## Modules to Import

```TypeScript
import { drm } from 'kits/@kit.DrmKit';
```

## clearOfflineMediaKeys

```TypeScript
clearOfflineMediaKeys(mediaKeyId: Uint8Array): void
```

Clears offline media keys with the specified IDs.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mediaKeyId | Uint8Array | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |

## createMediaKeySession

```TypeScript
createMediaKeySession(level: ContentProtectionLevel): MediaKeySession
```

Creates a MediaKeySession instance with the specified content protection level.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |
| [24700104](../errorcode-drm.md#24700104-too-many-mediakeysession-instances) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |

## createMediaKeySession

```TypeScript
createMediaKeySession(): MediaKeySession
```

Creates a MediaKeySession instance with the default content protection level.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MediaKeySession](arkts-drm-drm-mediakeysession-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |
| [24700104](../errorcode-drm.md#24700104-too-many-mediakeysession-instances) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |

## destroy

```TypeScript
destroy(): void
```

Destroys this MediaKeySystem instance.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Multimedia.Drm.Core

**Error codes:**

| Error Code ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |

## generateKeySystemRequest

```TypeScript
generateKeySystemRequest(): Promise<ProvisionRequest>
```

Generates a request to obtain a device certificate for the MediaKeySystem. This API uses a promise to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ProvisionRequest](arkts-drm-drm-provisionrequest-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |

## getCertificateStatus

```TypeScript
getCertificateStatus(): CertificateStatus
```

Obtains the status of the device certificate.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CertificateStatus](arkts-drm-drm-certificatestatus-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |

## getConfigurationByteArray

```TypeScript
getConfigurationByteArray(configName: string): Uint8Array
```

Obtains the value of a configuration item in the form of a byte array.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [configName](../../apis-performance-analysis-kit/arkts-apis/arkts-performanceanalysis-hiappevent-processor-i.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |

## getConfigurationString

```TypeScript
getConfigurationString(configName: string): string
```

Obtains the value of a configuration item in the form of a string.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [configName](../../apis-performance-analysis-kit/arkts-apis/arkts-performanceanalysis-hiappevent-processor-i.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |

## getMaxContentProtectionLevel

```TypeScript
getMaxContentProtectionLevel(): ContentProtectionLevel
```

Obtains the maximum content protection level supported by the current DRM solution.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ContentProtectionLevel](arkts-drm-drm-contentprotectionlevel-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |

## getOfflineMediaKeyIds

```TypeScript
getOfflineMediaKeyIds(): Uint8Array[]
```

Obtains the IDs of offline media keys.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array[] |

**Error codes:**

| Error Code ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |

## getOfflineMediaKeyStatus

```TypeScript
getOfflineMediaKeyStatus(mediaKeyId: Uint8Array): OfflineMediaKeyStatus
```

Obtains the status of offline media keys with the specified IDs.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |

## getStatistics

```TypeScript
getStatistics(): StatisticKeyValue[]
```

Obtains the DRM metrics, including the number of active sessions, plugin version details, the maximum decryption time for each session (over three attempts), the total count of decryption operations, and the number of decryption failures.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [StatisticKeyValue](arkts-drm-drm-statistickeyvalue-i.md)[] |

**Error codes:**

| Error Code ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |

## off('keySystemRequired')

```TypeScript
off(type: 'keySystemRequired', callback?: (eventInfo: EventInfo) => void): void
```

Unsubscribes from events indicating that the application requests a device certificate. This API uses an asynchronous callback to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keySystemRequired' | Yes |
| callback | (eventInfo: EventInfo) = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## on('keySystemRequired')

```TypeScript
on(type: 'keySystemRequired', callback: (eventInfo: EventInfo) => void): void
```

Subscribes to events indicating that the application requests a device certificate. This API uses an asynchronous callback to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keySystemRequired' | Yes |
| callback | (eventInfo: EventInfo) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## processKeySystemResponse

```TypeScript
processKeySystemResponse(response: Uint8Array): Promise<void>
```

Processes the response to a previously generated device certificate request. This API uses a promise to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| response | Uint8Array | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |

## setConfigurationByteArray

```TypeScript
setConfigurationByteArray(configName: string, value: Uint8Array): void
```

Sets a configuration item in the form of a byte array.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [configName](../../apis-performance-analysis-kit/arkts-apis/arkts-performanceanalysis-hiappevent-processor-i.md) | string | Yes |
| value | Uint8Array | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |

## setConfigurationString

```TypeScript
setConfigurationString(configName: string, value: string): void
```

Sets a configuration item in the form of a string.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [configName](../../apis-performance-analysis-kit/arkts-apis/arkts-performanceanalysis-hiappevent-processor-i.md) | string | Yes |
| value | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
