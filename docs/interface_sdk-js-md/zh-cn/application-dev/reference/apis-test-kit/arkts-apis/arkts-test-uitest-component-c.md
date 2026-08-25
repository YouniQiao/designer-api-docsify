# Component

UiTest框架在API9中，Component类代表了UI界面上的一个控件，提供控件属性获取，控件点击，滑动查找，文本注入等API。 该类对象可通过[findComponent](arkts-test-uitest-driver-c.md#findcomponent)、[findComponents](arkts-test-uitest-driver-c.md#findcomponents)、[waitForComponent](arkts-test-uitest-driver-c.md#waitforcomponent)等接口获取。 该类提供的所有方法都使用Promise方式作为异步方法，需使用await调用。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Test.UiTest

## 导入模块

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from '@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from '@kit.TestKit';
```

## clearText

```TypeScript
clearText(): Promise<void>
```

清除控件的文本信息，仅针对可编辑的文本组件生效。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let text: Component | null = await driver.findComponent(ON.text('hello world'));
  if (text) {
    await text.clearText();
  }
}
```

## click

```TypeScript
click(): Promise<void>
```

控件对象进行点击操作。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// xxx.test.ets
import { Driver, ON, Component } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component | null = await driver.findComponent(ON.type('Button'));
  if (button) {
    await button.click();
  }
}
```

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.click(100, 100);
}
```

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  await button.click();
}
```

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.click(100, 100);
}
```

## doubleClick

```TypeScript
doubleClick(): Promise<void>
```

控件对象进行双击操作。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component | null = await driver.findComponent(ON.type('Button'));
  if (button) {
    await button.doubleClick();
  }
}
```

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.doubleClick(100, 100);
}
```

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  await button.doubleClick();
}
```

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.doubleClick(100, 100);
}
```

## dragTo

```TypeScript
dragTo(target: Component): Promise<void>
```

将控件拖拽至目标控件处。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component | null = await driver.findComponent(ON.type('Button'));
  let text: Component | null = await driver.findComponent(ON.text('hello world'));
  if (button && text) {
    await button.dragTo(text);
  }
}
```

## getBounds

```TypeScript
getBounds(): Promise<Rect>
```

获取控件对象的边框信息。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component | null = await driver.findComponent(ON.type('Button'));
  if (button) {
    let rect = await button.getBounds();
  }
}
```

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow | null = await driver.findWindow({ active: true });
  if (window) {
    let rect = await window.getBounds();
  }
}
```

## getBoundsCenter

```TypeScript
getBoundsCenter(): Promise<Point>
```

获取控件对象所占区域的中心点信息。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component | null = await driver.findComponent(ON.type('Button'));
  if (button) {
    let point = await button.getBoundsCenter();
  }
}
```

## getDescription

```TypeScript
getDescription(): Promise<string>
```

获取控件对象的描述信息。使用Promise异步回调。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component | null = await driver.findComponent(ON.type('Button'));
  if (button) {
    let description = await button.getDescription();
  }
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

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: Promise & lt;number & gt;<br>ArkTS-Sta：Promise & lt;int & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component | null = await driver.findComponent(ON.type('TextInput'));
  if (button) {
    let displayId = await button.getDisplayId();
  }
}
```

```TypeScript
// xxx.test.ets
import { UiWindow, Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow | null = await driver.findWindow({ active: true });
  if (window) {
    let id = await window.getDisplayId();
  }
}
```

## getHint

```TypeScript
getHint(): Promise<string>
```

获取控件对象的提示文本。使用Promise异步回调。

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component | null = await driver.findComponent(ON.type('TextInput'));
  if (button) {
    let hints = await button.getHint();
  }
}
```

## getId

```TypeScript
getId(): Promise<string>
```

获取控件对象的id值。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component | null = await driver.findComponent(ON.type('Button'));
  if (button) {
    let id = await button.getId();
  }
}
```

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  let id = await button.getId();
}
```

## getOriginalText

```TypeScript
getOriginalText(): Promise<string>
```

获取控件对象的文本信息。使用Promise异步回调。如果控件的无障碍属性 accessibilityLevel 设置为'no'或'no-hide-descendants'，可以使用本接口获取控件的文本信息，无法使用[Component.getText()](#gettext)获取控件的文本信息。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component | null = await driver.findComponent(ON.type('Button'));
  if (button) {
    let text = await button.getOriginalText();
  }
}
```

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

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component | null = await driver.findComponent(ON.type('Button'));
  if (button) {
    let text = await button.getText();
  }
}
```

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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component | null = await driver.findComponent(ON.type('Button'));
  if (button) {
    let type = await button.getType();
  }
}
```

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

清空组件内原有文本并输入指定文本内容，仅针对可编辑的文本组件生效。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let text: Component | null = await driver.findComponent(ON.text('hello world'));
  if (text) {
    await text.inputText('123');
  }
}
```

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function mode_demo() {
  let driver: Driver = Driver.create();
  let text: Component | null = await driver.findComponent(ON.text('hello world'));
  if (text) {
    await text.inputText('123', { paste: true, addition: false });
  }
}
```

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let text: Component | null = await driver.findComponent(ON.type('TextInput'));
  if (text) {
    let point = await text.getBoundsCenter();
    await driver.inputText(point, '123');
  }
}
```

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let text: Component | null = await driver.findComponent(ON.type('TextInput'));
  if (text) {
    let point = await text.getBoundsCenter();
    await driver.inputText(point, '123', { paste: true, addition: false });
  }
}

async function demo_Chinese() {
  let driver: Driver = Driver.create();
  let text: Component | null = await driver.findComponent(ON.type('TextInput'));
  if (text) {
    let point = await text.getBoundsCenter();
    await driver.inputText(point, '中文&', { paste: false, addition: true });
  }
}
```

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let text: UiComponent = await driver.findComponent(BY.text('hello world'));
  await text.inputText('123');
}
```

## inputText

```TypeScript
inputText(text: string, mode: InputTextMode): Promise<void>
```

向控件中输入文本，并支持指定文本输入方式，仅针对可编辑的文本组件生效。使用Promise异步回调。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

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

**示例**

参见 [inputText](#inputtext)

## isCheckable

```TypeScript
isCheckable(): Promise<boolean>
```

获取控件对象能否被勾选属性。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let checkBox: Component | null = await driver.findComponent(ON.type('Checkbox'));
  if (checkBox && await checkBox.isCheckable()) {
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let checkBox: Component | null = await driver.findComponent(ON.type('Checkbox'));
  if (checkBox && await checkBox.isChecked()) {
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component | null = await driver.findComponent(ON.type('Button'));
  if (button && await button.isClickable()) {
    console.info('This button can be Clicked');
  } else {
    console.info('This button can not be Clicked');
  }
}
```

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent | null = await driver.findComponent(BY.type('Button'));
  if (button) {
    if (await button.isLongClickable()) {
      console.info('This button supports long click');
    } else {
      console.info('This button can not support long click');
    }
  }
}
```

## isEnabled

```TypeScript
isEnabled(): Promise<boolean>
```

获取控件使能状态。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component | null = await driver.findComponent(ON.type('Button'));
  if (button && await button.isEnabled()) {
    console.info('This button can be operated');
  } else {
    console.info('This button can not be operated');
  }
}
```

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  if (await button.isEnabled()) {
    console.info('This button can be operated');
  } else {
    console.info('This button can not be operated');
  }
}
```

## isFocused

```TypeScript
isFocused(): Promise<boolean>
```

判断控件对象获焦状态。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component | null = await driver.findComponent(ON.type('Button'));
  if (button && await button.isFocused()) {
    console.info('This button is focused');
  } else {
    console.info('This button is not focused');
  }
}
```

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow | null = await driver.findWindow({ active: true });
  if (window) {
    let focused = await window.isFocused();
  }
}
```

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  if (button) {
    if (await button.isFocused()) {
      console.info('This button is focused');
    } else {
      console.info('This button is not focused');
    }
    if (await button.isSelected()) {
      console.info('This button is selected');
    } else {
      console.info('This button is not selected');
    }
  }
}
```

## isLongClickable

```TypeScript
isLongClickable(): Promise<boolean>
```

获取控件对象可点击属性。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component | null = await driver.findComponent(ON.type('Button'));
  if (button && await button.isLongClickable()) {
    console.info('This button can longClick');
  } else {
    console.info('This button can not longClick');
  }
}
```

## isScrollable

```TypeScript
isScrollable(): Promise<boolean>
```

获取控件对象可滑动属性。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component | null = await driver.findComponent(ON.scrollable(true));
  if (scrollBar && await scrollBar.isScrollable()) {
    console.info('This scrollBar can be operated');
  } else {
    console.info('This scrollBar can not be operated');
  }
}
```

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let scrollBar: UiComponent | null = await driver.findComponent(BY.scrollable(true));
  if (scrollBar) {
    if (await scrollBar.isScrollable()) {
      console.info('This scrollBar can be operated');
    } else {
      console.info('This scrollBar can not be operated');
    }
  }
}
```

## isSelected

```TypeScript
isSelected(): Promise<boolean>
```

获取控件对象被选中状态。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component | null = await driver.findComponent(ON.type('Button'));
  if (button && await button.isSelected()) {
    console.info('This button is selected');
  } else {
    console.info('This button is not selected');
  }
}
```

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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component | null = await driver.findComponent(ON.type('Button'));
  if (button) {
    await button.longClick();
  }
}
```

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.longClick(100, 100);
}
```

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  await button.longClick();
}
```

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.longClick(100, 100);
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scale | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let image: Component | null = await driver.findComponent(ON.type('Image'));
  if (image) {
    await image.pinchIn(0.5);
  }
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scale | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let image: Component | null = await driver.findComponent(ON.type('Image'));
  if (image) {
    await image.pinchOut(1.5);
  }
}
```

## scrollSearch

```TypeScript
scrollSearch(on: On): Promise<Component>
```

在控件上滑动查找目标控件（适用支持滑动的控件）。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component | null = await driver.findComponent(ON.type('Scroll'));
  if (scrollBar) {
  let button = await scrollBar.scrollSearch(ON.text('next page'));
    if (button) {
      await button.click();
    }
  }
}
```

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component | null = await driver.findComponent(ON.type('Scroll'));
  if (scrollBar) {
  let button = await scrollBar.scrollSearch(ON.text('next page'));
    if (button) {
      await button.click();
    }
  }
}
```

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
  let button = await scrollBar.scrollSearch(ON.text('next page'));
}
```

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let scrollBar: UiComponent = await driver.findComponent(BY.type('Scroll'));
  let button = await scrollBar.scrollSearch(BY.text('next page'));
}
```

## scrollSearch

```TypeScript
scrollSearch(on: On, vertical?: boolean, offset?: number): Promise<Component>
```

在控件上滑动查找目标控件（适用支持滑动的控件），支持指定滑动方向和滑动起止点与组件边框的偏移量。使用Promise异步回调。

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为18。

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

**示例**

参见 [scrollSearch](#scrollsearch)

## scrollSearch

```TypeScript
scrollSearch(on: On, vertical?: boolean, offset?: int): Promise<Component | null>
```

Scroll on this [Component](#component)to find matched [Component](#component),applicable to scrollable one.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | 是 |
| vertical | boolean | 否 |
| offset | int | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Component](arkts-test-uitest-component-c.md) \| null & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

**示例**

参见 [scrollSearch](#scrollsearch)

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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| speed | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component | null = await driver.findComponent(ON.type('Scroll'));
  if (scrollBar) {
    await scrollBar.scrollToBottom();
  }
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| speed | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

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

**示例**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component | null = await driver.findComponent(ON.type('Scroll'));
  if (scrollBar) {
    await scrollBar.scrollToTop();
  }
}
```
