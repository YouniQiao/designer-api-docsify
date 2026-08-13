# By

The UiTest framework provides a wide range of UI component feature description APIs in the **By** class to filter and match components. The APIs provided by the **By** class exhibit the following features: 1. Allow one or more attributes as the match conditions. For example, you can specify both the **text** and **id** attributes to find the target component. 2. Provide multiple match patterns for component attributes. 3. Support absolute positioning and relative positioning for components. APIs such as [By.isBefore&lt;sup&gt;(deprecated)&lt;/sup&gt;](#isBefore) and [By.isAfter&lt;sup&gt;(deprecated)&lt;/sup&gt;](#isAfter) can be used to specify the features of adjacent components to assist positioning. All APIs provided in the **By** class are synchronous. You are advised to use the static constructor **BY** to create a **By** object in chain mode.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [On](arkts-test-uitest-on-c.md#On)

<!--Device-unnamed-declare class By--><!--Device-unnamed-declare class By-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from '@kit.TestKit';
```

## clickable

```TypeScript
clickable(b?: boolean): By
```

Specifies the clickable attribute of the target component.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [clickable](arkts-test-uitest-on-c.md#clickable)

<!--Device-By-clickable(b?: boolean): By--><!--Device-By-clickable(b?: boolean): By-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| b | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## Examples

```TypeScript
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.clickable(true); // Use the static constructor BY to create a By object and specify the clickable attribute of the target component.
```

## enabled

```TypeScript
enabled(b?: boolean): By
```

Specifies the enabled attribute of the target component.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [enabled](arkts-test-uitest-on-c.md#enabled)

<!--Device-By-enabled(b?: boolean): By--><!--Device-By-enabled(b?: boolean): By-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| b | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## Examples

```TypeScript
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.enabled(true); // Use the static constructor BY to create a By object and specify the enabled attribute of the target component.
```

## focused

```TypeScript
focused(b?: boolean): By
```

Specifies the focused attribute of the target component.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [focused](arkts-test-uitest-on-c.md#focused)

<!--Device-By-focused(b?: boolean): By--><!--Device-By-focused(b?: boolean): By-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| b | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## Examples

```TypeScript
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.focused(true); // Use the static constructor BY to create a By object and specify the focused attribute of the target component.
```

## id

```TypeScript
id(id: number): By
```

Specifies the ID attribute of the target component.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [id](arkts-test-uitest-on-c.md#id)(id: string)

<!--Device-By-id(id: number): By--><!--Device-By-id(id: number): By-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [id](#id) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## Examples

```TypeScript
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.id(123); // Use the static constructor BY to create a By object and specify the id attribute of the target component.
```

## isAfter

```TypeScript
isAfter(by: By): By
```

Specifies that the target component is located after the given attribute component.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isAfter](arkts-test-uitest-on-c.md#isAfter)(on: On)

<!--Device-By-isAfter(by: By): By--><!--Device-By-isAfter(by: By): By-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| by | [By](arkts-test-uitest-by-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## Examples

```TypeScript
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

// Use the static constructor BY to create a by object and specify that the target component is located before the given attribute component.
let by: By = BY.type('Text').isAfter(BY.text('123')); // Search for the first Text component located after the component whose text is 123.
```

## isBefore

```TypeScript
isBefore(by: By): By
```

Specifies that the target component is located before the given attribute component.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isBefore](arkts-test-uitest-on-c.md#isBefore)(on: On)

<!--Device-By-isBefore(by: By): By--><!--Device-By-isBefore(by: By): By-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| by | [By](arkts-test-uitest-by-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## Examples

```TypeScript
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

// Use the static constructor BY to create a by object and specify that the target component is located before the given attribute component.
let by: By = BY.type('Button').isBefore(BY.text('123')); // Search for the first Button component located before the component whose text is 123.
```

## key

```TypeScript
key(key: string): By
```

Specifies the key attribute of the target component.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [id](arkts-test-uitest-on-c.md#id)(id: string)

<!--Device-By-key(key: string): By--><!--Device-By-key(key: string): By-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [key](#key) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## Examples

```TypeScript
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.key('123'); // Use the static constructor BY to create a By object and specify the key attribute of the target component.
```

## scrollable

```TypeScript
scrollable(b?: boolean): By
```

Specifies the scrollable attribute of the target component.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [scrollable](arkts-test-uitest-on-c.md#scrollable)

<!--Device-By-scrollable(b?: boolean): By--><!--Device-By-scrollable(b?: boolean): By-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| b | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## Examples

```TypeScript
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.scrollable(true); // Use the static constructor BY to create a By object and specify the scrollable attribute of the target component.
```

## selected

```TypeScript
selected(b?: boolean): By
```

Specifies the selected status of the target component.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [selected](arkts-test-uitest-on-c.md#selected)

<!--Device-By-selected(b?: boolean): By--><!--Device-By-selected(b?: boolean): By-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| b | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## Examples

```TypeScript
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.selected(true); // Use the static constructor BY to create a By object and specify the selected attribute of the target component.
```

## text

```TypeScript
text(txt: string, pattern?: MatchPattern): By
```

Specifies the text attribute of the target component. Multiple match patterns are supported.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [text](arkts-test-uitest-on-c.md#text)

<!--Device-By-text(txt: string, pattern?: MatchPattern): By--><!--Device-By-text(txt: string, pattern?: MatchPattern): By-End-->

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

## Examples

```TypeScript
// xxx.test.ets
import { BY, By } from '@kit.TestKit';

let by: By = BY.text('123'); // Use the static constructor BY to create a By object and specify the text attribute of the target component.
```

## type

```TypeScript
type(tp: string): By
```

Specifies the type attribute of the target component.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [type](arkts-test-uitest-on-c.md#type)(tp: string)

<!--Device-By-type(tp: string): By--><!--Device-By-type(tp: string): By-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tp | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [By](arkts-test-uitest-by-c.md) |

## Examples

```TypeScript
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.type('Button'); // Use the static constructor BY to create a By object and specify the type attribute of the target component.
```
