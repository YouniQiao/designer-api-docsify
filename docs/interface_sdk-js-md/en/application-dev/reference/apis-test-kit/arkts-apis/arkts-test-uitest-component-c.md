# Component

UiTest框架在API9中，Component类代表了UI界面上的一个控件，提供控件属性获取，控件点击，滑动查找，文本注入等API。该类对象可通过{@link Driver#findComponent}、{@link Driver#findComponents}、{@link Driver#waitForComponent}等接口获取。该类提供的所有方法都使用Promise方式作为异步方法，需使用await调用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class Component--><!--Device-unnamed-declare class Component-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from 'kits/@kit.TestKit';
```

## clearText

```TypeScript
clearText(): Promise<void>
```

清除控件的文本信息，仅针对可编辑的文本组件生效。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-clearText(): Promise<void>--><!--Device-Component-clearText(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.text('hello world'));
  await text.clearText();
}
```

## click

```TypeScript
click(): Promise<void>
```

控件对象进行点击操作。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-click(): Promise<void>--><!--Device-Component-click(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, ON, Component } from '@kit.TestKit';

async function demo() {
  // Create a Driver object.
  let driver: Driver = Driver.create();
  // Search for the Button component.
  let button: Component = await driver.findComponent(ON.type('Button'));
  // Tap the component.
  await button.click();
}
```

## doubleClick

```TypeScript
doubleClick(): Promise<void>
```

控件对象进行双击操作。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-doubleClick(): Promise<void>--><!--Device-Component-doubleClick(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  await button.doubleClick();
}
```

## dragTo

```TypeScript
dragTo(target: Component): Promise<void>
```

将控件拖拽至目标控件处。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-dragTo(target: Component): Promise<void>--><!--Device-Component-dragTo(target: Component): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | [Component](../../apis-arkui/arkts-apis/arkts-arkui-customcomponent-component-i.md) | Yes | 目标控件。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  // Create a Driver object.
  let driver: Driver = Driver.create();
  // Search for the target Button component.
  let button: Component = await driver.findComponent(ON.type('Button'));
  // Search for the component whose text is 'hello world' as the drag target.
  let text: Component = await driver.findComponent(ON.text('hello world'));
  // Drag the Button component to the Text component.
  await button.dragTo(text);
}
```

## getBounds

```TypeScript
getBounds(): Promise<Rect>
```

获取控件对象的边框信息。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-getBounds(): Promise<Rect>--><!--Device-Component-getBounds(): Promise<Rect>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Rect&gt; | Promise对象，返回控件对象的边框信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let rect = await button.getBounds();
}
```

## getBoundsCenter

```TypeScript
getBoundsCenter(): Promise<Point>
```

获取控件对象所占区域的中心点信息。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-getBoundsCenter(): Promise<Point>--><!--Device-Component-getBoundsCenter(): Promise<Point>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Point&gt; | Promise对象，返回控件对象所占区域的中心点信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let point = await button.getBoundsCenter();
}
```

## getDescription

```TypeScript
getDescription(): Promise<string>
```

获取控件对象的描述信息。使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-getDescription(): Promise<string>--><!--Device-Component-getDescription(): Promise<string>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回控件的描述信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let description = await button.getDescription();
}
```

## getDisplayId

ArkTS-Dyn:
```TypeScript
getDisplayId(): Promise<number>
```

ArkTS-Sta:
```TypeScript
getDisplayId(): Promise<int>
```

获取控件对象所属的屏幕ID。使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Component-getDisplayId(): Promise<int>--><!--Device-Component-getDisplayId(): Promise<int>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象，返回控件所属的屏幕ID。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('TextInput'));
  let displayId = await button.getDisplayId();
}
```

## getHint

```TypeScript
getHint(): Promise<string>
```

获取控件对象的提示文本。使用Promise异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Component-getHint(): Promise<string>--><!--Device-Component-getHint(): Promise<string>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回控件的提示文本。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('TextInput'));
  let hints = await button.getHint();
}
```

## getId

```TypeScript
getId(): Promise<string>
```

获取控件对象的id值。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-getId(): Promise<string>--><!--Device-Component-getId(): Promise<string>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回控件的id值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let id = await button.getId();
}
```

## getOriginalText

```TypeScript
getOriginalText(): Promise<string>
```

获取控件对象的文本信息。使用Promise异步回调。如果控件的无障碍属性  
[accessibilityLevel](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-accessibility.md#accessibilitylevel)设置为'no'或'no-hide-descendants'，可以使用本接口获取控件的文本信息，无法使用[Component.getText()](arkts-test-uitest-component-c.md#gettext)获取控件的文本信息。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Component-getOriginalText(): Promise<string>--><!--Device-Component-getOriginalText(): Promise<string>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回控件的文本信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let text = await button.getOriginalText();
}
```

## getText

```TypeScript
getText(): Promise<string>
```

获取控件对象的文本信息。使用Promise异步回调。

> **说明：**
> 
> 如果控件的无障碍属性
> [accessibilityLevel](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-accessibility.md#accessibilitylevel)
> 设置为'no'或'no-hide-descendants'，无法使用本接口获取控件的文本信息，可以使用[Component.getOriginalText()](arkts-test-uitest-component-c.md#getoriginaltext)
> 获取控件的文本信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-getText(): Promise<string>--><!--Device-Component-getText(): Promise<string>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回控件的文本信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let text = await button.getText();
}
```

## getType

```TypeScript
getType(): Promise<string>
```

获取控件对象的控件类型。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-getType(): Promise<string>--><!--Device-Component-getType(): Promise<string>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回控件的类型。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let type = await button.getType();
}
```

## inputText

```TypeScript
inputText(text: string): Promise<void>
```

清空组件内原有文本并输入指定文本内容，仅针对可编辑的文本组件生效。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-inputText(text: string): Promise<void>--><!--Device-Component-inputText(text: string): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 输入的文本信息，当前支持英文、中文和特殊字符。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  // Create a Driver object.
  let driver: Driver = Driver.create();
  // Search for the component whose text is 'hello world'.
  let text: Component = await driver.findComponent(ON.text('hello world'));
  // Clear the original text and enter '123'.
  await text.inputText('123');
}
```

## inputText

```TypeScript
inputText(text: string, mode: InputTextMode): Promise<void>
```

向控件中输入文本，并支持指定文本输入方式，仅针对可编辑的文本组件生效。使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Component-inputText(text: string, mode: InputTextMode): Promise<void>--><!--Device-Component-inputText(text: string, mode: InputTextMode): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 输入的文本信息，当前支持英文、中文和特殊字符。 |
| mode | [InputTextMode](arkts-test-uitest-inputtextmode-i.md) | Yes | 输入文本的方式，取值请参考[InputTextMode](arkts-test-uitest-inputtextmode-i.md)。  **说明：** InputTextMode.addition取值为true时，在控件已有文本末尾后追加指定文本。取值为false时，指定文本将覆盖控件已有文本。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Function can not work correctly due to limited device capabilities. |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function mode_demo() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.text('hello world'));
  await text.inputText('123', { paste: true, addition: false });
}
```

## isCheckable

```TypeScript
isCheckable(): Promise<boolean>
```

获取控件对象能否被勾选属性。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-isCheckable(): Promise<boolean>--><!--Device-Component-isCheckable(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回控件对象能否可被勾选属性。true：可被勾选。false：不可被勾选。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let checkBox: Component = await driver.findComponent(ON.type('Checkbox'));
  if (await checkBox.isCheckable()) {
    console.info('This checkBox is checkable');
  } else {
    console.info('This checkBox is not checkable');
  }
}
```

## isChecked

```TypeScript
isChecked(): Promise<boolean>
```

获取控件对象被勾选状态。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-isChecked(): Promise<boolean>--><!--Device-Component-isChecked(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回控件对象被勾选状态。true：被勾选。false：未被勾选。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let checkBox: Component = await driver.findComponent(ON.type('Checkbox'));
  if (await checkBox.isChecked()) {
    console.info('This checkBox is checked');
  } else {
    console.info('This checkBox is not checked');
  }
}
```

## isClickable

```TypeScript
isClickable(): Promise<boolean>
```

获取控件对象可点击属性。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-isClickable(): Promise<boolean>--><!--Device-Component-isClickable(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回控件对象是否可点击。true：可点击。false：不可点击。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  if (await button.isClickable()) {
    console.info('This button can be clicked');
  } else {
    console.info('This button cannot be clicked');
  }
}
```

## isEnabled

```TypeScript
isEnabled(): Promise<boolean>
```

获取控件使能状态。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-isEnabled(): Promise<boolean>--><!--Device-Component-isEnabled(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回控件使能状态。true：使能。false：未使能。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
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

判断控件对象获焦状态。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-isFocused(): Promise<boolean>--><!--Device-Component-isFocused(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回控件对象获焦状态。true：获焦。false：未获焦。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  if (await button.isFocused()) {
    console.info('This button is focused');
  } else {
    console.info('This button is not focused');
  }
}
```

## isLongClickable

```TypeScript
isLongClickable(): Promise<boolean>
```

获取控件对象可点击属性。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-isLongClickable(): Promise<boolean>--><!--Device-Component-isLongClickable(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回控件对象是否可点击。true：可点击。false：不可点击。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  if (await button.isLongClickable()) {
    console.info('This button supports long click');
  } else {
    console.info('This button can not support long click');
  }
}
```

## isScrollable

```TypeScript
isScrollable(): Promise<boolean>
```

获取控件对象可滑动属性。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-isScrollable(): Promise<boolean>--><!--Device-Component-isScrollable(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回控件对象是否可滑动。true：可滑动。false：不可滑动。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component = await driver.findComponent(ON.scrollable(true));
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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-isSelected(): Promise<boolean>--><!--Device-Component-isSelected(): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回控件对象被选中状态。true：被选中。false：未被选中。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-longClick(): Promise<void>--><!--Device-Component-longClick(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  await button.longClick();
}
```

## pinchIn

ArkTS-Dyn:
```TypeScript
pinchIn(scale: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
pinchIn(scale: double): Promise<void>
```

将控件按指定的比例进行捏合缩小。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-pinchIn(scale: double): Promise<void>--><!--Device-Component-pinchIn(scale: double): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scale | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 指定缩小的比例。取值范围为0~1。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let image: Component = await driver.findComponent(ON.type('Image'));
  await image.pinchIn(0.5);
}
```

## pinchOut

ArkTS-Dyn:
```TypeScript
pinchOut(scale: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
pinchOut(scale: double): Promise<void>
```

将控件按指定的比例进行捏合放大。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-pinchOut(scale: double): Promise<void>--><!--Device-Component-pinchOut(scale: double): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scale | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 指定放大的比例。取值范围大于1。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let image: Component = await driver.findComponent(ON.type('Image'));
  await image.pinchOut(1.5);
}
```

## scrollSearch

```TypeScript
scrollSearch(on: On): Promise<Component>
```

在控件上滑动查找目标控件（适用支持滑动的控件）。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-scrollSearch(on: On): Promise<Component>--><!--Device-Component-scrollSearch(on: On): Promise<Component>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | 目标控件的属性要求。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Component&gt; | Promise对象，返回目标控件对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  // Create a Driver object.
  let driver: Driver = Driver.create();
  // Obtain the scrollable Scroll component.
  let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
  // Scroll on the Scroll component to search for the component whose text is 'next page'.
  let button = await scrollBar.scrollSearch(ON.text('next page'));
}
```

## scrollSearch

```TypeScript
scrollSearch(on: On, vertical?: boolean, offset?: number): Promise<Component>
```

在控件上滑动查找目标控件（适用支持滑动的控件），支持指定滑动方向和滑动起止点与组件边框的偏移量。使用Promise异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Component-scrollSearch(on: On, vertical?: boolean, offset?: number): Promise<Component>--><!--Device-Component-scrollSearch(on: On, vertical?: boolean, offset?: number): Promise<Component>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | 目标控件的属性要求。 |
| vertical | boolean | No | 默认为true，表示查找方向是纵向。false表示查找方向为横向。 |
| offset | number | No | 滑动起点/终点到组件边框的偏移，默认80，单位：px，取值范围：大于等于0的整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Component&gt; | Promise对象，返回目标控件对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
  let button = await scrollBar.scrollSearch(ON.text('next page'));
}
```

## scrollSearch

```TypeScript
scrollSearch(on: On, vertical?: boolean, offset?: int): Promise<Component | null>
```

Scroll on this {@link Component}to find matched {@link Component},applicable to scrollable one.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Component-scrollSearch(on: On, vertical?: boolean, offset?: int): Promise<Component | null>--><!--Device-Component-scrollSearch(on: On, vertical?: boolean, offset?: int): Promise<Component | null>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | the attribute requirements of the target {@link Component}. |
| vertical | boolean | No | Whether the swipe direction is vertical, default is true. |
| offset | int | No | Offset from the swipe start/end point to the component border, default is 80. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Component \| null&gt; | the found result,or null if not found. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## scrollToBottom

ArkTS-Dyn:
```TypeScript
scrollToBottom(speed?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
scrollToBottom(speed?: int): Promise<void>
```

在控件上滑动到底部（适用支持滑动的控件）。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-scrollToBottom(speed?: int): Promise<void>--><!--Device-Component-scrollToBottom(speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| speed | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
  await scrollBar.scrollToBottom();
}
```

## scrollToTop

ArkTS-Dyn:
```TypeScript
scrollToTop(speed?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
scrollToTop(speed?: int): Promise<void>
```

在控件上滑动到顶部（适用支持滑动的控件）。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Component-scrollToTop(speed?: int): Promise<void>--><!--Device-Component-scrollToTop(speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| speed | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |
| 17000004 | The window or component is invisible or destroyed. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
  await scrollBar.scrollToTop();
}
```

