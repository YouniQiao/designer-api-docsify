# IntelligentVoiceManager (System API)

Implements intelligent voice management.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-intelligentVoice-interface IntelligentVoiceManager--><!--Device-intelligentVoice-interface IntelligentVoiceManager-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { intelligentVoice } from 'kits/@kit.BasicServicesKit';
```

## getCapabilityInfo

```TypeScript
getCapabilityInfo(): Array<IntelligentVoiceEngineType>
```

Obtains capability information.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-IntelligentVoiceManager-getCapabilityInfo(): Array<IntelligentVoiceEngineType>--><!--Device-IntelligentVoiceManager-getCapabilityInfo(): Array<IntelligentVoiceEngineType>-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;IntelligentVoiceEngineType&gt; | array of supported IntelligentVoiceEngineType. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |

## Examples

```TypeScript
if (intelligentVoiceManager != null) {
  let info = intelligentVoiceManager.getCapabilityInfo();
}
```

## off('serviceChange')

```TypeScript
off(type: 'serviceChange', callback?: Callback<ServiceChangeType>): void
```

Unsubscribes service change events.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-IntelligentVoiceManager-off(type: 'serviceChange', callback?: Callback<ServiceChangeType>): void--><!--Device-IntelligentVoiceManager-off(type: 'serviceChange', callback?: Callback<ServiceChangeType>): void-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'serviceChange' | Yes | Type of the event to listen for. Only the serviceChange event is supported. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;ServiceChangeType&gt; | No | Callback is invoked when the event is triggered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |

## Examples

```TypeScript
if (intelligentVoiceManager != null) {
  intelligentVoiceManager.off('serviceChange');
}
```

## offServiceChange

```TypeScript
offServiceChange(callback?: Callback<ServiceChangeType>): void
```

Unsubscribes service change events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-IntelligentVoiceManager-offServiceChange(callback?: Callback<ServiceChangeType>): void--><!--Device-IntelligentVoiceManager-offServiceChange(callback?: Callback<ServiceChangeType>): void-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;ServiceChangeType&gt; | No | Callback is invoked when the event is triggered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |

## on('serviceChange')

```TypeScript
on(type: 'serviceChange', callback: Callback<ServiceChangeType>): void
```

Subscribes service change events. When the state of intelligent voice service changes,the callback is invoked.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-IntelligentVoiceManager-on(type: 'serviceChange', callback: Callback<ServiceChangeType>): void--><!--Device-IntelligentVoiceManager-on(type: 'serviceChange', callback: Callback<ServiceChangeType>): void-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'serviceChange' | Yes | Type of the event to listen for. Only the serviceChange event is supported. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;ServiceChangeType&gt; | Yes | Callback is invoked when the event is triggered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |

## Examples

```TypeScript
if (intelligentVoiceManager != null) {
  intelligentVoiceManager.on('serviceChange', (serviceChangeType: intelligentVoice.ServiceChangeType) => {});
}
```

## onServiceChange

```TypeScript
onServiceChange(callback: Callback<ServiceChangeType>): void
```

Subscribes service change events. When the state of intelligent voice service changes,the callback is invoked.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-IntelligentVoiceManager-onServiceChange(callback: Callback<ServiceChangeType>): void--><!--Device-IntelligentVoiceManager-onServiceChange(callback: Callback<ServiceChangeType>): void-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;ServiceChangeType&gt; | Yes | Callback is invoked when the event is triggered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |

