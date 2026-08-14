# UIContext

class UIContext

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare class UIContext--><!--Device-unnamed-export declare class UIContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addLocalInputEventMonitor

```TypeScript
addLocalInputEventMonitor(eventMask: int, listener: InputEventListener): InputEventMonitor
```

Registers a local input event monitor. The "Local" in the interface name indicates that the monitor is only valid within the current UIContext, and does not affect other UIContext instances. Each UIContext maintains its own independent list of monitors. Performance Warning: Do not perform time-consuming operations in the callback! Monitor Object Notes: - The returned Monitor object is a unique identifier created by the system. - Developers cannot actively construct or forge this object. - Must save the returned monitor object reference for subsequent cancellation. - It is recommended to use a variable to save it to avoid losing the reference. Usage Examples: ```typescript // Monitor a single event type const monitor1 = uiContext.addLocalInputEventMonitor( InputEventSubTypeMask.LEFT_MOUSE_DOWN, (wrapper: RawInputEventWrapper) => { if (wrapper.isMouseEvent()) { const mouseEvent = wrapper.asMouseEvent(); console.log(`Mouse: (\${mouseEvent.windowX}, \${mouseEvent.windowY})`); return { action: InputEventInterceptAction.CONTINUE }; // Allow event to continue } return { action: InputEventInterceptAction.BLOCK }; // Block event } ); // Monitor multiple event types (using bitwise operations) const monitor2 = uiContext.addLocalInputEventMonitor( InputEventSubTypeMask.LEFT_MOUSE_DOWN | InputEventSubTypeMask.RIGHT_MOUSE_DOWN, (wrapper: RawInputEventWrapper) => { if (wrapper.isMouseEvent()) { const mouseEvent = wrapper.asMouseEvent()!; console.log(`Mouse button: \${mouseEvent.button}`); return { action: InputEventInterceptAction.BLOCK }; } return { action: InputEventInterceptAction.CONTINUE }; } ); // When unregistering the monitor, use the returned Monitor object uiContext.removeLocalInputEventMonitor(monitor1); uiContext.removeLocalInputEventMonitor(monitor2); ```

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-addLocalInputEventMonitor(eventMask: int, listener: InputEventListener): InputEventMonitor--><!--Device-UIContext-addLocalInputEventMonitor(eventMask: int, listener: InputEventListener): InputEventMonitor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventMask | int | Yes | Event type mask, specifying the types of events to monitor through bitwise operations. |
| listener | InputEventListener | Yes | Event listener callback function. |

**Return value:**

| Type | Description |
| --- | --- |
| InputEventMonitor | Unique identifier object for the monitor, used for subsequent cancellation of registration. |

## animateTo

```TypeScript
animateTo(value: AnimateParam, event: () => void): void
```

Defining animation function

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-animateTo(value: AnimateParam, event: () => void): void--><!--Device-UIContext-animateTo(value: AnimateParam, event: () => void): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | AnimateParam | Yes | parameters for animation. |
| event | () =&gt; void | Yes | the closure base on which, the system will create animation automatically |

## animateToImmediately

```TypeScript
animateToImmediately(param: AnimateParam, processor: VoidCallback): void
```

Define animation functions for immediate distribution.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-animateToImmediately(param: AnimateParam, processor: VoidCallback): void--><!--Device-UIContext-animateToImmediately(param: AnimateParam, processor: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | AnimateParam | Yes | Set animation effect parameters. |
| processor | VoidCallback | Yes | Specify the closure function that displays dynamic effects, and the system will automatically insert transition animations for state changes caused by the closure function. |

## bindTabsToNestedScrollable

```TypeScript
bindTabsToNestedScrollable(tabsController: TabsController, parentScroller: Scroller, childScroller: Scroller): void
```

Bind tabs to nested scrollable container components to automatically hide tab bar.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-bindTabsToNestedScrollable(tabsController: TabsController, parentScroller: Scroller, childScroller: Scroller): void--><!--Device-UIContext-bindTabsToNestedScrollable(tabsController: TabsController, parentScroller: Scroller, childScroller: Scroller): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tabsController | TabsController | Yes | The controller of the tabs. |
| parentScroller | Scroller | Yes | The controller of the parent scrollable container component. |
| childScroller | Scroller | Yes | The controller of the child scrollable container component. |

## bindTabsToScrollable

```TypeScript
bindTabsToScrollable(tabsController: TabsController, scroller: Scroller): void
```

Bind tabs to scrollable container component to automatically hide tab bar.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-bindTabsToScrollable(tabsController: TabsController, scroller: Scroller): void--><!--Device-UIContext-bindTabsToScrollable(tabsController: TabsController, scroller: Scroller): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tabsController | TabsController | Yes | The controller of the tabs. |
| scroller | Scroller | Yes | The controller of the scrollable container component. |

## closeBindSheet

```TypeScript
closeBindSheet(bindSheetContent: ComponentContentBase): Promise<void>
```

Close the BindSheet.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-closeBindSheet(bindSheetContent: ComponentContentBase): Promise<void>--><!--Device-UIContext-closeBindSheet(bindSheetContent: ComponentContentBase): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bindSheetContent | [ComponentContentBase](arkts-na-componentcontent-componentcontentbase-c.md) | Yes | The content of BindSheet. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [120001](../../apis-arkui/errorcode-bindSheet.md#120001-incorrect-bindsheetcontent) | The bindSheetContent is incorrect. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [120003](../../apis-arkui/errorcode-bindSheet.md#120003-no-matching-modal-found) | The bindSheetContent cannot be found. |

## constructor

```TypeScript
constructor()
```

UIContext constructor

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-constructor()--><!--Device-UIContext-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## createAnimator

```TypeScript
createAnimator(options: AnimatorOptions | SimpleAnimatorOptions): AnimatorResult
```

Create an animator object for custom animation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-createAnimator(options: AnimatorOptions | SimpleAnimatorOptions): AnimatorResult--><!--Device-UIContext-createAnimator(options: AnimatorOptions | SimpleAnimatorOptions): AnimatorResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [AnimatorOptions](../../apis-arkui/arkts-apis/arkts-arkui-animator-animatoroptions-i.md) \| [SimpleAnimatorOptions](../../apis-arkui/arkts-apis/arkts-arkui-animator-simpleanimatoroptions-c.md) | Yes | Options. |

**Return value:**

| Type | Description |
| --- | --- |
| [AnimatorResult](../../apis-arkui/arkts-apis/arkts-arkui-animator-animatorresult-i.md) |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |

## createUIContextWithoutWindow

```TypeScript
static createUIContextWithoutWindow(
    context: common.UIAbilityContext | common.ExtensionContext): UIContext | undefined
```

Create a UI instance singleton without window and get its UIContext object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-static createUIContextWithoutWindow(    context: common.UIAbilityContext | common.ExtensionContext): UIContext | undefined--><!--Device-UIContext-static createUIContextWithoutWindow(    context: common.UIAbilityContext | common.ExtensionContext): UIContext | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | common.UIAbilityContext \| common.ExtensionContext | Yes | UIAbilityContext or ExtensionContext. |

**Return value:**

| Type | Description |
| --- | --- |
| [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | object UIContext, or undefined when failed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal error. @static |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. The number of parameters is incorrect. <br> 2. Invalid parameter type of context. |

## destroyUIContextWithoutWindow

```TypeScript
static destroyUIContextWithoutWindow(): void
```

Destroy the UI instance singleton without window.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-static destroyUIContextWithoutWindow(): void--><!--Device-UIContext-static destroyUIContextWithoutWindow(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dispatchKeyEvent

```TypeScript
dispatchKeyEvent(node: int | string, event: KeyEvent): boolean
```

Dispach keyboard event to the frameNode with inspector key.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-dispatchKeyEvent(node: int | string, event: KeyEvent): boolean--><!--Device-UIContext-dispatchKeyEvent(node: int | string, event: KeyEvent): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | int \| string | Yes | The uniqueId or inspector key of the target FrameNode. |
| event | KeyEvent | Yes | The keyboard event. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns whether the key event is consumed. |

## enableEventPassthrough

```TypeScript
enableEventPassthrough(enabled: boolean | undefined, eventType: RawInputEventType): void
```

Whether to enable or disable event passthrough.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-enableEventPassthrough(enabled: boolean | undefined, eventType: RawInputEventType): void--><!--Device-UIContext-enableEventPassthrough(enabled: boolean | undefined, eventType: RawInputEventType): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes | enable or disable event passthrough. The default value is false. |
| eventType | RawInputEventType | Yes | the type of raw input event. |

## enableSwipeBack

```TypeScript
enableSwipeBack(enabled: boolean | undefined): void
```

whether to enable or disable swipe to back event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-enableSwipeBack(enabled: boolean | undefined): void--><!--Device-UIContext-enableSwipeBack(enabled: boolean | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes | enable or disable swipe to back event. |

## fp2px

```TypeScript
fp2px(value: double): double
```

Converts a value in fp units to a value in px.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-fp2px(value: double): double--><!--Device-UIContext-fp2px(value: double): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| double |  |

## getAllUIContexts

```TypeScript
static getAllUIContexts(): UIContext[]
```

Gets all currently active UIContext instances.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-static getAllUIContexts(): UIContext[]--><!--Device-UIContext-static getAllUIContexts(): UIContext[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md)[] | An array containing all valid UIContext instances, returns an empty array if no contexts are available. |

## getAtomicServiceBar

```TypeScript
getAtomicServiceBar(): Nullable<AtomicServiceBar>
```

Get AtomicServiceBar.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getAtomicServiceBar(): Nullable<AtomicServiceBar>--><!--Device-UIContext-getAtomicServiceBar(): Nullable<AtomicServiceBar>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Nullable&lt;[AtomicServiceBar](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-atomicservicebar-i.md)&gt; | The atomic service bar. |

## getAttachedFrameNodeById

```TypeScript
getAttachedFrameNodeById(id: string): FrameNode | null
```

Get the FrameNode attached to current window by id.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getAttachedFrameNodeById(id: string): FrameNode | null--><!--Device-UIContext-getAttachedFrameNodeById(id: string): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | The id of FrameNode. |

**Return value:**

| Type | Description |
| --- | --- |
| FrameNode | The instance of FrameNode. |

## getCallingScopeUIContext

```TypeScript
static getCallingScopeUIContext(): UIContext | undefined
```

Gets the UIContext associated with the current calling scope.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-static getCallingScopeUIContext(): UIContext | undefined--><!--Device-UIContext-static getCallingScopeUIContext(): UIContext | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | The UIContext for the current calling scope, or undefined if no context can be determined from the call stack. |

## getComponentSnapshot

```TypeScript
getComponentSnapshot(): ComponentSnapshot
```

Get ComponentSnapshot.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getComponentSnapshot(): ComponentSnapshot--><!--Device-UIContext-getComponentSnapshot(): ComponentSnapshot-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [ComponentSnapshot](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-componentsnapshot-c.md) | the ComponentSnapshot |

## getComponentUtils

```TypeScript
getComponentUtils(): ComponentUtils
```

get object ComponentUtils.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getComponentUtils(): ComponentUtils--><!--Device-UIContext-getComponentUtils(): ComponentUtils-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [ComponentUtils](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-componentutils-c.md) | object ComponentUtils. |

## getContextMenuController

```TypeScript
getContextMenuController(): ContextMenuController
```

Get object context menu controller.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getContextMenuController(): ContextMenuController--><!--Device-UIContext-getContextMenuController(): ContextMenuController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [ContextMenuController](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-contextmenucontroller-c.md) | object context menu controller. |

## getCursorController

```TypeScript
getCursorController(): CursorController
```

Get object cursor controller.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getCursorController(): CursorController--><!--Device-UIContext-getCursorController(): CursorController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [CursorController](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-cursorcontroller-c.md) | object cursor controller. |

## getDragController

```TypeScript
getDragController(): DragController
```

Get DragController.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getDragController(): DragController--><!--Device-UIContext-getDragController(): DragController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [DragController](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-dragcontroller-c.md) | the DragController |

## getFilteredInspectorTree

```TypeScript
getFilteredInspectorTree(filters?: Array<string>): string
```

Obtains the component tree and component attributes. This API has a long processing time and is intended for <br>testing scenarios only.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getFilteredInspectorTree(filters?: Array<string>): string--><!--Device-UIContext-getFilteredInspectorTree(filters?: Array<string>): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filters | Array&lt;string&gt; | No | List of component attributes used for filtering. Currently, only the following filter fields are supported: <br>**"id"**: unique ID of the component. <br>**"src"**: source of the resource. <br>**"content"**: information or data contained in the element, component, or object. <br>**"editable"**: whether the component is editable. <br>**"scrollable"**: whether the component is scrollable. <br>**"selectable"**: whether the component is selectable. <br>**"focusable"**: whether the component is focusable. <br>**"focused"**: whether the component is currently focused. <br>If **filters** includes one or more fields, unspecified fields will be filtered out from the results. <br>If **filters** is not provided or is an empty array, none of the aforementioned fields will be filtered out. <br>Other filter fields are used only in testing scenarios. |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON string of the component tree and component attributes. For details about each field in the component, see the return value description of [getInspectorInfo]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100023](../../apis-arkui/errorcode-node.md#100023-parameter-error) | Unable to obtain current ui context. |

## getFilteredInspectorTreeById

```TypeScript
getFilteredInspectorTreeById(id: string, depth: int, filters?: Array<string>): string
```

Obtains the attributes of the specified component and its child components. This API has a long processing time <br>and is intended for testing scenarios only.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getFilteredInspectorTreeById(id: string, depth: int, filters?: Array<string>): string--><!--Device-UIContext-getFilteredInspectorTreeById(id: string, depth: int, filters?: Array<string>): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | ID of the target component. |
| depth | int | Yes | Number of layers of child components. If the value is **0**, the attributes of the specified component and all its child components are obtained. If the value is **1**, only the attributes of <br>the specified component are obtained. If the value is **2**, the attributes of the specified component and its <br>level-1 child components are obtained. The rest can be deduced by analogy. |
| filters | Array&lt;string&gt; | No | List of component attributes used for filtering. Currently, only the following filter fields are supported: <br>**"id"**: unique ID of the component. <br>**"src"**: source of the resource. <br>**"content"**: information or data contained in the element, component, or object. <br>**"editable"**: whether the component is editable. <br>**"scrollable"**: whether the component is scrollable. <br>**"selectable"**: whether the component is selectable. <br>**"focusable"**: whether the component is focusable. <br>**"focused"**: whether the component is currently focused. <br>If **filters** includes one or more fields, unspecified fields will be filtered out from the results. <br>If **filters** is not provided or is an empty array, none of the aforementioned fields will be filtered out. <br>Other filter fields are used only in testing scenarios. |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON string of the attributes of the specified component and its child components. For details about each field in the component, see the return value description of [getInspectorInfo]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100023](../../apis-arkui/errorcode-node.md#100023-parameter-error) | Unable to obtain current ui context. |
| [100024](../../apis-arkui/errorcode-node.md#100024-no-common-ancestor-node-between-nodes) | The parameter depth must be greater than 0. |

## getFocusController

```TypeScript
getFocusController(): FocusController
```

Get FocusController.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getFocusController(): FocusController--><!--Device-UIContext-getFocusController(): FocusController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [FocusController](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-focuscontroller-c.md) | the FocusController |

## getFont

```TypeScript
getFont(): Font
```

get object font.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getFont(): Font--><!--Device-UIContext-getFont(): Font-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Font](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-font-c.md) | object Font. |

## getFrameNodeById

```TypeScript
getFrameNodeById(id: string): FrameNode | null
```

Get FrameNode by id.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getFrameNodeById(id: string): FrameNode | null--><!--Device-UIContext-getFrameNodeById(id: string): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | The id of FrameNode. |

**Return value:**

| Type | Description |
| --- | --- |
| FrameNode | The instance of FrameNode. |

## getFrameNodeByUniqueId

```TypeScript
getFrameNodeByUniqueId(id: int): FrameNode | null
```

Get FrameNode by uniqueId.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getFrameNodeByUniqueId(id: int): FrameNode | null--><!--Device-UIContext-getFrameNodeByUniqueId(id: int): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | int | Yes | The uniqueId of the FrameNode. |

**Return value:**

| Type | Description |
| --- | --- |
| FrameNode | The FrameNode with the target uniqueId, or null if the frameNode is not existed. |

## getHostContext

```TypeScript
getHostContext(): Context | undefined
```

Obtains context of the ability.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getHostContext(): Context | undefined--><!--Device-UIContext-getHostContext(): Context | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Context](../../apis-arkui/arkts-apis/arkts-arkui-context-t.md) |  |

## getId

```TypeScript
getId(): int
```

Get id of the UI instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getId(): int--><!--Device-UIContext-getId(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns id of the UI instance. |

## getKeyboardAvoidMode

```TypeScript
getKeyboardAvoidMode(): KeyboardAvoidMode
```

Get KeyboardAvoidMode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getKeyboardAvoidMode(): KeyboardAvoidMode--><!--Device-UIContext-getKeyboardAvoidMode(): KeyboardAvoidMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [KeyboardAvoidMode](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-keyboardavoidmode-e.md) | The mode of keyboard avoid. |

## getLastFocusedUIContext

```TypeScript
static getLastFocusedUIContext(): UIContext | undefined
```

Gets the UIContext of the last focused UI instance if one exists.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-static getLastFocusedUIContext(): UIContext | undefined--><!--Device-UIContext-static getLastFocusedUIContext(): UIContext | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | The UIContext of the last focused UI instance or undefined if no one exists. |

## getLastForegroundUIContext

```TypeScript
static getLastForegroundUIContext(): UIContext | undefined
```

Gets the UIContext of the last foregrounded UI instance if one exists.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-static getLastForegroundUIContext(): UIContext | undefined--><!--Device-UIContext-static getLastForegroundUIContext(): UIContext | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | The UIContext of the last foregrounded UI instance or undefined if no one exists |

## getMagnifier

```TypeScript
getMagnifier(): Magnifier
```

Obtains the Magnifier object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getMagnifier(): Magnifier--><!--Device-UIContext-getMagnifier(): Magnifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Magnifier](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-magnifier-c.md) | Magnifier instance obtained. |

## getMaxFontScale

```TypeScript
getMaxFontScale(): double
```

Get the max font scale.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getMaxFontScale(): double--><!--Device-UIContext-getMaxFontScale(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double | The max font scale. |

## getMeasureUtils

```TypeScript
getMeasureUtils(): MeasureUtils
```

Get MeasureUtils.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getMeasureUtils(): MeasureUtils--><!--Device-UIContext-getMeasureUtils(): MeasureUtils-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [MeasureUtils](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-measureutils-c.md) | the MeasureUtils |

## getMediaQuery

```TypeScript
getMediaQuery(): MediaQuery
```

get object mediaQuery.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getMediaQuery(): MediaQuery--><!--Device-UIContext-getMediaQuery(): MediaQuery-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [MediaQuery](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-mediaquery-c.md) | object MediaQuery. |

## getNavigationInfoByUniqueId

```TypeScript
getNavigationInfoByUniqueId(id: int): observer.NavigationInfo | undefined
```

Get navigation information of the frameNode with uniqueId.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getNavigationInfoByUniqueId(id: int): observer.NavigationInfo | undefined--><!--Device-UIContext-getNavigationInfoByUniqueId(id: int): observer.NavigationInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | int | Yes | The uniqueId of the target FrameNode. |

**Return value:**

| Type | Description |
| --- | --- |
| observer.NavigationInfo | The navigation information of the frameNode with the target uniqueId, or undefined if the frameNode is not existed or does not have navigation information. |

## getOverlayManager

```TypeScript
getOverlayManager(): OverlayManager
```

Get object OverlayManager.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getOverlayManager(): OverlayManager--><!--Device-UIContext-getOverlayManager(): OverlayManager-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [OverlayManager](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-overlaymanager-c.md) | object OverlayManager. |

## getOverlayManagerOptions

```TypeScript
getOverlayManagerOptions(): OverlayManagerOptions
```

Get object OverlayManagerOptions.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getOverlayManagerOptions(): OverlayManagerOptions--><!--Device-UIContext-getOverlayManagerOptions(): OverlayManagerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [OverlayManagerOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-overlaymanageroptions-i.md) | object OverlayManagerOptions. |

## getPageInfoByUniqueId

```TypeScript
getPageInfoByUniqueId(id: int): PageInfo
```

Get page information of the frameNode with uniqueId.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getPageInfoByUniqueId(id: int): PageInfo--><!--Device-UIContext-getPageInfoByUniqueId(id: int): PageInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | int | Yes | The uniqueId of the target FrameNode. |

**Return value:**

| Type | Description |
| --- | --- |
| [PageInfo](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-pageinfo-i.md) | The page information of the frameNode with the target uniqueId, includes navDestination and router page information. If the frame node does not have navDestination and router page information, it will return an empty object. |

## getPageRootNode

```TypeScript
getPageRootNode(): FrameNode | null
```

Retrieve the root node of the corresponding page of the UIContext.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getPageRootNode(): FrameNode | null--><!--Device-UIContext-getPageRootNode(): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| FrameNode | The root node of the corresponding page of the UIContext, or null if no root node exists. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [120007](../../apis-arkui/errorcode-uicontext.md#120007-instance-not-exist) | The UIContext is not available. |

## getPixelRoundMode

```TypeScript
getPixelRoundMode(): PixelRoundMode
```

Get the pixel round mode of the system.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getPixelRoundMode(): PixelRoundMode--><!--Device-UIContext-getPixelRoundMode(): PixelRoundMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| PixelRoundMode | the mode of pixel round. |

## getPromptAction

```TypeScript
getPromptAction(): PromptAction
```

get object PromptAction.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getPromptAction(): PromptAction--><!--Device-UIContext-getPromptAction(): PromptAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [PromptAction](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-promptaction-c.md) | object PromptAction. |

## getRouter

```TypeScript
getRouter(): Router
```

get object router.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getRouter(): Router--><!--Device-UIContext-getRouter(): Router-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Router](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-router-c.md) | object Router. |

## getSharedLocalStorage

```TypeScript
getSharedLocalStorage(): LocalStorage | undefined
```

Get current LocalStorage shared from stage.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getSharedLocalStorage(): LocalStorage | undefined--><!--Device-UIContext-getSharedLocalStorage(): LocalStorage | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| LocalStorage |  |

## getSmartGestureController

```TypeScript
getSmartGestureController(): SmartGestureController
```

Get object smart gesture controller.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getSmartGestureController(): SmartGestureController--><!--Device-UIContext-getSmartGestureController(): SmartGestureController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [SmartGestureController](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-smartgesturecontroller-c.md) | object smart gesture controller. |

## getTextMenuController

```TypeScript
getTextMenuController(): TextMenuController
```

Get object text menu controller.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getTextMenuController(): TextMenuController--><!--Device-UIContext-getTextMenuController(): TextMenuController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [TextMenuController](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-textmenucontroller-c.md) | object text menu controller. |

## getUIInspector

```TypeScript
getUIInspector(): UIInspector
```

Obtains the **UIInspector** object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getUIInspector(): UIInspector--><!--Device-UIContext-getUIInspector(): UIInspector-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [UIInspector](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uiinspector-c.md) | UIInspector** object. |

## getUIObserver

```TypeScript
getUIObserver(): UIObserver
```

Get the UI observer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getUIObserver(): UIObserver--><!--Device-UIContext-getUIObserver(): UIObserver-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [UIObserver](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uiobserver-c.md) | The UI observer. |

## getWindowHeightBreakpoint

```TypeScript
getWindowHeightBreakpoint(): HeightBreakpoint
```

Get the height breakpoint of current window.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getWindowHeightBreakpoint(): HeightBreakpoint--><!--Device-UIContext-getWindowHeightBreakpoint(): HeightBreakpoint-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| HeightBreakpoint | The height breakpoint of current window. |

## getWindowId

```TypeScript
getWindowId(): int | undefined
```

Get window id to which the current UIContext belongs. &lt;p&gt;**NOTE：**: If the current UIContext is in a UIExtensionAbility running within the host process, this method returns the top-level window ID of the host application. &lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getWindowId(): int | undefined--><!--Device-UIContext-getWindowId(): int | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | Window id. If the current UIContext is unavailable, return undefined. |

## getWindowName

```TypeScript
getWindowName(): string | undefined
```

Get the name of current window.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getWindowName(): string | undefined--><!--Device-UIContext-getWindowName(): string | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string | The name of current window, or undefined if the window doesn't exist. |

## getWindowWidthBreakpoint

```TypeScript
getWindowWidthBreakpoint(): WidthBreakpoint
```

Get the width breakpoint of current window.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getWindowWidthBreakpoint(): WidthBreakpoint--><!--Device-UIContext-getWindowWidthBreakpoint(): WidthBreakpoint-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| WidthBreakpoint | The width breakpoint of current window. |

## isAvailable

```TypeScript
isAvailable(): boolean
```

Check whether the UIContext object is available.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-isAvailable(): boolean--><!--Device-UIContext-isAvailable(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the UIContext object is available. |

## isEasySplit

```TypeScript
isEasySplit(): boolean
```

Checks whether the current UI instance is in easy split mode.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-isEasySplit(): boolean--><!--Device-UIContext-isEasySplit(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the current UI instance is in easy split mode; returns false otherwise. |

## isFollowingSystemFontScale

```TypeScript
isFollowingSystemFontScale(): boolean
```

Checks whether current font scale follows the system.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-isFollowingSystemFontScale(): boolean--><!--Device-UIContext-isFollowingSystemFontScale(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if current font scale follows the system; returns false otherwise. |

## keyframeAnimateTo

```TypeScript
keyframeAnimateTo(param: KeyframeAnimateParam, keyframes: Array<KeyframeState>): void
```

Defining keyframe animation function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-keyframeAnimateTo(param: KeyframeAnimateParam, keyframes: Array<KeyframeState>): void--><!--Device-UIContext-keyframeAnimateTo(param: KeyframeAnimateParam, keyframes: Array<KeyframeState>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | KeyframeAnimateParam | Yes | overall animation parameters |
| keyframes | Array&lt;KeyframeState&gt; | Yes | all keyframe states |

## lpx2px

```TypeScript
lpx2px(value: double): double
```

Converts a value in lpx units to a value in px.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-lpx2px(value: double): double--><!--Device-UIContext-lpx2px(value: double): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| double |  |

## openBindSheet

```TypeScript
openBindSheet(bindSheetContent: ComponentContentBase,
    sheetOptions?: SheetOptions, targetId?: int): Promise<void>
```

Open the BindSheet.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-openBindSheet(bindSheetContent: ComponentContentBase,    sheetOptions?: SheetOptions, targetId?: int): Promise<void>--><!--Device-UIContext-openBindSheet(bindSheetContent: ComponentContentBase,    sheetOptions?: SheetOptions, targetId?: int): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bindSheetContent | [ComponentContentBase](arkts-na-componentcontent-componentcontentbase-c.md) | Yes | The content of BindSheet. |
| sheetOptions | SheetOptions | No | The options of sheet. |
| targetId | int | No | The uniqueId of the FrameNode to which BindSheet is attached. <br>Value range:(0, +∞) |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [120001](../../apis-arkui/errorcode-bindSheet.md#120001-incorrect-bindsheetcontent) | The bindSheetContent is incorrect. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [120002](../../apis-arkui/errorcode-bindSheet.md#120002-modal-for-bindsheetcontent-already-exists) | The bindSheetContent already exists. |
| [120005](../../apis-arkui/errorcode-bindSheet.md#120005-node-specified-by-targetid-is-not-in-the-component-tree) | The node of targetId is not in the component tree. |
| [120004](../../apis-arkui/errorcode-bindSheet.md#120004-specified-targetid-does-not-exist) | The targetId does not exist. |
| [120006](../../apis-arkui/errorcode-bindSheet.md#120006-node-specified-by-targetid-is-not-a-child-of-a-page-node-or-navdestination-node) | The node of targetId is not a child of the page node or NavDestination node. |

## postDelayedFrameCallback

```TypeScript
postDelayedFrameCallback(frameCallback: FrameCallback, delayTime: long): void
```

Post a frame callback to run on the next frame after the specified delay.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-postDelayedFrameCallback(frameCallback: FrameCallback, delayTime: long): void--><!--Device-UIContext-postDelayedFrameCallback(frameCallback: FrameCallback, delayTime: long): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| frameCallback | [FrameCallback](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-framecallback-c.md) | Yes | The frame callback to run on the next frame. |
| delayTime | long | Yes | The delay time in milliseconds, |

## postFrameCallback

```TypeScript
postFrameCallback(frameCallback: FrameCallback): void
```

Post a frame callback to run on the next frame.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-postFrameCallback(frameCallback: FrameCallback): void--><!--Device-UIContext-postFrameCallback(frameCallback: FrameCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| frameCallback | [FrameCallback](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-framecallback-c.md) | Yes | The frame callback to run on the next frame. |

## px2fp

```TypeScript
px2fp(value: double): double
```

Converts a value in px units to a value in fp.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-px2fp(value: double): double--><!--Device-UIContext-px2fp(value: double): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| double |  |

## px2lpx

```TypeScript
px2lpx(value: double): double
```

Converts a value in px units to a value in lpx.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-px2lpx(value: double): double--><!--Device-UIContext-px2lpx(value: double): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| double |  |

## px2vp

```TypeScript
px2vp(value: double): double
```

Converts a value in px units to a value in vp.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-px2vp(value: double): double--><!--Device-UIContext-px2vp(value: double): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| double |  |

## removeLocalInputEventMonitor

```TypeScript
removeLocalInputEventMonitor(monitor: InputEventMonitor): void
```

Removes a local input event monitor. **Important Notes**: - Only Monitor objects returned by addLocalInputEventMonitor can be removed. - Cannot unregister a monitor by manually constructing an object. - If an invalid object is passed, the system silently ignores it.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-removeLocalInputEventMonitor(monitor: InputEventMonitor): void--><!--Device-UIContext-removeLocalInputEventMonitor(monitor: InputEventMonitor): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| monitor | InputEventMonitor | Yes | Monitor identifier object (returned by addLocalInputEventMonitor). |

## requireDynamicSyncScene

```TypeScript
requireDynamicSyncScene(id: string): Array<DynamicSyncScene>
```

Require DynamicSyncScene by id.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-requireDynamicSyncScene(id: string): Array<DynamicSyncScene>--><!--Device-UIContext-requireDynamicSyncScene(id: string): Array<DynamicSyncScene>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | The id of DynamicSyncScene. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[DynamicSyncScene](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-dynamicsyncscene-c.md)&gt; | The instance of SwiperDynamicSyncScene. |

## resolveUIContext

```TypeScript
static resolveUIContext(): ResolvedUIContext
```

Resolves a UIContext using priority strategy. Resolves and returns a UIContext instance following a predefined priority sequence. resolution rules in order: <br>1. the UIContext with current calling scope <br>2. Returns the unique UIContext if only one UI instance exists. <br>3. Returns the UIContext of the last focused UI instance if one exists. <br>4. Returns the UIContext of the last foregrounded UI instance if one exists. <br>5. Returns the UIContext of the most recently created UI instance if any UI instance exists. <br>6. Returns an invalid UIContext instance if none of the above conditions are met.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-static resolveUIContext(): ResolvedUIContext--><!--Device-UIContext-static resolveUIContext(): ResolvedUIContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [ResolvedUIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-resolveduicontext-c.md) | ResolvedUIContext instance |

## runScopedTask

```TypeScript
runScopedTask(callback: () => void): void
```

Run custom functions inside the UIContext scope.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-runScopedTask(callback: () => void): void--><!--Device-UIContext-runScopedTask(callback: () => void): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | () =&gt; void | Yes | The function called through UIContext. |

## setCustomKeyboardContinueFeature

```TypeScript
setCustomKeyboardContinueFeature(feature: CustomKeyboardContinueFeature): void
```

Set custom keyboard continue feature.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-setCustomKeyboardContinueFeature(feature: CustomKeyboardContinueFeature): void--><!--Device-UIContext-setCustomKeyboardContinueFeature(feature: CustomKeyboardContinueFeature): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| feature | [CustomKeyboardContinueFeature](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-customkeyboardcontinuefeature-e.md) | Yes | The custom keyboard continue feature. |

## setImageCacheCount

```TypeScript
setImageCacheCount(value: int): void
```

Set image cache capacity of decoded image count. if not set, the application will not cache any decoded image.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-setImageCacheCount(value: int): void--><!--Device-UIContext-setImageCacheCount(value: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | capacity of decoded image count. |

## setImageRawDataCacheSize

```TypeScript
setImageRawDataCacheSize(value: int): void
```

Set image cache capacity of raw image data size in bytes before decode. if not set, the application will not cache any raw image data.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-setImageRawDataCacheSize(value: int): void--><!--Device-UIContext-setImageRawDataCacheSize(value: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | capacity of raw image data size in bytes. |

## setKeyboardAvoidMode

```TypeScript
setKeyboardAvoidMode(value: KeyboardAvoidMode): void
```

Set KeyboardAvoidMode. The default mode is KeyboardAvoidMode.OFFSET

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-setKeyboardAvoidMode(value: KeyboardAvoidMode): void--><!--Device-UIContext-setKeyboardAvoidMode(value: KeyboardAvoidMode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [KeyboardAvoidMode](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-keyboardavoidmode-e.md) | Yes | The mode of keyboard avoid. |

## setOverlayManagerOptions

```TypeScript
setOverlayManagerOptions(options: OverlayManagerOptions): boolean
```

Init OverlayManager.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-setOverlayManagerOptions(options: OverlayManagerOptions): boolean--><!--Device-UIContext-setOverlayManagerOptions(options: OverlayManagerOptions): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [OverlayManagerOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-overlaymanageroptions-i.md) | Yes | Options. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if it is called first and before getting an OverlayManager instance; returns false otherwise. |

## setPixelRoundMode

```TypeScript
setPixelRoundMode(mode: PixelRoundMode): void
```

Set the pixel round mode of the system. The default mode is PixelRoundMode.PIXEL_ROUND_ON_LAYOUT_FINISH.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-setPixelRoundMode(mode: PixelRoundMode): void--><!--Device-UIContext-setPixelRoundMode(mode: PixelRoundMode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | PixelRoundMode | Yes | The mode of pixel round. |

## setResourceManagerCacheMaxCountForHSP

```TypeScript
static setResourceManagerCacheMaxCountForHSP(count: int): void
```

Set the upper limit for the cache count of HSP resource management objects. If the upper limit of the cache is set too high, there is a risk of excessive memory overhead. It is recommended to configure it according to actual needs.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-static setResourceManagerCacheMaxCountForHSP(count: int): void--><!--Device-UIContext-static setResourceManagerCacheMaxCountForHSP(count: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| count | int | Yes | The cache limit of resource manager for HSP, must be non negative integers. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100101](../../apis-arkui/errorcode-uicontext.md#100101-invalid-negative-parameter-value) | The parameter is less than 0. |
| [100103](../../apis-arkui/errorcode-uicontext.md#100103-invalid-thread-context) | The function cannot be called from a non main thread. @static |
| [100102](../../apis-arkui/errorcode-uicontext.md#100102-incorrect-parameter-type) | The parameter value cannot be a floating point number. |

## setTextSelectionClearPolicy

```TypeScript
setTextSelectionClearPolicy(policy: TextSelectionClearPolicy): void
```

Sets the text selection clear policy for text component. Default policy: **TextSelectionClearPolicy.KEEP_SELECTED_TEXT_ON_EXTERNAL_TOUCH**

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-setTextSelectionClearPolicy(policy: TextSelectionClearPolicy): void--><!--Device-UIContext-setTextSelectionClearPolicy(policy: TextSelectionClearPolicy): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| policy | [TextSelectionClearPolicy](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-textselectionclearpolicy-e.md) | Yes | The text selection clear policy. |

## setUIStates

```TypeScript
setUIStates(callback: VoidCallback): void
```

Thread-safe UI state variables updates interface.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-setUIStates(callback: VoidCallback): void--><!--Device-UIContext-setUIStates(callback: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | VoidCallback | Yes | The callback function to be executed in the UI thread. |

## showActionSheet

```TypeScript
showActionSheet(value: ActionSheetOptions): void
```

actionSheet display.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-showActionSheet(value: ActionSheetOptions): void--><!--Device-UIContext-showActionSheet(value: ActionSheetOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ActionSheetOptions | Yes | Options. |

## showAlertDialog

```TypeScript
showAlertDialog(
    options: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions): void
```

alertDialog display.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-showAlertDialog(    options: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions): void--><!--Device-UIContext-showAlertDialog(    options: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | AlertDialogParamWithConfirm \| AlertDialogParamWithButtons \| AlertDialogParamWithOptions | Yes | Options. |

## showDatePickerDialog

```TypeScript
showDatePickerDialog(options: DatePickerDialogOptions): void
```

datePickerDialog display.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-showDatePickerDialog(options: DatePickerDialogOptions): void--><!--Device-UIContext-showDatePickerDialog(options: DatePickerDialogOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | DatePickerDialogOptions | Yes | Options. |

## showTextPickerDialog

```TypeScript
showTextPickerDialog(style: TextPickerDialogOptions | TextPickerDialogOptionsExt): void
```

textPickerDialog display.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-showTextPickerDialog(style: TextPickerDialogOptions | TextPickerDialogOptionsExt): void--><!--Device-UIContext-showTextPickerDialog(style: TextPickerDialogOptions | TextPickerDialogOptionsExt): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | TextPickerDialogOptions \| TextPickerDialogOptionsExt | Yes | Dialog style. |

## showTimePickerDialog

```TypeScript
showTimePickerDialog(options: TimePickerDialogOptions): void
```

timePickerDialog display.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-showTimePickerDialog(options: TimePickerDialogOptions): void--><!--Device-UIContext-showTimePickerDialog(options: TimePickerDialogOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | TimePickerDialogOptions | Yes | Options. |

## unbindTabsFromNestedScrollable

```TypeScript
unbindTabsFromNestedScrollable(tabsController: TabsController, parentScroller: Scroller,
    childScroller: Scroller): void
```

Unbind tabs from nested scrollable container components.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-unbindTabsFromNestedScrollable(tabsController: TabsController, parentScroller: Scroller,    childScroller: Scroller): void--><!--Device-UIContext-unbindTabsFromNestedScrollable(tabsController: TabsController, parentScroller: Scroller,    childScroller: Scroller): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tabsController | TabsController | Yes | The controller of the tabs. |
| parentScroller | Scroller | Yes | The controller of the parent scrollable container component. |
| childScroller | Scroller | Yes | The controller of the child scrollable container component. |

## unbindTabsFromScrollable

```TypeScript
unbindTabsFromScrollable(tabsController: TabsController, scroller: Scroller): void
```

Unbind tabs from scrollable container component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-unbindTabsFromScrollable(tabsController: TabsController, scroller: Scroller): void--><!--Device-UIContext-unbindTabsFromScrollable(tabsController: TabsController, scroller: Scroller): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tabsController | TabsController | Yes | The controller of the tabs. |
| scroller | Scroller | Yes | The controller of the scrollable container component. |

## updateBindSheet

```TypeScript
updateBindSheet(bindSheetContent: ComponentContentBase,
    sheetOptions: SheetOptions, partialUpdate?: boolean): Promise<void>
```

Update the BindSheet with sheetOptions.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-updateBindSheet(bindSheetContent: ComponentContentBase,    sheetOptions: SheetOptions, partialUpdate?: boolean): Promise<void>--><!--Device-UIContext-updateBindSheet(bindSheetContent: ComponentContentBase,    sheetOptions: SheetOptions, partialUpdate?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bindSheetContent | [ComponentContentBase](arkts-na-componentcontent-componentcontentbase-c.md) | Yes | The content of BindSheet. |
| sheetOptions | SheetOptions | Yes | The update options of sheet. |
| partialUpdate | boolean | No | If true, only the specified properties in the sheetOptions are updated, otherwise the rest of the properties are overwritten with the default values. Default value is false. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [120001](../../apis-arkui/errorcode-bindSheet.md#120001-incorrect-bindsheetcontent) | The bindSheetContent is incorrect. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [120003](../../apis-arkui/errorcode-bindSheet.md#120003-no-matching-modal-found) | The bindSheetContent cannot be found. |

## vp2px

```TypeScript
vp2px(value: double): double
```

Converts a value in vp units to a value in px.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-vp2px(value: double): double--><!--Device-UIContext-vp2px(value: double): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| double |  |

