# IntelligentVoiceManager (System API)

Implements intelligent voice management.

**Since:** 23

**Deprecated since:** -1

<!--Device-intelligentVoice-interface IntelligentVoiceManager--><!--Device-intelligentVoice-interface IntelligentVoiceManager-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { intelligentVoice } from '@kit.BasicServicesKit';
```

## getCapabilityInfo

```TypeScript
getCapabilityInfo(): Array<IntelligentVoiceEngineType>
```

Obtains capability information.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-IntelligentVoiceManager-getCapabilityInfo(): Array<IntelligentVoiceEngineType>--><!--Device-IntelligentVoiceManager-getCapabilityInfo(): Array<IntelligentVoiceEngineType>-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[IntelligentVoiceEngineType](arkts-basicservices-intelligentvoice-intelligentvoiceenginetype-e-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
if (intelligentVoiceManager != null) {
  let info = intelligentVoiceManager.getCapabilityInfo();
}
```

## offServiceChange

```TypeScript
offServiceChange(callback?: Callback<ServiceChangeType>): void
```

Unsubscribes service change events.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-IntelligentVoiceManager-offServiceChange(callback?: Callback<ServiceChangeType>): void--><!--Device-IntelligentVoiceManager-offServiceChange(callback?: Callback<ServiceChangeType>): void-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[ServiceChangeType](arkts-basicservices-intelligentvoice-servicechangetype-e-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## off_serviceChange

```TypeScript
off(type: 'serviceChange', callback?: Callback<ServiceChangeType>): void
```

Unsubscribes service change events.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-IntelligentVoiceManager-off(type: 'serviceChange', callback?: Callback<ServiceChangeType>): void--><!--Device-IntelligentVoiceManager-off(type: 'serviceChange', callback?: Callback<ServiceChangeType>): void-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'serviceChange' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[ServiceChangeType](arkts-basicservices-intelligentvoice-servicechangetype-e-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
if (intelligentVoiceManager != null) {
  intelligentVoiceManager.off('serviceChange');
}
```

## onServiceChange

```TypeScript
onServiceChange(callback: Callback<ServiceChangeType>): void
```

Subscribes service change events. When the state of intelligent voice service changes, the callback is invoked.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-IntelligentVoiceManager-onServiceChange(callback: Callback<ServiceChangeType>): void--><!--Device-IntelligentVoiceManager-onServiceChange(callback: Callback<ServiceChangeType>): void-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[ServiceChangeType](arkts-basicservices-intelligentvoice-servicechangetype-e-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on_serviceChange

```TypeScript
on(type: 'serviceChange', callback: Callback<ServiceChangeType>): void
```

Subscribes service change events. When the state of intelligent voice service changes, the callback is invoked.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_INTELLIGENT_VOICE

<!--Device-IntelligentVoiceManager-on(type: 'serviceChange', callback: Callback<ServiceChangeType>): void--><!--Device-IntelligentVoiceManager-on(type: 'serviceChange', callback: Callback<ServiceChangeType>): void-End-->

**System capability:** SystemCapability.AI.IntelligentVoice.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'serviceChange' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[ServiceChangeType](arkts-basicservices-intelligentvoice-servicechangetype-e-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
if (intelligentVoiceManager != null) {
  intelligentVoiceManager.on('serviceChange', (serviceChangeType: intelligentVoice.ServiceChangeType) => {});
}
```
