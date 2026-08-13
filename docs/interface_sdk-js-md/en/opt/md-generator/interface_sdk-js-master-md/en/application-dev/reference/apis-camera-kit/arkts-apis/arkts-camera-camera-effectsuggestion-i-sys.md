# EffectSuggestion (System API)

EffectSuggestion object.

**Since:** 23

**Deprecated since:** -1

<!--Device-camera-interface EffectSuggestion--><!--Device-camera-interface EffectSuggestion-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## enableEffectSuggestion

```TypeScript
enableEffectSuggestion(enabled: boolean): void
```

Enable effect suggestion for session.

**Since:** 23

**Deprecated since:** -1

<!--Device-EffectSuggestion-enableEffectSuggestion(enabled: boolean): void--><!--Device-EffectSuggestion-enableEffectSuggestion(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getSupportedEffectSuggestionTypes

```TypeScript
getSupportedEffectSuggestionTypes(): Array<EffectSuggestionType>
```

Gets supported effect suggestion types.

**Since:** 23

**Deprecated since:** -1

<!--Device-EffectSuggestion-getSupportedEffectSuggestionTypes(): Array<EffectSuggestionType>--><!--Device-EffectSuggestion-getSupportedEffectSuggestionTypes(): Array<EffectSuggestionType>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[EffectSuggestionType](arkts-camera-camera-effectsuggestiontype-e-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## isEffectSuggestionSupported

```TypeScript
isEffectSuggestionSupported(): boolean
```

Checks whether effect suggestion is supported.

**Since:** 23

**Deprecated since:** -1

<!--Device-EffectSuggestion-isEffectSuggestionSupported(): boolean--><!--Device-EffectSuggestion-isEffectSuggestionSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## setEffectSuggestionStatus

```TypeScript
setEffectSuggestionStatus(status: Array<EffectSuggestionStatus>): void
```

Set the range of effect suggestion type and enable status. The application should fully set all data when it starts up.

**Since:** 23

**Deprecated since:** -1

<!--Device-EffectSuggestion-setEffectSuggestionStatus(status: Array<EffectSuggestionStatus>): void--><!--Device-EffectSuggestion-setEffectSuggestionStatus(status: Array<EffectSuggestionStatus>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| status | Array&lt;[EffectSuggestionStatus](arkts-camera-camera-effectsuggestionstatus-c-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## updateEffectSuggestion

```TypeScript
updateEffectSuggestion(type: EffectSuggestionType, enabled: boolean): void
```

Update the enable status of the effect suggestion type.

**Since:** 23

**Deprecated since:** -1

<!--Device-EffectSuggestion-updateEffectSuggestion(type: EffectSuggestionType, enabled: boolean): void--><!--Device-EffectSuggestion-updateEffectSuggestion(type: EffectSuggestionType, enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [EffectSuggestionType](arkts-camera-camera-effectsuggestiontype-e-sys.md) | Yes |
| enabled | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
