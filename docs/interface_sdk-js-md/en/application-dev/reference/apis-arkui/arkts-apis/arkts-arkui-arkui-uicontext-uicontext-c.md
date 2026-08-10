# UIContext

UIContext类

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class UIContext--><!--Device-unnamed-export declare class UIContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from 'kits/@kit.ArkUI';
```

## addLocalInputEventMonitor

```TypeScript
addLocalInputEventMonitor(eventMask: int, listener: InputEventListener): InputEventMonitor
```

注册本地输入事件监视器。接口名中的“Local”表示监视器只在当前UIContext内有效。并且不影响其他UIContext实例。每个UIContext都维护自己独立的监视器列表。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-addLocalInputEventMonitor(eventMask: int, listener: InputEventListener): InputEventMonitor--><!--Device-UIContext-addLocalInputEventMonitor(eventMask: int, listener: InputEventListener): InputEventMonitor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventMask | int | Yes | 事件类型掩码，指定要监视的事件类型 位运算。 |
| listener | [InputEventListener](../arkts-components/arkts-arkui-inputeventlistener-t.md) | Yes | 事件监听器回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [InputEventMonitor](../arkts-components/arkts-arkui-inputeventmonitor-i.md) | Unique identifier object for the monitor, used for subsequent cancellation of registration. |

## animateTo

```TypeScript
animateTo(value: AnimateParam, event: () => void): void
```

Defining animation function

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-animateTo(value: AnimateParam, event: () => void): void--><!--Device-UIContext-animateTo(value: AnimateParam, event: () => void): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [AnimateParam](../arkts-components/arkts-arkui-animateparam-i.md) | Yes | parameters for animation. |
| event | () =&gt; void | Yes | the closure base on which, the system will create animation automatically |

## animateToImmediately

```TypeScript
animateToImmediately(param: AnimateParam, processor: VoidCallback): void
```

通过 **UIContext** 对象提供提供显式动画立即下发功能。当多个属性动画同时加载时，您可以调用此 API 来立即执行由处理函数引起的视图状态变化的过渡动画。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-animateToImmediately(param: AnimateParam, processor: VoidCallback): void--><!--Device-UIContext-animateToImmediately(param: AnimateParam, processor: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | [AnimateParam](../arkts-components/arkts-arkui-animateparam-i.md) | Yes | 设置动画效果相关参数 |
| processor | [VoidCallback](arkts-arkui-voidcallback-t.md) | Yes | 指定显示动画的处理函数，在该函数中导致的状态变化系统会自动插入过渡动画。 |

## bindTabsToNestedScrollable

```TypeScript
bindTabsToNestedScrollable(tabsController: TabsController, parentScroller: Scroller, childScroller: Scroller): void
```

Bind tabs to nested scrollable container components to automatically hide tab bar.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-bindTabsToNestedScrollable(tabsController: TabsController, parentScroller: Scroller, childScroller: Scroller): void--><!--Device-UIContext-bindTabsToNestedScrollable(tabsController: TabsController, parentScroller: Scroller, childScroller: Scroller): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tabsController | [TabsController](../arkts-components/arkts-arkui-tabscontroller-c.md) | Yes | The controller of the tabs. |
| parentScroller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | Yes | The controller of the parent scrollable container component. |
| childScroller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | Yes | The controller of the child scrollable container component. |

## bindTabsToScrollable

```TypeScript
bindTabsToScrollable(tabsController: TabsController, scroller: Scroller): void
```

Bind tabs to scrollable container component to automatically hide tab bar.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-bindTabsToScrollable(tabsController: TabsController, scroller: Scroller): void--><!--Device-UIContext-bindTabsToScrollable(tabsController: TabsController, scroller: Scroller): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tabsController | [TabsController](../arkts-components/arkts-arkui-tabscontroller-c.md) | Yes | The controller of the tabs. |
| scroller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | Yes | The controller of the scrollable container component. |

## closeBindSheet

```TypeScript
closeBindSheet(bindSheetContent: ComponentContentBase): Promise<void>
```

关闭BindSheet半模态.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-closeBindSheet(bindSheetContent: ComponentContentBase): Promise<void>--><!--Device-UIContext-closeBindSheet(bindSheetContent: ComponentContentBase): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bindSheetContent | [ComponentContentBase](arkts-arkui-componentcontent-componentcontentbase-c.md) | Yes | BindSheet半模态的内容 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 120001 | The bindSheetContent is incorrect. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 120003 | The bindSheetContent cannot be found. |

## constructor

```TypeScript
constructor()
```

UIContext 构造函数

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

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

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-createAnimator(options: AnimatorOptions | SimpleAnimatorOptions): AnimatorResult--><!--Device-UIContext-createAnimator(options: AnimatorOptions | SimpleAnimatorOptions): AnimatorResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [AnimatorOptions](arkts-arkui-animator-animatoroptions-i.md) \| SimpleAnimatorOptions | Yes | Options. |

**Return value:**

| Type | Description |
| --- | --- |
| [AnimatorResult](arkts-arkui-animator-animatorresult-i.md) |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## createUIContextWithoutWindow

```TypeScript
static createUIContextWithoutWindow(context: common.UIAbilityContext | common.ExtensionContext) : UIContext | undefined
```

Create a UI instance singleton without window and get its UIContext object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-static createUIContextWithoutWindow(context: common.UIAbilityContext | common.ExtensionContext) : UIContext | undefined--><!--Device-UIContext-static createUIContextWithoutWindow(context: common.UIAbilityContext | common.ExtensionContext) : UIContext | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | common.UIAbilityContext \| common.ExtensionContext | Yes | UIAbilityContext or ExtensionContext. |

**Return value:**

| Type | Description |
| --- | --- |
| [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | object UIContext, or undefined when failed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100001 | Internal error. @static |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. The number of parameters is incorrect. &lt;br&gt; 2. Invalid parameter type of context. |

## destroyUIContextWithoutWindow

```TypeScript
static destroyUIContextWithoutWindow(): void
```

Destroy the UI instance singleton without window.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-dispatchKeyEvent(node: int | string, event: KeyEvent): boolean--><!--Device-UIContext-dispatchKeyEvent(node: int | string, event: KeyEvent): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | int \| string | Yes | The uniqueId or inspector key of the target FrameNode. |
| event | [KeyEvent](../arkts-components/arkts-arkui-keyevent-i.md) | Yes | The keyboard event. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns whether the key event is consumed. |

## enableEventPassthrough

```TypeScript
enableEventPassthrough(enabled: boolean | undefined, eventType: RawInputEventType): void
```

是否启用或禁用事件直通。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-enableEventPassthrough(enabled: boolean | undefined, eventType: RawInputEventType): void--><!--Device-UIContext-enableEventPassthrough(enabled: boolean | undefined, eventType: RawInputEventType): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes | 启用或禁用事件直通。默认值为false。 |
| eventType | [RawInputEventType](arkts-arkui-rawinputeventtype-e.md) | Yes | 原始输入事件的类型。 |

## enableSwipeBack

```TypeScript
enableSwipeBack(enabled: boolean | undefined): void
```

设置是否支持应用内横向滑动返回上一级。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-enableSwipeBack(enabled: boolean | undefined): void--><!--Device-UIContext-enableSwipeBack(enabled: boolean | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes | 是否支持应用内横向滑动返回，默认值为true。&lt;br&gt;当值为true时，支持应用内横向滑动返回。 &lt;br&gt;当值为false时，不支持应用内横向滑动返回。 |

## fp2px

```TypeScript
fp2px(value: double): double
```

Converts a value in fp units to a value in px.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

获取所有当前活跃的 UIContext 实例。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-static getAllUIContexts(): UIContext[]--><!--Device-UIContext-static getAllUIContexts(): UIContext[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md)[] | An array containing all valid UIContext instances, returns an empty array if no contexts are available. |

## getAtomicServiceBar

```TypeScript
getAtomicServiceBar(): Nullable<AtomicServiceBar>
```

获取AtomicServiceBar。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getAtomicServiceBar(): Nullable<AtomicServiceBar>--><!--Device-UIContext-getAtomicServiceBar(): Nullable<AtomicServiceBar>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Nullable](arkts-arkui-nullable-t.md)&lt;AtomicServiceBar&gt; | The atomic service bar. |

## getAttachedFrameNodeById

```TypeScript
getAttachedFrameNodeById(id: string): FrameNode | null
```

通过组件id获取当前窗口上的FrameNode。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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
| [FrameNode](arkts-arkui-framenode-t.md) | The instance of FrameNode. |

## getCallingScopeUIContext

```TypeScript
static getCallingScopeUIContext(): UIContext | undefined
```

获取与当前调用作用域关联的 UIContext

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-static getCallingScopeUIContext(): UIContext | undefined--><!--Device-UIContext-static getCallingScopeUIContext(): UIContext | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | The UIContext for the current calling scope, or undefined if no context can be determined from the call stack. |

## getComponentSnapshot

```TypeScript
getComponentSnapshot(): ComponentSnapshot
```

获取ComponentSnapshot对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getComponentSnapshot(): ComponentSnapshot--><!--Device-UIContext-getComponentSnapshot(): ComponentSnapshot-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [ComponentSnapshot](arkts-arkui-arkui-uicontext-componentsnapshot-c.md) | the ComponentSnapshot |

## getComponentUtils

```TypeScript
getComponentUtils(): ComponentUtils
```

get object ComponentUtils.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getComponentUtils(): ComponentUtils--><!--Device-UIContext-getComponentUtils(): ComponentUtils-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [ComponentUtils](arkts-arkui-arkui-uicontext-componentutils-c.md) | object ComponentUtils. |

## getContextMenuController

```TypeScript
getContextMenuController(): ContextMenuController
```

获取ContextMenuController对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getContextMenuController(): ContextMenuController--><!--Device-UIContext-getContextMenuController(): ContextMenuController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [ContextMenuController](arkts-arkui-arkui-uicontext-contextmenucontroller-c.md) | object context menu controller. |

## getCursorController

```TypeScript
getCursorController(): CursorController
```

获取CursorController对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getCursorController(): CursorController--><!--Device-UIContext-getCursorController(): CursorController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [CursorController](arkts-arkui-arkui-uicontext-cursorcontroller-c.md) | object cursor controller. |

## getDialogPresenter

```TypeScript
getDialogPresenter(): DialogPresenter
```

获取Dialog对象。

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getDialogPresenter(): DialogPresenter--><!--Device-UIContext-getDialogPresenter(): DialogPresenter-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [DialogPresenter](arkts-arkui-arkui-uicontext-dialogpresenter-c.md) | Dialog object. |

## getDragController

```TypeScript
getDragController(): DragController
```

获取DragController对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getDragController(): DragController--><!--Device-UIContext-getDragController(): DragController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [DragController](arkts-arkui-arkui-uicontext-dragcontroller-c.md) | the DragController |

## getFilteredInspectorTree

```TypeScript
getFilteredInspectorTree(filters?: Array<string>): string
```

获取组件树和组件属性。该接口处理时间较长，适用于&lt;br&gt;testing scenarios only.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getFilteredInspectorTree(filters?: Array<string>): string--><!--Device-UIContext-getFilteredInspectorTree(filters?: Array<string>): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filters | Array&lt;string&gt; | No | List of component attributes used for filtering. Currently, only the following filter fields are supported: &lt;br&gt;**"id"**: unique ID of the component. &lt;br&gt;**"src"**: source of the resource. &lt;br&gt;**"content"**: information or data contained in the element, component, or object. &lt;br&gt;**"editable"**: whether the component is editable. &lt;br&gt;**"scrollable"**: whether the component is scrollable. &lt;br&gt;**"selectable"**: whether the component is selectable. &lt;br&gt;**"focusable"**: whether the component is focusable. &lt;br&gt;**"focused"**: whether the component is currently focused. &lt;br&gt;If **filters** includes one or more fields, unspecified fields will be filtered out from the results. &lt;br&gt;If **filters** is not provided or is an empty array, none of the aforementioned fields will be filtered out. &lt;br&gt;Other filter fields are used only in testing scenarios. |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON string of the component tree and component attributes. For details about each field in the component, see the return value description of [getInspectorInfo]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100023 | Unable to obtain current ui context. |

## getFilteredInspectorTreeById

```TypeScript
getFilteredInspectorTreeById(id: string, depth: int, filters?: Array<string>): string
```

获取指定组件及其子组件的属性。该接口处理时间较长，&lt;br&gt;and is intended for testing scenarios only.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getFilteredInspectorTreeById(id: string, depth: int, filters?: Array<string>): string--><!--Device-UIContext-getFilteredInspectorTreeById(id: string, depth: int, filters?: Array<string>): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | [ID](arkts-arkui-common-commonmethod-i.md#id) of the target component. |
| depth | int | Yes | Number of layers of child components. If the value is **0**, the attributes of the specified component and all its child components are obtained. If the value is **1**, only the attributes of &lt;br&gt;the specified component are obtained. If the value is **2**, the attributes of the specified component and its &lt;br&gt;level-1 child components are obtained. The rest can be deduced by analogy. |
| filters | Array&lt;string&gt; | No | List of component attributes used for filtering. Currently, only the following filter fields are supported: &lt;br&gt;**"id"**: unique ID of the component. &lt;br&gt;**"src"**: source of the resource. &lt;br&gt;**"content"**: information or data contained in the element, component, or object. &lt;br&gt;**"editable"**: whether the component is editable. &lt;br&gt;**"scrollable"**: whether the component is scrollable. &lt;br&gt;**"selectable"**: whether the component is selectable. &lt;br&gt;**"focusable"**: whether the component is focusable. &lt;br&gt;**"focused"**: whether the component is currently focused. &lt;br&gt;If **filters** includes one or more fields, unspecified fields will be filtered out from the results. &lt;br&gt;If **filters** is not provided or is an empty array, none of the aforementioned fields will be filtered out. &lt;br&gt;Other filter fields are used only in testing scenarios. |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON string of the attributes of the specified component and its child components. For details about each field in the component, see the return value description of [getInspectorInfo]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100023 | Unable to obtain current ui context. |
| 100024 | The parameter depth must be greater than 0. |

## getFocusController

```TypeScript
getFocusController(): FocusController
```

获取FocusController对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getFocusController(): FocusController--><!--Device-UIContext-getFocusController(): FocusController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [FocusController](arkts-arkui-arkui-uicontext-focuscontroller-c.md) | the FocusController |

## getFont

```TypeScript
getFont(): Font
```

get object font.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getFont(): Font--><!--Device-UIContext-getFont(): Font-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Font](arkts-arkui-arkui-uicontext-font-c.md) | object Font. |

## getFrameNodeById

```TypeScript
getFrameNodeById(id: string): FrameNode | null
```

通过组件id获取FrameNode。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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
| [FrameNode](arkts-arkui-framenode-t.md) | The instance of FrameNode. |

## getFrameNodeByUniqueId

```TypeScript
getFrameNodeByUniqueId(id: int): FrameNode | null
```

通过uniqueId获取FrameNode。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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
| [FrameNode](arkts-arkui-framenode-t.md) | The FrameNode with the target uniqueId, or null if the frameNode is not existed. |

## getHostContext

```TypeScript
getHostContext(): Context | undefined
```

获取ability的上下文。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getHostContext(): Context | undefined--><!--Device-UIContext-getHostContext(): Context | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) |  |

## getId

```TypeScript
getId(): int
```

获取UI实例的id。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

获取KeyboardAvoidMode。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getKeyboardAvoidMode(): KeyboardAvoidMode--><!--Device-UIContext-getKeyboardAvoidMode(): KeyboardAvoidMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [KeyboardAvoidMode](arkts-arkui-arkui-uicontext-keyboardavoidmode-e.md) | The mode of keyboard avoid. |

## getLastFocusedUIContext

```TypeScript
static getLastFocusedUIContext(): UIContext | undefined
```

获取最后获焦的 UI 实例的 UIContext（如果存在）。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-static getLastFocusedUIContext(): UIContext | undefined--><!--Device-UIContext-static getLastFocusedUIContext(): UIContext | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | The UIContext of the last focused UI instance or undefined if no one exists. |

## getLastForegroundUIContext

```TypeScript
static getLastForegroundUIContext(): UIContext | undefined
```

获取最后处于前台的 UI 实例的 UIContext（如果存在）。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-static getLastForegroundUIContext(): UIContext | undefined--><!--Device-UIContext-static getLastForegroundUIContext(): UIContext | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | The UIContext of the last foregrounded UI instance or undefined if no one exists |

## getMagnifier

```TypeScript
getMagnifier(): Magnifier
```

获取放大镜对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getMagnifier(): Magnifier--><!--Device-UIContext-getMagnifier(): Magnifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Magnifier](arkts-arkui-arkui-uicontext-magnifier-c.md) | Magnifier instance obtained. |

## getMaxFontScale

```TypeScript
getMaxFontScale(): double
```

获取字体最大缩放比例。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

获取MeasureUtils对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getMeasureUtils(): MeasureUtils--><!--Device-UIContext-getMeasureUtils(): MeasureUtils-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [MeasureUtils](arkts-arkui-arkui-uicontext-measureutils-c.md) | the MeasureUtils |

## getMediaQuery

```TypeScript
getMediaQuery(): MediaQuery
```

get object mediaQuery.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getMediaQuery(): MediaQuery--><!--Device-UIContext-getMediaQuery(): MediaQuery-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [MediaQuery](arkts-arkui-system-mediaquery-mediaquery-c.md) | object MediaQuery. |

## getNavigationInfoByUniqueId

```TypeScript
getNavigationInfoByUniqueId(id: int): observer.NavigationInfo | undefined
```

通过uniqueId获取frameNode的navigation信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

获取OverlayManager对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getOverlayManager(): OverlayManager--><!--Device-UIContext-getOverlayManager(): OverlayManager-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [OverlayManager](arkts-arkui-arkui-uicontext-overlaymanager-c.md) | object OverlayManager. |

## getOverlayManagerOptions

```TypeScript
getOverlayManagerOptions(): OverlayManagerOptions
```

获取OverlayManagerOptions对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getOverlayManagerOptions(): OverlayManagerOptions--><!--Device-UIContext-getOverlayManagerOptions(): OverlayManagerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [OverlayManagerOptions](arkts-arkui-arkui-uicontext-overlaymanageroptions-i.md) | object OverlayManagerOptions. |

## getPageInfoByUniqueId

```TypeScript
getPageInfoByUniqueId(id: int): PageInfo
```

通过uniqueId获取frameNode的页面信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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
| [PageInfo](arkts-arkui-arkui-uicontext-pageinfo-i.md) | The page information of the frameNode with the target uniqueId, includes navDestination and router page information. If the frame node does not have navDestination and router page information, it will return an empty object. |

## getPageRootNode

```TypeScript
getPageRootNode(): FrameNode | null
```

获取UIContext对应页面的根节点。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getPageRootNode(): FrameNode | null--><!--Device-UIContext-getPageRootNode(): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [FrameNode](arkts-arkui-framenode-t.md) | The root node of the corresponding page of the UIContext, or null if no root node exists. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 120007 | The UIContext is not available. |

## getPixelRoundMode

```TypeScript
getPixelRoundMode(): PixelRoundMode
```

获取系统的像素取整模式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getPixelRoundMode(): PixelRoundMode--><!--Device-UIContext-getPixelRoundMode(): PixelRoundMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [PixelRoundMode](arkts-arkui-pixelroundmode-e.md) | the mode of pixel round. |

## getPromptAction

```TypeScript
getPromptAction(): PromptAction
```

get object PromptAction.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getPromptAction(): PromptAction--><!--Device-UIContext-getPromptAction(): PromptAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [PromptAction](arkts-arkui-arkui-uicontext-promptaction-c.md) | object PromptAction. |

## getRouter

```TypeScript
getRouter(): Router
```

get object router.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getRouter(): Router--><!--Device-UIContext-getRouter(): Router-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Router](arkts-arkui-arkui-uicontext-router-c.md) | object Router. |

## getSharedLocalStorage

```TypeScript
getSharedLocalStorage(): LocalStorage | undefined
```

获取当前stage共享的LocalStorage实例。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getSharedLocalStorage(): LocalStorage | undefined--><!--Device-UIContext-getSharedLocalStorage(): LocalStorage | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [LocalStorage](arkts-arkui-localstorage-c.md) |  |

## getSmartGestureController

```TypeScript
getSmartGestureController(): SmartGestureController
```

获取智能手势控制器。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getSmartGestureController(): SmartGestureController--><!--Device-UIContext-getSmartGestureController(): SmartGestureController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [SmartGestureController](arkts-arkui-arkui-uicontext-smartgesturecontroller-c.md) | object smart gesture controller. |

## getTextMenuController

```TypeScript
getTextMenuController(): TextMenuController
```

获取TextMenuController对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getTextMenuController(): TextMenuController--><!--Device-UIContext-getTextMenuController(): TextMenuController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [TextMenuController](arkts-arkui-arkui-uicontext-textmenucontroller-c.md) | object text menu controller. |

## getUIInspector

```TypeScript
getUIInspector(): UIInspector
```

获取**UIInspector**对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getUIInspector(): UIInspector--><!--Device-UIContext-getUIInspector(): UIInspector-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [UIInspector](arkts-arkui-arkui-uicontext-uiinspector-c.md) | 返回UIInspector实例对象。 |

## getUIObserver

```TypeScript
getUIObserver(): UIObserver
```

获取UIObserver对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getUIObserver(): UIObserver--><!--Device-UIContext-getUIObserver(): UIObserver-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [UIObserver](arkts-arkui-arkui-uicontext-uiobserver-c.md) | The UI observer. |

## getWindowHeightBreakpoint

```TypeScript
getWindowHeightBreakpoint(): HeightBreakpoint
```

获取当前实例所在窗口的高度断点。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getWindowHeightBreakpoint(): HeightBreakpoint--><!--Device-UIContext-getWindowHeightBreakpoint(): HeightBreakpoint-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [HeightBreakpoint](arkts-arkui-heightbreakpoint-e.md) | The height breakpoint of current window. |

## getWindowId

```TypeScript
getWindowId(): int | undefined
```

获取当前UIContext所属的窗口ID。&lt;p&gt;**注意**：如果当前UIContext处于宿主进程中运行的UIExtensionAbility内，此方法将返回宿主应用程序的顶层窗口ID。&lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

获取当前实例所在窗口的名称。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

获取当前实例所在窗口的宽度断点。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-getWindowWidthBreakpoint(): WidthBreakpoint--><!--Device-UIContext-getWindowWidthBreakpoint(): WidthBreakpoint-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [WidthBreakpoint](arkts-arkui-widthbreakpoint-e.md) | The width breakpoint of current window. |

## isAvailable

```TypeScript
isAvailable(): boolean
```

检查UIContext对象是否可用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-isAvailable(): boolean--><!--Device-UIContext-isAvailable(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the UIContext is available, otherwise false. |

## isEasySplit

```TypeScript
isEasySplit(): boolean
```

检查当前UI实例是否处于分栏模式。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

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

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-keyframeAnimateTo(param: KeyframeAnimateParam, keyframes: Array<KeyframeState>): void--><!--Device-UIContext-keyframeAnimateTo(param: KeyframeAnimateParam, keyframes: Array<KeyframeState>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | [KeyframeAnimateParam](../arkts-components/arkts-arkui-keyframeanimateparam-i.md) | Yes | overall animation parameters |
| keyframes | Array&lt;[KeyframeState](../arkts-components/arkts-arkui-keyframestate-i.md)&gt; | Yes | all keyframe states |

## lpx2px

```TypeScript
lpx2px(value: double): double
```

Converts a value in lpx units to a value in px.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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
openBindSheet(bindSheetContent: ComponentContentBase, sheetOptions?: SheetOptions, targetId?: int): Promise<void>
```

Open the BindSheet.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-openBindSheet(bindSheetContent: ComponentContentBase, sheetOptions?: SheetOptions, targetId?: int): Promise<void>--><!--Device-UIContext-openBindSheet(bindSheetContent: ComponentContentBase, sheetOptions?: SheetOptions, targetId?: int): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bindSheetContent | [ComponentContentBase](arkts-arkui-componentcontent-componentcontentbase-c.md) | Yes | The content of BindSheet. |
| sheetOptions | [SheetOptions](../arkts-components/arkts-arkui-sheetoptions-i.md) | No | The options of sheet. |
| targetId | int | No | The uniqueId of the FrameNode to which BindSheet is attached. &lt;br&gt;Value range:(0, +∞) |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 120001 | The bindSheetContent is incorrect. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 120002 | The bindSheetContent already exists. |
| 120005 | The node of targetId is not in the component tree. |
| 120004 | The targetId does not exist. |
| 120006 | The node of targetId is not a child of the page node or NavDestination node. |

## postDelayedFrameCallback

```TypeScript
postDelayedFrameCallback(frameCallback: FrameCallback, delayTime: long): void
```

Post a frame callback to run on the next frame after the specified delay.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-postDelayedFrameCallback(frameCallback: FrameCallback, delayTime: long): void--><!--Device-UIContext-postDelayedFrameCallback(frameCallback: FrameCallback, delayTime: long): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| frameCallback | [FrameCallback](arkts-arkui-arkui-uicontext-framecallback-c.md) | Yes | The frame callback to run on the next frame. |
| delayTime | long | Yes | The delay time in milliseconds, |

## postFrameCallback

```TypeScript
postFrameCallback(frameCallback: FrameCallback): void
```

Post a frame callback to run on the next frame.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-postFrameCallback(frameCallback: FrameCallback): void--><!--Device-UIContext-postFrameCallback(frameCallback: FrameCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| frameCallback | [FrameCallback](arkts-arkui-arkui-uicontext-framecallback-c.md) | Yes | The frame callback to run on the next frame. |

## px2fp

```TypeScript
px2fp(value: double): double
```

Converts a value in px units to a value in fp.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

删除本地输入事件监视器。  
**重要说明**：  
-只能移除addLocalInputEventMonitor返回的Monitor对象。  
-无法通过手动构造对象来注销监视器。  
-如果传递了一个无效的对象，系统会默默地忽略它。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-removeLocalInputEventMonitor(monitor: InputEventMonitor): void--><!--Device-UIContext-removeLocalInputEventMonitor(monitor: InputEventMonitor): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| monitor | [InputEventMonitor](../arkts-components/arkts-arkui-inputeventmonitor-i.md) | Yes | 监控标识对象（由addLocalInputEventMonitor返回）。 |

## requireDynamicSyncScene

```TypeScript
requireDynamicSyncScene(id: string): Array<DynamicSyncScene>
```

Require DynamicSyncScene by id.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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
| Array&lt;DynamicSyncScene&gt; | The instance of SwiperDynamicSyncScene. |

## resolveUIContext

```TypeScript
static resolveUIContext(): ResolvedUIContext
```

使用优先级策略解析UIContext按照预定义优先级顺序解析并返回UIContext实例。解析规则按顺序如下：&lt;br&gt;1. 返回当前调用作用域对应的UIContext&lt;br&gt;2. 当仅存在单个UI实例时，返回该唯一实例的UIContext&lt;br&gt;3. 若存在最后获得焦点的UI实例，返回其UIContext&lt;br&gt;4. 若存在最后进入前台的UI实例，返回其UIContext&lt;br&gt;5. 若存在任何UI实例，返回最大实例ID的UIContext&lt;br&gt;6. 当不满足上述所有条件时，返回未定义调用作用域内的UIContext实例

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-static resolveUIContext(): ResolvedUIContext--><!--Device-UIContext-static resolveUIContext(): ResolvedUIContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [ResolvedUIContext](arkts-arkui-arkui-uicontext-resolveduicontext-c.md) | ResolvedUIContext实例 |

## runScopedTask

```TypeScript
runScopedTask(callback: () => void): void
```

Run custom functions inside the UIContext scope.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

设置自定义键盘接续特性。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-setCustomKeyboardContinueFeature(feature: CustomKeyboardContinueFeature): void--><!--Device-UIContext-setCustomKeyboardContinueFeature(feature: CustomKeyboardContinueFeature): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| feature | [CustomKeyboardContinueFeature](arkts-arkui-arkui-uicontext-customkeyboardcontinuefeature-e.md) | Yes | 自定义键盘接续特性。 |

## setImageCacheCount

```TypeScript
setImageCacheCount(value: int): void
```

设置内存中缓存解码后图片的数量上限。if not set, the application will not cache any decoded image.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

设置内存中缓存解码前图片数据的大小上限，单位为字节。if not set, the application will not cache any raw image data.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

设置KeyboardAvoidMode。默认模式为KeyboardAvoidMode.OFFSET。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-setKeyboardAvoidMode(value: KeyboardAvoidMode): void--><!--Device-UIContext-setKeyboardAvoidMode(value: KeyboardAvoidMode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [KeyboardAvoidMode](arkts-arkui-arkui-uicontext-keyboardavoidmode-e.md) | Yes | The mode of keyboard avoid. |

## setOverlayManagerOptions

```TypeScript
setOverlayManagerOptions(options: OverlayManagerOptions): boolean
```

Init OverlayManager.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-setOverlayManagerOptions(options: OverlayManagerOptions): boolean--><!--Device-UIContext-setOverlayManagerOptions(options: OverlayManagerOptions): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [OverlayManagerOptions](arkts-arkui-arkui-uicontext-overlaymanageroptions-i.md) | Yes | Options. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if it is called first and before getting an OverlayManager instance; returns false otherwise. |

## setPixelRoundMode

```TypeScript
setPixelRoundMode(mode: PixelRoundMode): void
```

设置系统的像素取整模式。默认模式为PixelRoundMode.PIXEL_ROUND_ON_LAYOUT_FINISH。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-setPixelRoundMode(mode: PixelRoundMode): void--><!--Device-UIContext-setPixelRoundMode(mode: PixelRoundMode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [PixelRoundMode](arkts-arkui-pixelroundmode-e.md) | Yes | The mode of pixel round. |

## setResourceManagerCacheMaxCountForHSP

```TypeScript
static setResourceManagerCacheMaxCountForHSP(count: int): void
```

设置HSP资源管理对象的缓存数量上限。

如果缓存上限设置过高，存在内存开销过大的风险。建议根据实际需要进行配置。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-static setResourceManagerCacheMaxCountForHSP(count: int): void--><!--Device-UIContext-static setResourceManagerCacheMaxCountForHSP(count: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| count | int | Yes | The cache limit of resource manager for HSP, must be non-negative integers. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100101 | The parameter is less than 0. |
| 100103 | The function cannot be called from a non-main thread. @static |
| 100102 | The parameter value cannot be a floating-point number. |

## setTextSelectionClearPolicy

```TypeScript
setTextSelectionClearPolicy(policy: TextSelectionClearPolicy): void
```

设置文本组件的文本选择清除策略。默认策略：**TextSelectionClearPolicy.KEEP_ON_EXTERNAL_CLICK**。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-setTextSelectionClearPolicy(policy: TextSelectionClearPolicy): void--><!--Device-UIContext-setTextSelectionClearPolicy(policy: TextSelectionClearPolicy): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| policy | [TextSelectionClearPolicy](arkts-arkui-arkui-uicontext-textselectionclearpolicy-e.md) | Yes | 文本选择清除策略。 |

## setUIStates

```TypeScript
setUIStates(callback: VoidCallback): void
```

线程安全的UI状态变量更新接口。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-setUIStates(callback: VoidCallback): void--><!--Device-UIContext-setUIStates(callback: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) | Yes | 在UI线程中执行的回调函数。 |

## showActionSheet

```TypeScript
showActionSheet(value: ActionSheetOptions): void
```

actionSheet display.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-showActionSheet(value: ActionSheetOptions): void--><!--Device-UIContext-showActionSheet(value: ActionSheetOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ActionSheetOptions](arkts-arkui-actionsheetoptions-i.md) | Yes | Options. |

## showAlertDialog

```TypeScript
showAlertDialog(options: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions): void
```

alertDialog display.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-showAlertDialog(options: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions): void--><!--Device-UIContext-showAlertDialog(options: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [AlertDialogParamWithConfirm](arkts-arkui-alertdialogparamwithconfirm-i.md) \| AlertDialogParamWithButtons \| AlertDialogParamWithOptions | Yes | Options. |

## showDatePickerDialog

```TypeScript
showDatePickerDialog(options: DatePickerDialogOptions): void
```

datePickerDialog display.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-showDatePickerDialog(options: DatePickerDialogOptions): void--><!--Device-UIContext-showDatePickerDialog(options: DatePickerDialogOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DatePickerDialogOptions](../arkts-components/arkts-arkui-datepickerdialogoptions-i.md) | Yes | Options. |

## showTextPickerDialog

```TypeScript
showTextPickerDialog(style: TextPickerDialogOptions | TextPickerDialogOptionsExt): void
```

textPickerDialog display.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-showTextPickerDialog(style: TextPickerDialogOptions | TextPickerDialogOptionsExt): void--><!--Device-UIContext-showTextPickerDialog(style: TextPickerDialogOptions | TextPickerDialogOptionsExt): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [TextPickerDialogOptions](../arkts-components/arkts-arkui-textpickerdialogoptions-i.md) \| TextPickerDialogOptionsExt | Yes | Dialog style. |

## showTimePickerDialog

```TypeScript
showTimePickerDialog(options: TimePickerDialogOptions): void
```

timePickerDialog display.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-showTimePickerDialog(options: TimePickerDialogOptions): void--><!--Device-UIContext-showTimePickerDialog(options: TimePickerDialogOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TimePickerDialogOptions](../arkts-components/arkts-arkui-timepickerdialogoptions-i.md) | Yes | Options. |

## unbindTabsFromNestedScrollable

```TypeScript
unbindTabsFromNestedScrollable(tabsController: TabsController, parentScroller: Scroller, childScroller: Scroller): void
```

Unbind tabs from nested scrollable container components.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-unbindTabsFromNestedScrollable(tabsController: TabsController, parentScroller: Scroller, childScroller: Scroller): void--><!--Device-UIContext-unbindTabsFromNestedScrollable(tabsController: TabsController, parentScroller: Scroller, childScroller: Scroller): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tabsController | [TabsController](../arkts-components/arkts-arkui-tabscontroller-c.md) | Yes | The controller of the tabs. |
| parentScroller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | Yes | The controller of the parent scrollable container component. |
| childScroller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | Yes | The controller of the child scrollable container component. |

## unbindTabsFromScrollable

```TypeScript
unbindTabsFromScrollable(tabsController: TabsController, scroller: Scroller): void
```

Unbind tabs from scrollable container component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-unbindTabsFromScrollable(tabsController: TabsController, scroller: Scroller): void--><!--Device-UIContext-unbindTabsFromScrollable(tabsController: TabsController, scroller: Scroller): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tabsController | [TabsController](../arkts-components/arkts-arkui-tabscontroller-c.md) | Yes | The controller of the tabs. |
| scroller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | Yes | The controller of the scrollable container component. |

## updateBindSheet

```TypeScript
updateBindSheet(bindSheetContent: ComponentContentBase, sheetOptions: SheetOptions, partialUpdate?: boolean): Promise<void>
```

Update the BindSheet with sheetOptions.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIContext-updateBindSheet(bindSheetContent: ComponentContentBase, sheetOptions: SheetOptions, partialUpdate?: boolean): Promise<void>--><!--Device-UIContext-updateBindSheet(bindSheetContent: ComponentContentBase, sheetOptions: SheetOptions, partialUpdate?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bindSheetContent | [ComponentContentBase](arkts-arkui-componentcontent-componentcontentbase-c.md) | Yes | The content of BindSheet. |
| sheetOptions | [SheetOptions](../arkts-components/arkts-arkui-sheetoptions-i.md) | Yes | The update options of sheet. |
| partialUpdate | boolean | No | If true, only the specified properties in the sheetOptions are updated, otherwise the rest of the properties are overwritten with the default values. Default value is false. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 120001 | The bindSheetContent is incorrect. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 120003 | The bindSheetContent cannot be found. |

## vp2px

```TypeScript
vp2px(value: double): double
```

Converts a value in vp units to a value in px.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

