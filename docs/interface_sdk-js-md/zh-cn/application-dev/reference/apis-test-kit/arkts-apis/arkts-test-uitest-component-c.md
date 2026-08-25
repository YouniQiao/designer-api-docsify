# Component

UiTest框架在API9中，Component类代表了UI界面上的一个控件，提供控件属性获取，控件点击，滑动查找，文本注入等API。 该类对象可通过[findComponent](arkts-test-uitest-driver-c.md#findcomponent)、[findComponents](arkts-test-uitest-driver-c.md#findcomponents)、[waitForComponent](arkts-test-uitest-driver-c.md#waitforcomponent)等接口获取。 该类提供的所有方法都使用Promise方式作为异步方法，需使用await调用。

**起始版本：** 9

**系统能力：** SystemCapability.Test.UiTest

## 导入模块

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from 'kits/@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from 'kits/@kit.TestKit';
```

## clearText

```TypeScript
clearText(): Promise<void>
```

清除控件的文本信息，仅针对可编辑的文本组件生效。使用Promise异步回调。

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

## click

```TypeScript
click(): Promise<void>
```

控件对象进行点击操作。使用Promise异步回调。

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

## doubleClick

```TypeScript
doubleClick(): Promise<void>
```

控件对象进行双击操作。使用Promise异步回调。

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

## dragTo

```TypeScript
dragTo(target: Component): Promise<void>
```

将控件拖拽至目标控件处。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | [Component](arkts-test-uitest-component-c.md) | 是 |

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

## getBounds

```TypeScript
getBounds(): Promise<Rect>
```

获取控件对象的边框信息。使用Promise异步回调。

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

## getBoundsCenter

```TypeScript
getBoundsCenter(): Promise<Point>
```

获取控件对象所占区域的中心点信息。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Point](arkts-test-uitest-point-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## getDescription

```TypeScript
getDescription(): Promise<string>
```

获取控件对象的描述信息。使用Promise异步回调。

**起始版本：** 11

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

获取控件对象所属的屏幕ID。使用Promise异步回调。

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

## getHint

```TypeScript
getHint(): Promise<string>
```

获取控件对象的提示文本。使用Promise异步回调。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

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

## getId

```TypeScript
getId(): Promise<string>
```

获取控件对象的id值。使用Promise异步回调。

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

## getOriginalText

```TypeScript
getOriginalText(): Promise<string>
```

获取控件对象的文本信息。使用Promise异步回调。如果控件的无障碍属性 accessibilityLevel 设置为'no'或'no-hide-descendants'，可以使用本接口获取控件的文本信息，无法使用[Component.getText()](#gettext)获取控件的文本信息。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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

## getText

```TypeScript
getText(): Promise<string>
```

获取控件对象的文本信息。使用Promise异步回调。

> **说明：**&gt;
> 如果控件的无障碍属性
> accessibilityLevel
> 设置为'no'或'no-hide-descendants'，无法使用本接口获取控件的文本信息，可以使用[Component.getOriginalText()](#getoriginaltext)
> 获取控件的文本信息。

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

## getType

```TypeScript
getType(): Promise<string>
```

获取控件对象的控件类型。使用Promise异步回调。

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

## inputText

```TypeScript
inputText(text: string): Promise<void>
```

清空组件内原有文本并输入指定文本内容，仅针对可编辑的文本组件生效。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |

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

## inputText

```TypeScript
inputText(text: string, mode: InputTextMode): Promise<void>
```

向控件中输入文本，并支持指定文本输入方式，仅针对可编辑的文本组件生效。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| mode | [InputTextMode](arkts-test-uitest-inputtextmode-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## isCheckable

```TypeScript
isCheckable(): Promise<boolean>
```

获取控件对象能否被勾选属性。使用Promise异步回调。

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

## isChecked

```TypeScript
isChecked(): Promise<boolean>
```

获取控件对象被勾选状态。使用Promise异步回调。

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

## isClickable

```TypeScript
isClickable(): Promise<boolean>
```

获取控件对象可点击属性。使用Promise异步回调。

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

## isEnabled

```TypeScript
isEnabled(): Promise<boolean>
```

获取控件使能状态。使用Promise异步回调。

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

## isFocused

```TypeScript
isFocused(): Promise<boolean>
```

判断控件对象获焦状态。使用Promise异步回调。

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

## isLongClickable

```TypeScript
isLongClickable(): Promise<boolean>
```

获取控件对象可点击属性。使用Promise异步回调。

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

## isScrollable

```TypeScript
isScrollable(): Promise<boolean>
```

获取控件对象可滑动属性。使用Promise异步回调。

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

## isSelected

```TypeScript
isSelected(): Promise<boolean>
```

获取控件对象被选中状态。使用Promise异步回调。

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

## longClick

```TypeScript
longClick(): Promise<void>
```

控件对象进行长按操作。使用Promise异步回调。

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

## pinchIn

```TypeScript
pinchIn(scale: number): Promise<void>
```

将控件按指定的比例进行捏合缩小。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scale | number | 是 |

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

## pinchOut

```TypeScript
pinchOut(scale: number): Promise<void>
```

将控件按指定的比例进行捏合放大。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scale | number | 是 |

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

## scrollSearch

```TypeScript
scrollSearch(on: On): Promise<Component>
```

在控件上滑动查找目标控件（适用支持滑动的控件）。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Component](arkts-test-uitest-component-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## scrollSearch

```TypeScript
scrollSearch(on: On, vertical?: boolean, offset?: number): Promise<Component>
```

在控件上滑动查找目标控件（适用支持滑动的控件），支持指定滑动方向和滑动起止点与组件边框的偏移量。使用Promise异步回调。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | 是 |
| vertical | boolean | 否 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Component](arkts-test-uitest-component-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## scrollToBottom

```TypeScript
scrollToBottom(speed?: number): Promise<void>
```

在控件上滑动到底部（适用支持滑动的控件）。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| speed | number | 否 |

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

## scrollToTop

```TypeScript
scrollToTop(speed?: number): Promise<void>
```

在控件上滑动到顶部（适用支持滑动的控件）。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| speed | number | 否 |

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
