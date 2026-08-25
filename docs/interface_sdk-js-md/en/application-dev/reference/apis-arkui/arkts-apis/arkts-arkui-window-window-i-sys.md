# Window

Represents a window instance, which is the basic unit managed by the window manager.In the following API examples, you must use [getLastWindow()](arkts-arkui-window-getlastwindow-f.md), [createWindow()](arkts-arkui-window-createwindow-f.md), or [findWindow()](arkts-arkui-window-findwindow-f.md) to obtain a Window instance (named windowClass in this example) and then call a method in this instance.

**Since:** 6

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## attachLayoutToParentWindow

```TypeScript
attachLayoutToParentWindow(anchorInfo?: WindowAnchorInfo, attachOptions?: SubWindowAttachOptions): Promise<void>
```

Attaches a first-level child window to the main window to maintain a fixed relative position. This API uses a promise to return the result. The relative position is represented by the anchor point offset between the child window and the parent window. The child window and the parent window use the same window anchor point.

> **NOTE：**&gt;
> - Only first-level child windows can call this API. The child window must be in floating window mode
> (that is, the window mode is **window.WindowStatusType.FLOATING**).&gt;
> - After the child window calls this API, the display position of the child window immediately follows the
> main window and the relative position remains unchanged. In addition, the size and mode changes of the main
> window can be listened to. The effect will persist unless the
> [detachLayoutToParentWindow()](#detachlayouttoparentwindow) API is called for detaching.&gt;
> -After the child window calls this API, calling APIs such as
> [moveWindowTo()](arkts-arkui-window-window-i.md#movewindowto),
> [maximize()](arkts-arkui-window-window-i.md#maximize), and
> [setFollowParentWindowLayoutEnabled()](arkts-arkui-window-window-i.md#setfollowparentwindowlayoutenabled)
> to change the window position, or dragging and moving or dragging and resizing the child window through mouse
> or touch operations will not take effect.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| anchorInfo | [WindowAnchorInfo](arkts-arkui-window-windowanchorinfo-i-sys.md) | No |
| attachOptions | [SubWindowAttachOptions](arkts-arkui-window-subwindowattachoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [1300010](../errorcode-window.md#1300010-unsupported-operation-in-the-current-window-mode) |

## bindDialogTarget

```TypeScript
bindDialogTarget(token: rpc.RemoteObject, deathCallback: Callback<void>): Promise<void>
```

Binds the modal window to the target window. After the binding is successful, the target window cannot respond to user operations. In addition, a callback used to listen for modal window destruction events is added. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| token | rpc.RemoteObject | Yes |
| deathCallback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |

## bindDialogTarget

```TypeScript
bindDialogTarget(token: rpc.RemoteObject, deathCallback: Callback<void>, callback: AsyncCallback<void>): void
```

Binds the modal window to the target window. After the binding is successful, the target window cannot respond to user operations. In addition, a callback used to listen for modal window destruction events is added. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| token | rpc.RemoteObject | Yes |
| deathCallback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |

## bindDialogTarget

```TypeScript
bindDialogTarget(requestInfo: dialogRequest.RequestInfo, deathCallback: Callback<void>): Promise<void>
```

Binds the modal window to the target window. After the binding is successful, the target window cannot respond to user operations. In addition, a callback used to listen for modal window destruction events is added. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| requestInfo | dialogRequest.RequestInfo | Yes |
| deathCallback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |

## bindDialogTarget

```TypeScript
bindDialogTarget(requestInfo: dialogRequest.RequestInfo, deathCallback: Callback<void>, callback: AsyncCallback<void>): void
```

Binds the modal window to the target window. After the binding is successful, the target window cannot respond to user operations. In addition, a callback used to listen for modal window destruction events is added. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| requestInfo | dialogRequest.RequestInfo | Yes |
| deathCallback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |

## detachLayoutToParentWindow

```TypeScript
detachLayoutToParentWindow(): Promise<void>
```

Detach a first-level child window from the main window to cancel a fixed relative position. This API uses a promise to return the result.

> **NOTE：**&gt;
> - When the child window calls this API, the child window must be in the attached state.&gt;
> - After detached by calling this API, the child window retains its position during attaching.
> You can drag the child window to change its size and position.&gt;
> - After the detaching, calling APIs such as
> [moveWindowTo()](arkts-arkui-window-window-i.md#movewindowto) or
> [maximize()](arkts-arkui-window-window-i.md#maximize), and
> [setFollowParentWindowLayoutEnabled()](arkts-arkui-window-window-i.md#setfollowparentwindowlayoutenabled)
> to change the window position, or dragging and moving or dragging and resizing the child window through mouse
> or touch operations will take effect.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [1300010](../errorcode-window.md#1300010-unsupported-operation-in-the-current-window-mode) |

## getRotationLocked

```TypeScript
getRotationLocked(): boolean
```

Checks whether the [system window](../../../windowmanager/window-terminology.md#system-window) has its screen rotation locked. If this API is called by a non-system window, error code 1300029 is thrown.

**Since:** 22

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| 1300029 |

## getTransitionController

```TypeScript
getTransitionController(): TransitionController
```

Obtains the transition animation controller.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TransitionController](arkts-arkui-window-transitioncontroller-i-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## hide

```TypeScript
hide (callback: AsyncCallback<void>): void
```

Hides this window. This API uses an asynchronous callback to return the result. This API takes effect only for a system window or an application child window.

**Since:** 7

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## hide

```TypeScript
hide(): Promise<void>
```

Hides this window. This API uses a promise to return the result. This API takes effect only for a system window or an application child window.

**Since:** 7

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## hideNonSystemFloatingWindows

```TypeScript
hideNonSystemFloatingWindows(shouldHide: boolean, callback: AsyncCallback<void>): void
```

Sets whether to hide non-system floating windows (where [windowType](arkts-arkui-window-windowtype-e.md) is **TYPE_FLOAT**). This API uses an asynchronous callback to return the result.A non-system floating window is a floating window created by a non-system application. By default, the main window of a system application can be displayed together with a non-system floating window. This means that the main window may be blocked by an upper-layer non-system floating window. If the **shouldHide** parameter is set to **true**, all non-system floating windows are hidden, so that the main window will never be blocked by a non- system floating window.

**Since:** 11

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| shouldHide | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## hideNonSystemFloatingWindows

```TypeScript
hideNonSystemFloatingWindows(shouldHide: boolean): Promise<void>
```

Sets whether to hide non-system floating windows (where [windowType](arkts-arkui-window-windowtype-e.md) is **TYPE_FLOAT**). This API uses a promise to return the result.A non-system floating window is a floating window created by a non-system application. By default, the main window of a system application can be displayed together with a non-system floating window. This means that the main window may be blocked by an upper-layer non-system floating window. If the **shouldHide** parameter is set to **true**, all non-system floating windows are hidden, so that the main window will never be blocked by a non- system floating window.

**Since:** 11

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| shouldHide | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## hideWithAnimation

```TypeScript
hideWithAnimation(callback: AsyncCallback<void>): void
```

Hides this window and plays an animation during the process. This API uses an asynchronous callback to return the result. This API takes effect only for a system window.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## hideWithAnimation

```TypeScript
hideWithAnimation(): Promise<void>
```

Hides this window and plays an animation during the process. This API uses a promise to return the result. This API takes effect only for a system window.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## isMainWindowFullScreenAcrossDisplays

```TypeScript
isMainWindowFullScreenAcrossDisplays(): Promise<boolean>
```

Checks whether the main window is in full-screen mode across multiple displays. This API uses a promise to return the result. It takes effect only for the main window and child windows.

**Since:** 20

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## off('mainWindowFullScreenAcrossDisplaysChanged')

```TypeScript
off(type: 'mainWindowFullScreenAcrossDisplaysChanged', callback?: Callback<boolean>): void
```

Unsubscribes from events indicating whether the main window is in full-screen mode across multiple displays.

**Since:** 20

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'mainWindowFullScreenAcrossDisplaysChanged' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## on('mainWindowFullScreenAcrossDisplaysChanged')

```TypeScript
on(type: 'mainWindowFullScreenAcrossDisplaysChanged', callback: Callback<boolean>): void
```

Subscribes to events indicating whether the main window is in full-screen mode across multiple displays.

**Since:** 20

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'mainWindowFullScreenAcrossDisplaysChanged' | Yes |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## opacity

```TypeScript
opacity(opacity: number): void
```

Sets the opacity for this window. This API can be used only when you [customize an animation to be played during the display or hiding of a system window](../../../windowmanager/system-window-stage-sys.md#customizing-an-animation-to-be-played-during-the-display-or-hiding-of-a-system-window).

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [opacity](#opacity) | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## raiseAboveTarget

```TypeScript
raiseAboveTarget(windowId: number, callback: AsyncCallback<void>): void
```

Raises a child window above a target child window. This API uses an asynchronous callback to return the result.Before calling this API, ensure that the child window to raise and the target child window have been created and [showWindow()](arkts-arkui-window-window-i.md#showwindow) has been successfully executed for each.

**Since:** 10

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [1300009](../errorcode-window.md#1300009-invalid-parent-window) |

## raiseAboveTarget

```TypeScript
raiseAboveTarget(windowId: number): Promise<void>
```

Raises a child window above a target child window. This API uses a promise to return the result.Before calling this API, ensure that the child window to raise and the target child window have been created and [showWindow()](arkts-arkui-window-window-i.md#showwindow) has been successfully executed for each.

**Since:** 10

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

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
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [1300009](../errorcode-window.md#1300009-invalid-parent-window) |

## raiseMainWindowAboveTarget

```TypeScript
raiseMainWindowAboveTarget(windowId: number): Promise<void>
```

Moves the main window above another main window within the same application, with child windows following their parents' layer change. This API uses a promise to return the result.This API can be called only by the main window of a system application.You need to pass the ID of the target main window. Both the calling window and the target window must be in the same application process, displayed on the same physical screen, below the lock screen layer, not topmost, not modal, and have no application-modal child windows.  
- If the application's main window or its child windows currently have focus, calling this API to lower the layer  
will cause the window to lose focus automatically, and the highest-layered application window will gain focus.  
- If the main window calls this API to move above the current focused window, the highest-layered window among  
the raised main window and its child windows will gain focus. If the main window calls this API without moving above the current focused window, the focus remains unchanged.

**Since:** 20

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

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
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |

## raiseToAppTop

```TypeScript
raiseToAppTop(callback: AsyncCallback<void>): void
```

Raises the application child window to the top layer of the application. This API uses an asynchronous callback to return the result.Before calling this API, ensure that the child window has been created and [showWindow()](arkts-arkui-window-window-i.md#showwindow) has been successfully executed.

**Since:** 10

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [1300009](../errorcode-window.md#1300009-invalid-parent-window) |

## requestFocus

```TypeScript
requestFocus(isFocused: boolean): Promise<void>
```

Allows this window to proactively request to gain or lose focus. This API uses a promise to return the result. A value is returned as number as the API is successfully called. The return value does not indicate that the window has gained or lost focus. You can use on('windowEvent') to listen for the focus status of the window.When a focus request is sent, whether the window can successfully gain focus depends on its capability of being focused and its current visibility. To gain focus, the window must be capable of receiving focus and in a visible state (actively displayed and not hidden or destroyed).Conversely, once a blur request is sent, the window will lose focus without any conditions.

**Since:** 13

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isFocused | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |

## rotate

```TypeScript
rotate(rotateOptions: RotateOptions): void
```

Sets the rotation parameters for this window. This API can be used only when you [customize an animation to be played during the display or hiding of a system window](../../../windowmanager/system-window-stage-sys.md#customizing-an-animation-to-be-played-during-the-display-or-hiding-of-a-system-window).

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rotateOptions | [RotateOptions](../arkts-components/arkts-arkui-rotateoptions-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## scale

```TypeScript
scale(scaleOptions: ScaleOptions): void
```

Sets the scale parameters for this window. This API can be used only when you [customize an animation to be played during the display or hiding of a system window](../../../windowmanager/system-window-stage-sys.md#customizing-an-animation-to-be-played-during-the-display-or-hiding-of-a-system-window).

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scaleOptions | [ScaleOptions](../arkts-components/arkts-arkui-scaleoptions-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setBackdropBlur

```TypeScript
setBackdropBlur(radius: number): void
```

Blurs the background of this window.The window background refers to the lower-layer area covered by the window, which is the same as the window size.To make the blur effect visible, you must set the window background transparent by calling [setWindowBackgroundColor](arkts-arkui-window-window-i.md#setwindowbackgroundcolor).

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| radius | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setBackdropBlurStyle

```TypeScript
setBackdropBlurStyle(blurStyle: BlurStyle): void
```

Sets the blur style for the background of this window.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [blurStyle](../arkts-components/arkts-arkui-sheetoptions-i.md) | [BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## setBlur

```TypeScript
setBlur(radius: number): void
```

Blurs this window.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| radius | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setCornerRadius

```TypeScript
setCornerRadius(cornerRadius: number): void
```

Sets the radius of the rounded corners for this window.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cornerRadius | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setDefaultDensityEnabled

```TypeScript
setDefaultDensityEnabled(enabled: boolean): void
```

Sets whether the window uses the default density of the current screen. In the stage model, you need to call this API after [loadContent()](arkts-arkui-window-window-i.md#loadcontent) or [setUIContent()](arkts-arkui-window-window-i.md#setuicontent).If this API is not called, the default density is not used.If this API, [setDefaultDensityEnabled(true)](arkts-arkui-window-windowstage-i.md#setdefaultdensityenabled), and [setCustomDensity](arkts-arkui-window-windowstage-i.md#setcustomdensity) are all called, the setting from the last called API will be applied.

**Since:** 20

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setForbidSplitMove

```TypeScript
setForbidSplitMove(isForbidSplitMove: boolean, callback: AsyncCallback<void>): void
```

Sets whether the main window is forbidden to move in split-screen mode. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isForbidSplitMove | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |

## setForbidSplitMove

```TypeScript
setForbidSplitMove(isForbidSplitMove: boolean): Promise<void>
```

Sets whether the main window is forbidden to move in split-screen mode. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isForbidSplitMove | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |

## setHandwritingFlag

```TypeScript
setHandwritingFlag(enable: boolean): Promise<void>
```

Adds or deletes the handwriting flag for this window. After this flag is added, the window responds to stylus events but not touch events. This API uses a promise to return the result.

**Since:** 12

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

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
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |

## setMainWindowRaiseByClickEnabled

```TypeScript
setMainWindowRaiseByClickEnabled(enable: boolean): Promise<void>
```

Sets whether to enable the main window to raise itself by click. This API uses a promise to return the result.By default, clicking the main window raises both the main window and its associated child windows. Disabling this feature (by passing **false**) prevents the main window and its child windows from being raised when the main window is clicked, preserving their current state. However, clicking on a child window still raises both the child window and the main window together.

**Since:** 23

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

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
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setRaiseByClickEnabled

```TypeScript
setRaiseByClickEnabled(enable: boolean, callback: AsyncCallback<void>): void
```

Sets whether to enable a child window to raise itself by click. This API uses an asynchronous callback to return the result.Generally, when a user clicks a child window, the child window is displayed on the top. If the **enable** parameter is set to **false**, the child window is not displayed on the top when being clicked.Before calling this API, ensure that the child window has been created and [showWindow()](arkts-arkui-window-window-i.md#showwindow) has been successfully executed.

**Since:** 10

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [1300009](../errorcode-window.md#1300009-invalid-parent-window) |

## setRotationLocked

```TypeScript
setRotationLocked(locked: boolean): Promise<void>
```

Allows a [system window](../../../windowmanager/window-terminology.md#system-window) to lock or unlock its own screen-rotation behavior. When locked, the window's orientation remains unchanged. When unlocked, the window's orientation follows the main window's orientation, the system rotation-lock button, and the device's physical rotation sensor. If this API is called by a non-system window, error code 1300029 is thrown. This API uses a promise to return the result.

> **NOTE：**&gt;
> - If the main window sets the display orientation via
> [setPreferredOrientation()](arkts-arkui-window-window-i.md#setpreferredorientation)
> while rotation is locked, the window restores the last orientation request when brought to the foreground after
> unlocking.&gt;
> - If the system window sets the display orientation via
> [setPreferredOrientation()](arkts-arkui-window-window-i.md#setpreferredorientation)
> while rotation is locked, the window restores the last orientation request when brought to the foreground with
> the highest level after unlocking. The rotation lock set by a lower-level window using **setRotationLocked**
> does not hinder the system window at a higher level to set the display orientation by calling
> [setPreferredOrientation()](arkts-arkui-window-window-i.md#setpreferredorientation)
> .&gt;
> - If the sensor orientation changes while rotation is locked, the last sensor orientation is restored after
> unlocking.&gt;
> - If the application calls
> [setOrientation()](arkts-arkui-screen-screen-i-sys.md#setorientation)
> to set the screen orientation while rotation is locked, that screen?orientation setting is ignored.&gt;
> - When rotation is unlocked, the application's display orientation is determined based on the main window's
> display orientation set via
> [setPreferredOrientation()](arkts-arkui-window-window-i.md#setpreferredorientation)
> , the sensor orientation, and more. For details, see
> [Window Rotation Overview](../../../windowmanager/window-rotation.md#overview).&gt;
> - The API does not affect the launch orientation set by the **orientation** under
> [**abilities** in the module.json5 file](../../../quick-start/module-configuration-file.md#abilities) of the
> application.

**Since:** 22

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locked | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| 1300029 |

## setShadow

```TypeScript
setShadow(radius: number, color?: string, offsetX?: number, offsetY?: number): void
```

Sets the shadow for the window borders.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| radius | number | Yes |
| color | string | No |
| offsetX | number | No |
| offsetY | number | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setSingleFrameComposerEnabled

```TypeScript
setSingleFrameComposerEnabled(enable: boolean): Promise<void>
```

Enables or disables the single-frame composer. This API uses a promise to return the result.The single-frame composer is mainly used in scenarios that require extremely low interaction latency. It reduces the screen display latency of the rendering node.

**Since:** 11

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

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
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setSnapshotSkip

```TypeScript
setSnapshotSkip(isSkip: boolean): void
```

Sets whether to ignore this window during screen capture, recording, or casting. This API is typically used in situations where you want to prevent screen capture, recording, or casting.If you want the window to always be ignored during screen capture, recording, or casting while it is in the foreground, listen for window lifecycle changes using on('windowEvent'). Set **isSkip** to **false** when the window is in the background and **true** when it is in the foreground.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isSkip | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

## setTitleButtonVisible

```TypeScript
setTitleButtonVisible(isMaximizeVisible: boolean, isMinimizeVisible: boolean, isSplitVisible: boolean): void
```

Shows or hides the maximize, minimize, and split-screen buttons on the title bar of the main window.This API takes effect only for the title bar buttons (maximize, minimize, and split-screen) that are available in the current scenario.

**Since:** 12

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isMaximizeVisible | boolean | Yes |
| isMinimizeVisible | boolean | Yes |
| isSplitVisible | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setTopmost

```TypeScript
setTopmost(isTopmost: boolean): Promise<void>
```

Called by the main window to place the window above all the other windows. This API uses a promise to return the result.

**Since:** 12

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isTopmost](arkts-arkui-window-subwindowoptions-i-sys.md) | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## setWakeUpScreen

```TypeScript
setWakeUpScreen(wakeUp: boolean): void
```

Wakes up the screen.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wakeUp | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |

## setWaterMarkFlag

```TypeScript
setWaterMarkFlag(enable: boolean, callback: AsyncCallback<void>): void
```

Adds or deletes the watermark flag for this window. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300008](../errorcode-window.md#1300008-display-device-exception) |

## setWaterMarkFlag

```TypeScript
setWaterMarkFlag(enable: boolean): Promise<void>
```

Adds or deletes the watermark flag for this window. This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300008](../errorcode-window.md#1300008-display-device-exception) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## setWindowMode

```TypeScript
setWindowMode(mode: WindowMode): Promise<void>
```

Sets the mode of the main window. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [WindowMode](../../apis-test-kit/arkts-apis/arkts-test-uitest-windowmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |

## setWindowMode

```TypeScript
setWindowMode(mode: WindowMode, callback: AsyncCallback<void>): void
```

Sets the mode of the main window. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [WindowMode](../../apis-test-kit/arkts-apis/arkts-test-uitest-windowmode-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |

## setWindowType

```TypeScript
setWindowType(type: WindowType): Promise<void>
```

Sets the type of this window. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [WindowType](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-windowtype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setWindowType

```TypeScript
setWindowType(type: WindowType, callback: AsyncCallback<void>): void
```

Sets the type of this window. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [WindowType](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-windowtype-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## showWithAnimation

```TypeScript
showWithAnimation(callback: AsyncCallback<void>): void
```

Shows this window and plays an animation during the process. This API uses an asynchronous callback to return the result. This API takes effect only for a system window.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## showWithAnimation

```TypeScript
showWithAnimation(): Promise<void>
```

Shows this window and plays an animation during the process. This API uses a promise to return the result. This API takes effect only for a system window.

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## startMovingWithOptions

```TypeScript
startMovingWithOptions(startMovingOptions?: StartMovingOptions): Promise<void>
```

Starts moving this window. The window moves along with the cursor only when this API is called in the callback function of onTouch, where the event type is TouchType.Down.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startMovingOptions | [StartMovingOptions](arkts-arkui-window-startmovingoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300001](../errorcode-window.md#1300001-repeated-operation) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |

## translate

```TypeScript
translate(translateOptions: TranslateOptions): void
```

Sets the translation parameters for this window. This API can be used only when you [customize an animation to be played during the display or hiding of a system window](../../../windowmanager/system-window-stage-sys.md#customizing-an-animation-to-be-played-during-the-display-or-hiding-of-a-system-window).

**Since:** 9

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| translateOptions | [TranslateOptions](../arkts-components/arkts-arkui-translateoptions-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
