# Driver

The **Driver** class is the main entrance of the UiTest framework. This class provides APIs for features such as component matching/search, key injection, coordinate clicking/sliding, and screenshot. All APIs provided by this class, except **Driver.create()** and **Driver.createUIEventObserver()**, use an asynchronous method (promise) to return the result and must be invoked using **await**.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare class Driver--><!--Device-unnamed-declare class Driver-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from '@kit.TestKit';
```

## assertComponentExist

```TypeScript
assertComponentExist(on: On): Promise<void>
```

Asserts whether a component matches the specified attributes exists on the current page. If the assertion fails, a JS exception is thrown, causing the test case to fail. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-assertComponentExist(on: On): Promise<void>--><!--Device-Driver-assertComponentExist(on: On): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000003](../errorcode-uitest.md#17000003-assertion-failure) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
click(x: number, y: number): Promise<void>
```

Clicks the target coordinate point. This method can be used only on the default screen of the device. To specify a screen, use [clickAt](#clickAt). This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-click(x: int, y: int): Promise<void>--><!--Device-Driver-click(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

Clicks the target coordinate point. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-clickAt(point: Point): Promise<void>--><!--Device-Driver-clickAt(point: Point): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

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

Click on the specified location on the screen, with optional touch options.

**Since:** 26.0.0

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Driver-clickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>--><!--Device-Driver-clickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | Yes |
| options | [TouchOptions](arkts-test-uitest-touchoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

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

Creates a **Driver** object and returns the object created. This API is a static API.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-static create(): Driver--><!--Device-Driver-static create(): Driver-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Driver](arkts-test-uitest-driver-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [17000001](../errorcode-uitest.md#17000001-initialization-failure) |

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

Creates a UI event listener [UIEventObserver](arkts-test-uitest-uieventobserver-i.md#UIEventObserver).

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-createUIEventObserver(): UIEventObserver--><!--Device-Driver-createUIEventObserver(): UIEventObserver-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [UIEventObserver](arkts-test-uitest-uieventobserver-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
crownRotate(d: number, speed?: number): Promise<void>
```

Injects a crown rotation event. You can specify the rotation speed. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-crownRotate(d: int, speed?: int): Promise<void>--><!--Device-Driver-crownRotate(d: int, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | number | Yes |
| speed | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

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

```TypeScript
delayMs(duration: number): Promise<void>
```

Delays a duration of time. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-delayMs(duration: int): Promise<void>--><!--Device-Driver-delayMs(duration: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| duration | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
doubleClick(x: number, y: number): Promise<void>
```

Double-clicks the target coordinate point. This method can be used only on the default screen of the device. To specify a screen, use [doubleClickAt](#doubleClickAt). This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-doubleClick(x: int, y: int): Promise<void>--><!--Device-Driver-doubleClick(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

Double-clicks the target coordinate point. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-doubleClickAt(point: Point): Promise<void>--><!--Device-Driver-doubleClickAt(point: Point): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

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

```TypeScript
drag(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>
```

Drags from the start coordinate point to the target coordinate point. This method can be used only on the default screen of the device, and the long-click duration before dragging cannot be customized. To specify a screen or long-click duration, use [dragBetween](#dragBetween). This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-drag(startx: int, starty: int, endx: int, endy: int, speed?: int): Promise<void>--><!--Device-Driver-drag(startx: int, starty: int, endx: int, endy: int, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startx | number | Yes |
| starty | number | Yes |
| endx | number | Yes |
| endy | number | Yes |
| speed | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
dragBetween(from: Point, to: Point, speed?: number, duration?: number): Promise<void>
```

Drags from the start point to the target point. You can specify the drag speed and the click duration before dragging. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-dragBetween(from: Point, to: Point, speed?: int, duration?: int): Promise<void>--><!--Device-Driver-dragBetween(from: Point, to: Point, speed?: int, duration?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | Yes |
| to | [Point](arkts-test-uitest-point-i.md) | Yes |
| speed | number | No |
| duration | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

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

Drag on the screen between the specified points with optional settings.

**Since:** 26.0.0

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Driver-dragBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>--><!--Device-Driver-dragBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | Yes |
| to | [Point](arkts-test-uitest-point-i.md) | Yes |
| options | [TouchOptions](arkts-test-uitest-touchoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

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

```TypeScript
dumpLayout(savePath: string, displayId?: number): Promise<boolean>
```

Dumps the current layout information and saves it as a JSON file. This method is applicable to test scenarios where you need to analyze the hierarchy of UI controls or debug controls to locate issues. This API uses a promise to return the result.

**Since:** 26.0.0

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Driver-dumpLayout(savePath: string, displayId?: int): Promise<boolean>--><!--Device-Driver-dumpLayout(savePath: string, displayId?: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| savePath | string | Yes |
| displayId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

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

Searches for the target component based on the specified attributes. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-findComponent(on: On): Promise<Component>--><!--Device-Driver-findComponent(on: On): Promise<Component>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Component](arkts-test-uitest-component-c.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

Find the first matched [Component](arkts-test-uitest-component-c.md#Component) on current UI.

**Since:** 23

**Deprecated since:** -1

<!--Device-Driver-findComponent(on: On): Promise<Component | null>--><!--Device-Driver-findComponent(on: On): Promise<Component | null>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Component](arkts-test-uitest-component-c.md) \| null & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

## findComponents

```TypeScript
findComponents(on: On): Promise<Array<Component>>
```

Searches for all matched components based on the specified attributes and saves them in a list. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-findComponents(on: On): Promise<Array<Component>>--><!--Device-Driver-findComponents(on: On): Promise<Array<Component>>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[Component](arkts-test-uitest-component-c.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

Find all the matched [Component](arkts-test-uitest-component-c.md#Component)s on current UI.

**Since:** 23

**Deprecated since:** -1

<!--Device-Driver-findComponents(on: On): Promise<Array<Component> | null>--><!--Device-Driver-findComponents(on: On): Promise<Array<Component> | null>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[Component](arkts-test-uitest-component-c.md)&gt; \| null & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

## findWindow

```TypeScript
findWindow(filter: WindowFilter): Promise<UiWindow>
```

Searches for a window based on the specified attributes. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-findWindow(filter: WindowFilter): Promise<UiWindow>--><!--Device-Driver-findWindow(filter: WindowFilter): Promise<UiWindow>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | [WindowFilter](arkts-test-uitest-windowfilter-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[UiWindow](arkts-test-uitest-uiwindow-c.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

Find the first matched [UiWindow](arkts-test-uitest-uiwindow-c.md#UiWindow) window.

**Since:** 23

**Deprecated since:** -1

<!--Device-Driver-findWindow(filter: WindowFilter): Promise<UiWindow | null>--><!--Device-Driver-findWindow(filter: WindowFilter): Promise<UiWindow | null>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | [WindowFilter](arkts-test-uitest-windowfilter-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[UiWindow](arkts-test-uitest-uiwindow-c.md) \| null & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

## fling

```TypeScript
fling(from: Point, to: Point, stepLen: number, speed: number): Promise<void>
```

Simulates a fling operation. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-fling(from: Point, to: Point, stepLen: int, speed: int): Promise<void>--><!--Device-Driver-fling(from: Point, to: Point, stepLen: int, speed: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | Yes |
| to | [Point](arkts-test-uitest-point-i.md) | Yes |
| stepLen | number | Yes |
| speed | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
fling(direction: UiDirection, speed: number): Promise<void>
```

Simulates a fling operation with the specified direction and speed. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-fling(direction: UiDirection, speed: int): Promise<void>--><!--Device-Driver-fling(direction: UiDirection, speed: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| direction | [UiDirection](arkts-test-uitest-uidirection-e.md) | Yes |
| speed | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
fling(direction: UiDirection, speed: number, displayId: number): Promise<void>
```

Simulates a fling operation on a specified display with the specified direction and speed. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-fling(direction: UiDirection, speed: int, displayId: int): Promise<void>--><!--Device-Driver-fling(direction: UiDirection, speed: int, displayId: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| direction | [UiDirection](arkts-test-uitest-uidirection-e.md) | Yes |
| speed | number | Yes |
| displayId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

Obtains the display density of the current device. This API uses a promise to return the result. > **NOTE：**> > This method can only be used to obtain the display density of the home screen. To obtain the display density > of a specified screen, use [getDisplayDensity](#getDisplayDensity)(displayId: number).

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-getDisplayDensity(): Promise<Point>--><!--Device-Driver-getDisplayDensity(): Promise<Point>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Point](arkts-test-uitest-point-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
getDisplayDensity(displayId: number): Promise<Point>
```

Obtains the density of the specified display of the current device. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-getDisplayDensity(displayId: int): Promise<Point>--><!--Device-Driver-getDisplayDensity(displayId: int): Promise<Point>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Point](arkts-test-uitest-point-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

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

Obtains the display rotation of the current device. This API uses a promise to return the result. > **NOTE：**> > This method can only be used to obtain the display rotation of the home screen. To obtain the display rotation > of a specified screen, use [getDisplayRotation](#getDisplayRotation)(displayId: number).

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-getDisplayRotation(): Promise<DisplayRotation>--><!--Device-Driver-getDisplayRotation(): Promise<DisplayRotation>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DisplayRotation](arkts-test-uitest-displayrotation-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
getDisplayRotation(displayId: number): Promise<DisplayRotation>
```

Obtains the display rotation of the specified device. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-getDisplayRotation(displayId: int): Promise<DisplayRotation>--><!--Device-Driver-getDisplayRotation(displayId: int): Promise<DisplayRotation>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DisplayRotation](arkts-test-uitest-displayrotation-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

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

Obtains the display size of the current device. This API uses a promise to return the result. > **NOTE：**> > This method can only be used to obtain the display size of the home screen. To obtain the display size of a > specified screen, use [getDisplaySize](#getDisplaySize)(displayId: number).

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-getDisplaySize(): Promise<Point>--><!--Device-Driver-getDisplaySize(): Promise<Point>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Point](arkts-test-uitest-point-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
getDisplaySize(displayId: number): Promise<Point>
```

Obtains the size of the specified display on the current device. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-getDisplaySize(displayId: int): Promise<Point>--><!--Device-Driver-getDisplaySize(displayId: int): Promise<Point>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Point](arkts-test-uitest-point-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

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

```TypeScript
injectKnucklePointerAction(pointers: PointerMatrix, speed?: number): Promise<void>
```

Simulates a multi-point knuckle scrolling operation. This API uses a promise to return the result. > **NOTE：**> > If the knuckle gesture is disabled on the device&lt;!--RP4--&gt;&lt;!--RP4End--&gt;, 17000005 is returned.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-injectKnucklePointerAction(pointers: PointerMatrix, speed?: int): Promise<void>--><!--Device-Driver-injectKnucklePointerAction(pointers: PointerMatrix, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pointers | [PointerMatrix](arkts-test-uitest-pointermatrix-c.md) | Yes |
| speed | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) |

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

```TypeScript
injectMultiPointerAction(pointers: PointerMatrix, speed?: number): Promise<boolean>
```

Injects a multi-finger operation into a device. This method applies to test scenarios where multi-finger gestures need to be simulated, such as pinching or spreading two fingers to zoom in or out on the image or swiping with multiple fingers to switch between pages. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-injectMultiPointerAction(pointers: PointerMatrix, speed?: int): Promise<boolean>--><!--Device-Driver-injectMultiPointerAction(pointers: PointerMatrix, speed?: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pointers | [PointerMatrix](arkts-test-uitest-pointermatrix-c.md) | Yes |
| speed | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
injectPenPointerAction(pointers: PointerMatrix, speed?: number, pressure?: number): Promise<void>
```

Simulates a continuous multi-point pen injection operation. This method is applicable to test scenarios where custom track operations, such as continuous writing and drawing with a pen, need to be simulated. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-injectPenPointerAction(pointers: PointerMatrix, speed?: int, pressure?: double): Promise<void>--><!--Device-Driver-injectPenPointerAction(pointers: PointerMatrix, speed?: int, pressure?: double): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pointers | [PointerMatrix](arkts-test-uitest-pointermatrix-c.md) | Yes |
| speed | number | No |
| pressure | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

Inputs text at a specified coordinate without clearing the original text in the component. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-inputText(p: Point, text: string): Promise<void>--><!--Device-Driver-inputText(p: Point, text: string): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | Yes |
| text | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

Inputs text at a specified coordinate point in a specified input mode. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-inputText(p: Point, text: string, mode: InputTextMode): Promise<void>--><!--Device-Driver-inputText(p: Point, text: string, mode: InputTextMode): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | Yes |
| text | string | Yes |
| mode | [InputTextMode](arkts-test-uitest-inputtextmode-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
isComponentPresentWhenDrag(on: On, from: Point, to: Point, speed?: number, duration?: number): Promise<boolean>
```

Drags from the start point to the end point and checks whether the target component exists. This method is applicable to verifying the dynamic UI elements that appear during the drag operation. For example, when dragging a file to a target folder, you can use this API to verify the highlight effect of the folder. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-isComponentPresentWhenDrag(on: On, from: Point, to: Point, speed?: int, duration?: int): Promise<boolean>--><!--Device-Driver-isComponentPresentWhenDrag(on: On, from: Point, to: Point, speed?: int, duration?: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes |
| from | [Point](arkts-test-uitest-point-i.md) | Yes |
| to | [Point](arkts-test-uitest-point-i.md) | Yes |
| speed | number | No |
| duration | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

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

```TypeScript
isComponentPresentWhenLongClick(on: On, point: Point, duration?: number): Promise<boolean>
```

Long-clicks at the specified coordinates and checks whether the target component exists. This method is applicable to verifying the UI elements that dynamically appear after a long-click, such as the context menu or edit button. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-isComponentPresentWhenLongClick(on: On, point: Point, duration?: int): Promise<boolean>--><!--Device-Driver-isComponentPresentWhenLongClick(on: On, point: Point, duration?: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes |
| point | [Point](arkts-test-uitest-point-i.md) | Yes |
| duration | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

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

```TypeScript
isComponentPresentWhenSwipe(on: On, from: Point, to: Point, speed?: number): Promise<boolean>
```

Swipes from the start point to the end point and checks whether the target component exists. This method is applicable to verifying the dynamic UI elements that appear during the swipe operation, for example, verifying whether the delete button appears when swiping is used to delete a list item. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-isComponentPresentWhenSwipe(on: On, from: Point, to: Point, speed?: int): Promise<boolean>--><!--Device-Driver-isComponentPresentWhenSwipe(on: On, from: Point, to: Point, speed?: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes |
| from | [Point](arkts-test-uitest-point-i.md) | Yes |
| to | [Point](arkts-test-uitest-point-i.md) | Yes |
| speed | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

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

```TypeScript
knuckleKnock(pointers: Array<Point>, times: number): Promise<void>
```

Simulates a knuckle knock on the display. This API uses a promise to return the result. > **NOTE：**> > If the knuckle gesture is disabled on the device&lt;!--RP4--&gt;&lt;!--RP4End--&gt;, 17000005 is returned.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-knuckleKnock(pointers: Array<Point>, times: int): Promise<void>--><!--Device-Driver-knuckleKnock(pointers: Array<Point>, times: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pointers | Array&lt;[Point](arkts-test-uitest-point-i.md)&gt; | Yes |
| times | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) |

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

```TypeScript
longClick(x: number, y: number): Promise<void>
```

Long-clicks the target coordinate point. This method can be used only on the default screen of the device, and the long-click duration cannot be customized. To specify a screen or long-click duration, use [longClickAt](#longClickAt). This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-longClick(x: int, y: int): Promise<void>--><!--Device-Driver-longClick(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
longClickAt(point: Point, duration?: number): Promise<void>
```

Long-clicks the target coordinate point for a specified duration. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-longClickAt(point: Point, duration?: int): Promise<void>--><!--Device-Driver-longClickAt(point: Point, duration?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | Yes |
| duration | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

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

LongClick on the specified location on the screen, with optional touch settings.

**Since:** 26.0.0

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Driver-longClickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>--><!--Device-Driver-longClickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | Yes |
| options | [TouchOptions](arkts-test-uitest-touchoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

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

```TypeScript
mouseClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>
```

Injects a mouse click action at the specified coordinates, with the optional key or key combination. This API uses a promise to return the result. For example, if the key code value is **2072**, the **Ctrl** button is pressed with the mouse click.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-mouseClick(p: Point, btnId: MouseButton, key1?: int, key2?: int): Promise<void>--><!--Device-Driver-mouseClick(p: Point, btnId: MouseButton, key1?: int, key2?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | Yes |
| btnId | [MouseButton](arkts-test-uitest-mousebutton-e.md) | Yes |
| [key1](arkts-test-uitest-keyoptions-i.md) | number | No |
| [key2](arkts-test-uitest-keyoptions-i.md) | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
mouseDoubleClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>
```

Injects a double-click action at the specified coordinates, with the optional key or key combination. This API uses a promise to return the result. For example, if the key code value is **2072**, the **Ctrl** button is pressed with the double-click.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-mouseDoubleClick(p: Point, btnId: MouseButton, key1?: int, key2?: int): Promise<void>--><!--Device-Driver-mouseDoubleClick(p: Point, btnId: MouseButton, key1?: int, key2?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | Yes |
| btnId | [MouseButton](arkts-test-uitest-mousebutton-e.md) | Yes |
| [key1](arkts-test-uitest-keyoptions-i.md) | number | No |
| [key2](arkts-test-uitest-keyoptions-i.md) | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

Drags the mouse pointer from the start point to the end point. This API uses a promise to return the result.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-mouseDrag(from: Point, to: Point, speed?: number): Promise<void>--><!--Device-Driver-mouseDrag(from: Point, to: Point, speed?: number): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | Yes |
| to | [Point](arkts-test-uitest-point-i.md) | Yes |
| speed | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
mouseDrag(from: Point, to: Point, speed?: number, duration?: number): Promise<void>
```

Drags the mouse from the start point to the end point. You can specify the dragging speed and the duration before dragging. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-mouseDrag(from: Point, to: Point, speed?: int, duration?: int): Promise<void>--><!--Device-Driver-mouseDrag(from: Point, to: Point, speed?: int, duration?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | Yes |
| to | [Point](arkts-test-uitest-point-i.md) | Yes |
| speed | number | No |
| duration | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

Hold down the left mouse button and drag on the screen between the specified points, with optional touch and key settings.

**Since:** 26.0.0

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Driver-mouseDragWithOptions(from: Point, to: Point, touchOptions?: TouchOptions, keyOptions?: KeyOptions): Promise<void>--><!--Device-Driver-mouseDragWithOptions(from: Point, to: Point, touchOptions?: TouchOptions, keyOptions?: KeyOptions): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | Yes |
| to | [Point](arkts-test-uitest-point-i.md) | Yes |
| touchOptions | [TouchOptions](arkts-test-uitest-touchoptions-i.md) | No |
| keyOptions | [KeyOptions](arkts-test-uitest-keyoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

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

Injects a mouse long-click action at the specified coordinates, with the optional key or key combination. This API uses a promise to return the result. For example, if the key code value is **2072**, the **Ctrl** button is long-clicked with the mouse device.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>--><!--Device-Driver-mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | Yes |
| btnId | [MouseButton](arkts-test-uitest-mousebutton-e.md) | Yes |
| [key1](arkts-test-uitest-keyoptions-i.md) | number | No |
| [key2](arkts-test-uitest-keyoptions-i.md) | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number, duration?: number): Promise<void>
```

Injects a mouse long-click action at the specified coordinates, with the optional key or key combination and the specified duration. This API uses a promise to return the result. For example, if the key code value is **2072** , the **Ctrl** button is pressed with the long-click.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-mouseLongClick(p: Point, btnId: MouseButton, key1?: int, key2?: int, duration?: int): Promise<void>--><!--Device-Driver-mouseLongClick(p: Point, btnId: MouseButton, key1?: int, key2?: int, duration?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | Yes |
| btnId | [MouseButton](arkts-test-uitest-mousebutton-e.md) | Yes |
| [key1](arkts-test-uitest-keyoptions-i.md) | number | No |
| [key2](arkts-test-uitest-keyoptions-i.md) | number | No |
| duration | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

Moves the mouse cursor to the target point. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-mouseMoveTo(p: Point): Promise<void>--><!--Device-Driver-mouseMoveTo(p: Point): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
mouseMoveWithTrack(from: Point, to: Point, speed?: number): Promise<void>
```

Moves the mouse pointer from the start point to the end point, with a visible movement track. This method is applicable to test scenarios that depend on the mouse movement track, such as verification of the mouse hover effect and selecting an area by dragging with the mouse. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-mouseMoveWithTrack(from: Point, to: Point, speed?: int): Promise<void>--><!--Device-Driver-mouseMoveWithTrack(from: Point, to: Point, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | Yes |
| to | [Point](arkts-test-uitest-point-i.md) | Yes |
| speed | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

Injects a mouse scroll action at the specified coordinates, with the optional key or key combination. This API uses a promise to return the result. For example, if the key code value is **2072**, the **Ctrl** button is pressed with mouse scrolling.

**Since:** 10

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number): Promise<void>--><!--Device-Driver-mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | Yes |
| down | boolean | Yes |
| [d](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | number | Yes |
| [key1](arkts-test-uitest-keyoptions-i.md) | number | No |
| [key2](arkts-test-uitest-keyoptions-i.md) | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number, speed?: number): Promise<void>
```

Injects a mouse scroll action at the specified coordinates, with the optional key or key combination and the specified scroll speed. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-mouseScroll(p: Point, down: boolean, d: int, key1?: int, key2?: int, speed?: int): Promise<void>--><!--Device-Driver-mouseScroll(p: Point, down: boolean, d: int, key1?: int, key2?: int, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | Yes |
| down | boolean | Yes |
| [d](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | number | Yes |
| [key1](arkts-test-uitest-keyoptions-i.md) | number | No |
| [key2](arkts-test-uitest-keyoptions-i.md) | number | No |
| speed | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

Simulates a pen click operation. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-penClick(point: Point): Promise<void>--><!--Device-Driver-penClick(point: Point): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

Simulates a pen double-click operation. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-penDoubleClick(point: Point): Promise<void>--><!--Device-Driver-penDoubleClick(point: Point): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
penLongClick(point: Point, pressure?: number): Promise<void>
```

Simulates a pen long-click operation. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-penLongClick(point: Point, pressure?: double): Promise<void>--><!--Device-Driver-penLongClick(point: Point, pressure?: double): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | Yes |
| pressure | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
penSwipe(startPoint: Point, endPoint: Point, speed?: number, pressure?: number): Promise<void>
```

Simulates a pen swipe operation. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-penSwipe(startPoint: Point, endPoint: Point, speed?: int, pressure?: double): Promise<void>--><!--Device-Driver-penSwipe(startPoint: Point, endPoint: Point, speed?: int, pressure?: double): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startPoint | [Point](arkts-test-uitest-point-i.md) | Yes |
| endPoint | [Point](arkts-test-uitest-point-i.md) | Yes |
| speed | number | No |
| pressure | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

Simulates pressing the Back button. This API uses a promise to return the result. > **NOTE：**> > This method only simulates pressing the Back button on the home screen. To simulate pressing the Back button > on a specified screen, use pressBack(displayId: number).

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-pressBack(): Promise<void>--><!--Device-Driver-pressBack(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
pressBack(displayId: number): Promise<void>
```

Simulates pressing the Back button on a specified screen. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-pressBack(displayId: int): Promise<void>--><!--Device-Driver-pressBack(displayId: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

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

Injects an operation of returning to the home screen on the device. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-pressHome(): Promise<void>--><!--Device-Driver-pressHome(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
pressHome(displayId: number): Promise<void>
```

Injects an operation of returning to the home screen on the specified display. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-pressHome(displayId: int): Promise<void>--><!--Device-Driver-pressHome(displayId: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

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

Captures the current screen and saves it as a PNG image to the given save path. This API uses a promise to return the result. This API can be used in scenarios where screenshots are supported.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-screenCap(savePath: string): Promise<boolean>--><!--Device-Driver-screenCap(savePath: string): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| savePath | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
screenCap(savePath: string, displayId: number): Promise<boolean>
```

Captures the specified screen and saves it as a PNG image to the given save path. This API uses a promise to return the result. This API can be used in scenarios where screenshots are supported.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-screenCap(savePath: string, displayId: int): Promise<boolean>--><!--Device-Driver-screenCap(savePath: string, displayId: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| savePath | string | Yes |
| displayId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

Captures the specified area of the current screen and saves the captured screenshot as a PNG image to the specified path. This API uses a promise to return the result. This API can be used in scenarios where screenshots are supported. Unlike screenCap, this API allows you to specify the screenshot area using the **rect** parameter instead of capturing the entire screen.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-screenCapture(savePath: string, rect?: Rect): Promise<boolean>--><!--Device-Driver-screenCapture(savePath: string, rect?: Rect): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| savePath | string | Yes |
| rect | [Rect](arkts-test-uitest-rect-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

Sets the display rotation of the current scene. This API uses a promise to return the result. This API is applicable to scenarios where rotation is allowed. The rotation function can be enabled by setting **orientation=** to **auto_rotation** in the module.json5 configuration file.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-setDisplayRotation(rotation: DisplayRotation): Promise<void>--><!--Device-Driver-setDisplayRotation(rotation: DisplayRotation): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rotation | [DisplayRotation](arkts-test-uitest-displayrotation-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

Enables or disables display rotation. This method is applicable to scenarios where the screen orientation needs to be locked during the test to maintain a specific display state, for example, testing the layout stability in landscape or portrait mode. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-setDisplayRotationEnabled(enabled: boolean): Promise<void>--><!--Device-Driver-setDisplayRotationEnabled(enabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
swipe(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>
```

Swipes from the start coordinate point to the target coordinate point. This method can be used only on the default screen of the device. To specify a screen, use [swipeBetween](#swipeBetween). This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-swipe(startx: int, starty: int, endx: int, endy: int, speed?: int): Promise<void>--><!--Device-Driver-swipe(startx: int, starty: int, endx: int, endy: int, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startx | number | Yes |
| starty | number | Yes |
| endx | number | Yes |
| endy | number | Yes |
| speed | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
swipeBetween(from: Point, to: Point, speed?: number): Promise<void>
```

Swipes from the start coordinate point to the target coordinate point. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-swipeBetween(from: Point, to: Point, speed?: int): Promise<void>--><!--Device-Driver-swipeBetween(from: Point, to: Point, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | Yes |
| to | [Point](arkts-test-uitest-point-i.md) | Yes |
| speed | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

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

Swipe on the screen between the specified points with optional touch options.

**Since:** 26.0.0

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Driver-swipeBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>--><!--Device-Driver-swipeBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | Yes |
| to | [Point](arkts-test-uitest-point-i.md) | Yes |
| options | [TouchOptions](arkts-test-uitest-touchoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

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

```TypeScript
touchPadMultiFingerSwipe(fingers: number, direction: UiDirection, options?: TouchPadSwipeOptions): Promise<void>
```

Simulates a multi-finger swipe gesture on the touchpad. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-touchPadMultiFingerSwipe(fingers: int, direction: UiDirection, options?: TouchPadSwipeOptions): Promise<void>--><!--Device-Driver-touchPadMultiFingerSwipe(fingers: int, direction: UiDirection, options?: TouchPadSwipeOptions): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fingers | number | Yes |
| direction | [UiDirection](arkts-test-uitest-uidirection-e.md) | Yes |
| options | [TouchPadSwipeOptions](arkts-test-uitest-touchpadswipeoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) |

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

```TypeScript
touchPadTwoFingersScroll(point: Point, direction: UiDirection, d: number, speed?: number): Promise<void>
```

Simulates a two-finger scroll gesture on the touchpad. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-touchPadTwoFingersScroll(point: Point, direction: UiDirection, d: int, speed?: int): Promise<void>--><!--Device-Driver-touchPadTwoFingersScroll(point: Point, direction: UiDirection, d: int, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | Yes |
| direction | [UiDirection](arkts-test-uitest-uidirection-e.md) | Yes |
| [d](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | number | Yes |
| speed | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) |

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

Triggers a combination key event based on the specified key code values. This API uses a promise to return the result. For example, if the key code value is (2072, 2019), the module finds and clicks the key combination that matches the value, for example, **Ctrl+C**.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-triggerCombineKeys(key0: number, key1: number, key2?: number): Promise<void>--><!--Device-Driver-triggerCombineKeys(key0: number, key1: number, key2?: number): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key0 | number | Yes |
| [key1](arkts-test-uitest-keyoptions-i.md) | number | Yes |
| [key2](arkts-test-uitest-keyoptions-i.md) | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
triggerCombineKeys(key0: number, key1: number, key2?: number, displayId?: number): Promise<void>
```

Triggers a combination key event based on the specified key code values on the specified screen. This API uses a promise to return the result. For example, if the key code value is (2072, 2019), the module finds and clicks the key combination that matches the value, for example, **Ctrl+C**.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-triggerCombineKeys(key0: int, key1: int, key2?: int, displayId?: int): Promise<void>--><!--Device-Driver-triggerCombineKeys(key0: int, key1: int, key2?: int, displayId?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key0 | number | Yes |
| [key1](arkts-test-uitest-keyoptions-i.md) | number | Yes |
| [key2](arkts-test-uitest-keyoptions-i.md) | number | No |
| displayId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
triggerKey(keyCode: number): Promise<void>
```

Triggers a key event by passing the key code value. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-triggerKey(keyCode: int): Promise<void>--><!--Device-Driver-triggerKey(keyCode: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyCode | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

```TypeScript
triggerKey(keyCode: number, displayId: number): Promise<void>
```

Triggers a key event by passing the key code value on the specified screen. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-triggerKey(keyCode: int, displayId: int): Promise<void>--><!--Device-Driver-triggerKey(keyCode: int, displayId: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyCode | number | Yes |
| displayId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

Trigger pen key operation. Supported combinations: - HANDWRITING mode: HANDWRITING key with CLICK or DOUBLE_CLICK operation. - AIR_MOUSE mode: AIR_MOUSE key with CLICK or DOUBLE_CLICK operation (requires point in options), HANDWRITING key with CLICK or DOUBLE_CLICK operation, SMART key with CLICK operation. Other combinations will result in a BusinessError 17000007.

**Since:** 26.0.0

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Driver-triggerPenKey(key: PenKey, mode: PenMode, operation: PenKeyOperation, options?: PenKeyOperationOptions): Promise<void>--><!--Device-Driver-triggerPenKey(key: PenKey, mode: PenMode, operation: PenKeyOperation, options?: PenKeyOperationOptions): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | [PenKey](arkts-test-uitest-penkey-e.md) | Yes |
| mode | [PenMode](arkts-test-uitest-penmode-e.md) | Yes |
| operation | [PenKeyOperation](arkts-test-uitest-penkeyoperation-e.md) | Yes |
| options | [PenKeyOperationOptions](arkts-test-uitest-penkeyoperationoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) |

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

Searches for the target component based on the attributes within a specified time. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-waitForComponent(on: On, time: number): Promise<Component>--><!--Device-Driver-waitForComponent(on: On, time: number): Promise<Component>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes |
| time | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Component](arkts-test-uitest-component-c.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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
waitForComponent(on: On, time: number): Promise<Component | null>
```

Find the first matched [Component](arkts-test-uitest-component-c.md#Component) on current UI during the time given.

**Since:** 23

**Deprecated since:** -1

<!--Device-Driver-waitForComponent(on: On, time: int): Promise<Component | null>--><!--Device-Driver-waitForComponent(on: On, time: int): Promise<Component | null>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes |
| time | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Component](arkts-test-uitest-component-c.md) \| null & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

## waitForIdle

```TypeScript
waitForIdle(idleTime: number, timeout: number): Promise<boolean>
```

Checks whether all components on the current UI are idle. This method is applicable to scenarios such as page redirection, animation playback, and loading. After calling this method, you can perform subsequent test operations only after the UI becomes stable. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-waitForIdle(idleTime: int, timeout: int): Promise<boolean>--><!--Device-Driver-waitForIdle(idleTime: int, timeout: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| idleTime | number | Yes |
| timeout | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

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

Wakes up the current display. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-wakeUpDisplay(): Promise<void>--><!--Device-Driver-wakeUpDisplay(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

## Examples

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.wakeUpDisplay();
}
```
