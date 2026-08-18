# FloatViewController

Defines a float view controller instance, which is used to start and stop the float view and register callbacks. Before calling the following APIs, you must use [floatView.create()](arkts-arkui-floatview-create-f.md) to create a float view controller instance (that is, **floatViewController**).

**Since:** 26.0.0

<!--Device-floatView-interface FloatViewController--><!--Device-floatView-interface FloatViewController-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { floatView } from '@kit.ArkUI';
```

## getWindowProperties

```TypeScript
getWindowProperties(): FloatViewProperties
```

Obtains the properties of the float view.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewController-getWindowProperties(): FloatViewProperties--><!--Device-FloatViewController-getWindowProperties(): FloatViewProperties-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| [FloatViewProperties](arkts-arkui-floatview-floatviewproperties-i.md) | Properties of the float view. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The float view controller object is null. |
| [1300031](../errorcode-window.md#1300031-operation-not-supported-in-the-current-float-view-state) | This operation is not supported on the float view in the current state. Possible cause: The float view window has not started, has stopped, or is in an error state. |

## offLimitsChange

```TypeScript
offLimitsChange(callback?: Callback<FloatViewLimits>): void
```

Unregisters the callback for listening to limit changes of the float view.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewController-offLimitsChange(callback?: Callback<FloatViewLimits>): void--><!--Device-FloatViewController-offLimitsChange(callback?: Callback<FloatViewLimits>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[FloatViewLimits](arkts-arkui-floatview-floatviewlimits-i.md)&gt; | No | Callback used to return the limit change information of the current float view. If a value is passed in, the corresponding callback is unregistered. If no value is passed in, all callbacks associated with the limit change event of the float view are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The float view controller object is null. |

## offRectChange

```TypeScript
offRectChange(callback?: Callback<FloatViewRectChangeInfo>): void
```

Unregisters the callback for listening to changes in the rectangular area of the float view.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewController-offRectChange(callback?: Callback<FloatViewRectChangeInfo>): void--><!--Device-FloatViewController-offRectChange(callback?: Callback<FloatViewRectChangeInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[FloatViewRectChangeInfo](arkts-arkui-floatview-floatviewrectchangeinfo-i.md)&gt; | No | Callback used to return the rectangle area change information of the current float view. If a value is passed in, the corresponding callback is unregistered. If no value is passed in, all callbacks associated with the rectangle area change event of the float view are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The float view controller object is null. |

## offStateChange

```TypeScript
offStateChange(callback?: Callback<FloatViewStateChangeInfo>): void
```

Unregisters the callback for listening to float view state changes.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewController-offStateChange(callback?: Callback<FloatViewStateChangeInfo>): void--><!--Device-FloatViewController-offStateChange(callback?: Callback<FloatViewStateChangeInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[FloatViewStateChangeInfo](arkts-arkui-floatview-floatviewstatechangeinfo-i.md)&gt; | No | Callback used to return the status change information of the current float view. If a value is passed in, the corresponding callback is unregistered. If no value is passed in, all callbacks associated with the status change event of the float view are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The float view controller object is null. |

## onLimitsChange

```TypeScript
onLimitsChange(callback: Callback<FloatViewLimits>): void
```

Registers a callback for listening to limit changes of the float view. When the limit changes, for example, when the device is folded or unfolded, the callback is triggered. To prevent memory leaks, remember to unregister the callback when it is no longer needed.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewController-onLimitsChange(callback: Callback<FloatViewLimits>): void--><!--Device-FloatViewController-onLimitsChange(callback: Callback<FloatViewLimits>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[FloatViewLimits](arkts-arkui-floatview-floatviewlimits-i.md)&gt; | Yes | Callback used to return the limit change information of the current float view. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The float view controller object is null. |
| [1300030](../errorcode-window.md#1300030-repeated-operations-on-the-float-view) | Repeated operations on the float view. Possible cause: The callback has already registered. |

## onRectChange

```TypeScript
onRectChange(callback: Callback<FloatViewRectChangeInfo>): void
```

Registers a callback for listening to changes in the rectangular area (position and size) of the float view. To prevent memory leaks, remember to unregister the callback when it is no longer needed.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewController-onRectChange(callback: Callback<FloatViewRectChangeInfo>): void--><!--Device-FloatViewController-onRectChange(callback: Callback<FloatViewRectChangeInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[FloatViewRectChangeInfo](arkts-arkui-floatview-floatviewrectchangeinfo-i.md)&gt; | Yes | Callback used to return the rectangle area change information of the current float view. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The float view controller object is null. |
| [1300030](../errorcode-window.md#1300030-repeated-operations-on-the-float-view) | Repeated operations on the float view. Possible cause: The callback has already registered. |

## onStateChange

```TypeScript
onStateChange(callback: Callback<FloatViewStateChangeInfo>): void
```

Registers a callback for listening to float view state changes. To prevent memory leaks, remember to unregister the callback when it is no longer needed.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewController-onStateChange(callback: Callback<FloatViewStateChangeInfo>): void--><!--Device-FloatViewController-onStateChange(callback: Callback<FloatViewStateChangeInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[FloatViewStateChangeInfo](arkts-arkui-floatview-floatviewstatechangeinfo-i.md)&gt; | Yes | Callback used to return the status change information of the current float view. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The float view controller object is null. |
| [1300030](../errorcode-window.md#1300030-repeated-operations-on-the-float-view) | Repeated operations on the float view. Possible cause: The callback has already registered. |

## restoreMainWindow

```TypeScript
restoreMainWindow(wantParameters?: Record<string, Object>): Promise<void>
```

Restores the main window of the float view to display in the foreground. If this API is called when the main window is already in the foreground, the main window level will be raised. This API can be used only after the float view is clicked. If the main window is in the **PAUSED** state or in the multitasking state, error code 130 0032 will be returned if this API is called. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewController-restoreMainWindow(wantParameters?: Record<string, Object>): Promise<void>--><!--Device-FloatViewController-restoreMainWindow(wantParameters?: Record<string, Object>): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| wantParameters | Record&lt;string, Object&gt; | No | Custom parameters passed to the main window when the main window of the float view is restored. The main window will receive the parameters when the onNewWant callback is triggered. The default value is empty, indicating that no custom parameters are passed to the main window. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) | This window manager service works abnormally. Possible cause: Internal IPC error. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The float view controller object is null. |
| [1300032](../errorcode-window.md#1300032-failed-to-restore-the-main-window) | Failed to restore the main window. Possible cause: 1. User has never clicked the float view window before restore. 2. The float view window is not in the foreground. 3. The main window is in PAUSED lifecycle state. 4. The main window is in background during recent. |
| [1300031](../errorcode-window.md#1300031-operation-not-supported-in-the-current-float-view-state) | This operation is not supported on the float view in the current state. Possible cause: The float view window is not started when restoring. |

## setFloatViewVisibilityInApp

```TypeScript
setFloatViewVisibilityInApp(isVisible: boolean): Promise<void>
```

Sets whether the float view is visible when the application is running in the foreground. This API uses a promise to return the result. After the float view is created and before this API is called, the float view is visible by default when the application is running in the foreground.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewController-setFloatViewVisibilityInApp(isVisible: boolean): Promise<void>--><!--Device-FloatViewController-setFloatViewVisibilityInApp(isVisible: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isVisible | boolean | Yes | Whether the float view is visible when the application is running in the foreground. The value **true** indicates that the window is visible, and **false** indicates the opposite. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) | This window manager service works abnormally. Possible cause: Internal IPC error. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The float view controller object is null. |

## setUIContext

```TypeScript
setUIContext(path: string, storage?: LocalStorage): Promise<void>
```

Loads the content of a page, with its path specified in the current project, for the float view, and transfers the state attribute to the page through **LocalStorage**. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewController-setUIContext(path: string, storage?: LocalStorage): Promise<void>--><!--Device-FloatViewController-setUIContext(path: string, storage?: LocalStorage): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Path of the page content which needs to be loaded to the window. The path needs to be configured in the **main_pages.json** file of the project. The path cannot be a relative path and must be the same as the value of **src** in the **main_pages.json** file. |
| storage | LocalStorage | No | Page-level UI state storage unit, which is used to transfer the state attribute for the page. By default, the value is empty. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The float view controller object is null. |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) | Parameter error. Possible causes: Invalid path. |

## setUIContextByName

```TypeScript
setUIContextByName(name: string, storage?: LocalStorage): Promise<void>
```

Sets the UI content of a [named route](../../../ui/arkts-routing.md#named-route) page to this float view window.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewController-setUIContextByName(name: string, storage?: LocalStorage): Promise<void>--><!--Device-FloatViewController-setUIContextByName(name: string, storage?: LocalStorage): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the named route page. |
| storage | LocalStorage | No | The data object shared within the content instance loaded by the window. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The float view controller object is null. |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) | Parameter error. Possible causes: Invalid name. |

## setWindowSize

```TypeScript
setWindowSize(size: window.Size): Promise<void>
```

Sets the size of the float view. You are advised to call the [getFloatViewLimits](arkts-arkui-floatview-getfloatviewlimits-f.md) API to obtain the recommended width and height ranges and aspect ratio range, and then call this API based on the recommended values. The actual window size change can be listened to through the [onRectChange](#onrectchange) API. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewController-setWindowSize(size: window.Size): Promise<void>--><!--Device-FloatViewController-setWindowSize(size: window.Size): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | window.Size | Yes | Window size. It is recommended that the size meet the limits returned by the [getFloatViewLimits](arkts-arkui-floatview-getfloatviewlimits-f.md) API. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) | This window manager service works abnormally. Possible cause: Internal IPC error. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The float view controller object is null. |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) | Parameter error. Possible cause: The value of the size is less than or equal to 0. |

## start

```TypeScript
start(): Promise<void>
```

Starts the float view. The return value of this API does not indicate that the start process is complete. You need to use the [onStateChange](#onstatechange) API to listen for the **STARTED** callback to determine whether the start is successful. You are advised to call **start ()** after calling [setUIContext()](#setuicontext). This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.FLOAT_VIEW

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewController-start(): Promise<void>--><!--Device-FloatViewController-start(): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) | This window manager service works abnormally. Possible cause: Internal IPC error. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The float view controller object is null. |
| [1300034](../errorcode-window.md#1300034-operation-of-the-float-view-conflicts-with-those-of-other-floating-windows) | This operation conflicts with other floating windows. Possible cause: App has already started floating ball or pip window. |
| [1300033](../errorcode-window.md#1300033-failed-to-start-the-float-view) | Failed to start float view. Possible causes: 1. Start multiple float views. 2. The main window of context is not foreground. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. Possible cause: The application does not have the permission required to call the API. |
| [1300031](../errorcode-window.md#1300031-operation-not-supported-in-the-current-float-view-state) | The float view state does not support this operation. Possible cause: The float view is stopping. |
| [1300030](../errorcode-window.md#1300030-repeated-operations-on-the-float-view) | Repeated operations on the float view. Possible cause: The float view is starting or has already started. |

## stop

```TypeScript
stop(): Promise<void>
```

Stops the float view. The return value of this API does not indicate that the stop process is complete. You need to use the [onStateChange](#onstatechange) API to listen for the **STOPPED** callback to determine whether the stop is successful. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewController-stop(): Promise<void>--><!--Device-FloatViewController-stop(): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) | This window manager service works abnormally. Possible cause: Internal IPC error. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The float view controller object is null. |
| [1300031](../errorcode-window.md#1300031-operation-not-supported-in-the-current-float-view-state) | This operation is not supported on the float view in the current state. Possible cause: The float view window is not started. |
| [1300030](../errorcode-window.md#1300030-repeated-operations-on-the-float-view) | Repeated operations on the float view. Possible cause: The float view is stopping or has already stopped. |

## switchTemplate

```TypeScript
switchTemplate(templateProperty: TemplateProperty): Promise<void>
```

Switches the template of the flow view and changes the window size. You are advised to call the [getFloatViewLimits](arkts-arkui-floatview-getfloatviewlimits-f.md) API to obtain the recommended width and height ranges and aspect ratio range of the target template, and then call this API based on the recommended values. The actual window size change can be listened to through the [onRectChange](#onrectchange) API. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-FloatViewController-switchTemplate(templateProperty: TemplateProperty): Promise<void>--><!--Device-FloatViewController-switchTemplate(templateProperty: TemplateProperty): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| templateProperty | [TemplateProperty](arkts-arkui-floatview-templateproperty-i.md) | Yes | Target flow view template and window size. It is recommended that the size meet the limits returned by the [getFloatViewLimits](arkts-arkui-floatview-getfloatviewlimits-f.md) API. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) | This window manager service works abnormally. Possible cause: Internal IPC error. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The float view controller object is null. |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) | Parameter error. Possible cause: 1. Invalid template type. 2. The value of the size is less than or equal to 0. |

