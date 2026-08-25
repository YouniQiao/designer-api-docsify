# on

## Modules to Import

```TypeScript
import { accessibility } from 'kits/@kit.AccessibilityKit';
import { AccessibilityEventType, AccessibilityAction, FocusMoveResultCode, InjectActionType, AccessibilityFocusScene, FocusRuleType, OperateVirtualNodeResult, AccessibilitySourceType } from 'kits/@kit.AccessibilityKit';
```

## on('accessibilityStateChange')

```TypeScript
function on(type: 'accessibilityStateChange', callback: Callback<boolean>): void
```

Subscribes to the state changes of the accessibility application. This API uses an asynchronous callback to return the result.To obtain information about accessibility applications in the system, you are advised to use [accessibility.getAccessibilityExtensionListSync](arkts-accessibility-accessibility-getaccessibilityextensionlistsync-f.md).

> **NOTE：**&gt;
> - The callback parameter for registering a listener must use a named function instead of an anonymous function.
> Otherwise, a new underlying object is created each time the function is called, causing memory leakage.&gt;
> - After calling this method, ensure that
> accessibility.off('accessibilityStateChange')
> is used to unsubscribe before the component instance is destroyed (for example, in the **aboutToDisappear**
> lifecycle callback). Otherwise, a crash may occur.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'accessibilityStateChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## on('touchGuideStateChange')

```TypeScript
function on(type: 'touchGuideStateChange', callback: Callback<boolean>): void
```

Subscribes to the state changes of touch guide mode. This API uses an asynchronous callback to return the result.To obtain information about accessibility applications in the system, you are advised to use [accessibility.getAccessibilityExtensionListSync](arkts-accessibility-accessibility-getaccessibilityextensionlistsync-f.md).

> **NOTE：**&gt;
> - The callback parameter for registering a listener must use a named function instead of an anonymous function.
> Otherwise, a new underlying object is created each time the function is called, causing memory leakage.&gt;
> - After calling this method, ensure that
> accessibility.off('touchGuideStateChange')
> is used to unsubscribe before the component instance is destroyed (for example, in the **aboutToDisappear**
> lifecycle callback). Otherwise, a crash may occur.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.BarrierFree.Accessibility.Vision

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'touchGuideStateChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## on('screenReaderStateChange')

```TypeScript
function on(type: 'screenReaderStateChange', callback: Callback<boolean>): void
```

Subscribes to the state changes of screen reader mode. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> - The callback parameter for registering a listener must use a named function instead of an anonymous function.
> Otherwise, a new underlying object is created each time the function is called, causing memory leakage.&gt;
> - After calling this method, ensure that
> accessibility.off('screenReaderStateChange')
> is used to unsubscribe before the component instance is destroyed (for example, in the **aboutToDisappear**
> lifecycle callback). Otherwise, a crash may occur.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'screenReaderStateChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## on('touchModeChange')

```TypeScript
function on(type: 'touchModeChange', callback: Callback<string>): void
```

Subscribes to the single-tap/number-tap operation mode change event in touch guide mode. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> - The callback parameter for registering a listener must use a named function instead of an anonymous function.
> Otherwise, a new underlying object is created each time the function is called, causing memory leakage.&gt;
> - After calling this method, ensure that
> accessibility.off('touchModeChange')
> is used to unsubscribe before the component instance is destroyed (for example, in the **aboutToDisappear**
> lifecycle callback). Otherwise, a crash may occur.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'touchModeChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
