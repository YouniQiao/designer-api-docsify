# UiComponent

UiTest中，UiComponent类代表了UI界面上的一个控件，提供控件属性获取，控件点击，滑动查找，文本注入等API。该类提供的所有方法都使用Promise方式作为异步方法，需使用await调用。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[Component&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

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

控件对象进行点击操作。使用Promise异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[click&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#click)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [Component#click](arkts-test-uitest-component-c.md#click)

<!--Device-UiComponent-click(): Promise<void>--><!--Device-UiComponent-click(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

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

控件对象进行双击操作。使用Promise异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[doubleClick&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#doubleclick)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [Component#doubleClick](arkts-test-uitest-component-c.md#doubleclick)

<!--Device-UiComponent-doubleClick(): Promise<void>--><!--Device-UiComponent-doubleClick(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

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

获取控件对象的id值。使用Promise异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[getId&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#getid)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [Component#getId](arkts-test-uitest-component-c.md#getid)

<!--Device-UiComponent-getId(): Promise<number>--><!--Device-UiComponent-getId(): Promise<number>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回控件的id值。 |

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

获取控件对象的key值。使用Promise异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[getId&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#getid)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [Component#getId](arkts-test-uitest-component-c.md#getid)

<!--Device-UiComponent-getKey(): Promise<string>--><!--Device-UiComponent-getKey(): Promise<string>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回控件的key值。 |

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

获取控件对象的文本信息。使用Promise异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[getText&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#gettext)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [Component#getText](arkts-test-uitest-component-c.md#gettext)

<!--Device-UiComponent-getText(): Promise<string>--><!--Device-UiComponent-getText(): Promise<string>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回控件的文本信息。 |

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

获取控件对象的控件类型。使用Promise异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[getType&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#gettype)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [Component#getType](arkts-test-uitest-component-c.md#gettype)

<!--Device-UiComponent-getType(): Promise<string>--><!--Device-UiComponent-getType(): Promise<string>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回控件的类型。 |

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

向控件中输入文本，仅针对可编辑的文本组件生效。使用Promise异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[inputText&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#inputtext)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [Component#inputText](arkts-test-uitest-component-c.md#inputtext)(text:

<!--Device-UiComponent-inputText(text: string): Promise<void>--><!--Device-UiComponent-inputText(text: string): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 输入的文本信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

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

获取控件对象可点击状态。使用Promise异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[isClickable&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#isclickable)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [Component#isClickable](arkts-test-uitest-component-c.md#isclickable)

<!--Device-UiComponent-isClickable(): Promise<boolean>--><!--Device-UiComponent-isClickable(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回控件对象可点击状态。true：可点击。false：不可点击。 |

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

获取控件使能状态。使用Promise异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[isEnabled&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#isenabled)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [Component#isEnabled](arkts-test-uitest-component-c.md#isenabled)

<!--Device-UiComponent-isEnabled(): Promise<boolean>--><!--Device-UiComponent-isEnabled(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回控件使能状态。true：使能。false：未使能。 |

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

判断控件对象是否获焦。使用Promise异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[isFocused&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#isfocused)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [Component#isFocused](arkts-test-uitest-component-c.md#isfocused)

<!--Device-UiComponent-isFocused(): Promise<boolean>--><!--Device-UiComponent-isFocused(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回控件对象是否获焦。true：获焦。false：未获焦。 |

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

获取控件对象可滑动状态。使用Promise异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[isScrollable&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#isscrollable)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [Component#isScrollable](arkts-test-uitest-component-c.md#isscrollable)

<!--Device-UiComponent-isScrollable(): Promise<boolean>--><!--Device-UiComponent-isScrollable(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回控件对象可滑动状态。true：可滑动。false：不可滑动。 |

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

获取控件对象被选中状态。使用Promise异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[isSelected&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#isselected)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [Component#isSelected](arkts-test-uitest-component-c.md#isselected)

<!--Device-UiComponent-isSelected(): Promise<boolean>--><!--Device-UiComponent-isSelected(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回控件对象被选中的状态。true：被选中。false：未被选中。 |

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

控件对象进行长按操作。使用Promise异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[longClick&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#longclick)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [Component#longClick](arkts-test-uitest-component-c.md#longclick)

<!--Device-UiComponent-longClick(): Promise<void>--><!--Device-UiComponent-longClick(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

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

在控件上滑动查找目标控件（适用于List等支持滑动的控件）。使用Promise异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[scrollSearch&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#scrollsearch)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [Component#scrollSearch](arkts-test-uitest-component-c.md#scrollsearch)(on:

<!--Device-UiComponent-scrollSearch(by: By): Promise<UiComponent>--><!--Device-UiComponent-scrollSearch(by: By): Promise<UiComponent>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| by | [By](arkts-test-uitest-by-c.md) | Yes | 目标控件的属性要求。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[UiComponent](arkts-test-uitest-uicomponent-c.md)&gt; | Promise对象，返回目标控件对象。 |

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

