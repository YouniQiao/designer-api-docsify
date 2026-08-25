# Driver

Driver类为uitest测试框架的总入口，提供控件匹配/查找，按键注入，坐标点击/滑动，截图等能力。通过create创建实例。 该类提供的方法除Driver.create()和Driver.createUIEventObserver()以外的所有方法都使用Promise方式作为异步方法，需使用await方式调用。

**起始版本：** 9

**系统能力：** SystemCapability.Test.UiTest

## 导入模块

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from 'kits/@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from 'kits/@kit.TestKit';
```

## assertComponentExist

```TypeScript
assertComponentExist(on: On): Promise<void>
```

断言API，用于断言当前界面是否存在满足给出的目标属性的控件。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000003](../errorcode-uitest.md#17000003-断言失败) |

## click

```TypeScript
click(x: number, y: number): Promise<void>
```

在目标坐标点单击。仅支持在设备默认屏幕上操作，如需指定屏幕请使用[clickAt](#clickat)。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## clickAt

```TypeScript
clickAt(point: Point): Promise<void>
```

在目标坐标点进行单击。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## clickAtWithOptions

```TypeScript
clickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>
```

点击屏幕上的指定位置，可选择触摸选项。

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## create

```TypeScript
static create(): Driver
```

静态方法，构造一个Driver对象，并返回该对象。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| [Driver](arkts-test-uitest-driver-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [17000001](../errorcode-uitest.md#17000001-初始化失败) |

## createUIEventObserver

```TypeScript
createUIEventObserver(): UIEventObserver
```

创建一个UI事件监听器。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| [UIEventObserver](arkts-test-uitest-uieventobserver-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## crownRotate

```TypeScript
crownRotate(d: number, speed?: number): Promise<void>
```

注入手表表冠旋转事件，可指定旋转速度。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## delayMs

```TypeScript
delayMs(duration: number): Promise<void>
```

在给定的时间内延时。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## doubleClick

```TypeScript
doubleClick(x: number, y: number): Promise<void>
```

在目标坐标点双击。仅支持在设备默认屏幕上操作，如需指定屏幕请使用[doubleClickAt](#doubleclickat)。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## doubleClickAt

```TypeScript
doubleClickAt(point: Point): Promise<void>
```

对目标坐标进行双击。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## drag

```TypeScript
drag(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>
```

从起始坐标点拖拽至目的坐标点。仅支持在设备默认屏幕上操作，不支持自定义拖拽前长按时长，如需指定屏幕或长按时长请使用[dragBetween](#dragbetween)。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## dragBetween

```TypeScript
dragBetween(from: Point, to: Point, speed?: number, duration?: number): Promise<void>
```

从起始坐标点拖拽至目标坐标点，支持指定拖拽速度和拖拽前长按时间。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## dragBetweenWithOptions

```TypeScript
dragBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>
```

在屏幕上拖拽指定的点之间，具有可选设置。

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## dumpLayout

```TypeScript
dumpLayout(savePath: string, displayId?: number): Promise<boolean>
```

Get the current layout information and save as file with json format.

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## findComponent

```TypeScript
findComponent(on: On): Promise<Component>
```

根据给出的目标控件属性要求查找目标控件。使用Promise异步回调。

**起始版本：** 9

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

## findComponents

```TypeScript
findComponents(on: On): Promise<Array<Component>>
```

根据给出的目标控件属性要求查找出所有匹配控件，以列表保存。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## findWindow

```TypeScript
findWindow(filter: WindowFilter): Promise<UiWindow>
```

通过指定窗口的属性来查找目标窗口。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## fling

```TypeScript
fling(from: Point, to: Point, stepLen: number, speed: number): Promise<void>
```

模拟手指滑动后脱离屏幕的快速滑动操作。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## fling

```TypeScript
fling(direction: UiDirection, speed: number): Promise<void>
```

指定方向和滑动速率，模拟手指滑动后脱离屏幕的快速滑动操作。使用Promise异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## fling

```TypeScript
fling(direction: UiDirection, speed: number, displayId: number): Promise<void>
```

指定方向、滑动速率和操作屏幕，模拟手指滑动后脱离屏幕的快速滑动操作。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## getDisplayDensity

```TypeScript
getDisplayDensity(): Promise<Point>
```

获取当前设备屏幕的分辨率。使用Promise异步回调。

**起始版本：** 9

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

## getDisplayDensity

```TypeScript
getDisplayDensity(displayId: number): Promise<Point>
```

获取当前设备指定屏幕的分辨率。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## getDisplayRotation

```TypeScript
getDisplayRotation(): Promise<DisplayRotation>
```

获取当前设备的屏幕显示方向。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DisplayRotation](arkts-test-uitest-displayrotation-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## getDisplayRotation

```TypeScript
getDisplayRotation(displayId: number): Promise<DisplayRotation>
```

获取当前设备指定屏幕的显示方向。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## getDisplaySize

```TypeScript
getDisplaySize(): Promise<Point>
```

获取当前设备的屏幕大小。使用Promise异步回调。

**起始版本：** 9

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

## getDisplaySize

```TypeScript
getDisplaySize(displayId: number): Promise<Point>
```

获取当前设备指定屏幕的大小。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## injectKnucklePointerAction

```TypeScript
injectKnucklePointerAction(pointers: PointerMatrix, speed?: number): Promise<void>
```

模拟指关节多点注入滑动操作。使用Promise异步回调。

> **说明：**&gt;
> 若设备关闭了指关节手势，则调用本接口返回17000005错误码。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000005](../errorcode-uitest.md#17000005-操作不支持) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## injectMultiPointerAction

```TypeScript
injectMultiPointerAction(pointers: PointerMatrix, speed?: number): Promise<boolean>
```

向设备注入多指操作。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## injectPenPointerAction

```TypeScript
injectPenPointerAction(pointers: PointerMatrix, speed?: number, pressure?: number): Promise<void>
```

模拟手写笔多点连续注入操作。使用Promise异步回调。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## inputText

```TypeScript
inputText(p: Point, text: string): Promise<void>
```

在指定坐标点输入文本，不清空组件内原有文本，直接在坐标处追加输入。使用Promise异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## inputText

```TypeScript
inputText(p: Point, text: string, mode: InputTextMode): Promise<void>
```

在指定坐标点输入文本，支持指定文本输入方式。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## isComponentPresentWhenDrag

```TypeScript
isComponentPresentWhenDrag(on: On, from: Point, to: Point, speed?: number, duration?: number): Promise<boolean>
```

从起始点拖拽至终止点，并查找目标控件是否存在。使用Promise异步回调。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## isComponentPresentWhenLongClick

```TypeScript
isComponentPresentWhenLongClick(on: On, point: Point, duration?: number): Promise<boolean>
```

在坐标点长按，并查找目标控件是否存在。使用Promise异步回调。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## isComponentPresentWhenSwipe

```TypeScript
isComponentPresentWhenSwipe(on: On, from: Point, to: Point, speed?: number): Promise<boolean>
```

从起始点滑向终止点，并查找目标控件是否存在。使用Promise异步回调。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## knuckleKnock

```TypeScript
knuckleKnock(pointers: Array<Point>, times: number): Promise<void>
```

模拟指关节敲击屏幕操作。使用Promise异步回调。

> **说明：**&gt;
> 若设备关闭了指关节手势，则调用本接口返回17000005错误码。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000005](../errorcode-uitest.md#17000005-操作不支持) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## longClick

```TypeScript
longClick(x: number, y: number): Promise<void>
```

在目标坐标点长按。仅支持在设备默认屏幕上操作且不支持自定义长按时长，如需指定屏幕或长按时长请使用[longClickAt](#longclickat)。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## longClickAt

```TypeScript
longClickAt(point: Point, duration?: number): Promise<void>
```

长按目标坐标点，支持指定长按时长。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## longClickAtWithOptions

```TypeScript
longClickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>
```

长按屏幕上的指定位置，可选择触摸设置。

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## mouseClick

```TypeScript
mouseClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>
```

在指定坐标点注入鼠标点击动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标点击动作。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## mouseDoubleClick

```TypeScript
mouseDoubleClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>
```

在指定坐标点注入鼠标双击动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标双击动作。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## mouseDrag

```TypeScript
mouseDrag(from: Point, to: Point, speed?: number): Promise<void>
```

鼠标按住鼠标左键从起始坐标点拖拽至终点坐标点。使用Promise异步回调。对于 API version 26.0.0 之前的版本，该接口不支持鼠标跨屏拖拽操作，起始点与终点需属于同一屏幕，否则将抛出401错误码；从 API version 26.0.0 开始，该接口支持鼠标跨屏拖拽操作。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## mouseDrag

```TypeScript
mouseDrag(from: Point, to: Point, speed?: number, duration?: number): Promise<void>
```

鼠标按住鼠标左键从起始坐标点拖拽至终点坐标点，支持指定拖拽速度和拖拽前长按时间。使用Promise异步回调。 对于 API version 26.0.0 之前的版本，该接口不支持鼠标跨屏拖拽操作，起始点与终点需属于同一屏幕，否则将抛出401错误码； 从 API version 26.0.0 开始，该接口支持鼠标跨屏拖拽操作。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## mouseDragWithOptions

```TypeScript
mouseDragWithOptions(from: Point, to: Point, touchOptions?: TouchOptions, keyOptions?: KeyOptions): Promise<void>
```

按住鼠标左键并在屏幕上的指定点之间拖动， 具有可选的触摸和按键设置。

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## mouseLongClick

```TypeScript
mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>
```

在指定坐标点注入鼠标长按动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标长按动作。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## mouseLongClick

```TypeScript
mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number, duration?: number): Promise<void>
```

在指定坐标点注入鼠标长按动作，支持同时按下对应键盘组合键，支持指定长按时长。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标长按动作。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## mouseMoveTo

```TypeScript
mouseMoveTo(p: Point): Promise<void>
```

将鼠标光标移到目标点。使用Promise异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## mouseMoveWithTrack

```TypeScript
mouseMoveWithTrack(from: Point, to: Point, speed?: number): Promise<void>
```

鼠标从起始坐标点滑向终点坐标点。使用Promise异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## mouseScroll

```TypeScript
mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number): Promise<void>
```

在指定坐标点注入鼠标滚轮滑动动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标滚轮滑动动作。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | 是 |
| [down](../../apis-arkui/arkts-components/arkts-arkui-focusmovement-i.md) | boolean | 是 |
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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## mouseScroll

```TypeScript
mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number, speed?: number): Promise<void>
```

在指定坐标点注入鼠标滚轮滑动动作，支持同时按下对应键盘组合键并且指定滑动速度。使用Promise异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| p | [Point](arkts-test-uitest-point-i.md) | 是 |
| [down](../../apis-arkui/arkts-components/arkts-arkui-focusmovement-i.md) | boolean | 是 |
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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## penClick

```TypeScript
penClick(point: Point): Promise<void>
```

模拟手写笔点击操作。使用Promise异步回调。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## penDoubleClick

```TypeScript
penDoubleClick(point: Point): Promise<void>
```

模拟手写笔双击操作。使用Promise异步回调。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## penLongClick

```TypeScript
penLongClick(point: Point, pressure?: number): Promise<void>
```

模拟手写笔长按操作。使用Promise异步回调。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## penSwipe

```TypeScript
penSwipe(startPoint: Point, endPoint: Point, speed?: number, pressure?: number): Promise<void>
```

模拟手写笔的滑动操作。使用Promise异步回调。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## pressBack

```TypeScript
pressBack(): Promise<void>
```

进行点击BACK键的操作。使用Promise异步回调。

**起始版本：** 9

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

## pressBack

```TypeScript
pressBack(displayId: number): Promise<void>
```

对指定屏幕进行点击BACK键的操作。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## pressHome

```TypeScript
pressHome(): Promise<void>
```

设备注入返回桌面操作。使用Promise异步回调。

**起始版本：** 9

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

## pressHome

```TypeScript
pressHome(displayId: number): Promise<void>
```

设备指定屏幕上注入返回桌面操作。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## screenCap

```TypeScript
screenCap(savePath: string): Promise<boolean>
```

捕获当前屏幕，并保存为PNG格式的图片至给出的保存路径中。使用Promise异步回调。适用于支持截屏的场景。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## screenCap

```TypeScript
screenCap(savePath: string, displayId: number): Promise<boolean>
```

捕获指定屏幕，并保存为PNG格式的图片至给出的保存路径中。使用Promise异步回调。适用于支持截屏的场景。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## screenCapture

```TypeScript
screenCapture(savePath: string, rect?: Rect): Promise<boolean>
```

捕获当前屏幕的指定区域，并保存为PNG格式的图片至给出的保存路径中。使用Promise异步回调。适用于支持截屏的场景。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## setDisplayRotation

```TypeScript
setDisplayRotation(rotation: DisplayRotation): Promise<void>
```

将当前场景的显示方向设置为指定的显示方向。使用Promise异步回调。适用于可旋转的应用场景。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## setDisplayRotationEnabled

```TypeScript
setDisplayRotationEnabled(enabled: boolean): Promise<void>
```

启用/禁用设备旋转屏幕的功能。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## swipe

```TypeScript
swipe(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>
```

从起始坐标点滑向目的坐标点。仅支持在设备默认屏幕上操作，如需指定屏幕请使用[swipeBetween](#swipebetween)。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## swipeBetween

```TypeScript
swipeBetween(from: Point, to: Point, speed?: number): Promise<void>
```

从起始坐标点滑向目标坐标点。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## swipeBetweenWithOptions

```TypeScript
swipeBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>
```

使用可选的触摸选项在指定点之间滑动屏幕。

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## touchPadMultiFingerSwipe

```TypeScript
touchPadMultiFingerSwipe(fingers: number, direction: UiDirection, options?: TouchPadSwipeOptions): Promise<void>
```

模拟触摸板多指滑动手势。使用Promise异步回调。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000005](../errorcode-uitest.md#17000005-操作不支持) |

## touchPadTwoFingersScroll

```TypeScript
touchPadTwoFingersScroll(point: Point, direction: UiDirection, d: number, speed?: number): Promise<void>
```

模拟触摸板双指滚动手势。使用Promise异步回调。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000005](../errorcode-uitest.md#17000005-操作不支持) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## triggerCombineKeys

```TypeScript
triggerCombineKeys(key0: number, key1: number, key2?: number): Promise<void>
```

通过给定的key值，找到对应组合键并点击。使用Promise异步回调。例如，Key值为(2072, 2019)时，找到key值对应的组合键并点击，如Ctrl+c。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## triggerCombineKeys

```TypeScript
triggerCombineKeys(key0: number, key1: number, key2?: number, displayId?: number): Promise<void>
```

通过给定的key值，找到对应组合键，并在指定屏幕下进行点击。使用Promise异步回调。例如，Key值为(2072, 2019)时，找到key值对应的组合键并点击，如Ctrl+c。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## triggerKey

```TypeScript
triggerKey(keyCode: number): Promise<void>
```

传入key值实现模拟点击对应按键的效果。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## triggerKey

```TypeScript
triggerKey(keyCode: number, displayId: number): Promise<void>
```

在指定屏幕，传入key值实现模拟点击对应按键的效果。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## triggerPenKey

```TypeScript
triggerPenKey(key: PenKey, mode: PenMode, operation: PenKeyOperation, options?: PenKeyOperationOptions): Promise<void>
```

Trigger pen key operation.Supported combinations:  
- HANDWRITING mode: HANDWRITING key with CLICK or DOUBLE_CLICK operation.  
- AIR_MOUSE mode: AIR_MOUSE key with CLICK or DOUBLE_CLICK operation (requires point in options),  
HANDWRITING key with CLICK or DOUBLE_CLICK operation, SMART key with CLICK operation. Other combinations will result in a BusinessError 17000007.

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

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
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |
| [17000005](../errorcode-uitest.md#17000005-操作不支持) |
| [17000007](../errorcode-uitest.md#17000007-参数不合法) |

## waitForComponent

```TypeScript
waitForComponent(on: On, time: number): Promise<Component>
```

在用户给定的时间内，持续查找满足控件属性要求的目标控件。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## waitForIdle

```TypeScript
waitForIdle(idleTime: number, timeout: number): Promise<boolean>
```

判断当前界面的所有控件是否已经空闲。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17000002](../errorcode-uitest.md#17000002-接口不支持并发调用) |

## wakeUpDisplay

```TypeScript
wakeUpDisplay(): Promise<void>
```

唤醒当前设备即设备亮屏。使用Promise异步回调。

**起始版本：** 9

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
