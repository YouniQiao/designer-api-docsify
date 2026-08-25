# By

UiTest框架通过By类提供了丰富的控件特征描述API，用于进行控件筛选来匹配/查找出目标控件。By提供的API能力具有以下几个特点：1、支持单属性匹配和多属性组合匹配，例如同时指定目标控件text和id。2、控件属性支持多种匹配模式。3、支持控件绝对定位，相对定位，可通过[By.isBefore&lt;sup&gt;(deprecated)&lt;/sup&gt;](#isbefore)和 [By.isAfter&lt;sup&gt;(deprecated)&lt;/sup&gt;](#isafter)等API限定邻近控件特征进行辅助定位。By类提供的所有API均为同步接口，建议使用者通过静态构造器BY来链式创建By对象。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[On&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-on-c.md)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [On](arkts-test-uitest-on-c.md)

**系统能力：** SystemCapability.Test.UiTest

## 导入模块

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from 'kits/@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from 'kits/@kit.TestKit';
```

## clickable

```TypeScript
clickable(b?: boolean): By
```

指定目标控件的可点击状态属性，返回By对象自身。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[clickable&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-on-c.md#clickable)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [clickable](arkts-test-uitest-on-c.md#clickable)

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| b | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## enabled

```TypeScript
enabled(b?: boolean): By
```

指定目标控件的使能状态属性，返回By对象自身。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[enabled&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-on-c.md#enabled)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [enabled](arkts-test-uitest-on-c.md#enabled)

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| b | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## focused

```TypeScript
focused(b?: boolean): By
```

指定目标控件的获焦状态属性，返回By对象自身。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[focused&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-on-c.md#focused)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [focused](arkts-test-uitest-on-c.md#focused)

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| b | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## id

```TypeScript
id(id: number): By
```

指定目标控件id属性，返回By对象自身。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[id&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-on-c.md#id)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [id](arkts-test-uitest-on-c.md#id)(id: string)

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [id](#id) | number | 是 |

**返回值：**

| 类型 |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## isAfter

```TypeScript
isAfter(by: By): By
```

指定目标控件位于给出的特征属性控件之后，返回By对象自身。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[isAfter&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-on-c.md#isafter)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isAfter](arkts-test-uitest-on-c.md#isafter)(on: On)

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| by | [By](arkts-test-uitest-by-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## isBefore

```TypeScript
isBefore(by: By): By
```

指定目标控件位于给出的特征属性控件之前，返回By对象自身。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[isBefore&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-on-c.md#isbefore)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isBefore](arkts-test-uitest-on-c.md#isbefore)(on: On)

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| by | [By](arkts-test-uitest-by-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## key

```TypeScript
key(key: string): By
```

指定目标控件key值属性，返回By对象自身。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[id&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-on-c.md#id)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [id](arkts-test-uitest-on-c.md#id)(id: string)

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [key](#key) | string | 是 |

**返回值：**

| 类型 |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## scrollable

```TypeScript
scrollable(b?: boolean): By
```

指定目标控件的可滑动状态属性，返回By对象自身。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[scrollable&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-on-c.md#scrollable)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [scrollable](arkts-test-uitest-on-c.md#scrollable)

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| b | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## selected

```TypeScript
selected(b?: boolean): By
```

指定目标控件的被选中状态属性，返回By对象自身。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[selected&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-on-c.md#selected)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [selected](arkts-test-uitest-on-c.md#selected)

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| b | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## text

```TypeScript
text(txt: string, pattern?: MatchPattern): By
```

指定目标控件文本属性，支持多种匹配模式，返回By对象自身。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[text&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-on-c.md#text)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [text](arkts-test-uitest-on-c.md#text)

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| txt | string | 是 |
| [pattern](../../apis-sensor-service-kit/arkts-apis/arkts-sensorservice-vibrator-vibratefrompattern-i.md) | [MatchPattern](arkts-test-uitest-matchpattern-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## type

```TypeScript
type(tp: string): By
```

指定目标控件的控件类型属性，返回By对象自身。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用[type&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-on-c.md#type)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [type](arkts-test-uitest-on-c.md#type)(tp: string)

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tp | string | 是 |

**返回值：**

| 类型 |
| --- |
| [By](arkts-test-uitest-by-c.md) |
