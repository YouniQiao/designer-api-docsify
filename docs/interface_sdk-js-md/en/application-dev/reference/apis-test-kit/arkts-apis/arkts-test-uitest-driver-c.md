# Driver

The **Driver** class is the main entrance of the UiTest framework. This class provides APIs for features such as component matching/search, key injection, coordinate clicking/sliding, and screenshot. All APIs provided by this class, except **Driver.create()** and **Driver.createUIEventObserver()**, use an asynchronous method (promise) to return the result and must be invoked using **await**.

**Since:** 23

<!--Device-unnamed-declare class Driver--><!--Device-unnamed-declare class Driver-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from '@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from '@kit.TestKit';
```

## assertComponentExist

```TypeScript
assertComponentExist(on: On): Promise<void>
```

Asserts whether a component matches the specified attributes exists on the current page. If the assertion fails, a JS exception is thrown, causing the test case to fail. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-assertComponentExist(on: On): Promise<void>--><!--Device-Driver-assertComponentExist(on: On): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | Attributes of the target [Component](arkts-test-uitest-component-c.md). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000003](../errorcode-uitest.md#17000003-assertion-failure) | Assertion failed. |

**Examples**

```TypeScript
// xxx.test.ets
import { Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.assertComponentExist(ON.text('next page'));
}
```

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
click(x: int, y: int): Promise<void>
```

Clicks the target coordinate point. This method can be used only on the default screen of the device. To specify a screen, use [clickAt](#clickat). This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-click(x: int, y: int): Promise<void>--><!--Device-Driver-click(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | int | Yes | Horizontal coordinate of the target point, in pixels. The value is an integer greater than or equal to 0. If the value is out of range, error code 401 is thrown. |
| y | int | Yes | Vertical coordinate of the target point, in pixels. The value is an integer greater than or equal to 0. If the value is out of range, error code 401 is thrown. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { Driver, ON, Component } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  await button.click();
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
import { UiDriver, BY, Driver, UiComponent } from '@kit.TestKit';

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

## clickAt

```TypeScript
clickAt(point: Point): Promise<void>
```

Clicks the target coordinate point. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-clickAt(point: Point): Promise<void>--><!--Device-Driver-clickAt(point: Point): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | Yes | Point object, which is used to transfer the target point information. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

**Examples**

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

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Driver-clickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>--><!--Device-Driver-clickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | Yes | the coordinate point where the finger touches the screen. |
| options | [TouchOptions](arkts-test-uitest-touchoptions-i.md) | No | the options for the click operation. Only the 'pressure' property is applicable for this method. Setting other properties will result in a BusinessError 17000007. Default value: Refer to the default value of TouchOptions. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

## create

```TypeScript
static create(): Driver
```

Creates a **Driver** object and returns the object created. This API is a static API.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-static create(): Driver--><!--Device-Driver-static create(): Driver-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| [Driver](arkts-test-uitest-driver-c.md) | { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000001](../errorcode-uitest.md#17000001-initialization-failure) | Initialization failed. |

**Examples**

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
}
```

```TypeScript
// xxx.test.ets
import { PointerMatrix } from '@kit.TestKit';

async function demo() {
  let pointerMatrix: PointerMatrix = PointerMatrix.create(2, 3);
}
```

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
}
```

## createUIEventObserver

```TypeScript
createUIEventObserver(): UIEventObserver
```

Creates a UI event listener [UIEventObserver](arkts-test-uitest-uieventobserver-i.md).

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-createUIEventObserver(): UIEventObserver--><!--Device-Driver-createUIEventObserver(): UIEventObserver-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| [UIEventObserver](arkts-test-uitest-uieventobserver-i.md) | UI event listener object created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

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
crownRotate(d: int, speed?: int): Promise<void>
```

Injects a crown rotation event. You can specify the rotation speed. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-crownRotate(d: int, speed?: int): Promise<void>--><!--Device-Driver-crownRotate(d: int, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | int | Yes | Number of rotation ticks. A positive value indicates rotation, and a negative value indicates counterclockwise rotation. The value must be an integer. If the value is not an integer, error code 401 is returned. |
| speed | int | No | Rotation speed. <br>Unit: ticks/s. <br>Value range: [1, 500] <br>Throws error code 17000007 if negative. <br>Default value: 20 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

**Examples**

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
delayMs(duration: int): Promise<void>
```

Delays a duration of time. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-delayMs(duration: int): Promise<void>--><!--Device-Driver-delayMs(duration: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| duration | int | Yes | Specified time, in ms. The value is an integer greater than or equal to 0. If the value is a negative number, error code 401 is returned. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.delayMs(1000);
}
```

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
doubleClick(x: int, y: int): Promise<void>
```

Double-clicks the target coordinate point. This method can be used only on the default screen of the device. To specify a screen, use [doubleClickAt](#doubleclickat). This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-doubleClick(x: int, y: int): Promise<void>--><!--Device-Driver-doubleClick(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | int | Yes | Horizontal coordinate of the target point, in pixels. The value is an integer greater than or equal to 0. If the value is out of range, error code 401 is thrown. |
| y | int | Yes | Vertical coordinate of the target point, in pixels. The value is an integer greater than or equal to 0. If the value is out of range, error code 401 is thrown. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  await button.doubleClick();
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

## doubleClickAt

```TypeScript
doubleClickAt(point: Point): Promise<void>
```

Double-clicks the target coordinate point. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-doubleClickAt(point: Point): Promise<void>--><!--Device-Driver-doubleClickAt(point: Point): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | Yes | Point object, which is used to transfer the target point information. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

**Examples**

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
drag(startx: int, starty: int, endx: int, endy: int, speed?: int): Promise<void>
```

Drags from the start coordinate point to the target coordinate point. This method can be used only on the default screen of the device, and the long-click duration before dragging cannot be customized. To specify a screen or long-click duration, use [dragBetween](#dragbetween). This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-drag(startx: int, starty: int, endx: int, endy: int, speed?: int): Promise<void>--><!--Device-Driver-drag(startx: int, starty: int, endx: int, endy: int, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startx | int | Yes | Horizontal coordinate of the start point, in pixels. The value is an integer greater than or equal to 0. |
| starty | int | Yes | Vertical coordinate of the start point, in pixels. The value is an integer greater than or equal to 0. |
| endx | int | Yes | Horizontal coordinate of the end point, in pixels. The value is an integer greater than or equal to 0. |
| endy | int | Yes | Vertical coordinate of the end point, in pixels. The value is an integer greater than or equal to 0. |
| speed | int | No | Drag speed, in px/s. The value ranges from 200 to 40000. If the set value is not in the range, the default value **600** is used. <br>Value range:[200, 40000] <br>Unit: px/s. <br>Throws error code 401 if negative. <br>Default value: 600 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

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
dragBetween(from: Point, to: Point, speed?: int, duration?: int): Promise<void>
```

Drags from the start point to the target point. You can specify the drag speed and the click duration before dragging. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-dragBetween(from: Point, to: Point, speed?: int, duration?: int): Promise<void>--><!--Device-Driver-dragBetween(from: Point, to: Point, speed?: int, duration?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | Yes | Point object, which transfers the coordinates of the start point and the ID of the display to which the start point belongs. |
| to | [Point](arkts-test-uitest-point-i.md) | Yes | Point object, which transfers the coordinates of the target point and the ID of the display to which it belongs. <br> **Note：**: The target point and the start point must be on the same screen. Otherwise, the **17000007** exception is thrown. |
| speed | int | No | Drag speed, in px/s. The value ranges from 200 to 40000. If the set value is not in the range, the default value **600** is used. <br>Value range:[200, 40000] <br>Unit: px/s. <br>Throws error code 17000007 if negative. <br>Default value: 600 |
| duration | int | No | Click duration, in ms. The value is an integer greater than or equal to 1500. The default value is 1500. If the value is less than 1500, the 17000007 error code is thrown. If the value is **null** or **undefined**, the default value is used. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

**Examples**

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

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Driver-dragBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>--><!--Device-Driver-dragBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | Yes | the coordinate point where the finger touches the screen. |
| to | [Point](arkts-test-uitest-point-i.md) | Yes | the coordinate point where the finger leaves the screen. |
| options | [TouchOptions](arkts-test-uitest-touchoptions-i.md) | No | the options for the drag operation. Only the 'pressure', 'speed', and 'duration' properties are applicable for this method. Setting other properties will result in a BusinessError 17000007. Default value: Refer to the default value of TouchOptions. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

## dumpLayout

```TypeScript
dumpLayout(savePath: string, displayId?: int): Promise<boolean>
```

Dumps the current layout information and saves it as a JSON file. This method is applicable to test scenarios where you need to analyze the hierarchy of UI controls or debug controls to locate issues. This API uses a promise to return the result.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Driver-dumpLayout(savePath: string, displayId?: int): Promise<boolean>--><!--Device-Driver-dumpLayout(savePath: string, displayId?: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| savePath | string | Yes | the path where to store the json, must be in the application sandbox directory. The path must be the [sandbox path](../../../file-management/app-sandbox-directory.md) of the current application. |
| displayId | int | No | Display ID. The value is an integer greater than or equal to 0. The default value is the default screen ID of the device. <br> **Note：**: If the input **displayId** does not exist, the exception **17000007** is reported. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | true if dump layout and file-storing are completed successfully,false otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

## findComponent

```TypeScript
findComponent(on: On): Promise<Component>
```

Searches for the target component based on the specified attributes. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-findComponent(on: On): Promise<Component>--><!--Device-Driver-findComponent(on: On): Promise<Component>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | Attributes of the target [Component](arkts-test-uitest-component-c.md). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Component](arkts-test-uitest-component-c.md)&gt; | Promise used to return the { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.text('next page'));
}
```

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.text('next page'));
}
```

## findComponent

```TypeScript
findComponent(on: On): Promise<Component | null>
```

Find the first matched [Component](arkts-test-uitest-component-c.md) on current UI.

**Since:** 23

<!--Device-Driver-findComponent(on: On): Promise<Component | null>--><!--Device-Driver-findComponent(on: On): Promise<Component | null>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | the attribute requirements of the target [Component](arkts-test-uitest-component-c.md). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Component](arkts-test-uitest-component-c.md) \| null&gt; | the first matched { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

See [findComponent](#findcomponent)

## findComponents

```TypeScript
findComponents(on: On): Promise<Array<Component>>
```

Searches for all matched components based on the specified attributes and saves them in a list. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-findComponents(on: On): Promise<Array<Component>>--><!--Device-Driver-findComponents(on: On): Promise<Array<Component>>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | Attributes of the target [Component](arkts-test-uitest-component-c.md). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[Component](arkts-test-uitest-component-c.md)&gt;&gt; | Promise used to return the list of { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let buttonList: Array<Component> = await driver.findComponents(ON.text('next page'));
}
```

```TypeScript
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let buttonList: Array<UiComponent> = await driver.findComponents(BY.text('next page'));
}
```

## findComponents

```TypeScript
findComponents(on: On): Promise<Array<Component> | null>
```

Find all the matched [Component](arkts-test-uitest-component-c.md)s on current UI.

**Since:** 23

<!--Device-Driver-findComponents(on: On): Promise<Array<Component> | null>--><!--Device-Driver-findComponents(on: On): Promise<Array<Component> | null>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | the attribute requirements of the target [Component](arkts-test-uitest-component-c.md). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[Component](arkts-test-uitest-component-c.md)&gt; \| null&gt; | the matched { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

See [findComponents](#findcomponents)

## findWindow

```TypeScript
findWindow(filter: WindowFilter): Promise<UiWindow>
```

Searches for a window based on the specified attributes. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-findWindow(filter: WindowFilter): Promise<UiWindow>--><!--Device-Driver-findWindow(filter: WindowFilter): Promise<UiWindow>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | [WindowFilter](arkts-test-uitest-windowfilter-i.md) | Yes | Attributes of the target [UiWindow](arkts-test-uitest-uiwindow-c.md). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[UiWindow](arkts-test-uitest-uiwindow-c.md)&gt; | Promise used to return the target { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
}
```

## findWindow

```TypeScript
findWindow(filter: WindowFilter): Promise<UiWindow | null>
```

Find the first matched [UiWindow](arkts-test-uitest-uiwindow-c.md) window.

**Since:** 23

<!--Device-Driver-findWindow(filter: WindowFilter): Promise<UiWindow | null>--><!--Device-Driver-findWindow(filter: WindowFilter): Promise<UiWindow | null>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | [WindowFilter](arkts-test-uitest-windowfilter-i.md) | Yes | the filter condition of the target [UiWindow](arkts-test-uitest-uiwindow-c.md). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[UiWindow](arkts-test-uitest-uiwindow-c.md) \| null&gt; | the first matched { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

See [findWindow](#findwindow)

## fling

```TypeScript
fling(from: Point, to: Point, stepLen: int, speed: int): Promise<void>
```

Simulates a fling operation. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-fling(from: Point, to: Point, stepLen: int, speed: int): Promise<void>--><!--Device-Driver-fling(from: Point, to: Point, stepLen: int, speed: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | Yes | Coordinates of the point where the finger touches the screen. |
| to | [Point](arkts-test-uitest-point-i.md) | Yes | Coordinates of the point where the finger leaves the screen. |
| stepLen | int | Yes | Sliding step length, in pixels. The value is an integer greater than or equal to 0. If the value is a negative number, error code 401 is returned. <br>Unit: px |
| speed | int | Yes | Fling speed, in px/s. The value ranges from 200 to 40000. If the set value is not in the range, the default value **600** is used. <br>Value range:[200, 40000] <br>Unit: px/s. <br>Throws error code 17000007 if negative. <br>Default value: 600 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.fling({ x: 500, y: 480 }, { x: 450, y: 480 }, 5, 600);
}
```

```TypeScript
// xxx.test.ets
import { Driver, UiDirection } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.fling(UiDirection.DOWN, 10000);
}
```

```TypeScript
// xxx.test.ets
import { Driver, UiDirection } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.fling(UiDirection.DOWN, 10000, 0);
}
```

## fling

```TypeScript
fling(direction: UiDirection, speed: int): Promise<void>
```

Simulates a fling operation with the specified direction and speed. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-fling(direction: UiDirection, speed: int): Promise<void>--><!--Device-Driver-fling(direction: UiDirection, speed: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| direction | [UiDirection](arkts-test-uitest-uidirection-e.md) | Yes | Direction of the fling operation. |
| speed | int | Yes | Scroll speed. <br>Value range:[200, 40000] <br>Unit: px/s. <br>Throws error code 401 if negative. <br>Default value: 600 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

See [fling](#fling)

## fling

```TypeScript
fling(direction: UiDirection, speed: int, displayId: int): Promise<void>
```

Simulates a fling operation on a specified display with the specified direction and speed. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-fling(direction: UiDirection, speed: int, displayId: int): Promise<void>--><!--Device-Driver-fling(direction: UiDirection, speed: int, displayId: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| direction | [UiDirection](arkts-test-uitest-uidirection-e.md) | Yes | Direction of the fling operation. |
| speed | int | Yes | Fling speed, in px/s. The value ranges from 200 to 40000. If the set value is not in the range, the default value **600** is used. <br>Value range:[200, 40000] <br>Unit: px/s. <br>Throws error code 401 if negative. <br>Default value: 600 |
| displayId | int | Yes | Display ID. The value is an integer greater than or equal to 0. <br> **Note：**: If the input **displayId** does not exist, the exception **401** is reported. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

See [fling](#fling)

## getDisplayDensity

```TypeScript
getDisplayDensity(): Promise<Point>
```

Obtains the display density of the current device. This API uses a promise to return the result.

> **NOTE：**&gt;
> This method can only be used to obtain the display density of the home screen. To obtain the display density
> of a specified screen, use [getDisplayDensity](#getdisplaydensity)(displayId: number).

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-getDisplayDensity(): Promise<Point>--><!--Device-Driver-getDisplayDensity(): Promise<Point>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Point](arkts-test-uitest-point-i.md)&gt; | Promise used to return the **Point** object. The density of the current device display is **Point.x*Point.y**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let density = await driver.getDisplayDensity();
}
```

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let density = await driver.getDisplayDensity(0);
}
```

## getDisplayDensity

```TypeScript
getDisplayDensity(displayId: int): Promise<Point>
```

Obtains the density of the specified display of the current device. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-getDisplayDensity(displayId: int): Promise<Point>--><!--Device-Driver-getDisplayDensity(displayId: int): Promise<Point>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | int | Yes | Display ID. The value is an integer greater than or equal to 0. <br> **Note：**: If the input **displayId** does not exist, the exception **17000007** is reported. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Point](arkts-test-uitest-point-i.md)&gt; | Promise used to return the **Point** object. The density of the specified display is **Point.x*Point.y**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

**Examples**

See [getDisplayDensity](#getdisplaydensity)

## getDisplayRotation

```TypeScript
getDisplayRotation(): Promise<DisplayRotation>
```

Obtains the display rotation of the current device. This API uses a promise to return the result.

> **NOTE：**&gt;
> This method can only be used to obtain the display rotation of the home screen. To obtain the display rotation
> of a specified screen, use [getDisplayRotation](#getdisplayrotation)(displayId: number).

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-getDisplayRotation(): Promise<DisplayRotation>--><!--Device-Driver-getDisplayRotation(): Promise<DisplayRotation>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[DisplayRotation](arkts-test-uitest-displayrotation-e.md)&gt; | Promise used to return the display rotation of the current device. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { DisplayRotation, Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let rotation: DisplayRotation = await driver.getDisplayRotation();
}
```

```TypeScript
// xxx.test.ets
import { DisplayRotation, Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let rotation: DisplayRotation = await driver.getDisplayRotation(0);
}
```

## getDisplayRotation

```TypeScript
getDisplayRotation(displayId: int): Promise<DisplayRotation>
```

Obtains the display rotation of the specified device. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-getDisplayRotation(displayId: int): Promise<DisplayRotation>--><!--Device-Driver-getDisplayRotation(displayId: int): Promise<DisplayRotation>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | int | Yes | Display ID. The value is an integer greater than or equal to 0. <br> **Note：**: If the input **displayId** does not exist, the exception **17000007** is reported. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[DisplayRotation](arkts-test-uitest-displayrotation-e.md)&gt; | Promise used to return the display rotation of the specified device. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

**Examples**

See [getDisplayRotation](#getdisplayrotation)

## getDisplaySize

```TypeScript
getDisplaySize(): Promise<Point>
```

Obtains the display size of the current device. This API uses a promise to return the result.

> **NOTE：**&gt;
> This method can only be used to obtain the display size of the home screen. To obtain the display size of a
> specified screen, use [getDisplaySize](#getdisplaysize)(displayId: number).

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-getDisplaySize(): Promise<Point>--><!--Device-Driver-getDisplaySize(): Promise<Point>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Point](arkts-test-uitest-point-i.md)&gt; | Promise used to return the **Point** object. The size of the current device screen is **Point.x * Point.y**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let size = await driver.getDisplaySize();
}
```

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let size = await driver.getDisplaySize(0);
}
```

## getDisplaySize

```TypeScript
getDisplaySize(displayId: int): Promise<Point>
```

Obtains the size of the specified display on the current device. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-getDisplaySize(displayId: int): Promise<Point>--><!--Device-Driver-getDisplaySize(displayId: int): Promise<Point>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | int | Yes | Display ID. The value is an integer greater than or equal to 0. <br> **Note：**: If the input **displayId** does not exist, the exception **17000007** is reported. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Point](arkts-test-uitest-point-i.md)&gt; | Promise used to return the **Point** object. The size of the specified display is **Point.x * Point.y**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

**Examples**

See [getDisplaySize](#getdisplaysize)

## injectKnucklePointerAction

```TypeScript
injectKnucklePointerAction(pointers: PointerMatrix, speed?: int): Promise<void>
```

Simulates a multi-point knuckle scrolling operation. This API uses a promise to return the result.

> **NOTE：**&gt;
> If the knuckle gesture is disabled on the device<!--RP4--><!--RP4End-->, 17000005 is returned.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-injectKnucklePointerAction(pointers: PointerMatrix, speed?: int): Promise<void>--><!--Device-Driver-injectKnucklePointerAction(pointers: PointerMatrix, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pointers | [PointerMatrix](arkts-test-uitest-pointermatrix-c.md) | Yes | Scroll trajectory, including the number of fingers and an array of coordinates along the trajectory.   **Note：**: Currently, only the single-finger operation is supported. The value of **fingers** in **PointerMatrix** must be set to **1**. |
| speed | int | No | Knuckle pointer action speed. <br>Value range:[200, 40000] <br>Unit: px/s. <br>Throws error code 17000007 if negative. <br>Default value: 600 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) | This operation is not supported. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

**Examples**

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
injectMultiPointerAction(pointers: PointerMatrix, speed?: int): Promise<boolean>
```

Injects a multi-finger operation into a device. This method applies to test scenarios where multi-finger gestures need to be simulated, such as pinching or spreading two fingers to zoom in or out on the image or swiping with multiple fingers to switch between pages. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-injectMultiPointerAction(pointers: PointerMatrix, speed?: int): Promise<boolean>--><!--Device-Driver-injectMultiPointerAction(pointers: PointerMatrix, speed?: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pointers | [PointerMatrix](arkts-test-uitest-pointermatrix-c.md) | Yes | Scroll trajectory, including the number of fingers and an array of coordinates along the trajectory. |
| speed | int | No | Pointer action speed, in px/s. <br>Value range:[200, 40000] <br>Unit: px/s. <br>Throws error code 401 if negative. <br>Default value: 600 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return whether the operation is successful. The value **true** indicates that the operation is successful, and **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { Driver, PointerMatrix } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let pointers: PointerMatrix = PointerMatrix.create(2, 5);
  pointers.setPoint(0, 0, { x: 250, y: 480 });
  pointers.setPoint(0, 1, { x: 250, y: 440 });
  pointers.setPoint(0, 2, { x: 250, y: 400 });
  pointers.setPoint(0, 3, { x: 250, y: 360 });
  pointers.setPoint(0, 4, { x: 250, y: 320 });
  pointers.setPoint(1, 0, { x: 250, y: 480 });
  pointers.setPoint(1, 1, { x: 250, y: 440 });
  pointers.setPoint(1, 2, { x: 250, y: 400 });
  pointers.setPoint(1, 3, { x: 250, y: 360 });
  pointers.setPoint(1, 4, { x: 250, y: 320 });
  await driver.injectMultiPointerAction(pointers);
}
```

## injectPenPointerAction

```TypeScript
injectPenPointerAction(pointers: PointerMatrix, speed?: int, pressure?: double): Promise<void>
```

Simulates a continuous multi-point pen injection operation. This method is applicable to test scenarios where custom track operations, such as continuous writing and drawing with a pen, need to be simulated. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-injectPenPointerAction(pointers: PointerMatrix, speed?: int, pressure?: double): Promise<void>--><!--Device-Driver-injectPenPointerAction(pointers: PointerMatrix, speed?: int, pressure?: double): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pointers | [PointerMatrix](arkts-test-uitest-pointermatrix-c.md) | Yes | Scroll trajectory, including the number of fingers and an array of coordinates along the trajectory. **Note：**: Currently, only the single-finger operation is supported. The value of **fingers** in **PointerMatrix** must be set to **1**. |
| speed | int | No | Pen pointer action speed. <br>Value range:[200, 40000] <br>Unit: px/s. <br>Throws error code 401 if negative. <br>Default value: 600 |
| pressure | double | No | Injection pressure. The value range is [0.0, 1.0]. The default value is **1.0**. If the value is **null** or **undefined**, the default value is used. If the value is out of the value range, error code 401 is thrown. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |  |

**Examples**

```TypeScript
// xxx.test.ets
import { Driver, PointerMatrix } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let pointer = PointerMatrix.create(1, 8);
  for (let step = 0; step < 8; step++) {
    pointer.setPoint(0, step, { x: 500, y: 1100 - 100 * step });
  }
  await driver.injectPenPointerAction(pointer, 600, 0.5);
}
```

## inputText

```TypeScript
inputText(p: Point, text: string): Promise<void>
```

Inputs text at a specified coordinate without clearing the original text in the component. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-inputText(p: Point, text: string): Promise<void>--><!--Device-Driver-inputText(p: Point, text: string): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | Yes | Coordinates of the end point. |
| text | string | Yes | Input text. Currently, English, Chinese, and special characters are supported. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.text('hello world'));
  await text.inputText('123');
}
```

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function mode_demo() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.text('hello world'));
  await text.inputText('123', { paste: true, addition: false });
}
```

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.type('TextInput'));
  let point = await text.getBoundsCenter();
  await driver.inputText(point, '123');
}
```

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.type('TextInput'));
  let point = await text.getBoundsCenter();
  await driver.inputText(point, '123', { paste: true, addition: false });
}

async function demo_Chinese() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.type('TextInput'));
  let point = await text.getBoundsCenter();
  await driver.inputText(point, 'Chinese&', { paste: false, addition: true });
  // Copy and paste Chinese and a special character to the end of the specified text.
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
inputText(p: Point, text: string, mode: InputTextMode): Promise<void>
```

Inputs text at a specified coordinate point in a specified input mode. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-inputText(p: Point, text: string, mode: InputTextMode): Promise<void>--><!--Device-Driver-inputText(p: Point, text: string, mode: InputTextMode): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | Yes | Coordinates of the end point. |
| text | string | Yes | Input text. Currently, English, Chinese, and special characters are supported. |
| mode | [InputTextMode](arkts-test-uitest-inputtextmode-i.md) | Yes | Text input mode. For details, see [InputTextMode](arkts-test-uitest-inputtextmode-i.md). **NOTE：**If **InputTextMode.addition** is set to **true**, the cursor moves to the end of the text and the specified text is input. If the value is **false**, the specified text is input at the coordinate point. <br> If the input text contains Chinese characters or special characters or contains more than 200 characters, the text is copied and pasted regardless of the value of [InputTextMode](arkts-test-uitest-inputtextmode-i.md).paste. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [801](../../errorcode-universal.md#801-api-not-supported) |  |

**Examples**

See [inputText](#inputtext)

## isComponentPresentWhenDrag

```TypeScript
isComponentPresentWhenDrag(on: On, from: Point, to: Point, speed?: int, duration?: int): Promise<boolean>
```

Drags from the start point to the end point and checks whether the target component exists. This method is applicable to verifying the dynamic UI elements that appear during the drag operation. For example, when dragging a file to a target folder, you can use this API to verify the highlight effect of the folder. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-isComponentPresentWhenDrag(on: On, from: Point, to: Point, speed?: int, duration?: int): Promise<boolean>--><!--Device-Driver-isComponentPresentWhenDrag(on: On, from: Point, to: Point, speed?: int, duration?: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | Attributes of the target [Component](arkts-test-uitest-component-c.md). |
| from | [Point](arkts-test-uitest-point-i.md) | Yes | Point object, which transfers the coordinates of the start point and the ID of the display to which the start point belongs. |
| to | [Point](arkts-test-uitest-point-i.md) | Yes | Point object, which transfers the coordinates of the target point and the ID of the display to which it belongs. <br> **Note：**: The target point and the start point must be on the same screen. Otherwise, the **17000007** exception is thrown. |
| speed | int | No | Drag speed. <br>Value range:[200, 40000] <br>Throws error code 17000007 if negative. <br>Default value: 600 |
| duration | int | No | Click duration, in ms. The value is an integer greater than or equal to 1500. The default value is 1500. If the value is less than 1500, the 17000007 error code is thrown. If the value is **null** or **undefined**, the default value is used. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return whether the target component exists during the dragging operation. The value **true** indicates that the target component exists, and **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

**Examples**

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
isComponentPresentWhenLongClick(on: On, point: Point, duration?: int): Promise<boolean>
```

Long-clicks at the specified coordinates and checks whether the target component exists. This method is applicable to verifying the UI elements that dynamically appear after a long-click, such as the context menu or edit button. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-isComponentPresentWhenLongClick(on: On, point: Point, duration?: int): Promise<boolean>--><!--Device-Driver-isComponentPresentWhenLongClick(on: On, point: Point, duration?: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | Attributes of the target [Component](arkts-test-uitest-component-c.md). |
| point | [Point](arkts-test-uitest-point-i.md) | Yes | Coordinates of the long-clicked point. |
| duration | int | No | Long-click duration, in ms. The value is an integer greater than or equal to 1500. The default value is 1500. If the value is less than 1500, the 17000007 error code is thrown. If the value is **null** or **undefined**, the default value is used. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return whether the target component exists during a long-click operation. The value **true** indicates that the target component exists, and **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

**Examples**

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
isComponentPresentWhenSwipe(on: On, from: Point, to: Point, speed?: int): Promise<boolean>
```

Swipes from the start point to the end point and checks whether the target component exists. This method is applicable to verifying the dynamic UI elements that appear during the swipe operation, for example, verifying whether the delete button appears when swiping is used to delete a list item. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-isComponentPresentWhenSwipe(on: On, from: Point, to: Point, speed?: int): Promise<boolean>--><!--Device-Driver-isComponentPresentWhenSwipe(on: On, from: Point, to: Point, speed?: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | Attributes of the target component. |
| from | [Point](arkts-test-uitest-point-i.md) | Yes | Point object, which transfers the coordinates of the start point and the ID of the display to which the start point belongs. |
| to | [Point](arkts-test-uitest-point-i.md) | Yes | Point object, which transfers the coordinates of the target point and the ID of the display to which it belongs. <br> **Note：**: The target point and the start point must be on the same screen. Otherwise, the **17000007** exception is thrown. |
| speed | int | No | Scroll speed. <br>Value range:[200, 40000] <br>Throws error code 17000007 if negative. <br>Default value: 600 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return whether the target component exists during the swiping operation.The value **true** indicates that the target component exists, and **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

**Examples**

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
knuckleKnock(pointers: Array<Point>, times: int): Promise<void>
```

Simulates a knuckle knock on the display. This API uses a promise to return the result.

> **NOTE：**&gt;
> If the knuckle gesture is disabled on the device<!--RP4--><!--RP4End-->, 17000005 is returned.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-knuckleKnock(pointers: Array<Point>, times: int): Promise<void>--><!--Device-Driver-knuckleKnock(pointers: Array<Point>, times: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pointers | Array&lt;[Point](arkts-test-uitest-point-i.md)&gt; | Yes | Array of knuckle knock coordinates on the display. The array length can be 1 or 2. If the value is out of range, error code 17000007 is thrown. |
| times | int | Yes | Number of consecutive knocks on the display. The value can be 1 or 2. If the value is out of range, error code 17000007 is thrown. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) | This operation is not supported. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

**Examples**

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
longClick(x: int, y: int): Promise<void>
```

Long-clicks the target coordinate point. This method can be used only on the default screen of the device, and the long-click duration cannot be customized. To specify a screen or long-click duration, use [longClickAt](#longclickat). This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-longClick(x: int, y: int): Promise<void>--><!--Device-Driver-longClick(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | int | Yes | Horizontal coordinate of the target point, in pixels. The value is an integer greater than or equal to 0. If the value is out of range, error code 401 is thrown. |
| y | int | Yes | Vertical coordinate of the target point, in pixels. The value is an integer greater than or equal to 0. If the value is out of range, error code 401 is thrown. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  await button.longClick();
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

## longClickAt

```TypeScript
longClickAt(point: Point, duration?: int): Promise<void>
```

Long-clicks the target coordinate point for a specified duration. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-longClickAt(point: Point, duration?: int): Promise<void>--><!--Device-Driver-longClickAt(point: Point, duration?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | Yes | Point object, which is used to transfer the target point information. |
| duration | int | No | Long-click duration, in ms. The value is an integer greater than or equal to 1500. The default value is 1500. If the value is less than 1500, the 17000007 error code is thrown. If the value is **null** or **undefined**, the default value is used. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

**Examples**

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

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Driver-longClickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>--><!--Device-Driver-longClickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | Yes | the coordinate point where the finger touches the screen. |
| options | [TouchOptions](arkts-test-uitest-touchoptions-i.md) | No | the options for the long click operation. Only the 'duration' and 'pressure' properties are applicable for this method. Setting other properties will result in a BusinessError 17000007. Default value: Refer to the default value of TouchOptions. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

## mouseClick

```TypeScript
mouseClick(p: Point, btnId: MouseButton, key1?: int, key2?: int): Promise<void>
```

Injects a mouse click action at the specified coordinates, with the optional key or key combination. This API uses a promise to return the result. For example, if the key code value is **2072**, the **Ctrl** button is pressed with the mouse click.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-mouseClick(p: Point, btnId: MouseButton, key1?: int, key2?: int): Promise<void>--><!--Device-Driver-mouseClick(p: Point, btnId: MouseButton, key1?: int, key2?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | Yes | Target coordinates of the mouse click. |
| btnId | [MouseButton](arkts-test-uitest-mousebutton-e.md) | Yes | Mouse button pressed. |
| key1 | int | No | First key code value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md). <br>Default value: 0 |
| key2 | int | No | Second key code value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md). <br>Default value: 0 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

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
mouseDoubleClick(p: Point, btnId: MouseButton, key1?: int, key2?: int): Promise<void>
```

Injects a double-click action at the specified coordinates, with the optional key or key combination. This API uses a promise to return the result. For example, if the key code value is **2072**, the **Ctrl** button is pressed with the double-click.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-mouseDoubleClick(p: Point, btnId: MouseButton, key1?: int, key2?: int): Promise<void>--><!--Device-Driver-mouseDoubleClick(p: Point, btnId: MouseButton, key1?: int, key2?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | Yes | Coordinates of the double-click. |
| btnId | [MouseButton](arkts-test-uitest-mousebutton-e.md) | Yes | Mouse button pressed. |
| key1 | int | No | First key code value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md). <br>Default value: 0 |
| key2 | int | No | Second key code value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md). <br>Default value: 0 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

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

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-mouseDrag(from: Point, to: Point, speed?: number): Promise<void>--><!--Device-Driver-mouseDrag(from: Point, to: Point, speed?: number): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | Yes | Coordinates of the start point. |
| to | [Point](arkts-test-uitest-point-i.md) | Yes | Coordinates of the end point. |
| speed | number | No | Mouse drag speed. <br>Value range:[200, 40000] <br>Unit: px/s. <br>Throws error code 401 if negative. <br>Default value: 600 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseDrag({ x: 100, y: 100 }, { x: 200, y: 200 }, 600);
}
```

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseDrag({ x: 100, y: 100 }, { x: 200, y: 200 }, 600, 2000);
}
```

## mouseDrag

```TypeScript
mouseDrag(from: Point, to: Point, speed?: int, duration?: int): Promise<void>
```

Drags the mouse from the start point to the end point. You can specify the dragging speed and the duration before dragging. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-mouseDrag(from: Point, to: Point, speed?: int, duration?: int): Promise<void>--><!--Device-Driver-mouseDrag(from: Point, to: Point, speed?: int, duration?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | Yes | Coordinates of the start point. |
| to | [Point](arkts-test-uitest-point-i.md) | Yes | Coordinates of the end point. |
| speed | int | No | Speed of mouse drag. <br>Value range:[200, 40000] <br>Unit: px/s. <br>Throws error code 401 if negative. <br>Default value: 600 |
| duration | int | No | Click duration, in ms. The value is an integer greater than or equal to 1500. The default value is 1500. If the value is less than 1500, error code 401 is thrown. If the value is **null** or **undefined**, the default value is used. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

See [mouseDrag](#mousedrag)

## mouseDragWithOptions

```TypeScript
mouseDragWithOptions(from: Point, to: Point, touchOptions?: TouchOptions, keyOptions?: KeyOptions): Promise<void>
```

Hold down the left mouse button and drag on the screen between the specified points, with optional touch and key settings.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Driver-mouseDragWithOptions(from: Point, to: Point, touchOptions?: TouchOptions, keyOptions?: KeyOptions): Promise<void>--><!--Device-Driver-mouseDragWithOptions(from: Point, to: Point, touchOptions?: TouchOptions, keyOptions?: KeyOptions): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | Yes | the starting point. |
| to | [Point](arkts-test-uitest-point-i.md) | Yes | the ending point. |
| touchOptions | [TouchOptions](arkts-test-uitest-touchoptions-i.md) | No | the touch options for speed and duration settings. Only 'speed' and 'duration' properties are valid in this method. Setting other properties will cause BusinessError 17000007. Default value: Refer to the default value of TouchOptions. |
| keyOptions | [KeyOptions](arkts-test-uitest-keyoptions-i.md) | No | the key options for key codes to press during drag. Default value: Refer to the default value of keyOptions. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

## mouseLongClick

```TypeScript
mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>
```

Injects a mouse long-click action at the specified coordinates, with the optional key or key combination. This API uses a promise to return the result. For example, if the key code value is **2072**, the **Ctrl** button is long-clicked with the mouse device.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>--><!--Device-Driver-mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | Yes | Coordinates of the long-click of the mouse device. |
| btnId | [MouseButton](arkts-test-uitest-mousebutton-e.md) | Yes | Mouse button pressed. |
| key1 | number | No | First key code value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md). <br>Default value: 0 |
| key2 | number | No | Second key code value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md). <br>Default value: 0 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { Driver, MouseButton } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseLongClick({ x: 248, y: 194 }, MouseButton.MOUSE_BUTTON_LEFT, 2072);
}
```

```TypeScript
// xxx.test.ets
import { Driver, MouseButton } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseLongClick({ x: 248, y: 194 }, MouseButton.MOUSE_BUTTON_LEFT, 2072, 0, 2000);
}
```

## mouseLongClick

```TypeScript
mouseLongClick(p: Point, btnId: MouseButton, key1?: int, key2?: int, duration?: int): Promise<void>
```

Injects a mouse long-click action at the specified coordinates, with the optional key or key combination and the specified duration. This API uses a promise to return the result. For example, if the key code value is **2072**, the **Ctrl** button is pressed with the long-click.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-mouseLongClick(p: Point, btnId: MouseButton, key1?: int, key2?: int, duration?: int): Promise<void>--><!--Device-Driver-mouseLongClick(p: Point, btnId: MouseButton, key1?: int, key2?: int, duration?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | Yes | Coordinates of the long-click of the mouse device. |
| btnId | [MouseButton](arkts-test-uitest-mousebutton-e.md) | Yes | Mouse button pressed. |
| key1 | int | No | First key code value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md). <br>Default value: 0 |
| key2 | int | No | Second key code value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md). <br>Default value: 0 |
| duration | int | No | Long-click duration, in ms. The value is an integer greater than or equal to 1500. The default value is 1500. If the value is less than 1500, error code 401 is thrown. If the value is **null** or **undefined**, the default value is used. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

See [mouseLongClick](#mouselongclick)

## mouseMoveTo

```TypeScript
mouseMoveTo(p: Point): Promise<void>
```

Moves the mouse cursor to the target point. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-mouseMoveTo(p: Point): Promise<void>--><!--Device-Driver-mouseMoveTo(p: Point): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | Yes | Coordinates of the end point. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

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
mouseMoveWithTrack(from: Point, to: Point, speed?: int): Promise<void>
```

Moves the mouse pointer from the start point to the end point, with a visible movement track. This method is applicable to test scenarios that depend on the mouse movement track, such as verification of the mouse hover effect and selecting an area by dragging with the mouse. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-mouseMoveWithTrack(from: Point, to: Point, speed?: int): Promise<void>--><!--Device-Driver-mouseMoveWithTrack(from: Point, to: Point, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | Yes | Coordinates of the start point. |
| to | [Point](arkts-test-uitest-point-i.md) | Yes | Coordinates of the end point. |
| speed | int | No | Mouse move speed. <br>Value range:[200, 40000] <br>Unit: px/s. <br>Throws error code 401 if negative. <br>Default value: 600 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

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

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number): Promise<void>--><!--Device-Driver-mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | Yes | Target coordinates of mouse scrolling. |
| down | boolean | Yes | Whether the mouse wheel scrolls downward. The value **true** indicates the mouse wheel scrolls downward, and **false** indicates the mouse wheel scrolls upward. |
| d | number | Yes | Number of ticks scrolled by the mouse wheel. A tick indicates a 120 px scroll at the mouse cursor position. The value is an integer greater than or equal to 0. If the value is a negative number, error code 401 is returned. |
| key1 | number | No | First key code value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md). <br>Default value: 0 |
| key2 | number | No | Second key code value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md). <br>Default value: 0 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseScroll({ x: 360, y: 640 }, true, 30, 2072);
}
```

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseScroll({ x: 360, y: 640 }, true, 30, 2072, 20);
}
```

## mouseScroll

```TypeScript
mouseScroll(p: Point, down: boolean, d: int, key1?: int, key2?: int, speed?: int): Promise<void>
```

Injects a mouse scroll action at the specified coordinates, with the optional key or key combination and the specified scroll speed. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-mouseScroll(p: Point, down: boolean, d: int, key1?: int, key2?: int, speed?: int): Promise<void>--><!--Device-Driver-mouseScroll(p: Point, down: boolean, d: int, key1?: int, key2?: int, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | Yes | Target coordinates of mouse scrolling. |
| down | boolean | Yes | Whether the mouse wheel scrolls downward. The value **true** indicates the mouse wheel scrolls downward, and **false** indicates the mouse wheel scrolls upward. |
| d | int | Yes | Number of ticks scrolled by the mouse wheel. A tick indicates a 120 px scroll at the mouse cursor position. The value is an integer greater than or equal to 0. If the value is a negative number, error code 401 is returned. |
| key1 | int | No | First key code value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md). <br>Default value: 0 |
| key2 | int | No | Second key code value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md). <br>Default value: 0 |
| speed | int | No | Scroll speed of the mouse wheel. <br>Value range:[1, 500] <br>Unit: ticks/s <br>Throws error code 401 if negative. <br>Default value: 20 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

See [mouseScroll](#mousescroll)

## penClick

```TypeScript
penClick(point: Point): Promise<void>
```

Simulates a pen click operation. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-penClick(point: Point): Promise<void>--><!--Device-Driver-penClick(point: Point): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | Yes | Coordinates of the clicked point. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |  |

**Examples**

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

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-penDoubleClick(point: Point): Promise<void>--><!--Device-Driver-penDoubleClick(point: Point): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | Yes | Coordinates of the double-clicked point. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |  |

**Examples**

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
penLongClick(point: Point, pressure?: double): Promise<void>
```

Simulates a pen long-click operation. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-penLongClick(point: Point, pressure?: double): Promise<void>--><!--Device-Driver-penLongClick(point: Point, pressure?: double): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | Yes | Coordinates of the long-clicked point. |
| pressure | double | No | Long-click pressure of the pen. The value ranges from 0.0 to 1.0. The default value is **1.0**. If the value is **null** or **undefined**, the default value is used. If the value is out of the value range, error code 401 is thrown. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |  |

**Examples**

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
penSwipe(startPoint: Point, endPoint: Point, speed?: int, pressure?: double): Promise<void>
```

Simulates a pen swipe operation. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-penSwipe(startPoint: Point, endPoint: Point, speed?: int, pressure?: double): Promise<void>--><!--Device-Driver-penSwipe(startPoint: Point, endPoint: Point, speed?: int, pressure?: double): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startPoint | [Point](arkts-test-uitest-point-i.md) | Yes | Coordinates of the start point. |
| endPoint | [Point](arkts-test-uitest-point-i.md) | Yes | Coordinates of the end point. |
| speed | int | No | Speed of pen swipe. <br>Value range:[200, 40000] <br>Unit: px/s. <br>Throws error code 401 if negative. <br>Default value: 600 |
| pressure | double | No | Swipe pressure of the pen. The value ranges from 0.0 to 1.0. The default value is **1.0**. If the value is **null** or **undefined**, the default value is used. If the value is out of the value range, error code 401 is thrown. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |  |

**Examples**

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

Simulates pressing the Back button. This API uses a promise to return the result.

> **NOTE：**&gt;
> This method only simulates pressing the Back button on the home screen. To simulate pressing the Back button
> on a specified screen, use pressBack(displayId: number).

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-pressBack(): Promise<void>--><!--Device-Driver-pressBack(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.pressBack();
}
```

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.pressBack(0);
}
```

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.pressBack();
}
```

## pressBack

```TypeScript
pressBack(displayId: int): Promise<void>
```

Simulates pressing the Back button on a specified screen. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-pressBack(displayId: int): Promise<void>--><!--Device-Driver-pressBack(displayId: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | int | Yes | Display ID. The value is an integer greater than or equal to 0. <br> **Note：**: If the input **displayId** does not exist, the exception **17000007** is reported. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

**Examples**

See [pressBack](#pressback)

## pressHome

```TypeScript
pressHome(): Promise<void>
```

Injects an operation of returning to the home screen on the device. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-pressHome(): Promise<void>--><!--Device-Driver-pressHome(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.pressHome();
}
```

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.pressHome(0);
}
```

## pressHome

```TypeScript
pressHome(displayId: int): Promise<void>
```

Injects an operation of returning to the home screen on the specified display. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-pressHome(displayId: int): Promise<void>--><!--Device-Driver-pressHome(displayId: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | int | Yes | Display ID. The value is an integer greater than or equal to 0. <br> **Note：**: If the input **displayId** does not exist, the exception **17000007** is reported. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

**Examples**

See [pressHome](#presshome)

## screenCap

```TypeScript
screenCap(savePath: string): Promise<boolean>
```

Captures the current screen and saves it as a PNG image to the given save path. This API uses a promise to return the result. This API can be used in scenarios where screenshots are supported.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-screenCap(savePath: string): Promise<boolean>--><!--Device-Driver-screenCap(savePath: string): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| savePath | string | Yes | File save path. The path must be the [sandbox path](../../../file-management/app-sandbox-directory.md) of the current application. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return whether the screenshot operation is successful. The value **true** indicates the screenshot operation is successful, and **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.screenCap('/data/storage/el2/base/cache/1.png');
}
```

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.screenCap('/data/storage/el2/base/cache/1.png', 0);
}
```

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.screenCap('/data/storage/el2/base/cache/1.png');
}
```

## screenCap

```TypeScript
screenCap(savePath: string, displayId: int): Promise<boolean>
```

Captures the specified screen and saves it as a PNG image to the given save path. This API uses a promise to return the result. This API can be used in scenarios where screenshots are supported.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-screenCap(savePath: string, displayId: int): Promise<boolean>--><!--Device-Driver-screenCap(savePath: string, displayId: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| savePath | string | Yes | File save path. The path must be the [sandbox path](../../../file-management/app-sandbox-directory.md) of the current application. |
| displayId | int | Yes | Display ID. The value is an integer greater than or equal to 0. <br> **Note：**: If the input **displayId** does not exist, the exception **401** is reported. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return whether the screenshot operation is successful. The value **true** indicates that the screen capture operation is successful, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

See [screenCap](#screencap)

## screenCapture

```TypeScript
screenCapture(savePath: string, rect?: Rect): Promise<boolean>
```

Captures the specified area of the current screen and saves the captured screenshot as a PNG image to the specified path. This API uses a promise to return the result. This API can be used in scenarios where screenshots are supported. Unlike screenCap, this API allows you to specify the screenshot area using the **rect** parameter instead of capturing the entire screen.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-screenCapture(savePath: string, rect?: Rect): Promise<boolean>--><!--Device-Driver-screenCapture(savePath: string, rect?: Rect): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| savePath | string | Yes | File save path. The path must be the [sandbox path](../../../file-management/app-sandbox-directory.md) of the current application. |
| rect | [Rect](arkts-test-uitest-rect-i.md) | No | Area of the screen to capture. The default value is the entire screen. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return whether the screenshot operation is successful. The value **true** indicates the screenshot operation is successful, and **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

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

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-setDisplayRotation(rotation: DisplayRotation): Promise<void>--><!--Device-Driver-setDisplayRotation(rotation: DisplayRotation): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rotation | [DisplayRotation](arkts-test-uitest-displayrotation-e.md) | Yes | Display rotation of the device. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

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

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-setDisplayRotationEnabled(enabled: boolean): Promise<void>--><!--Device-Driver-setDisplayRotationEnabled(enabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Whether the screen can be rotated. The value **true** indicates that the screen can be rotated, and **false** indicates the opposite. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

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
swipe(startx: int, starty: int, endx: int, endy: int, speed?: int): Promise<void>
```

Swipes from the start coordinate point to the target coordinate point. This method can be used only on the default screen of the device. To specify a screen, use [swipeBetween](#swipebetween). This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-swipe(startx: int, starty: int, endx: int, endy: int, speed?: int): Promise<void>--><!--Device-Driver-swipe(startx: int, starty: int, endx: int, endy: int, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startx | int | Yes | Horizontal coordinate of the start point, in pixels. The value is an integer greater than or equal to 0. If the value is out of range, error code 401 is thrown. |
| starty | int | Yes | Vertical coordinate of the start point, in pixels. The value is an integer greater than or equal to 0. If the value is out of range, error code 401 is thrown. |
| endx | int | Yes | Horizontal coordinate of the end point, in pixels. The value is an integer greater than or equal to 0. If the value is out of range, error code 401 is thrown. |
| endy | int | Yes | Vertical coordinate of the end point, in pixels. The value is an integer greater than or equal to 0. If the value is out of range, error code 401 is thrown. |
| speed | int | No | Swipe speed, in px/s. The value ranges from 200 to 40000. If the set value is not in the range, the default value **600** is used. <br>Value range:[200, 40000] <br>Unit: px/s. <br>Throws error code 401 if negative. <br>Default value: 600 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.swipe(100, 100, 200, 200, 600);
}
```

```TypeScript
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.swipe(100, 100, 200, 200);
}
```

## swipeBetween

```TypeScript
swipeBetween(from: Point, to: Point, speed?: int): Promise<void>
```

Swipes from the start coordinate point to the target coordinate point. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-swipeBetween(from: Point, to: Point, speed?: int): Promise<void>--><!--Device-Driver-swipeBetween(from: Point, to: Point, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | Yes | Point object, which transfers the coordinates of the start point and the ID of the display to which the start point belongs. |
| to | [Point](arkts-test-uitest-point-i.md) | Yes | Point object, which transfers the coordinates of the target point and the ID of the display to which it belongs. <br> **Note：**: The target point and the start point must be on the same screen. Otherwise, the **17000007** exception is thrown. |
| speed | int | No | Swipe speed, in px/s. The value ranges from 200 to 40000. If the set value is not in the range, the default value **600** is used. <br>Value range:[200, 40000] <br>Unit: px/s. <br>Throws error code 17000007 if negative. <br>Default value: 600 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

**Examples**

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

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Driver-swipeBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>--><!--Device-Driver-swipeBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [Point](arkts-test-uitest-point-i.md) | Yes | the coordinate point where the finger touches the screen. |
| to | [Point](arkts-test-uitest-point-i.md) | Yes | the coordinate point where the finger leaves the screen. |
| options | [TouchOptions](arkts-test-uitest-touchoptions-i.md) | No | the options for the swipe operation. Only the 'speed' and 'pressure' properties are applicable for this method. Setting other properties will result in a BusinessError 17000007. Default value: Refer to the default value of TouchOptions. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

## touchPadMultiFingerSwipe

```TypeScript
touchPadMultiFingerSwipe(fingers: int, direction: UiDirection, options?: TouchPadSwipeOptions): Promise<void>
```

Simulates a multi-finger swipe gesture on the touchpad. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-touchPadMultiFingerSwipe(fingers: int, direction: UiDirection, options?: TouchPadSwipeOptions): Promise<void>--><!--Device-Driver-touchPadMultiFingerSwipe(fingers: int, direction: UiDirection, options?: TouchPadSwipeOptions): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fingers | int | Yes | Number of fingers. The value can be 3 or 4. If the value is out of range, error code 401 is thrown. |
| direction | [UiDirection](arkts-test-uitest-uidirection-e.md) | Yes | Swipe direction. |
| options | [TouchPadSwipeOptions](arkts-test-uitest-touchpadswipeoptions-i.md) | No | Additional options for the multi-finger swipe gesture on the touchpad. The default values of the attributes in **[TouchPadSwipeOptions](arkts-test-uitest-touchpadswipeoptions-i.md)** are used by default. This parameter is used to specify whether the multi-finger swipe gesture ends with a pause and the swipe speed. It is applicable to scenarios where multi-finger swipe gestures are simulated on the touchpad, for example, swiping up with three fingers to switch the task view. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |  |
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) |  |

**Examples**

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
touchPadTwoFingersScroll(point: Point, direction: UiDirection, d: int, speed?: int): Promise<void>
```

Simulates a two-finger scroll gesture on the touchpad. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-touchPadTwoFingersScroll(point: Point, direction: UiDirection, d: int, speed?: int): Promise<void>--><!--Device-Driver-touchPadTwoFingersScroll(point: Point, direction: UiDirection, d: int, speed?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | [Point](arkts-test-uitest-point-i.md) | Yes | Point of the mouse cursor when the two-finger scrolling is performed on the touchpad. |
| direction | [UiDirection](arkts-test-uitest-uidirection-e.md) | Yes | Direction of two-finger scrolling on the touchpad. |
| d | int | Yes | Number of grids scrolled by two fingers on the touchpad. A tick indicates a 120 px scroll at the mouse cursor position. The value is an integer greater than or equal to 0. If the value is a negative number, the 17000007 error code is returned. |
| speed | int | No | Speed of two-finger scrolling on the touchpad. <br>Unit: ticks/s. <br>Value range: [1, 500] <br>Throws error code 17000007 if negative. <br>Default value: 20 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) | This operation is not supported. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. |

**Examples**

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

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-triggerCombineKeys(key0: number, key1: number, key2?: number): Promise<void>--><!--Device-Driver-triggerCombineKeys(key0: number, key1: number, key2?: number): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key0 | number | Yes | First key code value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md). |
| key1 | number | Yes | Second key code value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md). |
| key2 | number | No | Third key code value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md). <br>Default value: 0 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.triggerCombineKeys(2072, 2047, 2035);
}
```

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.triggerCombineKeys(2072, 2047, 2035, 0);
}
```

## triggerCombineKeys

```TypeScript
triggerCombineKeys(key0: int, key1: int, key2?: int, displayId?: int): Promise<void>
```

Triggers a combination key event based on the specified key code values on the specified screen. This API uses a promise to return the result. For example, if the key code value is (2072, 2019), the module finds and clicks the key combination that matches the value, for example, **Ctrl+C**.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-triggerCombineKeys(key0: int, key1: int, key2?: int, displayId?: int): Promise<void>--><!--Device-Driver-triggerCombineKeys(key0: int, key1: int, key2?: int, displayId?: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key0 | int | Yes | First key code value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md). |
| key1 | int | Yes | Second key code value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md). |
| key2 | int | No | Third key code value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md). <br>Default value: 0 |
| displayId | int | No | Display ID. The value is an integer greater than or equal to 0. The default value is the default display ID of the device. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

See [triggerCombineKeys](#triggercombinekeys)

## triggerKey

```TypeScript
triggerKey(keyCode: int): Promise<void>
```

Triggers a key event by passing the key code value. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-triggerKey(keyCode: int): Promise<void>--><!--Device-Driver-triggerKey(keyCode: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyCode | int | Yes | Key code value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';
import { KeyCode } from '@kit.InputKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.triggerKey(KeyCode.KEYCODE_BACK); // Back button
}
```

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';
import { KeyCode } from '@kit.InputKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.triggerKey(KeyCode.KEYCODE_BACK, 0); // Back button
}
```

```TypeScript
// xxx.test.ets
import { Driver, UiDriver } from '@kit.TestKit';
import { KeyCode } from '@kit.InputKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.triggerKey(KeyCode.KEYCODE_BACK); // Back button
}
```

## triggerKey

```TypeScript
triggerKey(keyCode: int, displayId: int): Promise<void>
```

Triggers a key event by passing the key code value on the specified screen. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Driver-triggerKey(keyCode: int, displayId: int): Promise<void>--><!--Device-Driver-triggerKey(keyCode: int, displayId: int): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyCode | int | Yes | Key code value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md). |
| displayId | int | Yes | Display ID. The value is an integer greater than or equal to 0. <br> **Note：**: If the input **displayId** does not exist, the exception **401** is reported. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

See [triggerKey](#triggerkey)

## triggerPenKey

```TypeScript
triggerPenKey(key: PenKey, mode: PenMode, operation: PenKeyOperation, options?: PenKeyOperationOptions): Promise<void>
```

Trigger pen key operation.Supported combinations:  
- HANDWRITING mode: HANDWRITING key with CLICK or DOUBLE_CLICK operation. - AIR_MOUSE mode: AIR_MOUSE key with CLICK or DOUBLE_CLICK operation (requires point in options), HANDWRITING key with CLICK or DOUBLE_CLICK operation, SMART key with CLICK operation. Other combinations will result in a BusinessError 17000007.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Driver-triggerPenKey(key: PenKey, mode: PenMode, operation: PenKeyOperation, options?: PenKeyOperationOptions): Promise<void>--><!--Device-Driver-triggerPenKey(key: PenKey, mode: PenMode, operation: PenKeyOperation, options?: PenKeyOperationOptions): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | [PenKey](arkts-test-uitest-penkey-e.md) | Yes | Stylus key type, which specifies the stylus key to be used for the operation, such as the handwriting key, air mouse key, and smart key. |
| mode | [PenMode](arkts-test-uitest-penmode-e.md) | Yes | Stylus mode, which specifies the current operation mode of the stylus, such as the handwriting mode or air mouse mode. |
| operation | [PenKeyOperation](arkts-test-uitest-penkeyoperation-e.md) | Yes | Stylus key operation mode, which specifies the operation mode of the key, such as single-tap or double-tap. |
| options | [PenKeyOperationOptions](arkts-test-uitest-penkeyoperationoptions-i.md) | No | Operation options, including optional coordinates. The default values are inherited from the default values of the properties in [PenKeyOperationOptions](arkts-test-uitest-penkeyoperationoptions-i.md). <br> **Note：**: When **mode** is set to [AIR_MOUSE](arkts-test-uitest-penmode-e.md#air_mouse) and **key** is set to [AIR_MOUSE](arkts-test-uitest-penkey-e.md#air_mouse), the **point** attribute in **options** must be set. Otherwise, error code 17000007 will be thrown. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) | This operation is not supported. |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) | Parameter verification failed. Unsupported key, mode, and operation combination. |

## waitForComponent

```TypeScript
waitForComponent(on: On, time: number): Promise<Component>
```

Searches for the target component based on the attributes within a specified time. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-waitForComponent(on: On, time: number): Promise<Component>--><!--Device-Driver-waitForComponent(on: On, time: number): Promise<Component>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | Attributes of the target [Component](arkts-test-uitest-component-c.md). |
| time | number | Yes | Duration for searching for the target [Component](arkts-test-uitest-component-c.md), in ms. The value is an integer greater than or equal to 0. <br>Unit: ms <br>Value range: The value should be &gt;= 0 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Component](arkts-test-uitest-component-c.md)&gt; | the first matched { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

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

Find the first matched [Component](arkts-test-uitest-component-c.md) on current UI during the time given.

**Since:** 23

<!--Device-Driver-waitForComponent(on: On, time: int): Promise<Component | null>--><!--Device-Driver-waitForComponent(on: On, time: int): Promise<Component | null>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes | the attribute requirements of the target [Component](arkts-test-uitest-component-c.md). |
| time | int | Yes | duration of finding in milliseconds. <br>Value range: The value should be &gt;= 0 <br>Unit: ms |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Component](arkts-test-uitest-component-c.md) \| null&gt; | the first matched { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

See [waitForComponent](#waitforcomponent)

## waitForIdle

```TypeScript
waitForIdle(idleTime: int, timeout: int): Promise<boolean>
```

Checks whether all components on the current UI are idle. This method is applicable to scenarios such as page redirection, animation playback, and loading. After calling this method, you can perform subsequent test operations only after the UI becomes stable. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-waitForIdle(idleTime: int, timeout: int): Promise<boolean>--><!--Device-Driver-waitForIdle(idleTime: int, timeout: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| idleTime | int | Yes | Idle time threshold, in ms. If the duration for which a component remains inactive reaches this threshold, it is considered as idle. The value must be an integer greater than or equal to 0. If the value is a negative number, error code 401 is returned. |
| timeout | int | Yes | Maximum waiting time, in ms. The value is an integer greater than or equal to 0. If the value is a negative number, error code 401 is returned. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return whether all components on the current UI are idle. The value true indicates that all components on the current UI are idle, and false indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

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

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Driver-wakeUpDisplay(): Promise<void>--><!--Device-Driver-wakeUpDisplay(): Promise<void>-End-->

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) | The API does not support concurrent calls. |

**Examples**

```TypeScript
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.wakeUpDisplay();
}
```

