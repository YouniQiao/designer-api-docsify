# FloatViewController

Defines a float view controller instance, which is used to start and stop the float view and register callbacks.Before calling the following APIs, you must use [floatView.create()](arkts-arkui-floatview-create-f.md) to create a float view controller instance (that is, **floatViewController**).

**Since:** 26.0.0

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { floatView } from 'kits/@kit.ArkUI';
```

## getWindowProperties

```TypeScript
getWindowProperties(): FloatViewProperties
```

Obtains the properties of the float view.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FloatViewProperties](arkts-arkui-floatview-floatviewproperties-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300031](../errorcode-window.md#1300031-operation-not-supported-in-the-current-float-view-state) |

## offLimitsChange

```TypeScript
offLimitsChange(callback?: Callback<FloatViewLimits>): void
```

Unregisters the callback for listening to limit changes of the float view.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FloatViewLimits](arkts-arkui-floatview-floatviewlimits-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## offRectChange

```TypeScript
offRectChange(callback?: Callback<FloatViewRectChangeInfo>): void
```

Unregisters the callback for listening to changes in the rectangular area of the float view.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FloatViewRectChangeInfo](arkts-arkui-floatview-floatviewrectchangeinfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## offStateChange

```TypeScript
offStateChange(callback?: Callback<FloatViewStateChangeInfo>): void
```

Unregisters the callback for listening to float view state changes.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FloatViewStateChangeInfo](arkts-arkui-floatview-floatviewstatechangeinfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## onLimitsChange

```TypeScript
onLimitsChange(callback: Callback<FloatViewLimits>): void
```

Registers a callback for listening to limit changes of the float view. When the limit changes, for example, when the device is folded or unfolded, the callback is triggered. To prevent memory leaks, remember to unregister the callback when it is no longer needed.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FloatViewLimits](arkts-arkui-floatview-floatviewlimits-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300030](../errorcode-window.md#1300030-repeated-operations-on-the-float-view) |

## onRectChange

```TypeScript
onRectChange(callback: Callback<FloatViewRectChangeInfo>): void
```

Registers a callback for listening to changes in the rectangular area (position and size) of the float view. To prevent memory leaks, remember to unregister the callback when it is no longer needed.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FloatViewRectChangeInfo](arkts-arkui-floatview-floatviewrectchangeinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300030](../errorcode-window.md#1300030-repeated-operations-on-the-float-view) |

## onStateChange

```TypeScript
onStateChange(callback: Callback<FloatViewStateChangeInfo>): void
```

Registers a callback for listening to float view state changes. To prevent memory leaks, remember to unregister the callback when it is no longer needed.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FloatViewStateChangeInfo](arkts-arkui-floatview-floatviewstatechangeinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300030](../errorcode-window.md#1300030-repeated-operations-on-the-float-view) |

## restoreMainWindow

```TypeScript
restoreMainWindow(wantParameters?: Record<string, Object>): Promise<void>
```

Restores the main window of the float view to display in the foreground. If this API is called when the main window is already in the foreground, the main window level will be raised. This API can be used only after the float view is clicked. If the main window is in the **PAUSED** state or in the multitasking state, error code 130 0032 will be returned if this API is called. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [wantParameters](../../apis-notification-kit/arkts-apis/arkts-notification-notificationrequest-notificationparameters-i.md) | Record & lt;string, Object & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300031](../errorcode-window.md#1300031-operation-not-supported-in-the-current-float-view-state) |
| [1300032](../errorcode-window.md#1300032-failed-to-restore-the-main-window) |

## setFloatViewVisibilityInApp

```TypeScript
setFloatViewVisibilityInApp(isVisible: boolean): Promise<void>
```

Sets whether the float view is visible when the application is running in the foreground. This API uses a promise to return the result.After the float view is created and before this API is called, the float view is visible by default when the application is running in the foreground.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isVisible | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |

## setUIContext

```TypeScript
setUIContext(path: string, storage?: LocalStorage): Promise<void>
```

Loads the content of a page, with its path specified in the current project, for the float view, and transfers the state attribute to the page through **LocalStorage**. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| storage | [LocalStorage](arkts-arkui-localstorage-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |

## setUIContextByName

```TypeScript
setUIContextByName(name: string, storage?: LocalStorage): Promise<void>
```

Sets the UI content of a [named route](../../../ui/arkts-routing.md#named-route) page to this float view window.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

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
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |

## setWindowSize

```TypeScript
setWindowSize(size: window.Size): Promise<void>
```

Sets the size of the float view. You are advised to call the [getFloatViewLimits](arkts-arkui-floatview-getfloatviewlimits-f.md) API to obtain the recommended width and height ranges and aspect ratio range, and then call this API based on the recommended values. The actual window size change can be listened to through the [onRectChange](#onrectchange) API. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | window.Size | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |

## start

```TypeScript
start(): Promise<void>
```

Starts the float view. The return value of this API does not indicate that the start process is complete. You need to use the [onStateChange](#onstatechange) API to listen for the **STARTED** callback to determine whether the start is successful. You are advised to call **start ()** after calling [setUIContext()](#setuicontext). This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.FLOAT_VIEW

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300030](../errorcode-window.md#1300030-repeated-operations-on-the-float-view) |
| [1300031](../errorcode-window.md#1300031-operation-not-supported-in-the-current-float-view-state) |
| [1300033](../errorcode-window.md#1300033-failed-to-start-the-float-view) |
| [1300034](../errorcode-window.md#1300034-operation-of-the-float-view-conflicts-with-those-of-other-floating-windows) |

## stop

```TypeScript
stop(): Promise<void>
```

Stops the float view. The return value of this API does not indicate that the stop process is complete. You need to use the [onStateChange](#onstatechange) API to listen for the **STOPPED** callback to determine whether the stop is successful. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300030](../errorcode-window.md#1300030-repeated-operations-on-the-float-view) |
| [1300031](../errorcode-window.md#1300031-operation-not-supported-in-the-current-float-view-state) |

## switchTemplate

```TypeScript
switchTemplate(templateProperty: TemplateProperty): Promise<void>
```

Switches the template of the flow view and changes the window size. You are advised to call the [getFloatViewLimits](arkts-arkui-floatview-getfloatviewlimits-f.md) API to obtain the recommended width and height ranges and aspect ratio range of the target template, and then call this API based on the recommended values. The actual window size change can be listened to through the [onRectChange](#onrectchange) API. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| templateProperty | [TemplateProperty](arkts-arkui-floatview-templateproperty-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
