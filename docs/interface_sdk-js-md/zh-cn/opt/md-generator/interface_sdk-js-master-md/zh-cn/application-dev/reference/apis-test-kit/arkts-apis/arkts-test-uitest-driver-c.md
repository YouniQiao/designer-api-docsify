# Driver

Driver类为uitest测试框架的总入口，提供控件匹配/查找，按键注入，坐标点击/滑动，截图等能力。通过[create](create)创建实例。该类提供的方法除Driver.create()和Driver.createUIEventObserver()以外的所有方法都使用Promise方式作为异步方法，需使用await方式调用。

**起始版本：** 9

<!--Device-unnamed-declare class Driver--><!--Device-unnamed-declare class Driver-End-->

**系统能力：** SystemCapability.Test.UiTest

## assertComponentExist

```TypeScript
assertComponentExist(on: On): Promise<void>
```

断言API，用于断言当前界面是否存在满足给出的目标属性的控件。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-assertComponentExist(on: On): Promise<void>--><!--Device-Driver-assertComponentExist(on: On): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000003-断言失败) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.assertComponentExist(ON.text('next page'));
}
```

## click

```TypeScript
click(x: number, y: number): Promise<void>
```

在目标坐标点单击。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-click(x: int, y: int): Promise<void>--><!--Device-Driver-click(x: int, y: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  // 创建Driver对象。
  let driver: Driver = Driver.create();
  // 在坐标(100,100)处执行点击操作。
  await driver.click(100, 100);
}
```

## clickAt

```TypeScript
clickAt(point: Point): Promise<void>
```

在目标坐标点进行单击。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-clickAt(point: Point): Promise<void>--><!--Device-Driver-clickAt(point: Point): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.clickAt({ x: 100, y: 100, displayId: 0 });
}
```

## clickAtWithOptions

```TypeScript
clickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>
```

点击屏幕上的指定位置，可选择触摸选项。

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-clickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>--><!--Device-Driver-clickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | 是 |
| options | [TouchOptions](arkts-test-uitest-touchoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, TouchOptions } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let options: TouchOptions = {
    pressure: 0.5
  };
  // 在目标坐标点进行单击，并指定触摸压力。
  await driver.clickAtWithOptions({ x: 100, y: 100, displayId: 0 }, options);
}
```

## create

```TypeScript
static create(): Driver
```

静态方法，构造一个Driver对象，并返回该对象。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-static create(): Driver--><!--Device-Driver-static create(): Driver-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| [Driver](arkts-test-uitest-driver-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [17000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000001-初始化失败) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
}
```

## createUIEventObserver

```TypeScript
createUIEventObserver(): UIEventObserver
```

创建一个UI事件监听器。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-createUIEventObserver(): UIEventObserver--><!--Device-Driver-createUIEventObserver(): UIEventObserver-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| [UIEventObserver](arkts-test-uitest-uieventobserver-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, UIEventObserver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let observer: UIEventObserver = driver.createUIEventObserver();
}
```

## crownRotate

```TypeScript
crownRotate(d: number, speed?: number): Promise<void>
```

注入手表表冠旋转事件，可指定旋转速度。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-crownRotate(d: int, speed?: int): Promise<void>--><!--Device-Driver-crownRotate(d: int, speed?: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | number | 是 |
| speed | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // 顺时针旋转50格，旋转速度为30格/秒。
  await driver.crownRotate(50, 30);
  // 逆时针旋转20格，旋转速度为30格/秒。
  await driver.crownRotate(-20, 30);
}
```

## delayMs

```TypeScript
delayMs(duration: number): Promise<void>
```

在给定的时间内延时。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-delayMs(duration: int): Promise<void>--><!--Device-Driver-delayMs(duration: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| duration | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.delayMs(1000);
}
```

## doubleClick

```TypeScript
doubleClick(x: number, y: number): Promise<void>
```

在目标坐标点双击。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-doubleClick(x: int, y: int): Promise<void>--><!--Device-Driver-doubleClick(x: int, y: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.doubleClick(100, 100);
}
```

## doubleClickAt

```TypeScript
doubleClickAt(point: Point): Promise<void>
```

对目标坐标进行双击。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-doubleClickAt(point: Point): Promise<void>--><!--Device-Driver-doubleClickAt(point: Point): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.doubleClickAt({ x: 100, y: 100, displayId: 0 });
}
```

## drag

```TypeScript
drag(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>
```

从起始坐标点拖拽至目的坐标点。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-drag(startx: int, starty: int, endx: int, endy: int, speed?: int): Promise<void>--><!--Device-Driver-drag(startx: int, starty: int, endx: int, endy: int, speed?: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| startx | number | 是 |
| starty | number | 是 |
| endx | number | 是 |
| endy | number | 是 |
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

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.drag(100, 100, 200, 200, 600);
}
```

## dragBetween

```TypeScript
dragBetween(from: Point, to: Point, speed?: number, duration?: number): Promise<void>
```

从起始坐标点拖拽至目标坐标点，支持指定拖拽速度和拖拽前长按时间。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-dragBetween(from: Point, to: Point, speed?: int, duration?: int): Promise<void>--><!--Device-Driver-dragBetween(from: Point, to: Point, speed?: int, duration?: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | 是 |
| to | [Point](arkts-test-uitest-point-i.md) | 是 |
| speed | number | 否 |
| duration | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.dragBetween({ x: 100, y: 100, displayId: 0 }, { x: 1000, y: 1000, displayId: 0 }, 800, 1500);
}
```

## dragBetweenWithOptions

```TypeScript
dragBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>
```

在屏幕上拖拽指定的点之间，具有可选设置。

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-dragBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>--><!--Device-Driver-dragBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | 是 |
| to | [Point](arkts-test-uitest-point-i.md) | 是 |
| options | [TouchOptions](arkts-test-uitest-touchoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, TouchOptions } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let options: TouchOptions = {
    speed: 800,     // 拖拽速率800px/s。
    duration: 2000, // 拖拽前长按2000ms。
    pressure: 0.5   // 触摸压力值。
  };
  // 从起始坐标点拖拽至目标坐标点，并指定拖拽速率、长按时长和触摸压力。
  await driver.dragBetweenWithOptions({ x: 100, y: 100, displayId: 0 }, { x: 1000, y: 1000, displayId: 0 }, options);
}
```

## dumpLayout

```TypeScript
dumpLayout(savePath: string, displayId?: number): Promise<boolean>
```

Get the current layout information and save as file with json format.

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-dumpLayout(savePath: string, displayId?: int): Promise<boolean>--><!--Device-Driver-dumpLayout(savePath: string, displayId?: int): Promise<boolean>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| savePath | string | 是 |
| displayId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // 获取当前布局信息并保存为JSON文件。
  await driver.dumpLayout('/data/storage/el2/base/cache/layout.json', 0);
}
```

## findComponent

```TypeScript
findComponent(on: On): Promise<Component>
```

根据给出的目标控件属性要求查找目标控件。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-findComponent(on: On): Promise<Component>--><!--Device-Driver-findComponent(on: On): Promise<Component>-End-->

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

## 示例

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  // 创建Driver对象。
  let driver: Driver = Driver.create();
  // 查找text为'next page'的控件。
  let button: Component = await driver.findComponent(ON.text('next page'));
}
```

## findComponents

```TypeScript
findComponents(on: On): Promise<Array<Component>>
```

根据给出的目标控件属性要求查找出所有匹配控件，以列表保存。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-findComponents(on: On): Promise<Array<Component>>--><!--Device-Driver-findComponents(on: On): Promise<Array<Component>>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[Component](arkts-test-uitest-component-c.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  // 创建Driver对象。
  let driver: Driver = Driver.create();
  // 查找所有text为'next page'的控件。
  let buttonList: Array<Component> = await driver.findComponents(ON.text('next page'));
}
```

## findWindow

```TypeScript
findWindow(filter: WindowFilter): Promise<UiWindow>
```

通过指定窗口的属性来查找目标窗口。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-findWindow(filter: WindowFilter): Promise<UiWindow>--><!--Device-Driver-findWindow(filter: WindowFilter): Promise<UiWindow>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [WindowFilter](arkts-test-uitest-windowfilter-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[UiWindow](arkts-test-uitest-uiwindow-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ active: true });
}
```

## fling

```TypeScript
fling(from: Point, to: Point, stepLen: number, speed: number): Promise<void>
```

模拟手指滑动后脱离屏幕的快速滑动操作。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-fling(from: Point, to: Point, stepLen: int, speed: int): Promise<void>--><!--Device-Driver-fling(from: Point, to: Point, stepLen: int, speed: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | 是 |
| to | [Point](arkts-test-uitest-point-i.md) | 是 |
| stepLen | number | 是 |
| speed | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.fling({ x: 500, y: 480 }, { x: 450, y: 480 }, 5, 600);
}
```

## fling

```TypeScript
fling(direction: UiDirection, speed: number): Promise<void>
```

指定方向和滑动速率，模拟手指滑动后脱离屏幕的快速滑动操作。使用Promise异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-fling(direction: UiDirection, speed: int): Promise<void>--><!--Device-Driver-fling(direction: UiDirection, speed: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| direction | [UiDirection](arkts-test-uitest-uidirection-e.md) | 是 |
| speed | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, UiDirection } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.fling(UiDirection.DOWN, 10000);
}
```

## fling

```TypeScript
fling(direction: UiDirection, speed: number, displayId: number): Promise<void>
```

指定方向、滑动速率和操作屏幕，模拟手指滑动后脱离屏幕的快速滑动操作。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-fling(direction: UiDirection, speed: int, displayId: int): Promise<void>--><!--Device-Driver-fling(direction: UiDirection, speed: int, displayId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| direction | [UiDirection](arkts-test-uitest-uidirection-e.md) | 是 |
| speed | number | 是 |
| displayId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, UiDirection } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.fling(UiDirection.DOWN, 10000, 0);
}
```

## getDisplayDensity

```TypeScript
getDisplayDensity(): Promise<Point>
```

获取当前设备屏幕的分辨率。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-getDisplayDensity(): Promise<Point>--><!--Device-Driver-getDisplayDensity(): Promise<Point>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Point](arkts-test-uitest-point-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let density = await driver.getDisplayDensity();
}
```

## getDisplayDensity

```TypeScript
getDisplayDensity(displayId: number): Promise<Point>
```

获取当前设备指定屏幕的分辨率。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-getDisplayDensity(displayId: int): Promise<Point>--><!--Device-Driver-getDisplayDensity(displayId: int): Promise<Point>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Point](arkts-test-uitest-point-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let density = await driver.getDisplayDensity(0);
}
```

## getDisplayRotation

```TypeScript
getDisplayRotation(): Promise<DisplayRotation>
```

获取当前设备的屏幕显示方向。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-getDisplayRotation(): Promise<DisplayRotation>--><!--Device-Driver-getDisplayRotation(): Promise<DisplayRotation>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DisplayRotation](arkts-test-uitest-displayrotation-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { DisplayRotation, Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let rotation: DisplayRotation = await driver.getDisplayRotation();
}
```

## getDisplayRotation

```TypeScript
getDisplayRotation(displayId: number): Promise<DisplayRotation>
```

获取当前设备指定屏幕的显示方向。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-getDisplayRotation(displayId: int): Promise<DisplayRotation>--><!--Device-Driver-getDisplayRotation(displayId: int): Promise<DisplayRotation>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DisplayRotation](arkts-test-uitest-displayrotation-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |

## 示例

```TypeScript
// xxx.test.ets
import { DisplayRotation, Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let rotation: DisplayRotation = await driver.getDisplayRotation(0);
}
```

## getDisplaySize

```TypeScript
getDisplaySize(): Promise<Point>
```

获取当前设备的屏幕大小。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-getDisplaySize(): Promise<Point>--><!--Device-Driver-getDisplaySize(): Promise<Point>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Point](arkts-test-uitest-point-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let size = await driver.getDisplaySize();
}
```

## getDisplaySize

```TypeScript
getDisplaySize(displayId: number): Promise<Point>
```

获取当前设备指定屏幕的大小。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-getDisplaySize(displayId: int): Promise<Point>--><!--Device-Driver-getDisplaySize(displayId: int): Promise<Point>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Point](arkts-test-uitest-point-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let size = await driver.getDisplaySize(0);
}
```

## injectKnucklePointerAction

```TypeScript
injectKnucklePointerAction(pointers: PointerMatrix, speed?: number): Promise<void>
```

模拟指关节多点注入滑动操作。使用Promise异步回调。

> **说明：**
> 
> 若设备关闭了指关节手势&lt;!--RP4--&gt;&lt;!--RP4End--&gt;，则调用本接口返回17000005错误码。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-injectKnucklePointerAction(pointers: PointerMatrix, speed?: int): Promise<void>--><!--Device-Driver-injectKnucklePointerAction(pointers: PointerMatrix, speed?: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pointers | [PointerMatrix](arkts-test-uitest-pointermatrix-c.md) | 是 |
| speed | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |
| [17000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000005-操作不支持) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, PointerMatrix } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // 模拟指关节滑动在屏幕上画'S'。
  let pointers: PointerMatrix = PointerMatrix.create(1, 6);
  pointers.setPoint(0, 0, { x: 750, y: 300 });
  pointers.setPoint(0, 1, { x: 500, y: 100 });
  pointers.setPoint(0, 2, { x: 250, y: 300 });
  pointers.setPoint(0, 3, { x: 750, y: 800 });
  pointers.setPoint(0, 4, { x: 500, y: 1000 });
  pointers.setPoint(0, 5, { x: 250, y: 800 });
  await driver.injectKnucklePointerAction(pointers);
}
```

## injectMultiPointerAction

```TypeScript
injectMultiPointerAction(pointers: PointerMatrix, speed?: number): Promise<boolean>
```

向设备注入多指操作。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-injectMultiPointerAction(pointers: PointerMatrix, speed?: int): Promise<boolean>--><!--Device-Driver-injectMultiPointerAction(pointers: PointerMatrix, speed?: int): Promise<boolean>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pointers | [PointerMatrix](arkts-test-uitest-pointermatrix-c.md) | 是 |
| speed | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, PointerMatrix } from '@kit.TestKit';

async function demo() {
  // 创建Driver对象。
  let driver: Driver = Driver.create();
  // 创建2指5步的滑动轨迹矩阵。
  let pointers: PointerMatrix = PointerMatrix.create(2, 5);
  // 设置第一根手指的滑动轨迹。
  pointers.setPoint(0, 0, { x: 250, y: 480 });
  pointers.setPoint(0, 1, { x: 250, y: 440 });
  pointers.setPoint(0, 2, { x: 250, y: 400 });
  pointers.setPoint(0, 3, { x: 250, y: 360 });
  pointers.setPoint(0, 4, { x: 250, y: 320 });
  // 设置第二根手指的滑动轨迹。
  pointers.setPoint(1, 0, { x: 250, y: 480 });
  pointers.setPoint(1, 1, { x: 250, y: 440 });
  pointers.setPoint(1, 2, { x: 250, y: 400 });
  pointers.setPoint(1, 3, { x: 250, y: 360 });
  pointers.setPoint(1, 4, { x: 250, y: 320 });
  // 注入双指滑动操作。
  await driver.injectMultiPointerAction(pointers);
}
```

## injectPenPointerAction

```TypeScript
injectPenPointerAction(pointers: PointerMatrix, speed?: number, pressure?: number): Promise<void>
```

模拟手写笔多点连续注入操作。使用Promise异步回调。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-injectPenPointerAction(pointers: PointerMatrix, speed?: int, pressure?: double): Promise<void>--><!--Device-Driver-injectPenPointerAction(pointers: PointerMatrix, speed?: int, pressure?: double): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pointers | [PointerMatrix](arkts-test-uitest-pointermatrix-c.md) | 是 |
| speed | number | 否 |
| pressure | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, PointerMatrix } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // 创建单指8步的滑动轨迹矩阵。
  let pointer = PointerMatrix.create(1, 8);
  // 循环设置每步坐标点，模拟从下向上的滑动。
  for (let step = 0; step < 8; step++) {
    pointer.setPoint(0, step, { x: 500, y: 1100 - 100 * step });
  }
  // 以600px/s速率和0.5压力值注入手写笔滑动操作。
  await driver.injectPenPointerAction(pointer, 600, 0.5);
}
```

## inputText

```TypeScript
inputText(p: Point, text: string): Promise<void>
```

在指定坐标点输入文本，不清空组件内原有文本，直接在坐标处追加输入。使用Promise异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-inputText(p: Point, text: string): Promise<void>--><!--Device-Driver-inputText(p: Point, text: string): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | 是 |
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

## 示例

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  // 创建Driver对象。
  let driver: Driver = Driver.create();
  // 查找TextInput类型的目标控件。
  let text: Component = await driver.findComponent(ON.type('TextInput'));
  // 获取控件中心点坐标。
  let point = await text.getBoundsCenter();
  // 在坐标点处输入文本'123'。
  await driver.inputText(point, '123');
}
```

## inputText

```TypeScript
inputText(p: Point, text: string, mode: InputTextMode): Promise<void>
```

在指定坐标点输入文本，支持指定文本输入方式。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-inputText(p: Point, text: string, mode: InputTextMode): Promise<void>--><!--Device-Driver-inputText(p: Point, text: string, mode: InputTextMode): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | 是 |
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

## 示例

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.type('TextInput'));
  let point = await text.getBoundsCenter();
  await driver.inputText(point, '123', { paste: true, addition: false });
}

async function demoChinese() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.type('TextInput'));
  let point = await text.getBoundsCenter();
  await driver.inputText(point, '中文&', { paste: false, addition: true });
  // 以复制粘贴方式输入中文、特殊符号，指定文本追加到指定坐标所在文本段的末尾。
}
```

## isComponentPresentWhenDrag

```TypeScript
isComponentPresentWhenDrag(on: On, from: Point, to: Point, speed?: number, duration?: number): Promise<boolean>
```

从起始点拖拽至终止点，并查找目标控件是否存在。使用Promise异步回调。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-isComponentPresentWhenDrag(on: On, from: Point, to: Point, speed?: int, duration?: int): Promise<boolean>--><!--Device-Driver-isComponentPresentWhenDrag(on: On, from: Point, to: Point, speed?: int, duration?: int): Promise<boolean>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | 是 |
| from | [Point](arkts-test-uitest-point-i.md) | 是 |
| to | [Point](arkts-test-uitest-point-i.md) | 是 |
| speed | number | 否 |
| duration | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let isExist = await driver.isComponentPresentWhenDrag(ON.id('123'), { x: 100, y: 100 }, { x: 200, y: 200 }, 1000, 2000);
}
```

## isComponentPresentWhenLongClick

```TypeScript
isComponentPresentWhenLongClick(on: On, point: Point, duration?: number): Promise<boolean>
```

在坐标点长按，并查找目标控件是否存在。使用Promise异步回调。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-isComponentPresentWhenLongClick(on: On, point: Point, duration?: int): Promise<boolean>--><!--Device-Driver-isComponentPresentWhenLongClick(on: On, point: Point, duration?: int): Promise<boolean>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | 是 |
| point | [Point](arkts-test-uitest-point-i.md) | 是 |
| duration | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let isExist = await driver.isComponentPresentWhenLongClick(ON.id('123'), { x: 100, y: 100 }, 2000);
}
```

## isComponentPresentWhenSwipe

```TypeScript
isComponentPresentWhenSwipe(on: On, from: Point, to: Point, speed?: number): Promise<boolean>
```

从起始点滑向终止点，并查找目标控件是否存在。使用Promise异步回调。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-isComponentPresentWhenSwipe(on: On, from: Point, to: Point, speed?: int): Promise<boolean>--><!--Device-Driver-isComponentPresentWhenSwipe(on: On, from: Point, to: Point, speed?: int): Promise<boolean>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | 是 |
| from | [Point](arkts-test-uitest-point-i.md) | 是 |
| to | [Point](arkts-test-uitest-point-i.md) | 是 |
| speed | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let isExist = await driver.isComponentPresentWhenSwipe(ON.id('123'), { x: 100, y: 100 }, { x: 200, y: 200 }, 1000);
}
```

## knuckleKnock

```TypeScript
knuckleKnock(pointers: Array<Point>, times: number): Promise<void>
```

模拟指关节敲击屏幕操作。使用Promise异步回调。

> **说明：**
> 
> 若设备关闭了指关节手势&lt;!--RP4--&gt;&lt;!--RP4End--&gt;，则调用本接口返回17000005错误码。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-knuckleKnock(pointers: Array<Point>, times: int): Promise<void>--><!--Device-Driver-knuckleKnock(pointers: Array<Point>, times: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pointers | Array&lt;[Point](arkts-test-uitest-point-i.md)&gt; | 是 |
| times | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |
| [17000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000005-操作不支持) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, Point } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // 模拟指关节单指双击手势。
  let points: Array<Point> = [{ x: 100, y: 100 }];
  await driver.knuckleKnock(points, 2);
}
```

## longClick

```TypeScript
longClick(x: number, y: number): Promise<void>
```

在目标坐标点长按。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-longClick(x: int, y: int): Promise<void>--><!--Device-Driver-longClick(x: int, y: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.longClick(100, 100);
}
```

## longClickAt

```TypeScript
longClickAt(point: Point, duration?: number): Promise<void>
```

长按目标坐标点，支持指定长按时长。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-longClickAt(point: Point, duration?: int): Promise<void>--><!--Device-Driver-longClickAt(point: Point, duration?: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | 是 |
| duration | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.longClickAt({ x: 100, y: 100, displayId: 0 }, 1500);
}
```

## longClickAtWithOptions

```TypeScript
longClickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>
```

长按屏幕上的指定位置，可选择触摸设置。

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-longClickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>--><!--Device-Driver-longClickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | 是 |
| options | [TouchOptions](arkts-test-uitest-touchoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, TouchOptions } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let options: TouchOptions = {
    duration: 2000, // 长按持续2000ms。
    pressure: 0.8  // 触摸压力值。
  };
  // 在目标坐标点进行长按，并指定长按时长和触摸压力。
  await driver.longClickAtWithOptions({ x: 100, y: 100, displayId: 0 }, options);
}
```

## mouseClick

```TypeScript
mouseClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>
```

在指定坐标点注入鼠标点击动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标点击动作。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-mouseClick(p: Point, btnId: MouseButton, key1?: int, key2?: int): Promise<void>--><!--Device-Driver-mouseClick(p: Point, btnId: MouseButton, key1?: int, key2?: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | 是 |
| btnId | [MouseButton](arkts-test-uitest-mousebutton-e.md) | 是 |
| [key1](arkts-test-uitest-keyoptions-i.md) | number | 否 |
| [key2](arkts-test-uitest-keyoptions-i.md) | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, MouseButton } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseClick({ x: 248, y: 194 }, MouseButton.MOUSE_BUTTON_LEFT, 2072);
}
```

## mouseDoubleClick

```TypeScript
mouseDoubleClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>
```

在指定坐标点注入鼠标双击动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标双击动作。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-mouseDoubleClick(p: Point, btnId: MouseButton, key1?: int, key2?: int): Promise<void>--><!--Device-Driver-mouseDoubleClick(p: Point, btnId: MouseButton, key1?: int, key2?: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | 是 |
| btnId | [MouseButton](arkts-test-uitest-mousebutton-e.md) | 是 |
| [key1](arkts-test-uitest-keyoptions-i.md) | number | 否 |
| [key2](arkts-test-uitest-keyoptions-i.md) | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, MouseButton } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseDoubleClick({ x: 248, y: 194 }, MouseButton.MOUSE_BUTTON_LEFT, 2072);
}
```

## mouseDrag

```TypeScript
mouseDrag(from: Point, to: Point, speed?: number): Promise<void>
```

鼠标按住鼠标左键从起始坐标点拖拽至终点坐标点。使用Promise异步回调。对于 API version 26.0.0 之前的版本，该接口不支持鼠标跨屏拖拽操作，起始点与终点需属于同一屏幕，否则将抛出401错误码；从 API version 26.0.0 开始，该接口支持鼠标跨屏拖拽操作。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-mouseDrag(from: Point, to: Point, speed?: number): Promise<void>--><!--Device-Driver-mouseDrag(from: Point, to: Point, speed?: number): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | 是 |
| to | [Point](arkts-test-uitest-point-i.md) | 是 |
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

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseDrag({ x: 100, y: 100 }, { x: 200, y: 200 }, 600);
}
```

## mouseDrag

```TypeScript
mouseDrag(from: Point, to: Point, speed?: number, duration?: number): Promise<void>
```

鼠标按住鼠标左键从起始坐标点拖拽至终点坐标点，支持指定拖拽速度和拖拽前长按时间。使用Promise异步回调。对于 API version 26.0.0 之前的版本，该接口不支持鼠标跨屏拖拽操作，起始点与终点需属于同一屏幕，否则将抛出401错误码；从 API version 26.0.0 开始，该接口支持鼠标跨屏拖拽操作。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-mouseDrag(from: Point, to: Point, speed?: int, duration?: int): Promise<void>--><!--Device-Driver-mouseDrag(from: Point, to: Point, speed?: int, duration?: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | 是 |
| to | [Point](arkts-test-uitest-point-i.md) | 是 |
| speed | number | 否 |
| duration | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseDrag({ x: 100, y: 100 }, { x: 200, y: 200 }, 600, 2000);
}
```

## mouseDragWithOptions

```TypeScript
mouseDragWithOptions(from: Point, to: Point, touchOptions?: TouchOptions, keyOptions?: KeyOptions): Promise<void>
```

按住鼠标左键并在屏幕上的指定点之间拖动，具有可选的触摸和按键设置。

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-mouseDragWithOptions(from: Point, to: Point, touchOptions?: TouchOptions, keyOptions?: KeyOptions): Promise<void>--><!--Device-Driver-mouseDragWithOptions(from: Point, to: Point, touchOptions?: TouchOptions, keyOptions?: KeyOptions): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | 是 |
| to | [Point](arkts-test-uitest-point-i.md) | 是 |
| touchOptions | [TouchOptions](arkts-test-uitest-touchoptions-i.md) | 否 |
| keyOptions | [KeyOptions](arkts-test-uitest-keyoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, TouchOptions, KeyOptions } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let touchOptions: TouchOptions = {
    speed: 800,     // 拖拽速率800px/s。
    duration: 2000  // 拖拽前长按2000ms。
  };
  let keyOptions: KeyOptions = {
    key1: 2072,  // Ctrl键。
    key2: 2019   // C键。
  };
  // 鼠标拖拽并同时按下Ctrl+C组合键。
  await driver.mouseDragWithOptions({ x: 100, y: 100 }, { x: 200, y: 200 }, touchOptions, keyOptions);
}
```

## mouseLongClick

```TypeScript
mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>
```

在指定坐标点注入鼠标长按动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标长按动作。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>--><!--Device-Driver-mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | 是 |
| btnId | [MouseButton](arkts-test-uitest-mousebutton-e.md) | 是 |
| [key1](arkts-test-uitest-keyoptions-i.md) | number | 否 |
| [key2](arkts-test-uitest-keyoptions-i.md) | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, MouseButton } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // 键码值为2072时，按下Ctrl并进行鼠标长按动作。
  await driver.mouseLongClick({ x: 248, y: 194 }, MouseButton.MOUSE_BUTTON_LEFT, 2072);
}
```

## mouseLongClick

```TypeScript
mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number, duration?: number): Promise<void>
```

在指定坐标点注入鼠标长按动作，支持同时按下对应键盘组合键，支持指定长按时长。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标长按动作。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-mouseLongClick(p: Point, btnId: MouseButton, key1?: int, key2?: int, duration?: int): Promise<void>--><!--Device-Driver-mouseLongClick(p: Point, btnId: MouseButton, key1?: int, key2?: int, duration?: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | 是 |
| btnId | [MouseButton](arkts-test-uitest-mousebutton-e.md) | 是 |
| [key1](arkts-test-uitest-keyoptions-i.md) | number | 否 |
| [key2](arkts-test-uitest-keyoptions-i.md) | number | 否 |
| duration | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, MouseButton } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // 键码值为2072时，按下Ctrl并进行鼠标长按动作，长按时长2000ms。
  await driver.mouseLongClick({ x: 248, y: 194 }, MouseButton.MOUSE_BUTTON_LEFT, 2072, 0, 2000);
}
```

## mouseMoveTo

```TypeScript
mouseMoveTo(p: Point): Promise<void>
```

将鼠标光标移到目标点。使用Promise异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-mouseMoveTo(p: Point): Promise<void>--><!--Device-Driver-mouseMoveTo(p: Point): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseMoveTo({ x: 100, y: 100 });
}
```

## mouseMoveWithTrack

```TypeScript
mouseMoveWithTrack(from: Point, to: Point, speed?: number): Promise<void>
```

鼠标从起始坐标点滑向终点坐标点。使用Promise异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-mouseMoveWithTrack(from: Point, to: Point, speed?: int): Promise<void>--><!--Device-Driver-mouseMoveWithTrack(from: Point, to: Point, speed?: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | 是 |
| to | [Point](arkts-test-uitest-point-i.md) | 是 |
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

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseMoveWithTrack({ x: 100, y: 100 }, { x: 200, y: 200 }, 600);
}
```

## mouseScroll

```TypeScript
mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number): Promise<void>
```

在指定坐标点注入鼠标滚轮滑动动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标滚轮滑动动作。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number): Promise<void>--><!--Device-Driver-mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | 是 |
| down | boolean | 是 |
| [d](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | number | 是 |
| [key1](arkts-test-uitest-keyoptions-i.md) | number | 否 |
| [key2](arkts-test-uitest-keyoptions-i.md) | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseScroll({ x: 360, y: 640 }, true, 30, 2072);
}
```

## mouseScroll

```TypeScript
mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number, speed?: number): Promise<void>
```

在指定坐标点注入鼠标滚轮滑动动作，支持同时按下对应键盘组合键并且指定滑动速度。使用Promise异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-mouseScroll(p: Point, down: boolean, d: int, key1?: int, key2?: int, speed?: int): Promise<void>--><!--Device-Driver-mouseScroll(p: Point, down: boolean, d: int, key1?: int, key2?: int, speed?: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | 是 |
| down | boolean | 是 |
| [d](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | number | 是 |
| [key1](arkts-test-uitest-keyoptions-i.md) | number | 否 |
| [key2](arkts-test-uitest-keyoptions-i.md) | number | 否 |
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

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseScroll({ x: 360, y: 640 }, true, 30, 2072, 20);
}
```

## penClick

```TypeScript
penClick(point: Point): Promise<void>
```

模拟手写笔点击操作。使用Promise异步回调。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-penClick(point: Point): Promise<void>--><!--Device-Driver-penClick(point: Point): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.penClick({ x: 100, y: 100 });
}
```

## penDoubleClick

```TypeScript
penDoubleClick(point: Point): Promise<void>
```

模拟手写笔双击操作。使用Promise异步回调。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-penDoubleClick(point: Point): Promise<void>--><!--Device-Driver-penDoubleClick(point: Point): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.penDoubleClick({ x: 100, y: 100 });
}
```

## penLongClick

```TypeScript
penLongClick(point: Point, pressure?: number): Promise<void>
```

模拟手写笔长按操作。使用Promise异步回调。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-penLongClick(point: Point, pressure?: double): Promise<void>--><!--Device-Driver-penLongClick(point: Point, pressure?: double): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | 是 |
| pressure | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.penLongClick({ x: 100, y: 100 }, 0.5);
}
```

## penSwipe

```TypeScript
penSwipe(startPoint: Point, endPoint: Point, speed?: number, pressure?: number): Promise<void>
```

模拟手写笔的滑动操作。使用Promise异步回调。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-penSwipe(startPoint: Point, endPoint: Point, speed?: int, pressure?: double): Promise<void>--><!--Device-Driver-penSwipe(startPoint: Point, endPoint: Point, speed?: int, pressure?: double): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| startPoint | [Point](arkts-test-uitest-point-i.md) | 是 |
| endPoint | [Point](arkts-test-uitest-point-i.md) | 是 |
| speed | number | 否 |
| pressure | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.penSwipe({ x: 100, y: 100 }, { x: 100, y: 500 }, 600, 0.5);
}
```

## pressBack

```TypeScript
pressBack(): Promise<void>
```

进行点击BACK键的操作。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-pressBack(): Promise<void>--><!--Device-Driver-pressBack(): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.pressBack();
}
```

## pressBack

```TypeScript
pressBack(displayId: number): Promise<void>
```

对指定屏幕进行点击BACK键的操作。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-pressBack(displayId: int): Promise<void>--><!--Device-Driver-pressBack(displayId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.pressBack(0);
}
```

## pressHome

```TypeScript
pressHome(): Promise<void>
```

设备注入返回桌面操作。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-pressHome(): Promise<void>--><!--Device-Driver-pressHome(): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.pressHome();
}
```

## pressHome

```TypeScript
pressHome(displayId: number): Promise<void>
```

设备指定屏幕上注入返回桌面操作。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-pressHome(displayId: int): Promise<void>--><!--Device-Driver-pressHome(displayId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.pressHome(0);
}
```

## screenCap

```TypeScript
screenCap(savePath: string): Promise<boolean>
```

捕获当前屏幕，并保存为PNG格式的图片至给出的保存路径中。使用Promise异步回调。适用于支持截屏的场景。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-screenCap(savePath: string): Promise<boolean>--><!--Device-Driver-screenCap(savePath: string): Promise<boolean>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| savePath | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.screenCap('/data/storage/el2/base/cache/1.png');
}
```

## screenCap

```TypeScript
screenCap(savePath: string, displayId: number): Promise<boolean>
```

捕获指定屏幕，并保存为PNG格式的图片至给出的保存路径中。使用Promise异步回调。适用于支持截屏的场景。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-screenCap(savePath: string, displayId: int): Promise<boolean>--><!--Device-Driver-screenCap(savePath: string, displayId: int): Promise<boolean>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| savePath | string | 是 |
| displayId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.screenCap('/data/storage/el2/base/cache/1.png', 0);
}
```

## screenCapture

```TypeScript
screenCapture(savePath: string, rect?: Rect): Promise<boolean>
```

捕获当前屏幕的指定区域，并保存为PNG格式的图片至给出的保存路径中。使用Promise异步回调。适用于支持截屏的场景。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-screenCapture(savePath: string, rect?: Rect): Promise<boolean>--><!--Device-Driver-screenCapture(savePath: string, rect?: Rect): Promise<boolean>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| savePath | string | 是 |
| rect | [Rect](arkts-test-uitest-rect-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.screenCapture('/data/storage/el2/base/cache/1.png', {
    left: 0,
    top: 0,
    right: 100,
    bottom: 100
  });
}
```

## setDisplayRotation

```TypeScript
setDisplayRotation(rotation: DisplayRotation): Promise<void>
```

将当前场景的显示方向设置为指定的显示方向。使用Promise异步回调。适用于可旋转的应用场景。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-setDisplayRotation(rotation: DisplayRotation): Promise<void>--><!--Device-Driver-setDisplayRotation(rotation: DisplayRotation): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rotation | [DisplayRotation](arkts-test-uitest-displayrotation-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, DisplayRotation } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.setDisplayRotation(DisplayRotation.ROTATION_180);
}
```

## setDisplayRotationEnabled

```TypeScript
setDisplayRotationEnabled(enabled: boolean): Promise<void>
```

启用/禁用设备旋转屏幕的功能。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-setDisplayRotationEnabled(enabled: boolean): Promise<void>--><!--Device-Driver-setDisplayRotationEnabled(enabled: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.setDisplayRotationEnabled(false);
}
```

## swipe

```TypeScript
swipe(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>
```

从起始坐标点滑向目的坐标点。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-swipe(startx: int, starty: int, endx: int, endy: int, speed?: int): Promise<void>--><!--Device-Driver-swipe(startx: int, starty: int, endx: int, endy: int, speed?: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| startx | number | 是 |
| starty | number | 是 |
| endx | number | 是 |
| endy | number | 是 |
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

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  // 创建Driver对象。
  let driver: Driver = Driver.create();
  // 从坐标(100,100)滑动到坐标(200,200)，滑动速率为600px/s。
  await driver.swipe(100, 100, 200, 200, 600);
}
```

## swipeBetween

```TypeScript
swipeBetween(from: Point, to: Point, speed?: number): Promise<void>
```

从起始坐标点滑向目标坐标点。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-swipeBetween(from: Point, to: Point, speed?: int): Promise<void>--><!--Device-Driver-swipeBetween(from: Point, to: Point, speed?: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | 是 |
| to | [Point](arkts-test-uitest-point-i.md) | 是 |
| speed | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.swipeBetween({ x: 100, y: 100, displayId: 0 }, { x: 1000, y: 1000, displayId: 0 }, 800);
}
```

## swipeBetweenWithOptions

```TypeScript
swipeBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>
```

使用可选的触摸选项在指定点之间滑动屏幕。

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-swipeBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>--><!--Device-Driver-swipeBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | 是 |
| to | [Point](arkts-test-uitest-point-i.md) | 是 |
| options | [TouchOptions](arkts-test-uitest-touchoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, TouchOptions } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let options: TouchOptions = {
    speed: 800,   // 滑动速率800px/s。
    pressure: 0.5  // 触摸压力值。
  };
  // 从起始坐标点滑向目标坐标点，并指定滑动速率和触摸压力。
  await driver.swipeBetweenWithOptions({ x: 100, y: 100, displayId: 0 }, { x: 1000, y: 1000, displayId: 0 }, options);
}
```

## touchPadMultiFingerSwipe

```TypeScript
touchPadMultiFingerSwipe(fingers: number, direction: UiDirection, options?: TouchPadSwipeOptions): Promise<void>
```

模拟触摸板多指滑动手势。使用Promise异步回调。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-touchPadMultiFingerSwipe(fingers: int, direction: UiDirection, options?: TouchPadSwipeOptions): Promise<void>--><!--Device-Driver-touchPadMultiFingerSwipe(fingers: int, direction: UiDirection, options?: TouchPadSwipeOptions): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fingers | number | 是 |
| direction | [UiDirection](arkts-test-uitest-uidirection-e.md) | 是 |
| options | [TouchPadSwipeOptions](arkts-test-uitest-touchpadswipeoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000005-操作不支持) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, UiDirection } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.touchPadMultiFingerSwipe(3, UiDirection.UP);
}
```

## touchPadTwoFingersScroll

```TypeScript
touchPadTwoFingersScroll(point: Point, direction: UiDirection, d: number, speed?: number): Promise<void>
```

模拟触摸板双指滚动手势。使用Promise异步回调。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-touchPadTwoFingersScroll(point: Point, direction: UiDirection, d: int, speed?: int): Promise<void>--><!--Device-Driver-touchPadTwoFingersScroll(point: Point, direction: UiDirection, d: int, speed?: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | 是 |
| direction | [UiDirection](arkts-test-uitest-uidirection-e.md) | 是 |
| [d](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | number | 是 |
| speed | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |
| [17000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000005-操作不支持) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, UiDirection } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.touchPadTwoFingersScroll({ x: 100, y: 100 }, UiDirection.UP, 20, 10);
}
```

## triggerCombineKeys

```TypeScript
triggerCombineKeys(key0: number, key1: number, key2?: number): Promise<void>
```

通过给定的key值，找到对应组合键并点击。使用Promise异步回调。例如，Key值为(2072, 2019)时，找到key值对应的组合键并点击，如Ctrl+c。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-triggerCombineKeys(key0: number, key1: number, key2?: number): Promise<void>--><!--Device-Driver-triggerCombineKeys(key0: number, key1: number, key2?: number): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key0 | number | 是 |
| [key1](arkts-test-uitest-keyoptions-i.md) | number | 是 |
| [key2](arkts-test-uitest-keyoptions-i.md) | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // 注入Ctrl+Alt+Delete组合键。
  await driver.triggerCombineKeys(2072, 2047, 2035);
}
```

## triggerCombineKeys

```TypeScript
triggerCombineKeys(key0: number, key1: number, key2?: number, displayId?: number): Promise<void>
```

通过给定的key值，找到对应组合键，并在指定屏幕下进行点击。使用Promise异步回调。例如，Key值为(2072, 2019)时，找到key值对应的组合键并点击，如Ctrl+c。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-triggerCombineKeys(key0: int, key1: int, key2?: int, displayId?: int): Promise<void>--><!--Device-Driver-triggerCombineKeys(key0: int, key1: int, key2?: int, displayId?: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key0 | number | 是 |
| [key1](arkts-test-uitest-keyoptions-i.md) | number | 是 |
| [key2](arkts-test-uitest-keyoptions-i.md) | number | 否 |
| displayId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.triggerCombineKeys(2072, 2047, 2035, 0);
}
```

## triggerKey

```TypeScript
triggerKey(keyCode: number): Promise<void>
```

传入key值实现模拟点击对应按键的效果。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-triggerKey(keyCode: int): Promise<void>--><!--Device-Driver-triggerKey(keyCode: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyCode | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';
import { KeyCode } from '@kit.InputKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.triggerKey(KeyCode.KEYCODE_BACK); // 返回键。
}
```

## triggerKey

```TypeScript
triggerKey(keyCode: number, displayId: number): Promise<void>
```

在指定屏幕，传入key值实现模拟点击对应按键的效果。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-triggerKey(keyCode: int, displayId: int): Promise<void>--><!--Device-Driver-triggerKey(keyCode: int, displayId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyCode | number | 是 |
| displayId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';
import { KeyCode } from '@kit.InputKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.triggerKey(KeyCode.KEYCODE_BACK, 0); // 返回键。
}
```

## triggerPenKey

```TypeScript
triggerPenKey(key: PenKey, mode: PenMode, operation: PenKeyOperation, options?: PenKeyOperationOptions): Promise<void>
```

Trigger pen key operation.

Supported combinations:

- HANDWRITING mode: HANDWRITING key with CLICK or DOUBLE_CLICK operation.  
- AIR_MOUSE mode: AIR_MOUSE key with CLICK or DOUBLE_CLICK operation (requires point in options),  
HANDWRITING key with CLICK or DOUBLE_CLICK operation, SMART key with CLICK operation.Other combinations will result in a BusinessError 17000007.

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-triggerPenKey(key: PenKey, mode: PenMode, operation: PenKeyOperation, options?: PenKeyOperationOptions): Promise<void>--><!--Device-Driver-triggerPenKey(key: PenKey, mode: PenMode, operation: PenKeyOperation, options?: PenKeyOperationOptions): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | [PenKey](arkts-test-uitest-penkey-e.md) | 是 |
| mode | [PenMode](arkts-test-uitest-penmode-e.md) | 是 |
| operation | [PenKeyOperation](arkts-test-uitest-penkeyoperation-e.md) | 是 |
| options | [PenKeyOperationOptions](arkts-test-uitest-penkeyoperationoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000007-参数不合法) |
| [17000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000005-操作不支持) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver, PenKey, PenMode, PenKeyOperation } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // 手写模式下触发手写键单击。
  await driver.triggerPenKey(PenKey.HANDWRITING, PenMode.HANDWRITING, PenKeyOperation.CLICK);
  // 空鼠模式下触发空鼠键双击。
  await driver.triggerPenKey(PenKey.AIR_MOUSE, PenMode.AIR_MOUSE, PenKeyOperation.DOUBLE_CLICK, { point: { x: 500, y: 500 } });
  // 空鼠模式下触发智慧键单击。
  await driver.triggerPenKey(PenKey.SMART, PenMode.AIR_MOUSE, PenKeyOperation.CLICK);
}
```

## waitForComponent

```TypeScript
waitForComponent(on: On, time: number): Promise<Component>
```

在用户给定的时间内，持续查找满足控件属性要求的目标控件。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-waitForComponent(on: On, time: number): Promise<Component>--><!--Device-Driver-waitForComponent(on: On, time: number): Promise<Component>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | 是 |
| time | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Component](arkts-test-uitest-component-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.waitForComponent(ON.text('next page'), 500);
}
```

## waitForIdle

```TypeScript
waitForIdle(idleTime: number, timeout: number): Promise<boolean>
```

判断当前界面的所有控件是否已经空闲。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-waitForIdle(idleTime: int, timeout: int): Promise<boolean>--><!--Device-Driver-waitForIdle(idleTime: int, timeout: int): Promise<boolean>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| idleTime | number | 是 |
| timeout | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let idled: boolean = await driver.waitForIdle(4000, 5000);
}
```

## wakeUpDisplay

```TypeScript
wakeUpDisplay(): Promise<void>
```

唤醒当前设备即设备亮屏。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Driver-wakeUpDisplay(): Promise<void>--><!--Device-Driver-wakeUpDisplay(): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-test-kit/errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.wakeUpDisplay();
}
```
