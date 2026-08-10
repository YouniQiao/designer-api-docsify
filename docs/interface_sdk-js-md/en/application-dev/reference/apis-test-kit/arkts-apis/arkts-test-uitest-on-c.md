# On

UiTest框架从API version 9开始，通过On类提供了丰富的控件特征描述API，用于进行控件筛选来匹配/查找出目标控件。

On提供的API能力具有以下几个特点：

1、支持单属性匹配和多属性组合匹配，例如同时指定目标控件text和id。

2、控件属性支持多种匹配模式。

3、支持控件绝对定位，相对定位，可通过[ON.isBefore](arkts-test-uitest-on-c.md#isbefore)和[ON.isAfter](arkts-test-uitest-on-c.md#isafter)等API限定邻近控件特征进行辅助定位。

On类提供的所有API均为同步接口，建议使用者通过静态构造器ON来链式创建On对象。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class On--><!--Device-unnamed-declare class On-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from 'kits/@kit.TestKit';
```

## afterComponent

```TypeScript
afterComponent(com: Component): On
```

要求目标组件位于由给定{@link Component}指定的另一个组件之后对象，用于相对于组件定位。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-On-afterComponent(com: Component): On--><!--Device-On-afterComponent(com: Component): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| com | [Component](../../apis-arkui/arkts-apis/arkts-arkui-customcomponent-component-i.md) | Yes | 描述了目标组件在的后面。 |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | this { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000007 | Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, On, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let component: Component = await driver.findComponent(ON.type('Text'));
  let on: On = ON.text('123').afterComponent(component); // Search for the component whose text is 123 after the first text component.
}
```

## beforeComponent

```TypeScript
beforeComponent(com: Component): On
```

要求目标组件位于由给定{@link Component}指定的另一个组件之前对象，用于相对于组件定位。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-On-beforeComponent(com: Component): On--><!--Device-On-beforeComponent(com: Component): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| com | [Component](../../apis-arkui/arkts-apis/arkts-arkui-customcomponent-component-i.md) | Yes | 目标组件前面的组件如所示。 |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | this { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000007 | Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, On, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let component: Component = await driver.findComponent(ON.type('Text'));
  let on: On = ON.text('123').beforeComponent(component); // Search for the component whose text is 123 before the first text component.
}
```

## belongingDisplay

ArkTS-Dyn:
```TypeScript
belongingDisplay(displayId: number): On
```

ArkTS-Sta:
```TypeScript
belongingDisplay(displayId: int): On
```

获取指定屏幕内的控件对象，返回On对象自身。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-On-belongingDisplay(displayId: int): On--><!--Device-On-belongingDisplay(displayId: int): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定控件所属屏幕ID，取值范围：大于等于0的整数。 **说明：** 传入displayId不存在时，将抛出17000007异常。可通过 [getAllDisplays](../../apis-arkui/arkts-apis/arkts-arkui-display-getalldisplays-f.md/arkts-arkui-display-getalldisplays-f.md#getalldisplays)获取当前所有的 display对象，并由display对象获取对应的屏幕ID。&lt;!--RP2--&gt;&lt;!--RP2End--&gt; |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | 返回指定控件所属屏幕的On对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000007 | Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.belongingDisplay(0); // Use the static constructor ON to create an On object and specify the ID of the display to which the target component belongs.
```

## checkable

```TypeScript
checkable(b?: boolean): On
```

指定目标控件能否被勾选状态属性，返回On对象自身。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-On-checkable(b?: boolean): On--><!--Device-On-checkable(b?: boolean): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| b | boolean | No | 指定控件能否被勾选状态。true：能被勾选。false：不能被勾选。默认为true。&lt;!--RP2--&gt;&lt;!--RP2End--&gt;<br>**Since:** 10 |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | 返回指定目标控件能否被勾选状态属性的On对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.checkable(true); // Use the static constructor ON to create an On object and specify the checkable attribute of the target component.
```

## checked

```TypeScript
checked(b?: boolean): On
```

指定目标控件的被勾选状态属性，返回On对象自身。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-On-checked(b?: boolean): On--><!--Device-On-checked(b?: boolean): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| b | boolean | No | 指定控件被勾选状态。true：被勾选。false：未被勾选。默认为true。&lt;!--RP2--&gt;&lt;!--RP2End--&gt;<br>**Since:** 10 |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | 返回指定目标控件的被勾选状态属性的On对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.checked(true); // Use the static constructor ON to create an On object and specify the checked attribute of the target component.
```

## clickable

```TypeScript
clickable(b?: boolean): On
```

指定目标控件的可点击状态属性，返回On对象自身。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-On-clickable(b?: boolean): On--><!--Device-On-clickable(b?: boolean): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| b | boolean | No | 指定控件可点击状态。true：可点击。false：不可点击。默认为true。&lt;!--RP2--&gt;&lt;!--RP2End--&gt;<br>**Since:** 10 |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | 返回指定目标控件的可点击状态属性的On对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.clickable(true); // Use the static constructor ON to create an On object and specify the clickable attribute of the target component.
```

## description

```TypeScript
description(val: string, pattern?: MatchPattern): On
```

指定目标控件的描述属性，支持多种匹配模式，返回On对象自身。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-On-description(val: string, pattern?: MatchPattern): On--><!--Device-On-description(val: string, pattern?: MatchPattern): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | string | Yes | 控件的描述属性。 &lt;!--RP2--&gt;&lt;!--RP2End--&gt; |
| pattern | [MatchPattern](arkts-test-uitest-matchpattern-e.md) | No | 指定的文本匹配模式，默认为[EQUALS](arkts-test-uitest-matchpattern-e.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | 返回指定目标控件description属性的On对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.description('123'); // Use the static constructor ON to create an On object and specify the description attribute of the target component.
```

## enabled

```TypeScript
enabled(b?: boolean): On
```

指定目标控件的使能状态属性，返回On对象自身。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-On-enabled(b?: boolean): On--><!--Device-On-enabled(b?: boolean): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| b | boolean | No | 指定控件使能状态。true：使能。false：未使能。默认为true。&lt;!--RP2--&gt;&lt;!--RP2End--&gt;<br>**Since:** 10 |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | 返回指定目标控件的使能状态属性的On对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.enabled(true); // Use the static constructor ON to create an On object and specify the enabled attribute of the target component.
```

## focused

```TypeScript
focused(b?: boolean): On
```

指定目标控件的获焦状态属性，返回On对象自身。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-On-focused(b?: boolean): On--><!--Device-On-focused(b?: boolean): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| b | boolean | No | 控件获焦状态。true：获焦。false：未获焦。默认为true。&lt;!--RP2--&gt;&lt;!--RP2End--&gt;<br>**Since:** 10 |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | 返回指定目标控件的获焦状态属性的On对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.focused(true); // Use the static constructor ON to create an On object and specify the focused attribute of the target component.
```

## hint

```TypeScript
hint(val: string, pattern?: MatchPattern): On
```

获取指定提示文本的控件对象，返回On对象自身。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-On-hint(val: string, pattern?: MatchPattern): On--><!--Device-On-hint(val: string, pattern?: MatchPattern): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | string | Yes | 指定控件提示文本。 &lt;!--RP2--&gt;&lt;!--RP2End--&gt; |
| pattern | [MatchPattern](arkts-test-uitest-matchpattern-e.md) | No | 指定的文本匹配模式，默认为[EQUALS](arkts-test-uitest-matchpattern-e.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | 返回指定提示文本控件的On对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { MatchPattern, On, ON } from '@kit.TestKit';

let on: On = ON.hint('welcome', MatchPattern.EQUALS); // Use the static constructor ON to create an On object with the hint text attribute of the target component specified.
```

## id

```TypeScript
id(id: string): On
```

指定目标控件id属性，返回On对象自身。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-On-id(id: string): On--><!--Device-On-id(id: string): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | 指定控件的id值。&lt;!--RP2--&gt;&lt;!--RP2End--&gt; |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | 返回指定目标控件id属性的On对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.id('123'); // Use the static constructor ON to create an On object and specify the ID attribute of the target component.
```

## id

```TypeScript
id(id: string, pattern: MatchPattern): On
```

指定目标控件id属性和匹配模式，返回On对象自身。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-On-id(id: string, pattern: MatchPattern): On--><!--Device-On-id(id: string, pattern: MatchPattern): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | 指定控件的id值。&lt;!--RP2--&gt;&lt;!--RP2End--&gt; |
| pattern | [MatchPattern](arkts-test-uitest-matchpattern-e.md) | Yes | 指定的文本匹配模式。 |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | 返回指定目标控件id属性的On对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { MatchPattern, On, ON } from '@kit.TestKit';

let on: On = ON.id('id', MatchPattern.REG_EXP_ICASE); // Use case-insensitive regular expression to match the ID attribute value of the component.
```

## inWindow

```TypeScript
inWindow(bundleName: string): On
```

指定目标控件位于给出的应用窗口内，返回On对象自身。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-On-inWindow(bundleName: string): On--><!--Device-On-inWindow(bundleName: string): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 应用窗口的包名。&lt;!--RP2--&gt;&lt;!--RP2End--&gt; |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | 返回指定目标控件位于给出的应用窗口内的On对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.inWindow('com.uitestScene.acts'); // Use the static constructor ON to create an On object and specify that the target component is located within the given application window.
```

## isAfter

```TypeScript
isAfter(on: On): On
```

指定目标控件位于给出的特征属性控件之后，返回On对象自身。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-On-isAfter(on: On): On--><!--Device-On-isAfter(on: On): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | 特征控件的属性要求。 &lt;!--RP3--&gt;&lt;!--RP3End--&gt; |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | 返回指定目标控件位于给出的特征属性控件之后的On对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

// Use the static constructor ON to create an On object and specify that the target component is located after the given attribute component.
let on: On = ON.type('Text').isAfter(ON.text('123')); // Search for the first Text component located after the component whose text is 123.
```

## isBefore

```TypeScript
isBefore(on: On): On
```

指定目标控件位于给出的特征属性控件之前，返回On对象自身。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-On-isBefore(on: On): On--><!--Device-On-isBefore(on: On): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | 特征控件的属性要求。 &lt;!--RP3--&gt;&lt;!--RP3End--&gt; |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | 返回指定目标控件位于给出的特征属性控件之前的On对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

// Use the static constructor ON to create an On object and specify that the target component is located before the given attribute component.
let on: On = ON.type('Button').isBefore(ON.text('123')); // Search for the first Button component located before the component whose text is 123.
```

## longClickable

```TypeScript
longClickable(b?: boolean): On
```

指定目标控件的可长按点击状态属性，返回On对象自身。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-On-longClickable(b?: boolean): On--><!--Device-On-longClickable(b?: boolean): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| b | boolean | No | 指定控件可长按点击状态。true：可长按点击。false：不可长按点击。默认为true。&lt;!--RP2--&gt;&lt;!--RP2End--&gt;<br>**Since:** 10 |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | 返回指定目标控件的可长按点击状态属性的On对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.longClickable(true); // Use the static constructor ON to create an On object and specify the longClickable attribute of the target component.
```

## originalText

```TypeScript
originalText(text: string, pattern?: MatchPattern): On
```

指定控件的文本内容和文本匹配模式，返回On对象自身。

> **说明：**
> 
> 如果控件的无障碍属性
> [accessibilityLevel](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-accessibility.md#accessibilitylevel)
> 设置为'no'或'no-hide-descendants'，可以使用本接口指定目标控件的文本属性用于查找控件，使用[On.text()](arkts-test-uitest-on-c.md#text)接口不生效。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-On-originalText(text: string, pattern?: MatchPattern): On--><!--Device-On-originalText(text: string, pattern?: MatchPattern): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 指定控件文本，用于匹配目标控件文本。 &lt;!--RP2--&gt;&lt;!--RP2End--&gt; |
| pattern | [MatchPattern](arkts-test-uitest-matchpattern-e.md) | No | 指定的文本匹配模式，默认为[EQUALS](arkts-test-uitest-matchpattern-e.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | 返回指定目标控件文本属性的On对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000007 | Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.originalText('123'); // Use the static constructor ON to create an On object and specify the originalText attribute of the target component.
```

## scrollable

```TypeScript
scrollable(b?: boolean): On
```

指定目标控件的可滑动状态属性，返回On对象自身。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-On-scrollable(b?: boolean): On--><!--Device-On-scrollable(b?: boolean): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| b | boolean | No | 控件可滑动状态。true：可滑动。false：不可滑动。默认为true。&lt;!--RP2--&gt;&lt;!--RP2End--&gt;<br>**Since:** 10 |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | 返回指定目标控件的可滑动状态属性的On对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.scrollable(true); // Use the static constructor ON to create an On object and specify the scrollable attribute of the target component.
```

## selected

```TypeScript
selected(b?: boolean): On
```

指定目标控件的被选中状态属性，返回On对象自身。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-On-selected(b?: boolean): On--><!--Device-On-selected(b?: boolean): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| b | boolean | No | 指定控件被选中状态。true：被选中。false：未被选中。默认为true。&lt;!--RP2--&gt;&lt;!--RP2End--&gt;<br>**Since:** 10 |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | 返回指定目标控件的被选中状态属性的On对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.selected(true); // Use the static constructor ON to create an On object and specify the selected attribute of the target component.
```

## text

```TypeScript
text(txt: string, pattern?: MatchPattern): On
```

指定目标控件文本属性，支持多种匹配模式，返回On对象自身。

> **说明：**
> 
> 如果控件的无障碍属性
> [accessibilityLevel](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-accessibility.md#accessibilitylevel)
> 设置为'no'或'no-hide-descendants'，无法使用本接口指定目标控件的文本属性用于查找控件，可以使用[On.originalText()](arkts-test-uitest-on-c.md#originaltext)接口实现。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-On-text(txt: string, pattern?: MatchPattern): On--><!--Device-On-text(txt: string, pattern?: MatchPattern): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| txt | string | Yes | 指定控件文本，用于匹配目标控件文本。&lt;!--RP2--&gt;&lt;!--RP2End--&gt; |
| pattern | [MatchPattern](arkts-test-uitest-matchpattern-e.md) | No | 指定的文本匹配模式，默认为[EQUALS](arkts-test-uitest-matchpattern-e.md)。<br>**Since:** 10 |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | 返回指定目标控件文本属性的On对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.text('123'); // Use the static constructor ON to create an On object and specify the text attribute of the target component.
```

## type

```TypeScript
type(tp: string): On
```

指定目标控件的控件类型属性，返回On对象自身。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-On-type(tp: string): On--><!--Device-On-type(tp: string): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tp | string | Yes | 指定控件类型。&lt;!--RP2--&gt;&lt;!--RP2End--&gt; |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | 返回指定目标控件的控件类型属性的On对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.type('Button'); // Use the static constructor ON to create an On object and specify the type attribute of the target component.
```

## type

```TypeScript
type(tp: string, pattern: MatchPattern): On
```

指定目标控件的控件类型属性和匹配模式，返回On对象自身。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-On-type(tp: string, pattern: MatchPattern): On--><!--Device-On-type(tp: string, pattern: MatchPattern): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tp | string | Yes | 指定控件类型。&lt;!--RP2--&gt;&lt;!--RP2End--&gt; |
| pattern | [MatchPattern](arkts-test-uitest-matchpattern-e.md) | Yes | 指定的文本匹配模式。 |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | 返回指定目标控件的控件类型属性的On对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { On, ON, MatchPattern } from '@kit.TestKit';

let on: On = ON.type('Button', MatchPattern.EQUALS); // Use the static constructor ON to create an On object and specify the type attribute of the target component.
```

## within

```TypeScript
within(on: On): On
```

指定目标控件位于给出的特征属性控件之内，返回On对象自身。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-On-within(on: On): On--><!--Device-On-within(on: On): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | 特征控件的属性要求。&lt;!--RP3--&gt;&lt;!--RP3End--&gt; |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | 返回指定目标控件位于给出的特征属性控件内的On对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

// Use the static constructor ON to create an On object and specify that the target component is located within the given attribute component.
let on: On = ON.text('java').within(ON.type('Scroll')); // Search for the child component whose text is java within the Scroller component.
```

## withinComponent

```TypeScript
withinComponent(com: Component): On
```

要求目标组件位于由给定{@link Component}指定的另一个组件的内部对象，用于相对于组件定位。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-On-withinComponent(com: Component): On--><!--Device-On-withinComponent(com: Component): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| com | [Component](../../apis-arkui/arkts-apis/arkts-arkui-customcomponent-component-i.md) | Yes | 描述目标组件所在的组件。 |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | this { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000007 | Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, On, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let component: Component = await driver.findComponent(ON.type('Text'));
  let on: On = ON.text('123').withinComponent(component); // Search for the component whose text is 123 within the first text component.
}
```

