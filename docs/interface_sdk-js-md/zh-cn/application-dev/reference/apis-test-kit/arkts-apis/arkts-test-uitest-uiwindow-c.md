# UiWindow

UiWindow代表了UI界面上的一个窗口，提供窗口属性获取，窗口拖动、调整窗口大小等能力。该类对象可通过[findWindow](arkts-test-uitest-driver-c.md#findwindow)接口获取。 该类提供的所有方法都使用Promise方式作为异步方法，需使用await方式调用。

**起始版本：** 9

**系统能力：** SystemCapability.Test.UiTest

## 导入模块

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from 'kits/@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from 'kits/@kit.TestKit';
```

## close

```TypeScript
close(): Promise<void>
```

将窗口关闭。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |
| [17000005](../errorcode-uitest.md#17000005-操作不支持) |

## focus

```TypeScript
focus(): Promise<void>
```

让窗口获焦。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## getBounds

```TypeScript
getBounds(): Promise<Rect>
```

获取窗口的边框信息。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Rect](arkts-test-uitest-rect-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## getBundleName

```TypeScript
getBundleName(): Promise<string>
```

获取窗口归属应用的包名信息。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## getDisplayId

```TypeScript
getDisplayId(): Promise<number>
```

获取窗口所属的屏幕ID。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## getTitle

```TypeScript
getTitle(): Promise<string>
```

获取窗口的标题信息。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## getWindowMode

```TypeScript
getWindowMode(): Promise<WindowMode>
```

获取窗口的窗口模式信息。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise&lt;[WindowMode](arkts-test-uitest-windowmode-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## isActive

```TypeScript
isActive(): Promise<boolean>
```

判断窗口是否为用户正在交互窗口。使用Promise异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## isActived

```TypeScript
isActived(): Promise<boolean>
```

判断窗口是否为用户正在交互窗口。使用Promise异步回调。

> **说明：**&gt;
> 从API version 9开始支持，从API version 11开始废弃，建议使用[isActive&lt;sup&gt;11+&lt;/sup&gt;](#isactive)替代。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [isActive](#isactive)

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## isFocused

```TypeScript
isFocused(): Promise<boolean>
```

判断窗口是否处于获焦状态。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## maximize

```TypeScript
maximize(): Promise<void>
```

将窗口最大化。使用Promise异步回调。适用于支持窗口最大化操作的窗口。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |
| [17000005](../errorcode-uitest.md#17000005-操作不支持) |

## minimize

```TypeScript
minimize(): Promise<void>
```

将窗口最小化。使用Promise异步回调。适用于支持窗口最小化操作的窗口。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |
| [17000005](../errorcode-uitest.md#17000005-操作不支持) |

## moveTo

```TypeScript
moveTo(x: number, y: number): Promise<void>
```

将窗口移动到目标点。使用Promise异步回调。适用于支持移动的窗口。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |
| [17000005](../errorcode-uitest.md#17000005-操作不支持) |

## resize

```TypeScript
resize(wide: number, height: number, direction: ResizeDirection): Promise<void>
```

根据传入的宽、高和调整方向来调整窗口的大小。使用Promise异步回调。适用于支持调整大小的窗口。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| wide | number | 是 |
| height | number | 是 |
| direction | [ResizeDirection](arkts-test-uitest-resizedirection-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |
| [17000005](../errorcode-uitest.md#17000005-操作不支持) |

## resume

```TypeScript
resume(): Promise<void>
```

将窗口恢复到之前的窗口模式。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |
| [17000005](../errorcode-uitest.md#17000005-操作不支持) |

## split

```TypeScript
split(): Promise<void>
```

将窗口模式切换成分屏模式。使用Promise异步回调。适用于支持切换分屏模式的窗口。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |
| [17000005](../errorcode-uitest.md#17000005-操作不支持) |
