# Window

Represents a window instance, which is the basic unit managed by the window manager. In the following API examples, you must use [getLastWindow()](arkts-arkui-window-getlastwindow-f.md#getLastWindow), [createWindow()](arkts-arkui-window-createwindow-f.md#createWindow), or [findWindow()](arkts-arkui-window-findwindow-f.md#findWindow) to obtain a Window instance (named windowClass in this example) and then call a method in this instance.

**Since:** 23

**Deprecated since:** -1

<!--Device-window-interface Window--><!--Device-window-interface Window-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## Modules to Import

```TypeScript
import { window } from '@kit.ArkUI';
```

## clearWindowMask

```TypeScript
clearWindowMask(): Promise<void>
```

Clear the window mask of window

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Window-clearWindowMask(): Promise<void>--><!--Device-Window-clearWindowMask(): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## clientToGlobalDisplay

```TypeScript
clientToGlobalDisplay(winX: number, winY: number): Position
```

Converts relative coordinates (based on the top-left corner of the current window) into global coordinates (based on the top-left corner of the primary screen). This API is not supported in windows that are subject to display scaling, such as floating windows on phones or tablets not in free windows mode.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-clientToGlobalDisplay(winX: int, winY: int): Position--><!--Device-Window-clientToGlobalDisplay(winX: int, winY: int): Position-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| winX | number | Yes |
| winY | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Position](arkts-arkui-display-position-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
| [1300010](../errorcode-window.md#1300010-unsupported-operation-in-the-current-window-mode) |

## convertOrientationAndRotation

```TypeScript
convertOrientationAndRotation(from: RotationInfoType, to: RotationInfoType, value: number): number
```

Enables conversion between window orientation, screen orientation, and screen angle. Window orientation refers to the direction of the screen where the window resides, using the Window module's definitions for portrait and landscape modes. Window orientations are represented by the digits 0, 1, 2, and 3, corresponding to portrait, reverse landscape, reverse portrait, and landscape, respectively. These definitions match those in [RotationChangeInfo](arkts-arkui-window-rotationchangeinfo-i.md#RotationChangeInfo) and the [Orientation](arkts-arkui-window-orientation-e.md#Orientation) enum. For example, setting **Orientation** to **LANDSCAPE** indicates a landscape window orientation. > **NOTE：**> > The following figure and table show the relationship between the window orientation, screen orientation, and > screen angle of a bar-type device. > >  > | Screen Angle| Screen Orientation| Window Orientation| | ------- | ------- | ------- | | 0 | PORTRAIT | PORTRAIT | | 90 | LANDSCAPE | LANDSCAPE_INVERTED | | 180 | PORTRAIT_INVERTED | PORTRAIT_INVERTED | | 270 | LANDSCAPE_INVERTED | LANDSCAPE |

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-convertOrientationAndRotation(from: RotationInfoType, to: RotationInfoType, value: int): int--><!--Device-Window-convertOrientationAndRotation(from: RotationInfoType, to: RotationInfoType, value: int): int-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| from | [RotationInfoType](arkts-arkui-window-rotationinfotype-e.md) | Yes |
| to | [RotationInfoType](arkts-arkui-window-rotationinfotype-e.md) | Yes |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## createSubWindowWithOptions

```TypeScript
createSubWindowWithOptions(name: string, options: SubWindowOptions): Promise<Window>
```

Creates a child window under the main window, another child window, or floating window. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-createSubWindowWithOptions(name: string, options: SubWindowOptions): Promise<Window>--><!--Device-Window-createSubWindowWithOptions(name: string, options: SubWindowOptions): Promise<Window>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| options | [SubWindowOptions](arkts-arkui-window-subwindowoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Window](arkts-arkui-window-window-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## destroy

```TypeScript
destroy(callback: AsyncCallback<void>): void
```

Destroys this window. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [destroyWindow](#destroyWindow)(callback: AsyncCallback&lt;void&gt;)

<!--Device-Window-destroy(callback: AsyncCallback<void>): void--><!--Device-Window-destroy(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## destroy

```TypeScript
destroy(): Promise<void>
```

Destroys this window. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [destroyWindow](#destroyWindow)()

<!--Device-Window-destroy(): Promise<void>--><!--Device-Window-destroy(): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## destroyWindow

```TypeScript
destroyWindow(callback: AsyncCallback<void>): void
```

Destroys this window. This API uses an asynchronous callback to return the result. It takes effect for a system window, an application child window, a global floating window, or a modal window.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-destroyWindow(callback: AsyncCallback<void>): void--><!--Device-Window-destroyWindow(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## destroyWindow

```TypeScript
destroyWindow(): Promise<void>
```

Destroys this window. This API uses a promise to return the result. It takes effect for a system window, an application child window, a global floating window, or a modal window.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-destroyWindow(): Promise<void>--><!--Device-Window-destroyWindow(): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## disableLandscapeMultiWindow

```TypeScript
disableLandscapeMultiWindow(): Promise<void>
```

Disables the landscape multi-window mode for the UI page that supports the horizontal layout. This API takes effect only for the main window of the application. In addition, **preferMultiWindowOrientation** must be set to **landscape_auto** in the [abilities](../../../quick-start/module-configuration-file.md#abilities) tag in the **module.json5** file.

**Since:** 26.0.0

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Window-disableLandscapeMultiWindow(): Promise<void>--><!--Device-Window-disableLandscapeMultiWindow(): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## enableLandscapeMultiWindow

```TypeScript
enableLandscapeMultiWindow(): Promise<void>
```

Enables the landscape multi-window mode for the UI page that supports the horizontal layout. You are not advised to call this API for the UI page that adopts the vertical layout. This API takes effect only for the main window of the application. In addition, **preferMultiWindowOrientation** must be set to **landscape_auto** in the [abilities](../../../quick-start/module-configuration-file.md#abilities) tag in the **module.json5** file.

**Since:** 26.0.0

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Window-enableLandscapeMultiWindow(): Promise<void>--><!--Device-Window-enableLandscapeMultiWindow(): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## getAvoidArea

```TypeScript
getAvoidArea(type: AvoidAreaType, callback: AsyncCallback<AvoidArea>): void
```

Obtains the area where this window cannot be displayed, for example, the system bar area, notch, gesture area, and soft keyboard area. This API uses an asynchronous callback to return the result. Main window/Child window: - In the free-floating window mode under the [freeform window](../../../windowmanager/window-terminology.md#freeform-window) state (the window mode is **window.WindowStatusType.FLOATING**), only the avoidance area of the fixed soft keyboard type ( [AvoidAreaType](arkts-arkui-window-avoidareatype-e.md#AvoidAreaType) is **TYPE_KEYBOARD**) is available. - In the free-floating window mode of the main window in the non-freeform window state, only the avoidance area of the system bar type ([AvoidAreaType](arkts-arkui-window-avoidareatype-e.md#AvoidAreaType) is **TYPE_SYSTEM**) is available. - In other scenarios, this API can be called to obtain the calculated avoidance area only when the main window is not in the free-floating window mode or the device type is phone or tablet. Otherwise, the obtained avoidance area is empty. - For the child window in the non-freeform window state or non-free-floating window mode, this API can be called to obtain the calculated avoidance area only when the position and size of the child window are the same as those of the main window. Otherwise, the obtained avoidance area is empty. Global floating window, modal window, or system window: - This API can be called to obtain the avoidance area only after [setSystemAvoidAreaEnabled](#setSystemAvoidAreaEnabled) is called. Otherwise, the obtained avoidance area is empty.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getWindowAvoidArea](#getWindowAvoidArea)

<!--Device-Window-getAvoidArea(type: AvoidAreaType, callback: AsyncCallback<AvoidArea>): void--><!--Device-Window-getAvoidArea(type: AvoidAreaType, callback: AsyncCallback<AvoidArea>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [AvoidAreaType](arkts-arkui-window-avoidareatype-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AvoidArea](arkts-arkui-window-avoidarea-i.md)&gt; | Yes |

## getAvoidArea

```TypeScript
getAvoidArea(type: AvoidAreaType): Promise<AvoidArea>
```

Obtains the area where this window cannot be displayed, for example, the system bar area, notch, gesture area, and soft keyboard area. This API uses an asynchronous callback to return the result. Main window/Child window: - In the free-floating window mode under the [freeform window](../../../windowmanager/window-terminology.md#freeform-window) state (the window mode is **window.WindowStatusType.FLOATING**), only the avoidance area of the fixed soft keyboard type ( [AvoidAreaType](arkts-arkui-window-avoidareatype-e.md#AvoidAreaType) is **TYPE_KEYBOARD**) is available. - In the free-floating window mode of the main window in the non-freeform window state, only the avoidance area of the system bar type ([AvoidAreaType](arkts-arkui-window-avoidareatype-e.md#AvoidAreaType) is **TYPE_SYSTEM**) is available. - In other scenarios, this API can be called to obtain the calculated avoidance area only when the main window is not in the free-floating window mode or the device type is phone or tablet. Otherwise, the obtained avoidance area is empty. - For the child window in the non-freeform window state or non-free-floating window mode, this API can be called to obtain the calculated avoidance area only when the position and size of the child window are the same as those of the main window. Otherwise, the obtained avoidance area is empty. Global floating window, modal window, or system window: - This API can be called to obtain the avoidance area only after [setSystemAvoidAreaEnabled](#setSystemAvoidAreaEnabled) is called. Otherwise, the obtained avoidance area is empty.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getWindowAvoidArea](#getWindowAvoidArea)

<!--Device-Window-getAvoidArea(type: AvoidAreaType): Promise<AvoidArea>--><!--Device-Window-getAvoidArea(type: AvoidAreaType): Promise<AvoidArea>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [AvoidAreaType](arkts-arkui-window-avoidareatype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AvoidArea](arkts-arkui-window-avoidarea-i.md)&gt; |

## getColorSpace

```TypeScript
getColorSpace(): Promise<ColorSpace>
```

Obtains the color space of this window. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getWindowColorSpace](#getWindowColorSpace)

<!--Device-Window-getColorSpace(): Promise<ColorSpace>--><!--Device-Window-getColorSpace(): Promise<ColorSpace>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ColorSpace & gt; |

## getColorSpace

```TypeScript
getColorSpace(callback: AsyncCallback<ColorSpace>): void
```

Obtains the color space of this window. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getWindowColorSpace](#getWindowColorSpace)

<!--Device-Window-getColorSpace(callback: AsyncCallback<ColorSpace>): void--><!--Device-Window-getColorSpace(callback: AsyncCallback<ColorSpace>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ColorSpace&gt; | Yes |

## getDecorButtonStyle

```TypeScript
getDecorButtonStyle(): DecorButtonStyle
```

Obtains the button style of the decoration bar. The setting takes effect only for the main window and child windows.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-getDecorButtonStyle(): DecorButtonStyle--><!--Device-Window-getDecorButtonStyle(): DecorButtonStyle-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DecorButtonStyle](arkts-arkui-window-decorbuttonstyle-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## getGlobalRect

```TypeScript
getGlobalRect(): Rect
```

Obtains the actual display area of this window on the physical screen. This API returns the result synchronously. This API can determine the actual on-screen location and size of a window that has been resized on certain devices.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-getGlobalRect(): Rect--><!--Device-Window-getGlobalRect(): Rect-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## getImmersiveModeEnabledState

```TypeScript
getImmersiveModeEnabledState(): boolean
```

Checks whether the immersive layout is enabled for this window. This API can be called only by the main window and child windows. The return value is consistent with the settings applied via [setImmersiveModeEnabledState()](#setImmersiveModeEnabledState) and [setWindowLayoutFullScreen()](#setWindowLayoutFullScreen). If neither of these APIs has been called, the default return value is **false**.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-getImmersiveModeEnabledState(): boolean--><!--Device-Window-getImmersiveModeEnabledState(): boolean-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## getParentWindow

```TypeScript
getParentWindow(): Window
```

Obtains the parent window of this child window.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-getParentWindow(): Window--><!--Device-Window-getParentWindow(): Window-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Window](arkts-arkui-window-window-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [1300009](../errorcode-window.md#1300009-invalid-parent-window) |

## getPreferredOrientation

```TypeScript
getPreferredOrientation(): Orientation
```

Obtains the orientation of the window. If no orientation is specified, **window.Orientation.UNSPECIFIED** is returned.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-getPreferredOrientation(): Orientation--><!--Device-Window-getPreferredOrientation(): Orientation-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Orientation](arkts-arkui-window-orientation-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## getProperties

```TypeScript
getProperties(callback: AsyncCallback<WindowProperties>): void
```

Obtains the properties of this window. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getWindowProperties](#getWindowProperties)

<!--Device-Window-getProperties(callback: AsyncCallback<WindowProperties>): void--><!--Device-Window-getProperties(callback: AsyncCallback<WindowProperties>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[WindowProperties](arkts-arkui-window-windowproperties-i.md)&gt; | Yes |

## getProperties

```TypeScript
getProperties(): Promise<WindowProperties>
```

Obtains the properties of this window. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getWindowProperties](#getWindowProperties)

<!--Device-Window-getProperties(): Promise<WindowProperties>--><!--Device-Window-getProperties(): Promise<WindowProperties>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[WindowProperties](arkts-arkui-window-windowproperties-i.md)&gt; |

## getStatusBarProperty

```TypeScript
getStatusBarProperty(): StatusBarProperty
```

Obtains the properties (for example, text color) of the status bar in the main window. Calling this API is not supported for child window and will cause error code 1300004.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-getStatusBarProperty(): StatusBarProperty--><!--Device-Window-getStatusBarProperty(): StatusBarProperty-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [StatusBarProperty](arkts-arkui-window-statusbarproperty-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## getSubWindowZLevel

```TypeScript
getSubWindowZLevel(): number
```

Obtains the z-level of the current child window. This API cannot be called by the main window or system window.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-getSubWindowZLevel(): int--><!--Device-Window-getSubWindowZLevel(): int-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## getTitleButtonRect

```TypeScript
getTitleButtonRect(): TitleButtonRect
```

Obtains the rectangle that holds the minimize, maximize, and close buttons on the title bar of the main window or the decorated child window.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-getTitleButtonRect(): TitleButtonRect--><!--Device-Window-getTitleButtonRect(): TitleButtonRect-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TitleButtonRect](arkts-arkui-window-titlebuttonrect-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## getUIContext

```TypeScript
getUIContext() : UIContext
```

Obtains a UIContext instance.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-getUIContext() : UIContext--><!--Device-Window-getUIContext() : UIContext-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## getWindowAvoidArea

```TypeScript
getWindowAvoidArea(type: AvoidAreaType): AvoidArea
```

Obtains the avoid area of this window. Main window/Child window: - In the free-floating window mode under the [freeform window](../../../windowmanager/window-terminology.md#freeform-window) state (the window mode is **window.WindowStatusType.FLOATING**), only the avoidance area of the fixed soft keyboard type ( [AvoidAreaType](arkts-arkui-window-avoidareatype-e.md#AvoidAreaType) is **TYPE_KEYBOARD**) is available. - In the free-floating window mode of the main window in the non-freeform window state, only the avoidance area of the system bar type ([AvoidAreaType](arkts-arkui-window-avoidareatype-e.md#AvoidAreaType) is **TYPE_SYSTEM**) is available. - In other scenarios, this API can be called to obtain the calculated avoidance area only when the main window is not in the free-floating window mode or the device type is phone or tablet. Otherwise, the obtained avoidance area is empty. - For the child window in the non-freeform window state or non-free-floating window mode, this API can be called to obtain the calculated avoidance area only when the position and size of the child window are the same as those of the main window. Otherwise, the obtained avoidance area is empty. Global floating window, modal window, or system window: - This API can be called to obtain the avoidance area only after [setSystemAvoidAreaEnabled](#setSystemAvoidAreaEnabled) is called. Otherwise, the obtained avoidance area is empty. This API is generally applicable to the following scenarios: - In the [onWindowStageCreate()](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#onWindowStageCreate) callback, this API is used to obtain the initial layout avoid area when the application starts. - This API is used when a child window needs to temporarily display content and requires layout adjustments to avoid certain areas.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-getWindowAvoidArea(type: AvoidAreaType): AvoidArea--><!--Device-Window-getWindowAvoidArea(type: AvoidAreaType): AvoidArea-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [AvoidAreaType](arkts-arkui-window-avoidareatype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AvoidArea](arkts-arkui-window-avoidarea-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## getWindowAvoidAreaIgnoringVisibility

```TypeScript
getWindowAvoidAreaIgnoringVisibility(type: AvoidAreaType): AvoidArea
```

Obtains the avoid area of this application window, even if the avoid area is invisible. Main window/Child window: - When the main window is in the free-floating window mode under a non- [freeform window](../../../windowmanager/window-terminology.md#freeform-window) state (the window mode is **window.WindowStatusType.FLOATING**), only the avoidance area of the system bar type ( [AvoidAreaType](arkts-arkui-window-avoidareatype-e.md#AvoidAreaType) is **TYPE_SYSTEM**) is available. - In other scenarios, this API can be called to obtain the calculated avoidance area only when the main window is not in the free-floating window mode or the device type is phone or tablet. Otherwise, the obtained avoidance area is empty. - For the child window in the non-freeform window state or non-free-floating window mode, this API can be called to obtain the calculated avoidance area only when the position and size of the child window are the same as those of the main window. Otherwise, the obtained avoidance area is empty. Global floating window, modal window, or system window: - This API can be called to obtain the avoidance area only after [setSystemAvoidAreaEnabled](#setSystemAvoidAreaEnabled) is called. Otherwise, the obtained avoidance area is empty.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-getWindowAvoidAreaIgnoringVisibility(type: AvoidAreaType): AvoidArea--><!--Device-Window-getWindowAvoidAreaIgnoringVisibility(type: AvoidAreaType): AvoidArea-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [AvoidAreaType](arkts-arkui-window-avoidareatype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AvoidArea](arkts-arkui-window-avoidarea-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |

## getWindowColorSpace

```TypeScript
getWindowColorSpace(): ColorSpace
```

Obtains the color space of this window.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-getWindowColorSpace(): ColorSpace--><!--Device-Window-getWindowColorSpace(): ColorSpace-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorSpace](arkts-arkui-window-colorspace-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## getWindowCornerRadius

```TypeScript
getWindowCornerRadius(): number
```

Obtains the radius of rounded corners of a child window or floating window. If [setWindowCornerRadius()](#setWindowCornerRadius) is not called to set the radius of rounded corners, this API returns the default radius of rounded corners.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-getWindowCornerRadius(): double--><!--Device-Window-getWindowCornerRadius(): double-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## getWindowDecorHeight

```TypeScript
getWindowDecorHeight(): number
```

Obtains the height of the title bar of this window. This API takes effect for the window that has a title bar and a three-button area. In the stage model, this API must be used after the call of [loadContent](#loadContent) or [setUIContent()](#setUIContent) takes effect.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-getWindowDecorHeight(): int--><!--Device-Window-getWindowDecorHeight(): int-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## getWindowDecorVisible

```TypeScript
getWindowDecorVisible(): boolean
```

Checks whether the title bar of this window is visible. In the stage model, this API must be used after the call of [loadContent](#loadContent) or [setUIContent()](#setUIContent) takes effect.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-getWindowDecorVisible(): boolean--><!--Device-Window-getWindowDecorVisible(): boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## getWindowDensityInfo

```TypeScript
getWindowDensityInfo(): WindowDensityInfo
```

Obtains the display density information of this window.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-getWindowDensityInfo(): WindowDensityInfo--><!--Device-Window-getWindowDensityInfo(): WindowDensityInfo-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WindowDensityInfo](arkts-arkui-window-windowdensityinfo-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## getWindowLimits

```TypeScript
getWindowLimits(): WindowLimits
```

Obtains the size limits of this application window, in px.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-getWindowLimits(): WindowLimits--><!--Device-Window-getWindowLimits(): WindowLimits-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WindowLimits](arkts-arkui-window-windowlimits-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## getWindowLimitsVP

```TypeScript
getWindowLimitsVP(): WindowLimits
```

Obtains the size limits of this application window, in vp. For system windows and global floating windows, the default minimum width and height are set to 1 px. The 1 vp value obtained via this API represents the result after rounding calculations.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-getWindowLimitsVP(): WindowLimits--><!--Device-Window-getWindowLimitsVP(): WindowLimits-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WindowLimits](arkts-arkui-window-windowlimits-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## getWindowProperties

```TypeScript
getWindowProperties(): WindowProperties
```

Obtains the properties of this window.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-getWindowProperties(): WindowProperties--><!--Device-Window-getWindowProperties(): WindowProperties-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WindowProperties](arkts-arkui-window-windowproperties-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## getWindowStateSnapshot

```TypeScript
getWindowStateSnapshot(): Promise<string>
```

Get window state snapshot, including isPcMode information.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-getWindowStateSnapshot(): Promise<string>--><!--Device-Window-getWindowStateSnapshot(): Promise<string>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## getWindowStatus

```TypeScript
getWindowStatus(): WindowStatusType
```

Obtains the mode of this window. > **NOTE：**> > In [freeform window](../../../windowmanager/window-terminology.md#freeform-window) mode, when the window is > maximized (covering the entire screen, with a dock bar and status bar on 2-in-1 devices, and a status bar on > tablets), the return value differs based on the > [targetAPIVersion](../../../quick-start/app-configuration-file.md#tags-in-the-configuration-file) setting. For > versions below 14, the return value is **WindowStatusType::FULL_SCREEN**. For versions 14 and above, the return > value is **WindowStatusType::MAXIMIZE**.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-getWindowStatus(): WindowStatusType--><!--Device-Window-getWindowStatus(): WindowStatusType-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WindowStatusType](../arkts-components/arkts-arkui-windowstatustype-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## getWindowSystemBarProperties

```TypeScript
getWindowSystemBarProperties(): SystemBarProperties
```

Obtains the properties of the &lt;!--Del--&gt;three-button navigation bar and &lt;!--DelEnd--&gt;status bar in the main window.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-getWindowSystemBarProperties(): SystemBarProperties--><!--Device-Window-getWindowSystemBarProperties(): SystemBarProperties-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SystemBarProperties](arkts-arkui-window-systembarproperties-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## getWindowTransitionAnimation

```TypeScript
getWindowTransitionAnimation(transitionType: WindowTransitionType): TransitionAnimation | undefined
```

Obtains the window transition animation configuration in a specific scenario. Currently, this API can be used only on the main window of an application.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-getWindowTransitionAnimation(transitionType: WindowTransitionType): TransitionAnimation | undefined--><!--Device-Window-getWindowTransitionAnimation(transitionType: WindowTransitionType): TransitionAnimation | undefined-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| transitionType | [WindowTransitionType](arkts-arkui-window-windowtransitiontype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TransitionAnimation](arkts-arkui-window-transitionanimation-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## globalDisplayToClient

```TypeScript
globalDisplayToClient(globalDisplayX: number, globalDisplayY: number): Position
```

Converts global coordinates (based on the top-left corner of the primary screen) into relative coordinates (based on the top-left corner of the current window). This API is not supported in windows that are subject to display scaling, such as floating windows on phones or tablets not in free windows mode.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-globalDisplayToClient(globalDisplayX: int, globalDisplayY: int): Position--><!--Device-Window-globalDisplayToClient(globalDisplayX: int, globalDisplayY: int): Position-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| globalDisplayX | number | Yes |
| globalDisplayY | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Position](arkts-arkui-display-position-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
| [1300010](../errorcode-window.md#1300010-unsupported-operation-in-the-current-window-mode) |

## isFloatNavigationAvoidAreaEnabled

```TypeScript
isFloatNavigationAvoidAreaEnabled(): boolean
```

Get whether the float navigation avoid area can be obtained.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Window-isFloatNavigationAvoidAreaEnabled(): boolean--><!--Device-Window-isFloatNavigationAvoidAreaEnabled(): boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## isFocused

```TypeScript
isFocused(): boolean
```

Checks whether this window is focused.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-isFocused(): boolean--><!--Device-Window-isFocused(): boolean-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## isGestureBackEnabled

```TypeScript
isGestureBackEnabled(): boolean
```

Obtains whether the back gesture is enabled for the current window. This API can be successfully called only for the main window, and error code 1300004 is returned on other windows.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-isGestureBackEnabled(): boolean--><!--Device-Window-isGestureBackEnabled(): boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## isImmersiveLayout

```TypeScript
isImmersiveLayout(): boolean
```

Checks whether this window is in immersive mode.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-isImmersiveLayout(): boolean--><!--Device-Window-isImmersiveLayout(): boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## isInFreeWindowMode

```TypeScript
isInFreeWindowMode(): boolean
```

Checks whether this window is in [freeform window](../../../windowmanager/window-terminology.md#freeform-window) mode.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-isInFreeWindowMode(): boolean--><!--Device-Window-isInFreeWindowMode(): boolean-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## isInWindowPostureMode

```TypeScript
isInWindowPostureMode(mode: WindowPostureMode): boolean
```

Checks whether this window is in the specified window posture mode.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Window-isInWindowPostureMode(mode: WindowPostureMode): boolean--><!--Device-Window-isInWindowPostureMode(mode: WindowPostureMode): boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [WindowPostureMode](arkts-arkui-window-windowposturemode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |

## isReceiveDragEventEnabled

```TypeScript
isReceiveDragEventEnabled(): boolean
```

Obtains whether the current window can receive [drag events](../arkts-components/arkts-arkui-dragevent-i.md#DragEvent).

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Window-isReceiveDragEventEnabled(): boolean--><!--Device-Window-isReceiveDragEventEnabled(): boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## isSeparationTouchEnabled

```TypeScript
isSeparationTouchEnabled(): boolean
```

Obtains whether the current window supports the event separation state.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Window-isSeparationTouchEnabled(): boolean--><!--Device-Window-isSeparationTouchEnabled(): boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## isShowing

```TypeScript
isShowing(callback: AsyncCallback<boolean>): void
```

Checks whether this window is displayed. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [isWindowShowing](#isWindowShowing)

<!--Device-Window-isShowing(callback: AsyncCallback<boolean>): void--><!--Device-Window-isShowing(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## isShowing

```TypeScript
isShowing(): Promise<boolean>
```

Checks whether this window is displayed. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [isWindowShowing](#isWindowShowing)

<!--Device-Window-isShowing(): Promise<boolean>--><!--Device-Window-isShowing(): Promise<boolean>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## isSupportWideGamut

```TypeScript
isSupportWideGamut(): Promise<boolean>
```

Checks whether this window supports the wide-gamut color space. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isWindowSupportWideGamut](#isWindowSupportWideGamut)()

<!--Device-Window-isSupportWideGamut(): Promise<boolean>--><!--Device-Window-isSupportWideGamut(): Promise<boolean>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## isSupportWideGamut

```TypeScript
isSupportWideGamut(callback: AsyncCallback<boolean>): void
```

Checks whether this window supports the wide-gamut color space. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isWindowSupportWideGamut](#isWindowSupportWideGamut)(callback: AsyncCallback&lt;boolean&gt;)

<!--Device-Window-isSupportWideGamut(callback: AsyncCallback<boolean>): void--><!--Device-Window-isSupportWideGamut(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## isSystemAvoidAreaEnabled

```TypeScript
isSystemAvoidAreaEnabled(): boolean
```

Checks whether a floating window, modal window, or system window (**WindowType** is a system window) is enabled to access the [avoid area](arkts-arkui-window-avoidarea-i.md#AvoidArea).

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-isSystemAvoidAreaEnabled(): boolean--><!--Device-Window-isSystemAvoidAreaEnabled(): boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## isWindowHighlighted

```TypeScript
isWindowHighlighted(): boolean
```

Checks whether the window is active. To obtain the active state, call this API when the [WindowEventType](arkts-arkui-window-windoweventtype-e.md#WindowEventType) lifecycle is **WINDOW_ACTIVE**. You can use [on('windowHighlightChange')](#on_rotationChange) to listen for status changes and then execute the corresponding service.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-isWindowHighlighted(): boolean--><!--Device-Window-isWindowHighlighted(): boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## isWindowShowing

```TypeScript
isWindowShowing(): boolean
```

Checks whether this window is displayed.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-isWindowShowing(): boolean--><!--Device-Window-isWindowShowing(): boolean-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## isWindowSupportWideGamut

```TypeScript
isWindowSupportWideGamut(): Promise<boolean>
```

Checks whether this window supports the wide-gamut color space. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-isWindowSupportWideGamut(): Promise<boolean>--><!--Device-Window-isWindowSupportWideGamut(): Promise<boolean>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## isWindowSupportWideGamut

```TypeScript
isWindowSupportWideGamut(callback: AsyncCallback<boolean>): void
```

Checks whether this window supports the wide-gamut color space. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-isWindowSupportWideGamut(callback: AsyncCallback<boolean>): void--><!--Device-Window-isWindowSupportWideGamut(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## keepKeyboardOnFocus

```TypeScript
keepKeyboardOnFocus(keepKeyboardFlag: boolean): void
```

Determines whether to retain the soft keyboard created by another window when the current window gains focus. This API is only supported by system windows and application child windows.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-keepKeyboardOnFocus(keepKeyboardFlag: boolean): void--><!--Device-Window-keepKeyboardOnFocus(keepKeyboardFlag: boolean): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keepKeyboardFlag | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## loadContent

```TypeScript
loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void
```

Loads the content of a page, with its path in the current project specified, to this window, and transfers the state attribute to the page through a local storage. This API uses an asynchronous callback to return the result. You are advised to call this API during UIAbility startup. If called repeatedly, this API will destroy the existing page content (UIContent) before loading the new content. Exercise caution when using it. The execution context of the current UI may be unclear. Therefore, you are advised not to perform UI-related operations within the callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void--><!--Device-Window-loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| storage | [LocalStorage](arkts-arkui-localstorage-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## loadContent

```TypeScript
loadContent(path: string, storage: LocalStorage): Promise<void>
```

Loads the content of a page, with its path in the current project specified, to this window, and transfers the state attribute to the page through a local storage. This API uses a promise to return the result. You are advised to call this API during UIAbility startup. If called repeatedly, this API will destroy the existing page content (UIContent) before loading the new content. Exercise caution when using it. The execution context of the current UI may be unclear. Therefore, you are advised not to perform UI-related operations within the callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-loadContent(path: string, storage: LocalStorage): Promise<void>--><!--Device-Window-loadContent(path: string, storage: LocalStorage): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| storage | [LocalStorage](arkts-arkui-localstorage-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## loadContent

```TypeScript
loadContent(path: string, callback: AsyncCallback<void>): void
```

Loads content from a page to this window. This API uses an asynchronous callback to return the result. You are advised to call this API during UIAbility startup. If called multiple times, this API will destroy the existing page content (UIContent) before loading the new content. Exercise caution when using it. The execution context of the current UI may be unclear. Therefore, you are advised not to perform UI-related operations within the callback.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setUIContent](#setUIContent)(path: string, callback: AsyncCallback&lt;void&gt;)

<!--Device-Window-loadContent(path: string, callback: AsyncCallback<void>): void--><!--Device-Window-loadContent(path: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## loadContent

```TypeScript
loadContent(path: string): Promise<void>
```

Loads content from a page to this window. This API uses a promise to return the result. You are advised to call this API during UIAbility startup. If called multiple times, this API will destroy the existing page content ( UIContent) before loading the new content. Exercise caution when using it. The execution context of the current UI may be unclear. Therefore, you are advised not to perform UI-related operations within the callback.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setUIContent](#setUIContent)(path: string)

<!--Device-Window-loadContent(path: string): Promise<void>--><!--Device-Window-loadContent(path: string): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## loadContentByName

```TypeScript
loadContentByName(name: string, storage: LocalStorage, callback: AsyncCallback<void>): void
```

Loads the content of a [named route](../../../ui/arkts-routing.md#named-route) page to this window, and transfers the state attribute to the page through a local storage. This API uses an asynchronous callback to return the result. You are advised to call this API during UIAbility startup. If called repeatedly, this API will destroy the existing page content (UIContent) before loading the new content. Exercise caution when using it. The execution context of the current UI may be unclear. Therefore, you are advised not to perform UI-related operations within the callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-loadContentByName(name: string, storage: LocalStorage, callback: AsyncCallback<void>): void--><!--Device-Window-loadContentByName(name: string, storage: LocalStorage, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| storage | [LocalStorage](arkts-arkui-localstorage-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## loadContentByName

```TypeScript
loadContentByName(name: string, callback: AsyncCallback<void>): void
```

Loads the content of a [named route](../../../ui/arkts-routing.md#named-route) page to this window. This API uses an asynchronous callback to return the result. You are advised to call this API during UIAbility startup. If called repeatedly, this API will destroy the existing page content (UIContent) before loading the new content. Exercise caution when using it. The execution context of the current UI may be unclear. Therefore, you are advised not to perform UI-related operations within the callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-loadContentByName(name: string, callback: AsyncCallback<void>): void--><!--Device-Window-loadContentByName(name: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## loadContentByName

```TypeScript
loadContentByName(name: string, storage?: LocalStorage): Promise<void>
```

Loads the content of a [named route](../../../ui/arkts-routing.md#named-route) page to this window, and transfers the state attribute to the page through a local storage. This API uses a promise to return the result. You are advised to call this API during UIAbility startup. If called repeatedly, this API will destroy the existing page content (UIContent) before loading the new content. Exercise caution when using it. The execution context of the current UI may be unclear. Therefore, you are advised not to perform UI-related operations within the callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-loadContentByName(name: string, storage?: LocalStorage): Promise<void>--><!--Device-Window-loadContentByName(name: string, storage?: LocalStorage): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| storage | [LocalStorage](arkts-arkui-localstorage-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## maximize

```TypeScript
maximize(presentation?: MaximizePresentation): Promise<void>
```

Maximizes the window. The main window can use this API to maximize. For child windows, you need to set **maximizeSupported** to **true** when creating the windows and then call this API to maximize. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-maximize(presentation?: MaximizePresentation): Promise<void>--><!--Device-Window-maximize(presentation?: MaximizePresentation): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| presentation | [MaximizePresentation](arkts-arkui-window-maximizepresentation-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## maximize

```TypeScript
maximize(presentation?: MaximizePresentation, acrossDisplay?: boolean): Promise<void>
```

Maximizes the window. The main window can use this API to maximize. For child windows, you need to set **maximizeSupported** to **true** when creating the windows and then call this API to maximize. On 2-in-1 devices with folding capabilities, you can use the **acrossDisplay** parameter to control the main window's behavior in waterfall mode when maximized in the hover state. (See [Semi-Folded State of Foldable Screens](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-folded-hover) ). This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-maximize(presentation?: MaximizePresentation, acrossDisplay?: boolean): Promise<void>--><!--Device-Window-maximize(presentation?: MaximizePresentation, acrossDisplay?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| presentation | [MaximizePresentation](arkts-arkui-window-maximizepresentation-e.md) | No |
| acrossDisplay | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## maximizeWithOptions

```TypeScript
maximizeWithOptions(maximizeOptions?: MaximizeOptions): Promise<void>
```

Maximize the app window.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Window-maximizeWithOptions(maximizeOptions?: MaximizeOptions): Promise<void>--><!--Device-Window-maximizeWithOptions(maximizeOptions?: MaximizeOptions): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| maximizeOptions | [MaximizeOptions](arkts-arkui-window-maximizeoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## minimize

```TypeScript
minimize(callback: AsyncCallback<void>): void
```

The behavior of this API varies based on the caller: - Minimizes the main window if the caller is the main window. The main window can be restored in the dock bar. For 2-in-1 devices, it can be restored by calling [restore()](#restore). - Hides the child window or global floating window if the caller is a child window. The child window or floating window cannot be restored in the dock bar. It can be made visible again by calling [showWindow()](#showWindow). This API can be called only by the main window, child window, or global floating window. If it is called by other windows, error code 1300002 is thrown. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-minimize(callback: AsyncCallback<void>): void--><!--Device-Window-minimize(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## minimize

```TypeScript
minimize(): Promise<void>
```

The behavior of this API varies based on the caller: - Minimizes the main window if the caller is the main window. The main window can be restored in the dock bar. For 2-in-1 devices, it can be restored by calling [restore()](#restore). - Hides the child window or global floating window if the caller is a child window. The child window or floating window cannot be restored in the dock bar. It can be made visible again by calling [showWindow()](#showWindow). This API can be called only by the main window, child window, or global floating window. If it is called by other windows, error code 1300002 is thrown. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-minimize(): Promise<void>--><!--Device-Window-minimize(): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## moveTo

```TypeScript
moveTo(x: number, y: number): Promise<void>
```

Moves this window. This API uses a promise to return the result. This operation is not supported in a window in full-screen mode.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [moveWindowTo](#moveWindowTo)(x: int, y: int)

<!--Device-Window-moveTo(x: number, y: number): Promise<void>--><!--Device-Window-moveTo(x: number, y: number): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## moveTo

```TypeScript
moveTo(x: number, y: number, callback: AsyncCallback<void>): void
```

Moves this window. This API uses an asynchronous callback to return the result. This operation is not supported in a window in full-screen mode.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [moveWindowTo](#moveWindowTo)(x: int, y: int, callback: AsyncCallback&lt;void&gt;)

<!--Device-Window-moveTo(x: number, y: number, callback: AsyncCallback<void>): void--><!--Device-Window-moveTo(x: number, y: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## moveWindowTo

```TypeScript
moveWindowTo(x: number, y: number): Promise<void>
```

Moves this window. This API uses a promise to return the result. A value is returned once the API is called successfully. However, the final effect cannot be obtained immediately from the return value. To obtain the final effect immediately, call [moveWindowToAsync()](#moveWindowToAsync). > **NOTE：**> > - This API is best suited for the floating window mode (when the window mode is > **window.WindowStatusType.FLOATING**, which you can check using > [getWindowStatus()](#getWindowStatus)). You are not advised to use it in other window modes. > > - In [freeform window](../../../windowmanager/window-terminology.md#freeform-window) mode, the window moves > relative to the upper-left corner of the screen. In non-freeform window mode, the window moves relative to > the upper-left corner of its parent window. > > - To move the window relative to the top-left corner of the screen while in non-freeform window mode, call > [moveWindowToGlobal()](#moveWindowToGlobal) > . > > - This API does not work for the main window in non-freeform window mode. > > - In [freeform window](../../../windowmanager/window-terminology.md#freeform-window) mode, > if the title bar of the main window or a child window is moved out of the screen's visible area, > the system will automatically snap the window back to ensure the title bar is visible.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-moveWindowTo(x: int, y: int): Promise<void>--><!--Device-Window-moveWindowTo(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

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
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## moveWindowTo

```TypeScript
moveWindowTo(x: number, y: number, callback: AsyncCallback<void>): void
```

Moves this window. This API uses an asynchronous callback to return the result. A value is returned once the API is called successfully. However, the final effect cannot be obtained immediately from the return value. To obtain the final effect immediately, call [moveWindowToAsync()](#moveWindowToAsync). > **NOTE：**> > - This API is best suited for the floating window mode (when the window mode is > **window.WindowStatusType.FLOATING**, which can obtained using > [getWindowStatus()](#getWindowStatus)). You are advised not to use it in other window modes. > > - In [freeform window](../../../windowmanager/window-terminology.md#freeform-window) mode, the window moves > relative to the upper-left corner of the screen. In non-freeform window mode, the window moves relative to > the upper-left corner of its parent window. > > - To move the window relative to the top-left corner of the screen while in non-freeform window mode, call > [moveWindowToGlobal()](#moveWindowToGlobal) > . > > - This API does not work for the main window in non-freeform window mode. > > - In [freeform window](../../../windowmanager/window-terminology.md#freeform-window) mode, > if the title bar of the main window or a child window is moved out of the screen's visible area, > the system will automatically snap the window back to ensure the title bar is visible.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-moveWindowTo(x: int, y: int, callback: AsyncCallback<void>): void--><!--Device-Window-moveWindowTo(x: int, y: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## moveWindowToAsync

```TypeScript
moveWindowToAsync(x: number, y: number): Promise<void>
```

Moves this window. This API uses a promise to return the result. A value is returned once the call takes effect. You can use [getWindowProperties()](#getWindowProperties) in the callback (see the code snippet below) to obtain the final effect immediately. This API takes effect only when the window is in floating window mode (**window.WindowStatusType.FLOATING**). In other window modes, this API returns error code 1300010. (The window mode can be obtained through [getWindowStatus()](#getWindowStatus)). In floating window mode, the movement behavior of different types of windows is as follows. > **NOTE：**> > - In [freeform window](../../../windowmanager/window-terminology.md#freeform-window) mode, > if the title bar of the main window or a child window is moved out of the screen's visible area, > the system will automatically snap the window back to ensure the title bar is visible.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-moveWindowToAsync(x: int, y: int): Promise<void>--><!--Device-Window-moveWindowToAsync(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

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
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300010](../errorcode-window.md#1300010-unsupported-operation-in-the-current-window-mode) |

## moveWindowToAsync

```TypeScript
moveWindowToAsync(x: number, y: number, moveConfiguration?: MoveConfiguration): Promise<void>
```

Moves this window to the specified position. This API uses a promise to return the result. You can use the **moveConfiguration** parameter to specify the target display ID for the window movement. A value is returned once the call takes effect. You can use [getWindowProperties()](#getWindowProperties) in the callback (see the code snippet below) to obtain the final effect immediately. This API takes effect only when the window is in floating window mode (**window.WindowStatusType.FLOATING**). In other window modes, this API returns error code 1300010. (The window mode can be obtained through [getWindowStatus()](#getWindowStatus)). In floating window mode, the movement behavior of different types of windows is as follows. | Window Type| [Freeform Window](../../../windowmanager/window-terminology.md#freeform-window) State| Non-freeform Window State| |---------|---------------|-----------------| | Main window| Move relative to the screen.| API calls do not take effect or return an error.| | App subwindow/Modal window| Move relative to the screen.| Move relative to the main window.| | System window/Global floating window| Move relative to the screen.| Move relative to the screen.| > **NOTE：**> > - In [freeform window](../../../windowmanager/window-terminology.md#freeform-window) mode, > if the title bar of the main window or a child window is moved out of the screen's visible area, > the system will automatically snap the window back to ensure the title bar is visible.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-moveWindowToAsync(x: int, y: int, moveConfiguration?: MoveConfiguration): Promise<void>--><!--Device-Window-moveWindowToAsync(x: int, y: int, moveConfiguration?: MoveConfiguration): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| moveConfiguration | [MoveConfiguration](arkts-arkui-window-moveconfiguration-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300010](../errorcode-window.md#1300010-unsupported-operation-in-the-current-window-mode) |

## moveWindowToGlobal

```TypeScript
moveWindowToGlobal(x: number, y: number): Promise<void>
```

Moves this window based on the coordinates. This API uses a promise to return the result. A value is returned once the call takes effect. You can use [getWindowProperties()](#getWindowProperties) in the callback (see the code snippet below) to obtain the final effect immediately. This API takes effect only when the window is in floating window mode (**window.WindowStatusType.FLOATING**). In other window modes, this API returns error code 1300010. (The window mode can be obtained through [getWindowStatus()](#getWindowStatus)). > **NOTE：**> > - When the main window is in floating window mode, this API does not take effect or return an error if called > in non-[freeform window](../../../windowmanager/window-terminology.md#freeform-window) state. > > - In [freeform window](../../../windowmanager/window-terminology.md#freeform-window) mode, > if the title bar of the main window or a child window is moved out of the screen's visible area, > the system will automatically snap the window back to ensure the title bar is visible.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-moveWindowToGlobal(x: int, y: int): Promise<void>--><!--Device-Window-moveWindowToGlobal(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

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
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300010](../errorcode-window.md#1300010-unsupported-operation-in-the-current-window-mode) |

## moveWindowToGlobal

```TypeScript
moveWindowToGlobal(x: number, y: number, moveConfiguration?: MoveConfiguration): Promise<void>
```

Moves this window to the specified position based on the coordinates. This API uses a promise to return the result. You can use the **moveConfiguration** parameter to specify the target display ID for the window movement. A value is returned once the call takes effect. You can use [getWindowProperties()](#getWindowProperties) in the callback (see the code snippet below) to obtain the final effect immediately. This API takes effect only when the window is in floating window mode (**window.WindowStatusType.FLOATING**). In other window modes, this API returns error code 1300010. (The window mode can be obtained through [getWindowStatus()](#getWindowStatus)). > **NOTE：**> > - When the main window is in floating window mode, this API does not take effect or return an error if called > in non-[freeform window](../../../windowmanager/window-terminology.md#freeform-window) state. > > - In [freeform window](../../../windowmanager/window-terminology.md#freeform-window) mode, > if the title bar of the main window or a child window is moved out of the screen's visible area, > the system will automatically snap the window back to ensure the title bar is visible.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-moveWindowToGlobal(x: int, y: int, moveConfiguration?: MoveConfiguration): Promise<void>--><!--Device-Window-moveWindowToGlobal(x: int, y: int, moveConfiguration?: MoveConfiguration): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| moveConfiguration | [MoveConfiguration](arkts-arkui-window-moveconfiguration-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300010](../errorcode-window.md#1300010-unsupported-operation-in-the-current-window-mode) |

## moveWindowToGlobalDisplay

```TypeScript
moveWindowToGlobalDisplay(x: number, y: number): Promise<void>
```

Moves the window based on the [global coordinate system](../../../windowmanager/window-terminology.md#global-coordinate-system). This API uses a promise to return the result asynchronously. This API takes effect only when the window is in floating window mode (**window.WindowStatusType.FLOATING**). In other window modes, this API returns error code 1300010. (The window mode can be obtained through [getWindowStatus()](#getWindowStatus)). > **NOTE：**> > - When the main window is in floating window mode, this API does not take effect or return an error if called > in non-[freeform window](../../../windowmanager/window-terminology.md#freeform-window) state. > > - After a window is moved, if it spans multiple screens, the window will belong to the screen with which it > has the largest overlapping area. > > - In [freeform window](../../../windowmanager/window-terminology.md#freeform-window) mode, > if the title bar of the main window or a child window is moved out of the screen's visible area, > the system will automatically snap the window back to ensure the title bar is visible.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-moveWindowToGlobalDisplay(x: int, y: int): Promise<void>--><!--Device-Window-moveWindowToGlobalDisplay(x: int, y: int): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

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
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
| [1300010](../errorcode-window.md#1300010-unsupported-operation-in-the-current-window-mode) |

## offAvoidAreaChange

```TypeScript
offAvoidAreaChange(callback?: Callback<AvoidAreaOptions>): void
```

Unsubscribes from the event indicating changes to the area where this window cannot be displayed.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offAvoidAreaChange(callback?: Callback<AvoidAreaOptions>): void--><!--Device-Window-offAvoidAreaChange(callback?: Callback<AvoidAreaOptions>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[AvoidAreaOptions](arkts-arkui-window-avoidareaoptions-i.md)&gt; | No |

## offDialogTargetTouch

```TypeScript
offDialogTargetTouch(callback?: Callback<void>): void
```

Unsubscribes from the touch event of the target window in the modal window mode.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offDialogTargetTouch(callback?: Callback<void>): void--><!--Device-Window-offDialogTargetTouch(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | No |

## offDisplayIdChange

```TypeScript
offDisplayIdChange(callback?: Callback<number>): void
```

Unsubscribes from the display change event of this window.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offDisplayIdChange(callback?: Callback<long>): void--><!--Device-Window-offDisplayIdChange(callback?: Callback<long>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## offFrameMetricsMeasured

```TypeScript
offFrameMetricsMeasured(callback?: Callback<FrameMetrics>): void
```

Unsubscribes from events indicating changes in window frame metrics. This API must be used after the call of [loadContent](#loadContent)or [setUIContent()](#setUIContent) takes effect.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offFrameMetricsMeasured(callback?: Callback<FrameMetrics>): void--><!--Device-Window-offFrameMetricsMeasured(callback?: Callback<FrameMetrics>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[FrameMetrics](arkts-arkui-window-framemetrics-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## offFreeWindowModeChange

```TypeScript
offFreeWindowModeChange(callback?: Callback<boolean>): void
```

free window mode change callback off.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-offFreeWindowModeChange(callback?: Callback<boolean>): void--><!--Device-Window-offFreeWindowModeChange(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## offKeyboardDidHide

```TypeScript
offKeyboardDidHide(callback?: Callback<KeyboardInfo>): void
```

Unregister the callback of keyboard did hide

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offKeyboardDidHide(callback?: Callback<KeyboardInfo>): void--><!--Device-Window-offKeyboardDidHide(callback?: Callback<KeyboardInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## offKeyboardDidShow

```TypeScript
offKeyboardDidShow(callback?: Callback<KeyboardInfo>): void
```

Unregister the callback of keyboard did show

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offKeyboardDidShow(callback?: Callback<KeyboardInfo>): void--><!--Device-Window-offKeyboardDidShow(callback?: Callback<KeyboardInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## offKeyboardHeightChange

```TypeScript
offKeyboardHeightChange(callback?: Callback<number>): void
```

Unregister the callback of keyboard height change

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offKeyboardHeightChange(callback?: Callback<int>): void--><!--Device-Window-offKeyboardHeightChange(callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | No |

## offKeyboardWillHide

```TypeScript
offKeyboardWillHide(callback?: Callback<KeyboardInfo>): void
```

Unregister the callback of keyboard will hide

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offKeyboardWillHide(callback?: Callback<KeyboardInfo>): void--><!--Device-Window-offKeyboardWillHide(callback?: Callback<KeyboardInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## offKeyboardWillShow

```TypeScript
offKeyboardWillShow(callback?: Callback<KeyboardInfo>): void
```

Unregister the callback of keyboard will show

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offKeyboardWillShow(callback?: Callback<KeyboardInfo>): void--><!--Device-Window-offKeyboardWillShow(callback?: Callback<KeyboardInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## offNoInteractionDetected

```TypeScript
offNoInteractionDetected(callback?: Callback<void>): void
```

Unsubscribes from non-interaction events in a window within the specified period. Interaction events include physical keyboard input events and screen touch/click events, but not soft keyboard input events.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offNoInteractionDetected(callback?: Callback<void>): void--><!--Device-Window-offNoInteractionDetected(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## offOcclusionStateChanged

```TypeScript
offOcclusionStateChanged(callback?: Callback<OcclusionState>): void
```

Unregister the callback for occlusion state changed.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offOcclusionStateChanged(callback?: Callback<OcclusionState>): void--><!--Device-Window-offOcclusionStateChanged(callback?: Callback<OcclusionState>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[OcclusionState](arkts-arkui-window-occlusionstate-e.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## offRectChangeInGlobalDisplay

```TypeScript
offRectChangeInGlobalDisplay(callback?: Callback<RectChangeOptions>): void
```

Disables the listening event for changes in the window rectangle (window position and size) in the [global coordinate system](../../../windowmanager/window-terminology.md#global-coordinate-system).

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offRectChangeInGlobalDisplay(callback?: Callback<RectChangeOptions>): void--><!--Device-Window-offRectChangeInGlobalDisplay(callback?: Callback<RectChangeOptions>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;RectChangeOptions&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## offRotationChange

```TypeScript
offRotationChange(callback?: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | undefined>):
      void
```

Unregister the callback of rotation change

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offRotationChange(callback?: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | undefined>):      void--><!--Device-Window-offRotationChange(callback?: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | undefined>):      void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [RotationChangeCallback](arkts-arkui-window-rotationchangecallback-t.md)&lt;[RotationChangeInfo](arkts-arkui-window-rotationchangeinfo-i.md), [RotationChangeResult](arkts-arkui-window-rotationchangeresult-i.md) \| undefined & gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## offScreenshot

```TypeScript
offScreenshot(callback?: Callback<void>): void
```

Unsubscribes from the screenshot event.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offScreenshot(callback?: Callback<void>): void--><!--Device-Window-offScreenshot(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | No |

## offScreenshotAppEvent

```TypeScript
offScreenshotAppEvent(callback?: Callback<ScreenshotEventType>): void
```

Unsubscribes from the screenshot event.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offScreenshotAppEvent(callback?: Callback<ScreenshotEventType>): void--><!--Device-Window-offScreenshotAppEvent(callback?: Callback<ScreenshotEventType>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[ScreenshotEventType](arkts-arkui-window-screenshoteventtype-e.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## offSubWindowClose

```TypeScript
offSubWindowClose(callback?: Callback<void>): void
```

Unsubscribes from the event indicating that the child window is closed.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offSubWindowClose(callback?: Callback<void>): void--><!--Device-Window-offSubWindowClose(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## offSystemDensityChange

```TypeScript
offSystemDensityChange(callback?: Callback<number>): void
```

Unsubscribes from the system density change event. In the callback function, you are advised to directly use the return value to convert from virtual pixels (vp) to physical pixels (px). For example, if the return value is **density**, the calculation formula is vp * density = px.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offSystemDensityChange(callback?: Callback<double>): void--><!--Device-Window-offSystemDensityChange(callback?: Callback<double>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## offTouchOutside

```TypeScript
offTouchOutside(callback?: Callback<void>): void
```

Unsubscribes from the touch event outside this window.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offTouchOutside(callback?: Callback<void>): void--><!--Device-Window-offTouchOutside(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | No |

## offUiExtensionSecureLimitChange

```TypeScript
offUiExtensionSecureLimitChange(callback?: Callback<boolean>): void
```

UIExtension in window secure limit change callback off.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offUiExtensionSecureLimitChange(callback?: Callback<boolean>): void--><!--Device-Window-offUiExtensionSecureLimitChange(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## offWindowEvent

```TypeScript
offWindowEvent(callback?: Callback<WindowEventType>): void
```

Unsubscribes from the window lifecycle change event.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offWindowEvent(callback?: Callback<WindowEventType>): void--><!--Device-Window-offWindowEvent(callback?: Callback<WindowEventType>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[WindowEventType](arkts-arkui-window-windoweventtype-e.md)&gt; | No |

## offWindowHighlightChange

```TypeScript
offWindowHighlightChange(callback?: Callback<boolean>): void
```

Unregister the callback of window highlight state change

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offWindowHighlightChange(callback?: Callback<boolean>): void--><!--Device-Window-offWindowHighlightChange(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## offWindowPostureModeChange

```TypeScript
offWindowPostureModeChange(mode: WindowPostureMode, callback?: Callback<boolean>): void
```

Unregisters a callback that is invoked when he window changes to the specified window posture mode.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Window-offWindowPostureModeChange(mode: WindowPostureMode, callback?: Callback<boolean>): void--><!--Device-Window-offWindowPostureModeChange(mode: WindowPostureMode, callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [WindowPostureMode](arkts-arkui-window-windowposturemode-e.md) | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |

## offWindowRectChange

```TypeScript
offWindowRectChange(callback?: Callback<RectChangeOptions>): void
```

Unsubscribes from window rectangle (position and size) change events.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offWindowRectChange(callback?: Callback<RectChangeOptions>): void--><!--Device-Window-offWindowRectChange(callback?: Callback<RectChangeOptions>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;RectChangeOptions&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## offWindowSizeChange

```TypeScript
offWindowSizeChange(callback?: Callback<Size>): void
```

Unsubscribes from the window size change event. This API can be called only by the main thread.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offWindowSizeChange(callback?: Callback<Size>): void--><!--Device-Window-offWindowSizeChange(callback?: Callback<Size>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;Size&gt; | No |

## offWindowStatusChange

```TypeScript
offWindowStatusChange(callback?: Callback<WindowStatusType>): void
```

Disables the listening for window status changes.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offWindowStatusChange(callback?: Callback<WindowStatusType>): void--><!--Device-Window-offWindowStatusChange(callback?: Callback<WindowStatusType>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;WindowStatusType&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## offWindowStatusDidChange

```TypeScript
offWindowStatusDidChange(callback?: Callback<WindowStatusType>): void
```

Unsubscribes from the event indicating that the window status has changed.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offWindowStatusDidChange(callback?: Callback<WindowStatusType>): void--><!--Device-Window-offWindowStatusDidChange(callback?: Callback<WindowStatusType>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;WindowStatusType&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## offWindowTitleButtonRectChange

```TypeScript
offWindowTitleButtonRectChange(callback?: Callback<TitleButtonRect>): void
```

Unsubscribes from the change event of the rectangle that holds the minimize, maximize, and close buttons on the title bar of the window.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offWindowTitleButtonRectChange(callback?: Callback<TitleButtonRect>): void--><!--Device-Window-offWindowTitleButtonRectChange(callback?: Callback<TitleButtonRect>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[TitleButtonRect](arkts-arkui-window-titlebuttonrect-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## offWindowVisibilityChange

```TypeScript
offWindowVisibilityChange(callback?: Callback<boolean>): void
```

Unsubscribes from the visibility status change event of this window.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offWindowVisibilityChange(callback?: Callback<boolean>): void--><!--Device-Window-offWindowVisibilityChange(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## offWindowWillClose

```TypeScript
offWindowWillClose(callback?: Callback<void, Promise<boolean>>): void
```

Unsubscribes from the event indicating that the main window or child window will be closed.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-offWindowWillClose(callback?: Callback<void, Promise<boolean>>): void--><!--Device-Window-offWindowWillClose(callback?: Callback<void, Promise<boolean>>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void, Promise&lt;boolean&gt;&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## off_avoidAreaChange

```TypeScript
off(type: 'avoidAreaChange', callback?: Callback<AvoidAreaOptions>): void
```

Unsubscribes from the event indicating changes to the area where this window cannot be displayed.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-off(type: 'avoidAreaChange', callback?: Callback<AvoidAreaOptions>): void--><!--Device-Window-off(type: 'avoidAreaChange', callback?: Callback<AvoidAreaOptions>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'avoidAreaChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[AvoidAreaOptions](arkts-arkui-window-avoidareaoptions-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off_dialogTargetTouch

```TypeScript
off(type: 'dialogTargetTouch', callback?: Callback<void>): void
```

Unsubscribes from the touch event of the target window in the modal window mode.

**Since:** 10

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-off(type: 'dialogTargetTouch', callback?: Callback<void>): void--><!--Device-Window-off(type: 'dialogTargetTouch', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'dialogTargetTouch' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off_displayIdChange

```TypeScript
off(type: 'displayIdChange', callback?: Callback<number>): void
```

Unsubscribes from the display change event of this window.

**Since:** 14

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-Window-off(type: 'displayIdChange', callback?: Callback<long>): void--><!--Device-Window-off(type: 'displayIdChange', callback?: Callback<long>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'displayIdChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## off_frameMetricsMeasured

```TypeScript
off(type: 'frameMetricsMeasured', callback?: Callback<FrameMetrics>): void
```

Unsubscribes from events indicating changes in window frame metrics. This API must be used after the call of [loadContent](#loadContent) or [setUIContent()](#setUIContent) takes effect.

**Since:** 22

**Deprecated since:** -1

<!--Device-Window-off(type: 'frameMetricsMeasured', callback?: Callback<FrameMetrics>): void--><!--Device-Window-off(type: 'frameMetricsMeasured', callback?: Callback<FrameMetrics>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'frameMetricsMeasured' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[FrameMetrics](arkts-arkui-window-framemetrics-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## off_freeWindowModeChange

```TypeScript
off(type: 'freeWindowModeChange', callback?: Callback<boolean>): void
```

Unsubscribes from the freeform window mode change event.

**Since:** 22

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Window-off(type: 'freeWindowModeChange', callback?: Callback<boolean>): void--><!--Device-Window-off(type: 'freeWindowModeChange', callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'freeWindowModeChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## off_keyboardDidHide

```TypeScript
off(type: 'keyboardDidHide', callback?: Callback<KeyboardInfo>): void
```

Unsubscribes from the event indicating that the hide animation of the soft keyboard in the fixed state is completed, For details about the APIs used to transition the input method panel from the fixed state to the floating state, see [Input Method Service](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeFlag).

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Window-off(type: 'keyboardDidHide', callback?: Callback<KeyboardInfo>): void--><!--Device-Window-off(type: 'keyboardDidHide', callback?: Callback<KeyboardInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyboardDidHide' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## off_keyboardDidShow

```TypeScript
off(type: 'keyboardDidShow', callback?: Callback<KeyboardInfo>): void
```

Unsubscribes from the event indicating that the show animation of the soft keyboard in the fixed state is completed, For details about the APIs used to set the input method panel to the fixed or floating state, see [Input Method Service](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeFlag).

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Window-off(type: 'keyboardDidShow', callback?: Callback<KeyboardInfo>): void--><!--Device-Window-off(type: 'keyboardDidShow', callback?: Callback<KeyboardInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyboardDidShow' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## off_keyboardHeightChange

```TypeScript
off(type: 'keyboardHeightChange', callback?: Callback<number>): void
```

Unsubscribes from the event indicating soft keyboard height changes in the fixed state so that the application does not receive notifications of soft keyboard height changes. Starting from API version 10, the soft keyboard can be set to the fixed or floating state. For details, see [Input Method Service](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeFlag).

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-off(type: 'keyboardHeightChange', callback?: Callback<int>): void--><!--Device-Window-off(type: 'keyboardHeightChange', callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyboardHeightChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off_keyboardWillHide

```TypeScript
off(type: 'keyboardWillHide', callback?: Callback<KeyboardInfo>): void
```

Unsubscribes from the event indicating that the soft keyboard in the fixed state is about to hide. For details about the APIs used to transition the input method panel from the fixed state to the floating state, see [Input Method Service](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeFlag).

**Since:** 20

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Window-off(type: 'keyboardWillHide', callback?: Callback<KeyboardInfo>): void--><!--Device-Window-off(type: 'keyboardWillHide', callback?: Callback<KeyboardInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyboardWillHide' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## off_keyboardWillShow

```TypeScript
off(type: 'keyboardWillShow', callback?: Callback<KeyboardInfo>): void
```

Unsubscribes from the event indicating that the soft keyboard in the fixed state is about to show. For details about the APIs used to set the input method panel to the fixed or floating state, see [Input Method Service](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeFlag).

**Since:** 20

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Window-off(type: 'keyboardWillShow', callback?: Callback<KeyboardInfo>): void--><!--Device-Window-off(type: 'keyboardWillShow', callback?: Callback<KeyboardInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyboardWillShow' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## off_noInteractionDetected

```TypeScript
off(type: 'noInteractionDetected', callback?: Callback<void>): void
```

Unsubscribes from non-interaction events in a window within the specified period. Interaction events include physical keyboard input events and screen touch/click events, but not soft keyboard input events.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-off(type: 'noInteractionDetected', callback?: Callback<void>): void--><!--Device-Window-off(type: 'noInteractionDetected', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'noInteractionDetected' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## off_occlusionStateChanged

```TypeScript
off(type: 'occlusionStateChanged', callback?: Callback<OcclusionState>): void
```

Unsubscribes from the visibility status change event of the window.

**Since:** 22

**Deprecated since:** -1

<!--Device-Window-off(type: 'occlusionStateChanged', callback?: Callback<OcclusionState>): void--><!--Device-Window-off(type: 'occlusionStateChanged', callback?: Callback<OcclusionState>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'occlusionStateChanged' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[OcclusionState](arkts-arkui-window-occlusionstate-e.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## off_rectChangeInGlobalDisplay

```TypeScript
off(type: 'rectChangeInGlobalDisplay', callback?: Callback<RectChangeOptions>): void
```

Disables the listening event for changes in the window rectangle (window position and size) in the [global coordinate system](../../../windowmanager/window-terminology.md#global-coordinate-system).

**Since:** 20

**Deprecated since:** -1

<!--Device-Window-off(type: 'rectChangeInGlobalDisplay', callback?: Callback<RectChangeOptions>): void--><!--Device-Window-off(type: 'rectChangeInGlobalDisplay', callback?: Callback<RectChangeOptions>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'rectChangeInGlobalDisplay' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;RectChangeOptions&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## off_rotationChange

```TypeScript
off(type: 'rotationChange', 
       callback?: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void>): void
```

Unsubscribes from the window rotation change event.

**Since:** 19

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Window-off(type: 'rotationChange',        callback?: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void>): void--><!--Device-Window-off(type: 'rotationChange',        callback?: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'rotationChange' | Yes |
| callback | [RotationChangeCallback](arkts-arkui-window-rotationchangecallback-t.md)&lt;[RotationChangeInfo](arkts-arkui-window-rotationchangeinfo-i.md), [RotationChangeResult](arkts-arkui-window-rotationchangeresult-i.md) \| void & gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## off_screenshot

```TypeScript
off(type: 'screenshot', callback?: Callback<void>): void
```

Unsubscribes from the screenshot event.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-off(type: 'screenshot', callback?: Callback<void>): void--><!--Device-Window-off(type: 'screenshot', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'screenshot' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off_screenshotAppEvent

```TypeScript
off(type: 'screenshotAppEvent', callback?: Callback<ScreenshotEventType>): void
```

Unsubscribes from the screenshot event.

**Since:** 20

**Deprecated since:** -1

<!--Device-Window-off(type: 'screenshotAppEvent', callback?: Callback<ScreenshotEventType>): void--><!--Device-Window-off(type: 'screenshotAppEvent', callback?: Callback<ScreenshotEventType>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'screenshotAppEvent' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[ScreenshotEventType](arkts-arkui-window-screenshoteventtype-e.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## off_subWindowClose

```TypeScript
off(type: 'subWindowClose', callback?: Callback<void>): void
```

Unsubscribes from the event indicating that the child window is closed.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-off(type: 'subWindowClose', callback?: Callback<void>): void--><!--Device-Window-off(type: 'subWindowClose', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'subWindowClose' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## off_systemAvoidAreaChange

```TypeScript
off(type: 'systemAvoidAreaChange', callback?: Callback<AvoidArea>): void
```

Unsubscribes from the event indicating changes to the area where this window cannot be displayed.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [off](#off_rotationChange)(type: 'avoidAreaChange', callback?: Callback&lt;AvoidAreaOptions&gt;)

<!--Device-Window-off(type: 'systemAvoidAreaChange', callback?: Callback<AvoidArea>): void--><!--Device-Window-off(type: 'systemAvoidAreaChange', callback?: Callback<AvoidArea>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'systemAvoidAreaChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[AvoidArea](arkts-arkui-window-avoidarea-i.md)&gt; | No |

## off_systemDensityChange

```TypeScript
off(type: 'systemDensityChange', callback?: Callback<number>): void
```

Unsubscribes from the system density change event. In the callback function, you are advised to directly use the return value to convert from virtual pixels (vp) to physical pixels (px). For example, if the return value is **density**, the calculation formula is vp * density = px.

**Since:** 15

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-Window-off(type: 'systemDensityChange', callback?: Callback<double>): void--><!--Device-Window-off(type: 'systemDensityChange', callback?: Callback<double>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'systemDensityChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## off_touchOutside

```TypeScript
off(type: 'touchOutside', callback?: Callback<void>): void
```

Unsubscribes from the touch event outside this window.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-off(type: 'touchOutside', callback?: Callback<void>): void--><!--Device-Window-off(type: 'touchOutside', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'touchOutside' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off_uiExtensionSecureLimitChange

```TypeScript
off(eventType: 'uiExtensionSecureLimitChange', callback?: Callback<boolean>): void
```

Unsubscribes from the event indicating changes in the security restrictions of the UIExtensionAbility within the window.

**Since:** 20

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Window-off(eventType: 'uiExtensionSecureLimitChange', callback?: Callback<boolean>): void--><!--Device-Window-off(eventType: 'uiExtensionSecureLimitChange', callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventType | 'uiExtensionSecureLimitChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## off_windowEvent

```TypeScript
off(type: 'windowEvent', callback?: Callback<WindowEventType>): void
```

Unsubscribes from the window lifecycle change event.

**Since:** 10

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-off(type: 'windowEvent', callback?: Callback<WindowEventType>): void--><!--Device-Window-off(type: 'windowEvent', callback?: Callback<WindowEventType>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'windowEvent' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[WindowEventType](arkts-arkui-window-windoweventtype-e.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off_windowHighlightChange

```TypeScript
off(type: 'windowHighlightChange', callback?: Callback<boolean>): void
```

Unsubscribes from the highlighted state change event of the window.

**Since:** 15

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-Window-off(type: 'windowHighlightChange', callback?: Callback<boolean>): void--><!--Device-Window-off(type: 'windowHighlightChange', callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'windowHighlightChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## off_windowRectChange

```TypeScript
off(type: 'windowRectChange', callback?: Callback<RectChangeOptions>): void
```

Unsubscribes from window rectangle (position and size) change events.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-off(type: 'windowRectChange', callback?: Callback<RectChangeOptions>): void--><!--Device-Window-off(type: 'windowRectChange', callback?: Callback<RectChangeOptions>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'windowRectChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;RectChangeOptions&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## off_windowSizeChange

```TypeScript
off(type: 'windowSizeChange', callback?: Callback<Size>): void
```

Unsubscribes from the window size change event. This API can be called only by the main thread.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-off(type: 'windowSizeChange', callback?: Callback<Size>): void--><!--Device-Window-off(type: 'windowSizeChange', callback?: Callback<Size>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'windowSizeChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;Size&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off_windowStatusChange

```TypeScript
off(type: 'windowStatusChange', callback?: Callback<WindowStatusType>): void
```

Disables the listening for window status changes.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-off(type: 'windowStatusChange', callback?: Callback<WindowStatusType>): void--><!--Device-Window-off(type: 'windowStatusChange', callback?: Callback<WindowStatusType>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'windowStatusChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;WindowStatusType&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## off_windowStatusDidChange

```TypeScript
off(type: 'windowStatusDidChange', callback?: Callback<WindowStatusType>): void
```

Unsubscribes from the event indicating that the window status has changed.

**Since:** 20

**Deprecated since:** -1

<!--Device-Window-off(type: 'windowStatusDidChange', callback?: Callback<WindowStatusType>): void--><!--Device-Window-off(type: 'windowStatusDidChange', callback?: Callback<WindowStatusType>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'windowStatusDidChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;WindowStatusType&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## off_windowTitleButtonRectChange

```TypeScript
off(type: 'windowTitleButtonRectChange', callback?: Callback<TitleButtonRect>): void
```

Unsubscribes from the change event of the rectangle that holds the minimize, maximize, and close buttons on the title bar of the window. This API takes effect for the window that has a title bar or a three-button area. In the stage model, this API must be used after the call of [loadContent](#loadContent) or [setUIContent()](#setUIContent) takes effect.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-off(type: 'windowTitleButtonRectChange', callback?: Callback<TitleButtonRect>): void--><!--Device-Window-off(type: 'windowTitleButtonRectChange', callback?: Callback<TitleButtonRect>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'windowTitleButtonRectChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[TitleButtonRect](arkts-arkui-window-titlebuttonrect-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## off_windowVisibilityChange

```TypeScript
off(type: 'windowVisibilityChange', callback?: Callback<boolean>): void
```

Unsubscribes from the visibility status change event of this window.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-off(type: 'windowVisibilityChange', callback?: Callback<boolean>): void--><!--Device-Window-off(type: 'windowVisibilityChange', callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'windowVisibilityChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## off_windowWillClose

```TypeScript
off(type: 'windowWillClose', callback?: Callback<void, Promise<boolean>>): void
```

Unsubscribes from the event indicating that the main window or child window will be closed.

**Since:** 15

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-Window-off(type: 'windowWillClose', callback?: Callback<void, Promise<boolean>>): void--><!--Device-Window-off(type: 'windowWillClose', callback?: Callback<void, Promise<boolean>>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'windowWillClose' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void, Promise&lt;boolean&gt;&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## onAvoidAreaChange

```TypeScript
onAvoidAreaChange(callback: Callback<AvoidAreaOptions>): void
```

Register the callback of avoidAreaChange

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onAvoidAreaChange(callback: Callback<AvoidAreaOptions>): void--><!--Device-Window-onAvoidAreaChange(callback: Callback<AvoidAreaOptions>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[AvoidAreaOptions](arkts-arkui-window-avoidareaoptions-i.md)&gt; | Yes |

## onDialogTargetTouch

```TypeScript
onDialogTargetTouch(callback: Callback<void>): void
```

Subscribes to click or touch events in a window covered by a modal window. This API takes effect only when it is called by a modal window.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onDialogTargetTouch(callback: Callback<void>): void--><!--Device-Window-onDialogTargetTouch(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | Yes |

## onDisplayIdChange

```TypeScript
onDisplayIdChange(callback: Callback<number>): void
```

Subscribes to the display change event of this window. For example, this event is triggered when the window is moved to a different display.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onDisplayIdChange(callback: Callback<long>): void--><!--Device-Window-onDisplayIdChange(callback: Callback<long>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## onFrameMetricsMeasured

```TypeScript
onFrameMetricsMeasured(callback: Callback<FrameMetrics>): void
```

Subscribes to events indicating changes in window frame metrics. This API must be used after the call of [loadContent](#loadContent) or [setUIContent()](#setUIContent) takes effect. The callback is triggered only when the client UI content is redrawn (for example, during page transitions, interactions with responsive components, setting background colors, or adjusting opacity).

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onFrameMetricsMeasured(callback: Callback<FrameMetrics>): void--><!--Device-Window-onFrameMetricsMeasured(callback: Callback<FrameMetrics>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[FrameMetrics](arkts-arkui-window-framemetrics-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## onFreeWindowModeChange

```TypeScript
onFreeWindowModeChange(callback: Callback<boolean>): void
```

free window mode change callback on.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-onFreeWindowModeChange(callback: Callback<boolean>): void--><!--Device-Window-onFreeWindowModeChange(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## onKeyboardDidHide

```TypeScript
onKeyboardDidHide(callback: Callback<KeyboardInfo>): void
```

Register the callback of keyboard did hide

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onKeyboardDidHide(callback: Callback<KeyboardInfo>): void--><!--Device-Window-onKeyboardDidHide(callback: Callback<KeyboardInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## onKeyboardDidShow

```TypeScript
onKeyboardDidShow(callback: Callback<KeyboardInfo>): void
```

Register the callback of keyboard did show

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onKeyboardDidShow(callback: Callback<KeyboardInfo>): void--><!--Device-Window-onKeyboardDidShow(callback: Callback<KeyboardInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## onKeyboardHeightChange

```TypeScript
onKeyboardHeightChange(callback: Callback<number>): void
```

Register the callback of keyboard height change. This API only takes effect when the soft keyboard is invoked from this window and overlaps with it.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onKeyboardHeightChange(callback: Callback<int>): void--><!--Device-Window-onKeyboardHeightChange(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | Yes |

## onKeyboardWillHide

```TypeScript
onKeyboardWillHide(callback: Callback<KeyboardInfo>): void
```

Register the callback of keyboard will hide

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onKeyboardWillHide(callback: Callback<KeyboardInfo>): void--><!--Device-Window-onKeyboardWillHide(callback: Callback<KeyboardInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## onKeyboardWillShow

```TypeScript
onKeyboardWillShow(callback: Callback<KeyboardInfo>): void
```

Register the callback of keyboard will show

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onKeyboardWillShow(callback: Callback<KeyboardInfo>): void--><!--Device-Window-onKeyboardWillShow(callback: Callback<KeyboardInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## onNoInteractionDetected

```TypeScript
onNoInteractionDetected(timeout: number, callback: Callback<void>): void
```

Subscribes to non-interaction events in a window within the specified period. Interaction events include physical keyboard input events and screen touch/click events, but not soft keyboard input events.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onNoInteractionDetected(timeout: long, callback: Callback<void>): void--><!--Device-Window-onNoInteractionDetected(timeout: long, callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeout | number | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## onOcclusionStateChanged

```TypeScript
onOcclusionStateChanged(callback: Callback<OcclusionState>): void
```

Subscribes to the visibility status change event of the window. The visibility returned by this API may be different from that perceived by human eyes in the following scenarios: - If the shadow area of a non-main window ( [setWindowShadowEnabled](#setWindowShadowEnabled) and [setWindowShadowRadius](#setWindowShadowRadius) can be used to set whether the shadow area is displayed and the shadow radius,respectively) is blocked, the window will be considered as partially visible even though it is completely visible to human eyes. - If the upper-layer window has a transparency effect (including all transparency degrees except the completely opaque degree), the lower-layer window will not be blocked and is visible. - Most windows with animation effects do not block lower-layer windows. For example, when you drag a floating window on a mobile phone, the lower-layer window returned remains visible. - If the shadow area of a non-main window ( [setWindowShadowEnabled](#setWindowShadowEnabled) and [setWindowShadowRadius](#setWindowShadowRadius) can be used to set whether the shadow area is displayed and the shadow radius,respectively) is blocked, the window will be considered as partially visible even though it is completely visible to human eyes. - If the upper-layer window has a transparency effect (including all transparency degrees except the completely opaque degree), the lower-layer window will not be blocked and is visible. - Most windows with animation effects do not block lower-layer windows. For example, when you drag a floating window on a mobile phone, the lower-layer window returned remains visible.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onOcclusionStateChanged(callback: Callback<OcclusionState>): void--><!--Device-Window-onOcclusionStateChanged(callback: Callback<OcclusionState>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[OcclusionState](arkts-arkui-window-occlusionstate-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## onRectChangeInGlobalDisplay

```TypeScript
onRectChangeInGlobalDisplay(callback: Callback<RectChangeOptions>): void
```

Enables the listening event for changes in the window rectangle (window position and size) in the [global coordinate system](../../../windowmanager/window-terminology.md#global-coordinate-system).

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onRectChangeInGlobalDisplay(callback: Callback<RectChangeOptions>): void--><!--Device-Window-onRectChangeInGlobalDisplay(callback: Callback<RectChangeOptions>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;RectChangeOptions&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## onRotationChange

```TypeScript
onRotationChange(callback: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | undefined>): void
```

Register the callback of rotation change

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onRotationChange(callback: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | undefined>): void--><!--Device-Window-onRotationChange(callback: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | undefined>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [RotationChangeCallback](arkts-arkui-window-rotationchangecallback-t.md)&lt;[RotationChangeInfo](arkts-arkui-window-rotationchangeinfo-i.md), [RotationChangeResult](arkts-arkui-window-rotationchangeresult-i.md) \| undefined & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## onScreenshot

```TypeScript
onScreenshot(callback: Callback<void>): void
```

Subscribes to the screenshot event.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onScreenshot(callback: Callback<void>): void--><!--Device-Window-onScreenshot(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | Yes |

## onScreenshotAppEvent

```TypeScript
onScreenshotAppEvent(callback: Callback<ScreenshotEventType>): void
```

Subscribes to the screenshot event.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onScreenshotAppEvent(callback: Callback<ScreenshotEventType>): void--><!--Device-Window-onScreenshotAppEvent(callback: Callback<ScreenshotEventType>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[ScreenshotEventType](arkts-arkui-window-screenshoteventtype-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## onSubWindowClose

```TypeScript
onSubWindowClose(callback: Callback<void>): void
```

Subscribes to the event indicating that the child window is closed. This event is triggered only when the user clicks the system-provided close button in the upper right corner to close the child window. It is not triggered when the child window is closed in other ways.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onSubWindowClose(callback: Callback<void>): void--><!--Device-Window-onSubWindowClose(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## onSystemDensityChange

```TypeScript
onSystemDensityChange(callback: Callback<number>): void
```

Subscribes to the system density change event, which is triggered when the system's display size scale factor changes for the screen where the window is located. In the callback function, you are advised to directly use the return value to convert from virtual pixels (vp) to physical pixels (px). For example, if the return value is **density**, the calculation formula is vp * density = px.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onSystemDensityChange(callback: Callback<double>): void--><!--Device-Window-onSystemDensityChange(callback: Callback<double>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## onTouchOutside

```TypeScript
onTouchOutside(callback: Callback<void>): void
```

Subscribes to the touch event outside this window.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onTouchOutside(callback: Callback<void>): void--><!--Device-Window-onTouchOutside(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | Yes |

## onUiExtensionSecureLimitChange

```TypeScript
onUiExtensionSecureLimitChange(callback: Callback<boolean>): void
```

UIExtension in window secure limit change callback on.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onUiExtensionSecureLimitChange(callback: Callback<boolean>): void--><!--Device-Window-onUiExtensionSecureLimitChange(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## onWindowEvent

```TypeScript
onWindowEvent(callback: Callback<WindowEventType>): void
```

Subscribes to the window lifecycle change event.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onWindowEvent(callback: Callback<WindowEventType>): void--><!--Device-Window-onWindowEvent(callback: Callback<WindowEventType>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[WindowEventType](arkts-arkui-window-windoweventtype-e.md)&gt; | Yes |

## onWindowHighlightChange

```TypeScript
onWindowHighlightChange(callback: Callback<boolean>): void
```

Register the callback of window highlight state change

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onWindowHighlightChange(callback: Callback<boolean>): void--><!--Device-Window-onWindowHighlightChange(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## onWindowPostureModeChange

```TypeScript
onWindowPostureModeChange(mode: WindowPostureMode, callback: Callback<boolean>): void
```

Registers a callback that is invoked when the window changes to the specified window posture mode.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Window-onWindowPostureModeChange(mode: WindowPostureMode, callback: Callback<boolean>): void--><!--Device-Window-onWindowPostureModeChange(mode: WindowPostureMode, callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [WindowPostureMode](arkts-arkui-window-windowposturemode-e.md) | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |

## onWindowRectChange

```TypeScript
onWindowRectChange(callback: Callback<RectChangeOptions>): void
```

Subscribes to window rectangle (position and size) change events.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onWindowRectChange(callback: Callback<RectChangeOptions>): void--><!--Device-Window-onWindowRectChange(callback: Callback<RectChangeOptions>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;RectChangeOptions&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## onWindowSizeChange

```TypeScript
onWindowSizeChange(callback: Callback<Size>): void
```

Subscribes to the window size change event. This API can be called only by the main thread.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onWindowSizeChange(callback: Callback<Size>): void--><!--Device-Window-onWindowSizeChange(callback: Callback<Size>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;Size&gt; | Yes |

## onWindowStatusChange

```TypeScript
onWindowStatusChange(callback: Callback<WindowStatusType>): void
```

Enables the listening for window status changes. When the window status changes, a notification is sent. (In this case, the window attributes may not be updated yet. If you need to obtain the changed window size and position immediately after receiving the window status change notification, you are advised to use [on('windowStatusDidChange')](#on_rotationChange) .) After the listening is enabled using this API, multiple callbacks will be received when the **maximize** or **recover** method is called. To obtain the deduplicated callback, you can use [on('windowStatusDidChange')](#on_rotationChange) . > **NOTE：**> > In [freeform window](../../../windowmanager/window-terminology.md#freeform-window) mode, when the window is > maximized (covering the entire screen, with a dock bar and status bar on 2-in-1 devices, and a status bar on > tablets), the return value differs based on the > [targetAPIVersion](../../../quick-start/app-configuration-file.md#tags-in-the-configuration-file) setting. For > versions below 14, the return value is **WindowStatusType::FULL_SCREEN**. For versions 14 and above, the return > value is **WindowStatusType::MAXIMIZE**.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onWindowStatusChange(callback: Callback<WindowStatusType>): void--><!--Device-Window-onWindowStatusChange(callback: Callback<WindowStatusType>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;WindowStatusType&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## onWindowStatusDidChange

```TypeScript
onWindowStatusDidChange(callback: Callback<WindowStatusType>): void
```

Subscribes to the event indicating that the window status has changed (the [Rect](arkts-arkui-window-rect-i.md#Rect) property of the window has been updated).

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onWindowStatusDidChange(callback: Callback<WindowStatusType>): void--><!--Device-Window-onWindowStatusDidChange(callback: Callback<WindowStatusType>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;WindowStatusType&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## onWindowTitleButtonRectChange

```TypeScript
onWindowTitleButtonRectChange(callback: Callback<TitleButtonRect>): void
```

Subscribes to the change event of the rectangle that holds the minimize, maximize, and close buttons on the title bar of the window.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onWindowTitleButtonRectChange(callback: Callback<TitleButtonRect>): void--><!--Device-Window-onWindowTitleButtonRectChange(callback: Callback<TitleButtonRect>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[TitleButtonRect](arkts-arkui-window-titlebuttonrect-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## onWindowVisibilityChange

```TypeScript
onWindowVisibilityChange(callback: Callback<boolean>): void
```

Subscribes to the visibility status change event of this window. The visibility returned by this API may be different from that perceived by human eyes in the following scenarios: - If the shadow area of a non-main window ( [setWindowShadowEnabled](#setWindowShadowEnabled) and [setWindowShadowRadius](#setWindowShadowRadius) can be used to set whether the shadow area is displayed and the shadow radius,respectively) is blocked, the window will be considered as partially visible even though it is completely visible to human eyes. - If the upper-layer window has a transparency effect (including all transparency degrees except the completely opaque degree), the lower-layer window will not be blocked and is visible. - Most windows with animation effects do not block lower-layer windows. For example, when you drag a floating window on a mobile phone, the lower-layer window returned remains visible.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onWindowVisibilityChange(callback: Callback<boolean>): void--><!--Device-Window-onWindowVisibilityChange(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## onWindowWillClose

```TypeScript
onWindowWillClose(callback: Callback<void, Promise<boolean>>): void
```

Subscribes to the event indicating that the main window or child window will be closed. This event is triggered only when the user clicks the close button in the system-provided title bar to close the window. It is not triggered when the window is closed in other ways.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-onWindowWillClose(callback: Callback<void, Promise<boolean>>): void--><!--Device-Window-onWindowWillClose(callback: Callback<void, Promise<boolean>>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void, Promise&lt;boolean&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## on_avoidAreaChange

```TypeScript
on(type: 'avoidAreaChange', callback: Callback<AvoidAreaOptions>): void
```

Subscribes to the event indicating changes to the area where this window cannot be displayed. Main window/Child window: - When the callback is triggered in the free-floating window mode (the window mode is **window.WindowStatusType.FLOATING**) under the [freeform window](../../../windowmanager/window-terminology.md#freeform-window) state, only the avoidance area of the fixed soft keyboard type ([AvoidAreaType](arkts-arkui-window-avoidareatype-e.md#AvoidAreaType) is **TYPE_KEYBOARD**) is available. - When the callback is triggered in the free-floating window mode of the main window in the non-freeform window state, only the avoidance area of the system bar type ([AvoidAreaType](arkts-arkui-window-avoidareatype-e.md#AvoidAreaType) is **TYPE_SYSTEM**) is available. - When the callback is triggered in the other scenarios of the main window, the calculated avoidance area can be returned only when the window is not in the free-floating window mode or the device type is phone or tablet. Otherwise, an empty avoidance area is returned. - When the callback is triggered for the child window in the non-freeform window state or non-free-floating window mode, the calculated avoidance area of the child window is returned only when the position and size of the child window are the same as those of the main window. Otherwise, an empty avoidance area is returned. Global floating window, modal window, or system window: - The calculated avoidance area is returned only when the callback is triggered after [setSystemAvoidAreaEnabled](#setSystemAvoidAreaEnabled) is called. Otherwise, an empty avoidance area is returned. &lt;!--RP7--&gt;Common scenarios for triggering this event are as follows: transitions between full-screen mode, floating mode, and split-screen mode of the application window; rotation of the application window; transitions between folded and unfolded states of a foldable device; transfer of the application window between multiple devices.&lt;!--RP7End--&gt;

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-on(type: 'avoidAreaChange', callback: Callback<AvoidAreaOptions>): void--><!--Device-Window-on(type: 'avoidAreaChange', callback: Callback<AvoidAreaOptions>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'avoidAreaChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[AvoidAreaOptions](arkts-arkui-window-avoidareaoptions-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on_dialogTargetTouch

```TypeScript
on(type: 'dialogTargetTouch', callback: Callback<void>): void
```

Subscribes to click or touch events in a window covered by a modal window. This API takes effect only when it is called by a modal window.

**Since:** 10

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-on(type: 'dialogTargetTouch', callback: Callback<void>): void--><!--Device-Window-on(type: 'dialogTargetTouch', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'dialogTargetTouch' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on_displayIdChange

```TypeScript
on(type: 'displayIdChange', callback: Callback<number>): void
```

Subscribes to the display change event of this window. For example, this event is triggered when the window is moved to a different display.

**Since:** 14

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-Window-on(type: 'displayIdChange', callback: Callback<long>): void--><!--Device-Window-on(type: 'displayIdChange', callback: Callback<long>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'displayIdChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## on_frameMetricsMeasured

```TypeScript
on(type: 'frameMetricsMeasured', callback: Callback<FrameMetrics>): void
```

Subscribes to events indicating changes in window frame metrics. This API must be used after the call of [loadContent](#loadContent) or [setUIContent()](#setUIContent) takes effect. The callback is triggered only when the client UI content is redrawn (for example, during page transitions, interactions with responsive components, setting background colors, or adjusting opacity).

**Since:** 22

**Deprecated since:** -1

<!--Device-Window-on(type: 'frameMetricsMeasured', callback: Callback<FrameMetrics>): void--><!--Device-Window-on(type: 'frameMetricsMeasured', callback: Callback<FrameMetrics>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'frameMetricsMeasured' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[FrameMetrics](arkts-arkui-window-framemetrics-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## on_freeWindowModeChange

```TypeScript
on(type: 'freeWindowModeChange', callback: Callback<boolean>): void
```

Subscribes to the freeform window mode change event.

**Since:** 22

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Window-on(type: 'freeWindowModeChange', callback: Callback<boolean>): void--><!--Device-Window-on(type: 'freeWindowModeChange', callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'freeWindowModeChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## on_keyboardDidHide

```TypeScript
on(type: 'keyboardDidHide', callback: Callback<KeyboardInfo>): void
```

Subscribes to the event indicating that the hide animation of the soft keyboard in the fixed state is completed, or when the soft keyboard finishes transitioning from the fixed state to the floating state. For details about the APIs used to set the soft keyboard to the fixed or floating state, see [Input Method Service](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeFlag).

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Window-on(type: 'keyboardDidHide', callback: Callback<KeyboardInfo>): void--><!--Device-Window-on(type: 'keyboardDidHide', callback: Callback<KeyboardInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyboardDidHide' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## on_keyboardDidShow

```TypeScript
on(type: 'keyboardDidShow', callback: Callback<KeyboardInfo>): void
```

Subscribes to the event indicating that the show animation of the soft keyboard in the fixed state is completed, or when the soft keyboard finishes transitioning from the floating state to the fixed state. For details about the APIs used to set the soft keyboard to the fixed or floating state, see [Input Method Service](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeFlag).

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Window-on(type: 'keyboardDidShow', callback: Callback<KeyboardInfo>): void--><!--Device-Window-on(type: 'keyboardDidShow', callback: Callback<KeyboardInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyboardDidShow' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## on_keyboardHeightChange

```TypeScript
on(type: 'keyboardHeightChange', callback: Callback<number>): void
```

Subscribes to the event indicating soft keyboard height changes in the fixed state. The system notifies the keyboard height change when the soft keyboard is invoked by the window and overlaps with the window. Starting from API version 10, the soft keyboard can be set to the fixed or floating state. For details, see [Input Method Service](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeFlag).

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-on(type: 'keyboardHeightChange', callback: Callback<int>): void--><!--Device-Window-on(type: 'keyboardHeightChange', callback: Callback<int>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyboardHeightChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on_keyboardWillHide

```TypeScript
on(type: 'keyboardWillHide', callback: Callback<KeyboardInfo>): void
```

Subscribes to the event indicating that the soft keyboard in the fixed state is about to hide, or the soft keyboard is transitioning from the fixed state to the floating state. For details about the APIs used to set the soft keyboard to the fixed or floating state, see [Input Method Service](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeFlag).

**Since:** 20

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Window-on(type: 'keyboardWillHide', callback: Callback<KeyboardInfo>): void--><!--Device-Window-on(type: 'keyboardWillHide', callback: Callback<KeyboardInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyboardWillHide' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## on_keyboardWillShow

```TypeScript
on(type: 'keyboardWillShow', callback: Callback<KeyboardInfo>): void
```

Subscribes to the event indicating that the soft keyboard in the fixed state is about to show, or the soft keyboard is transitioning from the floating state to the fixed state. For details about the APIs used to set the soft keyboard to the fixed or floating state, see [Input Method Service](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-panel-i.md#changeFlag).

**Since:** 20

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Window-on(type: 'keyboardWillShow', callback: Callback<KeyboardInfo>): void--><!--Device-Window-on(type: 'keyboardWillShow', callback: Callback<KeyboardInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyboardWillShow' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[KeyboardInfo](arkts-arkui-window-keyboardinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## on_noInteractionDetected

```TypeScript
on(type: 'noInteractionDetected', timeout: number, callback: Callback<void>): void
```

Register the callback function that has no interaction for a long time. Interaction events include physical keyboard input events and screen touch/click events, but not soft keyboard input events.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-on(type: 'noInteractionDetected', timeout: number, callback: Callback<void>): void--><!--Device-Window-on(type: 'noInteractionDetected', timeout: number, callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'noInteractionDetected' | Yes |
| timeout | number | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## on_occlusionStateChanged

```TypeScript
on(type: 'occlusionStateChanged', callback: Callback<OcclusionState>): void
```

Subscribes to the visibility status change event of the window. The visibility returned by this API may be different from that perceived by human eyes in the following scenarios: - If the shadow area of a non-main window ( [setWindowShadowEnabled](#setWindowShadowEnabled) and [setWindowShadowRadius](#setWindowShadowRadius) can be used to set whether the shadow area is displayed and the shadow radius,respectively) is blocked, the window will be considered as partially visible even though it is completely visible to human eyes. - If the upper-layer window has a transparency effect (including all transparency degrees except the completely opaque degree), the lower-layer window will not be blocked and is visible. - Most windows with animation effects do not block lower-layer windows. For example, when you drag a floating window on a mobile phone, the lower-layer window returned remains visible.

**Since:** 22

**Deprecated since:** -1

<!--Device-Window-on(type: 'occlusionStateChanged', callback: Callback<OcclusionState>): void--><!--Device-Window-on(type: 'occlusionStateChanged', callback: Callback<OcclusionState>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'occlusionStateChanged' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[OcclusionState](arkts-arkui-window-occlusionstate-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## on_rectChangeInGlobalDisplay

```TypeScript
on(type: 'rectChangeInGlobalDisplay', callback: Callback<RectChangeOptions>): void
```

Enables the listening event for changes in the window rectangle (window position and size) in the [global coordinate system](../../../windowmanager/window-terminology.md#global-coordinate-system).

**Since:** 20

**Deprecated since:** -1

<!--Device-Window-on(type: 'rectChangeInGlobalDisplay', callback: Callback<RectChangeOptions>): void--><!--Device-Window-on(type: 'rectChangeInGlobalDisplay', callback: Callback<RectChangeOptions>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'rectChangeInGlobalDisplay' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;RectChangeOptions&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## on_rotationChange

```TypeScript
on(type: 'rotationChange', callback: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void>): void
```

Subscribes to the window rotation change event. If the window rotation event type in [RotationChangeInfo](arkts-arkui-window-rotationchangeinfo-i.md#RotationChangeInfo) is **WINDOW_WILL_ROTATE**, [RotationChangeResult](arkts-arkui-window-rotationchangeresult-i.md#RotationChangeResult) must be returned. If the window rotation event type is **WINDOW_DID_ROTATE**, [RotationChangeResult](arkts-arkui-window-rotationchangeresult-i.md#RotationChangeResult) does not take effect. This API can be registered only on the main thread. If a window registers multiple callbacks of the same type, only the return value of the most recently registered callback will be effective. The system provides a timeout protection mechanism. If the window does not return [RotationChangeResult](arkts-arkui-window-rotationchangeresult-i.md#RotationChangeResult) within 20 ms, the system does not process the return value.

**Since:** 19

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Window-on(type: 'rotationChange', callback: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void>): void--><!--Device-Window-on(type: 'rotationChange', callback: RotationChangeCallback<RotationChangeInfo, RotationChangeResult | void>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'rotationChange' | Yes |
| callback | [RotationChangeCallback](arkts-arkui-window-rotationchangecallback-t.md)&lt;[RotationChangeInfo](arkts-arkui-window-rotationchangeinfo-i.md), [RotationChangeResult](arkts-arkui-window-rotationchangeresult-i.md) \| void & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## on_screenshot

```TypeScript
on(type: 'screenshot', callback: Callback<void>): void
```

Subscribes to the screenshot event.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-on(type: 'screenshot', callback: Callback<void>): void--><!--Device-Window-on(type: 'screenshot', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'screenshot' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on_screenshotAppEvent

```TypeScript
on(type: 'screenshotAppEvent', callback: Callback<ScreenshotEventType>): void
```

Subscribes to the screenshot event.

**Since:** 20

**Deprecated since:** -1

<!--Device-Window-on(type: 'screenshotAppEvent', callback: Callback<ScreenshotEventType>): void--><!--Device-Window-on(type: 'screenshotAppEvent', callback: Callback<ScreenshotEventType>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'screenshotAppEvent' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[ScreenshotEventType](arkts-arkui-window-screenshoteventtype-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## on_subWindowClose

```TypeScript
on(type: 'subWindowClose', callback: Callback<void>): void
```

Subscribes to the event indicating that the child window is closed. This event is triggered only when the user clicks the system-provided close button in the top-right corner to close the child window. It is not triggered when the child window is closed in other ways. If the event is subscribed to multiple times, only the most recently subscribed-to event takes effect. The callback function in this API is executed synchronously. For asynchronous close events of child windows, refer to [on('windowWillClose')](#on_rotationChange) . If there is an existing event subscribed to by calling [on('windowWillClose')](#on_rotationChange) , only the [on('windowWillClose')](#on_rotationChange) API will be responded to.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-on(type: 'subWindowClose', callback: Callback<void>): void--><!--Device-Window-on(type: 'subWindowClose', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'subWindowClose' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## on_systemAvoidAreaChange

```TypeScript
on(type: 'systemAvoidAreaChange', callback: Callback<AvoidArea>): void
```

Subscribes to the event indicating changes to the area where this window cannot be displayed.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [on](#on_rotationChange)(type: 'avoidAreaChange', callback: Callback&lt;AvoidAreaOptions&gt;)

<!--Device-Window-on(type: 'systemAvoidAreaChange', callback: Callback<AvoidArea>): void--><!--Device-Window-on(type: 'systemAvoidAreaChange', callback: Callback<AvoidArea>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'systemAvoidAreaChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[AvoidArea](arkts-arkui-window-avoidarea-i.md)&gt; | Yes |

## on_systemDensityChange

```TypeScript
on(type: 'systemDensityChange', callback: Callback<number>): void
```

Subscribes to the system density change event, which is triggered when the system's display size scale factor changes for the screen where the window is located. In the callback function, you are advised to directly use the return value to convert from virtual pixels (vp) to physical pixels (px). For example, if the return value is **density**, the calculation formula is vp * density = px.

**Since:** 15

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-Window-on(type: 'systemDensityChange', callback: Callback<double>): void--><!--Device-Window-on(type: 'systemDensityChange', callback: Callback<double>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'systemDensityChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## on_touchOutside

```TypeScript
on(type: 'touchOutside', callback: Callback<void>): void
```

Subscribes to the touch event outside this window.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-on(type: 'touchOutside', callback: Callback<void>): void--><!--Device-Window-on(type: 'touchOutside', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'touchOutside' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on_uiExtensionSecureLimitChange

```TypeScript
on(eventType: 'uiExtensionSecureLimitChange', callback: Callback<boolean>): void
```

Subscribes to the event indicating changes in the security restrictions of the UIExtensionAbility within the window. You are advised to initiate the subscription right after the window is created.

**Since:** 20

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Window-on(eventType: 'uiExtensionSecureLimitChange', callback: Callback<boolean>): void--><!--Device-Window-on(eventType: 'uiExtensionSecureLimitChange', callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventType | 'uiExtensionSecureLimitChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## on_windowEvent

```TypeScript
on(type: 'windowEvent', callback: Callback<WindowEventType>): void
```

Subscribes to the window lifecycle change event.

**Since:** 10

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-on(type: 'windowEvent', callback: Callback<WindowEventType>): void--><!--Device-Window-on(type: 'windowEvent', callback: Callback<WindowEventType>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'windowEvent' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[WindowEventType](arkts-arkui-window-windoweventtype-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on_windowHighlightChange

```TypeScript
on(type: 'windowHighlightChange', callback: Callback<boolean>): void
```

Subscribes to the highlighted state change event of the window.

**Since:** 15

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-Window-on(type: 'windowHighlightChange', callback: Callback<boolean>): void--><!--Device-Window-on(type: 'windowHighlightChange', callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'windowHighlightChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## on_windowRectChange

```TypeScript
on(type: 'windowRectChange', callback: Callback<RectChangeOptions>): void
```

Subscribes to window rectangle (position and size) change events.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-on(type: 'windowRectChange', callback: Callback<RectChangeOptions>): void--><!--Device-Window-on(type: 'windowRectChange', callback: Callback<RectChangeOptions>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'windowRectChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;RectChangeOptions&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## on_windowSizeChange

```TypeScript
on(type: 'windowSizeChange', callback: Callback<Size>): void
```

Subscribes to the window size change event. This API can be called only by the main thread.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-on(type: 'windowSizeChange', callback: Callback<Size>): void--><!--Device-Window-on(type: 'windowSizeChange', callback: Callback<Size>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'windowSizeChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;Size&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on_windowStatusChange

```TypeScript
on(type: 'windowStatusChange', callback: Callback<WindowStatusType>): void
```

Enables the listening for window status changes. When the window status changes, a notification is sent. (In this case, the window attributes may not be updated yet. If you need to obtain the changed window size and position immediately after receiving the window status change notification, you are advised to use [on('windowStatusDidChange')](#on_rotationChange) .) After the listening is enabled using this API, multiple callbacks will be received when the **maximize** or **recover** method is called. To obtain the deduplicated callback, you can use [on('windowStatusDidChange')](#on_rotationChange) . > **NOTE：**> > In [freeform window](../../../windowmanager/window-terminology.md#freeform-window) mode, when the window is > maximized (covering the entire screen, with a dock bar and status bar on 2-in-1 devices, and a status bar on > tablets), the return value differs based on the > [targetAPIVersion](../../../quick-start/app-configuration-file.md#tags-in-the-configuration-file) setting. For > versions below 14, the return value is **WindowStatusType::FULL_SCREEN**. For versions 14 and above, the return > value is **WindowStatusType::MAXIMIZE**.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-on(type: 'windowStatusChange', callback: Callback<WindowStatusType>): void--><!--Device-Window-on(type: 'windowStatusChange', callback: Callback<WindowStatusType>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'windowStatusChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;WindowStatusType&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## on_windowStatusDidChange

```TypeScript
on(type: 'windowStatusDidChange', callback: Callback<WindowStatusType>): void
```

Subscribes to the event indicating that the window status has changed (the [Rect](arkts-arkui-window-rect-i.md#Rect) property of the window has been updated).

**Since:** 20

**Deprecated since:** -1

<!--Device-Window-on(type: 'windowStatusDidChange', callback: Callback<WindowStatusType>): void--><!--Device-Window-on(type: 'windowStatusDidChange', callback: Callback<WindowStatusType>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'windowStatusDidChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;WindowStatusType&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## on_windowTitleButtonRectChange

```TypeScript
on(type: 'windowTitleButtonRectChange', callback: Callback<TitleButtonRect>): void
```

Subscribes to the change event of the rectangle that holds the minimize, maximize, and close buttons on the title bar of the window. This API takes effect for the window that has a title bar or a three-button area. In the stage model, this API must be used after the call of [loadContent](#loadContent) or [setUIContent()](#setUIContent) takes effect.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-on(type: 'windowTitleButtonRectChange', callback: Callback<TitleButtonRect>): void--><!--Device-Window-on(type: 'windowTitleButtonRectChange', callback: Callback<TitleButtonRect>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'windowTitleButtonRectChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[TitleButtonRect](arkts-arkui-window-titlebuttonrect-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## on_windowVisibilityChange

```TypeScript
on(type: 'windowVisibilityChange', callback: Callback<boolean>): void
```

Subscribes to the visibility status change event of this window. The visibility returned by this API may be different from that perceived by human eyes in the following scenarios: - If the shadow area of a non-main window ( [setWindowShadowEnabled](#setWindowShadowEnabled) and [setWindowShadowRadius](#setWindowShadowRadius) can be used to set whether the shadow area is displayed and the shadow radius,respectively) is blocked, the window will be considered as partially visible even though it is completely visible to human eyes. - If the upper-layer window has a transparency effect (including all transparency degrees except the completely opaque degree), the lower-layer window will not be blocked and is visible. - Most windows with animation effects do not block lower-layer windows. For example, when you drag a floating window on a mobile phone, the lower-layer window returned remains visible.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-on(type: 'windowVisibilityChange', callback: Callback<boolean>): void--><!--Device-Window-on(type: 'windowVisibilityChange', callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'windowVisibilityChange' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## on_windowWillClose

```TypeScript
on(type: 'windowWillClose', callback: Callback<void, Promise<boolean>>): void
```

Subscribes to the event indicating that the main window or child window will be closed. This event is triggered only when the user clicks the close button in the system-provided title bar to close the window. It is not triggered when the window is closed in other ways. The callback function in this API is executed asynchronously. For synchronous close events of child windows, refer to [on('subWindowClose')](#on_rotationChange). For synchronous close events of the main window, refer to [on('windowStageClose')](#on_rotationChange).

**Since:** 15

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-Window-on(type: 'windowWillClose', callback: Callback<void, Promise<boolean>>): void--><!--Device-Window-on(type: 'windowWillClose', callback: Callback<void, Promise<boolean>>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'windowWillClose' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void, Promise&lt;boolean&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## raiseToAppTop

```TypeScript
raiseToAppTop(): Promise<void>
```

Brings a child window to the top. This action is limited to child windows of the same type under the same parent window within the current application. For child windows with a custom zLevel property, it only applies to child windows with the same zLevel value under the same parent window within the current application. This API uses a promise to return the result. Before calling this API, ensure that the child window has been created and [showWindow()](#showWindow) has been successfully executed.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-raiseToAppTop(): Promise<void>--><!--Device-Window-raiseToAppTop(): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [1300009](../errorcode-window.md#1300009-invalid-parent-window) |

## recover

```TypeScript
recover(): Promise<void>
```

Restores the main window from the full-screen, maximized, or split-screen mode to a floating window ( **window.WindowStatusType.FLOATING** mode), and restores the window size and position to those before the full- screen, maximized, or split-screen mode is entered. If the main window is already in the floating window mode, nothing will happen. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-recover(): Promise<void>--><!--Device-Window-recover(): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300001](../errorcode-window.md#1300001-repeated-operation) |

## recover

```TypeScript
recover(snapshotAnimationConfig: WindowSnapshotAnimationConfig): Promise<void>
```

Restores the main window from full-screen, maximized, or split-screen mode to a floating window, and resets its size and position to their previous values before full-screen, maximized, or split-screen mode was entered.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Window-recover(snapshotAnimationConfig: WindowSnapshotAnimationConfig): Promise<void>--><!--Device-Window-recover(snapshotAnimationConfig: WindowSnapshotAnimationConfig): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [snapshotAnimationConfig](arkts-arkui-window-maximizeoptions-i.md) | [WindowSnapshotAnimationConfig](arkts-arkui-window-windowsnapshotanimationconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300001](../errorcode-window.md#1300001-repeated-operation) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## resetAspectRatio

```TypeScript
resetAspectRatio(callback: AsyncCallback<void>): void
```

Resets the aspect ratio of the window content layout. This API uses an asynchronous callback to return the result. This API is valid only for the main window. After it is called, the persistently saved aspect ratio is cleared.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-resetAspectRatio(callback: AsyncCallback<void>): void--><!--Device-Window-resetAspectRatio(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## resetAspectRatio

```TypeScript
resetAspectRatio(): Promise<void>
```

Resets the aspect ratio of the window content layout. This API uses a promise to return the result. This API is valid only for the main window. After it is called, the persistently saved aspect ratio is cleared.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-resetAspectRatio(): Promise<void>--><!--Device-Window-resetAspectRatio(): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## resetSize

```TypeScript
resetSize(width: number, height: number): Promise<void>
```

Changes the size of this window based on the top-left vertex of the window. This API uses a promise to return the result. The main window and child window have the following default size limits: [320, 1920] in width and [240, 1920] in height, both in units of vp. The minimum width and height of the main window and child window of the application depends on the configuration on the product side. You can call [getWindowLimits](#getWindowLimits) to obtain size limits. The system window has the following size limits: (0, 1920] in width and (0, 1920] in height, both in units of vp. The new window width and height you set must meet the following limits: If the window width or height is less than the minimum width or height limit, then the minimum width or height limit takes effect. If the window width or height is greater than the maximum width or height limit, then the maximum width or height limit takes effect. This operation is not supported in a window in full-screen mode.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [resize](#resize)(width: int, height: int)

<!--Device-Window-resetSize(width: number, height: number): Promise<void>--><!--Device-Window-resetSize(width: number, height: number): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | number | Yes |
| height | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## resetSize

```TypeScript
resetSize(width: number, height: number, callback: AsyncCallback<void>): void
```

Changes the size of this window based on the top-left vertex of the window. This API uses an asynchronous callback to return the result. The main window and child window have the following default size limits: [320, 1920] in width and [240, 1920] in height, both in units of vp. The minimum width and height of the main window and child window of the application depends on the configuration on the product side. You can call [getWindowLimits](#getWindowLimits) to obtain size limits. The system window has the following size limits: (0, 1920] in width and (0, 1920] in height, both in units of vp. The new window width and height you set must meet the following limits: If the window width or height is less than the minimum width or height limit, then the minimum width or height limit takes effect. If the window width or height is greater than the maximum width or height limit, then the maximum width or height limit takes effect. This operation is not supported in a window in full-screen mode.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [resize](#resize)(width: int, height: int, callback: AsyncCallback&lt;void&gt;)

<!--Device-Window-resetSize(width: number, height: number, callback: AsyncCallback<void>): void--><!--Device-Window-resetSize(width: number, height: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | number | Yes |
| height | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## resize

```TypeScript
resize(width: number, height: number): Promise<void>
```

Changes the size of this window based on the top-left vertex of the window. This API uses a promise to return the result. A value is returned once the API is called successfully. However, the final effect cannot be obtained immediately from the return value. To obtain the final effect immediately, call [resizeAsync()](#resizeAsync). The window size is restricted by [WindowLimits](arkts-arkui-window-windowlimits-i.md#WindowLimits). You can call [getWindowLimits](#getWindowLimits) to find out the exact limits. The new window width and height you set must meet the following limits: If the window width or height is less than the minimum width or height limit, then the minimum width or height limit takes effect. However, the system window and global floating window settings are not subject to these minimum width or height restrictions. If the window width or height is greater than the maximum width or height limit, then the maximum width or height limit takes effect. This API takes effect only when the window is in floating window mode (**window.WindowStatusType.FLOATING**). If this API is called when the window is in other window modes, error code 1300002 is reported. (The window mode can be obtained through [getWindowStatus()](#getWindowStatus)). > **NOTE：**> > - When the main window is in floating window mode, this API does not take effect or return an error if called > in non-[freeform window](../../../windowmanager/window-terminology.md#freeform-window) state.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-resize(width: int, height: int): Promise<void>--><!--Device-Window-resize(width: int, height: int): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | number | Yes |
| height | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## resize

```TypeScript
resize(width: number, height: number, callback: AsyncCallback<void>): void
```

Changes the size of this window based on the top-left vertex of the window. This API uses an asynchronous callback to return the result. A value is returned once the API is called successfully. However, the final effect cannot be obtained immediately from the return value. To obtain the final effect immediately, call [resizeAsync()](#resizeAsync). The window size is restricted by [WindowLimits](arkts-arkui-window-windowlimits-i.md#WindowLimits). You can call [getWindowLimits](#getWindowLimits) to find out the exact limits. The new window width and height you set must meet the following limits: If the window width or height is less than the minimum width or height limit, then the minimum width or height limit takes effect. However, the system window and global floating window settings are not subject to these minimum width or height restrictions. If the window width or height is greater than the maximum width or height limit, then the maximum width or height limit takes effect. > **NOTE：**> > - When the main window is in floating window mode, this API does not take effect or return an error if called > in non-[freeform window](../../../windowmanager/window-terminology.md#freeform-window) state.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-resize(width: int, height: int, callback: AsyncCallback<void>): void--><!--Device-Window-resize(width: int, height: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | number | Yes |
| height | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## resizeAsync

```TypeScript
resizeAsync(width: number, height: number): Promise<void>
```

Changes the size of this window based on the top-left vertex of the window. This API uses a promise to return the result. A value is returned once the call takes effect. You can use [getWindowProperties()](#getWindowProperties) in the callback (see the code snippet below) to obtain the final effect immediately. The window size is restricted by [WindowLimits](arkts-arkui-window-windowlimits-i.md#WindowLimits). You can call [getWindowLimits](#getWindowLimits) to find out the exact limits. The new window width and height you set must meet the following limits: If the window width or height is less than the minimum width or height limit, then the minimum width or height limit takes effect. However, the system window and global floating window settings are not subject to these minimum width or height restrictions. If the window width or height is greater than the maximum width or height limit, then the maximum width or height limit takes effect. This API takes effect only when the window is in floating window mode (**window.WindowStatusType.FLOATING**). In other scenarios, this API returns error code 1300010. (The window mode can be obtained through [getWindowStatus()](#getWindowStatus)). > **NOTE：**> > - In non-[freeform window](../../../windowmanager/window-terminology.md#freeform-window) mode, > this API does not work for the main window.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-resizeAsync(width: int, height: int): Promise<void>--><!--Device-Window-resizeAsync(width: int, height: int): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | number | Yes |
| height | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300010](../errorcode-window.md#1300010-unsupported-operation-in-the-current-window-mode) |

## restore

```TypeScript
restore(): Promise<void>
```

Restores the main window from minimization to the foreground, returning it to its size and position before it is minimized. This API takes effect only when the main window is minimized and the UIAbility is in the onForeground state. If the main window is already in the foreground, this API simply raises the window's layer. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-restore(): Promise<void>--><!--Device-Window-restore(): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## restoreMainWindow

```TypeScript
restoreMainWindow(wantParameters?: Record<string, Object>): Promise<void>
```

Restores the main window of the current window to the foreground. If the main window is already in the foreground , the main window level is raised. This API is applicable only to [TYPE_FLOAT](arkts-arkui-window-windowtype-e.md#WindowType) windows and can be called only after the DOWN event is triggered in the windows. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Window-restoreMainWindow(wantParameters?: Record<string, Object>): Promise<void>--><!--Device-Window-restoreMainWindow(wantParameters?: Record<string, Object>): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [wantParameters](../../apis-notification-kit/arkts-apis/arkts-notification-notificationrequest-notificationparameters-i.md) | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Object&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300007](../errorcode-window.md#1300007-application-startup-failure-by-windowextensionability) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setAspectRatio

```TypeScript
setAspectRatio(ratio: number, callback: AsyncCallback<void>): void
```

Sets the aspect ratio of the window content layout (excluding decorations like borders and title bars). This API uses an asynchronous callback to return the result. > **NOTE：**> > - When the window size is set by using other APIs such as > [resize](#resize) and > [resizeAsync](#resizeAsync), the window size is not restricted by **ratio**. > > - This setting is available only for the main window and takes effect only in floating window mode ( > **window.WindowStatusType.FLOATING** mode). The aspect ratio is saved persistently, which means that the > setting is valid in floating window mode even after the application is closed or the device is restarted. > > - After the aspect ratio is set for a main window of an application, the aspect ratio is used for subsequent > main windows. If you need to set the aspect ratio for just one main window, use > [setContentAspectRatio](#setContentAspectRatio) instead.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-setAspectRatio(ratio: double, callback: AsyncCallback<void>): void--><!--Device-Window-setAspectRatio(ratio: double, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [ratio](arkts-arkui-componentutils-getitemsinshapepathparams-i-sys.md) | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setAspectRatio

```TypeScript
setAspectRatio(ratio: number): Promise<void>
```

Sets the aspect ratio of the window content layout (excluding decorations like borders and title bars). This API uses a promise to return the result. > **NOTE：**> > - When the window size is set by using other APIs such as > [resize](#resize) and > [resizeAsync](#resizeAsync), the window size is not restricted by **ratio**. > > - This setting is available only for the main window and takes effect only in floating window mode ( > **window.WindowStatusType.FLOATING** mode). The aspect ratio is saved persistently, which means that the > setting is valid in floating window mode even after the application is closed or the device is restarted. > > - After the aspect ratio is set for a main window of an application, the aspect ratio is used for subsequent > main windows. If you need to set the aspect ratio for just one main window, use > [setContentAspectRatio](#setContentAspectRatio) instead.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-setAspectRatio(ratio: double): Promise<void>--><!--Device-Window-setAspectRatio(ratio: double): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [ratio](arkts-arkui-componentutils-getitemsinshapepathparams-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setBackgroundColor

```TypeScript
setBackgroundColor(color: string): Promise<void>
```

Sets the background color for this window. This API uses a promise to return the result. In the stage model, this API must be used after the call of [loadContent](#loadContent) or [setUIContent()](#setUIContent) takes effect.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [setWindowBackgroundColor](#setWindowBackgroundColor)

<!--Device-Window-setBackgroundColor(color: string): Promise<void>--><!--Device-Window-setBackgroundColor(color: string): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setBackgroundColor

```TypeScript
setBackgroundColor(color: string, callback: AsyncCallback<void>): void
```

Sets the background color for this window. This API uses an asynchronous callback to return the result. In the stage model, this API must be used after the call of [loadContent](#loadContent) or [setUIContent()](#setUIContent) takes effect.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [setWindowBackgroundColor](#setWindowBackgroundColor)

<!--Device-Window-setBackgroundColor(color: string, callback: AsyncCallback<void>): void--><!--Device-Window-setBackgroundColor(color: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setBrightness

```TypeScript
setBrightness(brightness: number): Promise<void>
```

Sets the screen brightness for this window. This API uses a promise to return the result. When the screen brightness setting for the window takes effect, Control Panel cannot adjust the system screen brightness. It can do so only after the window screen brightness is restored to the default value.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [setWindowBrightness](#setWindowBrightness)(brightness: double)

<!--Device-Window-setBrightness(brightness: number): Promise<void>--><!--Device-Window-setBrightness(brightness: number): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| brightness | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setBrightness

```TypeScript
setBrightness(brightness: number, callback: AsyncCallback<void>): void
```

Sets the screen brightness for this window. This API uses an asynchronous callback to return the result. When the screen brightness setting for the window takes effect, Control Panel cannot adjust the system screen brightness. It can do so only after the window screen brightness is restored to the default value.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [setWindowBrightness](#setWindowBrightness)(brightness: double, callback: AsyncCallback&lt;void&gt;)

<!--Device-Window-setBrightness(brightness: number, callback: AsyncCallback<void>): void--><!--Device-Window-setBrightness(brightness: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| brightness | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setColorSpace

```TypeScript
setColorSpace(colorSpace: ColorSpace): Promise<void>
```

Sets a color space for this window. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setWindowColorSpace](#setWindowColorSpace)(colorSpace:ColorSpace)

<!--Device-Window-setColorSpace(colorSpace: ColorSpace): Promise<void>--><!--Device-Window-setColorSpace(colorSpace: ColorSpace): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| colorSpace | [ColorSpace](arkts-arkui-window-colorspace-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setColorSpace

```TypeScript
setColorSpace(colorSpace: ColorSpace, callback: AsyncCallback<void>): void
```

Sets a color space for this window. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setWindowColorSpace](#setWindowColorSpace)(colorSpace:ColorSpace, callback: AsyncCallback&lt;void&gt;)

<!--Device-Window-setColorSpace(colorSpace: ColorSpace, callback: AsyncCallback<void>): void--><!--Device-Window-setColorSpace(colorSpace: ColorSpace, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| colorSpace | [ColorSpace](arkts-arkui-window-colorspace-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setContentAspectRatio

```TypeScript
setContentAspectRatio(ratio: number, isPersistent?: boolean, needUpdateRect?: boolean): Promise<void>
```

Sets the aspect ratio of the window content layout (excluding decorations like borders and title bars). This API uses a promise to return the result. > **NOTE：**> > - When you adjust the window width and height using the same **ratio** parameter, the window size adapts to > changes in the border decoration size or visibility. > > - When the window title bar is set to invisible by using > [setWindowDecorVisible](#setWindowDecorVisible), the window content area takes over the > space that was previously used by the title bar. > > - When the window size is set by using other APIs such as > [resize](#resize) and > [resizeAsync](#resizeAsync), the window size is not restricted by **ratio**. > > - This setting is available only for the main window and takes effect only in floating window mode ( > **window.WindowStatusType.FLOATING** mode).

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-setContentAspectRatio(ratio: double, isPersistent?: boolean, needUpdateRect?: boolean): Promise<void>--><!--Device-Window-setContentAspectRatio(ratio: double, isPersistent?: boolean, needUpdateRect?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [ratio](arkts-arkui-componentutils-getitemsinshapepathparams-i-sys.md) | number | Yes |
| [isPersistent](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-backgroundtaskmanager-efficiencyresourcesinfo-i-sys.md) | boolean | No |
| needUpdateRect | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setDecorButtonStyle

```TypeScript
setDecorButtonStyle(dectorStyle: DecorButtonStyle): void
```

Sets the button style of the decoration bar. The setting takes effect only for the main window and child windows. In the stage model, this API must be used after the call of [loadContent](#loadContent) or [setUIContent()](#setUIContent) takes effect.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setDecorButtonStyle(dectorStyle: DecorButtonStyle): void--><!--Device-Window-setDecorButtonStyle(dectorStyle: DecorButtonStyle): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dectorStyle | [DecorButtonStyle](arkts-arkui-window-decorbuttonstyle-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setDialogBackGestureEnabled

```TypeScript
setDialogBackGestureEnabled(enabled: boolean): Promise<void>
```

Sets whether the modal window responds to the back gesture event. An error code is returned if this API is called for a non-modal window.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setDialogBackGestureEnabled(enabled: boolean): Promise<void>--><!--Device-Window-setDialogBackGestureEnabled(enabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

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
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setDimBehind

```TypeScript
setDimBehind(dimBehindValue: number, callback: AsyncCallback<void>): void
```

Sets the dimness of the window that is not on top. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

<!--Device-Window-setDimBehind(dimBehindValue: number, callback: AsyncCallback<void>): void--><!--Device-Window-setDimBehind(dimBehindValue: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [dimBehindValue](arkts-arkui-window-windowproperties-i.md) | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setDimBehind

```TypeScript
setDimBehind(dimBehindValue: number): Promise<void>
```

Sets the dimness of the window that is not on top. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

<!--Device-Window-setDimBehind(dimBehindValue: number): Promise<void>--><!--Device-Window-setDimBehind(dimBehindValue: number): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [dimBehindValue](arkts-arkui-window-windowproperties-i.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setDragKeyFramePolicy

```TypeScript
setDragKeyFramePolicy(keyFramePolicy: KeyFramePolicy): Promise<KeyFramePolicy>
```

Sets the keyframe policy for dragging the main window. This API uses a promise to return the result. If this API is called by a non-main window, error code 1300004 is returned.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-setDragKeyFramePolicy(keyFramePolicy: KeyFramePolicy): Promise<KeyFramePolicy>--><!--Device-Window-setDragKeyFramePolicy(keyFramePolicy: KeyFramePolicy): Promise<KeyFramePolicy>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyFramePolicy | [KeyFramePolicy](arkts-arkui-window-keyframepolicy-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[KeyFramePolicy](arkts-arkui-window-keyframepolicy-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setExclusivelyHighlighted

```TypeScript
setExclusivelyHighlighted(exclusivelyHighlighted: boolean): Promise<void>
```

Sets the exclusive highlight property for the window. When a window set to exclusive highlight gains focus, other windows in the current parent-child window chain that are in the highlighted state will lose their highlighted state. This API uses a promise to return the result. This API does not take effect for the main window or modal window.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setExclusivelyHighlighted(exclusivelyHighlighted: boolean): Promise<void>--><!--Device-Window-setExclusivelyHighlighted(exclusivelyHighlighted: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| exclusivelyHighlighted | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setFloatNavigationAvoidAreaEnabled

```TypeScript
setFloatNavigationAvoidAreaEnabled(enabled: boolean): Promise<void>
```

Specifies whether to enable the avoid area for the float navigation type. When enabled, the actual value of the avoid area can be obtained by calling getWindowAvoidArea(AvoidAreaType.TYPE_FLOAT_NAVIGATION) or listening for AvoidAreaType of TYPE_FLOAT_NAVIGATION via on('avoidAreaChange') or declaring environment variables. When disabled, the float avoid area obtained through the above methods will always be 0.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Window-setFloatNavigationAvoidAreaEnabled(enabled: boolean): Promise<void>--><!--Device-Window-setFloatNavigationAvoidAreaEnabled(enabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

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
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setFocusable

```TypeScript
setFocusable(isFocusable: boolean): Promise<void>
```

Sets whether this window is focusable, that is, whether the window can gain focus after it is being clicked or using other methods. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setWindowFocusable](#setWindowFocusable)(isFocusable: boolean)

<!--Device-Window-setFocusable(isFocusable: boolean): Promise<void>--><!--Device-Window-setFocusable(isFocusable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isFocusable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setFocusable

```TypeScript
setFocusable(isFocusable: boolean, callback: AsyncCallback<void>): void
```

Sets whether this window is focusable, that is, whether the window can gain focus after it is being operated or using other methods. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setWindowFocusable](#setWindowFocusable)(isFocusable: boolean, callback: AsyncCallback&lt;void&gt;)

<!--Device-Window-setFocusable(isFocusable: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setFocusable(isFocusable: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isFocusable | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setFollowParentMultiScreenPolicy

```TypeScript
setFollowParentMultiScreenPolicy(enabled: boolean): Promise<void>
```

Sets whether a child window can span multiple screens and be simultaneously displayed while its parent window is being dragged or resized. This API uses a promise to return the result. By default, when a child window follows its parent window's layout changes (by using [moveWindowTo()](#moveWindowTo)), it does not support spanning multiple screens and being simultaneously displayed. However, calling this API on the child window enables it to span multiple screens and be simultaneously displayed during the layout adjustment process.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setFollowParentMultiScreenPolicy(enabled: boolean): Promise<void>--><!--Device-Window-setFollowParentMultiScreenPolicy(enabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

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
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setFollowParentWindowLayoutEnabled

```TypeScript
setFollowParentWindowLayoutEnabled(enabled: boolean): Promise<void>
```

Sets whether the layout information (position and size) of a child window or modal window (a window with **WindowType** set to **TYPE_DIALOG**) follows the main window. This API uses a promise to return the result. 1. This API applies only to first-level child windows or modal windows of the main window. 2. Once this API is called on a child window or modal window, its layout information will immediately match the main window and remain synchronized. This effect will persist until this API is called again with **false**. 3. If this API is called on a child window or modal window, subsequent calls to APIs like **moveTo** or **resize** to modify the layout information will not take effect. 4. When a child window or modal window stops using this functionality, its layout information (position and size) may not be a specific value. The application needs to reset it. Once this API is successfully called, the [setRelativePositionToParentWindowEnabled()](#setRelativePositionToParentWindowEnabled) API will no longer take effect.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setFollowParentWindowLayoutEnabled(enabled: boolean): Promise<void>--><!--Device-Window-setFollowParentWindowLayoutEnabled(enabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

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
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setFullScreen

```TypeScript
setFullScreen(isFullScreen: boolean, callback: AsyncCallback<void>): void
```

Sets whether the main window or the child window is in full-screen mode. This API uses an asynchronous callback to return the result. Full-screen mode means that the layout does not avoid the status bar or &lt;!--RP15--&gt;three-button navigation bar&lt;!- -RP15End--&gt;, and components may overlap with them. Non-full-screen mode means that the layout avoids the status bar and &lt;!--RP15--&gt;three-button navigation bar&lt;!--RP 15End--&gt;, and components do not overlap with them. > **NOTE：**> > This API is supported since API version 6 and deprecated since API version 9. You are advised to use > [setWindowSystemBarEnable()](#setWindowSystemBarEnable) > and [setWindowLayoutFullScreen()](#setWindowLayoutFullScreen) > to implement the full-screen mode.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [setWindowLayoutFullScreen](#setWindowLayoutFullScreen)(isLayoutFullScreen: boolean)

<!--Device-Window-setFullScreen(isFullScreen: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setFullScreen(isFullScreen: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isFullScreen](arkts-arkui-window-windowproperties-i.md) | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setFullScreen

```TypeScript
setFullScreen(isFullScreen: boolean): Promise<void>
```

Sets whether the main window or the child window is in full-screen mode. This API uses a promise to return the result. Full-screen mode means that the layout does not avoid the status bar or &lt;!--RP15--&gt;three-button navigation bar&lt;!- -RP15End--&gt;, and components may overlap with them. Non-full-screen mode means that the layout avoids the status bar and &lt;!--RP15--&gt;three-button navigation bar&lt;!--RP 15End--&gt;, and components do not overlap with them. > **NOTE：**> > This API is supported since API version 6 and deprecated since API version 9. You are advised to use > [setWindowSystemBarEnable()](#setWindowSystemBarEnable) > and [setWindowLayoutFullScreen()](#setWindowLayoutFullScreen) > to implement the full-screen mode.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [setWindowLayoutFullScreen](#setWindowLayoutFullScreen)(isLayoutFullScreen: boolean)

<!--Device-Window-setFullScreen(isFullScreen: boolean): Promise<void>--><!--Device-Window-setFullScreen(isFullScreen: boolean): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isFullScreen](arkts-arkui-window-windowproperties-i.md) | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setGestureBackEnabled

```TypeScript
setGestureBackEnabled(enabled: boolean): Promise<void>
```

Sets whether to enable the side-swipe gesture for back redirection in the current window. This API can be successfully called only for the main window, and error code 1300004 is returned on other windows. After being enabled, this function takes effect only when the window is in full-screen mode and in the foreground with the focus gained. After this function is disabled, the gesture hot zone of the current application is disabled, and the side-swipe for back redirection becomes invalid. After the user switches to another application or returns to the home screen, the gesture hot zone is restored, and the side-swipe for back redirection becomes normal.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setGestureBackEnabled(enabled: boolean): Promise<void>--><!--Device-Window-setGestureBackEnabled(enabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

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
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setImmersiveModeEnabledState

```TypeScript
setImmersiveModeEnabledState(enabled: boolean): void
```

Sets whether to enable the immersive layout for the main window. This API does not change the window mode or size. It can be called only by the main window and child windows.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setImmersiveModeEnabledState(enabled: boolean): void--><!--Device-Window-setImmersiveModeEnabledState(enabled: boolean): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setKeepScreenOn

```TypeScript
setKeepScreenOn(isKeepScreenOn: boolean): Promise<void>
```

Sets whether to keep the screen always on. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [setWindowKeepScreenOn](#setWindowKeepScreenOn)(isKeepScreenOn: boolean)

<!--Device-Window-setKeepScreenOn(isKeepScreenOn: boolean): Promise<void>--><!--Device-Window-setKeepScreenOn(isKeepScreenOn: boolean): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isKeepScreenOn](arkts-arkui-window-windowproperties-i.md) | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setKeepScreenOn

```TypeScript
setKeepScreenOn(isKeepScreenOn: boolean, callback: AsyncCallback<void>): void
```

Sets whether to keep the screen always on. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [setWindowKeepScreenOn](#setWindowKeepScreenOn)(isKeepScreenOn: boolean, callback: AsyncCallback&lt;void&gt;)

<!--Device-Window-setKeepScreenOn(isKeepScreenOn: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setKeepScreenOn(isKeepScreenOn: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isKeepScreenOn](arkts-arkui-window-windowproperties-i.md) | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setLayoutFullScreen

```TypeScript
setLayoutFullScreen(isLayoutFullScreen: boolean, callback: AsyncCallback<void>): void
```

Sets whether the main window layout or the child window layout is immersive. This API uses an asynchronous callback to return the result. An immersive layout means that the layout does not avoid the status bar or &lt;!--RP15--&gt;three-button navigation bar &lt;!--RP15End--&gt;, and components may overlap with them. A non-immersive layout means that the layout avoids the status bar and &lt;!--RP15--&gt;three-button navigation bar&lt;!-- RP15End--&gt;, and components do not overlap with them.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setWindowLayoutFullScreen](#setWindowLayoutFullScreen)(isLayoutFullScreen: boolean)

<!--Device-Window-setLayoutFullScreen(isLayoutFullScreen: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setLayoutFullScreen(isLayoutFullScreen: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isLayoutFullScreen](arkts-arkui-window-windowproperties-i.md) | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setLayoutFullScreen

```TypeScript
setLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void>
```

Sets whether the main window layout or the child window layout is immersive. This API uses a promise to return the result. An immersive layout means that the layout does not avoid the status bar or &lt;!--RP15--&gt;three-button navigation bar &lt;!--RP15End--&gt;, and components may overlap with them. A non-immersive layout means that the layout avoids the status bar and &lt;!--RP15--&gt;three-button navigation bar&lt;!-- RP15End--&gt;, and components do not overlap with them.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setWindowLayoutFullScreen](#setWindowLayoutFullScreen)(isLayoutFullScreen: boolean)

<!--Device-Window-setLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void>--><!--Device-Window-setLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isLayoutFullScreen](arkts-arkui-window-windowproperties-i.md) | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setOutsideTouchable

```TypeScript
setOutsideTouchable(touchable: boolean): Promise<void>
```

Sets whether the area outside the child window is touchable. This API uses a promise to return the result. > Starting from API version 9, the area outside the child window is touchable by default. This API is no longer > supported and no substitute API is provided.

**Since:** 7

**Deprecated since:** 9

<!--Device-Window-setOutsideTouchable(touchable: boolean): Promise<void>--><!--Device-Window-setOutsideTouchable(touchable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| touchable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setOutsideTouchable

```TypeScript
setOutsideTouchable(touchable: boolean, callback: AsyncCallback<void>): void
```

Sets whether the area outside the child window is touchable. This API uses an asynchronous callback to return the result. > Starting from API version 9, the area outside the child window is touchable by default. This API is no longer > supported and no substitute API is provided.

**Since:** 7

**Deprecated since:** 9

<!--Device-Window-setOutsideTouchable(touchable: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setOutsideTouchable(touchable: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| touchable | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setParentWindow

```TypeScript
setParentWindow(windowId: number): Promise<void>
```

Sets a new parent window for this child window. The new parent window can be a main window, another child window, or a floating window in the same process. This API uses a promise to return the result. If the child window is focused and the new parent window is in the foreground, the new parent window will be raised. If the child window is focused and the new parent window has a modal child window with a higher level, the focus will be transferred to that modal child window.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setParentWindow(windowId: int): Promise<void>--><!--Device-Window-setParentWindow(windowId: int): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [1300009](../errorcode-window.md#1300009-invalid-parent-window) |

## setPreferredOrientation

```TypeScript
setPreferredOrientation(orientation: Orientation): Promise<void>
```

Sets the preferred orientation for the main window. This API uses a promise to return the result. This API does not take effect when it is called by a child window. Before &lt;!--RP1--&gt;OpenHarmony 6.1&lt;!--RP1End--&gt;, this API can be called only by and takes effect for the main window. If it is called for other window types, it does not take effect. Starting from &lt;!--RP1--&gt;OpenHarmony 6.1&lt;!--RP1End--&gt;, this API can be called by the main window and the system window with **WindowType** set to **TYPE_WALLET_SWIPE_CARD**. If it is called for other window types, it does not take effect. When the system window calls the **setPreferredOrientation** API, if there is a higher-level window for which the display orientation has been set, the call will not take effect immediately. In this case, the set display orientation will be recorded. When there is a no higher-level window with the display orientation set, the last orientation request will be restored. When the display orientation is set for the system window whose **WindowType** is **TYPE_WALLET_SWIPE_CARD** and takes effect, the foreground application will transition to the background.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-setPreferredOrientation(orientation: Orientation): Promise<void>--><!--Device-Window-setPreferredOrientation(orientation: Orientation): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| orientation | [Orientation](arkts-arkui-window-orientation-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setPreferredOrientation

```TypeScript
setPreferredOrientation(orientation: Orientation, callback: AsyncCallback<void>): void
```

Sets the preferred orientation for this window. This API uses an asynchronous callback to return the result. For details about the development practices of orientation, see [Display Orientation Switching](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-landscape-and-portrait-development) . Before &lt;!--RP1--&gt;OpenHarmony 6.1&lt;!--RP1End--&gt;, this API can be called only by and takes effect for the main window. If it is called for other window types, it does not take effect. Starting from &lt;!--RP1--&gt;OpenHarmony 6.1&lt;!--RP1End--&gt;, this API can be called by the main window and the system window with **WindowType** set to **TYPE_WALLET_SWIPE_CARD**. If it is called for other window types, it does not take effect. When the system window calls the **setPreferredOrientation** API, if there is a higher-level window for which the display orientation has been set, the call will not take effect immediately. In this case, the set display orientation will be recorded. When there is a no higher-level window with the display orientation set, the last orientation request will be restored. When the display orientation is set for the system window whose **WindowType** is **TYPE_WALLET_SWIPE_CARD** and takes effect, the foreground application will transition to the background.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-setPreferredOrientation(orientation: Orientation, callback: AsyncCallback<void>): void--><!--Device-Window-setPreferredOrientation(orientation: Orientation, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| orientation | [Orientation](arkts-arkui-window-orientation-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setPreferredOrientationWithResult

```TypeScript
setPreferredOrientationWithResult(orientation: Orientation): Promise<OrientationResult>
```

Sets the preferred orientation for the main window. This API uses a promise to return the result. It does not take effect on devices that do not support rotation with the sensor, on 2-in-1 devices or for the child window.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Window-setPreferredOrientationWithResult(orientation: Orientation): Promise<OrientationResult>--><!--Device-Window-setPreferredOrientationWithResult(orientation: Orientation): Promise<OrientationResult>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| orientation | [Orientation](arkts-arkui-window-orientation-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OrientationResult](arkts-arkui-window-orientationresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setPrivacyMode

```TypeScript
setPrivacyMode(isPrivacyMode: boolean): Promise<void>
```

Sets whether this window is in privacy mode. This API uses a promise to return the result. A window in privacy mode cannot be captured or recorded. This API can be used in scenarios where screen capture or recording is disabled.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setWindowPrivacyMode](#setWindowPrivacyMode)(isPrivacyMode: boolean)

<!--Device-Window-setPrivacyMode(isPrivacyMode: boolean): Promise<void>--><!--Device-Window-setPrivacyMode(isPrivacyMode: boolean): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isPrivacyMode](arkts-arkui-window-windowproperties-i.md) | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setPrivacyMode

```TypeScript
setPrivacyMode(isPrivacyMode: boolean, callback: AsyncCallback<void>): void
```

Sets whether this window is in privacy mode. This API uses an asynchronous callback to return the result. A window in privacy mode cannot be captured or recorded. This API can be used in scenarios where screen capture or recording is disabled.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setWindowPrivacyMode](#setWindowPrivacyMode)(isPrivacyMode: boolean, callback: AsyncCallback&lt;void&gt;)

<!--Device-Window-setPrivacyMode(isPrivacyMode: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setPrivacyMode(isPrivacyMode: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isPrivacyMode](arkts-arkui-window-windowproperties-i.md) | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setRaiseByClickEnabled

```TypeScript
setRaiseByClickEnabled(enable: boolean): Promise<void>
```

Sets whether to enable a child window to raise itself by click. This API uses a promise to return the result. Generally, when a child window is clicked, it is brought to the forefront among sibling child windows of the same type that share the same parent window within the application. If the **enable** parameter is set to **false**, when the child window is clicked, it still stays in its existing position. Before calling this API, ensure that the child window has been created and [showWindow()](#showWindow) has been successfully executed.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-setRaiseByClickEnabled(enable: boolean): Promise<void>--><!--Device-Window-setRaiseByClickEnabled(enable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [1300009](../errorcode-window.md#1300009-invalid-parent-window) |

## setReceiveDragEventEnabled

```TypeScript
setReceiveDragEventEnabled(enabled: boolean): Promise<void>
```

Sets whether the current window can receive [drag events](../arkts-components/arkts-arkui-dragevent-i.md#DragEvent). This API uses a promise to return the result. By default, the value of **enabled** is **true**, indicating that the window can receive drag events. If the value of **enabled** is **false**, the current window cannot receive drag events.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Window-setReceiveDragEventEnabled(enabled: boolean): Promise<void>--><!--Device-Window-setReceiveDragEventEnabled(enabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

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
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setRelativePositionToParentWindowEnabled

```TypeScript
setRelativePositionToParentWindowEnabled(enabled: boolean, anchor?: WindowAnchor,
        offsetX?: number, offsetY?: number): Promise<void>
```

Sets whether a first-level child window can maintain a fixed relative position to the main window. This API works only in [freeform window](../../../windowmanager/window-terminology.md#freeform-window) mode. This API uses a promise to return the result. The relative position is defined by the offset between the anchor points of the child window and the main window. Both the child window and the main window use the same type of anchor point. 1. This API applies only to level-1 child windows that are not maximized. 2. Once this API is called on a child window, its display position will immediately follow the main window and maintain a fixed relative position. This effect will persist until this API is called again with **false**. 3. If this API is called on a child window, subsequent calls to [moveWindowTo()](#moveWindowTo) or [maximize()](#maximize) to modify the window's position or size will not take effect. Once this API is successfully called, the [setFollowParentWindowLayoutEnabled()](#setFollowParentWindowLayoutEnabled) API will no longer take effect.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-setRelativePositionToParentWindowEnabled(enabled: boolean, anchor?: WindowAnchor,        offsetX?: int, offsetY?: int): Promise<void>--><!--Device-Window-setRelativePositionToParentWindowEnabled(enabled: boolean, anchor?: WindowAnchor,        offsetX?: int, offsetY?: int): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |
| anchor | [WindowAnchor](arkts-arkui-window-windowanchor-e.md) | No |
| offsetX | number | No |
| offsetY | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setResizeByDragEnabled

```TypeScript
setResizeByDragEnabled(enable: boolean, callback: AsyncCallback<void>): void
```

Sets whether to enable the main window or child window with decorations to resize itself by dragging. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setResizeByDragEnabled(enable: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setResizeByDragEnabled(enable: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setResizeByDragEnabled

```TypeScript
setResizeByDragEnabled(enable: boolean): Promise<void>
```

Sets whether to enable the main window or child window with decorations to resize itself by dragging. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setResizeByDragEnabled(enable: boolean): Promise<void>--><!--Device-Window-setResizeByDragEnabled(enable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setSeparationTouchEnabled

```TypeScript
setSeparationTouchEnabled(enabled: boolean): Promise<void>
```

Sets whether the current window supports the event separation state. This API uses a promise to return the result. In the default scenario, the value of **enabled** is **true**, indicating that the event separation state is supported. When the event separation state is supported: - All events generated by finger taps are sent to the window that the finger taps hit. When the event separation state is not supported (the value of **enabled** is **false**): - If the first finger taps the window, keeps hitting the window, and does not lift up, the events generated by subsequent taps of other fingers are distributed to the window, regardless of whether the taps of other fingers hit the window. - If the first finger taps the window and does not keep hitting the window, the events generated by subsequent taps of other fingers are not distributed to the window and are discarded by the system, even if the taps of other fingers hit the window.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Window-setSeparationTouchEnabled(enabled: boolean): Promise<void>--><!--Device-Window-setSeparationTouchEnabled(enabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

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
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setSpecificSystemBarEnabled

```TypeScript
setSpecificSystemBarEnabled(name: SpecificSystemBar, enable: boolean, enableAnimation?: boolean): Promise<void>
```

Sets whether to show or hide the status bar and &lt;!--RP15--&gt;three-button navigation bar&lt;!--RP15End--&gt; of the main window. This API uses a promise to return the result. The return value does not indicate that the status bar and &lt;!--RP15--&gt;three-button navigation bar&lt;!--RP15End--&gt; are shown or hidden. This API does not take effect when it is called by a child window. The setting does not take effect when the main window is in non-full-screen or non-maximized mode (such as floating windows or split-screen mode). It takes effect once the main window enters full-screen or maximized mode.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setSpecificSystemBarEnabled(name: SpecificSystemBar, enable: boolean, enableAnimation?: boolean): Promise<void>--><!--Device-Window-setSpecificSystemBarEnabled(name: SpecificSystemBar, enable: boolean, enableAnimation?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | [SpecificSystemBar](arkts-arkui-window-specificsystembar-t.md) | Yes |
| enable | boolean | Yes |
| enableAnimation | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setStatusBarColor

```TypeScript
setStatusBarColor(color: ColorMetrics): Promise<void>
```

Sets the text color of the status bar in the main window. This API uses a promise to return the result. Setting the status bar text color is not supported for child windows. Calling this API on a child window will have no effect. The setting does not take effect when the main window is in non-full-screen or non-maximized mode (such as floating windows or split-screen mode). It takes effect once the main window enters full-screen or maximized mode.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setStatusBarColor(color: ColorMetrics): Promise<void>--><!--Device-Window-setStatusBarColor(color: ColorMetrics): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [ColorMetrics](../../apis-na/arkts-apis/arkts-na-graphics-colormetrics-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setSubWindowModal

```TypeScript
setSubWindowModal(isModal: boolean): Promise<void>
```

Enables the modal property of the child window. This API uses a promise to return the result. This API must be called by a child window and the setting takes effect for the child window. After the modal property is enabled, the parent window does not respond to user interactions until the child window is closed or the child window's modal property is disabled. If this API is called by a main window, an error is reported.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setSubWindowModal(isModal: boolean): Promise<void>--><!--Device-Window-setSubWindowModal(isModal: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isModal | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setSubWindowModal

```TypeScript
setSubWindowModal(isModal: boolean, modalityType: ModalityType): Promise<void>
```

Sets the modality type of the child window. This API uses a promise to return the result. When the child window is of the window-modal type, its parent window does not respond to user interactions until the child window is closed or the child window's modal property is disabled. When the child window is of the application-modal type, its parent window and the windows from other instances of the application do not respond to user interactions until the child window is closed or the child window's modal property is disabled. This API is used to set the modality type. To disable the modal property, you are advised to use [setSubWindowModal&lt;sup&gt;12+&lt;/sup&gt;](#setSubWindowModal). If this API is called by a window other than the child window, an error is reported.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setSubWindowModal(isModal: boolean, modalityType: ModalityType): Promise<void>--><!--Device-Window-setSubWindowModal(isModal: boolean, modalityType: ModalityType): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isModal | boolean | Yes |
| [modalityType](arkts-arkui-window-subwindowoptions-i.md) | [ModalityType](arkts-arkui-window-modalitytype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setSubWindowZLevel

```TypeScript
setSubWindowZLevel(zLevel: number): Promise<void>
```

Sets the z-level of the current child window. Child windows with modal properties are not supported. This API uses a promise to return the result. Changing the z-level of a child window using this API will not cause a focus switch. You are advised to use [shiftAppWindowFocus()](arkts-arkui-window-shiftappwindowfocus-f.md#shiftAppWindowFocus) for focus switching.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setSubWindowZLevel(zLevel: int): Promise<void>--><!--Device-Window-setSubWindowZLevel(zLevel: int): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [zLevel](arkts-arkui-window-subwindowoptions-i.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [1300009](../errorcode-window.md#1300009-invalid-parent-window) |

## setSupportedWindowModes

```TypeScript
setSupportedWindowModes(supportedWindowModes: Array<bundleManager.SupportWindowMode>): Promise<void>
```

Sets the supported window modes of the app window.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Window-setSupportedWindowModes(supportedWindowModes: Array<bundleManager.SupportWindowMode>): Promise<void>--><!--Device-Window-setSupportedWindowModes(supportedWindowModes: Array<bundleManager.SupportWindowMode>): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| supportedWindowModes | Array & lt;bundleManager.SupportWindowMode & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setSystemAvoidAreaEnabled

```TypeScript
setSystemAvoidAreaEnabled(enabled: boolean): Promise<void>
```

Enables the capability to obtain the window avoidance area information using [getWindowAvoidArea()](#getWindowAvoidArea) or listen for window avoidance area changes using [on('avoidAreaChange')](#on_rotationChange) after a global floating window, modal window, or system window is created.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setSystemAvoidAreaEnabled(enabled: boolean): Promise<void>--><!--Device-Window-setSystemAvoidAreaEnabled(enabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

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
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setSystemBarEnable

```TypeScript
setSystemBarEnable(names: Array<'status' | 'navigation'>, callback: AsyncCallback<void>): void
```

&lt;!--RP14--&gt;Sets whether to show the status bar and three-button navigation bar in the main window. The visibility of the status bar and three-button navigation bar is controlled by **status** and **navigation**, respectively.&lt;!--RP14End--&gt; This API uses an asynchronous callback to return the result. From API version 12, &lt;!--RP5--&gt;this API does not take effect on 2-in-1 devices.&lt;!--RP5End--&gt; The return value does not indicate that the status bar and &lt;!--RP15--&gt;three-button navigation bar&lt;!--RP15End--&gt; are shown or hidden. This API does not take effect when it is called by a child window. The configuration does not take effect in non-full-screen mode (such as floating window or split-screen mode).

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setWindowSystemBarEnable](#setWindowSystemBarEnable)(names: Array&lt;'status'|'navigation'&gt;)

<!--Device-Window-setSystemBarEnable(names: Array<'status' | 'navigation'>, callback: AsyncCallback<void>): void--><!--Device-Window-setSystemBarEnable(names: Array<'status' | 'navigation'>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| names | Array & lt;'status' \ | 'navigation' & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setSystemBarEnable

```TypeScript
setSystemBarEnable(names: Array<'status' | 'navigation'>): Promise<void>
```

&lt;!--RP14--&gt;Sets whether to show the status bar and three-button navigation bar in the main window. The visibility of the status bar and three-button navigation bar is controlled by **status** and **navigation**, respectively.&lt;!--RP14End--&gt; This API uses a promise to return the result. From API version 12, &lt;!--RP5--&gt;this API does not take effect on 2-in-1 devices.&lt;!--RP5End--&gt; The return value does not indicate that the status bar and &lt;!--RP15--&gt;three-button navigation bar&lt;!--RP15End--&gt; are shown or hidden. This API does not take effect when it is called by a child window. The configuration does not take effect in non-full-screen mode (such as floating window or split-screen mode).

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setWindowSystemBarEnable](#setWindowSystemBarEnable)(names: Array&lt;'status'|'navigation'&gt;)

<!--Device-Window-setSystemBarEnable(names: Array<'status' | 'navigation'>): Promise<void>--><!--Device-Window-setSystemBarEnable(names: Array<'status' | 'navigation'>): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| names | Array & lt;'status' \ | 'navigation' & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setSystemBarProperties

```TypeScript
setSystemBarProperties(systemBarProperties: SystemBarProperties, callback: AsyncCallback<void>): void
```

Sets the properties of the &lt;!--Del--&gt;three-button navigation bar and &lt;!--DelEnd--&gt;status bar of the main window. This API uses an asynchronous callback to return the result. &lt;!--RP5--&gt;This API does not take effect on 2-in-1 devices.&lt;!--RP5End--&gt; This API does not take effect when it is called by a child window. The configuration does not take effect in non- full-screen mode (such as floating window or split-screen mode).

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [setWindowSystemBarProperties](#setWindowSystemBarProperties)(systemBarProperties: SystemBarProperties)

<!--Device-Window-setSystemBarProperties(systemBarProperties: SystemBarProperties, callback: AsyncCallback<void>): void--><!--Device-Window-setSystemBarProperties(systemBarProperties: SystemBarProperties, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| systemBarProperties | [SystemBarProperties](arkts-arkui-window-systembarproperties-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setSystemBarProperties

```TypeScript
setSystemBarProperties(systemBarProperties: SystemBarProperties): Promise<void>
```

Sets the properties of the &lt;!--Del--&gt;three-button navigation bar and &lt;!--DelEnd--&gt;status bar of the main window. This API uses a promise to return the result. &lt;!--RP5--&gt;This API does not take effect on 2-in-1 devices.&lt;!--RP5 End--&gt; This API does not take effect when it is called by a child window.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [setWindowSystemBarProperties](#setWindowSystemBarProperties)(systemBarProperties: SystemBarProperties)

<!--Device-Window-setSystemBarProperties(systemBarProperties: SystemBarProperties): Promise<void>--><!--Device-Window-setSystemBarProperties(systemBarProperties: SystemBarProperties): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| systemBarProperties | [SystemBarProperties](arkts-arkui-window-systembarproperties-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setTitleAndDockHoverShown

```TypeScript
setTitleAndDockHoverShown(isTitleHoverShown?: boolean, isDockHoverShown?: boolean): Promise<void>
```

Sets whether to show the window title bar and dock bar when the cursor hovers over the hot zone while the main window is in full-screen mode. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setTitleAndDockHoverShown(isTitleHoverShown?: boolean, isDockHoverShown?: boolean): Promise<void>--><!--Device-Window-setTitleAndDockHoverShown(isTitleHoverShown?: boolean, isDockHoverShown?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isTitleHoverShown | boolean | No |
| isDockHoverShown | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setTouchable

```TypeScript
setTouchable(isTouchable: boolean): Promise<void>
```

Sets whether this window is touchable. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setWindowTouchable](#setWindowTouchable)(isTouchable: boolean)

<!--Device-Window-setTouchable(isTouchable: boolean): Promise<void>--><!--Device-Window-setTouchable(isTouchable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isTouchable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setTouchable

```TypeScript
setTouchable(isTouchable: boolean, callback: AsyncCallback<void>): void
```

Sets whether this window is touchable. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setWindowTouchable](#setWindowTouchable)(isTouchable: boolean, callback: AsyncCallback&lt;void&gt;)

<!--Device-Window-setTouchable(isTouchable: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setTouchable(isTouchable: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isTouchable | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setUIContent

```TypeScript
setUIContent(path: string, callback: AsyncCallback<void>): void
```

Loads the content of a page, with its path in the current project specified, to this window. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-setUIContent(path: string, callback: AsyncCallback<void>): void--><!--Device-Window-setUIContent(path: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setUIContent

```TypeScript
setUIContent(path: string): Promise<void>
```

Loads the content of a page, with its path in the current project specified, to this window. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-setUIContent(path: string): Promise<void>--><!--Device-Window-setUIContent(path: string): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setWindowBackgroundColor

```TypeScript
setWindowBackgroundColor(color: string | ColorMetrics): void
```

Sets the background color for this window. If this API is not called, the default background color of the window is **'#FFF0F0F0'** in light mode and **'#FF1A1A1A'** in dark mode. In the stage model, this API must be used after the call of [loadContent](#loadContent) or [setUIContent()](#setUIContent) takes effect.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-setWindowBackgroundColor(color: string | ColorMetrics): void--><!--Device-Window-setWindowBackgroundColor(color: string | ColorMetrics): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | string \| [ColorMetrics](../../apis-na/arkts-apis/arkts-na-graphics-colormetrics-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setWindowBrightness

```TypeScript
setWindowBrightness(brightness: number): Promise<void>
```

Sets the window brightness for the main window. The window brightness takes effect only when the window is in the foreground and has focus. This API uses a promise to return the result. When the setting is valid, it affects only the physical screen where the window is displayed. It does not apply to virtual displays (for example, casting/mirroring screens). If the input parameter is **-1**, the window brightness reverts to the system brightness (which can be adjusted through Control Panel or shortcut keys). When the window moves to the background, the setting becomes invalid, and brightness can be adjusted through Control Panel or shortcut keys. You are advised not to call this API consecutively or when the window transitions to the background. Otherwise, timing issues may occur.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-setWindowBrightness(brightness: double): Promise<void>--><!--Device-Window-setWindowBrightness(brightness: double): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| brightness | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setWindowBrightness

```TypeScript
setWindowBrightness(brightness: number, callback: AsyncCallback<void>): void
```

Sets the window brightness for the main window. The window brightness takes effect only when the window is in the foreground and has focus. This API uses an asynchronous callback to return the result. When the setting is valid, it affects only the physical screen where the window is displayed. It does not apply to virtual displays (for example, casting/mirroring screens). If the input parameter is **-1**, the window brightness reverts to the system brightness (which can be adjusted through Control Panel or shortcut keys). When the window moves to the background, the setting becomes invalid, and brightness can be adjusted through Control Panel or shortcut keys. You are advised not to call this API consecutively or when the window transitions to the background. Otherwise, timing issues may occur.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-setWindowBrightness(brightness: double, callback: AsyncCallback<void>): void--><!--Device-Window-setWindowBrightness(brightness: double, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| brightness | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setWindowColorSpace

```TypeScript
setWindowColorSpace(colorSpace:ColorSpace): Promise<void>
```

Sets a color space for this window. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-setWindowColorSpace(colorSpace:ColorSpace): Promise<void>--><!--Device-Window-setWindowColorSpace(colorSpace:ColorSpace): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| colorSpace | [ColorSpace](arkts-arkui-window-colorspace-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setWindowColorSpace

```TypeScript
setWindowColorSpace(colorSpace:ColorSpace, callback: AsyncCallback<void>): void
```

Sets a color space for this window. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-setWindowColorSpace(colorSpace:ColorSpace, callback: AsyncCallback<void>): void--><!--Device-Window-setWindowColorSpace(colorSpace:ColorSpace, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| colorSpace | [ColorSpace](arkts-arkui-window-colorspace-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setWindowContainerColor

```TypeScript
setWindowContainerColor(activeColor: string, inactiveColor: string): void
```

Sets the background color of the main window container for both when it has focus and when it does not. In the stage model, you need to call this API after [loadContent()](#loadContent) or [setUIContent()](#setUIContent). The background color you set here covers the entire window, including both the title bar and the content area. If you also use [setWindowBackgroundColor()](#setWindowBackgroundColor), the content area shows the window background color, whereas the title bar shows the container background color.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.SET_WINDOW_TRANSPARENT

<!--Device-Window-setWindowContainerColor(activeColor: string, inactiveColor: string): void--><!--Device-Window-setWindowContainerColor(activeColor: string, inactiveColor: string): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| activeColor | string | Yes |
| inactiveColor | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## setWindowCornerRadius

```TypeScript
setWindowCornerRadius(cornerRadius: number): Promise<void>
```

Sets the radius of the rounded corners for a child window or floating window. This API uses a promise to return the result. If the radius of the rounded corner is too large, it may cause the three buttons (maximize, minimize, and close) to be clipped and make their hotspots less recognizable. Set an appropriate radius based on the window size. Before calling this API, you can call [getWindowCornerRadius()](#getWindowCornerRadius) to obtain the default radius of rounded corners of the window.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setWindowCornerRadius(cornerRadius: double): Promise<void>--><!--Device-Window-setWindowCornerRadius(cornerRadius: double): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cornerRadius | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setWindowDecorHeight

```TypeScript
setWindowDecorHeight(height: number): void
```

Sets the height of the title bar of this window. This API takes effect for the window that has a title bar and a three-button area. In the stage model, this API must be used after the call of [loadContent](#loadContent) or [setUIContent()](#setUIContent) takes effect. For tablets, if this API is called outside of [free windows](../../../windowmanager/window-terminology.md#free-windows) mode, the change applies once the device switches to free windows mode. If this API is called in free windows mode, the change takes effect immediately. When the main window transitions into full-screen mode, hovering the mouse over the hot zone of the window's title bar region will cause a floating title bar to appear, with a fixed height of 37 vp.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-setWindowDecorHeight(height: int): void--><!--Device-Window-setWindowDecorHeight(height: int): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| height | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setWindowDecorVisible

```TypeScript
setWindowDecorVisible(isVisible: boolean): void
```

Sets whether the title bar is visible in the window. This API takes effect for the window that has a title bar or a three-button area. In the stage model, this API must be used after the call of [loadContent](#loadContent) or [setUIContent()](#setUIContent) takes effect. When the window title bar is hidden and the main window transitions into full-screen mode, hovering the cursor over the hot zone of the top window's title bar will cause a floating title bar to appear. To prevent the floating title bar from appearing, call [setTitleAndDockHoverShown()](#setTitleAndDockHoverShown).

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-setWindowDecorVisible(isVisible: boolean): void--><!--Device-Window-setWindowDecorVisible(isVisible: boolean): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isVisible | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setWindowDelayRaiseOnDrag

```TypeScript
setWindowDelayRaiseOnDrag(isEnabled: boolean): void
```

Sets whether to enable delayed raising for the window. This API takes effect only for the main window and child windows. If this API is not called or **false** is passed, the main window and child windows are raised immediately upon a left mouse button press by default. When this API is called to enable delayed raising, in cross-window drag-and-drop situations, the window that contains the draggable component does not raise until the left mouse button is released, rather than raising immediately when the button is pressed.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setWindowDelayRaiseOnDrag(isEnabled: boolean): void--><!--Device-Window-setWindowDelayRaiseOnDrag(isEnabled: boolean): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isEnabled | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setWindowFocusable

```TypeScript
setWindowFocusable(isFocusable: boolean): Promise<void>
```

Sets whether this window is focusable. This API uses a promise to return the result. Starting from API version 22, if a virtual screen is created by calling [createVirtualScreen](arkts-arkui-display-createvirtualscreen-f.md#createVirtualScreen) with **supportsFocus** set to **false**, windows on that virtual screen cannot call the current API to change their focusability. Attempting to do so will result in error code 1300002.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-setWindowFocusable(isFocusable: boolean): Promise<void>--><!--Device-Window-setWindowFocusable(isFocusable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isFocusable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setWindowFocusable

```TypeScript
setWindowFocusable(isFocusable: boolean, callback: AsyncCallback<void>): void
```

Sets whether this window is focusable. This API uses an asynchronous callback to return the result. Starting from API version 22, if a virtual screen is created by calling [createVirtualScreen](arkts-arkui-display-createvirtualscreen-f.md#createVirtualScreen) with **supportsFocus** set to **false**, windows on that virtual screen cannot call the current API to change their focusability. Attempting to do so will result in error code 1300002.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-setWindowFocusable(isFocusable: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setWindowFocusable(isFocusable: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isFocusable | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setWindowGrayScale

```TypeScript
setWindowGrayScale(grayScale: number): Promise<void>
```

Sets the grayscale effect for this window. This API uses a promise to return the result. This API can be called only after [loadContent()](#loadContent) or [setUIContent()](#setUIContent) is called.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setWindowGrayScale(grayScale: double): Promise<void>--><!--Device-Window-setWindowGrayScale(grayScale: double): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| grayScale | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setWindowKeepScreenOn

```TypeScript
setWindowKeepScreenOn(isKeepScreenOn: boolean): Promise<void>
```

Sets whether to keep the screen always on. This API uses a promise to return the result. Set **isKeepScreenOn** to **true** only in necessary scenarios (such as navigation, video playback, drawing, and gaming scenarios). After exiting these scenarios, set the parameter to **false**. Do not use this API in other scenarios (such as no screen interaction or audio playback). When the system detects that the API is used in a non-standard manner, automatic screen-off may be invoked.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-setWindowKeepScreenOn(isKeepScreenOn: boolean): Promise<void>--><!--Device-Window-setWindowKeepScreenOn(isKeepScreenOn: boolean): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isKeepScreenOn](arkts-arkui-window-windowproperties-i.md) | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setWindowKeepScreenOn

```TypeScript
setWindowKeepScreenOn(isKeepScreenOn: boolean, callback: AsyncCallback<void>): void
```

Sets whether to keep the screen always on. This API uses an asynchronous callback to return the result. Set **isKeepScreenOn** to **true** only in necessary scenarios (such as navigation, video playback, drawing, and gaming scenarios). After exiting these scenarios, set the parameter to **false**. Do not use this API in other scenarios (such as no screen interaction or audio playback). When the system detects that the API is used in a non-standard manner, automatic screen-off may be invoked.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-setWindowKeepScreenOn(isKeepScreenOn: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setWindowKeepScreenOn(isKeepScreenOn: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isKeepScreenOn](arkts-arkui-window-windowproperties-i.md) | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setWindowLayoutFullScreen

```TypeScript
setWindowLayoutFullScreen(isLayoutFullScreen: boolean, callback: AsyncCallback<void>): void
```

Sets whether the main window layout or the child window layout is immersive. This API uses an asynchronous callback to return the result. It does not work when called by a system window. An immersive layout means that the layout does not avoid the status bar or &lt;!--RP15--&gt;three-button navigation bar &lt;!--RP15End--&gt;, and components may overlap with them. A non-immersive layout means that the layout avoids the status bar and &lt;!--RP15--&gt;three-button navigation bar&lt;!-- RP15End--&gt;, and components do not overlap with them.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [setWindowLayoutFullScreen](#setWindowLayoutFullScreen)(isLayoutFullScreen: boolean)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-setWindowLayoutFullScreen(isLayoutFullScreen: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setWindowLayoutFullScreen(isLayoutFullScreen: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isLayoutFullScreen](arkts-arkui-window-windowproperties-i.md) | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setWindowLayoutFullScreen

```TypeScript
setWindowLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void>
```

Sets whether the application main window layout or the application child window layout is immersive. This API uses a promise to return the result. It does not work when called by other windows, and no error is reported. An immersive layout means that the layout does not avoid the status bar or &lt;!--RP15--&gt;three-button navigation bar &lt;!--RP15End--&gt;, and components may overlap with them. A non-immersive layout means that the layout avoids the status bar and &lt;!--RP15--&gt;three-button navigation bar&lt;!-- RP15End--&gt;, and components do not overlap with them.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-setWindowLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void>--><!--Device-Window-setWindowLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isLayoutFullScreen](arkts-arkui-window-windowproperties-i.md) | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setWindowLimits

```TypeScript
setWindowLimits(windowLimits: WindowLimits): Promise<WindowLimits>
```

Sets the size limits for this window. This API uses a promise to return the result. By default, system size limits are provided. They are determined by the product configuration and cannot be modified. If **setWindowLimits** has not been called, you can call [getWindowLimits](#getWindowLimits) or [getWindowLimitsVP](#getWindowLimitsVP) to obtain the system size limits.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-setWindowLimits(windowLimits: WindowLimits): Promise<WindowLimits>--><!--Device-Window-setWindowLimits(windowLimits: WindowLimits): Promise<WindowLimits>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowLimits | [WindowLimits](arkts-arkui-window-windowlimits-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[WindowLimits](arkts-arkui-window-windowlimits-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setWindowLimits

```TypeScript
setWindowLimits(windowLimits: WindowLimits, isForcible: boolean): Promise<WindowLimits>
```

Sets the size limits for this window. This API uses a promise to return the result. By default, system size limits are provided. They are determined by the product configuration and cannot be modified. If **setWindowLimits** has not been called, you can call [getWindowLimits](#getWindowLimits) or [getWindowLimitsVP](#getWindowLimitsVP) to obtain the system size limits.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setWindowLimits(windowLimits: WindowLimits, isForcible: boolean): Promise<WindowLimits>--><!--Device-Window-setWindowLimits(windowLimits: WindowLimits, isForcible: boolean): Promise<WindowLimits>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowLimits | [WindowLimits](arkts-arkui-window-windowlimits-i.md) | Yes |
| isForcible | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[WindowLimits](arkts-arkui-window-windowlimits-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setWindowMask

```TypeScript
setWindowMask(windowMask: Array<Array<number>>): Promise<void>
```

Sets a mask for this window to get an irregularly shaped window. This API uses a promise to return the result. The mask is used to describe the shape of the irregularly shaped window. This API is available only for child windows and global floating windows. When the size of an irregularly shaped window changes, the actual display content is the intersection of the mask size and the window size. Error code 1300002 may be returned only when multiple threads operate the same window. Error code 401 is returned when the window is destroyed.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setWindowMask(windowMask: Array<Array<long>>): Promise<void>--><!--Device-Window-setWindowMask(windowMask: Array<Array<long>>): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowMask | Array & lt;Array & lt;number & gt; & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setWindowMaskWithAlpha

```TypeScript
setWindowMaskWithAlpha(windowMask: Uint8Array, maskWidth: number, maskHeight: number): Promise<void>
```

Set the window mask using a per-pixel alpha array

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Window-setWindowMaskWithAlpha(windowMask: Uint8Array, maskWidth: int, maskHeight: int): Promise<void>--><!--Device-Window-setWindowMaskWithAlpha(windowMask: Uint8Array, maskWidth: int, maskHeight: int): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowMask | Uint8Array | Yes |
| maskWidth | number | Yes |
| maskHeight | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setWindowPrivacyMode

```TypeScript
setWindowPrivacyMode(isPrivacyMode: boolean): Promise<void>
```

Sets whether this window is in privacy mode. This API uses a promise to return the result. A window in privacy mode cannot be captured or recorded. When a window in privacy mode is moved to the background, it displays as a white overlay or privacy mask in the multi-tasking view. If this API is not called, the privacy mode is disabled by default, and the window can be captured or recorded.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.PRIVACY_WINDOW

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-setWindowPrivacyMode(isPrivacyMode: boolean): Promise<void>--><!--Device-Window-setWindowPrivacyMode(isPrivacyMode: boolean): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isPrivacyMode](arkts-arkui-window-windowproperties-i.md) | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## setWindowPrivacyMode

```TypeScript
setWindowPrivacyMode(isPrivacyMode: boolean, callback: AsyncCallback<void>): void
```

Sets whether this window is in privacy mode. This API uses an asynchronous callback to return the result. A window in privacy mode cannot be captured or recorded. When a window in privacy mode is moved to the background, it displays as a white overlay or privacy mask in the multi-tasking view. If this API is not called, the privacy mode is disabled by default, and the window can be captured or recorded.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.PRIVACY_WINDOW

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-setWindowPrivacyMode(isPrivacyMode: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setWindowPrivacyMode(isPrivacyMode: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isPrivacyMode](arkts-arkui-window-windowproperties-i.md) | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## setWindowShadowEnabled

```TypeScript
setWindowShadowEnabled(enable: boolean): Promise<void>
```

Sets whether the main window displays a shadow. This API uses a promise to return the result. By default, the main window displays a shadow unless you explicitly change it with this API.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.SET_WINDOW_TRANSPARENT

<!--Device-Window-setWindowShadowEnabled(enable: boolean): Promise<void>--><!--Device-Window-setWindowShadowEnabled(enable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## setWindowShadowRadius

```TypeScript
setWindowShadowRadius(radius: number): void
```

Sets the blur radius of the shadow on the edges of a child window or floating window.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setWindowShadowRadius(radius: double): void--><!--Device-Window-setWindowShadowRadius(radius: double): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| radius | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setWindowSystemBarEnable

```TypeScript
setWindowSystemBarEnable(names: Array<'status' | 'navigation'>, callback: AsyncCallback<void>): void
```

&lt;!--RP14--&gt;Sets whether to show the status bar and three-button navigation bar in the main window. The visibility of the status bar and three-button navigation bar is controlled by **status** and **navigation**, respectively.&lt;!--RP14End--&gt; This API uses an asynchronous callback to return the result. From API version 12, &lt;!--RP5--&gt;this API does not take effect on 2-in-1 devices.&lt;!--RP5End--&gt; The return value does not indicate that the status bar and &lt;!--RP15--&gt;three-button navigation bar&lt;!--RP15End--&gt; are shown or hidden. This API does not take effect when it is called by a child window. The configuration does not take effect in non-full-screen mode (such as floating window or split-screen mode).

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [setWindowSystemBarEnable](#setWindowSystemBarEnable)(names: Array&lt;'status' | 'navigation'&gt;)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-setWindowSystemBarEnable(names: Array<'status' | 'navigation'>, callback: AsyncCallback<void>): void--><!--Device-Window-setWindowSystemBarEnable(names: Array<'status' | 'navigation'>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| names | Array & lt;'status' \ | 'navigation' & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setWindowSystemBarEnable

```TypeScript
setWindowSystemBarEnable(names: Array<'status'|'navigation'>): Promise<void>
```

&lt;!--RP14--&gt;Sets whether to show the status bar and three-button navigation bar in the main window. The visibility of the status bar and three-button navigation bar is controlled by **status** and **navigation**, respectively.&lt;!--RP14End--&gt; This API uses a promise to return the result. The return value does not indicate that the status bar and &lt;!--RP15--&gt;three-button navigation bar&lt;!--RP15End--&gt; are shown or hidden. The setting does not take effect when the main window is in non-full-screen or non-maximized mode (such as floating windows or split-screen mode). It takes effect once the main window enters full-screen or maximized mode.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-setWindowSystemBarEnable(names: Array<'status'|'navigation'>): Promise<void>--><!--Device-Window-setWindowSystemBarEnable(names: Array<'status'|'navigation'>): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| names | Array & lt;'status' \ | 'navigation' & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setWindowSystemBarProperties

```TypeScript
setWindowSystemBarProperties(systemBarProperties: SystemBarProperties, callback: AsyncCallback<void>): void
```

Sets the properties of the &lt;!--Del--&gt;three-button navigation bar and &lt;!--DelEnd--&gt;status bar of the main window. This API uses an asynchronous callback to return the result. &lt;!--RP5--&gt;This API does not take effect on 2-in-1 devices.&lt;!--RP5End--&gt; This API does not take effect when it is called by a child window.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [setWindowSystemBarProperties](#setWindowSystemBarProperties)(systemBarProperties: SystemBarProperties)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-setWindowSystemBarProperties(systemBarProperties: SystemBarProperties, callback: AsyncCallback<void>): void--><!--Device-Window-setWindowSystemBarProperties(systemBarProperties: SystemBarProperties, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| systemBarProperties | [SystemBarProperties](arkts-arkui-window-systembarproperties-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setWindowSystemBarProperties

```TypeScript
setWindowSystemBarProperties(systemBarProperties: SystemBarProperties): Promise<void>
```

Sets the properties of the &lt;!--Del--&gt;three-button navigation bar and &lt;!--DelEnd--&gt;status bar of the main window. This API uses a promise to return the result. This API does not take effect when it is called by a child window. The setting does not take effect when the main window is in non-full-screen or non-maximized mode (such as floating windows or split-screen mode). It takes effect once the main window enters full-screen or maximized mode.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-setWindowSystemBarProperties(systemBarProperties: SystemBarProperties): Promise<void>--><!--Device-Window-setWindowSystemBarProperties(systemBarProperties: SystemBarProperties): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| systemBarProperties | [SystemBarProperties](arkts-arkui-window-systembarproperties-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setWindowTitle

```TypeScript
setWindowTitle(titleName: string): Promise<void>
```

Sets the window title. This API uses a promise to return the result. In the stage model, this API must be used after the call of [loadContent](#loadContent) or [setUIContent()](#setUIContent) takes effect.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setWindowTitle(titleName: string): Promise<void>--><!--Device-Window-setWindowTitle(titleName: string): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [titleName](../../apis-avsession-kit/arkts-apis/arkts-avsession-avmusictemplate-qrcodeinfo-i.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setWindowTitleButtonVisible

```TypeScript
setWindowTitleButtonVisible(isMaximizeButtonVisible: boolean, isMinimizeButtonVisible: boolean, isCloseButtonVisible?: boolean): void
```

Shows or hides the maximize, minimize, and close buttons on the title bar of the main window.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setWindowTitleButtonVisible(isMaximizeButtonVisible: boolean, isMinimizeButtonVisible: boolean, isCloseButtonVisible?: boolean): void--><!--Device-Window-setWindowTitleButtonVisible(isMaximizeButtonVisible: boolean, isMinimizeButtonVisible: boolean, isCloseButtonVisible?: boolean): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isMaximizeButtonVisible | boolean | Yes |
| isMinimizeButtonVisible | boolean | Yes |
| isCloseButtonVisible | boolean | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setWindowTitleMoveEnabled

```TypeScript
setWindowTitleMoveEnabled(enabled: boolean): void
```

Enables or disables the capability to move the window (either main window or child window) by dragging its title bar and to maximize the window with a double-click. When this capability is disabled, you can use [startMoving()](#startMoving) to move the window by dragging in the application's hot zone and use [maximize()](#maximize) to maximize the window. In the stage model, this API must be used after the call of [loadContent](#loadContent) or [setUIContent()](#setUIContent) takes effect.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setWindowTitleMoveEnabled(enabled: boolean): void--><!--Device-Window-setWindowTitleMoveEnabled(enabled: boolean): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setWindowTopmost

```TypeScript
setWindowTopmost(isWindowTopmost: boolean): Promise<void>
```

Places the main window above all the other windows of the application. This API uses a promise to return the result. Applications use custom shortcut keys to pin or unpin the main window.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.WINDOW_TOPMOST

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setWindowTopmost(isWindowTopmost: boolean): Promise<void>--><!--Device-Window-setWindowTopmost(isWindowTopmost: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isWindowTopmost | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## setWindowTouchable

```TypeScript
setWindowTouchable(isTouchable: boolean): Promise<void>
```

Sets whether this window is touchable. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-setWindowTouchable(isTouchable: boolean): Promise<void>--><!--Device-Window-setWindowTouchable(isTouchable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isTouchable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setWindowTouchable

```TypeScript
setWindowTouchable(isTouchable: boolean, callback: AsyncCallback<void>): void
```

Sets whether this window is touchable. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-setWindowTouchable(isTouchable: boolean, callback: AsyncCallback<void>): void--><!--Device-Window-setWindowTouchable(isTouchable: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isTouchable | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setWindowTransitionAnimation

```TypeScript
setWindowTransitionAnimation(transitionType: WindowTransitionType, animation: TransitionAnimation): Promise<void>
```

Adds a transition animation to windows in specific scenarios. Currently, this API can be used only on the main window of an application.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-setWindowTransitionAnimation(transitionType: WindowTransitionType, animation: TransitionAnimation): Promise<void>--><!--Device-Window-setWindowTransitionAnimation(transitionType: WindowTransitionType, animation: TransitionAnimation): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| transitionType | [WindowTransitionType](arkts-arkui-window-windowtransitiontype-e.md) | Yes |
| animation | [TransitionAnimation](arkts-arkui-window-transitionanimation-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## show

```TypeScript
show(callback: AsyncCallback<void>): void
```

Shows this window. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [showWindow](#showWindow)(callback: AsyncCallback&lt;void&gt;)

<!--Device-Window-show(callback: AsyncCallback<void>): void--><!--Device-Window-show(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## show

```TypeScript
show(): Promise<void>
```

Shows this window. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [showWindow](#showWindow)()

<!--Device-Window-show(): Promise<void>--><!--Device-Window-show(): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## showWindow

```TypeScript
showWindow(callback: AsyncCallback<void>): void
```

Shows this window. This API uses an asynchronous callback to return the result. This API takes effect only for a system window, application child window, modal window, or global floating window. For the main window of an application, this API moves it at the top when the main window is already displayed. > **NOTE：**> > Before calling this API, you are advised to load the page by using > [loadContent](#loadContent) or > [setUIContent](#setUIContent). If the main window has not > finished loading and you call this API directly, the starting window keeps showing. Similarly, if the system > window, application child window, modal window, or global floating window has finished loading and you call > this API directly, the window is in the foreground but is not visible.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-showWindow(callback: AsyncCallback<void>): void--><!--Device-Window-showWindow(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## showWindow

```TypeScript
showWindow(): Promise<void>
```

Shows this window. This API uses a promise to return the result. This API takes effect only for a system window, application child window, modal window, or global floating window. For the main window of an application, this API moves it at the top when the main window is already displayed. > **NOTE：**> > Before calling this API, you are advised to load the page by using > [loadContent](#loadContent) or > [setUIContent](#setUIContent). If the main window has not > finished loading and you call this API directly, the starting window keeps showing. Similarly, if the system > window, application child window, modal window, or global floating window has finished loading and you call > this API directly, the window is in the foreground but is not visible.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Window-showWindow(): Promise<void>--><!--Device-Window-showWindow(): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## showWindow

```TypeScript
showWindow(options: ShowWindowOptions): Promise<void>
```

Shows this window or moves an already visible application main window to the top of the stack. You can pass options to control the window display behavior. This API uses a promise to return the result. This API can be used only for application child windows, application main windows, global floating windows, and system windows, excluding windows of the TYPE_DIALOG type and modal child windows (windows that have the modal property enabled via **setSubWindowModal**). > **NOTE：**> > Before calling this API, you are advised to load the page by using > [loadContent](#loadContent) or > [setUIContent](#setUIContent). If the main window has not > finished loading and you call this API directly, the starting window keeps showing. Similarly, if the system > window, application child window, or global floating window has finished loading and you call this API directly > , the window is in the foreground but is not visible.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-showWindow(options: ShowWindowOptions): Promise<void>--><!--Device-Window-showWindow(options: ShowWindowOptions): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ShowWindowOptions](arkts-arkui-window-showwindowoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## snapshot

```TypeScript
snapshot(callback: AsyncCallback<image.PixelMap>): void
```

Captures this window. This API uses an asynchronous callback to return the result. If privacy mode is enabled for the current window (using [setWindowPrivacyMode](#setWindowPrivacyMode) ), taking a screenshot will result in a blank screen.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-snapshot(callback: AsyncCallback<image.PixelMap>): void--><!--Device-Window-snapshot(callback: AsyncCallback<image.PixelMap>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## snapshot

```TypeScript
snapshot(): Promise<image.PixelMap>
```

Captures this window. If privacy mode is enabled for the current window (using [setWindowPrivacyMode](#setWindowPrivacyMode) ), taking a screenshot will result in a blank screen.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Window-snapshot(): Promise<image.PixelMap>--><!--Device-Window-snapshot(): Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## snapshotIgnorePrivacy

```TypeScript
snapshotIgnorePrivacy(): Promise<image.PixelMap>
```

Captures this window. This API can be called to obtain the screenshot of the current window even if privacy mode is enabled for the current window (using [setWindowPrivacyMode](#setWindowPrivacyMode) ).

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-snapshotIgnorePrivacy(): Promise<image.PixelMap>--><!--Device-Window-snapshotIgnorePrivacy(): Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## snapshotSync

```TypeScript
snapshotSync(): image.PixelMap
```

Captures this window. This API returns the result synchronously. If privacy mode is enabled for the current window (using [setWindowPrivacyMode](#setWindowPrivacyMode) ), taking a screenshot will result in a blank screen. In the stage model, this API must be used after the call of [loadContent](#loadContent) or [setUIContent()](#setUIContent) takes effect.

**Since:** 23

**Deprecated since:** -1

<!--Device-Window-snapshotSync(): image.PixelMap--><!--Device-Window-snapshotSync(): image.PixelMap-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| image.PixelMap |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300018](../errorcode-window.md#1300018-api-call-timeout) |

## startMoving

```TypeScript
startMoving(): Promise<void>
```

In [freeform window](../../../windowmanager/window-terminology.md#freeform-window) mode, this API takes effect for system windows, application main windows, application child windows, global floating windows, and modal windows. In non-freeform window mode, this API takes effect only for system windows, application child windows, global floating windows, and modal windows. Starts moving this window. This API uses a promise to return the result. The window moves along with the cursor or touch point only when this API is called in the callback function of onTouch, where the event type is **TouchType.Down**. In click-and-drag scenarios, if you do not want the drag to start as soon as you press down, you can call this API when the event type is [TouchType.Move](arkts-arkui-touchtype-e.md#TouchType) (as long as **TouchType.Down** has already been triggered) to start the moving effect.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-startMoving(): Promise<void>--><!--Device-Window-startMoving(): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300001](../errorcode-window.md#1300001-repeated-operation) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## startMoving

```TypeScript
startMoving(offsetX: number, offsetY: number): Promise<void>
```

Specifies the cursor position within the window and moves the window. This API uses a promise to return the result. When windows within the same application are split or merged, and the mouse is pressed down to move the new window directly, the cursor may move outside the window if it moves too quickly. This API allows you to set the cursor position within the window during movement. It first adjusts the window to the cursor position before starting to move the window. The window moves along with the cursor only when this API is called in the callback function of onTouch, where the event type is **TouchType.Down**. In click-and-drag scenarios, if you do not want the drag to start as soon as you press down, you can call this API when the event type is [TouchType.Move](arkts-arkui-touchtype-e.md#TouchType) (as long as **TouchType.Down** has already been triggered) to start the moving effect.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-startMoving(offsetX: int, offsetY: int): Promise<void>--><!--Device-Window-startMoving(offsetX: int, offsetY: int): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offsetX | number | Yes |
| offsetY | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300001](../errorcode-window.md#1300001-repeated-operation) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## stopMoving

```TypeScript
stopMoving(): Promise<void>
```

Stops window movement when a window is being dragged. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Window-stopMoving(): Promise<void>--><!--Device-Window-stopMoving(): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
