# Component

UiTest框架在API9中，Component类代表了UI界面上的一个控件，提供控件属性获取，控件点击，滑动查找，文本注入等API。该类对象可通过[findComponent](arkts-test-uitest-driver-c.md#findComponent)、[findComponents](arkts-test-uitest-driver-c.md#findComponents)、[waitForComponent](arkts-test-uitest-driver-c.md#waitForComponent)等接口获取。该类提供的所有方法都使用Promise方式作为异步方法，需使用await调用。

**起始版本：** 9

<!--Device-unnamed-declare class Component--><!--Device-unnamed-declare class Component-End-->

**系统能力：** SystemCapability.Test.UiTest

## clearText

```TypeScript
clearText(): Promise<void>
```

清除控件的文本信息，仅针对可编辑的文本组件生效。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-clearText(): Promise<void>--><!--Device-Component-clearText(): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-click(): Promise<void>--><!--Device-Component-click(): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, ON, Component } from '@kit.TestKit';

async function demo() {
  // 创建Driver对象。
  let driver: Driver = Driver.create();
  // 查找Button类型的控件。
  let button: Component = await driver.findComponent(ON.type('Button'));
  // 点击该控件。
  await button.click();
}
```

## doubleClick

```TypeScript
doubleClick(): Promise<void>
```

控件对象进行双击操作。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-doubleClick(): Promise<void>--><!--Device-Component-doubleClick(): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-dragTo(target: Component): Promise<void>--><!--Device-Component-dragTo(target: Component): Promise<void>-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  // 创建Driver对象。
  let driver: Driver = Driver.create();
  // 查找Button类型的目标控件。
  let button: Component = await driver.findComponent(ON.type('Button'));
  // 查找text为'hello world'的控件作为拖拽目标。
  let text: Component = await driver.findComponent(ON.text('hello world'));
  // 将Button控件拖拽至text控件处。
  await button.dragTo(text);
}
```

## getBounds

```TypeScript
getBounds(): Promise<Rect>
```

获取控件对象的边框信息。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-getBounds(): Promise<Rect>--><!--Device-Component-getBounds(): Promise<Rect>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Rect](arkts-test-uitest-rect-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-getBoundsCenter(): Promise<Point>--><!--Device-Component-getBoundsCenter(): Promise<Point>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Point](arkts-test-uitest-point-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-getDescription(): Promise<string>--><!--Device-Component-getDescription(): Promise<string>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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

```TypeScript
getDisplayId(): Promise<number>
```

获取控件对象所属的屏幕ID。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Component-getDisplayId(): Promise<int>--><!--Device-Component-getDisplayId(): Promise<int>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Component-getHint(): Promise<string>--><!--Device-Component-getHint(): Promise<string>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-getId(): Promise<string>--><!--Device-Component-getId(): Promise<string>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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
[accessibilityLevel](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-accessibility.md#accessibilitylevel)设置为'no'或'no-hide-descendants'，可以使用本接口获取控件的文本信息，无法使用[Component.getText()](#getText)获取控件的文本信息。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Component-getOriginalText(): Promise<string>--><!--Device-Component-getOriginalText(): Promise<string>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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
> 设置为'no'或'no-hide-descendants'，无法使用本接口获取控件的文本信息，可以使用[Component.getOriginalText()](#getOriginalText)
> 获取控件的文本信息。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-getText(): Promise<string>--><!--Device-Component-getText(): Promise<string>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-getType(): Promise<string>--><!--Device-Component-getType(): Promise<string>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-inputText(text: string): Promise<void>--><!--Device-Component-inputText(text: string): Promise<void>-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  // 创建Driver对象。
  let driver: Driver = Driver.create();
  // 查找text为'hello world'的控件。
  let text: Component = await driver.findComponent(ON.text('hello world'));
  // 清空原有文本并输入'123'。
  await text.inputText('123');
}
```

## inputText

```TypeScript
inputText(text: string, mode: InputTextMode): Promise<void>
```

向控件中输入文本，并支持指定文本输入方式，仅针对可编辑的文本组件生效。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Component-inputText(text: string, mode: InputTextMode): Promise<void>--><!--Device-Component-inputText(text: string, mode: InputTextMode): Promise<void>-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-isCheckable(): Promise<boolean>--><!--Device-Component-isCheckable(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-isChecked(): Promise<boolean>--><!--Device-Component-isChecked(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-isClickable(): Promise<boolean>--><!--Device-Component-isClickable(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-isEnabled(): Promise<boolean>--><!--Device-Component-isEnabled(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-isFocused(): Promise<boolean>--><!--Device-Component-isFocused(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-isLongClickable(): Promise<boolean>--><!--Device-Component-isLongClickable(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-isScrollable(): Promise<boolean>--><!--Device-Component-isScrollable(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-isSelected(): Promise<boolean>--><!--Device-Component-isSelected(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-longClick(): Promise<void>--><!--Device-Component-longClick(): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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

```TypeScript
pinchIn(scale: number): Promise<void>
```

将控件按指定的比例进行捏合缩小。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-pinchIn(scale: double): Promise<void>--><!--Device-Component-pinchIn(scale: double): Promise<void>-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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

```TypeScript
pinchOut(scale: number): Promise<void>
```

将控件按指定的比例进行捏合放大。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-pinchOut(scale: double): Promise<void>--><!--Device-Component-pinchOut(scale: double): Promise<void>-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-scrollSearch(on: On): Promise<Component>--><!--Device-Component-scrollSearch(on: On): Promise<Component>-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  // 创建Driver对象。
  let driver: Driver = Driver.create();
  // 获取可滑动的Scroll控件。
  let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
  // 在Scroll控件上滑动查找text为'next page'的控件。
  let button = await scrollBar.scrollSearch(ON.text('next page'));
}
```

## scrollSearch

```TypeScript
scrollSearch(on: On, vertical?: boolean, offset?: number): Promise<Component>
```

在控件上滑动查找目标控件（适用支持滑动的控件），支持指定滑动方向和滑动起止点与组件边框的偏移量。使用Promise异步回调。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Component-scrollSearch(on: On, vertical?: boolean, offset?: number): Promise<Component>--><!--Device-Component-scrollSearch(on: On, vertical?: boolean, offset?: number): Promise<Component>-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
  let button = await scrollBar.scrollSearch(ON.text('next page'));
}
```

## scrollToBottom

```TypeScript
scrollToBottom(speed?: number): Promise<void>
```

在控件上滑动到底部（适用支持滑动的控件）。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-scrollToBottom(speed?: int): Promise<void>--><!--Device-Component-scrollToBottom(speed?: int): Promise<void>-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

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

```TypeScript
scrollToTop(speed?: number): Promise<void>
```

在控件上滑动到顶部（适用支持滑动的控件）。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Component-scrollToTop(speed?: int): Promise<void>--><!--Device-Component-scrollToTop(speed?: int): Promise<void>-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000004-目标控件窗口不可见或已销毁) |

## 示例

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
  await scrollBar.scrollToTop();
}
```
