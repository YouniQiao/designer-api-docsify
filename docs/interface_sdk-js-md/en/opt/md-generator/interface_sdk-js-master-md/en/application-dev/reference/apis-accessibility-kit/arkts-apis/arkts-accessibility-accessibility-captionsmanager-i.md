# CaptionsManager

Implements configuration management for captions. Before calling any API of **CaptionsManager**, you must use the   
[accessibility.getCaptionsManager()](arkts-accessibility-accessibility-getcaptionsmanager-f.md#getcaptionsmanager) API to obtain a **CaptionsManager** instance.

**Since:** 8

<!--Device-accessibility-interface CaptionsManager--><!--Device-accessibility-interface CaptionsManager-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Hearing

## Modules to Import

```TypeScript
import { accessibility } from 'kits/@kit.AccessibilityKit';
```

## off('enableChange')

```TypeScript
off(type: 'enableChange', callback?: Callback<boolean>): void
```

Unsubscribes from the state changes of captions configuration. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 12

<!--Device-CaptionsManager-off(type: 'enableChange', callback?: Callback<boolean>): void--><!--Device-CaptionsManager-off(type: 'enableChange', callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Hearing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'enableChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | No |

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
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe caption manager enable state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.on('enableChange', this.callback);
  }

  aboutToDisappear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.off('enableChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

## off('styleChange')

```TypeScript
off(type: 'styleChange', callback?: Callback<CaptionsStyle>): void
```

Unsubscribes from the captions style changes. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 12

<!--Device-CaptionsManager-off(type: 'styleChange', callback?: Callback<CaptionsStyle>): void--><!--Device-CaptionsManager-off(type: 'styleChange', callback?: Callback<CaptionsStyle>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Hearing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'styleChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CaptionsStyle&gt; | No |

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
  callback: (data: accessibility.CaptionsStyle) => void = this.eventCallback;
  eventCallback(data: accessibility.CaptionsStyle): void {
    console.info(`subscribe caption manager style state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.on('styleChange', this.callback);
  }

  aboutToDisappear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.off('styleChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

## on('enableChange')

```TypeScript
on(type: 'enableChange', callback: Callback<boolean>): void
```

Subscribes to the state changes of captions configuration. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> - The callback parameter for registering a listener must use a named function instead of an anonymous function.
> Otherwise, a new underlying object is created each time the function is called, causing memory leakage.
> 
> - After calling this method, you must use
> [off('enableChange')](accessibility.CaptionsManager.off(type: 'enableChange', callback?: Callback&lt;boolean&gt;))
> to cancel the listener before the object's lifecycle ends. Otherwise, a crash may occur.

**Since:** 8

**Deprecated since:** 12

<!--Device-CaptionsManager-on(type: 'enableChange', callback: Callback<boolean>): void--><!--Device-CaptionsManager-on(type: 'enableChange', callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Hearing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'enableChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes |

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
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe caption manager enable state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.on('enableChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

## on('styleChange')

```TypeScript
on(type: 'styleChange', callback: Callback<CaptionsStyle>): void
```

Subscribes to captions style changes. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> - The callback parameter for registering a listener must use a named function instead of an anonymous function.
> Otherwise, a new underlying object is created each time the function is called, causing memory leakage.
> 
> - After calling this method, you must use
> [off('styleChange')](accessibility.CaptionsManager.off(type: 'styleChange', callback?: Callback&lt;CaptionsStyle&gt;))
> to cancel the listener before the object's lifecycle ends. Otherwise, a crash may occur.

**Since:** 8

**Deprecated since:** 12

<!--Device-CaptionsManager-on(type: 'styleChange', callback: Callback<CaptionsStyle>): void--><!--Device-CaptionsManager-on(type: 'styleChange', callback: Callback<CaptionsStyle>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Hearing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'styleChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CaptionsStyle&gt; | Yes |

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
  callback: (data: accessibility.CaptionsStyle) => void = this.eventCallback;
  eventCallback(data: accessibility.CaptionsStyle): void {
    console.info(`subscribe caption manager style state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.on('styleChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

## enabled

```TypeScript
enabled: boolean
```

Whether to enable captions configuration. The value **true** indicates that the caption configuration is enabled,and **false** indicates the opposite.

**Type:** boolean

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-CaptionsManager-enabled: boolean--><!--Device-CaptionsManager-enabled: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Hearing

## style

```TypeScript
style: CaptionsStyle
```

Style of captions.

**Type:** [CaptionsStyle](arkts-accessibility-accessibility-captionsstyle-i.md)

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-CaptionsManager-style: CaptionsStyle--><!--Device-CaptionsManager-style: CaptionsStyle-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Hearing
