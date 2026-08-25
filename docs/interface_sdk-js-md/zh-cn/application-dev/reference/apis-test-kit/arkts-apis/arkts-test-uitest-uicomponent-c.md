# UiComponent

UiTest中，UiComponent类代表了UI界面上的一个控件，提供控件属性获取，控件点击，滑动查找，文本注入等API。 该类提供的所有方法都使用Promise方式作为异步方法，需使用await调用。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[Component&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [Component](arkts-test-uitest-component-c.md)

**系统能力：** SystemCapability.Test.UiTest

## 导入模块

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from 'kits/@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from 'kits/@kit.TestKit';
```

## click

```TypeScript
click(): Promise<void>
```

控件对象进行点击操作。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[click&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#click)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [click](arkts-test-uitest-component-c.md#click)

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## doubleClick

```TypeScript
doubleClick(): Promise<void>
```

控件对象进行双击操作。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[doubleClick&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#doubleclick)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [doubleClick](arkts-test-uitest-component-c.md#doubleclick)

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## getId

```TypeScript
getId(): Promise<number>
```

获取控件对象的id值。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[getId&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#getid)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getId](arkts-test-uitest-component-c.md#getid)

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getKey

```TypeScript
getKey(): Promise<string>
```

获取控件对象的key值。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[getId&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#getid)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getId](arkts-test-uitest-component-c.md#getid)

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getText

```TypeScript
getText(): Promise<string>
```

获取控件对象的文本信息。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[getText&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#gettext)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getText](arkts-test-uitest-component-c.md#gettext)

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getType

```TypeScript
getType(): Promise<string>
```

获取控件对象的控件类型。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[getType&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#gettype)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getType](arkts-test-uitest-component-c.md#gettype)

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## inputText

```TypeScript
inputText(text: string): Promise<void>
```

向控件中输入文本，仅针对可编辑的文本组件生效。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[inputText&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#inputtext)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [inputText](arkts-test-uitest-component-c.md#inputtext)(text: string)

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## isClickable

```TypeScript
isClickable(): Promise<boolean>
```

获取控件对象可点击状态。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[isClickable&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#isclickable)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isClickable](arkts-test-uitest-component-c.md#isclickable)

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## isEnabled

```TypeScript
isEnabled(): Promise<boolean>
```

获取控件使能状态。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[isEnabled&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#isenabled)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isEnabled](arkts-test-uitest-component-c.md#isenabled)

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## isFocused

```TypeScript
isFocused(): Promise<boolean>
```

判断控件对象是否获焦。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[isFocused&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#isfocused)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isFocused](arkts-test-uitest-component-c.md#isfocused)

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## isScrollable

```TypeScript
isScrollable(): Promise<boolean>
```

获取控件对象可滑动状态。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[isScrollable&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#isscrollable)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isScrollable](arkts-test-uitest-component-c.md#isscrollable)

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## isSelected

```TypeScript
isSelected(): Promise<boolean>
```

获取控件对象被选中状态。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[isSelected&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#isselected)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isSelected](arkts-test-uitest-component-c.md#isselected)

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## longClick

```TypeScript
longClick(): Promise<void>
```

控件对象进行长按操作。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[longClick&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#longclick)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [longClick](arkts-test-uitest-component-c.md#longclick)

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## scrollSearch

```TypeScript
scrollSearch(by: By): Promise<UiComponent>
```

在控件上滑动查找目标控件（适用于List等支持滑动的控件）。使用Promise异步回调。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[scrollSearch&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#scrollsearch)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [scrollSearch](arkts-test-uitest-component-c.md#scrollsearch)(on: On)

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| by | [By](arkts-test-uitest-by-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[UiComponent](arkts-test-uitest-uicomponent-c.md)&gt; |
