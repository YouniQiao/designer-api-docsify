# UIEventObserver

Defines a UI event listener, which is used to listen for various events on the UI, including the display of the  
**Toast** and **Dialog** components, window change event, and component operation event. An instance can be created using {@link Driver#createUIEventObserver}.

**Since:** 10

<!--Device-unnamed-declare interface UIEventObserver--><!--Device-unnamed-declare interface UIEventObserver-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from 'kits/@kit.TestKit';
```

## once('toastShow')

```TypeScript
once(type: 'toastShow', callback: Callback<UIElementInfo>): void
```

Subscribes to events of the toast component. This API uses a callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UIEventObserver-once(type: 'toastShow', callback: Callback<UIElementInfo>): void--><!--Device-UIEventObserver-once(type: 'toastShow', callback: Callback<UIElementInfo>): void-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'toastShow' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UIElementInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UIElementInfo, UIEventObserver } from '@kit.TestKit';

async function demo() {
  // Create a Driver object.
  let driver: Driver = Driver.create();
  // Register a UI event listener.
  let observer: UIEventObserver = driver.createUIEventObserver();
  // Define a callback to output the attribute information of the Toast component.
  let callback = (UIElementInfo: UIElementInfo) => {
    console.info(UIElementInfo.bundleName);
    console.info(UIElementInfo.text);
    console.info(UIElementInfo.type);
  }
  // Subscribe to the events of the Toast component display.
  observer.once('toastShow', callback);
}
```

## once('dialogShow')

```TypeScript
once(type: 'dialogShow', callback: Callback<UIElementInfo>): void
```

Subscribes to events of the dialog component. This API uses a callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UIEventObserver-once(type: 'dialogShow', callback: Callback<UIElementInfo>): void--><!--Device-UIEventObserver-once(type: 'dialogShow', callback: Callback<UIElementInfo>): void-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'dialogShow' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UIElementInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UIElementInfo, UIEventObserver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let observer: UIEventObserver = driver.createUIEventObserver();
  let callback = (UIElementInfo: UIElementInfo) => {
    console.info(UIElementInfo.bundleName);
    console.info(UIElementInfo.text);
    console.info(UIElementInfo.type);
  }
  observer.once('dialogShow', callback);
}
```

## once('windowChange')

```TypeScript
once(type: 'windowChange', windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void
```

Starts listening for window change events of the specified type with extended configuration supported. This API triggers a callback when a specified window change event is detected.This API can be used only in [free windows](../../../windowmanager/window-terminology.md#free-windows) mode.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-UIEventObserver-once(type: 'windowChange', windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void--><!--Device-UIEventObserver-once(type: 'windowChange', windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'windowChange' | Yes |
| windowChangeType | [WindowChangeType](arkts-test-uitest-windowchangetype-e.md) | Yes |
| options | [WindowChangeOptions](arkts-test-uitest-windowchangeoptions-i.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UIElementInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UIElementInfo, UIEventObserver, WindowChangeOptions, WindowChangeType } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let observer: UIEventObserver = driver.createUIEventObserver();
  let options: WindowChangeOptions = {
    timeout: 20000,
    bundleName: 'com.example.myapplication'  // Use the actual bundle name.
  }
  let callback = (UIElementInfo: UIElementInfo) => {
    console.info(UIElementInfo.bundleName);
    console.info(UIElementInfo.text);
    console.info(UIElementInfo.type);
    console.info(UIElementInfo.windowChangeType?.toString());
    console.info(UIElementInfo.windowId?.toString());
  }
  observer.once('windowChange', WindowChangeType.WINDOW_ADDED, options, callback);
}
```

## once('componentEventOccur')

```TypeScript
once(type: 'componentEventOccur', componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void
```

Starts listening for component operation events of the specified type with extended configuration supported. This API triggers a callback when a specified component operation event is detected.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-UIEventObserver-once(type: 'componentEventOccur', componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void--><!--Device-UIEventObserver-once(type: 'componentEventOccur', componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'componentEventOccur' | Yes |
| componentEventType | [ComponentEventType](arkts-test-uitest-componenteventtype-e.md) | Yes |
| options | [ComponentEventOptions](arkts-test-uitest-componenteventoptions-i.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UIElementInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UIElementInfo, UIEventObserver, ComponentEventOptions, ComponentEventType, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let observer: UIEventObserver = driver.createUIEventObserver();
  let option: ComponentEventOptions = {
    timeout: 20000,
    on: ON.id('123')  // Use the actual component ID.
  };
  let callback = (UIElementInfo: UIElementInfo) => {
    console.info(UIElementInfo.bundleName);
    console.info(UIElementInfo.text);
    console.info(UIElementInfo.type);
    console.info(UIElementInfo.componentEventType?.toString());
    console.info(UIElementInfo.windowId?.toString());
    console.info(UIElementInfo.componentId);
    console.info(UIElementInfo.componentRect?.left.toString());
    console.info(UIElementInfo.componentRect?.top.toString());
    console.info(UIElementInfo.componentRect?.right.toString());
    console.info(UIElementInfo.componentRect?.bottom.toString());
  };
  observer.once('componentEventOccur', ComponentEventType.COMPONENT_CLICKED, option, callback);
}
```
