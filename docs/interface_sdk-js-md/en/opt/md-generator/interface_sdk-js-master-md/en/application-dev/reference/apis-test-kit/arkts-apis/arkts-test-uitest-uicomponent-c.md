# UiComponent

In **UiTest**, the **UiComponent** class represents a component on the UI and provides APIs for obtaining component attributes, clicking a component, scrolling to search for a component, and text injection.All APIs provided in this class use a promise to return the result and must be invoked using **await**.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [Component](arkts-test-uitest-component-c.md)

<!--Device-unnamed-declare class UiComponent--><!--Device-unnamed-declare class UiComponent-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from 'kits/@kit.TestKit';
```

## click

```TypeScript
click(): Promise<void>
```

Clicks this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [Component#click](arkts-test-uitest-component-c.md#click)

<!--Device-UiComponent-click(): Promise<void>--><!--Device-UiComponent-click(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  await button.click();
}
```

## doubleClick

```TypeScript
doubleClick(): Promise<void>
```

Double-clicks this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [Component#doubleClick](arkts-test-uitest-component-c.md#doubleclick)

<!--Device-UiComponent-doubleClick(): Promise<void>--><!--Device-UiComponent-doubleClick(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  await button.doubleClick();
}
```

## getId

```TypeScript
getId(): Promise<number>
```

Obtains the ID of this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [Component#getId](arkts-test-uitest-component-c.md#getid)

<!--Device-UiComponent-getId(): Promise<number>--><!--Device-UiComponent-getId(): Promise<number>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

## Examples

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  let id = await button.getId();
}
```

## getKey

```TypeScript
getKey(): Promise<string>
```

Obtains the key of this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [Component#getId](arkts-test-uitest-component-c.md#getid)

<!--Device-UiComponent-getKey(): Promise<string>--><!--Device-UiComponent-getKey(): Promise<string>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

## Examples

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  let str_key = await button.getKey();
}
```

## getText

```TypeScript
getText(): Promise<string>
```

Obtains the text information of this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [Component#getText](arkts-test-uitest-component-c.md#gettext)

<!--Device-UiComponent-getText(): Promise<string>--><!--Device-UiComponent-getText(): Promise<string>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

## Examples

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  let text = await button.getText();
}
```

## getType

```TypeScript
getType(): Promise<string>
```

Obtains the type of this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [Component#getType](arkts-test-uitest-component-c.md#gettype)

<!--Device-UiComponent-getType(): Promise<string>--><!--Device-UiComponent-getType(): Promise<string>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

## Examples

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  let type = await button.getType();
}
```

## inputText

```TypeScript
inputText(text: string): Promise<void>
```

Inputs text to a component. This API takes effect only for editable text components. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [Component#inputText](arkts-test-uitest-component-c.md#inputtext)(text:

<!--Device-UiComponent-inputText(text: string): Promise<void>--><!--Device-UiComponent-inputText(text: string): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let text: UiComponent = await driver.findComponent(BY.text('hello world'));
  await text.inputText('123');
}
```

## isClickable

```TypeScript
isClickable(): Promise<boolean>
```

Obtains the clickable status of this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [Component#isClickable](arkts-test-uitest-component-c.md#isclickable)

<!--Device-UiComponent-isClickable(): Promise<boolean>--><!--Device-UiComponent-isClickable(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

## Examples

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  if (await button.isClickable()) {
    console.info('This button can be Clicked');
  } else {
    console.info('This button cannot be Clicked');
  }
}
```

## isEnabled

```TypeScript
isEnabled(): Promise<boolean>
```

Obtains the enabled status of this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [Component#isEnabled](arkts-test-uitest-component-c.md#isenabled)

<!--Device-UiComponent-isEnabled(): Promise<boolean>--><!--Device-UiComponent-isEnabled(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

## Examples

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  if (await button.isEnabled()) {
    console.info('This button can be operated');
  } else {
    console.info('This button cannot be operated');
  }
}
```

## isFocused

```TypeScript
isFocused(): Promise<boolean>
```

Obtains the focused status of this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [Component#isFocused](arkts-test-uitest-component-c.md#isfocused)

<!--Device-UiComponent-isFocused(): Promise<boolean>--><!--Device-UiComponent-isFocused(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

## Examples

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  if (await button.isFocused()) {
    console.info('This button is focused');
  } else {
    console.info('This button is not focused');
  }
}
```

## isScrollable

```TypeScript
isScrollable(): Promise<boolean>
```

Obtains the scrollable status of this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [Component#isScrollable](arkts-test-uitest-component-c.md#isscrollable)

<!--Device-UiComponent-isScrollable(): Promise<boolean>--><!--Device-UiComponent-isScrollable(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

## Examples

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let scrollBar: UiComponent = await driver.findComponent(BY.scrollable(true));
  if (await scrollBar.isScrollable()) {
    console.info('This scrollBar can be operated');
  } else {
    console.info('This scrollBar cannot be operated');
  }
}
```

## isSelected

```TypeScript
isSelected(): Promise<boolean>
```

Obtains the selected status of this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [Component#isSelected](arkts-test-uitest-component-c.md#isselected)

<!--Device-UiComponent-isSelected(): Promise<boolean>--><!--Device-UiComponent-isSelected(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

## Examples

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  if (await button.isSelected()) {
    console.info('This button is selected');
  } else {
    console.info('This button is not selected');
  }
}
```

## longClick

```TypeScript
longClick(): Promise<void>
```

Long-clicks this component. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [Component#longClick](arkts-test-uitest-component-c.md#longclick)

<!--Device-UiComponent-longClick(): Promise<void>--><!--Device-UiComponent-longClick(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  await button.longClick();
}
```

## scrollSearch

```TypeScript
scrollSearch(by: By): Promise<UiComponent>
```

Scrolls on this component to search for the target component (applicable to components that support scrolling, such as **List**). This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [Component#scrollSearch](arkts-test-uitest-component-c.md#scrollsearch)(on:

<!--Device-UiComponent-scrollSearch(by: By): Promise<UiComponent>--><!--Device-UiComponent-scrollSearch(by: By): Promise<UiComponent>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| by | [By](arkts-test-uitest-by-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[UiComponent](arkts-test-uitest-uicomponent-c.md)&gt; |

## Examples

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let scrollBar: UiComponent = await driver.findComponent(BY.type('Scroll'));
  let button = await scrollBar.scrollSearch(BY.text('next page'));
}
```
