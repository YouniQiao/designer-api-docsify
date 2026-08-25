# By

The UiTest framework provides a wide range of UI component feature description APIs in the **By** class to filter and match components.The APIs provided by the **By** class exhibit the following features:
1. Allow one or more attributes as the match conditions.
For example, you can specify both the **text** and **id** attributes to find the target component.
2. Provide multiple match patterns for component attributes.
3. Support absolute positioning and relative positioning for components.
APIs such as [By.isBefore&lt;sup&gt;(deprecated)&lt;/sup&gt;](#isbefore) and [By.isAfter&lt;sup&gt;(deprecated)&lt;/sup&gt;](#isafter) can be used to specify the features of adjacent components to assist positioning.All APIs provided in the **By** class are synchronous. You are advised to use the static constructor **BY** to create a **By** object in chain mode.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [On](arkts-test-uitest-on-c.md)

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from 'kits/@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from 'kits/@kit.TestKit';
```

## clickable

```TypeScript
clickable(b?: boolean): By
```

Specifies the clickable attribute of the target component.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [clickable](arkts-test-uitest-on-c.md#clickable)

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| b | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## enabled

```TypeScript
enabled(b?: boolean): By
```

Specifies the enabled attribute of the target component.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [enabled](arkts-test-uitest-on-c.md#enabled)

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| b | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## focused

```TypeScript
focused(b?: boolean): By
```

Specifies the focused attribute of the target component.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [focused](arkts-test-uitest-on-c.md#focused)

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| b | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## id

```TypeScript
id(id: number): By
```

Specifies the ID attribute of the target component.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [id](arkts-test-uitest-on-c.md#id)(id: string)

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [id](#id) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## isAfter

```TypeScript
isAfter(by: By): By
```

Specifies that the target component is located after the given attribute component.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isAfter](arkts-test-uitest-on-c.md#isafter)(on: On)

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| by | [By](arkts-test-uitest-by-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## isBefore

```TypeScript
isBefore(by: By): By
```

Specifies that the target component is located before the given attribute component.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isBefore](arkts-test-uitest-on-c.md#isbefore)(on: On)

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| by | [By](arkts-test-uitest-by-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## key

```TypeScript
key(key: string): By
```

Specifies the key attribute of the target component.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [id](arkts-test-uitest-on-c.md#id)(id: string)

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [key](#key) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## scrollable

```TypeScript
scrollable(b?: boolean): By
```

Specifies the scrollable attribute of the target component.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [scrollable](arkts-test-uitest-on-c.md#scrollable)

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| b | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## selected

```TypeScript
selected(b?: boolean): By
```

Specifies the selected status of the target component.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [selected](arkts-test-uitest-on-c.md#selected)

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| b | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## text

```TypeScript
text(txt: string, pattern?: MatchPattern): By
```

Specifies the text attribute of the target component. Multiple match patterns are supported.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [text](arkts-test-uitest-on-c.md#text)

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| txt | string | Yes |
| [pattern](../../apis-sensor-service-kit/arkts-apis/arkts-sensorservice-vibrator-vibratefrompattern-i.md) | [MatchPattern](arkts-test-uitest-matchpattern-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## type

```TypeScript
type(tp: string): By
```

Specifies the type attribute of the target component.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [type](arkts-test-uitest-on-c.md#type)(tp: string)

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tp | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [By](arkts-test-uitest-by-c.md) |
