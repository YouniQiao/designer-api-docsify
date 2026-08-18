# UIEventObserver

UI事件监听器。

**起始版本：** 23

<!--Device-unnamed-declare interface UIEventObserver--><!--Device-unnamed-declare interface UIEventObserver-End-->

**系统能力：** SystemCapability.Test.UiTest

## 导入模块

```TypeScript
```

## onceComponentEventOccur

```TypeScript
onceComponentEventOccur(componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void
```

Listen on component event once, additional listening options can be set.

**起始版本：** 23

<!--Device-UIEventObserver-onceComponentEventOccur(componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void--><!--Device-UIEventObserver-onceComponentEventOccur(componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [componentEventType](arkts-test-uitest-uielementinfo-i.md) | [ComponentEventType](arkts-test-uitest-componenteventtype-e.md) | 是 |
| options | [ComponentEventOptions](arkts-test-uitest-componenteventoptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UIElementInfo](arkts-test-uitest-uielementinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |
| [17000005](../errorcode-uitest.md#17000005-操作不支持) |

## onceDialogShow

```TypeScript
onceDialogShow(callback: Callback<UIElementInfo>): void
```

Listen for dialog show once

**起始版本：** 23

<!--Device-UIEventObserver-onceDialogShow(callback: Callback<UIElementInfo>): void--><!--Device-UIEventObserver-onceDialogShow(callback: Callback<UIElementInfo>): void-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UIElementInfo](arkts-test-uitest-uielementinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## onceToastShow

```TypeScript
onceToastShow(callback: Callback<UIElementInfo>): void
```

Listen for toast show once

**起始版本：** 23

<!--Device-UIEventObserver-onceToastShow(callback: Callback<UIElementInfo>): void--><!--Device-UIEventObserver-onceToastShow(callback: Callback<UIElementInfo>): void-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UIElementInfo](arkts-test-uitest-uielementinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## onceWindowChange

```TypeScript
onceWindowChange(windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void
```

Listen on window change once, additional listening options can be set.

**起始版本：** 23

<!--Device-UIEventObserver-onceWindowChange(windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void--><!--Device-UIEventObserver-onceWindowChange(windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [windowChangeType](arkts-test-uitest-uielementinfo-i.md) | [WindowChangeType](arkts-test-uitest-windowchangetype-e.md) | 是 |
| options | [WindowChangeOptions](arkts-test-uitest-windowchangeoptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UIElementInfo](arkts-test-uitest-uielementinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |
| [17000005](../errorcode-uitest.md#17000005-操作不支持) |

## once_componentEventOccur

```TypeScript
once(type: 'componentEventOccur', componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void
```

开始监听指定类型的控件操作事件，支持设置事件监听的扩展配置，监听到指定控件操作事件时触发callback回调。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UIEventObserver-once(type: 'componentEventOccur', componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void--><!--Device-UIEventObserver-once(type: 'componentEventOccur', componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'componentEventOccur' | 是 |
| [componentEventType](arkts-test-uitest-uielementinfo-i.md) | [ComponentEventType](arkts-test-uitest-componenteventtype-e.md) | 是 |
| options | [ComponentEventOptions](arkts-test-uitest-componenteventoptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UIElementInfo](arkts-test-uitest-uielementinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |
| [17000005](../errorcode-uitest.md#17000005-操作不支持) |

**示例**

```TypeScript
// xxx.test.ets
import { Driver, UIElementInfo, UIEventObserver, ComponentEventOptions, ComponentEventType, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let observer: UIEventObserver = driver.createUIEventObserver();
  let option: ComponentEventOptions = {
    timeout: 20000,
    on: ON.id('123')  // 请开发者替换为实际存在的控件id值。
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

## once_dialogShow

```TypeScript
once(type: 'dialogShow', callback: Callback<UIElementInfo>): void
```

开始监听dialog控件出现的事件，使用callback的形式返回结果。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIEventObserver-once(type: 'dialogShow', callback: Callback<UIElementInfo>): void--><!--Device-UIEventObserver-once(type: 'dialogShow', callback: Callback<UIElementInfo>): void-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'dialogShow' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UIElementInfo](arkts-test-uitest-uielementinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

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

## once_toastShow

```TypeScript
once(type: 'toastShow', callback: Callback<UIElementInfo>): void
```

开始监听toast控件出现的事件，使用callback的形式返回结果。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIEventObserver-once(type: 'toastShow', callback: Callback<UIElementInfo>): void--><!--Device-UIEventObserver-once(type: 'toastShow', callback: Callback<UIElementInfo>): void-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'toastShow' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UIElementInfo](arkts-test-uitest-uielementinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
// xxx.test.ets
import { Driver, UIElementInfo, UIEventObserver } from '@kit.TestKit';

async function demo() {
  // 创建Driver对象。
  let driver: Driver = Driver.create();
  // 创建UI事件监听器。
  let observer: UIEventObserver = driver.createUIEventObserver();
  // 定义回调函数，输出toast控件的属性信息。
  let callback = (UIElementInfo: UIElementInfo) => {
    console.info(UIElementInfo.bundleName);
    console.info(UIElementInfo.text);
    console.info(UIElementInfo.type);
  }
  // 订阅toast控件出现事件。
  observer.once('toastShow', callback);
}
```

## once_windowChange

```TypeScript
once(type: 'windowChange', windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void
```

开始监听指定类型的窗口变化事件，支持设置事件监听的扩展配置，监听到指定窗口变化事件时触发callback回调。仅支持 [自由多窗模式](../../../windowmanager/window-terminology.md#自由多窗模式)的窗口监听。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UIEventObserver-once(type: 'windowChange', windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void--><!--Device-UIEventObserver-once(type: 'windowChange', windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'windowChange' | 是 |
| [windowChangeType](arkts-test-uitest-uielementinfo-i.md) | [WindowChangeType](arkts-test-uitest-windowchangetype-e.md) | 是 |
| options | [WindowChangeOptions](arkts-test-uitest-windowchangeoptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UIElementInfo](arkts-test-uitest-uielementinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |
| [17000005](../errorcode-uitest.md#17000005-操作不支持) |

**示例**

```TypeScript
// xxx.test.ets
import { Driver, UIElementInfo, UIEventObserver, WindowChangeOptions, WindowChangeType } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let observer: UIEventObserver = driver.createUIEventObserver();
  let options: WindowChangeOptions = {
    timeout: 20000,
    bundleName: 'com.example.myapplication'  // 请开发者替换为实际包名。
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
