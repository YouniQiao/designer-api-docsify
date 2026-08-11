# on

## Modules to Import

```TypeScript
import { accessibility } from 'kits/@kit.AccessibilityKit';
```

## on('accessibilityStateChange')

```TypeScript
function on(type: 'accessibilityStateChange', callback: Callback<boolean>): void
```

Subscribes to the state changes of the accessibility application. This API uses an asynchronous callback to return the result. To obtain information about accessibility applications in the system, use   
[accessibility.getAccessibilityExtensionListSync](arkts-accessibility-accessibility-getaccessibilityextensionlistsync-f.md#getaccessibilityextensionlistsync).

> **NOTE：**
> 
> - The callback parameter for registering a listener must use a named function instead of an anonymous function.
> Otherwise, a new underlying object is created each time the function is called, causing memory leakage.
> 
> - After calling this method, you must use
> [accessibility.off('accessibilityStateChange')](accessibility.off(type: 'accessibilityStateChange', callback?: Callback&lt;boolean&gt;))
> to cancel the listener before the object's lifecycle ends. Otherwise, a crash may occur.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-accessibility-function on(type: 'accessibilityStateChange', callback: Callback<boolean>): void--><!--Device-accessibility-function on(type: 'accessibilityStateChange', callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'accessibilityStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';

// When one or more accessibility applications have been installed in the system:
// 1. After the first application is enabled, the callback returns true.
// 2. If one or more applications have been enabled and the last enabled one is disabled, the callback returns false.
accessibility.on('accessibilityStateChange', (data: boolean) => {
  console.info(`subscribe accessibility state change, result: ${JSON.stringify(data)}`);
});
```


## on('touchGuideStateChange')

```TypeScript
function on(type: 'touchGuideStateChange', callback: Callback<boolean>): void
```

Subscribes to the state changes in touch guide mode. This API uses an asynchronous callback to return the result. To obtain information about accessibility applications in the system, use   
[accessibility.getAccessibilityExtensionListSync](arkts-accessibility-accessibility-getaccessibilityextensionlistsync-f.md#getaccessibilityextensionlistsync).

> **NOTE：**
> 
> - The callback parameter for registering a listener must use a named function instead of an anonymous function.
> Otherwise, a new underlying object is created each time the function is called, causing memory leakage.
> 
> - After calling this method, you must use
> [accessibility.off('touchGuideStateChange')](accessibility.off(type: 'touchGuideStateChange', callback?: Callback&lt;boolean&gt;))
> to cancel the listener before the object's lifecycle ends. Otherwise, a crash may occur.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-accessibility-function on(type: 'touchGuideStateChange', callback: Callback<boolean>): void--><!--Device-accessibility-function on(type: 'touchGuideStateChange', callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Vision

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'touchGuideStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';

// When one or more accessibility applications with touch guide mode (touchGuide is set in Capability) have been installed in the system:
// 1. After the first application is enabled, the callback returns true.
// 2. If one or more applications have been enabled and the last enabled one is disabled, the callback returns false.
accessibility.on('touchGuideStateChange', (data: boolean) => {
  console.info(`subscribe touch guide state change, result: ${JSON.stringify(data)}`);
});
```


## on('screenReaderStateChange')

```TypeScript
function on(type: 'screenReaderStateChange', callback: Callback<boolean>): void
```

Subscribes to the state changes of the screen reader. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> - The callback parameter for registering a listener must use a named function instead of an anonymous function.
> Otherwise, a new underlying object is created each time the function is called, causing memory leakage.
> 
> - After calling this method, you must use
> [accessibility.off('screenReaderStateChange')](accessibility.off(type: 'screenReaderStateChange', callback?: Callback&lt;boolean&gt;))
> to cancel the listener before the object's lifecycle ends. Otherwise, a crash may occur.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-accessibility-function on(type: 'screenReaderStateChange', callback: Callback<boolean>): void--><!--Device-accessibility-function on(type: 'screenReaderStateChange', callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'screenReaderStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';

accessibility.on('screenReaderStateChange', (data: boolean) => {
  console.info(`subscribe screen reader state change, result: ${JSON.stringify(data)}`);
});
```


## on('touchModeChange')

```TypeScript
function on(type: 'touchModeChange', callback: Callback<string>): void
```

Subscribes to the single- or double-touch event changes in touch guide mode. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> - The callback parameter for registering a listener must use a named function instead of an anonymous function.
> Otherwise, a new underlying object is created each time the function is called, causing memory leakage.
> 
> - After calling this method, you must use
> [accessibility.off('touchModeChange')](accessibility.off(type: 'touchModeChange', callback?: Callback&lt;string&gt;))
> to cancel the listener before the object's lifecycle ends. Otherwise, a crash may occur.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-accessibility-function on(type: 'touchModeChange', callback: Callback<string>): void--><!--Device-accessibility-function on(type: 'touchModeChange', callback: Callback<string>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'touchModeChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (mode: string) => void = this.eventCallback;
  eventCallback(mode: string): void {
    console.info(`current touch mode: ${JSON.stringify(mode)}`);
  }

  aboutToAppear(): void {
    accessibility.on('touchModeChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```
