# UIEventObserver

UI事件监听器。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

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

开始监听toast控件出现的事件，使用callback的形式返回结果。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UIEventObserver-once(type: 'toastShow', callback: Callback<UIElementInfo>): void--><!--Device-UIEventObserver-once(type: 'toastShow', callback: Callback<UIElementInfo>): void-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'toastShow' | Yes | 订阅的事件类型，取值为'toastShow'。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UIElementInfo&gt; | Yes | 事件发生时执行的回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

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

开始监听dialog控件出现的事件，使用callback的形式返回结果。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UIEventObserver-once(type: 'dialogShow', callback: Callback<UIElementInfo>): void--><!--Device-UIEventObserver-once(type: 'dialogShow', callback: Callback<UIElementInfo>): void-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'dialogShow' | Yes | 订阅的事件类型，取值为'dialogShow'。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UIElementInfo&gt; | Yes | 事件发生时执行的回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

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

开始监听指定类型的窗口变化事件，支持设置事件监听的扩展配置，监听到指定窗口变化事件时触发callback回调。仅支持  
[自由多窗模式](../../../windowmanager/window-terminology.md#自由多窗模式)的窗口监听。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-UIEventObserver-once(type: 'windowChange', windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void--><!--Device-UIEventObserver-once(type: 'windowChange', windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'windowChange' | Yes | 订阅的事件类型，支持的事件为'windowChange'。当监听到窗口变化时，触发该事件。 |
| windowChangeType | [WindowChangeType](arkts-test-uitest-windowchangetype-e.md) | Yes | 窗口变化事件类型。 |
| options | [WindowChangeOptions](arkts-test-uitest-windowchangeoptions-i.md) | Yes | 窗口变化事件监听的扩展配置，包括监听超时时间和监听窗口对应包名。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UIElementInfo&gt; | Yes | 事件发生时执行的回调函数，返回事件的相关信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000007 | Parameter verification failed. |
| 17000005 | This operation is not supported. |

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

开始监听指定类型的控件操作事件，支持设置事件监听的扩展配置，监听到指定控件操作事件时触发callback回调。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-UIEventObserver-once(type: 'componentEventOccur', componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void--><!--Device-UIEventObserver-once(type: 'componentEventOccur', componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'componentEventOccur' | Yes | 订阅的事件类型，支持的事件为'componentEventOccur'。当监听到控件操作时，触发该事件。 |
| componentEventType | [ComponentEventType](arkts-test-uitest-componenteventtype-e.md) | Yes | 控件操作事件类型。 |
| options | [ComponentEventOptions](arkts-test-uitest-componenteventoptions-i.md) | Yes | 控件操作事件监听的扩展配置，包括监听超时时间和监听控件匹配条件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UIElementInfo&gt; | Yes | 事件发生时执行的回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000007 | Parameter verification failed. |
| 17000005 | This operation is not supported. |

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

## onceComponentEventOccur

```TypeScript
onceComponentEventOccur(componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void
```

Listen on component event once, additional listening options can be set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-UIEventObserver-onceComponentEventOccur(componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void--><!--Device-UIEventObserver-onceComponentEventOccur(componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| componentEventType | [ComponentEventType](arkts-test-uitest-componenteventtype-e.md) | Yes | Component event type to be listened on. |
| options | [ComponentEventOptions](arkts-test-uitest-componenteventoptions-i.md) | Yes | Additional listening options of component event. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UIElementInfo&gt; | Yes | function, returns the monitored UIElementInfo. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000007 | Parameter verification failed. |
| 17000005 | This operation is not supported. |

## onceDialogShow

```TypeScript
onceDialogShow(callback: Callback<UIElementInfo>): void
```

Listen for dialog show once

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-UIEventObserver-onceDialogShow(callback: Callback<UIElementInfo>): void--><!--Device-UIEventObserver-onceDialogShow(callback: Callback<UIElementInfo>): void-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UIElementInfo&gt; | Yes | function, returns the monitored UIElementInfo. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## onceToastShow

```TypeScript
onceToastShow(callback: Callback<UIElementInfo>): void
```

Listen for toast show once

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-UIEventObserver-onceToastShow(callback: Callback<UIElementInfo>): void--><!--Device-UIEventObserver-onceToastShow(callback: Callback<UIElementInfo>): void-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UIElementInfo&gt; | Yes | function, returns the monitored UIElementInfo. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## onceWindowChange

```TypeScript
onceWindowChange(windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void
```

Listen on window change once, additional listening options can be set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-UIEventObserver-onceWindowChange(windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void--><!--Device-UIEventObserver-onceWindowChange(windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| windowChangeType | [WindowChangeType](arkts-test-uitest-windowchangetype-e.md) | Yes | Window change type to be listened on. |
| options | [WindowChangeOptions](arkts-test-uitest-windowchangeoptions-i.md) | Yes | Additional listening options of window change. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UIElementInfo&gt; | Yes | function, returns the monitored UIElementInfo. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000007 | Parameter verification failed. |
| 17000005 | This operation is not supported. |

