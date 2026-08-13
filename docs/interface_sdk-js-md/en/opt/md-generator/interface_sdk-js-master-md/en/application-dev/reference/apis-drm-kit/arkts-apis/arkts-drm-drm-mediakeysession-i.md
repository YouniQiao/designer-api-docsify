# MediaKeySession

MediaKeySession implements media key management. Before calling any API in MediaKeySession, you must use [createMediaKeySession](arkts-drm-drm-mediakeysystem-i.md#createMediaKeySession) to create a MediaKeySession instance.

**Since:** 23

**Deprecated since:** -1

<!--Device-drm-interface MediaKeySession--><!--Device-drm-interface MediaKeySession-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

## Modules to Import

```TypeScript
import { drm } from '@kit.DrmKit';
```

## checkMediaKeyStatus

```TypeScript
checkMediaKeyStatus(): MediaKeyStatus[]
```

Checks the status of the media keys in use.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaKeySession-checkMediaKeyStatus(): MediaKeyStatus[]--><!--Device-MediaKeySession-checkMediaKeyStatus(): MediaKeyStatus[]-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MediaKeyStatus](arkts-drm-drm-mediakeystatus-i.md)[] |

**Error codes:**

| Error Code ID |
| --- |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## clearMediaKeys

```TypeScript
clearMediaKeys(): void
```

Clears the media keys in use.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaKeySession-clearMediaKeys(): void--><!--Device-MediaKeySession-clearMediaKeys(): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Error codes:**

| Error Code ID |
| --- |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## destroy

```TypeScript
destroy(): void
```

Destroys this MediaKeySession instance.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaKeySession-destroy(): void--><!--Device-MediaKeySession-destroy(): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Error codes:**

| Error Code ID |
| --- |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## generateMediaKeyRequest

```TypeScript
generateMediaKeyRequest(mimeType: string, initData: Uint8Array, mediaKeyType: number, options?: OptionsData[]): Promise<MediaKeyRequest>
```

Generates a media key request. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaKeySession-generateMediaKeyRequest(mimeType: string, initData: Uint8Array, mediaKeyType: int, options?: OptionsData[]): Promise<MediaKeyRequest>--><!--Device-MediaKeySession-generateMediaKeyRequest(mimeType: string, initData: Uint8Array, mediaKeyType: int, options?: OptionsData[]): Promise<MediaKeyRequest>-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mimeType | string | Yes |
| initData | Uint8Array | Yes |
| mediaKeyType | number | Yes |
| options | [OptionsData](arkts-drm-drm-optionsdata-i.md)[] | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[MediaKeyRequest](arkts-drm-drm-mediakeyrequest-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## generateOfflineReleaseRequest

```TypeScript
generateOfflineReleaseRequest(mediaKeyId: Uint8Array): Promise<Uint8Array>
```

Generates a request to release offline media keys. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaKeySession-generateOfflineReleaseRequest(mediaKeyId: Uint8Array): Promise<Uint8Array>--><!--Device-MediaKeySession-generateOfflineReleaseRequest(mediaKeyId: Uint8Array): Promise<Uint8Array>-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mediaKeyId | Uint8Array | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Uint8Array & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## getContentProtectionLevel

```TypeScript
getContentProtectionLevel(): ContentProtectionLevel
```

Obtains the content protection level of this media key session.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaKeySession-getContentProtectionLevel(): ContentProtectionLevel--><!--Device-MediaKeySession-getContentProtectionLevel(): ContentProtectionLevel-End-->

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

## offExpirationUpdate

```TypeScript
offExpirationUpdate(callback?: (eventInfo: EventInfo) => void): void
```

Unregister expirationUpdate event.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaKeySession-offExpirationUpdate(callback?: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-offExpirationUpdate(callback?: (eventInfo: EventInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (eventInfo: EventInfo) = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## offKeyExpired

```TypeScript
offKeyExpired(callback?: (eventInfo: EventInfo) => void): void
```

Unregister keyExpired event.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaKeySession-offKeyExpired(callback?: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-offKeyExpired(callback?: (eventInfo: EventInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (eventInfo: EventInfo) = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## offKeyRequired

```TypeScript
offKeyRequired(callback?: (eventInfo: EventInfo) => void): void
```

Unregister keyRequired event.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaKeySession-offKeyRequired(callback?: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-offKeyRequired(callback?: (eventInfo: EventInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (eventInfo: EventInfo) = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## offKeysChange

```TypeScript
offKeysChange(callback?: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void
```

Unregister keysChange event.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaKeySession-offKeysChange(callback?: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void--><!--Device-MediaKeySession-offKeysChange(callback?: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (keyInfo: KeysInfo[], newKeyAvailable: boolean) = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## offVendorDefined

```TypeScript
offVendorDefined(callback?: (eventInfo: EventInfo) => void): void
```

Unregister vendorDefined event.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaKeySession-offVendorDefined(callback?: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-offVendorDefined(callback?: (eventInfo: EventInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (eventInfo: EventInfo) = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## off_expirationUpdate

```TypeScript
off(type: 'expirationUpdate', callback?: (eventInfo: EventInfo) => void): void
```

Unsubscribes from events indicating that a media key is updated upon expiry. This API uses an asynchronous callback to return the result.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaKeySession-off(type: 'expirationUpdate', callback?: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-off(type: 'expirationUpdate', callback?: (eventInfo: EventInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'expirationUpdate' | Yes |
| callback | (eventInfo: EventInfo) = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## off_keyExpired

```TypeScript
off(type: 'keyExpired', callback?: (eventInfo: EventInfo) => void): void
```

Unsubscribes from events indicating that a media key expires. This API uses an asynchronous callback to return the result.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaKeySession-off(type: 'keyExpired', callback?: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-off(type: 'keyExpired', callback?: (eventInfo: EventInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyExpired' | Yes |
| callback | (eventInfo: EventInfo) = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## off_keyRequired

```TypeScript
off(type: 'keyRequired', callback?: (eventInfo: EventInfo) => void): void
```

Unsubscribes from events indicating that the application requests a media key. This API uses an asynchronous callback to return the result.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaKeySession-off(type: 'keyRequired', callback?: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-off(type: 'keyRequired', callback?: (eventInfo: EventInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyRequired' | Yes |
| callback | (eventInfo: EventInfo) = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## off_keysChange

```TypeScript
off(type: 'keysChange', callback?: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void
```

Unsubscribes from events indicating that a media key changes. This API uses an asynchronous callback to return the result.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaKeySession-off(type: 'keysChange', callback?: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void--><!--Device-MediaKeySession-off(type: 'keysChange', callback?: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keysChange' | Yes |
| callback | (keyInfo: KeysInfo[], newKeyAvailable: boolean) = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## off_vendorDefined

```TypeScript
off(type: 'vendorDefined', callback?: (eventInfo: EventInfo) => void): void
```

Unsubscribes from vendor-defined events. This API uses an asynchronous callback to return the result.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaKeySession-off(type: 'vendorDefined', callback?: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-off(type: 'vendorDefined', callback?: (eventInfo: EventInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'vendorDefined' | Yes |
| callback | (eventInfo: EventInfo) = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## onExpirationUpdate

```TypeScript
onExpirationUpdate(callback: (eventInfo: EventInfo) => void): void
```

Register expirationUpdate event.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaKeySession-onExpirationUpdate(callback: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-onExpirationUpdate(callback: (eventInfo: EventInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (eventInfo: EventInfo) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## onKeyExpired

```TypeScript
onKeyExpired(callback: (eventInfo: EventInfo) => void): void
```

Register keyExpired event.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaKeySession-onKeyExpired(callback: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-onKeyExpired(callback: (eventInfo: EventInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (eventInfo: EventInfo) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## onKeyRequired

```TypeScript
onKeyRequired(callback: (eventInfo: EventInfo) => void): void
```

Register keyRequired event.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaKeySession-onKeyRequired(callback: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-onKeyRequired(callback: (eventInfo: EventInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (eventInfo: EventInfo) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## onKeysChange

```TypeScript
onKeysChange(callback: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void
```

Register keysChange event.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaKeySession-onKeysChange(callback: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void--><!--Device-MediaKeySession-onKeysChange(callback: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (keyInfo: KeysInfo[], newKeyAvailable: boolean) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## onVendorDefined

```TypeScript
onVendorDefined(callback: (eventInfo: EventInfo) => void): void
```

Register vendorDefined event.

**Since:** 23

**Deprecated since:** -1

<!--Device-MediaKeySession-onVendorDefined(callback: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-onVendorDefined(callback: (eventInfo: EventInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (eventInfo: EventInfo) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## on_expirationUpdate

```TypeScript
on(type: 'expirationUpdate', callback: (eventInfo: EventInfo) => void): void
```

Subscribes to events indicating that a media key is updated upon expiry. This API uses an asynchronous callback to return the result.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaKeySession-on(type: 'expirationUpdate', callback: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-on(type: 'expirationUpdate', callback: (eventInfo: EventInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'expirationUpdate' | Yes |
| callback | (eventInfo: EventInfo) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## on_keyExpired

```TypeScript
on(type: 'keyExpired', callback: (eventInfo: EventInfo) => void): void
```

Subscribes to events indicating that a media key expires. This API uses an asynchronous callback to return the result.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaKeySession-on(type: 'keyExpired', callback: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-on(type: 'keyExpired', callback: (eventInfo: EventInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyExpired' | Yes |
| callback | (eventInfo: EventInfo) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## on_keyRequired

```TypeScript
on(type: 'keyRequired', callback: (eventInfo: EventInfo) => void): void
```

Subscribes to events indicating that the application requests a media key. This API uses an asynchronous callback to return the result.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaKeySession-on(type: 'keyRequired', callback: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-on(type: 'keyRequired', callback: (eventInfo: EventInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyRequired' | Yes |
| callback | (eventInfo: EventInfo) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## on_keysChange

```TypeScript
on(type: 'keysChange', callback: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void
```

Subscribes to events indicating that a media key changes. This API uses an asynchronous callback to return the result.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaKeySession-on(type: 'keysChange', callback: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void--><!--Device-MediaKeySession-on(type: 'keysChange', callback: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keysChange' | Yes |
| callback | (keyInfo: KeysInfo[], newKeyAvailable: boolean) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## on_vendorDefined

```TypeScript
on(type: 'vendorDefined', callback: (eventInfo: EventInfo) => void): void
```

Subscribes to vendor-defined events. This API uses an asynchronous callback to return the result.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaKeySession-on(type: 'vendorDefined', callback: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-on(type: 'vendorDefined', callback: (eventInfo: EventInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'vendorDefined' | Yes |
| callback | (eventInfo: EventInfo) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## processMediaKeyResponse

```TypeScript
processMediaKeyResponse(response: Uint8Array): Promise<Uint8Array>
```

Processes a media key response. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaKeySession-processMediaKeyResponse(response: Uint8Array): Promise<Uint8Array>--><!--Device-MediaKeySession-processMediaKeyResponse(response: Uint8Array): Promise<Uint8Array>-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| response | Uint8Array | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Uint8Array & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## processOfflineReleaseResponse

```TypeScript
processOfflineReleaseResponse(mediaKeyId: Uint8Array, response: Uint8Array): Promise<void>
```

Processes a response to a request for releasing offline media keys. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaKeySession-processOfflineReleaseResponse(mediaKeyId: Uint8Array, response: Uint8Array): Promise<void>--><!--Device-MediaKeySession-processOfflineReleaseResponse(mediaKeyId: Uint8Array, response: Uint8Array): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mediaKeyId | Uint8Array | Yes |
| response | Uint8Array | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## requireSecureDecoderModule

```TypeScript
requireSecureDecoderModule(mimeType: string): boolean
```

Checks whether secure decoding is required.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaKeySession-requireSecureDecoderModule(mimeType: string): boolean--><!--Device-MediaKeySession-requireSecureDecoderModule(mimeType: string): boolean-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mimeType | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |

## restoreOfflineMediaKeys

```TypeScript
restoreOfflineMediaKeys(mediaKeyId: Uint8Array): Promise<void>
```

Restores offline media keys. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaKeySession-restoreOfflineMediaKeys(mediaKeyId: Uint8Array): Promise<void>--><!--Device-MediaKeySession-restoreOfflineMediaKeys(mediaKeyId: Uint8Array): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mediaKeyId | Uint8Array | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |
