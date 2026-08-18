# Window

当前窗口实例，窗口管理器管理的基本单元。 下列API示例中都需先使用 [getLastWindow()](arkts-arkui-window-getlastwindow-f.md#getlastwindow)、 [createWindow()](arkts-arkui-window-createwindow-f.md#createwindow)、 [findWindow()](arkts-arkui-window-findwindow-f.md#findwindow)中的任一方法获取到Window实例（windowClass），再通过此实例调用对应方法。

**起始版本：** 23

<!--Device-window-interface Window--><!--Device-window-interface Window-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

## 导入模块

```TypeScript
```

## clearWindowMask

```TypeScript
clearWindowMask(): Promise<void>
```

清除异形窗口的掩码使其恢复为矩形窗口，使用Promise异步回调。异形窗口为非常规形状的窗口，掩码用于描述异形窗口的形状。此接口仅限子窗和全局悬浮窗可用。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Window-clearWindowMask(): Promise<void>--><!--Device-Window-clearWindowMask(): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## clientToGlobalDisplay

```TypeScript
clientToGlobalDisplay(winX: number, winY: number): Position
```

将相对于当前窗口左上角的坐标转换为相对于主屏幕左上角的全局坐标。 不支持在经过显示缩放的窗口中调用，例如手机或平板设备在非自由多窗模式下的悬浮窗场景。

**起始版本：** 23

<!--Device-Window-clientToGlobalDisplay(winX: int, winY: int): Position--><!--Device-Window-clientToGlobalDisplay(winX: int, winY: int): Position-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| winX | number | 是 |
| winY | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Position](arkts-arkui-display-position-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |
| [1300010](../errorcode-window.md#1300010-当前窗口模式不支持该操作) |

## convertOrientationAndRotation

```TypeScript
convertOrientationAndRotation(from: RotationInfoType, to: RotationInfoType, value: number): number
```

提供窗口方向、屏幕方向和屏幕角度互相转换的能力。 窗口方向指窗口所在屏幕的方向，以窗口模块对横竖屏的定义方式表示，窗口的方向分别用0、1、2和3表示竖屏、反向横屏、反向竖屏和横屏四个方向，其对横竖屏的定义与 [RotationChangeInfo](arkts-arkui-window-rotationchangeinfo-i.md#rotationchangeinfo)和枚举类 [Orientation](arkts-arkui-window-orientation-e.md#orientation)中对横竖屏的定义一致，如Orientation设置为LANDSCAPE时，窗口方向为横屏。 > **说明：** > > 示意图和表格展示了直板机窗口方向、屏幕方向和屏幕角度的关系。 > >  | 屏幕角度 | 屏幕方向 | 窗口方向 | | ------- | ------- | ------- | | 0 | PORTRAIT | PORTRAIT | | 90 | LANDSCAPE | LANDSCAPE_INVERTED | | 180 | PORTRAIT_INVERTED | PORTRAIT_INVERTED | | 270 | LANDSCAPE_INVERTED | LANDSCAPE |

**起始版本：** 23

<!--Device-Window-convertOrientationAndRotation(from: RotationInfoType, to: RotationInfoType, value: int): int--><!--Device-Window-convertOrientationAndRotation(from: RotationInfoType, to: RotationInfoType, value: int): int-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| from | [RotationInfoType](arkts-arkui-window-rotationinfotype-e.md) | 是 |
| to | [RotationInfoType](arkts-arkui-window-rotationinfotype-e.md) | 是 |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## createSubWindowWithOptions

```TypeScript
createSubWindowWithOptions(name: string, options: SubWindowOptions): Promise<Window>
```

创建主窗口、子窗口或悬浮窗下的子窗口，使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-createSubWindowWithOptions(name: string, options: SubWindowOptions): Promise<Window>--><!--Device-Window-createSubWindowWithOptions(name: string, options: SubWindowOptions): Promise<Window>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| options | [SubWindowOptions](arkts-arkui-window-subwindowoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Window](arkts-arkui-window-window-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## destroy

```TypeScript
destroy(callback: AsyncCallback<void>): void
```

销毁当前窗口，使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用 > [destroyWindow()](#destroywindow)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [destroyWindow](#destroywindow)(callback: AsyncCallback&lt;void&gt;)

<!--Device-Window-destroy(callback: AsyncCallback<void>): void--><!--Device-Window-destroy(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## destroy

```TypeScript
destroy(): Promise<void>
```

销毁当前窗口，使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用[destroyWindow()](#destroywindow)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [destroyWindow](#destroywindow)()

<!--Device-Window-destroy(): Promise<void>--><!--Device-Window-destroy(): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## destroyWindow

```TypeScript
destroyWindow(callback: AsyncCallback<void>): void
```

销毁当前窗口，使用callback异步回调，支持系统窗口及应用子窗口，全局悬浮窗和模态窗。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-destroyWindow(callback: AsyncCallback<void>): void--><!--Device-Window-destroyWindow(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## destroyWindow

```TypeScript
destroyWindow(): Promise<void>
```

销毁当前窗口，使用Promise异步回调，支持系统窗口及应用子窗口，全局悬浮窗和模态窗。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-destroyWindow(): Promise<void>--><!--Device-Window-destroyWindow(): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## disableLandscapeMultiWindow

```TypeScript
disableLandscapeMultiWindow(): Promise<void>
```

应用部分界面支持横向布局时，在退出该界面时去使能，去使能后不支持进入横向多窗。 此接口只对应用主窗口生效，且需要在module.json5配置文件中[abilities](../../../quick-start/module-configuration-file.md#abilities标签)标签中配 置preferMultiWindowOrientation属性为"landscape_auto"。

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-Window-disableLandscapeMultiWindow(): Promise<void>--><!--Device-Window-disableLandscapeMultiWindow(): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## enableLandscapeMultiWindow

```TypeScript
enableLandscapeMultiWindow(): Promise<void>
```

应用部分界面支持横向布局时，在进入该界面时使能，使能后可支持进入横向多窗。不建议竖向布局界面使用。 此接口只对应用主窗口生效，且需要在module.json5配置文件中[abilities](../../../quick-start/module-configuration-file.md#abilities标签)标签中配 置preferMultiWindowOrientation属性为"landscape_auto"。

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-Window-enableLandscapeMultiWindow(): Promise<void>--><!--Device-Window-enableLandscapeMultiWindow(): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## getAvoidArea

```TypeScript
getAvoidArea(type: AvoidAreaType, callback: AsyncCallback<AvoidArea>): void
```

获取当前窗口内容规避的区域；如系统栏区域、刘海屏区域、手势区域、软键盘区域等与窗口内容重叠时，需要窗口内容避让的区域。 主窗口/子窗口： - [自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态的自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）下， 仅存在固定态软键盘（[AvoidAreaType](arkts-arkui-window-avoidareatype-e.md#avoidareatype)为TYPE_KEYBOARD）类型的避让区域。 - 主窗口在非自由窗口状态的自由悬浮窗口模式下，仅存在系统栏（[AvoidAreaType](arkts-arkui-window-avoidareatype-e.md#avoidareatype)为TYPE_SYSTEM）类型的避让区域。 - 主窗口在其余场景下，仅当在非自由悬浮窗口模式下或设备类型为Phone和Tablet，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。 - 子窗口在非自由窗口状态或非自由悬浮窗口模式下，仅当窗口的位置和大小与主窗口一致时，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。 全局悬浮窗、模态窗或系统窗口： - 仅在调用[setSystemAvoidAreaEnabled](#setsystemavoidareaenabled)方法使能后，才能通过此接口获取计算后的避让区域，否则获取的避让区域 为空。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用[getWindowAvoidArea()](#getwindowavoidarea)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getWindowAvoidArea](#getwindowavoidarea)

<!--Device-Window-getAvoidArea(type: AvoidAreaType, callback: AsyncCallback<AvoidArea>): void--><!--Device-Window-getAvoidArea(type: AvoidAreaType, callback: AsyncCallback<AvoidArea>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [AvoidAreaType](arkts-arkui-window-avoidareatype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AvoidArea](arkts-arkui-window-avoidarea-i.md)&gt; | 是 |

## getAvoidArea

```TypeScript
getAvoidArea(type: AvoidAreaType): Promise<AvoidArea>
```

获取当前窗口内容规避的区域；如系统栏区域、刘海屏区域、手势区域、软键盘区域等与窗口内容重叠时，需要窗口内容避让的区域。 主窗口/子窗口： - [自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态的自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）下， 仅存在固定态软键盘（[AvoidAreaType](arkts-arkui-window-avoidareatype-e.md#avoidareatype)为TYPE_KEYBOARD）类型的避让区域。 - 主窗口在非自由窗口状态的自由悬浮窗口模式下，仅存在系统栏（[AvoidAreaType](arkts-arkui-window-avoidareatype-e.md#avoidareatype)为TYPE_SYSTEM）类型的避让区域。 - 主窗口在其余场景下，仅当在非自由悬浮窗口模式下或设备类型为Phone和Tablet，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。 - 子窗口在非自由窗口状态或非自由悬浮窗口模式下，仅当窗口的位置和大小与主窗口一致时，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。 全局悬浮窗、模态窗或系统窗口： - 仅在调用[setSystemAvoidAreaEnabled](#setsystemavoidareaenabled)方法使能后，才能通过此接口获取计算后的避让区域，否则获取的避让区域 为空。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用[getWindowAvoidArea()](#getwindowavoidarea)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getWindowAvoidArea](#getwindowavoidarea)

<!--Device-Window-getAvoidArea(type: AvoidAreaType): Promise<AvoidArea>--><!--Device-Window-getAvoidArea(type: AvoidAreaType): Promise<AvoidArea>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [AvoidAreaType](arkts-arkui-window-avoidareatype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AvoidArea](arkts-arkui-window-avoidarea-i.md)&gt; |

## getColorSpace

```TypeScript
getColorSpace(): Promise<ColorSpace>
```

获取当前窗口色域模式，使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[getWindowColorSpace()](#getwindowcolorspace)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getWindowColorSpace](#getwindowcolorspace)

<!--Device-Window-getColorSpace(): Promise<ColorSpace>--><!--Device-Window-getColorSpace(): Promise<ColorSpace>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;ColorSpace & gt; |

## getColorSpace

```TypeScript
getColorSpace(callback: AsyncCallback<ColorSpace>): void
```

获取当前窗口色域模式，使用callback异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用[getWindowColorSpace()](#getwindowcolorspace)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getWindowColorSpace](#getwindowcolorspace)

<!--Device-Window-getColorSpace(callback: AsyncCallback<ColorSpace>): void--><!--Device-Window-getColorSpace(callback: AsyncCallback<ColorSpace>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ColorSpace&gt; | 是 |

## getDecorButtonStyle

```TypeScript
getDecorButtonStyle(): DecorButtonStyle
```

获取装饰栏按钮样式，仅对主窗和子窗生效。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-getDecorButtonStyle(): DecorButtonStyle--><!--Device-Window-getDecorButtonStyle(): DecorButtonStyle-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| [DecorButtonStyle](arkts-arkui-window-decorbuttonstyle-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## getGlobalRect

```TypeScript
getGlobalRect(): Rect
```

获取窗口在其所在物理屏幕上的真实显示区域，同步接口。 在某些设备上，窗口显示时可能经过了缩放，此接口可以获取缩放后窗口在屏幕上的真实位置和大小。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-getGlobalRect(): Rect--><!--Device-Window-getGlobalRect(): Rect-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## getImmersiveModeEnabledState

```TypeScript
getImmersiveModeEnabledState(): boolean
```

查询当前窗口是否开启沉浸式布局。 仅支持主窗和子窗调用。 返回值与[setImmersiveModeEnabledState()](#setimmersivemodeenabledstate)以及 [setWindowLayoutFullScreen()](#setwindowlayoutfullscreen)设置结果一致，若 未调用上述两个接口则默认返回false。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-getImmersiveModeEnabledState(): boolean--><!--Device-Window-getImmersiveModeEnabledState(): boolean-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## getParentWindow

```TypeScript
getParentWindow(): Window
```

获取子窗口的父窗口。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-getParentWindow(): Window--><!--Device-Window-getParentWindow(): Window-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| [Window](arkts-arkui-window-window-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
| [1300009](../errorcode-window.md#1300009-父窗口无效) |

## getPreferredOrientation

```TypeScript
getPreferredOrientation(): Orientation
```

获取窗口的显示方向属性。未指定方向时，返回window.Orientation.UNSPECIFIED。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-getPreferredOrientation(): Orientation--><!--Device-Window-getPreferredOrientation(): Orientation-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| [Orientation](arkts-arkui-window-orientation-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## getProperties

```TypeScript
getProperties(callback: AsyncCallback<WindowProperties>): void
```

获取当前窗口的属性，使用callback异步回调，返回WindowProperties。 > **说明：** > > 从API version 6开始支持，从API version 9开始废弃，建议使用[getWindowProperties()](#getwindowproperties)替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [getWindowProperties](#getwindowproperties)

<!--Device-Window-getProperties(callback: AsyncCallback<WindowProperties>): void--><!--Device-Window-getProperties(callback: AsyncCallback<WindowProperties>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[WindowProperties](arkts-arkui-window-windowproperties-i.md)&gt; | 是 |

## getProperties

```TypeScript
getProperties(): Promise<WindowProperties>
```

获取当前窗口的属性，使用Promise异步回调，返回WindowProperties。 > **说明：** > > 从API version 6开始支持，从API version 9开始废弃，建议使用[getWindowProperties()](#getwindowproperties)替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [getWindowProperties](#getwindowproperties)

<!--Device-Window-getProperties(): Promise<WindowProperties>--><!--Device-Window-getProperties(): Promise<WindowProperties>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;[WindowProperties](arkts-arkui-window-windowproperties-i.md)&gt; |

## getStatusBarProperty

```TypeScript
getStatusBarProperty(): StatusBarProperty
```

获取主窗口状态栏的属性，如状态栏文字颜色。 子窗口不支持查询，调用会返回错误码1300004。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-getStatusBarProperty(): StatusBarProperty--><!--Device-Window-getStatusBarProperty(): StatusBarProperty-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| [StatusBarProperty](arkts-arkui-window-statusbarproperty-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## getSubWindowZLevel

```TypeScript
getSubWindowZLevel(): number
```

获取当前子窗口层级级别。不支持主窗、系统窗调用。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-getSubWindowZLevel(): int--><!--Device-Window-getSubWindowZLevel(): int-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## getTitleButtonRect

```TypeScript
getTitleButtonRect(): TitleButtonRect
```

获取主窗口或启用装饰的子窗口的标题栏上的最小化、最大化、关闭按钮矩形区域。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-getTitleButtonRect(): TitleButtonRect--><!--Device-Window-getTitleButtonRect(): TitleButtonRect-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| [TitleButtonRect](arkts-arkui-window-titlebuttonrect-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## getUIContext

```TypeScript
getUIContext() : UIContext
```

获取UIContext实例。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-getUIContext() : UIContext--><!--Device-Window-getUIContext() : UIContext-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## getWindowAvoidArea

```TypeScript
getWindowAvoidArea(type: AvoidAreaType): AvoidArea
```

获取当前窗口避让区域。 主窗口/子窗口： - [自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态的自由悬浮窗口模式（即窗口模式为 [window.WindowStatusType.FLOATING](arkts-arkui-window-windowstatustype-e.md#windowstatustype)）下，仅存在固定态软键盘（ [AvoidAreaType](arkts-arkui-window-avoidareatype-e.md#avoidareatype)为TYPE_KEYBOARD）类型的避让区域。 - 主窗口在非自由窗口状态的自由悬浮窗口模式下，仅存在系统栏（[AvoidAreaType](arkts-arkui-window-avoidareatype-e.md#avoidareatype)为TYPE_SYSTEM）类型的避让区域。 - 主窗口在其余场景下，仅当在非自由悬浮窗口模式下或设备类型为Phone和Tablet，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。 - 子窗口在非自由窗口状态或非自由悬浮窗口模式下，仅当窗口的位置和大小与主窗口一致时，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。 全局悬浮窗、模态窗或系统窗口： - 仅在调用[setSystemAvoidAreaEnabled](#setsystemavoidareaenabled)方法使能后，才能通过此接口获取避让区域，否则获取的避让区域为空。 该接口一般适用于两种场景： - 在[onWindowStageCreate()](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#onwindowstagecreate)方法中，获取应用启动时的初始布局避让区域时可 调用该接口。 - 当应用内子窗需要临时显示，对显示内容做布局避让时可调用该接口。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-getWindowAvoidArea(type: AvoidAreaType): AvoidArea--><!--Device-Window-getWindowAvoidArea(type: AvoidAreaType): AvoidArea-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [AvoidAreaType](arkts-arkui-window-avoidareatype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [AvoidArea](arkts-arkui-window-avoidarea-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## getWindowAvoidAreaIgnoringVisibility

```TypeScript
getWindowAvoidAreaIgnoringVisibility(type: AvoidAreaType): AvoidArea
```

获取当前应用窗口的避让区域，即使避让区域当前处于不可见状态。 主窗口/子窗口： - 主窗口在非[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态的自由悬浮窗口模式（即窗口模式为 [window.WindowStatusType.FLOATING](arkts-arkui-window-windowstatustype-e.md#windowstatustype)）下，仅存在系统栏（ [AvoidAreaType](arkts-arkui-window-avoidareatype-e.md#avoidareatype)为TYPE_SYSTEM）类型的避让区域。 - 主窗口在其余场景下，仅当在非自由悬浮窗口模式下或设备类型为Phone和Tablet，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。 - 子窗口在非自由窗口状态或非自由悬浮窗口模式下，仅当窗口的位置和大小与主窗口一致时，才能通过此接口获取计算后的避让区域，否则获取的避让区域为空。 全局悬浮窗、模态窗或系统窗口： - 仅在调用[setSystemAvoidAreaEnabled](#setsystemavoidareaenabled)方法使能后，才能通过此接口获取计算后的避让区域，否则获取的避让区域 为空。

**起始版本：** 23

<!--Device-Window-getWindowAvoidAreaIgnoringVisibility(type: AvoidAreaType): AvoidArea--><!--Device-Window-getWindowAvoidAreaIgnoringVisibility(type: AvoidAreaType): AvoidArea-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [AvoidAreaType](arkts-arkui-window-avoidareatype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [AvoidArea](arkts-arkui-window-avoidarea-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |

## getWindowColorSpace

```TypeScript
getWindowColorSpace(): ColorSpace
```

获取当前窗口色域模式。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-getWindowColorSpace(): ColorSpace--><!--Device-Window-getWindowColorSpace(): ColorSpace-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| [ColorSpace](arkts-arkui-window-colorspace-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## getWindowCornerRadius

```TypeScript
getWindowCornerRadius(): number
```

该接口用于获取子窗或悬浮窗的圆角半径值，在未调用[setWindowCornerRadius()](#setwindowcornerradius)接口设置窗口圆角半径值时，调用此接口可获取 窗口默认圆角半径值。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-getWindowCornerRadius(): double--><!--Device-Window-getWindowCornerRadius(): double-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## getWindowDecorHeight

```TypeScript
getWindowDecorHeight(): number
```

对存在标题栏和三键区的窗口形态生效，用于获取窗口的标题栏高度。如果使用Stage模型，该接口需要在 [loadContent()](#loadcontent) 或[setUIContent()](#setuicontent)调用生效后使用。 由于系统像素转换可能存在精度误差，调用[setWindowDecorHeight()](#setwindowdecorheight)设置的值与获取的值可能存在1vp的差异。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-getWindowDecorHeight(): int--><!--Device-Window-getWindowDecorHeight(): int-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## getWindowDecorVisible

```TypeScript
getWindowDecorVisible(): boolean
```

查询窗口标题栏是否可见。如果使用Stage模型，该接口需要在 [loadContent()](#loadcontent) 或[setUIContent()](#setuicontent)调用生效后使用。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-getWindowDecorVisible(): boolean--><!--Device-Window-getWindowDecorVisible(): boolean-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## getWindowDensityInfo

```TypeScript
getWindowDensityInfo(): WindowDensityInfo
```

获取当前窗口所在屏幕的系统显示大小缩放系数、系统默认显示大小缩放系数和自定义显示大小缩放系数信息。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-getWindowDensityInfo(): WindowDensityInfo--><!--Device-Window-getWindowDensityInfo(): WindowDensityInfo-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| [WindowDensityInfo](arkts-arkui-window-windowdensityinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## getWindowLimits

```TypeScript
getWindowLimits(): WindowLimits
```

获取当前应用窗口的尺寸限制，单位为物理像素px。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-getWindowLimits(): WindowLimits--><!--Device-Window-getWindowLimits(): WindowLimits-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| [WindowLimits](arkts-arkui-window-windowlimits-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## getWindowLimitsVP

```TypeScript
getWindowLimitsVP(): WindowLimits
```

获取当前应用窗口的尺寸限制，单位为虚拟像素vp。 对于系统窗口和全局悬浮窗，默认窗口宽高的系统限制最小值为1px，通过此接口获取到的1vp，是计算取整后的值。

**起始版本：** 23

<!--Device-Window-getWindowLimitsVP(): WindowLimits--><!--Device-Window-getWindowLimitsVP(): WindowLimits-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| [WindowLimits](arkts-arkui-window-windowlimits-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## getWindowProperties

```TypeScript
getWindowProperties(): WindowProperties
```

获取当前窗口的属性。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-getWindowProperties(): WindowProperties--><!--Device-Window-getWindowProperties(): WindowProperties-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| [WindowProperties](arkts-arkui-window-windowproperties-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## getWindowStateSnapshot

```TypeScript
getWindowStateSnapshot(): Promise<string>
```

获取设备形态，仅测试使用

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-getWindowStateSnapshot(): Promise<string>--><!--Device-Window-getWindowStateSnapshot(): Promise<string>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## getWindowStatus

```TypeScript
getWindowStatus(): WindowStatusType
```

获取当前应用窗口的模式。 > **说明：** > > 在[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下，应用的 > [targetAPIVersion](../../../quick-start/app-configuration-file.md#配置文件标签)设置小于14时，在窗口最大化状态（窗口铺满整个屏幕，2in1设备会有 > dock栏和状态栏，Tablet设备会有状态栏）时返回值对应为WindowStatusType::FULL_SCREEN。应用的 > [targetAPIVersion](../../../quick-start/app-configuration-file.md#配置文件标签)设置大于等于14时，在窗口最大化状态（窗口铺满整个屏幕，2in1设备会有 > dock栏和状态栏，Tablet设备会有状态栏）时返回值对应为WindowStatusType::MAXIMIZE。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-getWindowStatus(): WindowStatusType--><!--Device-Window-getWindowStatus(): WindowStatusType-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| [WindowStatusType](../arkts-components/arkts-arkui-windowstatustype-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## getWindowSystemBarProperties

```TypeScript
getWindowSystemBarProperties(): SystemBarProperties
```

获取主窗口&lt;!--Del--&gt;三键导航栏、&lt;!--DelEnd--&gt;状态栏的属性。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-getWindowSystemBarProperties(): SystemBarProperties--><!--Device-Window-getWindowSystemBarProperties(): SystemBarProperties-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| [SystemBarProperties](arkts-arkui-window-systembarproperties-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## getWindowTransitionAnimation

```TypeScript
getWindowTransitionAnimation(transitionType: WindowTransitionType): TransitionAnimation | undefined
```

获取特定场景下的窗口转场动画配置。 当前只支持在应用主窗下使用。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-getWindowTransitionAnimation(transitionType: WindowTransitionType): TransitionAnimation | undefined--><!--Device-Window-getWindowTransitionAnimation(transitionType: WindowTransitionType): TransitionAnimation | undefined-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| transitionType | [WindowTransitionType](arkts-arkui-window-windowtransitiontype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [TransitionAnimation](arkts-arkui-window-transitionanimation-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## globalDisplayToClient

```TypeScript
globalDisplayToClient(globalDisplayX: number, globalDisplayY: number): Position
```

将相对于主屏幕左上角的全局坐标转换为相对于当前窗口左上角的坐标。 不支持在经过显示缩放的窗口中调用，例如手机或平板设备在非自由多窗模式下的悬浮窗场景。

**起始版本：** 23

<!--Device-Window-globalDisplayToClient(globalDisplayX: int, globalDisplayY: int): Position--><!--Device-Window-globalDisplayToClient(globalDisplayX: int, globalDisplayY: int): Position-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| globalDisplayX | number | 是 |
| globalDisplayY | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Position](arkts-arkui-display-position-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |
| [1300010](../errorcode-window.md#1300010-当前窗口模式不支持该操作) |

## isFloatNavigationAvoidAreaEnabled

```TypeScript
isFloatNavigationAvoidAreaEnabled(): boolean
```

查询当前窗口是否支持获取三键导航类型的避让区域。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-Window-isFloatNavigationAvoidAreaEnabled(): boolean--><!--Device-Window-isFloatNavigationAvoidAreaEnabled(): boolean-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## isFocused

```TypeScript
isFocused(): boolean
```

判断当前窗口是否已获焦。为获取准确的获焦状态，需要在[WindowEventType](arkts-arkui-window-windoweventtype-e.md#windoweventtype)生命周期处于WINDOW_ACTIVE之后调用。 可使用[on('windowEvent')](#onrotationchange)监听对应状态变更， 再执行对应具体业务。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-isFocused(): boolean--><!--Device-Window-isFocused(): boolean-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## isGestureBackEnabled

```TypeScript
isGestureBackEnabled(): boolean
```

获取当前窗口是否启用返回手势功能，仅主窗可以调用成功，其他类型的窗口调用返回1300004错误码。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-isGestureBackEnabled(): boolean--><!--Device-Window-isGestureBackEnabled(): boolean-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## isImmersiveLayout

```TypeScript
isImmersiveLayout(): boolean
```

查询当前窗口是否处于沉浸式布局状态。

**起始版本：** 23

<!--Device-Window-isImmersiveLayout(): boolean--><!--Device-Window-isImmersiveLayout(): boolean-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## isInFreeWindowMode

```TypeScript
isInFreeWindowMode(): boolean
```

查询当前窗口是否为[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)模式。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-isInFreeWindowMode(): boolean--><!--Device-Window-isInFreeWindowMode(): boolean-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## isReceiveDragEventEnabled

```TypeScript
isReceiveDragEventEnabled(): boolean
```

获取当前窗口是否能接收[拖拽事件](../arkts-components/arkts-arkui-dragevent-i.md#dragevent)的状态。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Window-isReceiveDragEventEnabled(): boolean--><!--Device-Window-isReceiveDragEventEnabled(): boolean-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## isSeparationTouchEnabled

```TypeScript
isSeparationTouchEnabled(): boolean
```

获取当前窗口是否支持事件分离的状态。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Window-isSeparationTouchEnabled(): boolean--><!--Device-Window-isSeparationTouchEnabled(): boolean-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## isShowing

```TypeScript
isShowing(callback: AsyncCallback<boolean>): void
```

判断当前窗口是否已显示，使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用[isWindowShowing()](#iswindowshowing)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [isWindowShowing](#iswindowshowing)

<!--Device-Window-isShowing(callback: AsyncCallback<boolean>): void--><!--Device-Window-isShowing(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## isShowing

```TypeScript
isShowing(): Promise<boolean>
```

判断当前窗口是否已显示，使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用[isWindowShowing()](#iswindowshowing)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [isWindowShowing](#iswindowshowing)

<!--Device-Window-isShowing(): Promise<boolean>--><!--Device-Window-isShowing(): Promise<boolean>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## isSupportWideGamut

```TypeScript
isSupportWideGamut(): Promise<boolean>
```

判断当前窗口是否支持广色域模式，使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > [isWindowSupportWideGamut()](#iswindowsupportwidegamut)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isWindowSupportWideGamut](#iswindowsupportwidegamut)()

<!--Device-Window-isSupportWideGamut(): Promise<boolean>--><!--Device-Window-isSupportWideGamut(): Promise<boolean>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## isSupportWideGamut

```TypeScript
isSupportWideGamut(callback: AsyncCallback<boolean>): void
```

判断当前窗口是否支持广色域模式，使用callback异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > [isWindowSupportWideGamut()](#iswindowsupportwidegamut)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isWindowSupportWideGamut](#iswindowsupportwidegamut)(callback: AsyncCallback&lt;boolean&gt;)

<!--Device-Window-isSupportWideGamut(callback: AsyncCallback<boolean>): void--><!--Device-Window-isSupportWideGamut(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## isSystemAvoidAreaEnabled

```TypeScript
isSystemAvoidAreaEnabled(): boolean
```

获取悬浮窗、模态窗或WindowType为系统类型的窗口是否可以获取窗口内容的避让区[AvoidArea](arkts-arkui-window-avoidarea-i.md#avoidarea)。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-isSystemAvoidAreaEnabled(): boolean--><!--Device-Window-isSystemAvoidAreaEnabled(): boolean-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## isWindowHighlighted

```TypeScript
isWindowHighlighted(): boolean
```

获取当前窗口是否为激活态。为准确获取激活态，需要在[WindowEventType](arkts-arkui-window-windoweventtype-e.md#windoweventtype)生命周期处于WINDOW_ACTIVE之后调用。 可使用 [on('windowHighlightChange')](#onrotationchange) 监听对应状态变更，再执行对应具体业务。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-isWindowHighlighted(): boolean--><!--Device-Window-isWindowHighlighted(): boolean-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## isWindowShowing

```TypeScript
isWindowShowing(): boolean
```

判断当前窗口是否已显示。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-isWindowShowing(): boolean--><!--Device-Window-isWindowShowing(): boolean-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## isWindowSupportWideGamut

```TypeScript
isWindowSupportWideGamut(): Promise<boolean>
```

判断当前窗口是否支持广色域模式，使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-isWindowSupportWideGamut(): Promise<boolean>--><!--Device-Window-isWindowSupportWideGamut(): Promise<boolean>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## isWindowSupportWideGamut

```TypeScript
isWindowSupportWideGamut(callback: AsyncCallback<boolean>): void
```

判断当前窗口是否支持广色域模式，使用callback异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-isWindowSupportWideGamut(callback: AsyncCallback<boolean>): void--><!--Device-Window-isWindowSupportWideGamut(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## keepKeyboardOnFocus

```TypeScript
keepKeyboardOnFocus(keepKeyboardFlag: boolean): void
```

当前窗口获焦时是否保留由其他窗口创建的软键盘，支持系统窗口、应用子窗口、模态窗和全局悬浮窗。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-keepKeyboardOnFocus(keepKeyboardFlag: boolean): void--><!--Device-Window-keepKeyboardOnFocus(keepKeyboardFlag: boolean): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keepKeyboardFlag | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## loadContent

```TypeScript
loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void
```

根据当前工程中指定的页面路径为窗口加载具体页面内容，通过LocalStorage传递状态属性给加载的页面，使用callback异步回调。 建议在UIAbility启动过程中使用该接口，重复调用将先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。 当前UI的执行上下文可能不明确，所以不建议在本接口的回调函数中做UI相关的操作。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void--><!--Device-Window-loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| storage | [LocalStorage](arkts-arkui-localstorage-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## loadContent

```TypeScript
loadContent(path: string, storage: LocalStorage): Promise<void>
```

根据当前工程中指定的页面路径为窗口加载具体页面内容，通过LocalStorage传递状态属性给加载的页面，使用Promise异步回调。 建议在UIAbility启动过程中使用该接口，重复调用将先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。 当前UI的执行上下文可能不明确，所以不建议在本接口的回调函数中做UI相关的操作。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-loadContent(path: string, storage: LocalStorage): Promise<void>--><!--Device-Window-loadContent(path: string, storage: LocalStorage): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| storage | [LocalStorage](arkts-arkui-localstorage-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## loadContent

```TypeScript
loadContent(path: string, callback: AsyncCallback<void>): void
```

为当前窗口加载具体页面内容，使用callback异步回调。 建议在UIAbility启动过程中使用该接口，多次调用该接口会先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。 当前UI的执行上下文可能不明确，所以不建议在本接口的回调函数中做UI相关的操作。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用 > [setUIContent()](#setuicontent)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setUIContent](#setuicontent)(path: string, callback: AsyncCallback&lt;void&gt;)

<!--Device-Window-loadContent(path: string, callback: AsyncCallback<void>): void--><!--Device-Window-loadContent(path: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## loadContent

```TypeScript
loadContent(path: string): Promise<void>
```

为当前窗口加载具体页面内容，使用Promise异步回调。 建议在UIAbility启动过程中使用该接口，多次调用该接口会先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。 当前UI的执行上下文可能不明确，所以不建议在本接口的回调函数中做UI相关的操作。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用[setUIContent()](#setuicontent)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setUIContent](#setuicontent)(path: string)

<!--Device-Window-loadContent(path: string): Promise<void>--><!--Device-Window-loadContent(path: string): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## loadContentByName

```TypeScript
loadContentByName(name: string, storage: LocalStorage, callback: AsyncCallback<void>): void
```

根据指定路由页面名称为当前窗口加载[命名路由](../../../ui/arkts-routing.md#命名路由)页面，通过LocalStorage传递状态属性至加载页面，使用callback异步回调。 建议在UIAbility启动过程中使用该接口，重复调用该接口将先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。 当前UI的执行上下文可能不明确，所以不建议在本接口的回调函数中做UI相关的操作。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-loadContentByName(name: string, storage: LocalStorage, callback: AsyncCallback<void>): void--><!--Device-Window-loadContentByName(name: string, storage: LocalStorage, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| storage | [LocalStorage](arkts-arkui-localstorage-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## loadContentByName

```TypeScript
loadContentByName(name: string, callback: AsyncCallback<void>): void
```

根据指定路由页面名称为当前窗口加载[命名路由](../../../ui/arkts-routing.md#命名路由)页面，使用callback异步回调。 建议在UIAbility启动过程中使用该接口，重复调用该接口将先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。 当前UI的执行上下文可能不明确，所以不建议在本接口的回调函数中做UI相关的操作。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-loadContentByName(name: string, callback: AsyncCallback<void>): void--><!--Device-Window-loadContentByName(name: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## loadContentByName

```TypeScript
loadContentByName(name: string, storage?: LocalStorage): Promise<void>
```

根据指定路由页面名称为当前窗口加载[命名路由](../../../ui/arkts-routing.md#命名路由)页面，通过LocalStorage传递状态属性至加载页面，使用Promise异步回调。 建议在UIAbility启动过程中使用该接口，重复调用该接口将先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。 当前UI的执行上下文可能不明确，所以不建议在本接口的回调函数中做UI相关的操作。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-loadContentByName(name: string, storage?: LocalStorage): Promise<void>--><!--Device-Window-loadContentByName(name: string, storage?: LocalStorage): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| storage | [LocalStorage](arkts-arkui-localstorage-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## maximize

```TypeScript
maximize(presentation?: MaximizePresentation): Promise<void>
```

实现最大化功能。主窗口可调用此接口实现最大化功能；子窗口需在创建时设置子窗口参数maximizeSupported为true， 再调用此接口可实现最大化功能。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-maximize(presentation?: MaximizePresentation): Promise<void>--><!--Device-Window-maximize(presentation?: MaximizePresentation): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| presentation | [MaximizePresentation](arkts-arkui-window-maximizepresentation-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300005](../errorcode-window.md#1300005-windowstage异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## maximize

```TypeScript
maximize(presentation?: MaximizePresentation, acrossDisplay?: boolean): Promise<void>
```

实现最大化功能。主窗口可调用此接口实现最大化功能；子窗口需在创建时设置子窗口参数maximizeSupported为true，再调用此接口可实现最大化功能。在具备折叠功能的2in1设备上，支持控制悬停态（参考 [折叠屏悬停态最佳实践](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-folded-hover)）下主窗口的瀑布流模式行为，即窗口在悬停态下 最大化时是否跨上下两个半屏显示。使用Promise异步回调。

**起始版本：** 23

<!--Device-Window-maximize(presentation?: MaximizePresentation, acrossDisplay?: boolean): Promise<void>--><!--Device-Window-maximize(presentation?: MaximizePresentation, acrossDisplay?: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| presentation | [MaximizePresentation](arkts-arkui-window-maximizepresentation-e.md) | 否 |
| acrossDisplay | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## maximizeWithOptions

```TypeScript
maximizeWithOptions(maximizeOptions?: MaximizeOptions): Promise<void>
```

最大化应用窗口。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Window-maximizeWithOptions(maximizeOptions?: MaximizeOptions): Promise<void>--><!--Device-Window-maximizeWithOptions(maximizeOptions?: MaximizeOptions): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| maximizeOptions | [MaximizeOptions](arkts-arkui-window-maximizeoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## minimize

```TypeScript
minimize(callback: AsyncCallback<void>): void
```

此接口根据调用对象不同，实现不同的功能： - 当调用对象为主窗口时，实现最小化功能，可在Dock栏中还原，2in1 设备上可以使用[restore()](#restore)进行还原。 - 当调用对象为子窗口或全局悬浮窗时，实现隐藏功能，不可在Dock栏中还原，可以使用 [showWindow()](#showwindow)进行还原。 该接口仅支持主窗口、子窗口或全局悬浮窗，其它窗口调用返回1300002错误码，使用callback异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-minimize(callback: AsyncCallback<void>): void--><!--Device-Window-minimize(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## minimize

```TypeScript
minimize(): Promise<void>
```

此接口根据调用对象不同，实现不同的功能： - 当调用对象为主窗口时，实现最小化功能，可在Dock栏中还原，2in1 设备上可以使用[restore()](#restore)进行还原。 - 当调用对象为子窗口或全局悬浮窗时，实现隐藏功能，不可在Dock栏中还原，可以使用 [showWindow()](#showwindow)进行还原。 该接口仅支持主窗口、子窗口或全局悬浮窗，其它窗口调用返回1300002错误码，使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-minimize(): Promise<void>--><!--Device-Window-minimize(): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## moveTo

```TypeScript
moveTo(x: number, y: number): Promise<void>
```

移动窗口位置，使用Promise异步回调。 全屏模式窗口不支持该操作。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用[moveWindowTo()](#movewindowto)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [moveWindowTo](#movewindowto)(x: int, y: int)

<!--Device-Window-moveTo(x: number, y: number): Promise<void>--><!--Device-Window-moveTo(x: number, y: number): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## moveTo

```TypeScript
moveTo(x: number, y: number, callback: AsyncCallback<void>): void
```

移动窗口位置，使用callback异步回调。 全屏模式窗口不支持该操作。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用 > [moveWindowTo()](#movewindowto)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [moveWindowTo](#movewindowto)(x: int, y: int, callback: AsyncCallback&lt;void&gt;)

<!--Device-Window-moveTo(x: number, y: number, callback: AsyncCallback<void>): void--><!--Device-Window-moveTo(x: number, y: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## moveWindowTo

```TypeScript
moveWindowTo(x: number, y: number): Promise<void>
```

移动窗口位置，使用Promise异步回调。调用成功即返回，但返回后无法立即获取最终生效结果。如需立即获取，请使用 [moveWindowToAsync()](#movewindowtoasync)。 > **说明：** > > - 不建议在除自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，WindowStatusType可通过 > [getWindowStatus()](#getwindowstatus)获取）外的其他窗口模式下使用。 > > - 在[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下，窗口相对于屏幕左上顶点移动；在非自由窗口状态下，窗口相对于父窗口左上顶点移动。 > > - 若需在非自由窗口状态下实现相对于屏幕左上顶点的移动，请使用 > [moveWindowToGlobal()](#movewindowtoglobal) > 。 > > - 该方法对非自由窗口状态下的主窗口无效。 > > - [自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下，若主窗口或子窗口的标题栏移出屏幕可视区域，系统将自动回弹窗口，确保标题栏保持可见。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-moveWindowTo(x: int, y: int): Promise<void>--><!--Device-Window-moveWindowTo(x: int, y: int): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

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
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## moveWindowTo

```TypeScript
moveWindowTo(x: number, y: number, callback: AsyncCallback<void>): void
```

移动窗口位置，使用callback异步回调。调用成功即返回，但返回后无法立即获取最终生效结果。如需立即获取，请使用 [moveWindowToAsync()](#movewindowtoasync)。 > **说明：** > > - 不建议在除自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，WindowStatusType可通过 > [getWindowStatus()](#getwindowstatus)获取）外的其他窗口模式下使用。 > > - 在[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下，窗口相对于屏幕左上顶点移动；在非自由窗口状态下，窗口相对于父窗口左上顶点移动。 > > - 若需在非自由窗口状态下实现相对于屏幕左上顶点的移动，请使用 > [moveWindowToGlobal()](#movewindowtoglobal) > 。 > > - 该方法对非自由窗口状态下的主窗口无效。 > > - [自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下，若主窗口或子窗口的标题栏移出屏幕可视区域，系统将自动回弹窗口，确保标题栏保持可见。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-moveWindowTo(x: int, y: int, callback: AsyncCallback<void>): void--><!--Device-Window-moveWindowTo(x: int, y: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## moveWindowToAsync

```TypeScript
moveWindowToAsync(x: number, y: number): Promise<void>
```

移动窗口位置，使用Promise异步回调。调用生效后返回，回调中可使用[getWindowProperties()](#getwindowproperties)（见示例）立即获取最终生效结 果。 该接口仅在窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，窗口模式可通过 [getWindowStatus()](#getwindowstatus)获取）时调用生效，在其他窗口模式下调用返回错误码1300010错误码。 在自由悬浮窗口模式下，不同类型窗口的移动行为如下： | 窗口类型 | [自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态 | 非自由窗口状态 | |---------|---------------|-----------------| | 主窗口 | 相对于屏幕移动 | 调用不生效不报错 | | 应用子窗口/模态窗 | 相对于屏幕移动 | 相对于主窗口移动 | | 系统窗口/全局悬浮窗 | 相对于屏幕移动 | 相对于屏幕移动 | > **说明：** > > - [自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下，若主窗口或子窗口的标题栏移出屏幕可视区域，系统将自动回弹窗口，确保标题栏保持可见。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-moveWindowToAsync(x: int, y: int): Promise<void>--><!--Device-Window-moveWindowToAsync(x: int, y: int): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

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
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300010](../errorcode-window.md#1300010-当前窗口模式不支持该操作) |

## moveWindowToAsync

```TypeScript
moveWindowToAsync(x: number, y: number, moveConfiguration?: MoveConfiguration): Promise<void>
```

移动窗口位置，支持配置moveConfiguration参数指定窗口移动的目标屏幕ID，使用Promise异步回调。调用生效后返回，回调中可使用 [getWindowProperties()](#getwindowproperties)（见示例）立即获取最终生效结果。 该接口仅在窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，窗口模式可通过 [getWindowStatus()](#getwindowstatus)获取）时调用生效，在其他窗口模式下调用返回错误码1300010错误码。 在自由悬浮窗口模式下，不同类型窗口的移动行为如下： | 窗口类型 | [自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态 | 非自由窗口状态 | |---------|---------------|-----------------| | 主窗口 | 相对于屏幕移动 | 调用不生效不报错 | | 应用子窗口/模态窗 | 相对于屏幕移动 | 相对于主窗口移动 | | 系统窗口/全局悬浮窗 | 相对于屏幕移动 | 相对于屏幕移动 | > **说明：** > > - [自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下，若主窗口或子窗口的标题栏移出屏幕可视区域，系统将自动回弹窗口，确保标题栏保持可见。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-moveWindowToAsync(x: int, y: int, moveConfiguration?: MoveConfiguration): Promise<void>--><!--Device-Window-moveWindowToAsync(x: int, y: int, moveConfiguration?: MoveConfiguration): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| moveConfiguration | [MoveConfiguration](arkts-arkui-window-moveconfiguration-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300010](../errorcode-window.md#1300010-当前窗口模式不支持该操作) |

## moveWindowToGlobal

```TypeScript
moveWindowToGlobal(x: number, y: number): Promise<void>
```

基于屏幕坐标移动窗口位置，使用Promise异步回调。调用生效后返回，回调中可使用[getWindowProperties()](#getwindowproperties)（见示例）立即获 取最终生效结果。 该接口仅在窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，窗口模式可通过 [getWindowStatus()](#getwindowstatus)获取）时调用生效，在其他窗口模式下调用返回错误码1300010错误码。 > **说明：** > > - 主窗处于自由悬浮窗口模式时，在非[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下调用不生效不报错。 > > - [自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下，若主窗口或子窗口的标题栏移出屏幕可视区域，系统将自动回弹窗口，确保标题栏保持可见。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-moveWindowToGlobal(x: int, y: int): Promise<void>--><!--Device-Window-moveWindowToGlobal(x: int, y: int): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

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
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300010](../errorcode-window.md#1300010-当前窗口模式不支持该操作) |

## moveWindowToGlobal

```TypeScript
moveWindowToGlobal(x: number, y: number, moveConfiguration?: MoveConfiguration): Promise<void>
```

基于屏幕坐标移动窗口位置，支持配置moveConfiguration参数指定窗口移动的目标屏幕ID，使用Promise异步回调。调用生效后返回，回调中可使用 [getWindowProperties()](#getwindowproperties)（见示例）立即获取最终生效结果。 该接口仅在窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，窗口模式可通过 [getWindowStatus()](#getwindowstatus)获取）时调用生效，在其他窗口模式下调用返回错误码1300010错误码。 > **说明：** > > - 主窗处于自由悬浮窗口模式时，在非[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下调用不生效不报错。 > > - [自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下，若主窗口或子窗口的标题栏移出屏幕可视区域，系统将自动回弹窗口，确保标题栏保持可见。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-moveWindowToGlobal(x: int, y: int, moveConfiguration?: MoveConfiguration): Promise<void>--><!--Device-Window-moveWindowToGlobal(x: int, y: int, moveConfiguration?: MoveConfiguration): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| moveConfiguration | [MoveConfiguration](arkts-arkui-window-moveconfiguration-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300010](../errorcode-window.md#1300010-当前窗口模式不支持该操作) |

## moveWindowToGlobalDisplay

```TypeScript
moveWindowToGlobalDisplay(x: number, y: number): Promise<void>
```

基于[全局坐标系](../../../windowmanager/window-terminology.md#全局坐标系)移动窗口位置，使用Promise异步回调。 该接口仅在窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，窗口模式可通过 [getWindowStatus()](#getwindowstatus)获取）时调用生效，在其他窗口模式下调用返回错误码1300010错误码。 > **说明：** > > - 主窗处于自由悬浮窗口模式时，在非[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下调用不生效不报错。 > > - 窗口移动后，如果窗口跨越多个屏幕，窗口将归属于与其重叠面积最大的屏幕。 > > - [自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下，若主窗口或子窗口的标题栏移出屏幕可视区域，系统将自动回弹窗口，确保标题栏保持可见。

**起始版本：** 23

<!--Device-Window-moveWindowToGlobalDisplay(x: int, y: int): Promise<void>--><!--Device-Window-moveWindowToGlobalDisplay(x: int, y: int): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

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
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |
| [1300010](../errorcode-window.md#1300010-当前窗口模式不支持该操作) |

## offAvoidAreaChange

```TypeScript
offAvoidAreaChange(callback?: Callback<AvoidAreaOptions>): void
```

关闭当前窗口系统避让区变化的监听。

**起始版本：** 23

<!--Device-Window-offAvoidAreaChange(callback?: Callback<AvoidAreaOptions>): void--><!--Device-Window-offAvoidAreaChange(callback?: Callback<AvoidAreaOptions>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[AvoidAreaOptions](arkts-arkui-window-avoidareaoptions-i.md)&gt; | 否 |

## offDialogTargetTouch

```TypeScript
offDialogTargetTouch(callback?: Callback<void>): void
```

关闭模态窗口目标窗口的点击事件的监听。

**起始版本：** 23

<!--Device-Window-offDialogTargetTouch(callback?: Callback<void>): void--><!--Device-Window-offDialogTargetTouch(callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 否 |

## offDisplayIdChange

```TypeScript
offDisplayIdChange(callback?: Callback<number>): void
```

关闭本窗口所处屏幕变化事件的监听。

**起始版本：** 23

<!--Device-Window-offDisplayIdChange(callback?: Callback<long>): void--><!--Device-Window-offDisplayIdChange(callback?: Callback<long>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offFrameMetricsMeasured

```TypeScript
offFrameMetricsMeasured(callback?: Callback<FrameMetrics>): void
```

关闭窗口帧率指标变化事件的监听。该接口需要在 [loadContent()](#loadcontent) 或[setUIContent()](#setuicontent)调用生效后使用。

**起始版本：** 23

<!--Device-Window-offFrameMetricsMeasured(callback?: Callback<FrameMetrics>): void--><!--Device-Window-offFrameMetricsMeasured(callback?: Callback<FrameMetrics>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[FrameMetrics](arkts-arkui-window-framemetrics-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offFreeWindowModeChange

```TypeScript
offFreeWindowModeChange(callback?: Callback<boolean>): void
```

free window mode change callback off.

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-offFreeWindowModeChange(callback?: Callback<boolean>): void--><!--Device-Window-offFreeWindowModeChange(callback?: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offKeyboardDidHide

```TypeScript
offKeyboardDidHide(callback?: Callback<KeyboardInfo>): void
```

关闭固定态软键盘隐藏动画完成的监听。改变输入法窗口为固定态切换至悬浮态方法详细介绍请参见 [输入法服务](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeflag)。

**起始版本：** 23

<!--Device-Window-offKeyboardDidHide(callback?: Callback<KeyboardInfo>): void--><!--Device-Window-offKeyboardDidHide(callback?: Callback<KeyboardInfo>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offKeyboardDidShow

```TypeScript
offKeyboardDidShow(callback?: Callback<KeyboardInfo>): void
```

关闭固定态软键盘显示动画完成的监听。改变输入法窗口为固定态或者悬浮态方法详细介绍请参见 [输入法服务](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeflag)。

**起始版本：** 23

<!--Device-Window-offKeyboardDidShow(callback?: Callback<KeyboardInfo>): void--><!--Device-Window-offKeyboardDidShow(callback?: Callback<KeyboardInfo>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offKeyboardHeightChange

```TypeScript
offKeyboardHeightChange(callback?: Callback<number>): void
```

关闭固定态软键盘高度变化的监听，使应用程序不再接收键盘高度变化的通知。从API version 10开始，有关将软键盘设置为固定态或悬浮态的方法，请参见 [输入法服务](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeflag)。

**起始版本：** 23

<!--Device-Window-offKeyboardHeightChange(callback?: Callback<int>): void--><!--Device-Window-offKeyboardHeightChange(callback?: Callback<int>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | 否 |

## offKeyboardWillHide

```TypeScript
offKeyboardWillHide(callback?: Callback<KeyboardInfo>): void
```

关闭固定态软键盘即将开始隐藏的监听。改变输入法窗口为固定态切换至悬浮态方法详细介绍请参见 [输入法服务](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeflag)。

**起始版本：** 23

<!--Device-Window-offKeyboardWillHide(callback?: Callback<KeyboardInfo>): void--><!--Device-Window-offKeyboardWillHide(callback?: Callback<KeyboardInfo>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offKeyboardWillShow

```TypeScript
offKeyboardWillShow(callback?: Callback<KeyboardInfo>): void
```

关闭固定态软键盘即将开始显示的监听。改变输入法窗口为固定态或者悬浮态方法详细介绍请参见 [输入法服务](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeflag)。

**起始版本：** 23

<!--Device-Window-offKeyboardWillShow(callback?: Callback<KeyboardInfo>): void--><!--Device-Window-offKeyboardWillShow(callback?: Callback<KeyboardInfo>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offNoInteractionDetected

```TypeScript
offNoInteractionDetected(callback?: Callback<void>): void
```

关闭本窗口在指定超时时间内无交互事件的监听，交互事件支持物理键盘输入事件和屏幕触控点击事件，不支持软键盘输入事件。

**起始版本：** 23

<!--Device-Window-offNoInteractionDetected(callback?: Callback<void>): void--><!--Device-Window-offNoInteractionDetected(callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offOcclusionStateChanged

```TypeScript
offOcclusionStateChanged(callback?: Callback<OcclusionState>): void
```

关闭窗口可见性状态变化事件的监听。

**起始版本：** 23

<!--Device-Window-offOcclusionStateChanged(callback?: Callback<OcclusionState>): void--><!--Device-Window-offOcclusionStateChanged(callback?: Callback<OcclusionState>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[OcclusionState](arkts-arkui-window-occlusionstate-e.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offRectChangeInGlobalDisplay

```TypeScript
offRectChangeInGlobalDisplay(callback?: Callback<RectChangeOptions>): void
```

关闭[全局坐标系](../../../windowmanager/window-terminology.md#全局坐标系)下窗口矩形（窗口位置及窗口大小）变化的监听事件。

**起始版本：** 23

<!--Device-Window-offRectChangeInGlobalDisplay(callback?: Callback<RectChangeOptions>): void--><!--Device-Window-offRectChangeInGlobalDisplay(callback?: Callback<RectChangeOptions>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;RectChangeOptions&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offRotationChange

```TypeScript
offRotationChange(callback?: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | undefined>):
      void
```

Unregister the callback of rotation change

**起始版本：** 23

<!--Device-Window-offRotationChange(callback?: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | undefined>):      void--><!--Device-Window-offRotationChange(callback?: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | undefined>):      void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [RotationChangeCallback](arkts-arkui-window-rotationchangecallback-t.md)&lt;[RotationChangeInfo](arkts-arkui-window-rotationchangeinfo-i.md), [RotationChangeResult](arkts-arkui-window-rotationchangeresult-i.md) \| undefined & gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offScreenshot

```TypeScript
offScreenshot(callback?: Callback<void>): void
```

关闭截屏事件的监听。

**起始版本：** 23

<!--Device-Window-offScreenshot(callback?: Callback<void>): void--><!--Device-Window-offScreenshot(callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 否 |

## offScreenshotAppEvent

```TypeScript
offScreenshotAppEvent(callback?: Callback<ScreenshotEventType>): void
```

关闭屏幕截屏事件类型的监听。

**起始版本：** 23

<!--Device-Window-offScreenshotAppEvent(callback?: Callback<ScreenshotEventType>): void--><!--Device-Window-offScreenshotAppEvent(callback?: Callback<ScreenshotEventType>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[ScreenshotEventType](arkts-arkui-window-screenshoteventtype-e.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offSubWindowClose

```TypeScript
offSubWindowClose(callback?: Callback<void>): void
```

关闭子窗口关闭事件的监听。

**起始版本：** 23

<!--Device-Window-offSubWindowClose(callback?: Callback<void>): void--><!--Device-Window-offSubWindowClose(callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## offSystemDensityChange

```TypeScript
offSystemDensityChange(callback?: Callback<number>): void
```

关闭本窗口所处屏幕的系统显示大小缩放系数变化事件的监听。 在接口回调函数中，建议直接使用返回值进行vp和px的转换。例如，若返回值为density，计算px可使用vp * density = px。

**起始版本：** 23

<!--Device-Window-offSystemDensityChange(callback?: Callback<double>): void--><!--Device-Window-offSystemDensityChange(callback?: Callback<double>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offTouchOutside

```TypeScript
offTouchOutside(callback?: Callback<void>): void
```

关闭本窗口区域范围外的点击事件的监听。

**起始版本：** 23

<!--Device-Window-offTouchOutside(callback?: Callback<void>): void--><!--Device-Window-offTouchOutside(callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 否 |

## offUiExtensionSecureLimitChange

```TypeScript
offUiExtensionSecureLimitChange(callback?: Callback<boolean>): void
```

UIExtension in window secure limit change callback off.

**起始版本：** 23

<!--Device-Window-offUiExtensionSecureLimitChange(callback?: Callback<boolean>): void--><!--Device-Window-offUiExtensionSecureLimitChange(callback?: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offWindowEvent

```TypeScript
offWindowEvent(callback?: Callback<WindowEventType>): void
```

关闭窗口生命周期变化的监听。

**起始版本：** 23

<!--Device-Window-offWindowEvent(callback?: Callback<WindowEventType>): void--><!--Device-Window-offWindowEvent(callback?: Callback<WindowEventType>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[WindowEventType](arkts-arkui-window-windoweventtype-e.md)&gt; | 否 |

## offWindowHighlightChange

```TypeScript
offWindowHighlightChange(callback?: Callback<boolean>): void
```

关闭窗口激活态变化事件的监听。

**起始版本：** 23

<!--Device-Window-offWindowHighlightChange(callback?: Callback<boolean>): void--><!--Device-Window-offWindowHighlightChange(callback?: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offWindowRectChange

```TypeScript
offWindowRectChange(callback?: Callback<RectChangeOptions>): void
```

关闭窗口矩形（窗口位置及窗口大小）变化的监听。

**起始版本：** 23

<!--Device-Window-offWindowRectChange(callback?: Callback<RectChangeOptions>): void--><!--Device-Window-offWindowRectChange(callback?: Callback<RectChangeOptions>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;RectChangeOptions&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offWindowSizeChange

```TypeScript
offWindowSizeChange(callback?: Callback<Size>): void
```

关闭窗口尺寸变化的监听。仅在主线程调用。

**起始版本：** 23

<!--Device-Window-offWindowSizeChange(callback?: Callback<Size>): void--><!--Device-Window-offWindowSizeChange(callback?: Callback<Size>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;Size&gt; | 否 |

## offWindowStatusChange

```TypeScript
offWindowStatusChange(callback?: Callback<WindowStatusType>): void
```

关闭窗口模式变化的监听。

**起始版本：** 23

<!--Device-Window-offWindowStatusChange(callback?: Callback<WindowStatusType>): void--><!--Device-Window-offWindowStatusChange(callback?: Callback<WindowStatusType>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;WindowStatusType&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## offWindowStatusDidChange

```TypeScript
offWindowStatusDidChange(callback?: Callback<WindowStatusType>): void
```

关闭窗口模式变化的监听。

**起始版本：** 23

<!--Device-Window-offWindowStatusDidChange(callback?: Callback<WindowStatusType>): void--><!--Device-Window-offWindowStatusDidChange(callback?: Callback<WindowStatusType>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;WindowStatusType&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offWindowTitleButtonRectChange

```TypeScript
offWindowTitleButtonRectChange(callback?: Callback<TitleButtonRect>): void
```

Unsubscribes from the change event of the rectangle that holds the minimize, maximize, and close buttons on the title bar of the window.

**起始版本：** 23

<!--Device-Window-offWindowTitleButtonRectChange(callback?: Callback<TitleButtonRect>): void--><!--Device-Window-offWindowTitleButtonRectChange(callback?: Callback<TitleButtonRect>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[TitleButtonRect](arkts-arkui-window-titlebuttonrect-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offWindowVisibilityChange

```TypeScript
offWindowVisibilityChange(callback?: Callback<boolean>): void
```

关闭本窗口可见状态变化事件的监听。

**起始版本：** 23

<!--Device-Window-offWindowVisibilityChange(callback?: Callback<boolean>): void--><!--Device-Window-offWindowVisibilityChange(callback?: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## offWindowWillClose

```TypeScript
offWindowWillClose(callback?: Callback<void, Promise<boolean>>): void
```

关闭主窗口或子窗口关闭事件的监听。

**起始版本：** 23

<!--Device-Window-offWindowWillClose(callback?: Callback<void, Promise<boolean>>): void--><!--Device-Window-offWindowWillClose(callback?: Callback<void, Promise<boolean>>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void, Promise&lt;boolean&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## off_avoidAreaChange

```TypeScript
off(type: 'avoidAreaChange', callback?: Callback<AvoidAreaOptions>): void
```

关闭当前窗口系统避让区变化的监听。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'avoidAreaChange', callback?: Callback<AvoidAreaOptions>): void--><!--Device-Window-off(type: 'avoidAreaChange', callback?: Callback<AvoidAreaOptions>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'avoidAreaChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[AvoidAreaOptions](arkts-arkui-window-avoidareaoptions-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off_dialogTargetTouch

```TypeScript
off(type: 'dialogTargetTouch', callback?: Callback<void>): void
```

关闭模态窗口目标窗口的点击事件的监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'dialogTargetTouch', callback?: Callback<void>): void--><!--Device-Window-off(type: 'dialogTargetTouch', callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'dialogTargetTouch' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off_displayIdChange

```TypeScript
off(type: 'displayIdChange', callback?: Callback<number>): void
```

关闭本窗口所处屏幕变化事件的监听。

**起始版本：** 14

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'displayIdChange', callback?: Callback<long>): void--><!--Device-Window-off(type: 'displayIdChange', callback?: Callback<long>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'displayIdChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## off_frameMetricsMeasured

```TypeScript
off(type: 'frameMetricsMeasured', callback?: Callback<FrameMetrics>): void
```

关闭窗口帧率指标变化事件的监听。该接口需要在 [loadContent()](#loadcontent) 或[setUIContent()](#setuicontent)调用生效后使用。

**起始版本：** 22

<!--Device-Window-off(type: 'frameMetricsMeasured', callback?: Callback<FrameMetrics>): void--><!--Device-Window-off(type: 'frameMetricsMeasured', callback?: Callback<FrameMetrics>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'frameMetricsMeasured' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[FrameMetrics](arkts-arkui-window-framemetrics-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## off_freeWindowModeChange

```TypeScript
off(type: 'freeWindowModeChange', callback?: Callback<boolean>): void
```

关闭自由窗口模式变化事件的监听。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'freeWindowModeChange', callback?: Callback<boolean>): void--><!--Device-Window-off(type: 'freeWindowModeChange', callback?: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'freeWindowModeChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## off_keyboardDidHide

```TypeScript
off(type: 'keyboardDidHide', callback?: Callback<KeyboardInfo>): void
```

关闭固定态软键盘隐藏动画完成的监听。改变输入法窗口为固定态切换至悬浮态方法详细介绍请参见 [输入法服务](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeflag)。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'keyboardDidHide', callback?: Callback<KeyboardInfo>): void--><!--Device-Window-off(type: 'keyboardDidHide', callback?: Callback<KeyboardInfo>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyboardDidHide' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## off_keyboardDidShow

```TypeScript
off(type: 'keyboardDidShow', callback?: Callback<KeyboardInfo>): void
```

关闭固定态软键盘显示动画完成的监听。改变输入法窗口为固定态或者悬浮态方法详细介绍请参见 [输入法服务](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeflag)。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'keyboardDidShow', callback?: Callback<KeyboardInfo>): void--><!--Device-Window-off(type: 'keyboardDidShow', callback?: Callback<KeyboardInfo>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyboardDidShow' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## off_keyboardHeightChange

```TypeScript
off(type: 'keyboardHeightChange', callback?: Callback<number>): void
```

关闭固定态软键盘高度变化的监听，使应用程序不再接收键盘高度变化的通知。从API version 10开始，有关将软键盘设置为固定态或悬浮态的方法，请参见 [输入法服务](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeflag)。

**起始版本：** 7

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'keyboardHeightChange', callback?: Callback<int>): void--><!--Device-Window-off(type: 'keyboardHeightChange', callback?: Callback<int>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyboardHeightChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off_keyboardWillHide

```TypeScript
off(type: 'keyboardWillHide', callback?: Callback<KeyboardInfo>): void
```

关闭固定态软键盘即将开始隐藏的监听。改变输入法窗口为固定态切换至悬浮态方法详细介绍请参见 [输入法服务](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeflag)。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'keyboardWillHide', callback?: Callback<KeyboardInfo>): void--><!--Device-Window-off(type: 'keyboardWillHide', callback?: Callback<KeyboardInfo>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyboardWillHide' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## off_keyboardWillShow

```TypeScript
off(type: 'keyboardWillShow', callback?: Callback<KeyboardInfo>): void
```

关闭固定态软键盘即将开始显示的监听。改变输入法窗口为固定态或者悬浮态方法详细介绍请参见 [输入法服务](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeflag)。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'keyboardWillShow', callback?: Callback<KeyboardInfo>): void--><!--Device-Window-off(type: 'keyboardWillShow', callback?: Callback<KeyboardInfo>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyboardWillShow' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## off_noInteractionDetected

```TypeScript
off(type: 'noInteractionDetected', callback?: Callback<void>): void
```

关闭本窗口在指定超时时间内无交互事件的监听，交互事件支持物理键盘输入事件和屏幕触控点击事件，不支持软键盘输入事件。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'noInteractionDetected', callback?: Callback<void>): void--><!--Device-Window-off(type: 'noInteractionDetected', callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'noInteractionDetected' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## off_occlusionStateChanged

```TypeScript
off(type: 'occlusionStateChanged', callback?: Callback<OcclusionState>): void
```

关闭窗口可见性状态变化事件的监听。

**起始版本：** 22

<!--Device-Window-off(type: 'occlusionStateChanged', callback?: Callback<OcclusionState>): void--><!--Device-Window-off(type: 'occlusionStateChanged', callback?: Callback<OcclusionState>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'occlusionStateChanged' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[OcclusionState](arkts-arkui-window-occlusionstate-e.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## off_rectChangeInGlobalDisplay

```TypeScript
off(type: 'rectChangeInGlobalDisplay', callback?: Callback<RectChangeOptions>): void
```

关闭[全局坐标系](../../../windowmanager/window-terminology.md#全局坐标系)下窗口矩形（窗口位置及窗口大小）变化的监听事件。

**起始版本：** 20

<!--Device-Window-off(type: 'rectChangeInGlobalDisplay', callback?: Callback<RectChangeOptions>): void--><!--Device-Window-off(type: 'rectChangeInGlobalDisplay', callback?: Callback<RectChangeOptions>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'rectChangeInGlobalDisplay' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;RectChangeOptions&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## off_rotationChange

```TypeScript
off(type: 'rotationChange', 
       callback?: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void>): void
```

关闭窗口旋转变化的监听。

**起始版本：** 19

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'rotationChange',        callback?: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void>): void--><!--Device-Window-off(type: 'rotationChange',        callback?: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'rotationChange' | 是 |
| callback | [RotationChangeCallback](arkts-arkui-window-rotationchangecallback-t.md)&lt;[RotationChangeInfo](arkts-arkui-window-rotationchangeinfo-i.md), [RotationChangeResult](arkts-arkui-window-rotationchangeresult-i.md) \| void & gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## off_screenshot

```TypeScript
off(type: 'screenshot', callback?: Callback<void>): void
```

关闭截屏事件的监听。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'screenshot', callback?: Callback<void>): void--><!--Device-Window-off(type: 'screenshot', callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'screenshot' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off_screenshotAppEvent

```TypeScript
off(type: 'screenshotAppEvent', callback?: Callback<ScreenshotEventType>): void
```

关闭屏幕截屏事件类型的监听。

**起始版本：** 20

<!--Device-Window-off(type: 'screenshotAppEvent', callback?: Callback<ScreenshotEventType>): void--><!--Device-Window-off(type: 'screenshotAppEvent', callback?: Callback<ScreenshotEventType>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'screenshotAppEvent' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[ScreenshotEventType](arkts-arkui-window-screenshoteventtype-e.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## off_subWindowClose

```TypeScript
off(type: 'subWindowClose', callback?: Callback<void>): void
```

关闭子窗口关闭事件的监听。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'subWindowClose', callback?: Callback<void>): void--><!--Device-Window-off(type: 'subWindowClose', callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'subWindowClose' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## off_systemAvoidAreaChange

```TypeScript
off(type: 'systemAvoidAreaChange', callback?: Callback<AvoidArea>): void
```

关闭当前窗口系统避让区变化的监听。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用 > [off('avoidAreaChange')](#offrotationchange) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [off](#offrotationchange)(type: 'avoidAreaChange', callback?: Callback&lt;AvoidAreaOptions&gt;)

<!--Device-Window-off(type: 'systemAvoidAreaChange', callback?: Callback<AvoidArea>): void--><!--Device-Window-off(type: 'systemAvoidAreaChange', callback?: Callback<AvoidArea>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'systemAvoidAreaChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[AvoidArea](arkts-arkui-window-avoidarea-i.md)&gt; | 否 |

## off_systemDensityChange

```TypeScript
off(type: 'systemDensityChange', callback?: Callback<number>): void
```

关闭本窗口所处屏幕的系统显示大小缩放系数变化事件的监听。 在接口回调函数中，建议直接使用返回值进行vp和px的转换。例如，若返回值为density，计算px可使用vp * density = px。

**起始版本：** 15

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'systemDensityChange', callback?: Callback<double>): void--><!--Device-Window-off(type: 'systemDensityChange', callback?: Callback<double>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'systemDensityChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## off_touchOutside

```TypeScript
off(type: 'touchOutside', callback?: Callback<void>): void
```

关闭本窗口区域范围外的点击事件的监听。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'touchOutside', callback?: Callback<void>): void--><!--Device-Window-off(type: 'touchOutside', callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'touchOutside' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off_uiExtensionSecureLimitChange

```TypeScript
off(eventType: 'uiExtensionSecureLimitChange', callback?: Callback<boolean>): void
```

关闭窗口内uiextension安全限制变化事件的监听。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(eventType: 'uiExtensionSecureLimitChange', callback?: Callback<boolean>): void--><!--Device-Window-off(eventType: 'uiExtensionSecureLimitChange', callback?: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventType | 'uiExtensionSecureLimitChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## off_windowEvent

```TypeScript
off(type: 'windowEvent', callback?: Callback<WindowEventType>): void
```

关闭窗口生命周期变化的监听。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'windowEvent', callback?: Callback<WindowEventType>): void--><!--Device-Window-off(type: 'windowEvent', callback?: Callback<WindowEventType>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'windowEvent' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[WindowEventType](arkts-arkui-window-windoweventtype-e.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off_windowHighlightChange

```TypeScript
off(type: 'windowHighlightChange', callback?: Callback<boolean>): void
```

关闭窗口激活态变化事件的监听。

**起始版本：** 15

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'windowHighlightChange', callback?: Callback<boolean>): void--><!--Device-Window-off(type: 'windowHighlightChange', callback?: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'windowHighlightChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## off_windowRectChange

```TypeScript
off(type: 'windowRectChange', callback?: Callback<RectChangeOptions>): void
```

关闭窗口矩形（窗口位置及窗口大小）变化的监听。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'windowRectChange', callback?: Callback<RectChangeOptions>): void--><!--Device-Window-off(type: 'windowRectChange', callback?: Callback<RectChangeOptions>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'windowRectChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;RectChangeOptions&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## off_windowSizeChange

```TypeScript
off(type: 'windowSizeChange', callback?: Callback<Size>): void
```

关闭窗口尺寸变化的监听。仅在主线程调用。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'windowSizeChange', callback?: Callback<Size>): void--><!--Device-Window-off(type: 'windowSizeChange', callback?: Callback<Size>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'windowSizeChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;Size&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off_windowStatusChange

```TypeScript
off(type: 'windowStatusChange', callback?: Callback<WindowStatusType>): void
```

关闭窗口模式变化的监听。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'windowStatusChange', callback?: Callback<WindowStatusType>): void--><!--Device-Window-off(type: 'windowStatusChange', callback?: Callback<WindowStatusType>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'windowStatusChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;WindowStatusType&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## off_windowStatusDidChange

```TypeScript
off(type: 'windowStatusDidChange', callback?: Callback<WindowStatusType>): void
```

关闭窗口模式变化的监听。

**起始版本：** 20

<!--Device-Window-off(type: 'windowStatusDidChange', callback?: Callback<WindowStatusType>): void--><!--Device-Window-off(type: 'windowStatusDidChange', callback?: Callback<WindowStatusType>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'windowStatusDidChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;WindowStatusType&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## off_windowTitleButtonRectChange

```TypeScript
off(type: 'windowTitleButtonRectChange', callback?: Callback<TitleButtonRect>): void
```

关闭窗口标题栏上的最小化、最大化、关闭按钮矩形区域变化的监听，对存在标题栏和三键区的窗口形态生效。如果使用Stage模型，该接口需要在 [loadContent()](#loadcontent) 或[setUIContent()](#setuicontent)调用生效后使用。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'windowTitleButtonRectChange', callback?: Callback<TitleButtonRect>): void--><!--Device-Window-off(type: 'windowTitleButtonRectChange', callback?: Callback<TitleButtonRect>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'windowTitleButtonRectChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[TitleButtonRect](arkts-arkui-window-titlebuttonrect-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## off_windowVisibilityChange

```TypeScript
off(type: 'windowVisibilityChange', callback?: Callback<boolean>): void
```

关闭本窗口可见状态变化事件的监听。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'windowVisibilityChange', callback?: Callback<boolean>): void--><!--Device-Window-off(type: 'windowVisibilityChange', callback?: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'windowVisibilityChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## off_windowWillClose

```TypeScript
off(type: 'windowWillClose', callback?: Callback<void, Promise<boolean>>): void
```

用于关闭主窗口或子窗口关闭事件的监听。

**起始版本：** 15

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-Window-off(type: 'windowWillClose', callback?: Callback<void, Promise<boolean>>): void--><!--Device-Window-off(type: 'windowWillClose', callback?: Callback<void, Promise<boolean>>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'windowWillClose' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void, Promise&lt;boolean&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## onAvoidAreaChange

```TypeScript
onAvoidAreaChange(callback: Callback<AvoidAreaOptions>): void
```

开启当前应用窗口系统避让区域变化的监听。 主窗口/子窗口： - [自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态的自由悬浮窗口模式（即窗口模式为 [window.WindowStatusType.FLOATING](arkts-arkui-window-windowstatustype-e.md#windowstatustype)）下触发回调时，仅存在固定态软键盘（ [AvoidAreaType](arkts-arkui-window-avoidareatype-e.md#avoidareatype)为TYPE_KEYBOARD）类型的避让区域。 - 主窗口在非自由窗口状态的自由悬浮窗口模式下触发回调时，仅存在系统栏（[AvoidAreaType](arkts-arkui-window-avoidareatype-e.md#avoidareatype)为TYPE_SYSTEM）类型的避让区域。 - 主窗口在其余场景下触发回调时，仅当在非自由悬浮窗口模式下或设备类型为Phone和Tablet，才能返回计算后的避让区域，否则直接返回空的避让区域。 - 子窗口在非自由窗口状态或非自由悬浮窗口模式下触发回调时，仅当子窗口的位置和大小与主窗口一致时，才能返回计算后的子窗口避让区域，否则直接返回空的避让区域。 全局悬浮窗、模态窗或系统窗口： - 仅在调用[setSystemAvoidAreaEnabled](#setsystemavoidareaenabled)方法使能后，触发回调时才能返回计算后的避让区域，否则直接返回空的避 让区域。 &lt;!--RP7--&gt;常见的触发避让区回调的场景如下：应用窗口在全屏模式、悬浮模式、分屏模式之间的切换；应用窗口旋转；可折叠设备在屏幕折叠状态发生变化；应用窗口在多设备之间的流转。&lt;!--RP7End--&gt;

**起始版本：** 23

<!--Device-Window-onAvoidAreaChange(callback: Callback<AvoidAreaOptions>): void--><!--Device-Window-onAvoidAreaChange(callback: Callback<AvoidAreaOptions>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[AvoidAreaOptions](arkts-arkui-window-avoidareaoptions-i.md)&gt; | 是 |

## onDialogTargetTouch

```TypeScript
onDialogTargetTouch(callback: Callback<void>): void
```

开启模态窗口所遮盖窗口的点击或触摸事件的监听，除模态窗口以外其他窗口调用此接口不生效。

**起始版本：** 23

<!--Device-Window-onDialogTargetTouch(callback: Callback<void>): void--><!--Device-Window-onDialogTargetTouch(callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 是 |

## onDisplayIdChange

```TypeScript
onDisplayIdChange(callback: Callback<number>): void
```

开启本窗口所处屏幕变化事件的监听。比如，当前窗口移动到其他屏幕时，可以从此接口监听到这个行为。

**起始版本：** 23

<!--Device-Window-onDisplayIdChange(callback: Callback<long>): void--><!--Device-Window-onDisplayIdChange(callback: Callback<long>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## onFrameMetricsMeasured

```TypeScript
onFrameMetricsMeasured(callback: Callback<FrameMetrics>): void
```

开启窗口帧率指标变化事件的监听。该接口需要在 [loadContent()](#loadcontent) 或[setUIContent()](#setuicontent)调用生效后使用。 应用注册帧率变化监听后，只有当客户端UI内容发生重绘时（如页面切换、和可响应组件交互、设置背景色和透明度等），才会触发注册的回调。但当同时使用该接口和 [postFrameCallback](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#postframecallback)、 [postDelayedFrameCallback](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#postdelayedframecallback) 、 [displaySync.on('frame')](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-displaysync-displaysync-i.md#onframe) 中的任意一个时，即使无UI内容重绘，也可能触发回调。

**起始版本：** 23

<!--Device-Window-onFrameMetricsMeasured(callback: Callback<FrameMetrics>): void--><!--Device-Window-onFrameMetricsMeasured(callback: Callback<FrameMetrics>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[FrameMetrics](arkts-arkui-window-framemetrics-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## onFreeWindowModeChange

```TypeScript
onFreeWindowModeChange(callback: Callback<boolean>): void
```

free window mode change callback on.

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-onFreeWindowModeChange(callback: Callback<boolean>): void--><!--Device-Window-onFreeWindowModeChange(callback: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## onKeyboardDidHide

```TypeScript
onKeyboardDidHide(callback: Callback<KeyboardInfo>): void
```

开启固定态软键盘隐藏动画完成的监听。此监听在固定态软键盘隐藏动画完成或软键盘由固定态切换至悬浮态时触发，此监听仅对当前拉起或隐藏固定态软键盘的应用窗口生效。对于虚拟屏上应用拉起输入法键盘到主屏上，输入法键盘显隐通知只会给主屏上 获焦窗口，而不是虚拟屏上应用窗口。 改变软键盘为固定态或者悬浮态方法详细介绍请参见[输入法服务](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeflag)。

**起始版本：** 23

<!--Device-Window-onKeyboardDidHide(callback: Callback<KeyboardInfo>): void--><!--Device-Window-onKeyboardDidHide(callback: Callback<KeyboardInfo>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## onKeyboardDidShow

```TypeScript
onKeyboardDidShow(callback: Callback<KeyboardInfo>): void
```

开启固定态软键盘显示动画完成的监听。此监听在固定态软键盘显示动画完成或软键盘由悬浮态切换至固定态时触发，此监听仅对当前拉起或隐藏固定态软键盘的应用窗口生效。对于虚拟屏上应用拉起输入法键盘到主屏上，输入法键盘显隐通知只会给主屏上 获焦窗口，而不是虚拟屏上应用窗口。 改变软键盘为固定态或者悬浮态方法详细介绍请参见[输入法服务](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeflag)。

**起始版本：** 23

<!--Device-Window-onKeyboardDidShow(callback: Callback<KeyboardInfo>): void--><!--Device-Window-onKeyboardDidShow(callback: Callback<KeyboardInfo>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## onKeyboardHeightChange

```TypeScript
onKeyboardHeightChange(callback: Callback<number>): void
```

开启固定态软键盘高度变化的监听。当软键盘从本窗口唤出且与窗口有重叠区域时，通知键盘高度变化。从API version 10开始，有关将软键盘设置为固定态或悬浮态的方法，请参见 [输入法服务](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeflag)。

**起始版本：** 23

<!--Device-Window-onKeyboardHeightChange(callback: Callback<int>): void--><!--Device-Window-onKeyboardHeightChange(callback: Callback<int>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | 是 |

## onKeyboardWillHide

```TypeScript
onKeyboardWillHide(callback: Callback<KeyboardInfo>): void
```

开启固定态软键盘即将开始隐藏的监听。此监听在固定态软键盘即将开始隐藏或软键盘由固定态切换为悬浮态时触发，此监听仅对当前拉起或隐藏固定态软键盘的应用窗口生效。对于虚拟屏上应用拉起输入法键盘到主屏上，输入法键盘显隐通知只会给主屏上 获焦窗口，而不是虚拟屏上应用窗口。 改变软键盘为固定态或者悬浮态方法详细介绍请参见[输入法服务](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeflag)。

**起始版本：** 23

<!--Device-Window-onKeyboardWillHide(callback: Callback<KeyboardInfo>): void--><!--Device-Window-onKeyboardWillHide(callback: Callback<KeyboardInfo>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## onKeyboardWillShow

```TypeScript
onKeyboardWillShow(callback: Callback<KeyboardInfo>): void
```

开启固定态软键盘即将开始显示的监听。此监听在固定态软键盘即将开始显示或软键盘由悬浮态切换为固定态时触发，此监听仅对当前拉起或隐藏固定态软键盘的应用窗口生效。对于虚拟屏上应用拉起输入法键盘到主屏上，输入法键盘显隐通知只会给主屏上 获焦窗口，而不是虚拟屏上应用窗口。

**起始版本：** 23

<!--Device-Window-onKeyboardWillShow(callback: Callback<KeyboardInfo>): void--><!--Device-Window-onKeyboardWillShow(callback: Callback<KeyboardInfo>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## onNoInteractionDetected

```TypeScript
onNoInteractionDetected(timeout: number, callback: Callback<void>): void
```

开启本窗口在指定超时时间内无交互事件的监听，交互事件支持物理键盘输入事件和屏幕触控点击事件，不支持软键盘输入事件。

**起始版本：** 23

<!--Device-Window-onNoInteractionDetected(timeout: long, callback: Callback<void>): void--><!--Device-Window-onNoInteractionDetected(timeout: long, callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timeout | number | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## onOcclusionStateChanged

```TypeScript
onOcclusionStateChanged(callback: Callback<OcclusionState>): void
```

开启窗口可见性状态变化事件的监听。本接口返回的可见性与肉眼所见的可见性可能存在区别，如以下场景： - 非主窗口的阴影区域（可分别通过[setWindowShadowEnabled](#setwindowshadowenabled)和 [setWindowShadowRadius](#setwindowshadowradius)设置是否显示阴影以及对应的阴影半径）被挡住也算遮挡，此时肉眼所见虽是 完全可见，但实际返回的是部分可见。 - 上层窗口带有透明效果时（包括完全不透明之外的所有透明程度）不会遮挡下层窗口，此时下层窗口是可见的。 - 大多数处于动画效果下的窗口也不会遮挡住下层窗口，比如在手机设备上拖动悬浮窗时返回的下层窗口依然是可见的。

**起始版本：** 23

<!--Device-Window-onOcclusionStateChanged(callback: Callback<OcclusionState>): void--><!--Device-Window-onOcclusionStateChanged(callback: Callback<OcclusionState>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[OcclusionState](arkts-arkui-window-occlusionstate-e.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## onRectChangeInGlobalDisplay

```TypeScript
onRectChangeInGlobalDisplay(callback: Callback<RectChangeOptions>): void
```

开启[全局坐标系](../../../windowmanager/window-terminology.md#全局坐标系)下窗口矩形（窗口位置及窗口大小）变化的监听事件。

**起始版本：** 23

<!--Device-Window-onRectChangeInGlobalDisplay(callback: Callback<RectChangeOptions>): void--><!--Device-Window-onRectChangeInGlobalDisplay(callback: Callback<RectChangeOptions>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;RectChangeOptions&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## onRotationChange

```TypeScript
onRotationChange(callback: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | undefined>): void
```

Register the callback of rotation change

**起始版本：** 23

<!--Device-Window-onRotationChange(callback: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | undefined>): void--><!--Device-Window-onRotationChange(callback: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | undefined>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [RotationChangeCallback](arkts-arkui-window-rotationchangecallback-t.md)&lt;[RotationChangeInfo](arkts-arkui-window-rotationchangeinfo-i.md), [RotationChangeResult](arkts-arkui-window-rotationchangeresult-i.md) \| undefined & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## onScreenshot

```TypeScript
onScreenshot(callback: Callback<void>): void
```

开启截屏事件的监听。

**起始版本：** 23

<!--Device-Window-onScreenshot(callback: Callback<void>): void--><!--Device-Window-onScreenshot(callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 是 |

## onScreenshotAppEvent

```TypeScript
onScreenshotAppEvent(callback: Callback<ScreenshotEventType>): void
```

开启屏幕截屏事件类型的监听。

**起始版本：** 23

<!--Device-Window-onScreenshotAppEvent(callback: Callback<ScreenshotEventType>): void--><!--Device-Window-onScreenshotAppEvent(callback: Callback<ScreenshotEventType>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[ScreenshotEventType](arkts-arkui-window-screenshoteventtype-e.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## onSubWindowClose

```TypeScript
onSubWindowClose(callback: Callback<void>): void
```

开启子窗口关闭事件的监听。此监听仅能通过系统提供的子窗口右上角关闭按键触发，其余关闭窗口的方式不触发回调。

**起始版本：** 23

<!--Device-Window-onSubWindowClose(callback: Callback<void>): void--><!--Device-Window-onSubWindowClose(callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## onSystemDensityChange

```TypeScript
onSystemDensityChange(callback: Callback<number>): void
```

开启本窗口所处屏幕的系统显示大小缩放系数变化事件的监听。比如，当调整窗口所处屏幕的显示大小缩放系数时，可以从此接口监听到这个行为。 在接口回调函数中，建议直接使用返回值进行vp和px的转换。例如，若返回值为density，计算px可使用vp * density = px。

**起始版本：** 23

<!--Device-Window-onSystemDensityChange(callback: Callback<double>): void--><!--Device-Window-onSystemDensityChange(callback: Callback<double>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## onTouchOutside

```TypeScript
onTouchOutside(callback: Callback<void>): void
```

开启本窗口区域范围外的点击事件的监听。

**起始版本：** 23

<!--Device-Window-onTouchOutside(callback: Callback<void>): void--><!--Device-Window-onTouchOutside(callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 是 |

## onUiExtensionSecureLimitChange

```TypeScript
onUiExtensionSecureLimitChange(callback: Callback<boolean>): void
```

UIExtension in window secure limit change callback on.

**起始版本：** 23

<!--Device-Window-onUiExtensionSecureLimitChange(callback: Callback<boolean>): void--><!--Device-Window-onUiExtensionSecureLimitChange(callback: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## onWindowEvent

```TypeScript
onWindowEvent(callback: Callback<WindowEventType>): void
```

开启窗口生命周期变化的监听。

**起始版本：** 23

<!--Device-Window-onWindowEvent(callback: Callback<WindowEventType>): void--><!--Device-Window-onWindowEvent(callback: Callback<WindowEventType>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[WindowEventType](arkts-arkui-window-windoweventtype-e.md)&gt; | 是 |

## onWindowHighlightChange

```TypeScript
onWindowHighlightChange(callback: Callback<boolean>): void
```

开启窗口激活态变化事件的监听。

**起始版本：** 23

<!--Device-Window-onWindowHighlightChange(callback: Callback<boolean>): void--><!--Device-Window-onWindowHighlightChange(callback: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## onWindowRectChange

```TypeScript
onWindowRectChange(callback: Callback<RectChangeOptions>): void
```

开启窗口矩形（窗口位置及窗口大小）变化的监听。

**起始版本：** 23

<!--Device-Window-onWindowRectChange(callback: Callback<RectChangeOptions>): void--><!--Device-Window-onWindowRectChange(callback: Callback<RectChangeOptions>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;RectChangeOptions&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## onWindowSizeChange

```TypeScript
onWindowSizeChange(callback: Callback<Size>): void
```

开启窗口尺寸变化的监听。仅在主线程调用。

**起始版本：** 23

<!--Device-Window-onWindowSizeChange(callback: Callback<Size>): void--><!--Device-Window-onWindowSizeChange(callback: Callback<Size>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;Size&gt; | 是 |

## onWindowStatusChange

```TypeScript
onWindowStatusChange(callback: Callback<WindowStatusType>): void
```

开启窗口模式变化的监听，当窗口windowStatus发生变化时进行通知（此时窗口属性可能还没有更新，如果需要在收到windowStatus变化通知时能够立即获取到变化后的窗口大小、位置，建议使用 [on('windowStatusDidChange')](#onrotationchange) ）。 使用当前接口开启监听后，在调用maximize、recover方法时会收到多次回调，如需获取去重后的回调，可使用 [on('windowStatusDidChange')](#onrotationchange) 。 > **说明：** > > 在[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下，应用的 > [targetAPIVersion](../../../quick-start/app-configuration-file.md#配置文件标签)设置小于14时，在窗口最大化状态（窗口铺满整个屏幕，2in1设备会有 > dock栏和状态栏，Tablet设备会有状态栏）时返回值对应为WindowStatusType::FULL_SCREEN。应用的 > [targetAPIVersion](../../../quick-start/app-configuration-file.md#配置文件标签)设置大于等于14时，在窗口最大化状态（窗口铺满整个屏幕，2in1设备会有 > dock栏和状态栏，Tablet设备会有状态栏）时返回值对应为WindowStatusType::MAXIMIZE。

**起始版本：** 23

<!--Device-Window-onWindowStatusChange(callback: Callback<WindowStatusType>): void--><!--Device-Window-onWindowStatusChange(callback: Callback<WindowStatusType>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;WindowStatusType&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## onWindowStatusDidChange

```TypeScript
onWindowStatusDidChange(callback: Callback<WindowStatusType>): void
```

开启窗口模式变化的监听，当窗口windowStatus发生变化后进行通知（此时窗口[Rect](arkts-arkui-window-rect-i.md#rect)属性已经完成更新）。

**起始版本：** 23

<!--Device-Window-onWindowStatusDidChange(callback: Callback<WindowStatusType>): void--><!--Device-Window-onWindowStatusDidChange(callback: Callback<WindowStatusType>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;WindowStatusType&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## onWindowTitleButtonRectChange

```TypeScript
onWindowTitleButtonRectChange(callback: Callback<TitleButtonRect>): void
```

Subscribes to the change event of the rectangle that holds the minimize, maximize, and close buttons on the title bar of the window.

**起始版本：** 23

<!--Device-Window-onWindowTitleButtonRectChange(callback: Callback<TitleButtonRect>): void--><!--Device-Window-onWindowTitleButtonRectChange(callback: Callback<TitleButtonRect>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[TitleButtonRect](arkts-arkui-window-titlebuttonrect-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## onWindowVisibilityChange

```TypeScript
onWindowVisibilityChange(callback: Callback<boolean>): void
```

开启本窗口可见状态变化事件的监听。本接口返回的可见性与肉眼所见的可见性可能存在区别，如以下场景： - 非主窗口的阴影区域（可分别通过[setWindowShadowEnabled](#setwindowshadowenabled)和 [setWindowShadowRadius](#setwindowshadowradius)设置是否显示阴影以及对应的阴影半径）被挡住也算遮挡，此时肉眼所见虽是 完全可见，但实际返回的是部分可见。 - 上层窗口带有透明效果时（包括完全不透明之外的所有透明程度）不会遮挡下层窗口，此时下层窗口是可见的。 - 大多数处于动画效果下的窗口也不会遮挡住下层窗口，比如在手机设备上拖动悬浮窗时返回的下层窗口依然是可见的。

**起始版本：** 23

<!--Device-Window-onWindowVisibilityChange(callback: Callback<boolean>): void--><!--Device-Window-onWindowVisibilityChange(callback: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## onWindowWillClose

```TypeScript
onWindowWillClose(callback: Callback<void, Promise<boolean>>): void
```

开启主窗口或子窗口关闭事件的监听。此监听仅能通过系统提供的窗口标题栏关闭按键触发，其余关闭窗口的方式不触发回调。

**起始版本：** 23

<!--Device-Window-onWindowWillClose(callback: Callback<void, Promise<boolean>>): void--><!--Device-Window-onWindowWillClose(callback: Callback<void, Promise<boolean>>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void, Promise&lt;boolean&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## on_avoidAreaChange

```TypeScript
on(type: 'avoidAreaChange', callback: Callback<AvoidAreaOptions>): void
```

开启当前应用窗口系统避让区域变化的监听。 主窗口/子窗口： - [自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态的自由悬浮窗口模式（即窗口模式为 [window.WindowStatusType.FLOATING](arkts-arkui-window-windowstatustype-e.md#windowstatustype)）下触发回调时，仅存在固定态软键盘（ [AvoidAreaType](arkts-arkui-window-avoidareatype-e.md#avoidareatype)为TYPE_KEYBOARD）类型的避让区域。 - 主窗口在非自由窗口状态的自由悬浮窗口模式下触发回调时，仅存在系统栏（[AvoidAreaType](arkts-arkui-window-avoidareatype-e.md#avoidareatype)为TYPE_SYSTEM）类型的避让区域。 - 主窗口在其余场景下触发回调时，仅当在非自由悬浮窗口模式下或设备类型为Phone和Tablet，才能返回计算后的避让区域，否则直接返回空的避让区域。 - 子窗口在非自由窗口状态或非自由悬浮窗口模式下触发回调时，仅当子窗口的位置和大小与主窗口一致时，才能返回计算后的子窗口避让区域，否则直接返回空的避让区域。 全局悬浮窗、模态窗或系统窗口： - 仅在调用[setSystemAvoidAreaEnabled](#setsystemavoidareaenabled)方法使能后，触发回调时才能返回计算后的避让区域，否则直接返回空的避 让区域。 &lt;!--RP7--&gt;常见的触发避让区回调的场景如下：应用窗口在全屏模式、悬浮模式、分屏模式之间的切换；应用窗口旋转；可折叠设备在屏幕折叠状态发生变化；应用窗口在多设备之间的流转。&lt;!--RP7End--&gt;

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'avoidAreaChange', callback: Callback<AvoidAreaOptions>): void--><!--Device-Window-on(type: 'avoidAreaChange', callback: Callback<AvoidAreaOptions>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'avoidAreaChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[AvoidAreaOptions](arkts-arkui-window-avoidareaoptions-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on_dialogTargetTouch

```TypeScript
on(type: 'dialogTargetTouch', callback: Callback<void>): void
```

开启模态窗口所遮盖窗口的点击或触摸事件的监听，除模态窗口以外其他窗口调用此接口不生效。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'dialogTargetTouch', callback: Callback<void>): void--><!--Device-Window-on(type: 'dialogTargetTouch', callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'dialogTargetTouch' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on_displayIdChange

```TypeScript
on(type: 'displayIdChange', callback: Callback<number>): void
```

开启本窗口所处屏幕变化事件的监听。比如，当前窗口移动到其他屏幕时，可以从此接口监听到这个行为。

**起始版本：** 14

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'displayIdChange', callback: Callback<long>): void--><!--Device-Window-on(type: 'displayIdChange', callback: Callback<long>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'displayIdChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## on_frameMetricsMeasured

```TypeScript
on(type: 'frameMetricsMeasured', callback: Callback<FrameMetrics>): void
```

开启窗口帧率指标变化事件的监听。该接口需要在 [loadContent()](#loadcontent) 或[setUIContent()](#setuicontent)调用生效后使用。 应用注册帧率变化监听后，只有当客户端UI内容发生重绘时（如页面切换、和可响应组件交互、设置背景色和透明度等），才会触发注册的回调。但当同时使用该接口和 [postFrameCallback](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#postframecallback)、 [postDelayedFrameCallback](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#postdelayedframecallback) 、 [displaySync.on('frame')](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-displaysync-displaysync-i.md#onframe) 中的任意一个时，即使无UI内容重绘，也可能触发回调。

**起始版本：** 22

<!--Device-Window-on(type: 'frameMetricsMeasured', callback: Callback<FrameMetrics>): void--><!--Device-Window-on(type: 'frameMetricsMeasured', callback: Callback<FrameMetrics>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'frameMetricsMeasured' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[FrameMetrics](arkts-arkui-window-framemetrics-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## on_freeWindowModeChange

```TypeScript
on(type: 'freeWindowModeChange', callback: Callback<boolean>): void
```

开启自由窗口模式变化事件的监听。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'freeWindowModeChange', callback: Callback<boolean>): void--><!--Device-Window-on(type: 'freeWindowModeChange', callback: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'freeWindowModeChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## on_keyboardDidHide

```TypeScript
on(type: 'keyboardDidHide', callback: Callback<KeyboardInfo>): void
```

开启固定态软键盘隐藏动画完成的监听。此监听在固定态软键盘隐藏动画完成或软键盘由固定态切换至悬浮态时触发，此监听仅对当前拉起或隐藏固定态软键盘的应用窗口生效。对于虚拟屏上应用拉起输入法键盘到主屏上，输入法键盘显隐通知只会给主屏上 获焦窗口，而不是虚拟屏上应用窗口。 改变软键盘为固定态或者悬浮态方法详细介绍请参见[输入法服务](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeflag)。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'keyboardDidHide', callback: Callback<KeyboardInfo>): void--><!--Device-Window-on(type: 'keyboardDidHide', callback: Callback<KeyboardInfo>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyboardDidHide' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## on_keyboardDidShow

```TypeScript
on(type: 'keyboardDidShow', callback: Callback<KeyboardInfo>): void
```

开启固定态软键盘显示动画完成的监听。此监听在固定态软键盘显示动画完成或软键盘由悬浮态切换至固定态时触发，此监听仅对当前拉起或隐藏固定态软键盘的应用窗口生效。对于虚拟屏上应用拉起输入法键盘到主屏上，输入法键盘显隐通知只会给主屏上 获焦窗口，而不是虚拟屏上应用窗口。 改变软键盘为固定态或者悬浮态方法详细介绍请参见[输入法服务](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeflag)。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'keyboardDidShow', callback: Callback<KeyboardInfo>): void--><!--Device-Window-on(type: 'keyboardDidShow', callback: Callback<KeyboardInfo>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyboardDidShow' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## on_keyboardHeightChange

```TypeScript
on(type: 'keyboardHeightChange', callback: Callback<number>): void
```

开启固定态软键盘高度变化的监听。当软键盘从本窗口唤出且与窗口有重叠区域时，通知键盘高度变化。从API version 10开始，有关将软键盘设置为固定态或悬浮态的方法，请参见 [输入法服务](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeflag)。

**起始版本：** 7

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'keyboardHeightChange', callback: Callback<int>): void--><!--Device-Window-on(type: 'keyboardHeightChange', callback: Callback<int>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyboardHeightChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on_keyboardWillHide

```TypeScript
on(type: 'keyboardWillHide', callback: Callback<KeyboardInfo>): void
```

开启固定态软键盘即将开始隐藏的监听。此监听在固定态软键盘即将开始隐藏或软键盘由固定态切换为悬浮态时触发，此监听仅对当前拉起或隐藏固定态软键盘的应用窗口生效。对于虚拟屏上应用拉起输入法键盘到主屏上，输入法键盘显隐通知只会给主屏上 获焦窗口，而不是虚拟屏上应用窗口。 改变软键盘为固定态或者悬浮态方法详细介绍请参见[输入法服务](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeflag)。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'keyboardWillHide', callback: Callback<KeyboardInfo>): void--><!--Device-Window-on(type: 'keyboardWillHide', callback: Callback<KeyboardInfo>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyboardWillHide' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## on_keyboardWillShow

```TypeScript
on(type: 'keyboardWillShow', callback: Callback<KeyboardInfo>): void
```

开启固定态软键盘即将开始显示的监听。此监听在固定态软键盘即将开始显示或软键盘由悬浮态切换为固定态时触发，此监听仅对当前拉起或隐藏固定态软键盘的应用窗口生效。对于虚拟屏上应用拉起输入法键盘到主屏上，输入法键盘显隐通知只会给主屏上 获焦窗口，而不是虚拟屏上应用窗口。 改变软键盘为固定态或者悬浮态方法详细介绍请参见[输入法服务](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeflag)。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'keyboardWillShow', callback: Callback<KeyboardInfo>): void--><!--Device-Window-on(type: 'keyboardWillShow', callback: Callback<KeyboardInfo>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyboardWillShow' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## on_noInteractionDetected

```TypeScript
on(type: 'noInteractionDetected', timeout: number, callback: Callback<void>): void
```

开启本窗口在指定超时时间内无交互事件的监听，交互事件支持物理键盘输入事件和屏幕触控点击事件，不支持软键盘输入事件。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'noInteractionDetected', timeout: number, callback: Callback<void>): void--><!--Device-Window-on(type: 'noInteractionDetected', timeout: number, callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'noInteractionDetected' | 是 |
| timeout | number | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## on_occlusionStateChanged

```TypeScript
on(type: 'occlusionStateChanged', callback: Callback<OcclusionState>): void
```

开启窗口可见性状态变化事件的监听。本接口返回的可见性与肉眼所见的可见性可能存在区别，如以下场景： - 非主窗口的阴影区域（可分别通过[setWindowShadowEnabled](#setwindowshadowenabled)和 [setWindowShadowRadius](#setwindowshadowradius)设置是否显示阴影以及对应的阴影半径）被挡住也算遮挡，此时肉眼所见虽是 完全可见，但实际返回的是部分可见。 - 上层窗口带有透明效果时（包括完全不透明之外的所有透明程度）不会遮挡下层窗口，此时下层窗口是可见的。 - 大多数处于动画效果下的窗口也不会遮挡住下层窗口，比如在手机设备上拖动悬浮窗时返回的下层窗口依然是可见的。

**起始版本：** 22

<!--Device-Window-on(type: 'occlusionStateChanged', callback: Callback<OcclusionState>): void--><!--Device-Window-on(type: 'occlusionStateChanged', callback: Callback<OcclusionState>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'occlusionStateChanged' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[OcclusionState](arkts-arkui-window-occlusionstate-e.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## on_rectChangeInGlobalDisplay

```TypeScript
on(type: 'rectChangeInGlobalDisplay', callback: Callback<RectChangeOptions>): void
```

开启[全局坐标系](../../../windowmanager/window-terminology.md#全局坐标系)下窗口矩形（窗口位置及窗口大小）变化的监听事件。

**起始版本：** 20

<!--Device-Window-on(type: 'rectChangeInGlobalDisplay', callback: Callback<RectChangeOptions>): void--><!--Device-Window-on(type: 'rectChangeInGlobalDisplay', callback: Callback<RectChangeOptions>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'rectChangeInGlobalDisplay' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;RectChangeOptions&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## on_rotationChange

```TypeScript
on(type: 'rotationChange', callback: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void>): void
```

开启窗口旋转变化的监听。[RotationChangeInfo](arkts-arkui-window-rotationchangeinfo-i.md#rotationchangeinfo)中窗口旋转事件类型为窗口即将旋转时，必须返回 [RotationChangeResult](arkts-arkui-window-rotationchangeresult-i.md#rotationchangeresult)。窗口旋转事件类型为窗口旋转结束时返回 [RotationChangeResult](arkts-arkui-window-rotationchangeresult-i.md#rotationchangeresult)不生效。 该函数只允许在主线程注册。同一个窗口多次注册同类型回调函数，只生效最新注册的同类型回调函数返回值。系统提供了超时保护机制，若20ms内窗口未返回 [RotationChangeResult](arkts-arkui-window-rotationchangeresult-i.md#rotationchangeresult)，系统不处理该返回值。

**起始版本：** 19

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'rotationChange', callback: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void>): void--><!--Device-Window-on(type: 'rotationChange', callback: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'rotationChange' | 是 |
| callback | [RotationChangeCallback](arkts-arkui-window-rotationchangecallback-t.md)&lt;[RotationChangeInfo](arkts-arkui-window-rotationchangeinfo-i.md), [RotationChangeResult](arkts-arkui-window-rotationchangeresult-i.md) \| void & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## on_screenshot

```TypeScript
on(type: 'screenshot', callback: Callback<void>): void
```

开启截屏事件的监听。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'screenshot', callback: Callback<void>): void--><!--Device-Window-on(type: 'screenshot', callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'screenshot' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on_screenshotAppEvent

```TypeScript
on(type: 'screenshotAppEvent', callback: Callback<ScreenshotEventType>): void
```

开启屏幕截屏事件类型的监听。

**起始版本：** 20

<!--Device-Window-on(type: 'screenshotAppEvent', callback: Callback<ScreenshotEventType>): void--><!--Device-Window-on(type: 'screenshotAppEvent', callback: Callback<ScreenshotEventType>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'screenshotAppEvent' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[ScreenshotEventType](arkts-arkui-window-screenshoteventtype-e.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## on_subWindowClose

```TypeScript
on(type: 'subWindowClose', callback: Callback<void>): void
```

开启子窗口关闭事件的监听。此监听仅在点击系统提供的右上角关闭按钮关闭子窗时触发，其余关闭方式不触发回调。 当重复注册窗口关闭事件的监听时，最后一次注册成功的监听事件生效。 该接口触发的窗口关闭事件监听回调函数是同步执行，子窗口的异步关闭事件监听参考 [on('windowWillClose')](#onrotationchange) 方法。 如果存在 [on('windowWillClose')](#onrotationchange) 监听事件，只响应 [on('windowWillClose')](#onrotationchange) 接口。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'subWindowClose', callback: Callback<void>): void--><!--Device-Window-on(type: 'subWindowClose', callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'subWindowClose' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## on_systemAvoidAreaChange

```TypeScript
on(type: 'systemAvoidAreaChange', callback: Callback<AvoidArea>): void
```

开启当前窗口系统避让区变化的监听。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用 > [on('avoidAreaChange')](#onrotationchange)替 > 代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [on](#onrotationchange)(type: 'avoidAreaChange', callback: Callback&lt;AvoidAreaOptions&gt;)

<!--Device-Window-on(type: 'systemAvoidAreaChange', callback: Callback<AvoidArea>): void--><!--Device-Window-on(type: 'systemAvoidAreaChange', callback: Callback<AvoidArea>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'systemAvoidAreaChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[AvoidArea](arkts-arkui-window-avoidarea-i.md)&gt; | 是 |

## on_systemDensityChange

```TypeScript
on(type: 'systemDensityChange', callback: Callback<number>): void
```

开启本窗口所处屏幕的系统显示大小缩放系数变化事件的监听。比如，当调整窗口所处屏幕的显示大小缩放系数时，可以从此接口监听到这个行为。 在接口回调函数中，建议直接使用返回值进行vp和px的转换。例如，若返回值为density，计算px可使用vp * density = px。

**起始版本：** 15

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'systemDensityChange', callback: Callback<double>): void--><!--Device-Window-on(type: 'systemDensityChange', callback: Callback<double>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'systemDensityChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## on_touchOutside

```TypeScript
on(type: 'touchOutside', callback: Callback<void>): void
```

开启本窗口区域范围外的点击事件的监听。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'touchOutside', callback: Callback<void>): void--><!--Device-Window-on(type: 'touchOutside', callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'touchOutside' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on_uiExtensionSecureLimitChange

```TypeScript
on(eventType: 'uiExtensionSecureLimitChange', callback: Callback<boolean>): void
```

开启窗口内uiExtension安全限制变化事件的监听, 建议在窗口创建后立即监听。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(eventType: 'uiExtensionSecureLimitChange', callback: Callback<boolean>): void--><!--Device-Window-on(eventType: 'uiExtensionSecureLimitChange', callback: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventType | 'uiExtensionSecureLimitChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## on_windowEvent

```TypeScript
on(type: 'windowEvent', callback: Callback<WindowEventType>): void
```

开启窗口生命周期变化的监听。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'windowEvent', callback: Callback<WindowEventType>): void--><!--Device-Window-on(type: 'windowEvent', callback: Callback<WindowEventType>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'windowEvent' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[WindowEventType](arkts-arkui-window-windoweventtype-e.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on_windowHighlightChange

```TypeScript
on(type: 'windowHighlightChange', callback: Callback<boolean>): void
```

开启窗口激活态变化事件的监听。

**起始版本：** 15

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'windowHighlightChange', callback: Callback<boolean>): void--><!--Device-Window-on(type: 'windowHighlightChange', callback: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'windowHighlightChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## on_windowRectChange

```TypeScript
on(type: 'windowRectChange', callback: Callback<RectChangeOptions>): void
```

开启窗口矩形（窗口位置及窗口大小）变化的监听。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'windowRectChange', callback: Callback<RectChangeOptions>): void--><!--Device-Window-on(type: 'windowRectChange', callback: Callback<RectChangeOptions>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'windowRectChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;RectChangeOptions&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## on_windowSizeChange

```TypeScript
on(type: 'windowSizeChange', callback: Callback<Size>): void
```

开启窗口尺寸变化的监听。仅在主线程调用。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'windowSizeChange', callback: Callback<Size>): void--><!--Device-Window-on(type: 'windowSizeChange', callback: Callback<Size>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'windowSizeChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;Size&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on_windowStatusChange

```TypeScript
on(type: 'windowStatusChange', callback: Callback<WindowStatusType>): void
```

开启窗口模式变化的监听，当窗口windowStatus发生变化时进行通知（此时窗口属性可能还没有更新，如果需要在收到windowStatus变化通知时能够立即获取到变化后的窗口大小、位置，建议使用 [on('windowStatusDidChange')](#onrotationchange) ）。 使用当前接口开启监听后，在调用maximize、recover方法时会收到多次回调，如需获取去重后的回调，可使用 [on('windowStatusDidChange')](#onrotationchange) 。 > **说明：** > > 在[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下，应用的 > [targetAPIVersion](../../../quick-start/app-configuration-file.md#配置文件标签)设置小于14时，在窗口最大化状态（窗口铺满整个屏幕，2in1设备会有 > dock栏和状态栏，Tablet设备会有状态栏）时返回值对应为WindowStatusType::FULL_SCREEN。应用的 > [targetAPIVersion](../../../quick-start/app-configuration-file.md#配置文件标签)设置大于等于14时，在窗口最大化状态（窗口铺满整个屏幕，2in1设备会有 > dock栏和状态栏，Tablet设备会有状态栏）时返回值对应为WindowStatusType::MAXIMIZE。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'windowStatusChange', callback: Callback<WindowStatusType>): void--><!--Device-Window-on(type: 'windowStatusChange', callback: Callback<WindowStatusType>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'windowStatusChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;WindowStatusType&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## on_windowStatusDidChange

```TypeScript
on(type: 'windowStatusDidChange', callback: Callback<WindowStatusType>): void
```

开启窗口模式变化的监听，当窗口windowStatus发生变化后进行通知（此时窗口[Rect](arkts-arkui-window-rect-i.md#rect)属性已经完成更新）。

**起始版本：** 20

<!--Device-Window-on(type: 'windowStatusDidChange', callback: Callback<WindowStatusType>): void--><!--Device-Window-on(type: 'windowStatusDidChange', callback: Callback<WindowStatusType>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'windowStatusDidChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;WindowStatusType&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## on_windowTitleButtonRectChange

```TypeScript
on(type: 'windowTitleButtonRectChange', callback: Callback<TitleButtonRect>): void
```

开启窗口标题栏上的最小化、最大化、关闭按钮矩形区域变化的监听，对存在标题栏和三键区的窗口形态生效。如果使用Stage模型，该接口需要在 [loadContent()](#loadcontent) 或[setUIContent()](#setuicontent)调用生效后使用。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'windowTitleButtonRectChange', callback: Callback<TitleButtonRect>): void--><!--Device-Window-on(type: 'windowTitleButtonRectChange', callback: Callback<TitleButtonRect>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'windowTitleButtonRectChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[TitleButtonRect](arkts-arkui-window-titlebuttonrect-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## on_windowVisibilityChange

```TypeScript
on(type: 'windowVisibilityChange', callback: Callback<boolean>): void
```

开启本窗口可见状态变化事件的监听。本接口返回的可见性与肉眼所见的可见性可能存在区别，如以下场景： - 非主窗口的阴影区域（可分别通过[setWindowShadowEnabled](#setwindowshadowenabled)和 [setWindowShadowRadius](#setwindowshadowradius)设置是否显示阴影以及对应的阴影半径）被挡住也算遮挡，此时肉眼所见虽是 完全可见，但实际返回的是部分可见。 - 上层窗口带有透明效果时（包括完全不透明之外的所有透明程度）不会遮挡下层窗口，此时下层窗口是可见的。 - 大多数处于动画效果下的窗口也不会遮挡住下层窗口，比如在手机设备上拖动悬浮窗时返回的下层窗口依然是可见的。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'windowVisibilityChange', callback: Callback<boolean>): void--><!--Device-Window-on(type: 'windowVisibilityChange', callback: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'windowVisibilityChange' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## on_windowWillClose

```TypeScript
on(type: 'windowWillClose', callback: Callback<void, Promise<boolean>>): void
```

开启主窗口或子窗口关闭事件的监听。此监听仅能通过系统提供的窗口标题栏关闭按键触发，其余关闭窗口的方式不触发回调。 该接口触发的回调函数是异步执行。子窗口的同步关闭事件监听参考 [on('subWindowClose')](#onrotationchange)方法。主窗口的同步关闭事件监听参考 [on('windowStageClose')](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#onwindowstageclose)方法。

**起始版本：** 15

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-Window-on(type: 'windowWillClose', callback: Callback<void, Promise<boolean>>): void--><!--Device-Window-on(type: 'windowWillClose', callback: Callback<void, Promise<boolean>>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'windowWillClose' | 是 |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void, Promise&lt;boolean&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## raiseToAppTop

```TypeScript
raiseToAppTop(): Promise<void>
```

应用子窗口调用，提升应用子窗口到顶层，只在当前应用同一个父窗口下的相同类型子窗范围内生效，对于自定义了zLevel属性的子窗口，只在当前应用同一个父窗口下相同zLevel值的子窗范围内生效。使用Promise异步回调。 使用该接口需要先创建子窗口，并确保该子窗口调用[showWindow()](#showwindow)并执行完毕。

**起始版本：** 23

<!--Device-Window-raiseToAppTop(): Promise<void>--><!--Device-Window-raiseToAppTop(): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
| [1300009](../errorcode-window.md#1300009-父窗口无效) |

## recover

```TypeScript
recover(): Promise<void>
```

将主窗口从全屏、最大化、分屏模式下还原为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING），并恢复到进入该模式之前的大小和位置，已经是自由悬浮窗口模式不可再还原。使用Promise 异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-recover(): Promise<void>--><!--Device-Window-recover(): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300001](../errorcode-window.md#1300001-重复操作) |

## recover

```TypeScript
recover(snapshotAnimationConfig: WindowSnapshotAnimationConfig): Promise<void>
```

Restores the main window from full-screen, maximized, or split-screen mode to a floating window, and resets its size and position to their previous values before full-screen, maximized, or split-screen mode was entered.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Window-recover(snapshotAnimationConfig: WindowSnapshotAnimationConfig): Promise<void>--><!--Device-Window-recover(snapshotAnimationConfig: WindowSnapshotAnimationConfig): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [snapshotAnimationConfig](arkts-arkui-window-maximizeoptions-i.md) | [WindowSnapshotAnimationConfig](arkts-arkui-window-windowsnapshotanimationconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300001](../errorcode-window.md#1300001-重复操作) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |

## resetAspectRatio

```TypeScript
resetAspectRatio(callback: AsyncCallback<void>): void
```

取消设置窗口内容布局的比例，使用callback异步回调。 仅主窗可设置，调用后将清除持久化储存的比例信息。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-resetAspectRatio(callback: AsyncCallback<void>): void--><!--Device-Window-resetAspectRatio(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## resetAspectRatio

```TypeScript
resetAspectRatio(): Promise<void>
```

取消设置窗口内容布局的比例，使用Promise异步回调。 仅主窗可设置，调用后将清除持久化储存的比例信息。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-resetAspectRatio(): Promise<void>--><!--Device-Window-resetAspectRatio(): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## resetSize

```TypeScript
resetSize(width: number, height: number): Promise<void>
```

基于窗口左上角顶点改变当前窗口大小，使用Promise异步回调。 应用主窗口与子窗口存在大小限制，默认宽度范围：[320, 1920]，默认高度范围：[240, 1920]，单位为vp。 应用主窗口与子窗口的最小宽度与最小高度可由产品端进行配置，配置后的最小宽度与最小高度以产品段配置值为准，具体尺寸限制范围可以通过 [getWindowLimits](#getwindowlimits)接口进行查询。 系统窗口存在大小限制，宽度范围：(0, 1920]，高度范围：(0, 1920]，单位为vp。 设置的宽度与高度受到此限制约束，规则： 若所设置的窗口宽/高尺寸小于窗口最小宽/高限制值，则窗口最小宽/高限制值生效； 若所设置的窗口宽/高尺寸大于窗口最大宽/高限制值，则窗口最大宽/高限制值生效。 全屏模式窗口不支持该操作。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用[resize()](#resize)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [resize](#resize)(width: int, height: int)

<!--Device-Window-resetSize(width: number, height: number): Promise<void>--><!--Device-Window-resetSize(width: number, height: number): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| width | number | 是 |
| height | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## resetSize

```TypeScript
resetSize(width: number, height: number, callback: AsyncCallback<void>): void
```

基于窗口左上角顶点改变当前窗口大小，使用callback异步回调。 应用主窗口与子窗口存在大小限制，默认宽度范围：[320, 1920]，默认高度范围：[240, 1920]，单位为vp。 应用主窗口与子窗口的最小宽度与最小高度可由产品端进行配置，配置后的最小宽度与最小高度以产品段配置值为准，具体尺寸限制范围可以通过 [getWindowLimits](#getwindowlimits)接口进行查询。 系统窗口存在大小限制，宽度范围：(0, 1920]，高度范围：(0, 1920]，单位为vp。 设置的宽度与高度受到此限制约束，规则： 若所设置的窗口宽/高尺寸小于窗口最小宽/高限制值，则窗口最小宽/高限制值生效； 若所设置的窗口宽/高尺寸大于窗口最大宽/高限制值，则窗口最大宽/高限制值生效。 全屏模式窗口不支持该操作。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用 > [resize()](#resize)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [resize](#resize)(width: int, height: int, callback: AsyncCallback&lt;void&gt;)

<!--Device-Window-resetSize(width: number, height: number, callback: AsyncCallback<void>): void--><!--Device-Window-resetSize(width: number, height: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| width | number | 是 |
| height | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## resize

```TypeScript
resize(width: number, height: number): Promise<void>
```

基于窗口左上角顶点改变当前窗口大小，使用Promise异步回调。 调用成功即返回，该接口返回后无法立即获取最终生效结果，如需立即获取，建议使用接口[resizeAsync()](#resizeasync)。 窗口存在大小限制[WindowLimits](arkts-arkui-window-windowlimits-i.md#windowlimits)，具体尺寸限制范围可以通过 [getWindowLimits](#getwindowlimits)接口进行查询。 调用该接口设置的宽度与高度受到此限制约束，规则： 若所设置的窗口宽/高尺寸小于窗口最小宽/高限制值，则窗口最小宽/高限制值生效，系统窗口和全局悬浮窗设置最小值不受窗口最小宽/高限制值限制； 若所设置的窗口宽/高尺寸大于窗口最大宽/高限制值，则窗口最大宽/高限制值生效。 该接口仅在窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，窗口模式可通过 [getWindowStatus()](#getwindowstatus)获取）时调用生效，在其他窗口模式下调用返回1300002错误码。 > **说明：** > > - 主窗口处于自由悬浮窗口模式时，在非[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下调用不报错不生效。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-resize(width: int, height: int): Promise<void>--><!--Device-Window-resize(width: int, height: int): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| width | number | 是 |
| height | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## resize

```TypeScript
resize(width: number, height: number, callback: AsyncCallback<void>): void
```

基于窗口左上角顶点改变当前窗口大小，使用callback异步回调。 调用成功即返回，该接口返回后无法立即获取最终生效结果，如需立即获取，建议使用接口[resizeAsync()](#resizeasync)。 窗口存在大小限制[WindowLimits](arkts-arkui-window-windowlimits-i.md#windowlimits)，具体尺寸限制范围可以通过 [getWindowLimits](#getwindowlimits)接口进行查询。 调用该接口设置的宽度与高度受到此限制约束，规则： 若所设置的窗口宽/高尺寸小于窗口最小宽/高限制值，则窗口最小宽/高限制值生效，系统窗口和全局悬浮窗设置最小值不受窗口最小宽/高限制值限制； 若所设置的窗口宽/高尺寸大于窗口最大宽/高限制值，则窗口最大宽/高限制值生效。 该接口仅在窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，窗口模式可通过 [getWindowStatus()](#getwindowstatus)获取）时调用生效，在其他窗口模式下调用返回1300002错误码。 > **说明：** > > - 主窗口处于自由悬浮窗口模式时，在非[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下调用不报错不生效。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-resize(width: int, height: int, callback: AsyncCallback<void>): void--><!--Device-Window-resize(width: int, height: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| width | number | 是 |
| height | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## resizeAsync

```TypeScript
resizeAsync(width: number, height: number): Promise<void>
```

基于窗口左上角顶点改变当前窗口大小，使用Promise异步回调。 调用生效后返回，回调中可使用[getWindowProperties()](#getwindowproperties)（见示例）立即获取最终生效结果。 窗口存在大小限制[WindowLimits](arkts-arkui-window-windowlimits-i.md#windowlimits)，具体尺寸限制范围可以通过 [getWindowLimits](#getwindowlimits)接口进行查询。 调用该接口设置的宽度与高度受到此限制约束，规则： 若所设置的窗口宽/高尺寸小于窗口最小宽/高限制值，则窗口最小宽/高限制值生效，系统窗口和全局悬浮窗设置最小值不受窗口最小宽/高限制值限制； 若所设置的窗口宽/高尺寸大于窗口最大宽/高限制值，则窗口最大宽/高限制值生效。 该接口仅在窗口为自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING，窗口模式可通过 [getWindowStatus()](#getwindowstatus)获取）时调用生效，否则抛出错误码1300010。 > **说明：** > > - 在非[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下，主窗口调用不生效。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-resizeAsync(width: int, height: int): Promise<void>--><!--Device-Window-resizeAsync(width: int, height: int): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| width | number | 是 |
| height | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300010](../errorcode-window.md#1300010-当前窗口模式不支持该操作) |

## restore

```TypeScript
restore(): Promise<void>
```

主窗口为最小化状态且UIAbility生命周期为onForeground时，将主窗口从最小化状态，恢复到前台显示，并恢复到进入最小化状态之前的大小和位置。主窗口为前台状态时，仅抬升主窗口层级。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-restore(): Promise<void>--><!--Device-Window-restore(): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## restoreMainWindow

```TypeScript
restoreMainWindow(wantParameters?: Record<string, Object>): Promise<void>
```

将当前窗口的主窗口恢复到前台显示，如果主窗口已处于前台，则会抬升主窗层级。此接口仅适用于类型为[TYPE_FLOAT](arkts-arkui-window-windowtype-e.md#windowtype)的窗口，并且需在窗口触发过 [DOWN](arkts-arkui-touchtype-e.md#touchtype)事件后才能调用。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Window-restoreMainWindow(wantParameters?: Record<string, Object>): Promise<void>--><!--Device-Window-restoreMainWindow(wantParameters?: Record<string, Object>): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [wantParameters](../../apis-notification-kit/arkts-apis/arkts-notification-notificationrequest-notificationparameters-i.md) | Record & lt;string, Object & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300007](../errorcode-window.md#1300007-windowextension拉起应用失败) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setAspectRatio

```TypeScript
setAspectRatio(ratio: number, callback: AsyncCallback<void>): void
```

设置窗口内容布局（不含边框和标题栏等装饰）的比例，使用callback异步回调。 > **说明：** > > - 通过其他接口如[resize](#resize)、 > [resizeAsync](#resizeasync)设置窗口大小时，不受ratio约束。 > > - 仅主窗可设置，且仅在自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）下生效。此比例参数将持久化保存，关闭应用或重启设备后，切换到自由悬浮窗口模式时，设置的比例仍然生效。 > > - 当同一应用的某个主窗口调用此接口设置宽高比生效后，后续打开的主窗口均会沿用该宽高比。若需为单个主窗口单独设置宽高比，请使用 > [setContentAspectRatio](#setcontentaspectratio)。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setAspectRatio(ratio: double, callback: AsyncCallback<void>): void--><!--Device-Window-setAspectRatio(ratio: double, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [ratio](arkts-arkui-componentutils-getitemsinshapepathparams-i-sys.md) | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setAspectRatio

```TypeScript
setAspectRatio(ratio: number): Promise<void>
```

设置窗口内容布局（不含边框和标题栏等装饰）的比例，使用Promise异步回调。 > **说明：** > > - 通过其他接口如[resize](#resize)、 > [resizeAsync](#resizeasync)设置窗口大小时，不受ratio约束。 > > - 仅主窗可设置，且仅在自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）下生效。此比例参数将持久化保存，关闭应用或重启设备后，切换到自由悬浮窗口模式时，设置的比例仍然生效。 > > - 当同一应用的某个主窗口调用此接口设置宽高比生效后，后续打开的主窗口均会沿用该宽高比。若需为单个主窗口单独设置宽高比，请使用 > [setContentAspectRatio](#setcontentaspectratio)。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setAspectRatio(ratio: double): Promise<void>--><!--Device-Window-setAspectRatio(ratio: double): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [ratio](arkts-arkui-componentutils-getitemsinshapepathparams-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setBackgroundColor

```TypeScript
setBackgroundColor(color: string): Promise<void>
```

设置窗口的背景色，使用Promise异步回调。Stage模型下，该接口需要在 [loadContent()](#loadcontent) 或[setUIContent()](#setuicontent)调用生效后使用。 > **说明：** > > 从API version 6开始支持，从API version 9开始废弃，建议使用 > [setWindowBackgroundColor()](#setwindowbackgroundcolor)替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [setWindowBackgroundColor](#setwindowbackgroundcolor)

<!--Device-Window-setBackgroundColor(color: string): Promise<void>--><!--Device-Window-setBackgroundColor(color: string): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setBackgroundColor

```TypeScript
setBackgroundColor(color: string, callback: AsyncCallback<void>): void
```

设置窗口的背景色，使用callback异步回调。Stage模型下，该接口需要在 [loadContent()](#loadcontent) 或[setUIContent()](#setuicontent)调用生效后使用。 > **说明：** > > 从API version 6开始支持，从API version 9开始废弃，建议使用 > [setWindowBackgroundColor()](#setwindowbackgroundcolor)替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [setWindowBackgroundColor](#setwindowbackgroundcolor)

<!--Device-Window-setBackgroundColor(color: string, callback: AsyncCallback<void>): void--><!--Device-Window-setBackgroundColor(color: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setBrightness

```TypeScript
setBrightness(brightness: number): Promise<void>
```

允许应用窗口设置屏幕亮度值，使用Promise异步回调。 当前屏幕亮度规格：窗口设置屏幕亮度生效时，控制中心不可以调整系统屏幕亮度，窗口恢复默认系统亮度之后，控制中心可以调整系统屏幕亮度。 > **说明：** > > 从API version 6开始支持，从API version 9开始废弃，建议使用 > [setWindowBrightness()](#setwindowbrightness)替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [setWindowBrightness](#setwindowbrightness)(brightness: double)

<!--Device-Window-setBrightness(brightness: number): Promise<void>--><!--Device-Window-setBrightness(brightness: number): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| brightness | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setBrightness

```TypeScript
setBrightness(brightness: number, callback: AsyncCallback<void>): void
```

允许应用窗口设置屏幕亮度值，使用callback异步回调。 当前屏幕亮度规格：窗口设置屏幕亮度生效时，控制中心不可以调整系统屏幕亮度，窗口恢复默认系统亮度之后，控制中心可以调整系统屏幕亮度。 > **说明：** > > 从API version 6开始支持，从API version 9开始废弃，建议使用 > [setWindowBrightness()](#setwindowbrightness) > 替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [setWindowBrightness](#setwindowbrightness)(brightness: double, callback: AsyncCallback&lt;void&gt;)

<!--Device-Window-setBrightness(brightness: number, callback: AsyncCallback<void>): void--><!--Device-Window-setBrightness(brightness: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| brightness | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setColorSpace

```TypeScript
setColorSpace(colorSpace: ColorSpace): Promise<void>
```

设置当前窗口为广色域模式或默认色域模式，使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > [setWindowColorSpace()](#setwindowcolorspace)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setWindowColorSpace](#setwindowcolorspace)(colorSpace:ColorSpace)

<!--Device-Window-setColorSpace(colorSpace: ColorSpace): Promise<void>--><!--Device-Window-setColorSpace(colorSpace: ColorSpace): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colorSpace | [ColorSpace](arkts-arkui-window-colorspace-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setColorSpace

```TypeScript
setColorSpace(colorSpace: ColorSpace, callback: AsyncCallback<void>): void
```

设置当前窗口为广色域模式或默认色域模式，使用callback异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃，建议使用 > [setWindowColorSpace()](#setwindowcolorspace) > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setWindowColorSpace](#setwindowcolorspace)(colorSpace:ColorSpace, callback: AsyncCallback&lt;void&gt;)

<!--Device-Window-setColorSpace(colorSpace: ColorSpace, callback: AsyncCallback<void>): void--><!--Device-Window-setColorSpace(colorSpace: ColorSpace, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colorSpace | [ColorSpace](arkts-arkui-window-colorspace-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setContentAspectRatio

```TypeScript
setContentAspectRatio(ratio: number, isPersistent?: boolean, needUpdateRect?: boolean): Promise<void>
```

设置窗口内容布局（不含边框和标题栏等装饰）的比例，使用Promise异步回调。 > **说明：** > > - 根据相同的ratio参数调整窗口宽高时，窗口宽高会跟随窗口边框装饰尺寸或可见性变化而调整。 > > - 通过[setWindowDecorVisible](#setwindowdecorvisible)将窗口标题栏设置为不可见时，窗口内容区域将占据原本标题栏的高度空间。 > > - 通过其他接口如[resize](#resize)、 > [resizeAsync](#resizeasync)设置窗口大小时，不受ratio约束。 > > - 仅主窗可设置，且仅在自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）下生效。

**起始版本：** 23

<!--Device-Window-setContentAspectRatio(ratio: double, isPersistent?: boolean, needUpdateRect?: boolean): Promise<void>--><!--Device-Window-setContentAspectRatio(ratio: double, isPersistent?: boolean, needUpdateRect?: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [ratio](arkts-arkui-componentutils-getitemsinshapepathparams-i-sys.md) | number | 是 |
| [isPersistent](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-backgroundtaskmanager-efficiencyresourcesinfo-i-sys.md) | boolean | 否 |
| needUpdateRect | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setDecorButtonStyle

```TypeScript
setDecorButtonStyle(dectorStyle: DecorButtonStyle): void
```

设置装饰栏按钮样式，仅对主窗和子窗生效。如果使用Stage模型，该接口需要在 [loadContent()](#loadcontent) 或[setUIContent()](#setuicontent)调用生效后使用。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setDecorButtonStyle(dectorStyle: DecorButtonStyle): void--><!--Device-Window-setDecorButtonStyle(dectorStyle: DecorButtonStyle): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dectorStyle | [DecorButtonStyle](arkts-arkui-window-decorbuttonstyle-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setDialogBackGestureEnabled

```TypeScript
setDialogBackGestureEnabled(enabled: boolean): Promise<void>
```

设置模态窗口是否响应手势返回事件，非模态窗口调用返回错误码。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setDialogBackGestureEnabled(enabled: boolean): Promise<void>--><!--Device-Window-setDialogBackGestureEnabled(enabled: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

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
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setDimBehind

```TypeScript
setDimBehind(dimBehindValue: number, callback: AsyncCallback<void>): void
```

窗口叠加时，设备有子窗口的情况下设置靠后的窗口的暗度值，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

<!--Device-Window-setDimBehind(dimBehindValue: number, callback: AsyncCallback<void>): void--><!--Device-Window-setDimBehind(dimBehindValue: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [dimBehindValue](arkts-arkui-window-windowproperties-i.md) | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setDimBehind

```TypeScript
setDimBehind(dimBehindValue: number): Promise<void>
```

窗口叠加时，设备有子窗口的情况下设置靠后的窗口的暗度值，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

<!--Device-Window-setDimBehind(dimBehindValue: number): Promise<void>--><!--Device-Window-setDimBehind(dimBehindValue: number): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [dimBehindValue](arkts-arkui-window-windowproperties-i.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setDragKeyFramePolicy

```TypeScript
setDragKeyFramePolicy(keyFramePolicy: KeyFramePolicy): Promise<KeyFramePolicy>
```

设置主窗口拖拽的关键帧策略，并使用Promise处理异步回调。 非主窗口调用时，返回1300004错误码。

**起始版本：** 23

<!--Device-Window-setDragKeyFramePolicy(keyFramePolicy: KeyFramePolicy): Promise<KeyFramePolicy>--><!--Device-Window-setDragKeyFramePolicy(keyFramePolicy: KeyFramePolicy): Promise<KeyFramePolicy>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyFramePolicy | [KeyFramePolicy](arkts-arkui-window-keyframepolicy-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[KeyFramePolicy](arkts-arkui-window-keyframepolicy-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setExclusivelyHighlighted

```TypeScript
setExclusivelyHighlighted(exclusivelyHighlighted: boolean): Promise<void>
```

设置窗口独占激活态属性。独占激活态表示窗口获焦时，会导致当前父子窗口链中处于激活态的其他窗口失去激活态。使用Promise异步回调。 此接口对主窗、模态窗不生效。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setExclusivelyHighlighted(exclusivelyHighlighted: boolean): Promise<void>--><!--Device-Window-setExclusivelyHighlighted(exclusivelyHighlighted: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| exclusivelyHighlighted | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setFloatNavigationAvoidAreaEnabled

```TypeScript
setFloatNavigationAvoidAreaEnabled(enabled: boolean): Promise<void>
```

设置当前窗口是否支持获取三键导航类型的避让区域。未调用此接口设置前，系统默认不支持获取三键导航类型的避让区域。使用Promise异步回调。 调用该接口使能后才可以通过[getWindowAvoidArea()](#getwindowavoidarea)获取到 [TYPE_FLOAT_NAVIGATION](arkts-arkui-window-avoidareatype-e.md#avoidareatype)避让类型对应的避让区域或通过 [on('avoidAreaChange')](#onrotationchange)监听 TYPE_FLOAT_NAVIGATION避让类型对应的避让区域的变化。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setFloatNavigationAvoidAreaEnabled(enabled: boolean): Promise<void>--><!--Device-Window-setFloatNavigationAvoidAreaEnabled(enabled: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

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
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setFocusable

```TypeScript
setFocusable(isFocusable: boolean): Promise<void>
```

设置使用点击或其他方式使该窗口获焦的场景时，该窗口是否支持窗口焦点从点击前的获焦窗口切换到该窗口，使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用 > [setWindowFocusable()](#setwindowfocusable)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setWindowFocusable](#setwindowfocusable)(isFocusable: boolean)

<!--Device-Window-setFocusable(isFocusable: boolean): Promise<void>--><!--Device-Window-setFocusable(isFocusable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isFocusable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setFocusable

```TypeScript
setFocusable(isFocusable: boolean, callback: AsyncCallback<void>): void
```

设置使用点击或其他方式使该窗口获焦的场景时，该窗口是否支持窗口焦点从操作前的获焦窗口切换到该窗口，使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用 > [setWindowFocusable()](#setwindowfocusable) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setWindowFocusable](#setwindowfocusable)(isFocusable: boolean, callback: AsyncCallback&lt;void&gt;)

<!--Device-Window-setFocusable(isFocusable: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setFocusable(isFocusable: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isFocusable | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setFollowParentMultiScreenPolicy

```TypeScript
setFollowParentMultiScreenPolicy(enabled: boolean): Promise<void>
```

设置子窗口在其父窗口处于拖拽移动或拖拽缩放过程时，该子窗口是否支持跨多个屏幕同时显示。使用Promise异步回调。 通过监听父窗口大小位置变化，对子窗口调用 [moveWindowTo()](#movewindowto)等接口实现子窗口跟随父窗口布局时 ，此时子窗口默认不支持跨多个屏幕同时显示。 对子窗口调用此接口后可以使能子窗口在跟随父窗口布局过程中跨多个屏幕同时显示。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setFollowParentMultiScreenPolicy(enabled: boolean): Promise<void>--><!--Device-Window-setFollowParentMultiScreenPolicy(enabled: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

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
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setFollowParentWindowLayoutEnabled

```TypeScript
setFollowParentWindowLayoutEnabled(enabled: boolean): Promise<void>
```

设置子窗或模态窗口（即WindowType为TYPE_DIALOG的窗口）的布局信息（position和size）是否跟随主窗，使用Promise异步回调。 1、只支持主窗的一级子窗或模态窗口使用该接口。 2、当子窗或模态窗口调用该接口后，立即使其布局信息与主窗完全一致并保持，除非传入false再次调用该接口，否则效果将持续。 3、当子窗或模态窗口调用该接口后，再调用moveTo、resize等修改布局信息的接口将不生效。 4、当子窗或模态窗口不再使用该功能后，不保证子窗或模态窗口的布局信息（position和size）为确定的值，需要应用重新进行设置。 该接口调用生效后， [setRelativePositionToParentWindowEnabled()](#setrelativepositiontoparentwindowenabled)接口调用不生效 。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setFollowParentWindowLayoutEnabled(enabled: boolean): Promise<void>--><!--Device-Window-setFollowParentWindowLayoutEnabled(enabled: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

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
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setFullScreen

```TypeScript
setFullScreen(isFullScreen: boolean, callback: AsyncCallback<void>): void
```

设置主窗口或子窗口的布局是否为全屏布局，使用callback异步回调。 全屏布局生效时，布局不避让状态栏与&lt;!--RP15--&gt;三键导航栏&lt;!--RP15End--&gt;，组件可能产生与其重叠的情况。 非全屏布局生效时，布局避让状态栏与&lt;!--RP15--&gt;三键导航栏&lt;!--RP15End--&gt;，组件不会与其重叠。 > **说明：** > > 从API version 6开始支持，从API version 9开始废弃，建议联合使用 > [setWindowSystemBarEnable()](#setwindowsystembarenable) > 和[setWindowLayoutFullScreen()](#setwindowlayoutfullscreen)替代实现全 > 屏。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [setWindowSystemBarEnable](#setwindowsystembarenable)(names: Array&lt;'status' | 'navigation'&gt;)

<!--Device-Window-setFullScreen(isFullScreen: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setFullScreen(isFullScreen: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isFullScreen](arkts-arkui-window-windowproperties-i.md) | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setFullScreen

```TypeScript
setFullScreen(isFullScreen: boolean): Promise<void>
```

设置主窗口或子窗口的布局是否为全屏布局，使用Promise异步回调。 全屏布局生效时，布局不避让状态栏与&lt;!--RP15--&gt;三键导航栏&lt;!--RP15End--&gt;，组件可能产生与其重叠的情况。 非全屏布局生效时，布局避让状态栏与&lt;!--RP15--&gt;三键导航栏&lt;!--RP15End--&gt;，组件不会与其重叠。 > **说明：** > > 从API version 6开始支持，从API version 9开始废弃，建议联合使用 > [setWindowSystemBarEnable()](#setwindowsystembarenable) > 和[setWindowLayoutFullScreen()](#setwindowlayoutfullscreen)替代实现全 > 屏。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [setWindowSystemBarEnable](#setwindowsystembarenable)(names: Array&lt;'status' | 'navigation'&gt;)

<!--Device-Window-setFullScreen(isFullScreen: boolean): Promise<void>--><!--Device-Window-setFullScreen(isFullScreen: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isFullScreen](arkts-arkui-window-windowproperties-i.md) | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setGestureBackEnabled

```TypeScript
setGestureBackEnabled(enabled: boolean): Promise<void>
```

设置当前窗口是否启用手势侧滑返回功能，仅主窗可以调用成功，其他类型的窗口调用返回1300004错误码。 开启此功能后，仅当窗口处于全屏模式且位于前台获焦状态下才会生效。 禁用此功能后，当前应用会禁用手势热区，侧滑返回功能失效；切换到其他应用或者回到桌面后，手势热区恢复，侧滑返回功能正常。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setGestureBackEnabled(enabled: boolean): Promise<void>--><!--Device-Window-setGestureBackEnabled(enabled: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

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
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setImmersiveModeEnabledState

```TypeScript
setImmersiveModeEnabledState(enabled: boolean): void
```

设置当前窗口是否开启沉浸式布局，该调用不会改变窗口模式和窗口大小。仅主窗口和子窗口可调用。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setImmersiveModeEnabledState(enabled: boolean): void--><!--Device-Window-setImmersiveModeEnabledState(enabled: boolean): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setKeepScreenOn

```TypeScript
setKeepScreenOn(isKeepScreenOn: boolean): Promise<void>
```

设置屏幕是否为常亮状态，使用Promise异步回调。 > **说明：** > > 从API version 6开始支持，从API version 9开始废弃，建议使用 > [setWindowKeepScreenOn()](#setwindowkeepscreenon)替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [setWindowKeepScreenOn](#setwindowkeepscreenon)(isKeepScreenOn: boolean)

<!--Device-Window-setKeepScreenOn(isKeepScreenOn: boolean): Promise<void>--><!--Device-Window-setKeepScreenOn(isKeepScreenOn: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isKeepScreenOn](arkts-arkui-window-windowproperties-i.md) | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setKeepScreenOn

```TypeScript
setKeepScreenOn(isKeepScreenOn: boolean, callback: AsyncCallback<void>): void
```

设置屏幕是否为常亮状态，使用callback异步回调。 > **说明：** > > 从API version 6开始支持，从API version 9开始废弃，建议使用 > [setWindowKeepScreenOn()](#setwindowkeepscreenon) > 替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [setWindowKeepScreenOn](#setwindowkeepscreenon)(isKeepScreenOn: boolean, callback: AsyncCallback&lt;void&gt;)

<!--Device-Window-setKeepScreenOn(isKeepScreenOn: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setKeepScreenOn(isKeepScreenOn: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isKeepScreenOn](arkts-arkui-window-windowproperties-i.md) | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setLayoutFullScreen

```TypeScript
setLayoutFullScreen(isLayoutFullScreen: boolean, callback: AsyncCallback<void>): void
```

设置主窗口或子窗口的布局是否为沉浸式布局，使用callback异步回调。 沉浸式布局生效时，布局不避让状态栏与&lt;!--RP15--&gt;三键导航栏&lt;!--RP15End--&gt;，组件可能产生与其重叠的情况。 非沉浸式布局生效时，布局避让状态栏与&lt;!--RP15--&gt;三键导航栏&lt;!--RP15End--&gt;，组件不会与其重叠。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用 > [setWindowLayoutFullScreen()](#setwindowlayoutfullscreen)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setWindowLayoutFullScreen](#setwindowlayoutfullscreen)(isLayoutFullScreen: boolean)

<!--Device-Window-setLayoutFullScreen(isLayoutFullScreen: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setLayoutFullScreen(isLayoutFullScreen: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isLayoutFullScreen](arkts-arkui-window-windowproperties-i.md) | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setLayoutFullScreen

```TypeScript
setLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void>
```

设置主窗口或子窗口的布局是否为沉浸式布局，使用Promise异步回调。 沉浸式布局生效时，布局不避让状态栏与&lt;!--RP15--&gt;三键导航栏&lt;!--RP15End--&gt;，组件可能产生与其重叠的情况。 非沉浸式布局生效时，布局避让状态栏与&lt;!--RP15--&gt;三键导航栏&lt;!--RP15End--&gt;，组件不会与其重叠。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用 > [setWindowLayoutFullScreen()](#setwindowlayoutfullscreen)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setWindowLayoutFullScreen](#setwindowlayoutfullscreen)(isLayoutFullScreen: boolean)

<!--Device-Window-setLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void>--><!--Device-Window-setLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isLayoutFullScreen](arkts-arkui-window-windowproperties-i.md) | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setOutsideTouchable

```TypeScript
setOutsideTouchable(touchable: boolean): Promise<void>
```

设置是否允许可点击子窗口之外的区域，使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。 > > 从API version 9开始，系统默认允许点击子窗口之外的区域，此接口不再支持使用，也不再提供替代接口。

**起始版本：** 7

**废弃版本：** 9

<!--Device-Window-setOutsideTouchable(touchable: boolean): Promise<void>--><!--Device-Window-setOutsideTouchable(touchable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| touchable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setOutsideTouchable

```TypeScript
setOutsideTouchable(touchable: boolean, callback: AsyncCallback<void>): void
```

设置是否允许可点击子窗口之外的区域，使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。 > > 从API version 9开始，系统默认允许点击子窗口之外的区域，此接口不再支持使用，也不再提供替代接口。

**起始版本：** 7

**废弃版本：** 9

<!--Device-Window-setOutsideTouchable(touchable: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setOutsideTouchable(touchable: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| touchable | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setParentWindow

```TypeScript
setParentWindow(windowId: number): Promise<void>
```

更改子窗口的父窗口，该父窗口仅支持同进程下的主窗口、子窗口或悬浮窗，使用Promise异步回调。 如果该子窗口处于获焦状态，且新的父窗口处于前台，则会抬升父窗口的层级。 如果该子窗口处于获焦状态，且新的父窗口的子窗口存在层级更高的模态子窗口，则焦点会转移给该模态子窗口。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setParentWindow(windowId: int): Promise<void>--><!--Device-Window-setParentWindow(windowId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
| [1300009](../errorcode-window.md#1300009-父窗口无效) |

## setPreferredOrientation

```TypeScript
setPreferredOrientation(orientation: Orientation): Promise<void>
```

设置主窗口的显示方向属性，使用Promise异步回调。非主窗口调用后不生效不报错。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setPreferredOrientation(orientation: Orientation): Promise<void>--><!--Device-Window-setPreferredOrientation(orientation: Orientation): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| orientation | [Orientation](arkts-arkui-window-orientation-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setPreferredOrientation

```TypeScript
setPreferredOrientation(orientation: Orientation, callback: AsyncCallback<void>): void
```

设置主窗口的显示方向属性，使用callback异步回调。相关横竖屏开发实践查询 [横竖屏切换](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-landscape-and-portrait-development)。非主窗口 调用后不生效不报错。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setPreferredOrientation(orientation: Orientation, callback: AsyncCallback<void>): void--><!--Device-Window-setPreferredOrientation(orientation: Orientation, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| orientation | [Orientation](arkts-arkui-window-orientation-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setPreferredOrientationWithResult

```TypeScript
setPreferredOrientationWithResult(orientation: Orientation): Promise<OrientationResult>
```

设置主窗口的显示方向属性，通过Promise异步返回显示方向的执行结果。非主窗口调用后不生效，OrientationResult返回window. [OrientationExecutionResult](arkts-arkui-window-orientationexecutionresult-e.md#orientationexecutionresult).ORIENTATION_IGNORED。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setPreferredOrientationWithResult(orientation: Orientation): Promise<OrientationResult>--><!--Device-Window-setPreferredOrientationWithResult(orientation: Orientation): Promise<OrientationResult>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| orientation | [Orientation](arkts-arkui-window-orientation-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[OrientationResult](arkts-arkui-window-orientationresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setPrivacyMode

```TypeScript
setPrivacyMode(isPrivacyMode: boolean): Promise<void>
```

设置窗口是否为隐私模式，使用Promise异步回调。设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。此接口可用于禁止截屏/录屏的场景。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用 > [setWindowPrivacyMode()](#setwindowprivacymode)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setWindowPrivacyMode](#setwindowprivacymode)(isPrivacyMode: boolean)

<!--Device-Window-setPrivacyMode(isPrivacyMode: boolean): Promise<void>--><!--Device-Window-setPrivacyMode(isPrivacyMode: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isPrivacyMode](arkts-arkui-window-windowproperties-i.md) | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setPrivacyMode

```TypeScript
setPrivacyMode(isPrivacyMode: boolean, callback: AsyncCallback<void>): void
```

设置窗口是否为隐私模式，使用callback异步回调。设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。此接口可用于禁止截屏/录屏的场景。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用 > [setWindowPrivacyMode()](#setwindowprivacymode) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setWindowPrivacyMode](#setwindowprivacymode)(isPrivacyMode: boolean, callback: AsyncCallback&lt;void&gt;)

<!--Device-Window-setPrivacyMode(isPrivacyMode: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setPrivacyMode(isPrivacyMode: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isPrivacyMode](arkts-arkui-window-windowproperties-i.md) | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setRaiseByClickEnabled

```TypeScript
setRaiseByClickEnabled(enable: boolean): Promise<void>
```

禁止/使能子窗点击抬升功能。使用Promise异步回调。 通常来说，点击一个子窗口，会将该子窗口显示抬升到应用内同一个父窗口下同类型子窗口的最上方，如果设置为false，那么点击子窗口的时候，不会将该子窗口进行抬升，而是保持不变。 使用该接口需要先创建子窗口，并确保该子窗口调用[showWindow()](#showwindow)并执行完毕。

**起始版本：** 23

<!--Device-Window-setRaiseByClickEnabled(enable: boolean): Promise<void>--><!--Device-Window-setRaiseByClickEnabled(enable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
| [1300009](../errorcode-window.md#1300009-父窗口无效) |

## setReceiveDragEventEnabled

```TypeScript
setReceiveDragEventEnabled(enabled: boolean): Promise<void>
```

设置当前窗口是否能接收[拖拽事件](../arkts-components/arkts-arkui-dragevent-i.md#dragevent)，使用Promise异步回调。 默认场景下为true，能够接收拖拽事件。 当enable为false，当前窗口不能接收拖拽事件。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Window-setReceiveDragEventEnabled(enabled: boolean): Promise<void>--><!--Device-Window-setReceiveDragEventEnabled(enabled: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

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
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setRelativePositionToParentWindowEnabled

```TypeScript
setRelativePositionToParentWindowEnabled(enabled: boolean, anchor?: WindowAnchor,
        offsetX?: number, offsetY?: number): Promise<void>
```

用于设置一级子窗是否支持与主窗保持相对位置不变。使用Promise异步回调。 该相对位置通过一级子窗与主窗之间锚点的偏移量表示，子窗和主窗使用的窗口锚点相同。 1. 只支持一级子窗调用该接口，子窗需处于自由悬浮窗口模式（即窗口模式为window.WindowStatusType.FLOATING）。 2. 当子窗调用该接口后，立即使其显示位置跟随主窗并保持相对位置不变，除非传入false再次调用该接口，否则效果将持续。 3. 当子窗调用该接口后，再调用[moveWindowTo()](#movewindowto)、[maximize()](#maximize)修改窗口位置或大小的接口将不生效。 该接口调用生效后，[setFollowParentWindowLayoutEnabled()](#setfollowparentwindowlayoutenabled)接口调用不生效。

**起始版本：** 23

<!--Device-Window-setRelativePositionToParentWindowEnabled(enabled: boolean, anchor?: WindowAnchor,        offsetX?: int, offsetY?: int): Promise<void>--><!--Device-Window-setRelativePositionToParentWindowEnabled(enabled: boolean, anchor?: WindowAnchor,        offsetX?: int, offsetY?: int): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |
| anchor | [WindowAnchor](arkts-arkui-window-windowanchor-e.md) | 否 |
| offsetX | number | 否 |
| offsetY | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setResizeByDragEnabled

```TypeScript
setResizeByDragEnabled(enable: boolean, callback: AsyncCallback<void>): void
```

禁止/使能通过拖拽方式缩放主窗口或启用装饰的子窗口的功能。使用callback异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setResizeByDragEnabled(enable: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setResizeByDragEnabled(enable: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setResizeByDragEnabled

```TypeScript
setResizeByDragEnabled(enable: boolean): Promise<void>
```

禁止/使能通过拖拽方式缩放主窗口或启用装饰的子窗口的功能。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setResizeByDragEnabled(enable: boolean): Promise<void>--><!--Device-Window-setResizeByDragEnabled(enable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setSeparationTouchEnabled

```TypeScript
setSeparationTouchEnabled(enabled: boolean): Promise<void>
```

设置当前窗口是否支持事件分离状态，使用Promise异步回调。默认场景下为true，支持事件分离状态。 当enable为true，支持事件分离状态下： - 所有手指点击产生的事件均会发送给其手指命中的窗口。 当enable为false，不支持事件分离状态下： - 当第一根手指点击持续命中该窗口未抬起时，后续其他手指无论是否点击命中该窗口，其产生的事件均会分发给该窗口。 - 当第一根手指点击未保持持续命中该窗口时，后续其他手指即使点击命中该窗口，其产生的事件也不会分发给该窗口，该事件会被系统丢弃。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Window-setSeparationTouchEnabled(enabled: boolean): Promise<void>--><!--Device-Window-setSeparationTouchEnabled(enabled: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

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
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setSpecificSystemBarEnabled

```TypeScript
setSpecificSystemBarEnabled(name: SpecificSystemBar, enable: boolean, enableAnimation?: boolean): Promise<void>
```

设置主窗口状态栏、&lt;!--RP15--&gt;三键导航栏&lt;!--RP15End--&gt;的显示或隐藏，使用Promise异步回调。 调用生效后返回并不表示状态栏、&lt;!--RP15--&gt;三键导航栏&lt;!--RP15End--&gt;的显示或隐藏已完成。子窗口调用后不生效。主窗口在非全屏/最大化模式（悬浮窗、分屏等场景）下配置不生效，进入全屏/最大化模式后配置生效。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setSpecificSystemBarEnabled(name: SpecificSystemBar, enable: boolean, enableAnimation?: boolean): Promise<void>--><!--Device-Window-setSpecificSystemBarEnabled(name: SpecificSystemBar, enable: boolean, enableAnimation?: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | [SpecificSystemBar](arkts-arkui-window-specificsystembar-t.md) | 是 |
| enable | boolean | 是 |
| enableAnimation | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setStatusBarColor

```TypeScript
setStatusBarColor(color: ColorMetrics): Promise<void>
```

设置主窗口状态栏的文字颜色，使用Promise异步回调。 子窗口不支持设置状态栏文字颜色，调用无效果。主窗口在非全屏/最大化模式（悬浮窗、分屏等场景）下配置不生效，进入全屏/最大化模式后配置生效。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setStatusBarColor(color: ColorMetrics): Promise<void>--><!--Device-Window-setStatusBarColor(color: ColorMetrics): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [ColorMetrics](../../apis-na/arkts-apis/arkts-na-graphics-colormetrics-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setSubWindowModal

```TypeScript
setSubWindowModal(isModal: boolean): Promise<void>
```

设置子窗的模态属性是否启用，使用Promise异步回调。 子窗口调用该接口时，设置子窗口模态属性是否启用。启用子窗口模态属性后，其父级窗口不能响应用户操作，直到子窗口关闭或者子窗口的模态属性被禁用。 子窗口之外的窗口调用该接口时，会报错。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setSubWindowModal(isModal: boolean): Promise<void>--><!--Device-Window-setSubWindowModal(isModal: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isModal | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setSubWindowModal

```TypeScript
setSubWindowModal(isModal: boolean, modalityType: ModalityType): Promise<void>
```

设置子窗的模态类型，使用Promise异步回调。 当子窗口模态类型为模窗口子窗时，其父级窗口不能响应用户操作，直到子窗口关闭或者子窗口的模态类型被禁用。 当子窗口模态类型为模应用子窗时，其父级窗口与该应用其他实例的窗口不能响应用户操作，直到子窗口关闭或者子窗口的模态类型被禁用。 此接口仅支持设置子窗口模态类型，当需要禁用子窗口模态属性时，建议使用 [setSubWindowModal&lt;sup&gt;12+&lt;/sup&gt;](#setsubwindowmodal)。 子窗口之外的窗口调用该接口时，会报错。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setSubWindowModal(isModal: boolean, modalityType: ModalityType): Promise<void>--><!--Device-Window-setSubWindowModal(isModal: boolean, modalityType: ModalityType): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isModal | boolean | 是 |
| [modalityType](arkts-arkui-window-subwindowoptions-i.md) | [ModalityType](arkts-arkui-window-modalitytype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setSubWindowZLevel

```TypeScript
setSubWindowZLevel(zLevel: number): Promise<void>
```

设置当前子窗口层级级别，设置了模态属性的子窗不支持。使用Promise异步回调。 通过该接口改变子窗口的显示层级时，不会发生焦点切换。推荐使用[shiftAppWindowFocus()](arkts-arkui-window-shiftappwindowfocus-f.md#shiftappwindowfocus)进行焦点切换。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setSubWindowZLevel(zLevel: int): Promise<void>--><!--Device-Window-setSubWindowZLevel(zLevel: int): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [zLevel](arkts-arkui-window-subwindowoptions-i.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
| [1300009](../errorcode-window.md#1300009-父窗口无效) |

## setSystemAvoidAreaEnabled

```TypeScript
setSystemAvoidAreaEnabled(enabled: boolean): Promise<void>
```

创建全局悬浮窗、模态窗或WindowType窗口类型为系统窗口时，调用该接口使能后才可以通过[getWindowAvoidArea()](#getwindowavoidarea)获取窗口避 让区信息或通过 [on('avoidAreaChange')](#onrotationchange)监听窗 口避让区变化。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setSystemAvoidAreaEnabled(enabled: boolean): Promise<void>--><!--Device-Window-setSystemAvoidAreaEnabled(enabled: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

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
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setSystemBarEnable

```TypeScript
setSystemBarEnable(names: Array<'status' | 'navigation'>, callback: AsyncCallback<void>): void
```

&lt;!--RP14--&gt;设置主窗口状态栏、三键导航栏的可见模式，状态栏通过status控制、三键导航栏通过navigation控制&lt;!--RP14End--&gt;，使用callback异步回调。 从API version 12开始，&lt;!--RP5--&gt;该接口在2in1设备上调用不生效。&lt;!--RP5End--&gt; 调用生效后返回并不表示状态栏、&lt;!--RP15--&gt;三键导航栏&lt;!--RP15End--&gt;的显示或隐藏已完成。子窗口调用后不生效。非全屏模式（悬浮窗、分屏等场景）下配置不生效。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用 > [setWindowSystemBarEnable()](#setwindowsystembarenable) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setWindowSystemBarEnable](#setwindowsystembarenable)(names: Array&lt;'status'|'navigation'&gt;)

<!--Device-Window-setSystemBarEnable(names: Array<'status' | 'navigation'>, callback: AsyncCallback<void>): void--><!--Device-Window-setSystemBarEnable(names: Array<'status' | 'navigation'>, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| names | Array & lt;'status' \ | 'navigation' & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setSystemBarEnable

```TypeScript
setSystemBarEnable(names: Array<'status' | 'navigation'>): Promise<void>
```

&lt;!--RP14--&gt;设置主窗口状态栏、三键导航栏的可见模式，状态栏通过status控制、三键导航栏通过navigation控制&lt;!--RP14End--&gt;，使用Promise异步回调。 从API version 12开始，&lt;!--RP5--&gt;该接口在2in1设备上调用不生效。&lt;!--RP5End--&gt; 调用生效后返回并不表示状态栏、&lt;!--RP15--&gt;三键导航栏&lt;!--RP15End--&gt;的显示或隐藏已完成。子窗口调用后不生效。非全屏模式（悬浮窗、分屏等场景）下配置不生效。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用 > [setWindowSystemBarEnable()](#setwindowsystembarenable) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setWindowSystemBarEnable](#setwindowsystembarenable)(names: Array&lt;'status'|'navigation'&gt;)

<!--Device-Window-setSystemBarEnable(names: Array<'status' | 'navigation'>): Promise<void>--><!--Device-Window-setSystemBarEnable(names: Array<'status' | 'navigation'>): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| names | Array & lt;'status' \ | 'navigation' & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setSystemBarProperties

```TypeScript
setSystemBarProperties(systemBarProperties: SystemBarProperties, callback: AsyncCallback<void>): void
```

设置主窗口&lt;!--Del--&gt;三键导航栏、&lt;!--DelEnd--&gt;状态栏的属性，使用callback异步回调，&lt;!--RP5--&gt;该接口在2in1设备上调用不生效。&lt;!--RP5End--&gt; 子窗口调用后不生效。非全屏模式（悬浮窗、分屏等场景）下配置不生效。 > **说明：** > > 从API version 6开始支持，从API version 9开始废弃，建议使用 > [setWindowSystemBarProperties()](#setwindowsystembarproperties) > 替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [setWindowSystemBarProperties](#setwindowsystembarproperties)(systemBarProperties: SystemBarProperties)

<!--Device-Window-setSystemBarProperties(systemBarProperties: SystemBarProperties, callback: AsyncCallback<void>): void--><!--Device-Window-setSystemBarProperties(systemBarProperties: SystemBarProperties, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| systemBarProperties | [SystemBarProperties](arkts-arkui-window-systembarproperties-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setSystemBarProperties

```TypeScript
setSystemBarProperties(systemBarProperties: SystemBarProperties): Promise<void>
```

设置主窗口&lt;!--Del--&gt;三键导航栏、&lt;!--DelEnd--&gt;状态栏的属性，使用Promise异步回调，&lt;!--RP5--&gt;该接口在2in1设备上调用不生效。&lt;!--RP5End--&gt; 子窗口调用后不生效。 > **说明：** > > 从API version 6开始支持，从API version 9开始废弃，建议使用 > [setWindowSystemBarProperties()](#setwindowsystembarproperties) > 替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [setWindowSystemBarProperties](#setwindowsystembarproperties)(systemBarProperties: SystemBarProperties)

<!--Device-Window-setSystemBarProperties(systemBarProperties: SystemBarProperties): Promise<void>--><!--Device-Window-setSystemBarProperties(systemBarProperties: SystemBarProperties): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| systemBarProperties | [SystemBarProperties](arkts-arkui-window-systembarproperties-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setTitleAndDockHoverShown

```TypeScript
setTitleAndDockHoverShown(isTitleHoverShown?: boolean, isDockHoverShown?: boolean): Promise<void>
```

设置主窗口进入全屏模式时鼠标Hover到热区上是否显示窗口标题栏和dock栏，使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setTitleAndDockHoverShown(isTitleHoverShown?: boolean, isDockHoverShown?: boolean): Promise<void>--><!--Device-Window-setTitleAndDockHoverShown(isTitleHoverShown?: boolean, isDockHoverShown?: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isTitleHoverShown | boolean | 否 |
| isDockHoverShown | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setTouchable

```TypeScript
setTouchable(isTouchable: boolean): Promise<void>
```

设置窗口是否为可触状态，使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用 > [setWindowTouchable()](#setwindowtouchable)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setWindowTouchable](#setwindowtouchable)(isTouchable: boolean)

<!--Device-Window-setTouchable(isTouchable: boolean): Promise<void>--><!--Device-Window-setTouchable(isTouchable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isTouchable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setTouchable

```TypeScript
setTouchable(isTouchable: boolean, callback: AsyncCallback<void>): void
```

设置窗口是否为可触状态，使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用 > [setWindowTouchable()](#setwindowtouchable) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setWindowTouchable](#setwindowtouchable)(isTouchable: boolean, callback: AsyncCallback&lt;void&gt;)

<!--Device-Window-setTouchable(isTouchable: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setTouchable(isTouchable: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isTouchable | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setUIContent

```TypeScript
setUIContent(path: string, callback: AsyncCallback<void>): void
```

根据当前工程中指定的某个页面路径为窗口加载具体页面内容，使用callback异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setUIContent(path: string, callback: AsyncCallback<void>): void--><!--Device-Window-setUIContent(path: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setUIContent

```TypeScript
setUIContent(path: string): Promise<void>
```

根据当前工程中指定的某个页面路径为窗口加载具体页面内容，使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setUIContent(path: string): Promise<void>--><!--Device-Window-setUIContent(path: string): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setWindowBackgroundColor

```TypeScript
setWindowBackgroundColor(color: string | ColorMetrics): void
```

设置窗口的背景色。 未调用该接口时，窗口在浅色模式默认背景色为`'#FFF0F0F0'`，在深色模式默认背景色为`'#FF1A1A1A'`。 Stage模型下，该接口需要在 [loadContent()](#loadcontent) 或[setUIContent()](#setuicontent)调用生效后使用。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowBackgroundColor(color: string | ColorMetrics): void--><!--Device-Window-setWindowBackgroundColor(color: string | ColorMetrics): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | string \| [ColorMetrics](../../apis-na/arkts-apis/arkts-na-graphics-colormetrics-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setWindowBrightness

```TypeScript
setWindowBrightness(brightness: number): Promise<void>
```

主窗口设置窗口亮度。当窗口处于前台且获焦时，窗口亮度生效。使用Promise异步回调。 窗口亮度生效时只会影响当前设备屏幕亮度，无法修改虚拟屏（如投屏所在的屏幕）的屏幕亮度。 当接口入参为-1时，窗口亮度恢复为系统屏幕亮度（可以通过控制中心或快捷键调整）。 当窗口退至后台时，窗口亮度失效，可以通过控制中心或快捷键调整。不建议连续调用或窗口退至后台时调用此接口，否则可能产生时序问题。 设备行为差异： 针对TV设备：当前接口不生效也不报错。 针对非2in1设备（不包含TV设备）： 在OpenHarmony 6.1之前，当前窗口的窗口亮度生效时，控制中心调整系统屏幕亮度不生效。 从OpenHarmony 6.1开始，当前窗口的窗口亮度生效时，控制中心可以调整系统屏幕亮度，同时会将当前窗口恢复为系统屏幕亮度。 针对2in1设备： 在OpenHarmony 5.0.2之前，窗口设置屏幕亮度生效时，控制中心或快捷键调整系统屏幕亮度不生效。 从OpenHarmony 5.0.2开始，窗口亮度与系统屏幕亮度保持一致，可以通过本接口、控制中心或者快捷键设置系统屏幕亮度。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowBrightness(brightness: double): Promise<void>--><!--Device-Window-setWindowBrightness(brightness: double): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| brightness | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setWindowBrightness

```TypeScript
setWindowBrightness(brightness: number, callback: AsyncCallback<void>): void
```

主窗口设置窗口亮度。当窗口处于前台且获焦时，窗口亮度生效。使用Promise异步回调。 窗口亮度生效时只会影响当前设备屏幕亮度，无法修改虚拟屏（如投屏所在的屏幕）的屏幕亮度。 当接口入参为-1时，窗口亮度恢复为系统屏幕亮度（可以通过控制中心或快捷键调整）。 当窗口退至后台时，窗口亮度失效，可以通过控制中心或快捷键调整。不建议连续调用或窗口退至后台时调用此接口，否则可能产生时序问题。 设备行为差异： 针对TV设备：当前接口不生效也不报错。 针对非2in1设备（不包含TV设备）： 在OpenHarmony 6.1之前，当前窗口的窗口亮度生效时，控制中心调整系统屏幕亮度不生效。 从OpenHarmony 6.1开始，当前窗口的窗口亮度生效时，控制中心可以调整系统屏幕亮度，同时会将当前窗口恢复为系统屏幕亮度。 针对2in1设备： 在OpenHarmony 5.0.2之前，窗口设置屏幕亮度生效时，控制中心或快捷键调整系统屏幕亮度不生效。 从OpenHarmony 5.0.2开始，窗口亮度与系统屏幕亮度保持一致，可以通过本接口、控制中心或者快捷键设置系统屏幕亮度。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowBrightness(brightness: double, callback: AsyncCallback<void>): void--><!--Device-Window-setWindowBrightness(brightness: double, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| brightness | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setWindowColorSpace

```TypeScript
setWindowColorSpace(colorSpace:ColorSpace): Promise<void>
```

设置当前窗口为广色域模式或默认色域模式，使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowColorSpace(colorSpace:ColorSpace): Promise<void>--><!--Device-Window-setWindowColorSpace(colorSpace:ColorSpace): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colorSpace | [ColorSpace](arkts-arkui-window-colorspace-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setWindowColorSpace

```TypeScript
setWindowColorSpace(colorSpace:ColorSpace, callback: AsyncCallback<void>): void
```

设置当前窗口为广色域模式或默认色域模式，使用callback异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowColorSpace(colorSpace:ColorSpace, callback: AsyncCallback<void>): void--><!--Device-Window-setWindowColorSpace(colorSpace:ColorSpace, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colorSpace | [ColorSpace](arkts-arkui-window-colorspace-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setWindowContainerColor

```TypeScript
setWindowContainerColor(activeColor: string, inactiveColor: string): void
```

设置主窗口容器在焦点态和非焦点态时的背景色。在Stage模型下，该接口需在调用 [loadContent()](#loadcontent) 或[setUIContent()](#setuicontent)后使用。 窗口容器背景色覆盖整个窗口区域，包括标题栏和内容区域。内容区域背景色默认跟随系统深浅色，当同时使用该接口和 [setWindowBackgroundColor()](#setwindowbackgroundcolor)设置背景色时，内容区域显示窗口背景色，标题栏显示窗口容器背景色。

**起始版本：** 23

**需要权限：** ohos.permission.SET_WINDOW_TRANSPARENT

<!--Device-Window-setWindowContainerColor(activeColor: string, inactiveColor: string): void--><!--Device-Window-setWindowContainerColor(activeColor: string, inactiveColor: string): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| activeColor | string | 是 |
| inactiveColor | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## setWindowCornerRadius

```TypeScript
setWindowCornerRadius(cornerRadius: number): Promise<void>
```

设置子窗或悬浮窗的圆角半径值，使用Promise异步回调。 圆角半径值过大将会导致三键（最大化、最小化、关闭按钮）位置被裁切，且会导致热区不易识别，请根据窗口大小设置合适的圆角半径值。 在调用此接口之前调用[getWindowCornerRadius()](#getwindowcornerradius)接口可以获得窗口默认圆角半径值。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowCornerRadius(cornerRadius: double): Promise<void>--><!--Device-Window-setWindowCornerRadius(cornerRadius: double): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cornerRadius | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setWindowDecorHeight

```TypeScript
setWindowDecorHeight(height: number): void
```

设置窗口的标题栏高度，对存在标题栏和三键区的窗口形态生效。如果使用Stage模型，该接口需要在 [loadContent()](#loadcontent) 或[setUIContent()](#setuicontent)调用生效后使用。 当主窗口进入全屏沉浸状态时，此时鼠标Hover到窗口标题栏热区时，会显示悬浮标题栏，悬浮标题栏高度固定为37vp。 由于系统像素转换可能存在精度误差，设置后调用[getWindowDecorHeight()](#getwindowdecorheight)获取的值可能与设置的值存在1vp的差异。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowDecorHeight(height: int): void--><!--Device-Window-setWindowDecorHeight(height: int): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| height | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setWindowDecorVisible

```TypeScript
setWindowDecorVisible(isVisible: boolean): void
```

设置窗口标题栏是否可见，对存在标题栏和三键区的窗口形态生效。Stage模型下，该接口需要在 [loadContent()](#loadcontent) 或[setUIContent()](#setuicontent)调用生效后使用。 设置窗口标题栏不可见后，当主窗口进入全屏沉浸状态时，此时鼠标Hover到上方窗口标题栏热区上会显示悬浮标题栏。若想禁用悬浮标题栏显示，请使用 [setTitleAndDockHoverShown()](#settitleanddockhovershown)接口。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowDecorVisible(isVisible: boolean): void--><!--Device-Window-setWindowDecorVisible(isVisible: boolean): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isVisible | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setWindowDelayRaiseOnDrag

```TypeScript
setWindowDelayRaiseOnDrag(isEnabled: boolean): void
```

设置窗口是否使能延迟抬升，仅主窗和子窗可设置。 不调用此接口或传入false，主窗和子窗在鼠标左键按下时，默认立即抬升。 调用此接口使能延迟抬升后，在跨窗拖拽场景，可拖拽组件所在窗口在鼠标左键按下时不会立即抬升，直到鼠标左键抬起。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowDelayRaiseOnDrag(isEnabled: boolean): void--><!--Device-Window-setWindowDelayRaiseOnDrag(isEnabled: boolean): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isEnabled | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setWindowFocusable

```TypeScript
setWindowFocusable(isFocusable: boolean): Promise<void>
```

设置窗口是否具有获得焦点的能力，使用Promise异步回调。 从API version 22开始，调用[createVirtualScreen](arkts-arkui-display-createvirtualscreen-f.md#createvirtualscreen)接口创建虚拟屏，并设置 supportsFocus配置项为false时，位于该虚拟屏的窗口无法调用该接口修改窗口的可获焦能力，如果调用，会抛出1300002错误码。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowFocusable(isFocusable: boolean): Promise<void>--><!--Device-Window-setWindowFocusable(isFocusable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isFocusable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setWindowFocusable

```TypeScript
setWindowFocusable(isFocusable: boolean, callback: AsyncCallback<void>): void
```

设置窗口是否具有获得焦点的能力，使用callback异步回调。 从API version 22开始，调用[createVirtualScreen](arkts-arkui-display-createvirtualscreen-f.md#createvirtualscreen)接口创建虚拟屏，并设置 supportsFocus配置项为false时，位于该虚拟屏的窗口无法调用该接口修改窗口的可获焦能力，如果调用，会抛出1300002错误码。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowFocusable(isFocusable: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setWindowFocusable(isFocusable: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isFocusable | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setWindowGrayScale

```TypeScript
setWindowGrayScale(grayScale: number): Promise<void>
```

设置窗口灰阶，使用Promise异步回调。该接口需要在调用 [loadContent()](#loadcontent) 或[setUIContent()](#setuicontent)使窗口加载页面内容后调用。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowGrayScale(grayScale: double): Promise<void>--><!--Device-Window-setWindowGrayScale(grayScale: double): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| grayScale | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setWindowKeepScreenOn

```TypeScript
setWindowKeepScreenOn(isKeepScreenOn: boolean): Promise<void>
```

设置当前窗口位于前台时当前设备的屏幕是否为常亮状态，异源虚拟屏下不生效。使用Promise异步回调。 仅在必要场景（导航、视频播放、绘画、游戏等场景）下，设置该属性为true；退出上述场景后，应当重置该属性为false；其他场景（无屏幕互动、音频播放等）下，不使用该接口；系统检测到非规范使用该接口时，可能会恢复自动灭屏功能。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowKeepScreenOn(isKeepScreenOn: boolean): Promise<void>--><!--Device-Window-setWindowKeepScreenOn(isKeepScreenOn: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isKeepScreenOn](arkts-arkui-window-windowproperties-i.md) | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setWindowKeepScreenOn

```TypeScript
setWindowKeepScreenOn(isKeepScreenOn: boolean, callback: AsyncCallback<void>): void
```

设置当前窗口位于前台时当前设备的屏幕是否为常亮状态，异源虚拟屏下不生效。使用callback异步回调。 仅在必要场景（导航、视频播放、绘画、游戏等场景）下，设置该属性为true；退出上述场景后，应当重置该属性为false；其他场景（无屏幕互动、音频播放等）下，不使用该接口；系统检测到非规范使用该接口时，可能会恢复自动灭屏功能。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowKeepScreenOn(isKeepScreenOn: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setWindowKeepScreenOn(isKeepScreenOn: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isKeepScreenOn](arkts-arkui-window-windowproperties-i.md) | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setWindowLayoutFullScreen

```TypeScript
setWindowLayoutFullScreen(isLayoutFullScreen: boolean, callback: AsyncCallback<void>): void
```

设置主窗口或子窗口的布局是否为沉浸式布局，使用callback异步回调。系统窗口调用不生效。 沉浸式布局生效时，布局不避让状态栏与&lt;!--RP15--&gt;三键导航栏&lt;!--RP15End--&gt;，组件可能产生与其重叠的情况。 非沉浸式布局生效时，布局避让状态栏与&lt;!--RP15--&gt;三键导航栏&lt;!--RP15End--&gt;，组件不会与其重叠。 > **说明：** > > 从API version 9开始支持，从API version 12开始废弃，建议使用Promise方式的 > [setWindowLayoutFullScreen()](#setwindowlayoutfullscreen)替代。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** [setWindowLayoutFullScreen](#setwindowlayoutfullscreen)(isLayoutFullScreen: boolean)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowLayoutFullScreen(isLayoutFullScreen: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setWindowLayoutFullScreen(isLayoutFullScreen: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isLayoutFullScreen](arkts-arkui-window-windowproperties-i.md) | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setWindowLayoutFullScreen

```TypeScript
setWindowLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void>
```

设置应用主窗口或应用子窗口的布局是否为沉浸式布局，使用Promise异步回调。其余窗口调用不生效也不报错。 沉浸式布局生效时，布局不避让状态栏与&lt;!--RP15--&gt;三键导航栏&lt;!--RP15End--&gt;，组件可能产生与其重叠的情况。 非沉浸式布局生效时，布局避让状态栏与&lt;!--RP15--&gt;三键导航栏&lt;!--RP15End--&gt;，组件不会与其重叠。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void>--><!--Device-Window-setWindowLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isLayoutFullScreen](arkts-arkui-window-windowproperties-i.md) | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setWindowLimits

```TypeScript
setWindowLimits(windowLimits: WindowLimits): Promise<WindowLimits>
```

设置当前窗口的尺寸限制，使用Promise异步回调。 默认存在一个系统尺寸限制，系统尺寸限制由产品配置决定，不可修改。 未调用setWindowLimits配置过WindowLimits时，使用[getWindowLimits](#getwindowlimits)或 [getWindowLimitsVP](#getwindowlimitsvp)可获取系统限制。 > **说明：** > > - [自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下，处于自由悬浮窗口模式（即窗口模式为 > window.WindowStatusType.FLOATING）的窗口在尺寸变化时受[WindowLimits](arkts-arkui-window-windowlimits-i.md#windowlimits)约束。触发场景包括：应用主动 > 改变窗口大小（如调用[resize()](#resize)）；系统调节窗 > 口大小（如分辨率变化、显示大小缩放系数变化）；用户拖拽缩放窗口。 > > - 非[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下，主窗口尺寸不受 > [WindowLimits](arkts-arkui-window-windowlimits-i.md#windowlimits)约束，其他类型窗口仍受 > [WindowLimits](arkts-arkui-window-windowlimits-i.md#windowlimits)约束。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowLimits(windowLimits: WindowLimits): Promise<WindowLimits>--><!--Device-Window-setWindowLimits(windowLimits: WindowLimits): Promise<WindowLimits>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowLimits | [WindowLimits](arkts-arkui-window-windowlimits-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[WindowLimits](arkts-arkui-window-windowlimits-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setWindowLimits

```TypeScript
setWindowLimits(windowLimits: WindowLimits, isForcible: boolean): Promise<WindowLimits>
```

设置当前窗口的尺寸限制，使用Promise异步回调。 默认存在一个系统尺寸限制，系统尺寸限制由产品配置决定，不可修改。 未调用setWindowLimits配置过WindowLimits时，使用[getWindowLimits](#getwindowlimits)或 [getWindowLimitsVP](#getwindowlimitsvp)可获取系统限制。 > **说明：** > > - [自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下，处于自由悬浮窗口模式（即窗口模式为 > window.WindowStatusType.FLOATING）的窗口在尺寸变化时受[WindowLimits](arkts-arkui-window-windowlimits-i.md#windowlimits)约束。触发场景包括：应用主动 > 改变窗口大小（如调用[resize()](#resize)）；系统调节窗 > 口大小（如分辨率变化、显示大小缩放系数变化）；用户拖拽缩放窗口。 > > - 非[自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下，主窗口尺寸不受 > [WindowLimits](arkts-arkui-window-windowlimits-i.md#windowlimits)约束，其他类型窗口仍受 > [WindowLimits](arkts-arkui-window-windowlimits-i.md#windowlimits)约束。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowLimits(windowLimits: WindowLimits, isForcible: boolean): Promise<WindowLimits>--><!--Device-Window-setWindowLimits(windowLimits: WindowLimits, isForcible: boolean): Promise<WindowLimits>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowLimits | [WindowLimits](arkts-arkui-window-windowlimits-i.md) | 是 |
| isForcible | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[WindowLimits](arkts-arkui-window-windowlimits-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setWindowMask

```TypeScript
setWindowMask(windowMask: Array<Array<number>>): Promise<void>
```

设置异形窗口的掩码，使用Promise异步回调。异形窗口为非常规形状的窗口，掩码用于描述异形窗口的形状。此接口仅限子窗和全局悬浮窗可用。 当异形窗口大小发生变化时，实际的显示内容为掩码大小和窗口大小的交集部分。 该接口只在多个线程操作同一个窗口时可能返回错误码1300002。窗口被销毁场景下错误码返回401。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowMask(windowMask: Array<Array<long>>): Promise<void>--><!--Device-Window-setWindowMask(windowMask: Array<Array<long>>): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowMask | Array & lt;Array & lt;number & gt; & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setWindowMaskWithAlpha

```TypeScript
setWindowMaskWithAlpha(windowMask: Uint8Array, maskWidth: number, maskHeight: number): Promise<void>
```

设置异形窗口的掩码

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Window-setWindowMaskWithAlpha(windowMask: Uint8Array, maskWidth: int, maskHeight: int): Promise<void>--><!--Device-Window-setWindowMaskWithAlpha(windowMask: Uint8Array, maskWidth: int, maskHeight: int): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowMask | Uint8Array | 是 |
| maskWidth | number | 是 |
| [maskHeight](../arkts-components/arkts-arkui-floatingtabbarstyle-i.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setWindowPrivacyMode

```TypeScript
setWindowPrivacyMode(isPrivacyMode: boolean): Promise<void>
```

设置窗口是否为隐私模式，使用Promise异步回调。 设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。 隐私模式窗口退后台后在多任务卡片中显示为白色蒙层或隐私蒙层。 未调用此接口时，窗口默认不开启隐私模式，可以被截屏或录屏。

**起始版本：** 23

**需要权限：** ohos.permission.PRIVACY_WINDOW

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowPrivacyMode(isPrivacyMode: boolean): Promise<void>--><!--Device-Window-setWindowPrivacyMode(isPrivacyMode: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isPrivacyMode](arkts-arkui-window-windowproperties-i.md) | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## setWindowPrivacyMode

```TypeScript
setWindowPrivacyMode(isPrivacyMode: boolean, callback: AsyncCallback<void>): void
```

设置窗口是否为隐私模式，使用callback异步回调。 设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。 隐私模式窗口退后台后在多任务卡片中显示为白色蒙层或隐私蒙层。 未调用此接口时，窗口默认不开启隐私模式，可以被截屏或录屏。

**起始版本：** 23

**需要权限：** ohos.permission.PRIVACY_WINDOW

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowPrivacyMode(isPrivacyMode: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setWindowPrivacyMode(isPrivacyMode: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isPrivacyMode](arkts-arkui-window-windowproperties-i.md) | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## setWindowShadowEnabled

```TypeScript
setWindowShadowEnabled(enable: boolean): Promise<void>
```

设置主窗口是否显示阴影，使用Promise异步回调。未调用该接口时，主窗口默认显示阴影。

**起始版本：** 23

**需要权限：** ohos.permission.SET_WINDOW_TRANSPARENT

<!--Device-Window-setWindowShadowEnabled(enable: boolean): Promise<void>--><!--Device-Window-setWindowShadowEnabled(enable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## setWindowShadowRadius

```TypeScript
setWindowShadowRadius(radius: number): void
```

设置子窗或悬浮窗窗口边缘阴影的模糊半径。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowShadowRadius(radius: double): void--><!--Device-Window-setWindowShadowRadius(radius: double): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| radius | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setWindowSystemBarEnable

```TypeScript
setWindowSystemBarEnable(names: Array<'status' | 'navigation'>, callback: AsyncCallback<void>): void
```

&lt;!--RP14--&gt;设置主窗口状态栏、三键导航栏的可见模式，状态栏通过status控制、三键导航栏通过navigation控制&lt;!--RP14End--&gt;，使用callback异步回调。 从API version 12开始，&lt;!--RP5--&gt;该接口在2in1设备上调用不生效。&lt;!--RP5End--&gt; 调用生效后返回并不表示状态栏、&lt;!--RP15--&gt;三键导航栏&lt;!--RP15End--&gt;的显示或隐藏已完成。子窗口调用后不生效。非全屏模式（悬浮窗、分屏等场景）下配置不生效。 > **说明：** > > 从API version 9开始支持，从API version 12开始废弃，建议使用Promise方式的 > [setWindowSystemBarEnable()](#setwindowsystembarenable) > 替代。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** [setWindowSystemBarEnable](#setwindowsystembarenable)(names: Array&lt;'status' | 'navigation'&gt;)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowSystemBarEnable(names: Array<'status' | 'navigation'>, callback: AsyncCallback<void>): void--><!--Device-Window-setWindowSystemBarEnable(names: Array<'status' | 'navigation'>, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| names | Array & lt;'status' \ | 'navigation' & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setWindowSystemBarEnable

```TypeScript
setWindowSystemBarEnable(names: Array<'status'|'navigation'>): Promise<void>
```

&lt;!--RP14--&gt;设置主窗口状态栏、三键导航栏的可见模式，状态栏通过status控制、三键导航栏通过navigation控制&lt;!--RP14End--&gt;，使用Promise异步回调。 调用生效后返回并不表示状态栏、&lt;!--RP15--&gt;三键导航栏&lt;!--RP15End--&gt;的显示或隐藏已完成。主窗口在非全屏/最大化模式（悬浮窗、分屏等场景）下配置不生效，进入全屏/最大化模式后配置生效。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowSystemBarEnable(names: Array<'status'|'navigation'>): Promise<void>--><!--Device-Window-setWindowSystemBarEnable(names: Array<'status'|'navigation'>): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| names | Array & lt;'status' \ | 'navigation' & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setWindowSystemBarProperties

```TypeScript
setWindowSystemBarProperties(systemBarProperties: SystemBarProperties, callback: AsyncCallback<void>): void
```

设置主窗口&lt;!--Del--&gt;三键导航栏、&lt;!--DelEnd--&gt;状态栏的属性，使用callback异步回调，&lt;!--RP5--&gt;该接口在2in1设备上调用不生效。&lt;!--RP5End--&gt; 子窗口调用后不生效。 > **说明：** > > 从API version 9开始支持，从API version 12开始废弃，建议使用Promise方式的 > [setWindowSystemBarProperties()](#setwindowsystembarproperties) > 替代。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** [setWindowSystemBarProperties](#setwindowsystembarproperties)(systemBarProperties: SystemBarProperties)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowSystemBarProperties(systemBarProperties: SystemBarProperties, callback: AsyncCallback<void>): void--><!--Device-Window-setWindowSystemBarProperties(systemBarProperties: SystemBarProperties, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| systemBarProperties | [SystemBarProperties](arkts-arkui-window-systembarproperties-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setWindowSystemBarProperties

```TypeScript
setWindowSystemBarProperties(systemBarProperties: SystemBarProperties): Promise<void>
```

设置主窗口&lt;!--Del--&gt;三键导航栏、&lt;!--DelEnd--&gt;状态栏的属性，使用Promise异步回调。 子窗口调用后不生效。主窗口在非全屏/最大化模式（悬浮窗、分屏等场景）下配置不生效，进入全屏/最大化模式后配置生效。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowSystemBarProperties(systemBarProperties: SystemBarProperties): Promise<void>--><!--Device-Window-setWindowSystemBarProperties(systemBarProperties: SystemBarProperties): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| systemBarProperties | [SystemBarProperties](arkts-arkui-window-systembarproperties-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setWindowTitle

```TypeScript
setWindowTitle(titleName: string): Promise<void>
```

设置窗口标题，使用Promise异步回调。如果使用Stage模型，该接口需要在 [loadContent()](#loadcontent) 或[setUIContent()](#setuicontent)调用生效后使用。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowTitle(titleName: string): Promise<void>--><!--Device-Window-setWindowTitle(titleName: string): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [titleName](../../apis-avsession-kit/arkts-apis/arkts-avsession-avmusictemplate-qrcodeinfo-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setWindowTitleButtonVisible

```TypeScript
setWindowTitleButtonVisible(isMaximizeButtonVisible: boolean, isMinimizeButtonVisible: boolean, isCloseButtonVisible?: boolean): void
```

设置主窗标题栏上的最大化、最小化、关闭按钮是否可见。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowTitleButtonVisible(isMaximizeButtonVisible: boolean, isMinimizeButtonVisible: boolean, isCloseButtonVisible?: boolean): void--><!--Device-Window-setWindowTitleButtonVisible(isMaximizeButtonVisible: boolean, isMinimizeButtonVisible: boolean, isCloseButtonVisible?: boolean): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isMaximizeButtonVisible | boolean | 是 |
| isMinimizeButtonVisible | boolean | 是 |
| isCloseButtonVisible | boolean | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setWindowTitleMoveEnabled

```TypeScript
setWindowTitleMoveEnabled(enabled: boolean): void
```

禁止/使能主窗或子窗标题栏默认移动窗口和双击最大化的功能，当禁用标题栏默认移动窗口和双击最大化的功能时，可使用[startMoving()](#startmoving)在应用热区中发起 拖拽移动，使用[maximize()](#maximize)实现最大化功能。如果使用Stage模型，该接口需要在 [loadContent()](#loadcontent) 或[setUIContent()](#setuicontent)调用生效后使用。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowTitleMoveEnabled(enabled: boolean): void--><!--Device-Window-setWindowTitleMoveEnabled(enabled: boolean): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## setWindowTopmost

```TypeScript
setWindowTopmost(isWindowTopmost: boolean): Promise<void>
```

应用主窗口调用，用于实现将窗口置于其他应用窗口之上不被遮挡，使用Promise异步回调。 应用可通过自定义快捷键实现主窗口的置顶和取消置顶。

**起始版本：** 23

**需要权限：** ohos.permission.WINDOW_TOPMOST

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowTopmost(isWindowTopmost: boolean): Promise<void>--><!--Device-Window-setWindowTopmost(isWindowTopmost: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isWindowTopmost | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## setWindowTouchable

```TypeScript
setWindowTouchable(isTouchable: boolean): Promise<void>
```

设置窗口是否为可点击状态，使用Promise异步回调。 当窗口处于可点击状态时，若用户点击命中该窗口，事件将发送给该窗口处理。当窗口处于不可点击状态时，透传点击事件，传递给下层窗口。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowTouchable(isTouchable: boolean): Promise<void>--><!--Device-Window-setWindowTouchable(isTouchable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isTouchable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setWindowTouchable

```TypeScript
setWindowTouchable(isTouchable: boolean, callback: AsyncCallback<void>): void
```

设置窗口是否为可点击状态，使用callback异步回调。 当窗口处于可点击状态时，若用户点击命中该窗口，事件将发送给该窗口处理。当窗口处于不可点击状态时，透传点击事件，传递给下层窗口。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowTouchable(isTouchable: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setWindowTouchable(isTouchable: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isTouchable | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## setWindowTransitionAnimation

```TypeScript
setWindowTransitionAnimation(transitionType: WindowTransitionType, animation: TransitionAnimation): Promise<void>
```

给特定场景下的窗口增加转场动画。 当前只支持在应用主窗下使用。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-setWindowTransitionAnimation(transitionType: WindowTransitionType, animation: TransitionAnimation): Promise<void>--><!--Device-Window-setWindowTransitionAnimation(transitionType: WindowTransitionType, animation: TransitionAnimation): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| transitionType | [WindowTransitionType](arkts-arkui-window-windowtransitiontype-e.md) | 是 |
| animation | [TransitionAnimation](arkts-arkui-window-transitionanimation-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## show

```TypeScript
show(callback: AsyncCallback<void>): void
```

显示当前窗口，使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用 > [showWindow()](#showwindow)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [showWindow](#showwindow)(callback: AsyncCallback&lt;void&gt;)

<!--Device-Window-show(callback: AsyncCallback<void>): void--><!--Device-Window-show(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## show

```TypeScript
show(): Promise<void>
```

显示当前窗口，使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用[showWindow()](#showwindow)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [showWindow](#showwindow)()

<!--Device-Window-show(): Promise<void>--><!--Device-Window-show(): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## showWindow

```TypeScript
showWindow(callback: AsyncCallback<void>): void
```

显示当前窗口，使用callback异步回调，支持系统窗口、应用子窗口、模态窗和全局悬浮窗，或将已显示的应用主窗口层级提升至顶部。 > **说明：** > > 调用该接口前，建议先通过[loadContent](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#loadcontent9)方法或者 > [setUIContent](#setuicontent)方法完成页面加载。如果应用主窗口没有完成页面加载，直接调用该接口，界面会 > 一直显示启动界面；如果系统窗口、应用子窗口、模态窗和全局悬浮窗没有完成页面加载，直接调用该接口，窗口会处于前台，但不可见。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-showWindow(callback: AsyncCallback<void>): void--><!--Device-Window-showWindow(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## showWindow

```TypeScript
showWindow(): Promise<void>
```

显示当前窗口，使用Promise异步回调，支持系统窗口、应用子窗口、模态窗和全局悬浮窗，或将已显示的应用主窗口层级提升至顶部。 > **说明：** > > 调用该接口前，建议优先通过[loadContent](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#loadcontent9)方法或者 > [setUIContent](#setuicontent)方法完成页面加载。如果应用主窗口没有完成页面加载，直接调用该接口，界面会 > 一直显示启动界面；如果系统窗口、应用子窗口、模态窗和全局悬浮窗没有完成页面加载，直接调用该接口，窗口会处于前台，但不可见。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Window-showWindow(): Promise<void>--><!--Device-Window-showWindow(): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## showWindow

```TypeScript
showWindow(options: ShowWindowOptions): Promise<void>
```

显示当前窗口或将已显示的应用主窗口的层级提升至顶部，支持传入参数来控制窗口显示的行为，使用Promise异步回调。 仅支持除TYPE_DIALOG类型的窗口和模态子窗口（即使用setSubWindowModal启用了子窗的模态属性）之外的应用子窗口、应用主窗、全局悬浮窗以及系统窗口。 > **说明：** > > 调用该接口前，建议优先通过[loadContent](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#loadcontent9)方法或者 > [setUIContent](#setuicontent)方法完成页面加载。如果应用主窗口没有完成页面加载，直接调用该接口，界面会 > 一直显示启动界面；如果系统窗口、应用子窗口和全局悬浮窗没有完成页面加载，直接调用该接口，窗口会处于前台，但不可见。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-showWindow(options: ShowWindowOptions): Promise<void>--><!--Device-Window-showWindow(options: ShowWindowOptions): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ShowWindowOptions](arkts-arkui-window-showwindowoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## snapshot

```TypeScript
snapshot(callback: AsyncCallback<image.PixelMap>): void
```

获取窗口截图，使用callback异步回调。若当前窗口设置为隐私模式（可通过 [setWindowPrivacyMode](#setwindowprivacymode) 接口设置），截图结果为白屏。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-snapshot(callback: AsyncCallback<image.PixelMap>): void--><!--Device-Window-snapshot(callback: AsyncCallback<image.PixelMap>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## snapshot

```TypeScript
snapshot(): Promise<image.PixelMap>
```

获取当前窗口截图。若当前窗口设置为隐私模式（可通过 [setWindowPrivacyMode](#setwindowprivacymode) 接口设置），截图结果为白屏。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Window-snapshot(): Promise<image.PixelMap>--><!--Device-Window-snapshot(): Promise<image.PixelMap>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## snapshotIgnorePrivacy

```TypeScript
snapshotIgnorePrivacy(): Promise<image.PixelMap>
```

获取当前窗口截图。即使当前窗口设置为隐私模式（可通过 [setWindowPrivacyMode](#setwindowprivacymode) 接口设置），仍可调用本接口返回当前窗口截图。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-snapshotIgnorePrivacy(): Promise<image.PixelMap>--><!--Device-Window-snapshotIgnorePrivacy(): Promise<image.PixelMap>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

## snapshotSync

```TypeScript
snapshotSync(): image.PixelMap
```

获取当前窗口截图，此接口为同步接口。若当前窗口设置为隐私模式（ [setWindowPrivacyMode](#setwindowprivacymode) 接口设置），截图结果为白屏。 Stage模型下，该接口需要在 [loadContent()](#loadcontent) 或[setUIContent()](#setuicontent)调用生效后使用。

**起始版本：** 23

<!--Device-Window-snapshotSync(): image.PixelMap--><!--Device-Window-snapshotSync(): image.PixelMap-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| image.PixelMap |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300018](../errorcode-window.md#1300018-api调用超时) |

## startMoving

```TypeScript
startMoving(): Promise<void>
```

开始移动窗口，使用Promise异步回调。 [自由窗口](../../../windowmanager/window-terminology.md#自由窗口)状态下，对系统窗口、应用主窗口、应用子窗口、全局悬浮窗和模态窗口生效。非自由窗口状态下，仅对系统窗口、应用子窗 口、全局悬浮窗和模态窗口生效，应用主窗口调用该接口返回801或1300004错误码。 仅在[onTouch](../../../reference/apis-arkui/arkui-ts/ts-universal-events-touch.md#touchevent对象说明)事件（其中，事件类型必须为 TouchType.Down）的回调方法中调用此接口才会有移动效果，成功调用此接口后，窗口将跟随鼠标或触摸点移动。 在点击拖拽场景下，若不期望在按下时触发拖拽事件，则可以在事件类型为[TouchType.Move](arkts-arkui-touchtype-e.md#touchtype)（需要保证当前行为已经触发 TouchType.Down事件）时调用此接口，触发移动效果。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-startMoving(): Promise<void>--><!--Device-Window-startMoving(): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300001](../errorcode-window.md#1300001-重复操作) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## startMoving

```TypeScript
startMoving(offsetX: number, offsetY: number): Promise<void>
```

指定鼠标在窗口内的位置并移动窗口，使用Promise异步回调。 在同应用内窗口分合后，且鼠标保持按下状态直接移动新窗口，如果此时鼠标快速移动，窗口移动时鼠标可能会在窗口外。可以使用本接口指定窗口移动时鼠标在窗口内的位置，先移动窗口到鼠标位置，再开始移动窗口。 仅在[onTouch](../../../reference/apis-arkui/arkui-ts/ts-universal-events-touch.md#touchevent对象说明)事件（其中，事件类型必须为 TouchType.Down）的回调方法中调用此接口才会有移动效果，成功调用此接口后，窗口将跟随鼠标移动。 在点击拖拽场景下，若不期望在按下时触发拖拽事件，则可以在事件类型为[TouchType.Move](arkts-arkui-touchtype-e.md#touchtype)（需要保证当前行为已经触发 TouchType.Down事件）时调用此接口，触发移动效果。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-startMoving(offsetX: int, offsetY: int): Promise<void>--><!--Device-Window-startMoving(offsetX: int, offsetY: int): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offsetX | number | 是 |
| offsetY | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300001](../errorcode-window.md#1300001-重复操作) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |

## stopMoving

```TypeScript
stopMoving(): Promise<void>
```

在窗口拖拽移动过程中，通过此接口来停止窗口移动，使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Window-stopMoving(): Promise<void>--><!--Device-Window-stopMoving(): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
