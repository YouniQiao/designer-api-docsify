# Driver

The **Driver** class is the main entrance of the UiTest framework. This class provides APIs for features such as component matching/search, key injection, coordinate clicking/sliding, and screenshot. All APIs provided by this class, except **Driver.create()** and **Driver.createUIEventObserver()**, use an asynchronous method (promise) to return the result and must be invoked using **await**.

**Since:** 9

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from 'kits/@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from 'kits/@kit.TestKit';
```

## assertComponentExist

```TypeScript
assertComponentExist(on: On): Promise<void>
```

Asserts whether a component matches the specified attributes exists on the current page. If the assertion fails, a JS exception is thrown, causing the test case to fail. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [17000003](../errorcode-uitest.md#17000003-assertion-failure) |

## click

```TypeScript
click(x: number, y: number): Promise<void>
```

Clicks the target coordinate point. This method can be used only on the default screen of the device. To specify a screen, use [clickAt](#clickat). This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## clickAt

```TypeScript
clickAt(point: Point): Promise<void>
```

Clicks the target coordinate point. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

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

## clickAtWithOptions

```TypeScript
clickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>
```

Click on the specified location on the screen, with optional touch options.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

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

## create

```TypeScript
static create(): Driver
```

Creates a **Driver** object and returns the object created. This API is a static API.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Driver](arkts-test-uitest-driver-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [17000001](../errorcode-uitest.md#17000001-initialization-failure) |

## createUIEventObserver

```TypeScript
createUIEventObserver(): UIEventObserver
```

Creates a UI event listener [UIEventObserver](arkts-test-uitest-uieventobserver-i.md).

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [UIEventObserver](arkts-test-uitest-uieventobserver-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

## crownRotate

```TypeScript
crownRotate(d: number, speed?: number): Promise<void>
```

Injects a crown rotation event. You can specify the rotation speed. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

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

## delayMs

```TypeScript
delayMs(duration: number): Promise<void>
```

Delays a duration of time. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## doubleClick

```TypeScript
doubleClick(x: number, y: number): Promise<void>
```

Double-clicks the target coordinate point. This method can be used only on the default screen of the device. To specify a screen, use [doubleClickAt](#doubleclickat). This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## doubleClickAt

```TypeScript
doubleClickAt(point: Point): Promise<void>
```

Double-clicks the target coordinate point. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

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

## drag

```TypeScript
drag(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>
```

Drags from the start coordinate point to the target coordinate point. This method can be used only on the default screen of the device, and the number-click duration before dragging cannot be customized. To specify a screen or number-click duration, use [dragBetween](#dragbetween). This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## dragBetween

```TypeScript
dragBetween(from: Point, to: Point, speed?: number, duration?: number): Promise<void>
```

Drags from the start point to the target point. You can specify the drag speed and the click duration before dragging. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

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

## dragBetweenWithOptions

```TypeScript
dragBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>
```

Drag on the screen between the specified points with optional settings.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

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

## dumpLayout

```TypeScript
dumpLayout(savePath: string, displayId?: number): Promise<boolean>
```

Dumps the current layout information and saves it as a JSON file. This method is applicable to test scenarios where you need to analyze the hierarchy of UI controls or debug controls to locate issues. This API uses a promise to return the result.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

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

## findComponent

```TypeScript
findComponent(on: On): Promise<Component>
```

Searches for the target component based on the specified attributes. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## findComponents

```TypeScript
findComponents(on: On): Promise<Array<Component>>
```

Searches for all matched components based on the specified attributes and saves them in a list. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## findWindow

```TypeScript
findWindow(filter: WindowFilter): Promise<UiWindow>
```

Searches for a window based on the specified attributes. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## fling

```TypeScript
fling(from: Point, to: Point, stepLen: number, speed: number): Promise<void>
```

Simulates a fling operation. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## fling

```TypeScript
fling(direction: UiDirection, speed: number): Promise<void>
```

Simulates a fling operation with the specified direction and speed. This API uses a promise to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## fling

```TypeScript
fling(direction: UiDirection, speed: number, displayId: number): Promise<void>
```

Simulates a fling operation on a specified display with the specified direction and speed. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

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

## getDisplayDensity

```TypeScript
getDisplayDensity(): Promise<Point>
```

Obtains the display density of the current device. This API uses a promise to return the result.

> **NOTE：**&gt;
> This method can only be used to obtain the display density of the home screen. To obtain the display density
> of a specified screen, use [getDisplayDensity](#getdisplaydensity)(displayId: number).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Point](arkts-test-uitest-point-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

## getDisplayDensity

```TypeScript
getDisplayDensity(displayId: number): Promise<Point>
```

Obtains the density of the specified display of the current device. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

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

## getDisplayRotation

```TypeScript
getDisplayRotation(): Promise<DisplayRotation>
```

Obtains the display rotation of the current device. This API uses a promise to return the result.

> **NOTE：**&gt;
> This method can only be used to obtain the display rotation of the home screen. To obtain the display rotation
> of a specified screen, use [getDisplayRotation](#getdisplayrotation)(displayId: number).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DisplayRotation](arkts-test-uitest-displayrotation-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

## getDisplayRotation

```TypeScript
getDisplayRotation(displayId: number): Promise<DisplayRotation>
```

Obtains the display rotation of the specified device. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

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

## getDisplaySize

```TypeScript
getDisplaySize(): Promise<Point>
```

Obtains the display size of the current device. This API uses a promise to return the result.

> **NOTE：**&gt;
> This method can only be used to obtain the display size of the home screen. To obtain the display size of a
> specified screen, use [getDisplaySize](#getdisplaysize)(displayId: number).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Point](arkts-test-uitest-point-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

## getDisplaySize

```TypeScript
getDisplaySize(displayId: number): Promise<Point>
```

Obtains the size of the specified display on the current device. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

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

## injectKnucklePointerAction

```TypeScript
injectKnucklePointerAction(pointers: PointerMatrix, speed?: number): Promise<void>
```

Simulates a multi-point knuckle scrolling operation. This API uses a promise to return the result.

> **NOTE：**&gt;
> If the knuckle gesture is disabled on the device, 17000005 is returned.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

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
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

## injectMultiPointerAction

```TypeScript
injectMultiPointerAction(pointers: PointerMatrix, speed?: number): Promise<boolean>
```

Injects a multi-finger operation into a device. This method applies to test scenarios where multi-finger gestures need to be simulated, such as pinching or spreading two fingers to zoom in or out on the image or swiping with multiple fingers to switch between pages. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## injectPenPointerAction

```TypeScript
injectPenPointerAction(pointers: PointerMatrix, speed?: number, pressure?: number): Promise<void>
```

Simulates a continuous multi-point pen injection operation. This method is applicable to test scenarios where custom track operations, such as continuous writing and drawing with a pen, need to be simulated. This API uses a promise to return the result.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

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
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## inputText

```TypeScript
inputText(p: Point, text: string): Promise<void>
```

Inputs text at a specified coordinate without clearing the original text in the component. This API uses a promise to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## inputText

```TypeScript
inputText(p: Point, text: string, mode: InputTextMode): Promise<void>
```

Inputs text at a specified coordinate point in a specified input mode. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

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
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## isComponentPresentWhenDrag

```TypeScript
isComponentPresentWhenDrag(on: On, from: Point, to: Point, speed?: number, duration?: number): Promise<boolean>
```

Drags from the start point to the end point and checks whether the target component exists. This method is applicable to verifying the dynamic UI elements that appear during the drag operation. For example, when dragging a file to a target folder, you can use this API to verify the highlight effect of the folder. This API uses a promise to return the result.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

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

## isComponentPresentWhenLongClick

```TypeScript
isComponentPresentWhenLongClick(on: On, point: Point, duration?: number): Promise<boolean>
```

Long-clicks at the specified coordinates and checks whether the target component exists. This method is applicable to verifying the UI elements that dynamically appear after a number-click, such as the context menu or edit button. This API uses a promise to return the result.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

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

## isComponentPresentWhenSwipe

```TypeScript
isComponentPresentWhenSwipe(on: On, from: Point, to: Point, speed?: number): Promise<boolean>
```

Swipes from the start point to the end point and checks whether the target component exists. This method is applicable to verifying the dynamic UI elements that appear during the swipe operation, for example, verifying whether the delete button appears when swiping is used to delete a list item. This API uses a promise to return the result.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

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

## knuckleKnock

```TypeScript
knuckleKnock(pointers: Array<Point>, times: number): Promise<void>
```

Simulates a knuckle knock on the display. This API uses a promise to return the result.

> **NOTE：**&gt;
> If the knuckle gesture is disabled on the device, 17000005 is returned.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

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
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

## longClick

```TypeScript
longClick(x: number, y: number): Promise<void>
```

Long-clicks the target coordinate point. This method can be used only on the default screen of the device, and the number-click duration cannot be customized. To specify a screen or number-click duration, use [longClickAt](#longclickat). This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## longClickAt

```TypeScript
longClickAt(point: Point, duration?: number): Promise<void>
```

Long-clicks the target coordinate point for a specified duration. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

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

## longClickAtWithOptions

```TypeScript
longClickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>
```

LongClick on the specified location on the screen, with optional touch settings.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

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

## mouseClick

```TypeScript
mouseClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>
```

Injects a mouse click action at the specified coordinates, with the optional key or key combination. This API uses a promise to return the result. For example, if the key code value is **2072**, the **Ctrl** button is pressed with the mouse click.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## mouseDoubleClick

```TypeScript
mouseDoubleClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>
```

Injects a number-click action at the specified coordinates, with the optional key or key combination. This API uses a promise to return the result. For example, if the key code value is **2072**, the **Ctrl** button is pressed with the number-click.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## mouseDrag

```TypeScript
mouseDrag(from: Point, to: Point, speed?: number): Promise<void>
```

Drags the mouse pointer from the start point to the end point. This API uses a promise to return the result. For API version 26.0.0 and earlier, this API does not support cross-screen mouse dragging. The start point and end point must be on the same screen. Otherwise, error code 401 will be returned. Since API version 26.0.0, this API supports cross-screen mouse dragging.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## mouseDrag

```TypeScript
mouseDrag(from: Point, to: Point, speed?: number, duration?: number): Promise<void>
```

Drags the mouse from the start point to the end point. You can specify the dragging speed and the duration before dragging. This API uses a promise to return the result. For API version 26.0.0 and earlier, this API does not support cross-screen mouse dragging. The start point and end point must be on the same screen. Otherwise, error code 401 will be returned. Since API version 26.0.0, this API supports cross-screen mouse dragging.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

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

## mouseDragWithOptions

```TypeScript
mouseDragWithOptions(from: Point, to: Point, touchOptions?: TouchOptions, keyOptions?: KeyOptions): Promise<void>
```

Hold down the left mouse button and drag on the screen between the specified points, with optional touch and key settings.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

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

## mouseLongClick

```TypeScript
mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>
```

Injects a mouse number-click action at the specified coordinates, with the optional key or key combination. This API uses a promise to return the result. For example, if the key code value is **2072**, the **Ctrl** button is number-clicked with the mouse device.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## mouseLongClick

```TypeScript
mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number, duration?: number): Promise<void>
```

Injects a mouse number-click action at the specified coordinates, with the optional key or key combination and the specified duration. This API uses a promise to return the result. For example, if the key code value is **2072**, the **Ctrl** button is pressed with the number-click.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

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

## mouseMoveTo

```TypeScript
mouseMoveTo(p: Point): Promise<void>
```

Moves the mouse cursor to the target point. This API uses a promise to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## mouseMoveWithTrack

```TypeScript
mouseMoveWithTrack(from: Point, to: Point, speed?: number): Promise<void>
```

Moves the mouse pointer from the start point to the end point, with a visible movement track. This method is applicable to test scenarios that depend on the mouse movement track, such as verification of the mouse hover effect and selecting an area by dragging with the mouse. This API uses a promise to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## mouseScroll

```TypeScript
mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number): Promise<void>
```

Injects a mouse scroll action at the specified coordinates, with the optional key or key combination. This API uses a promise to return the result. For example, if the key code value is **2072**, the **Ctrl** button is pressed with mouse scrolling.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | Yes |
| [down](../../apis-arkui/arkts-components/arkts-arkui-focusmovement-i.md) | boolean | Yes |
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

## mouseScroll

```TypeScript
mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number, speed?: number): Promise<void>
```

Injects a mouse scroll action at the specified coordinates, with the optional key or key combination and the specified scroll speed. This API uses a promise to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | Yes |
| [down](../../apis-arkui/arkts-components/arkts-arkui-focusmovement-i.md) | boolean | Yes |
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

## penClick

```TypeScript
penClick(point: Point): Promise<void>
```

Simulates a pen click operation. This API uses a promise to return the result.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## penDoubleClick

```TypeScript
penDoubleClick(point: Point): Promise<void>
```

Simulates a pen number-click operation. This API uses a promise to return the result.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## penLongClick

```TypeScript
penLongClick(point: Point, pressure?: number): Promise<void>
```

Simulates a pen number-click operation. This API uses a promise to return the result.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

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
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## penSwipe

```TypeScript
penSwipe(startPoint: Point, endPoint: Point, speed?: number, pressure?: number): Promise<void>
```

Simulates a pen swipe operation. This API uses a promise to return the result.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

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
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## pressBack

```TypeScript
pressBack(): Promise<void>
```

Simulates pressing the Back button. This API uses a promise to return the result.

> **NOTE：**&gt;
> This method only simulates pressing the Back button on the home screen. To simulate pressing the Back button
> on a specified screen, use pressBack(displayId: number).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

## pressBack

```TypeScript
pressBack(displayId: number): Promise<void>
```

Simulates pressing the Back button on a specified screen. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

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

## pressHome

```TypeScript
pressHome(): Promise<void>
```

Injects an operation of returning to the home screen on the device. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |

## pressHome

```TypeScript
pressHome(displayId: number): Promise<void>
```

Injects an operation of returning to the home screen on the specified display. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

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

## screenCap

```TypeScript
screenCap(savePath: string): Promise<boolean>
```

Captures the current screen and saves it as a PNG image to the given save path. This API uses a promise to return the result. This API can be used in scenarios where screenshots are supported.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## screenCap

```TypeScript
screenCap(savePath: string, displayId: number): Promise<boolean>
```

Captures the specified screen and saves it as a PNG image to the given save path. This API uses a promise to return the result. This API can be used in scenarios where screenshots are supported.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

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

## screenCapture

```TypeScript
screenCapture(savePath: string, rect?: Rect): Promise<boolean>
```

Captures the specified area of the current screen and saves the captured screenshot as a PNG image to the specified path. This API uses a promise to return the result. This API can be used in scenarios where screenshots are supported. Unlike screenCap, this API allows you to specify the screenshot area using the **rect** parameter instead of capturing the entire screen.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## setDisplayRotation

```TypeScript
setDisplayRotation(rotation: DisplayRotation): Promise<void>
```

Sets the display rotation of the current scene. This API uses a promise to return the result. This API is applicable to scenarios where rotation is allowed. The rotation function can be enabled by setting **orientation=** to **auto_rotation** in the module.json5 configuration file.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## setDisplayRotationEnabled

```TypeScript
setDisplayRotationEnabled(enabled: boolean): Promise<void>
```

Enables or disables display rotation. This method is applicable to scenarios where the screen orientation needs to be locked during the test to maintain a specific display state, for example, testing the layout stability in landscape or portrait mode. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## swipe

```TypeScript
swipe(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>
```

Swipes from the start coordinate point to the target coordinate point. This method can be used only on the default screen of the device. To specify a screen, use [swipeBetween](#swipebetween). This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## swipeBetween

```TypeScript
swipeBetween(from: Point, to: Point, speed?: number): Promise<void>
```

Swipes from the start coordinate point to the target coordinate point. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

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

## swipeBetweenWithOptions

```TypeScript
swipeBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>
```

Swipe on the screen between the specified points with optional touch options.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

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

## touchPadMultiFingerSwipe

```TypeScript
touchPadMultiFingerSwipe(fingers: number, direction: UiDirection, options?: TouchPadSwipeOptions): Promise<void>
```

Simulates a multi-finger swipe gesture on the touchpad. This API uses a promise to return the result.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

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
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) |

## touchPadTwoFingersScroll

```TypeScript
touchPadTwoFingersScroll(point: Point, direction: UiDirection, d: number, speed?: number): Promise<void>
```

Simulates a two-finger scroll gesture on the touchpad. This API uses a promise to return the result.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

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
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

## triggerCombineKeys

```TypeScript
triggerCombineKeys(key0: number, key1: number, key2?: number): Promise<void>
```

Triggers a combination key event based on the specified key code values. This API uses a promise to return the result. For example, if the key code value is (2072, 2019), the module finds and clicks the key combination that matches the value, for example, **Ctrl+C**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## triggerCombineKeys

```TypeScript
triggerCombineKeys(key0: number, key1: number, key2?: number, displayId?: number): Promise<void>
```

Triggers a combination key event based on the specified key code values on the specified screen. This API uses a promise to return the result. For example, if the key code value is (2072, 2019), the module finds and clicks the key combination that matches the value, for example, **Ctrl+C**.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

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

## triggerKey

```TypeScript
triggerKey(keyCode: number): Promise<void>
```

Triggers a key event by passing the key code value. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## triggerKey

```TypeScript
triggerKey(keyCode: number, displayId: number): Promise<void>
```

Triggers a key event by passing the key code value on the specified screen. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

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

## triggerPenKey

```TypeScript
triggerPenKey(key: PenKey, mode: PenMode, operation: PenKeyOperation, options?: PenKeyOperationOptions): Promise<void>
```

Triggers a stylus key operation. This method is applicable to test scenarios where stylus switching needs to be simulated, for example, simulating a click operation in air mouse mode or invoking the smart key. This API uses a promise to return the result.Supported combinations:  
- HANDWRITING mode: HANDWRITING key with CLICK or DOUBLE_CLICK operation.  
- AIR_MOUSE mode: AIR_MOUSE key with CLICK or DOUBLE_CLICK operation (requires point in options),  
HANDWRITING key with CLICK or DOUBLE_CLICK operation, SMART key with CLICK operation. Other combinations will result in a BusinessError 17000007.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

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
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

## waitForComponent

```TypeScript
waitForComponent(on: On, time: number): Promise<Component>
```

Searches for the target component based on the attributes within a specified time. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## waitForIdle

```TypeScript
waitForIdle(idleTime: number, timeout: number): Promise<boolean>
```

Checks whether all components on the current UI are idle. This method is applicable to scenarios such as page redirection, animation playback, and loading. After calling this method, you can perform subsequent test operations only after the UI becomes stable. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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

## wakeUpDisplay

```TypeScript
wakeUpDisplay(): Promise<void>
```

Wakes up the current display. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-api-does-not-support-concurrent-calls) |
