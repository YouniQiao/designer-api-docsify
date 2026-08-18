# WindowStage

Implements a window manager, which manages each basic window unit, that is, [Window](arkts-arkui-window-n.md) instance. Before calling any of the following APIs, you must use [onWindowStageCreate()](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#onwindowstagecreate) to create a WindowStage instance.

**Since:** 23

<!--Device-window-interface WindowStage--><!--Device-window-interface WindowStage-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## Modules to Import

```TypeScript
import { floatingBall } from '@kit.ArkUI';
import { floatView } from '@kit.ArkUI';
import { window } from '@kit.ArkUI';
```

## createSubWindow

```TypeScript
createSubWindow(name: string): Promise<Window>
```

Create sub window of the stage.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowStage-createSubWindow(name: string): Promise<Window>--><!--Device-WindowStage-createSubWindow(name: string): Promise<Window>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | window name of sub window |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Window](arkts-arkui-window-window-i.md)&gt; | Promise used to return the subwindow. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: Incorrect parameter types. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The subWindow has been created and can not be created again. |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal.<br>**Applicable version:** 9 and later |

## createSubWindow

```TypeScript
createSubWindow(name: string, callback: AsyncCallback<Window>): void
```

Create sub window of the stage.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowStage-createSubWindow(name: string, callback: AsyncCallback<Window>): void--><!--Device-WindowStage-createSubWindow(name: string, callback: AsyncCallback<Window>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | window name of sub window |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[Window](arkts-arkui-window-window-i.md)&gt; | Yes | Callback used to return the subwindow. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: Incorrect parameter types. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The subWindow has been created and cannot be created again. |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal.<br>**Applicable version:** 9 and later |

## createSubWindowWithOptions

```TypeScript
createSubWindowWithOptions(name: string, options: SubWindowOptions): Promise<Window>
```

Create sub window of the stage.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WindowStage-createSubWindowWithOptions(name: string, options: SubWindowOptions): Promise<Window>--><!--Device-WindowStage-createSubWindowWithOptions(name: string, options: SubWindowOptions): Promise<Window>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | window name of sub window |
| options | [SubWindowOptions](arkts-arkui-window-subwindowoptions-i.md) | Yes | options of sub window creation |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Window](arkts-arkui-window-window-i.md)&gt; | Promise used to return the subwindow. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. The subWindow has been created and cannot be created again. |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal. |

## getMainWindow

```TypeScript
getMainWindow(): Promise<Window>
```

Get main window of the stage.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowStage-getMainWindow(): Promise<Window>--><!--Device-WindowStage-getMainWindow(): Promise<Window>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Window](arkts-arkui-window-window-i.md)&gt; | Callback used to return the subwindow. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal. |

## getMainWindow

```TypeScript
getMainWindow(callback: AsyncCallback<Window>): void
```

Get main window of the stage.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowStage-getMainWindow(callback: AsyncCallback<Window>): void--><!--Device-WindowStage-getMainWindow(callback: AsyncCallback<Window>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[Window](arkts-arkui-window-window-i.md)&gt; | Yes | Callback used to return the main window. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal. |

## getMainWindowSync

```TypeScript
getMainWindowSync(): Window
```

Get main window of the stage.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowStage-getMainWindowSync(): Window--><!--Device-WindowStage-getMainWindowSync(): Window-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| [Window](arkts-arkui-window-window-i.md) |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal. |

## getSubWindow

```TypeScript
getSubWindow(): Promise<Array<Window>>
```

Get sub window of the stage.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowStage-getSubWindow(): Promise<Array<Window>>--><!--Device-WindowStage-getSubWindow(): Promise<Array<Window>>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[Window](arkts-arkui-window-window-i.md)&gt;&gt; |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed.<br>**Applicable version:** 10 and later |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal.<br>**Applicable version:** 9 and later |

## getSubWindow

```TypeScript
getSubWindow(callback: AsyncCallback<Array<Window>>): void
```

Get sub window of the stage.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowStage-getSubWindow(callback: AsyncCallback<Array<Window>>): void--><!--Device-WindowStage-getSubWindow(callback: AsyncCallback<Array<Window>>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;Array&lt;[Window](arkts-arkui-window-window-i.md)&gt;&gt; | Yes | Callback used to return all the subwindows. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed.<br>**Applicable version:** 10 and later |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal.<br>**Applicable version:** 9 and later |

## isWindowRectAutoSave

```TypeScript
isWindowRectAutoSave(): Promise<boolean>
```

Whether the window supports the window rect auto-save.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-WindowStage-isWindowRectAutoSave(): Promise<boolean>--><!--Device-WindowStage-isWindowRectAutoSave(): Promise<boolean>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value true means that the window rect auto-save is supported, and false means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) | This window manager service works abnormally.<br>**Applicable version:** 20 and later |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

## loadContent

```TypeScript
loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void
```

Loads the content of a page, with its path in the current project specified, to the main window of this window stage, and transfers the state attribute to the page through a local storage. This API uses an asynchronous callback to return the result. You are advised to call this API during UIAbility startup. If called multiple times, this API will destroy the existing page content (UIContent) before loading the new content. Exercise caution when using it.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowStage-loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void--><!--Device-WindowStage-loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Path of the page to which the content will be loaded |
| storage | LocalStorage | Yes | The data object shared within the content instance loaded by the window |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Invalid path parameter. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal.<br>**Applicable version:** 9 and later |

## loadContent

```TypeScript
loadContent(path: string, storage?: LocalStorage): Promise<void>
```

Loads the content of a page, with its path in the current project specified, to the main window of this window stage, and transfers the state attribute to the page through a local storage. This API uses a promise to return the result. You are advised to call this API during UIAbility startup. If called multiple times, this API will destroy the existing page content (UIContent) before loading the new content. Exercise caution when using it.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowStage-loadContent(path: string, storage?: LocalStorage): Promise<void>--><!--Device-WindowStage-loadContent(path: string, storage?: LocalStorage): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | of the page to which the content will be loaded |
| storage | LocalStorage | No | The data object shared within the content instance loaded by the window |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Invalid path parameter. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal.<br>**Applicable version:** 9 and later |

## loadContent

```TypeScript
loadContent(path: string, callback: AsyncCallback<void>): void
```

Loads content from a page to this window stage. This API uses an asynchronous callback to return the result. You are advised to call this API during UIAbility startup. If called multiple times, this API will destroy the existing page content (UIContent) before loading the new content. Exercise caution when using it.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowStage-loadContent(path: string, callback: AsyncCallback<void>): void--><!--Device-WindowStage-loadContent(path: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | of the page to which the content will be loaded |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Invalid path parameter. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal.<br>**Applicable version:** 9 and later |

## loadContentByName

```TypeScript
loadContentByName(name: string, storage: LocalStorage, callback: AsyncCallback<void>): void
```

Loads the content of a [named route](../../../ui/arkts-routing.md#named-route) page to this window, and transfers the state attribute to the page through a local storage. This API uses an asynchronous callback to return the result. You are advised to call this API during UIAbility startup. If called repeatedly, this API will destroy the existing page content (UIContent) before loading the new content. Exercise caution when using it. The execution context of the current UI may be unclear. Therefore, you are advised not to perform UI-related operations within the callback of this API.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-WindowStage-loadContentByName(name: string, storage: LocalStorage, callback: AsyncCallback<void>): void--><!--Device-WindowStage-loadContentByName(name: string, storage: LocalStorage, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | name of the page to which the content will be loaded. |
| storage | LocalStorage | Yes | The data object shared within the content instance loaded by the window. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed. |

## loadContentByName

```TypeScript
loadContentByName(name: string, callback: AsyncCallback<void>): void
```

Loads the content of a [named route](../../../ui/arkts-routing.md#named-route) page to this window. This API uses an asynchronous callback to return the result. You are advised to call this API during UIAbility startup. If called repeatedly, this API will destroy the existing page content (UIContent) before loading the new content. Exercise caution when using it. The execution context of the current UI may be unclear. Therefore, you are advised not to perform UI-related operations within the callback of this API.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-WindowStage-loadContentByName(name: string, callback: AsyncCallback<void>): void--><!--Device-WindowStage-loadContentByName(name: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | name of the page to which the content will be loaded. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed. |

## loadContentByName

```TypeScript
loadContentByName(name: string, storage?: LocalStorage): Promise<void>
```

Loads content by named router

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-WindowStage-loadContentByName(name: string, storage?: LocalStorage): Promise<void>--><!--Device-WindowStage-loadContentByName(name: string, storage?: LocalStorage): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | name of the page to which the content will be loaded. |
| storage | LocalStorage | No | The data object shared within the content instance loaded by the window. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed. |

## offWindowStageClose

```TypeScript
offWindowStageClose(callback?: Callback<void, boolean>): void
```

Unsubscribes from the event indicating that the main window is closed.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStage-offWindowStageClose(callback?: Callback<void, boolean>): void--><!--Device-WindowStage-offWindowStageClose(callback?: Callback<void, boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void, boolean&gt; | No | Unregister the callback function. If not provided, all callbacks for the given event type will be removed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed. |

## offWindowStageEvent

```TypeScript
offWindowStageEvent(callback?: Callback<WindowStageEventType>): void
```

Unsubscribes from the window stage lifecycle change event.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStage-offWindowStageEvent(callback?: Callback<WindowStageEventType>): void--><!--Device-WindowStage-offWindowStageEvent(callback?: Callback<WindowStageEventType>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[WindowStageEventType](arkts-arkui-window-windowstageeventtype-e.md)&gt; | No | Unregister the callback function. If not provided, all callbacks for the given event type will be removed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal. |

## offWindowStageLifecycleEvent

```TypeScript
offWindowStageLifecycleEvent(callback?: Callback<WindowStageLifecycleEventType>): void
```

Unsubscribes from the window stage lifecycle change event.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStage-offWindowStageLifecycleEvent(callback?: Callback<WindowStageLifecycleEventType>): void--><!--Device-WindowStage-offWindowStageLifecycleEvent(callback?: Callback<WindowStageLifecycleEventType>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[WindowStageLifecycleEventType](arkts-arkui-window-windowstagelifecycleeventtype-e.md)&gt; | No | Unregister the callback function. If not provided, all callbacks for the given event type will be removed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal. |

## off_windowStageClose

```TypeScript
off(eventType: 'windowStageClose', callback?: Callback<void>): void
```

Window stage close callback off.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-WindowStage-off(eventType: 'windowStageClose', callback?: Callback<void>): void--><!--Device-WindowStage-off(eventType: 'windowStageClose', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventType | 'windowStageClose' | Yes | The value is fixed at 'windowStageClose', indicating the window stage close event. |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | No | Callback function requires a boolean return value to determine whether to close the current main window. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed. |

## off_windowStageEvent

```TypeScript
off(eventType: 'windowStageEvent', callback?: Callback<WindowStageEventType>): void
```

Unsubscribes from the window stage lifecycle change event.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowStage-off(eventType: 'windowStageEvent', callback?: Callback<WindowStageEventType>): void--><!--Device-WindowStage-off(eventType: 'windowStageEvent', callback?: Callback<WindowStageEventType>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventType | 'windowStageEvent' | Yes | Event type. The value is fixed at 'windowStageEvent', indicating the window stage lifecycle change event. |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[WindowStageEventType](arkts-arkui-window-windowstageeventtype-e.md)&gt; | No | Callback used to return the window stage lifecycle state. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal. |

## off_windowStageLifecycleEvent

```TypeScript
off(eventType: 'windowStageLifecycleEvent', callback?: Callback<WindowStageLifecycleEventType>): void
```

Unsubscribes from the window stage lifecycle change event.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStage-off(eventType: 'windowStageLifecycleEvent', callback?: Callback<WindowStageLifecycleEventType>): void--><!--Device-WindowStage-off(eventType: 'windowStageLifecycleEvent', callback?: Callback<WindowStageLifecycleEventType>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventType | 'windowStageLifecycleEvent' | Yes | Event type. The value is fixed at 'windowStageLifecycleEvent', indicating the window stage lifecycle change event. |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[WindowStageLifecycleEventType](arkts-arkui-window-windowstagelifecycleeventtype-e.md)&gt; | No | Callback used to return the window stage lifecycle state. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal. |

## onWindowStageClose

```TypeScript
onWindowStageClose(callback: Callback<void, boolean>): void
```

Subscribes to the click event on the close button in the three-button navigation bar of the main window. This event is triggered when the close button in the three-button navigation bar of the main window is clicked.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStage-onWindowStageClose(callback: Callback<void, boolean>): void--><!--Device-WindowStage-onWindowStageClose(callback: Callback<void, boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void, boolean&gt; | Yes | Callback invoked when the close button in the upper right corner of the main window is clicked. The return value determines whether to continue to close the main window. The value true means not to close the main window, and false means to continue to close the main window. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed. |

## onWindowStageEvent

```TypeScript
onWindowStageEvent(callback: Callback<WindowStageEventType>): void
```

Subscribes to the window stage lifecycle change event.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStage-onWindowStageEvent(callback: Callback<WindowStageEventType>): void--><!--Device-WindowStage-onWindowStageEvent(callback: Callback<WindowStageEventType>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[WindowStageEventType](arkts-arkui-window-windowstageeventtype-e.md)&gt; | Yes | Callback used to return the window stage lifecycle state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal. |

## onWindowStageLifecycleEvent

```TypeScript
onWindowStageLifecycleEvent(callback: Callback<WindowStageLifecycleEventType>): void
```

Subscribes to the window stage lifecycle change event.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStage-onWindowStageLifecycleEvent(callback: Callback<WindowStageLifecycleEventType>): void--><!--Device-WindowStage-onWindowStageLifecycleEvent(callback: Callback<WindowStageLifecycleEventType>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[WindowStageLifecycleEventType](arkts-arkui-window-windowstagelifecycleeventtype-e.md)&gt; | Yes | Callback used to return the window stage lifecycle state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal. |

## on_windowStageClose

```TypeScript
on(eventType: 'windowStageClose', callback: Callback<void>): void
```

Window stage close callback on.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-WindowStage-on(eventType: 'windowStageClose', callback: Callback<void>): void--><!--Device-WindowStage-on(eventType: 'windowStageClose', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventType | 'windowStageClose' | Yes | The value is fixed at 'windowStageClose', indicating the window stage close event. |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;void&gt; | Yes | Callback function requires a boolean return value to determine whether to close the current main window. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed. |

## on_windowStageEvent

```TypeScript
on(eventType: 'windowStageEvent', callback: Callback<WindowStageEventType>): void
```

Subscribes to the window stage lifecycle change event.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WindowStage-on(eventType: 'windowStageEvent', callback: Callback<WindowStageEventType>): void--><!--Device-WindowStage-on(eventType: 'windowStageEvent', callback: Callback<WindowStageEventType>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventType | 'windowStageEvent' | Yes | Event type. The value is fixed at 'windowStageEvent', indicating the window stage lifecycle change event. |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[WindowStageEventType](arkts-arkui-window-windowstageeventtype-e.md)&gt; | Yes | Callback used to return the window stage lifecycle state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal. |

## on_windowStageLifecycleEvent

```TypeScript
on(eventType: 'windowStageLifecycleEvent', callback: Callback<WindowStageLifecycleEventType>): void
```

Subscribes to the window stage lifecycle change event.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStage-on(eventType: 'windowStageLifecycleEvent', callback: Callback<WindowStageLifecycleEventType>): void--><!--Device-WindowStage-on(eventType: 'windowStageLifecycleEvent', callback: Callback<WindowStageLifecycleEventType>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventType | 'windowStageLifecycleEvent' | Yes | Event type. The value is fixed at 'windowStageLifecycleEvent', indicating the window stage lifecycle change event. |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[WindowStageLifecycleEventType](arkts-arkui-window-windowstagelifecycleeventtype-e.md)&gt; | Yes | Callback used to return the window stage lifecycle state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal. |

## releaseUIContent

```TypeScript
releaseUIContent(): Promise<void>
```

Release the content of this window in the current project. This API uses a promise to return the result.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStage-releaseUIContent(): Promise<void>--><!--Device-WindowStage-releaseUIContent(): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value, indicating successful completion. Throws exception if window state is abnormal. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed. |

## removeStartingWindow

```TypeScript
removeStartingWindow(): Promise<void>
```

Remove the starting window, it must be used with configuration "enable.remove.starting.window".

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-WindowStage-removeStartingWindow(): Promise<void>--><!--Device-WindowStage-removeStartingWindow(): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) | This window manager service works abnormally. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: 1. The window stage is not created or destroyed; 2. The main window is not created or destroyed; 3. Internal task error. |

## setCustomDensity

```TypeScript
setCustomDensity(density: number): void
```

Allows the main window of the application to customize its display size scale factor. Existing child windows and system windows do not immediately re-layout to match the main window's new scale factor. They will re-layout to reflect this change only when their layout information (such as position, size, and system scale size) changes. If both this API and [setDefaultDensityEnabled(true)](#setdefaultdensityenabled) are called, the setting from the last called API will be applied.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-WindowStage-setCustomDensity(density: number): void--><!--Device-WindowStage-setCustomDensity(density: number): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| density | number | Yes | the specified custom density value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal. |

## setCustomDensity

```TypeScript
setCustomDensity(density: double, applyToSubWindow?: boolean): void
```

Allows the main window of the application to customize its display size scale factor and control when child windows and system windows re-layout to match the main window. If both this API and [setDefaultDensityEnabled(true)](#setdefaultdensityenabled) are called, the setting from the last called API will be applied.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStage-setCustomDensity(density: double, applyToSubWindow?: boolean): void--><!--Device-WindowStage-setCustomDensity(density: double, applyToSubWindow?: boolean): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| density | double | Yes | the specified custom density value. |
| applyToSubWindow | boolean | No | whether to apply the custom density to already created subwindows. The default value is false. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The main window is not created or destroyed. |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal. Possible cause: The window stage is not created or destroyed. |

## setDefaultDensityEnabled

```TypeScript
setDefaultDensityEnabled(enabled: boolean): void
```

Sets whether the main window of the application uses the system's default density. Child windows and system windows will follow the main window's setting. Before calling this API, call [WindowStage.loadContent()](#loadcontent) to initialize the layout to ensure the correct call sequence. If this API is not called, the default density is not used. When the default density is not used, if [setCustomDensity()](#setcustomdensity) has been called, the window will be re-laid out according to the custom display size changes. Otherwise, it will be re-laid out according to the system display size changes.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-WindowStage-setDefaultDensityEnabled(enabled: boolean): void--><!--Device-WindowStage-setDefaultDensityEnabled(enabled: boolean): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Use default density if true, or follow system density change if false |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The main window is not created or destroyed. |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal. Possible cause: The window stage is not created or destroyed. |

## setSupportedWindowModes

```TypeScript
setSupportedWindowModes(supportedWindowModes: Array<bundleManager.SupportWindowMode>): Promise<void>
```

Sets the supported window modes.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-WindowStage-setSupportedWindowModes(supportedWindowModes: Array<bundleManager.SupportWindowMode>): Promise<void>--><!--Device-WindowStage-setSupportedWindowModes(supportedWindowModes: Array<bundleManager.SupportWindowMode>): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| supportedWindowModes | Array&lt;bundleManager.SupportWindowMode&gt; | Yes | The supported modes of window. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) | This window manager service works abnormally. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. Internal task error. |

## setSupportedWindowModes

```TypeScript
setSupportedWindowModes(supportedWindowModes: Array<bundleManager.SupportWindowMode>, grayOutMaximizeButton: boolean): Promise<void>
```

Sets the supported window modes of the main window.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowStage-setSupportedWindowModes(supportedWindowModes: Array<bundleManager.SupportWindowMode>, grayOutMaximizeButton: boolean): Promise<void>--><!--Device-WindowStage-setSupportedWindowModes(supportedWindowModes: Array<bundleManager.SupportWindowMode>, grayOutMaximizeButton: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| supportedWindowModes | Array&lt;bundleManager.SupportWindowMode&gt; | Yes | The supported modes of window. |
| grayOutMaximizeButton | boolean | Yes | Whether to gray out the window maximize button. The value true means to gray out the button, and false means the opposite. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) | This window manager service works abnormally. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Function setSupportedWindowModes can not work correctly due to limited device capabilities. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. Internal task error. |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) | Parameter error. Possible cause: 1. Invalid parameter range. 2. Invalid parameter length. 3. Incorrect parameter format. |

## setWindowModal

```TypeScript
setWindowModal(isModal: boolean): Promise<void>
```

Set the application modality of the windowStage.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-WindowStage-setWindowModal(isModal: boolean): Promise<void>--><!--Device-WindowStage-setWindowModal(isModal: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isModal | boolean | Yes | Enable the window modal if true, otherwise means the opposite. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) | This window manager service works abnormally. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| [1300005](../errorcode-window.md#1300005-abnormal-windowstage) | This window stage is abnormal. Possible cause: The window is not created or destroyed.<br>**Applicable version:** 20 and later |

## setWindowRectAutoSave

```TypeScript
setWindowRectAutoSave(enabled: boolean): Promise<void>
```

Set to automatically save the window rect.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-WindowStage-setWindowRectAutoSave(enabled: boolean): Promise<void>--><!--Device-WindowStage-setWindowRectAutoSave(enabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Enable the window rect auto-save if true, otherwise means the opposite. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) | This window manager service works abnormally. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

## setWindowRectAutoSave

```TypeScript
setWindowRectAutoSave(enabled: boolean, isSaveBySpecifiedFlag: boolean): Promise<void>
```

Set to automatically save the window rect and whether to enable specifiedFlag. Through the specifiedFlag flag, the window is marked and its rect is saved.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-WindowStage-setWindowRectAutoSave(enabled: boolean, isSaveBySpecifiedFlag: boolean): Promise<void>--><!--Device-WindowStage-setWindowRectAutoSave(enabled: boolean, isSaveBySpecifiedFlag: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Enable the window rect auto-save if true, otherwise means the opposite. |
| isSaveBySpecifiedFlag | boolean | Yes | Enable the specifiedFlag if true, otherwise means the opposite. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) | This window manager service works abnormally. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Function setWindowRectAutoSave can not work correctly due to limited device capabilities. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |

