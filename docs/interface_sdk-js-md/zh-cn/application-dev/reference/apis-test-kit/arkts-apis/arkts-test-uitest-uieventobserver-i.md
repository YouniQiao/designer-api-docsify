# UIEventObserver

UI事件监听器。

**起始版本：** 10

**系统能力：** SystemCapability.Test.UiTest

## 导入模块

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from 'kits/@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from 'kits/@kit.TestKit';
```

## once('toastShow')

```TypeScript
once(type: 'toastShow', callback: Callback<UIElementInfo>): void
```

开始监听toast控件出现的事件，使用callback的形式返回结果。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'toastShow' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UIElementInfo](arkts-test-uitest-uielementinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## once('dialogShow')

```TypeScript
once(type: 'dialogShow', callback: Callback<UIElementInfo>): void
```

开始监听dialog控件出现的事件，使用callback的形式返回结果。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'dialogShow' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UIElementInfo](arkts-test-uitest-uielementinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## once('windowChange')

```TypeScript
once(type: 'windowChange', windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void
```

开始监听指定类型的窗口变化事件，支持设置事件监听的扩展配置，监听到指定窗口变化事件时触发callback回调。仅支持 [自由多窗模式](../../../windowmanager/window-terminology.md#自由多窗模式)的窗口监听。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'windowChange' | 是 |
| [windowChangeType](arkts-test-uitest-uielementinfo-i.md) | [WindowChangeType](arkts-test-uitest-windowchangetype-e.md) | 是 |
| options | [WindowChangeOptions](arkts-test-uitest-windowchangeoptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UIElementInfo](arkts-test-uitest-uielementinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17000005](../errorcode-uitest.md#17000005-操作不支持) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## once('componentEventOccur')

```TypeScript
once(type: 'componentEventOccur', componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void
```

开始监听指定类型的控件操作事件，支持设置事件监听的扩展配置，监听到指定控件操作事件时触发callback回调。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'componentEventOccur' | 是 |
| [componentEventType](arkts-test-uitest-uielementinfo-i.md) | [ComponentEventType](arkts-test-uitest-componenteventtype-e.md) | 是 |
| options | [ComponentEventOptions](arkts-test-uitest-componenteventoptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UIElementInfo](arkts-test-uitest-uielementinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17000005](../errorcode-uitest.md#17000005-操作不支持) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |
