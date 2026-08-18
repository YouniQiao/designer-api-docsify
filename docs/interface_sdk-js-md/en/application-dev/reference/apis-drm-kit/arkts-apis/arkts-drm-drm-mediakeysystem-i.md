# MediaKeySystem(Defines the DRM capability.)

MediaKeySystem manages MediaKeySystem instances, handles device certificate (DRM certificate) requests and processing, creates sessions, manages offline media keys, obtains DRM metrics, and obtain device configurations. Before calling any API in MediaKeySystem, you must use [createMediaKeySystem](arkts-drm-drm-createmediakeysystem-f.md) to create a MediaKeySystem instance.

**Since:** 23

<!--Device-drm-interface MediaKeySystem--><!--Device-drm-interface MediaKeySystem-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

## Modules to Import

```TypeScript
import { drm } from '@kit.DrmKit';
```

## clearOfflineMediaKeys

```TypeScript
clearOfflineMediaKeys(mediaKeyId: Uint8Array): void
```

Clears offline media keys with the specified IDs.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-clearOfflineMediaKeys(mediaKeyId: Uint8Array): void--><!--Device-MediaKeySystem-clearOfflineMediaKeys(mediaKeyId: Uint8Array): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mediaKeyId | Uint8Array | Yes | Array of offline media key IDs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed.Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [24700201](../errorcode-drm.md#24700201-service-exception) | Fatal service error, for example, service died. |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

## createMediaKeySession

```TypeScript
createMediaKeySession(level: ContentProtectionLevel): MediaKeySession
```

Creates a MediaKeySession instance with the specified content protection level.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-createMediaKeySession(level: ContentProtectionLevel): MediaKeySession--><!--Device-MediaKeySystem-createMediaKeySession(level: ContentProtectionLevel): MediaKeySession-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| level | [ContentProtectionLevel](arkts-drm-drm-contentprotectionlevel-e.md) | Yes | Content protection level. |

**Return value:**

| Type | Description |
| --- | --- |
| [MediaKeySession](arkts-drm-drm-mediakeysession-i.md) | MediaKeySession instance. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [24700104](../errorcode-drm.md#24700104-too-many-mediakeysession-instances) | Meet max MediaKeySession num limit. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.The param level exceeds reasonable range, please use value in ContentProtectionLevel. |
| [24700201](../errorcode-drm.md#24700201-service-exception) | Fatal service error, for example, service died. |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

## createMediaKeySession

```TypeScript
createMediaKeySession(level: ContentProtectionLevel): MediaKeySession | undefined
```

Create a MediaKeySession instance with level.

**Since:** 23

<!--Device-MediaKeySystem-createMediaKeySession(level: ContentProtectionLevel): MediaKeySession | undefined--><!--Device-MediaKeySystem-createMediaKeySession(level: ContentProtectionLevel): MediaKeySession | undefined-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| level | [ContentProtectionLevel](arkts-drm-drm-contentprotectionlevel-e.md) | Yes | Used to specify the content protection level. |

**Return value:**

| Type | Description |
| --- | --- |
| [MediaKeySession](arkts-drm-drm-mediakeysession-i.md) | A MediaKeySession instance or undefined. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [24700104](../errorcode-drm.md#24700104-too-many-mediakeysession-instances) | Meet max MediaKeySession num limit. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.The param level exceeds reasonable range, please use value in ContentProtectionLevel. |
| [24700201](../errorcode-drm.md#24700201-service-exception) | Fatal service error, for example, service died. |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

## createMediaKeySession

```TypeScript
createMediaKeySession(): MediaKeySession
```

Creates a MediaKeySession instance with the default content protection level.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-createMediaKeySession(): MediaKeySession--><!--Device-MediaKeySystem-createMediaKeySession(): MediaKeySession-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| Type | Description |
| --- | --- |
| [MediaKeySession](arkts-drm-drm-mediakeysession-i.md) | MediaKeySession instance. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [24700104](../errorcode-drm.md#24700104-too-many-mediakeysession-instances) | Meet max MediaKeySession num limit. |
| [24700201](../errorcode-drm.md#24700201-service-exception) | Fatal service error, for example, service died. |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

## createMediaKeySession

```TypeScript
createMediaKeySession(): MediaKeySession | undefined
```

Create a MediaKeySession instance.

**Since:** 23

<!--Device-MediaKeySystem-createMediaKeySession(): MediaKeySession | undefined--><!--Device-MediaKeySystem-createMediaKeySession(): MediaKeySession | undefined-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| Type | Description |
| --- | --- |
| [MediaKeySession](arkts-drm-drm-mediakeysession-i.md) | A MediaKeySession instance or undefined. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [24700104](../errorcode-drm.md#24700104-too-many-mediakeysession-instances) | Meet max MediaKeySession num limit. |
| [24700201](../errorcode-drm.md#24700201-service-exception) | Fatal service error, for example, service died. |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

## destroy

```TypeScript
destroy(): void
```

Destroys this MediaKeySystem instance.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-destroy(): void--><!--Device-MediaKeySystem-destroy(): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [24700201](../errorcode-drm.md#24700201-service-exception) | Fatal service error, for example, service died. |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

## generateKeySystemRequest

```TypeScript
generateKeySystemRequest(): Promise<ProvisionRequest>
```

Generates a request to obtain a device certificate for the MediaKeySystem. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-generateKeySystemRequest(): Promise<ProvisionRequest>--><!--Device-MediaKeySystem-generateKeySystemRequest(): Promise<ProvisionRequest>-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ProvisionRequest](arkts-drm-drm-provisionrequest-i.md)&gt; | Promise used to return the request for a device certificate. If a device certificate already exists on the device, this operation fails. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [24700201](../errorcode-drm.md#24700201-service-exception) | Fatal service error, for example, service died. |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

## getCertificateStatus

```TypeScript
getCertificateStatus(): CertificateStatus
```

Obtains the status of the device certificate.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-getCertificateStatus(): CertificateStatus--><!--Device-MediaKeySystem-getCertificateStatus(): CertificateStatus-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| Type | Description |
| --- | --- |
| [CertificateStatus](arkts-drm-drm-certificatestatus-e.md) | Certificate status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [24700201](../errorcode-drm.md#24700201-service-exception) | Fatal service error, for example, service died. |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

## getConfigurationByteArray

```TypeScript
getConfigurationByteArray(configName: string): Uint8Array
```

Obtains the value of a configuration item in the form of a byte array.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-getConfigurationByteArray(configName: string): Uint8Array--><!--Device-MediaKeySystem-getConfigurationByteArray(configName: string): Uint8Array-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| configName | string | Yes | Name of the configuration item, which is determined by the DRM solution on the device and cannot be empty. For details about available options, see [PreDefinedConfigName](arkts-drm-drm-predefinedconfigname-e.md). |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | Value of the configuration item in the form of an array. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [24700201](../errorcode-drm.md#24700201-service-exception) | Fatal service error, for example, service died. |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

## getConfigurationString

```TypeScript
getConfigurationString(configName: string): string
```

Obtains the value of a configuration item in the form of a string.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-getConfigurationString(configName: string): string--><!--Device-MediaKeySystem-getConfigurationString(configName: string): string-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| configName | string | Yes | Name of the configuration item, which is determined by the DRM solution on the device and cannot be empty. For details about available options, see [PreDefinedConfigName](arkts-drm-drm-predefinedconfigname-e.md). |

**Return value:**

| Type | Description |
| --- | --- |
| string | Value of the configuration item in the form of a string. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed, the param's length is zero or too big(exceeds 4096 Bytes). |
| [24700201](../errorcode-drm.md#24700201-service-exception) | Fatal service error, for example, service died. |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

## getMaxContentProtectionLevel

```TypeScript
getMaxContentProtectionLevel(): ContentProtectionLevel
```

Obtains the maximum content protection level supported by the current DRM solution.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-getMaxContentProtectionLevel(): ContentProtectionLevel--><!--Device-MediaKeySystem-getMaxContentProtectionLevel(): ContentProtectionLevel-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| Type | Description |
| --- | --- |
| [ContentProtectionLevel](arkts-drm-drm-contentprotectionlevel-e.md) | Maximum content protection level. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [24700201](../errorcode-drm.md#24700201-service-exception) | Fatal service error, for example, service died. |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

## getOfflineMediaKeyIds

```TypeScript
getOfflineMediaKeyIds(): Uint8Array[]
```

Obtains the IDs of offline media keys.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-getOfflineMediaKeyIds(): Uint8Array[]--><!--Device-MediaKeySystem-getOfflineMediaKeyIds(): Uint8Array[]-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array[] | Array of offline media key IDs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [24700201](../errorcode-drm.md#24700201-service-exception) | Fatal service error, for example, service died. |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

## getOfflineMediaKeyStatus

```TypeScript
getOfflineMediaKeyStatus(mediaKeyId: Uint8Array): OfflineMediaKeyStatus
```

Obtains the status of offline media keys with the specified IDs.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-getOfflineMediaKeyStatus(mediaKeyId: Uint8Array): OfflineMediaKeyStatus--><!--Device-MediaKeySystem-getOfflineMediaKeyStatus(mediaKeyId: Uint8Array): OfflineMediaKeyStatus-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mediaKeyId | Uint8Array | Yes | Array of offline media key IDs. |

**Return value:**

| Type | Description |
| --- | --- |
| [OfflineMediaKeyStatus](arkts-drm-drm-offlinemediakeystatus-e.md) | Status of the offline media keys. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [24700201](../errorcode-drm.md#24700201-service-exception) | Fatal service error, for example, service died. |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

## getStatistics

```TypeScript
getStatistics(): StatisticKeyValue[]
```

Obtains the DRM metrics, including the number of active sessions, plugin version details, the maximum decryption time for each session (over three attempts), the total count of decryption operations, and the number of decryption failures.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-getStatistics(): StatisticKeyValue[]--><!--Device-MediaKeySystem-getStatistics(): StatisticKeyValue[]-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| Type | Description |
| --- | --- |
| [StatisticKeyValue](arkts-drm-drm-statistickeyvalue-i.md)[] | Metrics. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [24700201](../errorcode-drm.md#24700201-service-exception) | Fatal service error, for example, service died. |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

## offKeySystemRequired

```TypeScript
offKeySystemRequired(callback?: (eventInfo: EventInfo) => void): void
```

Unregister keySystemRequired events.

**Since:** 23

<!--Device-MediaKeySystem-offKeySystemRequired(callback?: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySystem-offKeySystemRequired(callback?: (eventInfo: EventInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (eventInfo: EventInfo) =&gt; void | No | Used to listen for the key system required event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

## off_keySystemRequired('keySystemRequired')

```TypeScript
off(type: 'keySystemRequired', callback?: (eventInfo: EventInfo) => void): void
```

Unsubscribes from events indicating that the application requests a device certificate. This API uses an asynchronous callback to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-off(type: 'keySystemRequired', callback?: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySystem-off(type: 'keySystemRequired', callback?: (eventInfo: EventInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keySystemRequired' | Yes | Event type. This event is available for listening after a MediaKeySystem instance is created by calling [createMediaKeySystem](arkts-drm-drm-createmediakeysystem-f.md). |
| callback | (eventInfo: EventInfo) =&gt; void | No | Callback used to return the event information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

## onKeySystemRequired

```TypeScript
onKeySystemRequired(callback: (eventInfo: EventInfo) => void): void
```

Register keySystemRequired events.

**Since:** 23

<!--Device-MediaKeySystem-onKeySystemRequired(callback: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySystem-onKeySystemRequired(callback: (eventInfo: EventInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (eventInfo: EventInfo) =&gt; void | Yes | Used to listen for the key system required event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

## on_keySystemRequired('keySystemRequired')

```TypeScript
on(type: 'keySystemRequired', callback: (eventInfo: EventInfo) => void): void
```

Subscribes to events indicating that the application requests a device certificate. This API uses an asynchronous callback to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-on(type: 'keySystemRequired', callback: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySystem-on(type: 'keySystemRequired', callback: (eventInfo: EventInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keySystemRequired' | Yes | Event type. This event is available for listening after a MediaKeySystem instance is created by calling [createMediaKeySystem](arkts-drm-drm-createmediakeysystem-f.md). It is triggered when a device certificate is required. |
| callback | (eventInfo: EventInfo) =&gt; void | Yes | Callback used to return the event information. The occurrence of this event signals the need to request a device certificate. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

## processKeySystemResponse

```TypeScript
processKeySystemResponse(response: Uint8Array): Promise<void>
```

Processes the response to a previously generated device certificate request. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-processKeySystemResponse(response: Uint8Array): Promise<void>--><!--Device-MediaKeySystem-processKeySystemResponse(response: Uint8Array): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| response | Uint8Array | Yes | Response to a previously generated device certificate request. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [24700201](../errorcode-drm.md#24700201-service-exception) | Fatal service error, for example, service died. |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

## setConfigurationByteArray

```TypeScript
setConfigurationByteArray(configName: string, value: Uint8Array): void
```

Sets a configuration item in the form of a byte array.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-setConfigurationByteArray(configName: string, value: Uint8Array): void--><!--Device-MediaKeySystem-setConfigurationByteArray(configName: string, value: Uint8Array): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| configName | string | Yes | Name of the configuration item, which is determined by the DRM solution on the device and cannot be empty. For details about available options, see [PreDefinedConfigName](arkts-drm-drm-predefinedconfigname-e.md). |
| value | Uint8Array | Yes | Value of the configuration item in the form of an array. The specific value is determined by the DRM solution on the device. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [24700201](../errorcode-drm.md#24700201-service-exception) | Fatal service error, for example, service died. |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

## setConfigurationString

```TypeScript
setConfigurationString(configName: string, value: string): void
```

Sets a configuration item in the form of a string.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-MediaKeySystem-setConfigurationString(configName: string, value: string): void--><!--Device-MediaKeySystem-setConfigurationString(configName: string, value: string): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| configName | string | Yes | Name of the configuration item, which is determined by the DRM solution on the device and cannot be empty. For details about available options, see [PreDefinedConfigName](arkts-drm-drm-predefinedconfigname-e.md). |
| value | string | Yes | Value of the configuration item. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [24700201](../errorcode-drm.md#24700201-service-exception) | Fatal service error, for example, service died. |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

