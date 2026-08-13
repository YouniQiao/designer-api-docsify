# UiDriver

UiDriver类为uitest测试框架的总入口，提供控件匹配/查找，按键注入，坐标点击/滑动，截图等API。 该类提供的方法除UiDriver.create()以外的所有方法都使用Promise方式作为异步方法，需使用await调用。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[Driver&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-driver-c.md#Driver)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [Driver](arkts-test-uitest-driver-c.md#Driver)

<!--Device-unnamed-declare class UiDriver--><!--Device-unnamed-declare class UiDriver-End-->

**系统能力：** SystemCapability.Test.UiTest

## assertComponentExist

```TypeScript
assertComponentExist(by: By): Promise<void>
```

断言API，用于断言当前界面存在满足给出的目标控件属性的控件；如果控件不存在，该API将抛出JS异常，使当前测试用例失败。使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[assertComponentExist&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-driver-c.md#assertComponentExist)替 > 代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [assertComponentExist](arkts-test-uitest-driver-c.md#assertComponentExist)

<!--Device-UiDriver-assertComponentExist(by: By): Promise<void>--><!--Device-UiDriver-assertComponentExist(by: By): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| by | [By](arkts-test-uitest-by-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000003](../errorcode-uitest.md#17000003-断言失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## 示例

```TypeScript
// xxx.test.ets
import { UiDriver, BY } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.assertComponentExist(BY.text('next page'));
}
```

## click

```TypeScript
click(x: number, y: number): Promise<void>
```

UiDriver对象采取如下操作：在目标坐标点单击。使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[click&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#click)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [click](arkts-test-uitest-component-c.md#click)

<!--Device-UiDriver-click(x: number, y: number): Promise<void>--><!--Device-UiDriver-click(x: number, y: number): Promise<void>-End-->

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

## 示例

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.click(100, 100);
}
```

## create

```TypeScript
static create(): UiDriver
```

静态方法，构造一个UiDriver对象，并返回该对象。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[create&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-driver-c.md#create)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [create](arkts-test-uitest-driver-c.md#create)

<!--Device-UiDriver-static create(): UiDriver--><!--Device-UiDriver-static create(): UiDriver-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| [UiDriver](arkts-test-uitest-uidriver-c.md) |

## 示例

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
}
```

## delayMs

```TypeScript
delayMs(duration: number): Promise<void>
```

UiDriver对象在给定的时间内延时。使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[delayMs&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-driver-c.md#delayMs)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [delayMs](arkts-test-uitest-driver-c.md#delayMs)

<!--Device-UiDriver-delayMs(duration: number): Promise<void>--><!--Device-UiDriver-delayMs(duration: number): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| duration | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## 示例

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.delayMs(1000);
}
```

## doubleClick

```TypeScript
doubleClick(x: number, y: number): Promise<void>
```

UiDriver对象采取如下操作：在目标坐标点双击。使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[doubleClick&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#doubleClick)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [doubleClick](arkts-test-uitest-component-c.md#doubleClick)

<!--Device-UiDriver-doubleClick(x: number, y: number): Promise<void>--><!--Device-UiDriver-doubleClick(x: number, y: number): Promise<void>-End-->

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

## 示例

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.doubleClick(100, 100);
}
```

## findComponent

```TypeScript
findComponent(by: By): Promise<UiComponent>
```

在UiDriver对象中，根据给出的目标控件属性要求查找目标控件。使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[findComponent&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-driver-c.md#findComponent)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [findComponent](arkts-test-uitest-driver-c.md#findComponent)(on: On)

<!--Device-UiDriver-findComponent(by: By): Promise<UiComponent>--><!--Device-UiDriver-findComponent(by: By): Promise<UiComponent>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| by | [By](arkts-test-uitest-by-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[UiComponent](arkts-test-uitest-uicomponent-c.md)&gt; |

## 示例

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.text('next page'));
}
```

## findComponents

```TypeScript
findComponents(by: By): Promise<Array<UiComponent>>
```

在UiDriver对象中，根据给出的目标控件属性要求查找出所有匹配控件，以列表保存。使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[findComponents&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-driver-c.md#findComponents)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [findComponents](arkts-test-uitest-driver-c.md#findComponents)(on: On)

<!--Device-UiDriver-findComponents(by: By): Promise<Array<UiComponent>>--><!--Device-UiDriver-findComponents(by: By): Promise<Array<UiComponent>>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| by | [By](arkts-test-uitest-by-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[UiComponent](arkts-test-uitest-uicomponent-c.md)&gt;&gt; |

## 示例

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let buttonList: Array<UiComponent> = await driver.findComponents(BY.text('next page'));
}
```

## longClick

```TypeScript
longClick(x: number, y: number): Promise<void>
```

UiDriver对象采取如下操作：在目标坐标点长按下鼠标左键。使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[longClick&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-component-c.md#longClick)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [longClick](arkts-test-uitest-component-c.md#longClick)

<!--Device-UiDriver-longClick(x: number, y: number): Promise<void>--><!--Device-UiDriver-longClick(x: number, y: number): Promise<void>-End-->

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

## 示例

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.longClick(100, 100);
}
```

## pressBack

```TypeScript
pressBack(): Promise<void>
```

UiDriver对象进行点击BACK键的操作。使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[pressBack&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-driver-c.md#pressBack)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [pressBack](arkts-test-uitest-driver-c.md#pressBack)()

<!--Device-UiDriver-pressBack(): Promise<void>--><!--Device-UiDriver-pressBack(): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## 示例

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.pressBack();
}
```

## screenCap

```TypeScript
screenCap(savePath: string): Promise<boolean>
```

UiDriver对象采取如下操作：捕获当前屏幕，并保存为PNG格式的图片至给出的保存路径中。使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[screenCap&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-driver-c.md#screenCap)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [screenCap](arkts-test-uitest-driver-c.md#screenCap)(savePath: string)

<!--Device-UiDriver-screenCap(savePath: string): Promise<boolean>--><!--Device-UiDriver-screenCap(savePath: string): Promise<boolean>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| savePath | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## 示例

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.screenCap('/data/storage/el2/base/cache/1.png');
}
```

## swipe

```TypeScript
swipe(startx: number, starty: number, endx: number, endy: number): Promise<void>
```

UiDriver对象采取如下操作：从给出的起始坐标点滑向给出的目的坐标点。使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[swipe&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-driver-c.md#swipe)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [swipe](arkts-test-uitest-driver-c.md#swipe)

<!--Device-UiDriver-swipe(startx: number, starty: number, endx: number, endy: number): Promise<void>--><!--Device-UiDriver-swipe(startx: number, starty: number, endx: number, endy: number): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| startx | number | 是 |
| starty | number | 是 |
| endx | number | 是 |
| endy | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## 示例

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.swipe(100, 100, 200, 200);
}
```

## triggerKey

```TypeScript
triggerKey(keyCode: number): Promise<void>
```

UiDriver对象采取如下操作：通过key值找到对应键并点击。使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[triggerKey&lt;sup&gt;9+&lt;/sup&gt;](arkts-test-uitest-driver-c.md#triggerKey)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [triggerKey](arkts-test-uitest-driver-c.md#triggerKey)(keyCode: int)

<!--Device-UiDriver-triggerKey(keyCode: number): Promise<void>--><!--Device-UiDriver-triggerKey(keyCode: number): Promise<void>-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyCode | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## 示例

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';
import { KeyCode } from '@kit.InputKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.triggerKey(KeyCode.KEYCODE_BACK); // 返回键。
}
```
