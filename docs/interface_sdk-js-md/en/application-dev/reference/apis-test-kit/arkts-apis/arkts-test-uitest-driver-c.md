# Driver

Driver类为uitest测试框架的总入口，提供控件匹配/查找，按键注入，坐标点击/滑动，截图等能力。通过{@link create}创建实例。该类提供的方法除Driver.create()和Driver.createUIEventObserver()以外的所有方法都使用Promise方式作为异步方法，需使用await方式调用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class Driver--><!--Device-unnamed-declare class Driver-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from 'kits/@kit.TestKit';
```

## assertComponentExist

```TypeScript
assertComponentExist(on: On): Promise<void>
```

断言API，用于断言当前界面是否存在满足给出的目标属性的控件。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-assertComponentExist(on: On): Promise<void>--><!--Device-Driver-assertComponentExist(on: On): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | 目标控件的属性要求。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000003 | Assertion failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.assertComponentExist(ON.text('next page'));
}
```

## click

ArkTS-Dyn:
```TypeScript
click(x: number, y: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
click(x: int, y: int): Promise<void>
```

在目标坐标点单击。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-click(x: int, y: int): Promise<void>--><!--Device-Driver-click(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  // Create a Driver object.
  let driver: Driver = Driver.create();
  // Perform a tap operation at the coordinate (100,100).
  await driver.click(100, 100);
}
```

## clickAt

```TypeScript
clickAt(point: Point): Promise<void>
```

在目标坐标点进行单击。使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Driver-clickAt(point: Point): Promise<void>--><!--Device-Driver-clickAt(point: Point): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 以Point对象的形式传入目标点信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |

## Examples

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

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Driver-clickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>--><!--Device-Driver-clickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 手指接触屏幕的坐标点。 |
| options | [TouchOptions](arkts-test-uitest-touchoptions-i.md) | No | 单击操作的选项。 只有''属性适用于此方法。 设置其他属性将导致BusinessError 17000007。 &lt;br&gt;默认值：参考TouchOptions的默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, TouchOptions } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let options: TouchOptions = {
    pressure: 0.5
  };
  // Clicks the target coordinate point and specifies the touch pressure.
  await driver.clickAtWithOptions({ x: 100, y: 100, displayId: 0 }, options);
}
```

## create

```TypeScript
static create(): Driver
```

静态方法，构造一个Driver对象，并返回该对象。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-static create(): Driver--><!--Device-Driver-static create(): Driver-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| [Driver](arkts-test-uitest-driver-c.md) | 返回构造的Driver对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000001 | Initialization failed. |

## Examples

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

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-createUIEventObserver(): UIEventObserver--><!--Device-Driver-createUIEventObserver(): UIEventObserver-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| [UIEventObserver](arkts-test-uitest-uieventobserver-i.md) | 返回找到的目标窗口对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UIEventObserver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let observer: UIEventObserver = driver.createUIEventObserver();
}
```

## crownRotate

ArkTS-Dyn:
```TypeScript
crownRotate(d: number, speed?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
crownRotate(d: int, speed?: int): Promise<void>
```

注入手表表冠旋转事件，可指定旋转速度。使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Driver-crownRotate(d: int, speed?: int): Promise<void>--><!--Device-Driver-crownRotate(d: int, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 手表表冠旋转的格数，正值表示顺时针旋转，负值表示逆时针旋转，取值需为整数。 |
| speed | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 手表表冠旋转的格数，正值表示顺时针旋转，负值表示逆时针旋转，取值需为整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // Rotate 50 ticks clockwise at a speed of 30 ticks per second.
  await driver.crownRotate(50, 30);
  // Rotate 20 ticks counterclockwise at a speed of 30 ticks per second.
  await driver.crownRotate(-20, 30);
}
```

## delayMs

ArkTS-Dyn:
```TypeScript
delayMs(duration: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
delayMs(duration: int): Promise<void>
```

在给定的时间内延时。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-delayMs(duration: int): Promise<void>--><!--Device-Driver-delayMs(duration: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| duration | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 给定的时间，单位：ms，取值范围：大于等于0的整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.delayMs(1000);
}
```

## doubleClick

ArkTS-Dyn:
```TypeScript
doubleClick(x: number, y: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
doubleClick(x: int, y: int): Promise<void>
```

在目标坐标点双击。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-doubleClick(x: int, y: int): Promise<void>--><!--Device-Driver-doubleClick(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

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

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Driver-doubleClickAt(point: Point): Promise<void>--><!--Device-Driver-doubleClickAt(point: Point): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 以Point对象的形式传入目标点信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.doubleClickAt({ x: 100, y: 100, displayId: 0 });
}
```

## drag

ArkTS-Dyn:
```TypeScript
drag(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
drag(startx: int, starty: int, endx: int, endy: int, speed?: int): Promise<void>
```

从起始坐标点拖拽至目的坐标点。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-drag(startx: int, starty: int, endx: int, endy: int, speed?: int): Promise<void>--><!--Device-Driver-drag(startx: int, starty: int, endx: int, endy: int, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startx | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 以number的形式传入起始点的横坐标信息，取值范围：大于等于0的整数。 |
| starty | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 以number的形式传入起始点的纵坐标信息，取值范围：大于等于0的整数。 |
| endx | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 以number的形式传入目的点的横坐标信息，取值范围：大于等于0的整数。 |
| endy | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 以number的形式传入目的点的纵坐标信息，取值范围：大于等于0的整数。 |
| speed | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.drag(100, 100, 200, 200, 600);
}
```

## dragBetween

ArkTS-Dyn:
```TypeScript
dragBetween(from: Point, to: Point, speed?: number, duration?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
dragBetween(from: Point, to: Point, speed?: int, duration?: int): Promise<void>
```

从起始坐标点拖拽至目标坐标点，支持指定拖拽速度和拖拽前长按时间。使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Driver-dragBetween(from: Point, to: Point, speed?: int, duration?: int): Promise<void>--><!--Device-Driver-dragBetween(from: Point, to: Point, speed?: int, duration?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 以Point对象的形式传入起始点的坐标信息和所属屏幕ID。 |
| to | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 以Point对象的形式传入终止点的坐标信息和所属屏幕ID。  **说明：** 应与起始点属于同一个屏幕，否则将抛出17000007异常。 |
| speed | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出17000007错 误码。 |
| duration | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 拖拽前长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。取值小于1500时抛出17000007错误码，为null或undefined时使用默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |

## Examples

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

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Driver-dragBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>--><!--Device-Driver-dragBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 手指接触屏幕的坐标点。 |
| to | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 手指离开屏幕的坐标点。 |
| options | [TouchOptions](arkts-test-uitest-touchoptions-i.md) | No | 拖动操作的选项。 只有“压力”、“速度”和“持续时间”属性适用于此方法。 设置其他属性将导致BusinessError 17000007。 &lt;br&gt;默认值：参考TouchOptions的默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, TouchOptions } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let options: TouchOptions = {
    speed: 800,     // Drag speed: 800 px/s
    duration: 2000, // Click duration before dragging: 2000 ms.
    pressure: 0.5   // Touch pressure value.
  };
  // Drag from the start coordinate point to the target coordinate point, and specify the drag speed, click duration, and touch pressure.
  await driver.dragBetweenWithOptions({ x: 100, y: 100, displayId: 0 }, { x: 1000, y: 1000, displayId: 0 }, options);
}
```

## dumpLayout

ArkTS-Dyn:
```TypeScript
dumpLayout(savePath: string, displayId?: number): Promise<boolean>
```

ArkTS-Sta:
```TypeScript
dumpLayout(savePath: string, displayId?: int): Promise<boolean>
```

Get the current layout information and save as file with json format.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Driver-dumpLayout(savePath: string, displayId?: int): Promise<boolean>--><!--Device-Driver-dumpLayout(savePath: string, displayId?: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| savePath | string | Yes | the path where to store the json, must be in the application sandbox directory. The path must be the [sandbox path](../../../file-management/app-sandbox-directory.md) of the current application. |
| displayId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | the Id of the specified display, default is the displayId of the main screen. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | true if dump layout and file-storing are completed successfully,false otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // Obtain the current layout information and save it as a JSON file.
  await driver.dumpLayout('/data/storage/el2/base/cache/layout.json', 0);
}
```

## findComponent

```TypeScript
findComponent(on: On): Promise<Component>
```

根据给出的目标控件属性要求查找目标控件。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-findComponent(on: On): Promise<Component>--><!--Device-Driver-findComponent(on: On): Promise<Component>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | 目标控件的属性要求。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Component&gt; | Promise对象，返回控件对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  // Create a Driver object.
  let driver: Driver = Driver.create();
  // Search for the component whose text is 'next page'.
  let button: Component = await driver.findComponent(ON.text('next page'));
}
```

## findComponent

```TypeScript
findComponent(on: On): Promise<Component | null>
```

Find the first matched {@link Component} on current UI.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Driver-findComponent(on: On): Promise<Component | null>--><!--Device-Driver-findComponent(on: On): Promise<Component | null>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | the attribute requirements of the target {@link Component}. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Component \| null&gt; | the first matched { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## findComponents

```TypeScript
findComponents(on: On): Promise<Array<Component>>
```

根据给出的目标控件属性要求查找出所有匹配控件，以列表保存。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-findComponents(on: On): Promise<Array<Component>>--><!--Device-Driver-findComponents(on: On): Promise<Array<Component>>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | 目标控件的属性要求。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;Component&gt;&gt; | Promise对象，返回控件对象的列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  // Create a Driver object.
  let driver: Driver = Driver.create();
  // Search for all components whose text is 'next page'.
  let buttonList: Array<Component> = await driver.findComponents(ON.text('next page'));
}
```

## findComponents

```TypeScript
findComponents(on: On): Promise<Array<Component> | null>
```

Find all the matched {@link Component}s on current UI.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Driver-findComponents(on: On): Promise<Array<Component> | null>--><!--Device-Driver-findComponents(on: On): Promise<Array<Component> | null>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | the attribute requirements of the target {@link Component}. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;Component&gt; \| null&gt; | the matched { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## findWindow

```TypeScript
findWindow(filter: WindowFilter): Promise<UiWindow>
```

通过指定窗口的属性来查找目标窗口。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-findWindow(filter: WindowFilter): Promise<UiWindow>--><!--Device-Driver-findWindow(filter: WindowFilter): Promise<UiWindow>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | [WindowFilter](arkts-test-uitest-windowfilter-i.md) | Yes | 目标窗口的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;UiWindow&gt; | Promise对象，返回目标窗口对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ active: true });
}
```

## findWindow

```TypeScript
findWindow(filter: WindowFilter): Promise<UiWindow | null>
```

Find the first matched {@link UiWindow} window.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Driver-findWindow(filter: WindowFilter): Promise<UiWindow | null>--><!--Device-Driver-findWindow(filter: WindowFilter): Promise<UiWindow | null>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | [WindowFilter](arkts-test-uitest-windowfilter-i.md) | Yes | the filter condition of the target {@link UiWindow}. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;UiWindow \| null&gt; | the first matched { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## fling

ArkTS-Dyn:
```TypeScript
fling(from: Point, to: Point, stepLen: number, speed: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
fling(from: Point, to: Point, stepLen: int, speed: int): Promise<void>
```

模拟手指滑动后脱离屏幕的快速滑动操作。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-fling(from: Point, to: Point, stepLen: int, speed: int): Promise<void>--><!--Device-Driver-fling(from: Point, to: Point, stepLen: int, speed: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 手指接触屏幕的起始点坐标。 |
| to | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 手指离开屏幕时的坐标点。 |
| stepLen | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 间隔距离，取值大于等于0的整数，单位：px。 |
| speed | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数时设为默认值600。为负数时抛出401错误码。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.fling({ x: 500, y: 480 }, { x: 450, y: 480 }, 5, 600);
}
```

## fling

ArkTS-Dyn:
```TypeScript
fling(direction: UiDirection, speed: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
fling(direction: UiDirection, speed: int): Promise<void>
```

指定方向和滑动速率，模拟手指滑动后脱离屏幕的快速滑动操作。使用Promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-fling(direction: UiDirection, speed: int): Promise<void>--><!--Device-Driver-fling(direction: UiDirection, speed: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| direction | [UiDirection](arkts-test-uitest-uidirection-e.md) | Yes | 进行抛滑的方向。 |
| speed | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数时设为默认值600。为负数时抛出401错误码。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiDirection } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.fling(UiDirection.DOWN, 10000);
}
```

## fling

ArkTS-Dyn:
```TypeScript
fling(direction: UiDirection, speed: number, displayId: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
fling(direction: UiDirection, speed: int, displayId: int): Promise<void>
```

指定方向、滑动速率和操作屏幕，模拟手指滑动后脱离屏幕的快速滑动操作。使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Driver-fling(direction: UiDirection, speed: int, displayId: int): Promise<void>--><!--Device-Driver-fling(direction: UiDirection, speed: int, displayId: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| direction | [UiDirection](arkts-test-uitest-uidirection-e.md) | Yes | 进行抛滑的方向。 |
| speed | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 滑动速率，取值范围为200-40000，默认值为600，单位：px/s。为不在范围内的非负数时设为默认值600。为负数时抛出401错误码。 |
| displayId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定设备屏幕ID。取值范围：大于等于0的整数。 **说明：** 传入displayId不存在时，将抛出17000007异常。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-getDisplayDensity(): Promise<Point>--><!--Device-Driver-getDisplayDensity(): Promise<Point>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Point&gt; | Promise对象，返回Point对象，当前设备屏幕的分辨率为Point.x*Point.y。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let density = await driver.getDisplayDensity();
}
```

## getDisplayDensity

ArkTS-Dyn:
```TypeScript
getDisplayDensity(displayId: number): Promise<Point>
```

ArkTS-Sta:
```TypeScript
getDisplayDensity(displayId: int): Promise<Point>
```

获取当前设备指定屏幕的分辨率。使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Driver-getDisplayDensity(displayId: int): Promise<Point>--><!--Device-Driver-getDisplayDensity(displayId: int): Promise<Point>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定设备屏幕ID。取值范围：大于等于0的整数。  **说明：** 传入displayId不存在时，将抛出17000007异常。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Point&gt; | Promise对象，返回Point对象，当前设备指定屏幕的分辨率为Point.x*Point.y。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-getDisplayRotation(): Promise<DisplayRotation>--><!--Device-Driver-getDisplayRotation(): Promise<DisplayRotation>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DisplayRotation&gt; | Promise对象，返回当前设备的显示方向。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { DisplayRotation, Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let rotation: DisplayRotation = await driver.getDisplayRotation();
}
```

## getDisplayRotation

ArkTS-Dyn:
```TypeScript
getDisplayRotation(displayId: number): Promise<DisplayRotation>
```

ArkTS-Sta:
```TypeScript
getDisplayRotation(displayId: int): Promise<DisplayRotation>
```

获取当前设备指定屏幕的显示方向。使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Driver-getDisplayRotation(displayId: int): Promise<DisplayRotation>--><!--Device-Driver-getDisplayRotation(displayId: int): Promise<DisplayRotation>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定设备屏幕ID。取值范围：大于等于0的整数。  **说明：** 传入displayId不存在时，将抛出17000007异常。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DisplayRotation&gt; | Promise对象，返回指定屏幕的显示方向。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-getDisplaySize(): Promise<Point>--><!--Device-Driver-getDisplaySize(): Promise<Point>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Point&gt; | Promise对象，返回Point对象，当前设备屏幕的大小为Point.x Point.y。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let size = await driver.getDisplaySize();
}
```

## getDisplaySize

ArkTS-Dyn:
```TypeScript
getDisplaySize(displayId: number): Promise<Point>
```

ArkTS-Sta:
```TypeScript
getDisplaySize(displayId: int): Promise<Point>
```

获取当前设备指定屏幕的大小。使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Driver-getDisplaySize(displayId: int): Promise<Point>--><!--Device-Driver-getDisplaySize(displayId: int): Promise<Point>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定设备屏幕ID。取值范围：大于等于0的整数。 **说明：** 传入displayId不存在时，将抛出17000007异常。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Point&gt; | Promise对象，返回Point对象，当前设备指定屏幕的大小为Point.x Point.y。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let size = await driver.getDisplaySize(0);
}
```

## injectKnucklePointerAction

ArkTS-Dyn:
```TypeScript
injectKnucklePointerAction(pointers: PointerMatrix, speed?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
injectKnucklePointerAction(pointers: PointerMatrix, speed?: int): Promise<void>
```

模拟指关节多点注入滑动操作。使用Promise异步回调。

> **说明：**
> 
> 若设备关闭了指关节手势&lt;!--RP4--&gt;&lt;!--RP4End--&gt;，则调用本接口返回17000005错误码。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Driver-injectKnucklePointerAction(pointers: PointerMatrix, speed?: int): Promise<void>--><!--Device-Driver-injectKnucklePointerAction(pointers: PointerMatrix, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pointers | [PointerMatrix](arkts-test-uitest-pointermatrix-c.md) | Yes | 滑动轨迹，包括操作手指个数和滑动坐标序列。  **说明：**当前仅支持单指操作，PointerMatrix中的操作手指个数fingers必须设置为1。 |
| speed | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出17000007错 误码。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |
| 17000005 | This operation is not supported. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, PointerMatrix } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // Simulate a knuckle gesture to draw an S on the display.
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

ArkTS-Dyn:
```TypeScript
injectMultiPointerAction(pointers: PointerMatrix, speed?: number): Promise<boolean>
```

ArkTS-Sta:
```TypeScript
injectMultiPointerAction(pointers: PointerMatrix, speed?: int): Promise<boolean>
```

向设备注入多指操作。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-injectMultiPointerAction(pointers: PointerMatrix, speed?: int): Promise<boolean>--><!--Device-Driver-injectMultiPointerAction(pointers: PointerMatrix, speed?: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pointers | [PointerMatrix](arkts-test-uitest-pointermatrix-c.md) | Yes | 滑动轨迹，包括操作手指个数和滑动坐标序列。 |
| speed | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回操作是否成功完成。true：完成，false：未完成。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, PointerMatrix } from '@kit.TestKit';

async function demo() {
  // Create a Driver object.
  let driver: Driver = Driver.create();
  // Create a 2-finger 5-step sliding track matrix.
  let pointers: PointerMatrix = PointerMatrix.create(2, 5);
  // Set the sliding track of the first finger.
  pointers.setPoint(0, 0, { x: 250, y: 480 });
  pointers.setPoint(0, 1, { x: 250, y: 440 });
  pointers.setPoint(0, 2, { x: 250, y: 400 });
  pointers.setPoint(0, 3, { x: 250, y: 360 });
  pointers.setPoint(0, 4, { x: 250, y: 320 });
  // Set the sliding track of the second finger.
  pointers.setPoint(1, 0, { x: 250, y: 480 });
  pointers.setPoint(1, 1, { x: 250, y: 440 });
  pointers.setPoint(1, 2, { x: 250, y: 400 });
  pointers.setPoint(1, 3, { x: 250, y: 360 });
  pointers.setPoint(1, 4, { x: 250, y: 320 });
  // Inject the two-finger sliding operation.
  await driver.injectMultiPointerAction(pointers);
}
```

## injectPenPointerAction

ArkTS-Dyn:
```TypeScript
injectPenPointerAction(pointers: PointerMatrix, speed?: number, pressure?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
injectPenPointerAction(pointers: PointerMatrix, speed?: int, pressure?: double): Promise<void>
```

模拟手写笔多点连续注入操作。使用Promise异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Driver-injectPenPointerAction(pointers: PointerMatrix, speed?: int, pressure?: double): Promise<void>--><!--Device-Driver-injectPenPointerAction(pointers: PointerMatrix, speed?: int, pressure?: double): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pointers | [PointerMatrix](arkts-test-uitest-pointermatrix-c.md) | Yes | 滑动轨迹，包括操作手指个数和滑动坐标序列。  **说明：**当前仅支持单指操作，PointerMatrix中的操作手指个数fingers必须设置为1。 |
| speed | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |
| pressure | ArkTS-Dyn: number  <br>ArkTS-Sta：double | No | 手写笔多点连续注入的压力，默认为1.0，取值范围为0.0到1.0。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，返回无结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, PointerMatrix } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // Create a single-finger 8-step sliding track matrix.
  let pointer = PointerMatrix.create(1, 8);
  // Set the coordinates of each step cyclically to simulate a downward-to-upward sliding.
  for (let step = 0; step < 8; step++) {
    pointer.setPoint(0, step, { x: 500, y: 1100 - 100 * step });
  }
  // Inject swiping with a stylus at a speed of 600 px/s and a pressure of 0.5.
  await driver.injectPenPointerAction(pointer, 600, 0.5);
}
```

## inputText

```TypeScript
inputText(p: Point, text: string): Promise<void>
```

在指定坐标点输入文本，不清空组件内原有文本，直接在坐标处追加输入。使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-inputText(p: Point, text: string): Promise<void>--><!--Device-Driver-inputText(p: Point, text: string): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| p | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 输入文本的坐标点。 |
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

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  // Create a Driver object.
  let driver: Driver = Driver.create();
  // Search for the target TextInput component.
  let text: Component = await driver.findComponent(ON.type('TextInput'));
  // Obtain the coordinates of the component center point.
  let point = await text.getBoundsCenter();
  // Enter the text '123' at the coordinate point.
  await driver.inputText(point, '123');
}
```

## inputText

```TypeScript
inputText(p: Point, text: string, mode: InputTextMode): Promise<void>
```

在指定坐标点输入文本，支持指定文本输入方式。使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Driver-inputText(p: Point, text: string, mode: InputTextMode): Promise<void>--><!--Device-Driver-inputText(p: Point, text: string, mode: InputTextMode): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| p | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 输入文本的坐标点。 |
| text | string | Yes | 输入的文本信息，当前支持英文、中文和特殊字符。 |
| mode | [InputTextMode](arkts-test-uitest-inputtextmode-i.md) | Yes | 输入文本的方式，取值请参考[InputTextMode](arkts-test-uitest-inputtextmode-i.md)。  **说明：**  InputTextMode.addition取值为true时，将光标移动至文本末尾后输入指定文本。取值为false时，将在坐标点位置输入指定文本。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. function can not work correctly due to limited device capabilities. |
| 17000002 | The API does not support concurrent calls. |

## Examples

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
  await driver.inputText(point, 'Chinese&', { paste: false, addition: true });
  // Copy and paste Chinese and a special character to the end of the specified text.
}
```

## isComponentPresentWhenDrag

ArkTS-Dyn:
```TypeScript
isComponentPresentWhenDrag(on: On, from: Point, to: Point, speed?: number, duration?: number): Promise<boolean>
```

ArkTS-Sta:
```TypeScript
isComponentPresentWhenDrag(on: On, from: Point, to: Point, speed?: int, duration?: int): Promise<boolean>
```

从起始点拖拽至终止点，并查找目标控件是否存在。使用Promise异步回调。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Driver-isComponentPresentWhenDrag(on: On, from: Point, to: Point, speed?: int, duration?: int): Promise<boolean>--><!--Device-Driver-isComponentPresentWhenDrag(on: On, from: Point, to: Point, speed?: int, duration?: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | 目标控件的属性要求。 |
| from | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 以Point对象的形式传入起始点的坐标信息和所属屏幕ID。 |
| to | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 以Point对象的形式传入终止点的坐标信息和所属屏幕ID。  **说明：** 应与起始点属于同一个屏幕，否则将抛出17000007异常。 |
| speed | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出17000007错 误码。 |
| duration | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 拖拽前长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。取值小于1500时抛出17000007错误码，为null或undefined时使用默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回拖拽操作期间目标控件是否存在。true：存在。false：不存在。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let isExist = await driver.isComponentPresentWhenDrag(ON.id('123'), { x: 100, y: 100 }, { x: 200, y: 200 }, 1000, 2000);
}
```

## isComponentPresentWhenLongClick

ArkTS-Dyn:
```TypeScript
isComponentPresentWhenLongClick(on: On, point: Point, duration?: number): Promise<boolean>
```

ArkTS-Sta:
```TypeScript
isComponentPresentWhenLongClick(on: On, point: Point, duration?: int): Promise<boolean>
```

在坐标点长按，并查找目标控件是否存在。使用Promise异步回调。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Driver-isComponentPresentWhenLongClick(on: On, point: Point, duration?: int): Promise<boolean>--><!--Device-Driver-isComponentPresentWhenLongClick(on: On, point: Point, duration?: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | 目标控件的属性要求。 |
| point | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 长按的坐标点。 |
| duration | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。取值小于1500时抛出17000007错误码，为null或undefined时使用默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回长按操作期间目标控件是否存在。true：存在。false：不存在。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let isExist = await driver.isComponentPresentWhenLongClick(ON.id('123'), { x: 100, y: 100 }, 2000);
}
```

## isComponentPresentWhenSwipe

ArkTS-Dyn:
```TypeScript
isComponentPresentWhenSwipe(on: On, from: Point, to: Point, speed?: number): Promise<boolean>
```

ArkTS-Sta:
```TypeScript
isComponentPresentWhenSwipe(on: On, from: Point, to: Point, speed?: int): Promise<boolean>
```

从起始点滑向终止点，并查找目标控件是否存在。使用Promise异步回调。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Driver-isComponentPresentWhenSwipe(on: On, from: Point, to: Point, speed?: int): Promise<boolean>--><!--Device-Driver-isComponentPresentWhenSwipe(on: On, from: Point, to: Point, speed?: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | 目标控件的属性要求。 |
| from | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 以Point对象的形式传入起始点的坐标信息和所属屏幕ID。 |
| to | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 以Point对象的形式传入终止点的坐标信息和所属屏幕ID。  **说明：** 应与起始点属于同一个屏幕，否则将抛出17000007异常。 |
| speed | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出17000007错 误码。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回滑动操作期间目标控件是否存在。true：存在。false：不存在。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let isExist = await driver.isComponentPresentWhenSwipe(ON.id('123'), { x: 100, y: 100 }, { x: 200, y: 200 }, 1000);
}
```

## knuckleKnock

ArkTS-Dyn:
```TypeScript
knuckleKnock(pointers: Array<Point>, times: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
knuckleKnock(pointers: Array<Point>, times: int): Promise<void>
```

模拟指关节敲击屏幕操作。使用Promise异步回调。

> **说明：**
> 
> 若设备关闭了指关节手势&lt;!--RP4--&gt;&lt;!--RP4End--&gt;，则调用本接口返回17000005错误码。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Driver-knuckleKnock(pointers: Array<Point>, times: int): Promise<void>--><!--Device-Driver-knuckleKnock(pointers: Array<Point>, times: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pointers | Array&lt;Point&gt; | Yes | 指关节敲击屏幕坐标点的数组，数组长度取值为1或2。 |
| times | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指关节连续敲击屏幕的次数，取值为1或2。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |
| 17000005 | This operation is not supported. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, Point } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // Simulate a single-knuckle double-knock gesture.
  let points: Array<Point> = [{ x: 100, y: 100 }];
  await driver.knuckleKnock(points, 2);
}
```

## longClick

ArkTS-Dyn:
```TypeScript
longClick(x: number, y: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
longClick(x: int, y: int): Promise<void>
```

在目标坐标点长按。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-longClick(x: int, y: int): Promise<void>--><!--Device-Driver-longClick(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.longClick(100, 100);
}
```

## longClickAt

ArkTS-Dyn:
```TypeScript
longClickAt(point: Point, duration?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
longClickAt(point: Point, duration?: int): Promise<void>
```

长按目标坐标点，支持指定长按时长。使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Driver-longClickAt(point: Point, duration?: int): Promise<void>--><!--Device-Driver-longClickAt(point: Point, duration?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 以Point对象的形式传入目标点信息。 |
| duration | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。取值小于1500时抛出17000007错误码，为null或undefined时使用默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |

## Examples

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

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Driver-longClickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>--><!--Device-Driver-longClickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 手指接触屏幕的坐标点。 |
| options | [TouchOptions](arkts-test-uitest-touchoptions-i.md) | No | 用于长单击操作的选项。 只有“持续时间”和“压力”属性适用于此方法。 设置其他属性将导致BusinessError 17000007。 &lt;br&gt;默认值：参考TouchOptions的默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, TouchOptions } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let options: TouchOptions = {
    duration: 2000, // The click duration is 2000 ms.
    pressure: 0.8 // Touch pressure value.
  };
  // Long-click the target coordinate point, and specify the touch duration and pressure.
  await driver.longClickAtWithOptions({ x: 100, y: 100, displayId: 0 }, options);
}
```

## mouseClick

ArkTS-Dyn:
```TypeScript
mouseClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
mouseClick(p: Point, btnId: MouseButton, key1?: int, key2?: int): Promise<void>
```

在指定坐标点注入鼠标点击动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标点击动作。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-mouseClick(p: Point, btnId: MouseButton, key1?: int, key2?: int): Promise<void>--><!--Device-Driver-mouseClick(p: Point, btnId: MouseButton, key1?: int, key2?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| p | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 鼠标点击的坐标。 |
| btnId | [MouseButton](../../apis-arkui/arkts-apis/arkts-arkui-enums-mousebutton-e.md) | Yes | 按下的鼠标按钮。 |
| key1 | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md/arkts-input-multimodalinput-keycode-keycode-e.md)，默认值为0。<br>**Since:** 11 |
| key2 | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md/arkts-input-multimodalinput-keycode-keycode-e.md)，默认值为0。<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, MouseButton } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseClick({ x: 248, y: 194 }, MouseButton.MOUSE_BUTTON_LEFT, 2072);
}
```

## mouseDoubleClick

ArkTS-Dyn:
```TypeScript
mouseDoubleClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
mouseDoubleClick(p: Point, btnId: MouseButton, key1?: int, key2?: int): Promise<void>
```

在指定坐标点注入鼠标双击动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标双击动作。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-mouseDoubleClick(p: Point, btnId: MouseButton, key1?: int, key2?: int): Promise<void>--><!--Device-Driver-mouseDoubleClick(p: Point, btnId: MouseButton, key1?: int, key2?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| p | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 鼠标双击的坐标。 |
| btnId | [MouseButton](../../apis-arkui/arkts-apis/arkts-arkui-enums-mousebutton-e.md) | Yes | 按下的鼠标按钮。 |
| key1 | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md/arkts-input-multimodalinput-keycode-keycode-e.md)，默认值0。 |
| key2 | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md/arkts-input-multimodalinput-keycode-keycode-e.md)，默认值0。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

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

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-mouseDrag(from: Point, to: Point, speed?: number): Promise<void>--><!--Device-Driver-mouseDrag(from: Point, to: Point, speed?: number): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 起始点坐标。 |
| to | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 终点坐标。 |
| speed | number | No | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码 。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseDrag({ x: 100, y: 100 }, { x: 200, y: 200 }, 600);
}
```

## mouseDrag

ArkTS-Dyn:
```TypeScript
mouseDrag(from: Point, to: Point, speed?: number, duration?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
mouseDrag(from: Point, to: Point, speed?: int, duration?: int): Promise<void>
```

鼠标按住鼠标左键从起始坐标点拖拽至终点坐标点，支持指定拖拽速度和拖拽前长按时间。使用Promise异步回调。对于 API version 26.0.0 之前的版本，该接口不支持鼠标跨屏拖拽操作，起始点与终点需属于同一屏幕，否则将抛出401错误码；从 API version 26.0.0 开始，该接口支持鼠标跨屏拖拽操作。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Driver-mouseDrag(from: Point, to: Point, speed?: int, duration?: int): Promise<void>--><!--Device-Driver-mouseDrag(from: Point, to: Point, speed?: int, duration?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 起始点坐标。 |
| to | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 终点坐标。 |
| speed | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |
| duration | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 拖拽前长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。取值小于1500时抛出401错误码，为null或undefined时使用默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

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

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Driver-mouseDragWithOptions(from: Point, to: Point, touchOptions?: TouchOptions, keyOptions?: KeyOptions): Promise<void>--><!--Device-Driver-mouseDragWithOptions(from: Point, to: Point, touchOptions?: TouchOptions, keyOptions?: KeyOptions): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 起点。 |
| to | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 终点。 |
| touchOptions | [TouchOptions](arkts-test-uitest-touchoptions-i.md) | No | 速度和持续时间设置的触摸选项。 在此方法中，只有“速度”和“持续时间”属性有效。 设置其他属性会导致BusinessError 17000007。 &lt;br&gt;默认值：参考TouchOptions的默认值。 |
| keyOptions | [KeyOptions](arkts-test-uitest-keyoptions-i.md) | No | 拖动期间要按的键代码的键选项。 &lt;br&gt;默认值：参考keyOptions的默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, TouchOptions, KeyOptions } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let touchOptions: TouchOptions = {
    speed: 800,     // Drag speed: 800 px/s
    duration: 2000  // Click duration before dragging: 2000 ms.
  };
  let keyOptions: KeyOptions = {
    key1: 2072,  // Ctrl key
    key2: 2019   // C key
  };
  // Drag the mouse and press Ctrl+C.
  await driver.mouseDragWithOptions({ x: 100, y: 100 }, { x: 200, y: 200 }, touchOptions, keyOptions);
}
```

## mouseLongClick

```TypeScript
mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>
```

在指定坐标点注入鼠标长按动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标长按动作。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>--><!--Device-Driver-mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| p | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 鼠标长按的坐标。 |
| btnId | [MouseButton](../../apis-arkui/arkts-apis/arkts-arkui-enums-mousebutton-e.md) | Yes | 按下的鼠标按钮。 |
| key1 | number | No | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md/arkts-input-multimodalinput-keycode-keycode-e.md)，默认值 为0。 |
| key2 | number | No | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md/arkts-input-multimodalinput-keycode-keycode-e.md)，默认值 为0。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, MouseButton } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // If the key code value is 2072, the Ctrl button is pressed with the long-click.
  await driver.mouseLongClick({ x: 248, y: 194 }, MouseButton.MOUSE_BUTTON_LEFT, 2072);
}
```

## mouseLongClick

ArkTS-Dyn:
```TypeScript
mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number, duration?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
mouseLongClick(p: Point, btnId: MouseButton, key1?: int, key2?: int, duration?: int): Promise<void>
```

在指定坐标点注入鼠标长按动作，支持同时按下对应键盘组合键，支持指定长按时长。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标长按动作。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Driver-mouseLongClick(p: Point, btnId: MouseButton, key1?: int, key2?: int, duration?: int): Promise<void>--><!--Device-Driver-mouseLongClick(p: Point, btnId: MouseButton, key1?: int, key2?: int, duration?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| p | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 鼠标长按的坐标。 |
| btnId | [MouseButton](../../apis-arkui/arkts-apis/arkts-arkui-enums-mousebutton-e.md) | Yes | 按下的鼠标按钮。 |
| key1 | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md/arkts-input-multimodalinput-keycode-keycode-e.md)，默认值为0。 |
| key2 | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md/arkts-input-multimodalinput-keycode-keycode-e.md)，默认值为0。 |
| duration | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。取值小于1500时抛出401错误码，为null或undefined时使用默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, MouseButton } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // If the key code value is 2072, the Ctrl button is pressed with the long-click for 2,000 ms.
  await driver.mouseLongClick({ x: 248, y: 194 }, MouseButton.MOUSE_BUTTON_LEFT, 2072, 0, 2000);
}
```

## mouseMoveTo

```TypeScript
mouseMoveTo(p: Point): Promise<void>
```

将鼠标光标移到目标点。使用Promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-mouseMoveTo(p: Point): Promise<void>--><!--Device-Driver-mouseMoveTo(p: Point): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| p | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 目标点的坐标。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseMoveTo({ x: 100, y: 100 });
}
```

## mouseMoveWithTrack

ArkTS-Dyn:
```TypeScript
mouseMoveWithTrack(from: Point, to: Point, speed?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
mouseMoveWithTrack(from: Point, to: Point, speed?: int): Promise<void>
```

鼠标从起始坐标点滑向终点坐标点。使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-mouseMoveWithTrack(from: Point, to: Point, speed?: int): Promise<void>--><!--Device-Driver-mouseMoveWithTrack(from: Point, to: Point, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 起始点坐标。 |
| to | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 终点坐标。 |
| speed | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

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

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number): Promise<void>--><!--Device-Driver-mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| p | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 鼠标点击的坐标。 |
| down | boolean | Yes | 滚轮滑动方向是否向下。true表示向下滑动。false表示向上滚动。 |
| d | number | Yes | 鼠标滚轮滚动的格数，取值大于等于0的整数，每格对应目标点位移120px。 |
| key1 | number | No | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md/arkts-input-multimodalinput-keycode-keycode-e.md)，默认值 为0。<br>**Since:** 11 |
| key2 | number | No | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md/arkts-input-multimodalinput-keycode-keycode-e.md)，默认值 为0。<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseScroll({ x: 360, y: 640 }, true, 30, 2072);
}
```

## mouseScroll

ArkTS-Dyn:
```TypeScript
mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number, speed?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
mouseScroll(p: Point, down: boolean, d: int, key1?: int, key2?: int, speed?: int): Promise<void>
```

在指定坐标点注入鼠标滚轮滑动动作，支持同时按下对应键盘组合键并且指定滑动速度。使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-mouseScroll(p: Point, down: boolean, d: int, key1?: int, key2?: int, speed?: int): Promise<void>--><!--Device-Driver-mouseScroll(p: Point, down: boolean, d: int, key1?: int, key2?: int, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| p | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 鼠标点击的坐标。 |
| down | boolean | Yes | 滚轮滑动方向是否向下。true表示向下滑动。false表示向上滚动。 |
| d | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 鼠标滚轮滚动的格数，取值大于等于0的整数，每格对应目标点位移120px。 |
| key1 | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md/arkts-input-multimodalinput-keycode-keycode-e.md)，默认值为0。 |
| key2 | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md/arkts-input-multimodalinput-keycode-keycode-e.md)，默认值为0。 |
| speed | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 鼠标滚轮滚动的速度，范围：1-500的整数，单位：格/秒。为不在范围内的非负数或为null/undefined时设为默认值20。为负数时抛出401错误码。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

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

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Driver-penClick(point: Point): Promise<void>--><!--Device-Driver-penClick(point: Point): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 点击的坐标点。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，返回无结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

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

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Driver-penDoubleClick(point: Point): Promise<void>--><!--Device-Driver-penDoubleClick(point: Point): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 双击的坐标点。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，返回无结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.penDoubleClick({ x: 100, y: 100 });
}
```

## penLongClick

ArkTS-Dyn:
```TypeScript
penLongClick(point: Point, pressure?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
penLongClick(point: Point, pressure?: double): Promise<void>
```

模拟手写笔长按操作。使用Promise异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Driver-penLongClick(point: Point, pressure?: double): Promise<void>--><!--Device-Driver-penLongClick(point: Point, pressure?: double): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 长按的坐标点。 |
| pressure | ArkTS-Dyn: number  <br>ArkTS-Sta：double | No | 手写笔滑动操作的压力，默认为1.0，取值范围为0.0到1.0。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，返回无结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.penLongClick({ x: 100, y: 100 }, 0.5);
}
```

## penSwipe

ArkTS-Dyn:
```TypeScript
penSwipe(startPoint: Point, endPoint: Point, speed?: number, pressure?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
penSwipe(startPoint: Point, endPoint: Point, speed?: int, pressure?: double): Promise<void>
```

模拟手写笔的滑动操作。使用Promise异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Driver-penSwipe(startPoint: Point, endPoint: Point, speed?: int, pressure?: double): Promise<void>--><!--Device-Driver-penSwipe(startPoint: Point, endPoint: Point, speed?: int, pressure?: double): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startPoint | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 起始位置的坐标点。 |
| endPoint | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 结束位置的坐标点。 |
| speed | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |
| pressure | ArkTS-Dyn: number  <br>ArkTS-Sta：double | No | 手写笔滑动操作的压力，默认为1.0，取值范围为0.0到1.0。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，返回无结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-pressBack(): Promise<void>--><!--Device-Driver-pressBack(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.pressBack();
}
```

## pressBack

ArkTS-Dyn:
```TypeScript
pressBack(displayId: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
pressBack(displayId: int): Promise<void>
```

对指定屏幕进行点击BACK键的操作。使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Driver-pressBack(displayId: int): Promise<void>--><!--Device-Driver-pressBack(displayId: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定的屏幕ID，取值范围：大于等于0的整数。 **说明：** 传入displayId不存在时，将抛出17000007异常。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-pressHome(): Promise<void>--><!--Device-Driver-pressHome(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.pressHome();
}
```

## pressHome

ArkTS-Dyn:
```TypeScript
pressHome(displayId: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
pressHome(displayId: int): Promise<void>
```

设备指定屏幕上注入返回桌面操作。使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Driver-pressHome(displayId: int): Promise<void>--><!--Device-Driver-pressHome(displayId: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定设备屏幕ID。取值范围：大于等于0的整数。  **说明：** 传入displayId不存在时，将抛出17000007异常。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-screenCap(savePath: string): Promise<boolean>--><!--Device-Driver-screenCap(savePath: string): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| savePath | string | Yes | 文件保存路径。路径需为当前应用的[沙箱路径](../../../file-management/app-sandbox-directory.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回截图操作是否成功完成。true：完成，false：未完成。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.screenCap('/data/storage/el2/base/cache/1.png');
}
```

## screenCap

ArkTS-Dyn:
```TypeScript
screenCap(savePath: string, displayId: number): Promise<boolean>
```

ArkTS-Sta:
```TypeScript
screenCap(savePath: string, displayId: int): Promise<boolean>
```

捕获指定屏幕，并保存为PNG格式的图片至给出的保存路径中。使用Promise异步回调。适用于支持截屏的场景。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Driver-screenCap(savePath: string, displayId: int): Promise<boolean>--><!--Device-Driver-screenCap(savePath: string, displayId: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| savePath | string | Yes | 文件保存路径。路径需为当前应用的[沙箱路径](../../../file-management/app-sandbox-directory.md)。 |
| displayId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定设备屏幕ID。取值范围：大于等于0的整数。 **说明：** 传入displayId不存在时，将抛出17000007异常。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回截图操作是否成功完成。true：完成。false：未完成。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

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

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-screenCapture(savePath: string, rect?: Rect): Promise<boolean>--><!--Device-Driver-screenCapture(savePath: string, rect?: Rect): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| savePath | string | Yes | 文件保存路径。路径需为当前应用的[沙箱路径](../../../file-management/app-sandbox-directory.md)。 |
| rect | [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md) | No | 截图区域，默认为全屏。<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回截图操作是否成功完成。true：成功完成，false：未成功完成。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-setDisplayRotation(rotation: DisplayRotation): Promise<void>--><!--Device-Driver-setDisplayRotation(rotation: DisplayRotation): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rotation | [DisplayRotation](arkts-test-uitest-displayrotation-e.md) | Yes | 设备的显示方向。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-setDisplayRotationEnabled(enabled: boolean): Promise<void>--><!--Device-Driver-setDisplayRotationEnabled(enabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | 能否旋转屏幕的标识。true：可以旋转。false：不可以旋转。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.setDisplayRotationEnabled(false);
}
```

## swipe

ArkTS-Dyn:
```TypeScript
swipe(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
swipe(startx: int, starty: int, endx: int, endy: int, speed?: int): Promise<void>
```

从起始坐标点滑向目的坐标点。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-swipe(startx: int, starty: int, endx: int, endy: int, speed?: int): Promise<void>--><!--Device-Driver-swipe(startx: int, starty: int, endx: int, endy: int, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startx | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 以number的形式传入起始点的横坐标信息，取值范围：大于等于0的整数。 |
| starty | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 以number的形式传入起始点的纵坐标信息，取值范围：大于等于0的整数。 |
| endx | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 以number的形式传入目的点的横坐标信息，取值范围：大于等于0的整数。 |
| endy | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 以number的形式传入目的点的纵坐标信息，取值范围：大于等于0的整数。 |
| speed | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  // Create a Driver object.
  let driver: Driver = Driver.create();
  // Swipe from coordinates (100, 100) to coordinates (200, 200) at a speed of 600 px/s.
  await driver.swipe(100, 100, 200, 200, 600);
}
```

## swipeBetween

ArkTS-Dyn:
```TypeScript
swipeBetween(from: Point, to: Point, speed?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
swipeBetween(from: Point, to: Point, speed?: int): Promise<void>
```

从起始坐标点滑向目标坐标点。使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Driver-swipeBetween(from: Point, to: Point, speed?: int): Promise<void>--><!--Device-Driver-swipeBetween(from: Point, to: Point, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 以Point对象的形式传入起始点的坐标信息和所属屏幕ID。 |
| to | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 以Point对象的形式传入终止点的坐标信息和所属屏幕ID。  **说明：** 应与起始点属于同一个屏幕，否则将抛出17000007异常。 |
| speed | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出17000007错 误码。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |

## Examples

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

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Driver-swipeBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>--><!--Device-Driver-swipeBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 手指接触屏幕的坐标点。 |
| to | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 手指离开屏幕的坐标点。 |
| options | [TouchOptions](arkts-test-uitest-touchoptions-i.md) | No | 滑动操作的选项。 只有“速度”和“压力”属性适用于此方法。 设置其他属性将导致BusinessError 17000007。 &lt;br&gt;默认值：参考TouchOptions的默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, TouchOptions } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let options: TouchOptions = {
    speed: 800,   // Swipe speed: 800 px/s
    pressure: 0.5  // Touch pressure value.
  };
  // Swipes from the start coordinate point to the target coordinate point, and specifies the swipe speed and touch pressure.
  await driver.swipeBetweenWithOptions({ x: 100, y: 100, displayId: 0 }, { x: 1000, y: 1000, displayId: 0 }, options);
}
```

## touchPadMultiFingerSwipe

ArkTS-Dyn:
```TypeScript
touchPadMultiFingerSwipe(fingers: number, direction: UiDirection, options?: TouchPadSwipeOptions): Promise<void>
```

ArkTS-Sta:
```TypeScript
touchPadMultiFingerSwipe(fingers: int, direction: UiDirection, options?: TouchPadSwipeOptions): Promise<void>
```

模拟触摸板多指滑动手势。使用Promise异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Driver-touchPadMultiFingerSwipe(fingers: int, direction: UiDirection, options?: TouchPadSwipeOptions): Promise<void>--><!--Device-Driver-touchPadMultiFingerSwipe(fingers: int, direction: UiDirection, options?: TouchPadSwipeOptions): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fingers | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 触摸板多指滑动的手指数。取值为3或者4。 |
| direction | [UiDirection](arkts-test-uitest-uidirection-e.md) | Yes | 触摸板多指滑动的方向。 |
| options | [TouchPadSwipeOptions](arkts-test-uitest-touchpadswipeoptions-i.md) | No | 触摸板多指滑动手势附加选项，默认取TouchPadSwipeOptions中各属性的默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，返回无结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |
| 17000005 | This operation is not supported. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, UiDirection } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.touchPadMultiFingerSwipe(3, UiDirection.UP);
}
```

## touchPadTwoFingersScroll

ArkTS-Dyn:
```TypeScript
touchPadTwoFingersScroll(point: Point, direction: UiDirection, d: number, speed?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
touchPadTwoFingersScroll(point: Point, direction: UiDirection, d: int, speed?: int): Promise<void>
```

模拟触摸板双指滚动手势。使用Promise异步回调。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Driver-touchPadTwoFingersScroll(point: Point, direction: UiDirection, d: int, speed?: int): Promise<void>--><!--Device-Driver-touchPadTwoFingersScroll(point: Point, direction: UiDirection, d: int, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 触摸板双指滚动时鼠标光标的位置。 |
| direction | [UiDirection](arkts-test-uitest-uidirection-e.md) | Yes | 触摸板双指滚动的方向。 |
| d | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 触摸板双指滚动的格数，取值为大于等于0的整数，每格对应目标点位移120px。 |
| speed | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 触摸板双指滚动的速度，范围：1-500的整数，单位：格/秒。为不在范围内的非负数或为null/undefined时设为默认值20。为负数时抛出17000007错误码。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. |
| 17000005 | This operation is not supported. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-triggerCombineKeys(key0: number, key1: number, key2?: number): Promise<void>--><!--Device-Driver-triggerCombineKeys(key0: number, key1: number, key2?: number): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key0 | number | Yes | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md/arkts-input-multimodalinput-keycode-keycode-e.md)。 |
| key1 | number | Yes | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md/arkts-input-multimodalinput-keycode-keycode-e.md)。 |
| key2 | number | No | 指定的第三个key值，取值范围：大于等于0的整数。取值范围：[KeyCode键码值](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md/arkts-input-multimodalinput-keycode-keycode-e.md)， 默认值为0。<br>**Since:** 11 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // Inject the Ctrl+Alt+Delete key combination.
  await driver.triggerCombineKeys(2072, 2047, 2035);
}
```

## triggerCombineKeys

ArkTS-Dyn:
```TypeScript
triggerCombineKeys(key0: number, key1: number, key2?: number, displayId?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
triggerCombineKeys(key0: int, key1: int, key2?: int, displayId?: int): Promise<void>
```

通过给定的key值，找到对应组合键，并在指定屏幕下进行点击。使用Promise异步回调。例如，Key值为(2072, 2019)时，找到key值对应的组合键并点击，如Ctrl+c。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Driver-triggerCombineKeys(key0: int, key1: int, key2?: int, displayId?: int): Promise<void>--><!--Device-Driver-triggerCombineKeys(key0: int, key1: int, key2?: int, displayId?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key0 | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md/arkts-input-multimodalinput-keycode-keycode-e.md)。 |
| key1 | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md/arkts-input-multimodalinput-keycode-keycode-e.md)。 |
| key2 | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 指定的第三个key值，取值范围：大于等于0的整数，取值范围：[KeyCode键码值](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md/arkts-input-multimodalinput-keycode-keycode-e.md)，默认值 为0。 |
| displayId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 指定的屏幕ID，取值范围：大于等于0的整数，默认值为设备默认屏幕ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.triggerCombineKeys(2072, 2047, 2035, 0);
}
```

## triggerKey

ArkTS-Dyn:
```TypeScript
triggerKey(keyCode: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
triggerKey(keyCode: int): Promise<void>
```

传入key值实现模拟点击对应按键的效果。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-triggerKey(keyCode: int): Promise<void>--><!--Device-Driver-triggerKey(keyCode: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyCode | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定的key值，取值范围：大于等于0的整数。取值范围：[KeyCode键码值](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md/arkts-input-multimodalinput-keycode-keycode-e.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';
import { KeyCode } from '@kit.InputKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.triggerKey(KeyCode.KEYCODE_BACK); // Back button
}
```

## triggerKey

ArkTS-Dyn:
```TypeScript
triggerKey(keyCode: number, displayId: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
triggerKey(keyCode: int, displayId: int): Promise<void>
```

在指定屏幕，传入key值实现模拟点击对应按键的效果。使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Driver-triggerKey(keyCode: int, displayId: int): Promise<void>--><!--Device-Driver-triggerKey(keyCode: int, displayId: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyCode | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定的key值，取值范围：大于等于0的整数。取值范围：[KeyCode键码值](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md/arkts-input-multimodalinput-keycode-keycode-e.md)。 |
| displayId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定的屏幕ID，取值范围：大于等于0的整数。 **说明：** 传入displayId不存在时，将抛出17000007异常。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';
import { KeyCode } from '@kit.InputKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.triggerKey(KeyCode.KEYCODE_BACK, 0); // Back button
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

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Driver-triggerPenKey(key: PenKey, mode: PenMode, operation: PenKeyOperation, options?: PenKeyOperationOptions): Promise<void>--><!--Device-Driver-triggerPenKey(key: PenKey, mode: PenMode, operation: PenKeyOperation, options?: PenKeyOperationOptions): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | [PenKey](arkts-test-uitest-penkey-e.md) | Yes | the pen key to operate. |
| mode | [PenMode](arkts-test-uitest-penmode-e.md) | Yes | the pen mode. |
| operation | [PenKeyOperation](arkts-test-uitest-penkeyoperation-e.md) | Yes | the operation type. |
| options | [PenKeyOperationOptions](arkts-test-uitest-penkeyoperationoptions-i.md) | No | the operation options, including optional coordinate point. Default value: Refer to the default value of PenKeyOperationOption. &lt;br&gt;默认值：参考PenKeyOperationOption的默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |
| 17000007 | Parameter verification failed. Unsupported key, mode, and operation combination. |
| 17000005 | This operation is not supported. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver, PenKey, PenMode, PenKeyOperation } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // Trigger the handwriting key click in handwriting mode.
  await driver.triggerPenKey(PenKey.HANDWRITING, PenMode.HANDWRITING, PenKeyOperation.CLICK);
  // Trigger the air mouse key double-click in air mouse mode.
  await driver.triggerPenKey(PenKey.AIR_MOUSE, PenMode.AIR_MOUSE, PenKeyOperation.DOUBLE_CLICK, { point: { x: 500, y: 500 } });
  // Trigger the smart key click in air mouse mode.
  await driver.triggerPenKey(PenKey.SMART, PenMode.AIR_MOUSE, PenKeyOperation.CLICK);
}
```

## waitForComponent

```TypeScript
waitForComponent(on: On, time: number): Promise<Component>
```

在用户给定的时间内，持续查找满足控件属性要求的目标控件。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-waitForComponent(on: On, time: number): Promise<Component>--><!--Device-Driver-waitForComponent(on: On, time: number): Promise<Component>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | 目标控件的属性要求。 |
| time | number | Yes | 查找目标控件的持续时间。单位ms，取值范围：大于等于0的整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Component&gt; | Promise对象，返回控件对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.waitForComponent(ON.text('next page'), 500);
}
```

## waitForComponent

```TypeScript
waitForComponent(on: On, time: int): Promise<Component | null>
```

Find the first matched {@link Component} on current UI during the time given.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Driver-waitForComponent(on: On, time: int): Promise<Component | null>--><!--Device-Driver-waitForComponent(on: On, time: int): Promise<Component | null>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | the attribute requirements of the target {@link Component}. |
| time | int | Yes | duration of finding in milliseconds, not less than 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Component \| null&gt; | the first matched { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## waitForIdle

ArkTS-Dyn:
```TypeScript
waitForIdle(idleTime: number, timeout: number): Promise<boolean>
```

ArkTS-Sta:
```TypeScript
waitForIdle(idleTime: int, timeout: int): Promise<boolean>
```

判断当前界面的所有控件是否已经空闲。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-waitForIdle(idleTime: int, timeout: int): Promise<boolean>--><!--Device-Driver-waitForIdle(idleTime: int, timeout: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| idleTime | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 空闲时间的阈值。在这个时间段控件不发生变化，视为该控件空闲，单位：毫秒，取值范围：大于等于0的整数。 |
| timeout | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 等待空闲的最大时间，单位：毫秒，取值范围：大于等于0的整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回当前界面的所有控件是否已经空闲。true：已经空闲，false：不空闲。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17000002 | The API does not support concurrent calls. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-wakeUpDisplay(): Promise<void>--><!--Device-Driver-wakeUpDisplay(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17000002 | The API does not support concurrent calls. |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.wakeUpDisplay();
}
```

