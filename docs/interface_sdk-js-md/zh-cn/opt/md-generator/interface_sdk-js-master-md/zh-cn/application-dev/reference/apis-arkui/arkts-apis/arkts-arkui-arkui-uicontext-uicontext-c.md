# UIContext

UIContext实例对象。

> **说明：**

> - 示例效果请以真机运行为准，当前DevEco Studio预览器不支持。
> 
> - 以下API需要通过对应的UIContext实例调用。获取UIContext分为三种方式，第一种是使用ohos.window中的
> [getUIContext()](../../../reference/apis-arkui/arkts-apis-window-Window.md#getuicontext10)方法获取UIContext实例，第二种是通过自定
> 义组件内置方法[getUIContext()](../../../reference/apis-arkui/arkui-ts/ts-custom-component-api.md#getuicontext)获取UIContext
> 实例，第三种是通过UIContext类的静态方法如[getCallingScopeUIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#getcallingscopeuicontext)获取UIContext实例。本文中
> UIContext对象以uiContext表示。

**起始版本：** 10

<!--Device-unnamed-export class UIContext--><!--Device-unnamed-export class UIContext-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## addLocalInputEventMonitor

```TypeScript
addLocalInputEventMonitor(eventMask: number, listener: InputEventListener): InputEventMonitor
```

注册本地输入事件监视器。

接口名中的“Local”表示监视器只在当前UIContext内有效。并且不影响其他UIContext实例。每个UIContext都维护自己独立的监视器列表。

> **说明：**
> >性能警告：不要在回调中执行耗时操作！
> >监控对象注释：
> >
> -返回的Monitor对象是系统创建的唯一标识符。
> >
> -开发人员不能主动构造或伪造此对象。
> >
> -必须保存返回的监控对象引用，以便后续取消。
> >
> -建议使用变量来保存，以免丢失引用。
> >使用示例：
> >。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-addLocalInputEventMonitor(eventMask: int, listener: InputEventListener): InputEventMonitor--><!--Device-UIContext-addLocalInputEventMonitor(eventMask: int, listener: InputEventListener): InputEventMonitor-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventMask | number | 是 |
| listener | [InputEventListener](../arkts-components/arkts-arkui-inputeventlistener-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [InputEventMonitor](../arkts-components/arkts-arkui-inputeventmonitor-i.md) |

## animateTo

```TypeScript
animateTo(value: AnimateParam, event: () => void): void
```

提供animateTo接口，用于为闭包代码中的状态变化添加过渡动画效果。

> **说明：**
> 
> - 不推荐在aboutToAppear、aboutToDisappear中调用动画。
> 
> - 如果在[aboutToAppear](../../../reference/apis-arkui/arkui-ts/ts-custom-component-lifecycle.md#abouttoappear)中调用动
> 画，自定义组件内的build还未执行，内部组件还未创建，动画时机过早，动画属性没有初值无法对组件产生动画。
> 
> - 执行[aboutToDisappear](../../../reference/apis-arkui/arkui-ts/ts-custom-component-lifecycle.md#abouttodisappear)
> 时，组件即将销毁，不能在aboutToDisappear里面做动画。
> 
> - 在组件出现和消失时，可以通过[组件内转场](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)添加动画效果。
> 
> - 组件内转场不支持的属性，可以参考[显式动画](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)中的
> [示例2](../../../reference/apis-arkui/arkui-ts/ts-explicit-animation.md#示例2动画执行结束后组件消失)，使用animateTo实现动画执行结束后组件消失的效
> 果。
> 
> - 某些场景下，在[状态管理V2](../../../ui/state-management/arkts-state-management-overview.md#状态管理v2)中使用animateTo动画，会产生异常效果，
> 具体可参考：[在状态管理V2中使用animateTo动画效果异常](../../../ui/state-management/arkts-new-local.md#在状态管理v2中使用animateto动画效果异常)。
> 
> - UIAbility从前台切换至后台时会立即结束仍在步进中的有限循环动画，从而触发动画播放完成回调[onFinish](../arkts-components/arkts-arkui-animateparam-i.md/arkts-arkui-animateparam-i.md)。
> 
> - 在设置的开发者选项中关闭过渡动画，动画会当帧结束，onFinish动画播放完成回调会立即执行，请避免在回调中加入时序相关的功能逻辑。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-animateTo(value: AnimateParam, event: () => void): void--><!--Device-UIContext-animateTo(value: AnimateParam, event: () => void): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [AnimateParam](../arkts-components/arkts-arkui-animateparam-i.md) | 是 |
| event | () =&gt; void | 是 |

## animateToImmediately

```TypeScript
animateToImmediately(param: AnimateParam, processor: Callback<void>): void
```

通过UIContext对象指定明确的动画主实例上下文，并触发显式动画立即下发。避免由于找不到实例或实例不对，导致的动画不执行或动画结束回调不执行问题。使用callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-animateToImmediately(param: AnimateParam, processor: Callback<void>): void--><!--Device-UIContext-animateToImmediately(param: AnimateParam, processor: Callback<void>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| param | [AnimateParam](../arkts-components/arkts-arkui-animateparam-i.md) | 是 |
| processor | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

## bindTabsToNestedScrollable

```TypeScript
bindTabsToNestedScrollable(tabsController: TabsController, parentScroller: Scroller, childScroller: Scroller): void
```

Bind tabs to nested scrollable container components to automatically hide tab bar.

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-bindTabsToNestedScrollable(tabsController: TabsController, parentScroller: Scroller, childScroller: Scroller): void--><!--Device-UIContext-bindTabsToNestedScrollable(tabsController: TabsController, parentScroller: Scroller, childScroller: Scroller): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tabsController | [TabsController](../arkts-components/arkts-arkui-tabscontroller-c.md) | 是 |
| parentScroller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | 是 |
| childScroller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | 是 |

## bindTabsToScrollable

```TypeScript
bindTabsToScrollable(tabsController: TabsController, scroller: Scroller): void
```

Bind tabs to scrollable container component to automatically hide tab bar.

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-bindTabsToScrollable(tabsController: TabsController, scroller: Scroller): void--><!--Device-UIContext-bindTabsToScrollable(tabsController: TabsController, scroller: Scroller): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tabsController | [TabsController](../arkts-components/arkts-arkui-tabscontroller-c.md) | 是 |
| scroller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | 是 |

## closeBindSheet

```TypeScript
closeBindSheet<T extends Object>(bindSheetContent: ComponentContent<T>): Promise<void>
```

关闭bindSheetContent对应的半模态页面，使用Promise异步回调。

> **说明：**
> 
> 使用此接口关闭半模态页面时，不会触发shouldDismiss回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-closeBindSheet<T extends Object>(bindSheetContent: ComponentContent<T>): Promise<void>--><!--Device-UIContext-closeBindSheet<T extends Object>(bindSheetContent: ComponentContent<T>): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bindSheetContent | [ComponentContent](../arkts-components/arkts-arkui-componentcontent-t.md)&lt;T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [120001](../errorcode-bindSheet.md#120001-内容节点对应半模态页面错误) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [120003](../errorcode-bindSheet.md#120003-无法找到内容节点对应的半模态页面) |

## constructor

```TypeScript
constructor()
```

构造UIContext对象。

> **说明：**
> 
> 通过构造函数创建的UIContext对象指向不明确的UI上下文，即不指向任何UI实例。该UIContext对应实例的唯一标识ID为-1。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-constructor()--><!--Device-UIContext-constructor()-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## createAnimator

```TypeScript
createAnimator(options: AnimatorOptions): AnimatorResult
```

定义Animator类。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-createAnimator(options: AnimatorOptions): AnimatorResult--><!--Device-UIContext-createAnimator(options: AnimatorOptions): AnimatorResult-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [AnimatorOptions](arkts-arkui-animator-animatoroptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [AnimatorResult](arkts-arkui-animator-animatorresult-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## createAnimator

```TypeScript
createAnimator(options: AnimatorOptions | SimpleAnimatorOptions): AnimatorResult
```

创建animator动画结果对象（AnimatorResult）。与[createAnimator](arkts-arkui-arkui-uicontext-uicontext-c.md#createanimator)相比，新增对  
[SimpleAnimatorOptions](arkts-arkui-animator-simpleanimatoroptions-c.md)类型入参的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-createAnimator(options: AnimatorOptions | SimpleAnimatorOptions): AnimatorResult--><!--Device-UIContext-createAnimator(options: AnimatorOptions | SimpleAnimatorOptions): AnimatorResult-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [AnimatorOptions](arkts-arkui-animator-animatoroptions-i.md) \| [SimpleAnimatorOptions](arkts-arkui-animator-simpleanimatoroptions-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [AnimatorResult](arkts-arkui-animator-animatorresult-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## createUIContextWithoutWindow

```TypeScript
static createUIContextWithoutWindow(context: common.UIAbilityContext | common.ExtensionContext) : UIContext | undefined
```

创建一个不依赖窗口的UI实例，并返回其UI上下文。该接口所创建的UI实例是单例。

> **说明：**
> 
> 返回的UI上下文只可用于创建[自定义节点](../../../ui/arkts-user-defined-node.md)，不能执行其他UI操作。

**起始版本：** 17

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本17开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-static createUIContextWithoutWindow(context: common.UIAbilityContext | common.ExtensionContext) : UIContext | undefined--><!--Device-UIContext-static createUIContextWithoutWindow(context: common.UIAbilityContext | common.ExtensionContext) : UIContext | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | common.UIAbilityContext \| common.ExtensionContext | 是 |

**返回值：**

| 类型 |
| --- |
| [UIContext](../arkts-components/arkts-arkui-uicontext-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## destroyUIContextWithoutWindow

```TypeScript
static destroyUIContextWithoutWindow(): void
```

销毁[createUIContextWithoutWindow](arkts-arkui-arkui-uicontext-uicontext-c.md#createuicontextwithoutwindow)创建的UI实例。

**起始版本：** 17

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本17开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-static destroyUIContextWithoutWindow(): void--><!--Device-UIContext-static destroyUIContextWithoutWindow(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## dispatchKeyEvent

```TypeScript
dispatchKeyEvent(node: number | string, event: KeyEvent): boolean
```

Dispach keyboard event to the frameNode with inspector key.

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-dispatchKeyEvent(node: number | string, event: KeyEvent): boolean--><!--Device-UIContext-dispatchKeyEvent(node: number | string, event: KeyEvent): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| node | number \| string | 是 |
| event | [KeyEvent](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keyevent-keyevent-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## enableEventPassthrough

```TypeScript
enableEventPassthrough(enabled: boolean, eventType: RawInputEventType): void
```

是否启用或禁用事件直通。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-enableEventPassthrough(enabled: boolean, eventType: RawInputEventType): void--><!--Device-UIContext-enableEventPassthrough(enabled: boolean, eventType: RawInputEventType): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |
| eventType | [RawInputEventType](arkts-arkui-rawinputeventtype-e.md) | 是 |

## enableSwipeBack

```TypeScript
enableSwipeBack(enabled: Optional<boolean>): void
```

whether to enable or disable swipe to back event.

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-enableSwipeBack(enabled: Optional<boolean>): void--><!--Device-UIContext-enableSwipeBack(enabled: Optional<boolean>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;boolean&gt; | 是 |

## fp2px

```TypeScript
fp2px(value: number): number
```

将fp单位的数值转换为以px为单位的数值。

转换公式为：px值 = fp值 × 像素密度 × 字体缩放比例

像素密度：当前窗口生效的像素密度值，即虚拟屏幕的密度[VirtualScreenConfig](arkts-arkui-display-virtualscreenconfig-i.md).density。

字体缩放比例：系统设置的字体缩放系数，对应 [Configuration.fontScale](../../../reference/apis-arkui/arkui-ts/ts-types.md#configuration)。

> **说明：**
> 
> getUIContext需在windowStage.
> [loadContent](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#loadcontent9)之后调用，确保UIContext初始化完成后
> 调用此接口，否则无法返回准确结果。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-fp2px(value: number): number--><!--Device-UIContext-fp2px(value: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## getAllUIContexts

```TypeScript
static getAllUIContexts(): UIContext[]
```

获取所有当前有效的UIContext实例。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-static getAllUIContexts(): UIContext[]--><!--Device-UIContext-static getAllUIContexts(): UIContext[]-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [UIContext](../arkts-components/arkts-arkui-uicontext-t.md)[] |

## getAtomicServiceBar

```TypeScript
getAtomicServiceBar(): Nullable<AtomicServiceBar>
```

Get AtomicServiceBar.

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getAtomicServiceBar(): Nullable<AtomicServiceBar>--><!--Device-UIContext-getAtomicServiceBar(): Nullable<AtomicServiceBar>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Nullable](arkts-arkui-nullable-t.md)&lt;AtomicServiceBar&gt; |

## getAttachedFrameNodeById

```TypeScript
getAttachedFrameNodeById(id: string): FrameNode | null
```

通过组件的id获取当前窗口上的实体节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getAttachedFrameNodeById(id: string): FrameNode | null--><!--Device-UIContext-getAttachedFrameNodeById(id: string): FrameNode | null-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |

**返回值：**

| 类型 |
| --- |
| [FrameNode](arkts-arkui-framenode-t.md) |

## getCallingScopeUIContext

```TypeScript
static getCallingScopeUIContext(): UIContext | undefined
```

获取当前[调用作用域](../../../ui/arkts-global-interface.md#基本概念)的UIContext，调用作用域不明确时返回undefined。

> **说明：**
> 
> 返回的UIContext对象可能指向一个已销毁的UI实例，通常在由已销毁的实例抛出异步任务时出现。建议通过[isAvailable](arkts-arkui-arkui-uicontext-uicontext-c.md#isavailable)接口判断其有效性。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-static getCallingScopeUIContext(): UIContext | undefined--><!--Device-UIContext-static getCallingScopeUIContext(): UIContext | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [UIContext](../arkts-components/arkts-arkui-uicontext-t.md) |

## getComponentSnapshot

```TypeScript
getComponentSnapshot(): ComponentSnapshot
```

获取组件快照。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getComponentSnapshot(): ComponentSnapshot--><!--Device-UIContext-getComponentSnapshot(): ComponentSnapshot-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [ComponentSnapshot](arkts-arkui-arkui-uicontext-componentsnapshot-c.md) |

## getComponentUtils

```TypeScript
getComponentUtils(): ComponentUtils
```

get object ComponentUtils.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getComponentUtils(): ComponentUtils--><!--Device-UIContext-getComponentUtils(): ComponentUtils-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [ComponentUtils](arkts-arkui-arkui-uicontext-componentutils-c.md) |

## getContextMenuController

```TypeScript
getContextMenuController(): ContextMenuController
```

Get object context menu controller.

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getContextMenuController(): ContextMenuController--><!--Device-UIContext-getContextMenuController(): ContextMenuController-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [ContextMenuController](arkts-arkui-arkui-uicontext-contextmenucontroller-c.md) |

## getCursorController

```TypeScript
getCursorController(): CursorController
```

Get object cursor controller.

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getCursorController(): CursorController--><!--Device-UIContext-getCursorController(): CursorController-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [CursorController](arkts-arkui-arkui-uicontext-cursorcontroller-c.md) |

## getDialogPresenter

```TypeScript
getDialogPresenter(): DialogPresenter
```

获取Dialog对象。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getDialogPresenter(): DialogPresenter--><!--Device-UIContext-getDialogPresenter(): DialogPresenter-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [DialogPresenter](arkts-arkui-arkui-uicontext-dialogpresenter-c.md) |

## getDragController

```TypeScript
getDragController(): DragController
```

Get DragController.

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getDragController(): DragController--><!--Device-UIContext-getDragController(): DragController-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [DragController](arkts-arkui-arkui-uicontext-dragcontroller-c.md) |

## getFilteredInspectorTree

```TypeScript
getFilteredInspectorTree(filters?: Array<string>): string
```

get the filtered attributes of the component tree.

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getFilteredInspectorTree(filters?: Array<string>): string--><!--Device-UIContext-getFilteredInspectorTree(filters?: Array<string>): string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filters | Array&lt;string&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## getFilteredInspectorTreeById

```TypeScript
getFilteredInspectorTreeById(id: string, depth: number, filters?: Array<string>): string
```

get the filtered attributes of the component tree with the specified id and depth

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getFilteredInspectorTreeById(id: string, depth: number, filters?: Array<string>): string--><!--Device-UIContext-getFilteredInspectorTreeById(id: string, depth: number, filters?: Array<string>): string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |
| depth | number | 是 |
| filters | Array&lt;string&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## getFocusController

```TypeScript
getFocusController(): FocusController
```

获取焦点控制器。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getFocusController(): FocusController--><!--Device-UIContext-getFocusController(): FocusController-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [FocusController](arkts-arkui-arkui-uicontext-focuscontroller-c.md) |

## getFont

```TypeScript
getFont(): Font
```

获取Font对象。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getFont(): Font--><!--Device-UIContext-getFont(): Font-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Font](arkts-arkui-arkui-uicontext-font-c.md) |

## getFrameNodeById

```TypeScript
getFrameNodeById(id: string): FrameNode | null
```

通过组件的id获取组件树的实体节点。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getFrameNodeById(id: string): FrameNode | null--><!--Device-UIContext-getFrameNodeById(id: string): FrameNode | null-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |

**返回值：**

| 类型 |
| --- |
| [FrameNode](arkts-arkui-framenode-t.md) |

## getFrameNodeByUniqueId

```TypeScript
getFrameNodeByUniqueId(id: number): FrameNode | null
```

通过组件的uniqueId获取组件树的实体节点。

1. 当uniqueId对应的是系统组件时，返回组件所对应的FrameNode；2. 当uniqueId对应的是自定义组件时：  
 - 若其有渲染内容，且没有被[@Reusable装饰器](../../../ui/state-management/arkts-reusable.md)修饰时，返回该自定义组件的根节点，类型为__Common__。  
 - 若其无渲染内容，或者被[@Reusable装饰器](../../../ui/state-management/arkts-reusable.md)修饰时，在该自定义组件的子组件创建完成前调用此接口，将返回null；在该自定义组件的子组件创建完成后调用，返回其第一个子组件的FrameNode。  
3. 当uniqueId无对应的组件时，返回null。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getFrameNodeByUniqueId(id: number): FrameNode | null--><!--Device-UIContext-getFrameNodeByUniqueId(id: number): FrameNode | null-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |

**返回值：**

| 类型 |
| --- |
| [FrameNode](arkts-arkui-framenode-t.md) |

## getHostContext

```TypeScript
getHostContext(): Context | undefined
```

获得当前元能力的Context。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getHostContext(): Context | undefined--><!--Device-UIContext-getHostContext(): Context | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Context](../arkts-components/arkts-arkui-context-t.md) |

## getId

```TypeScript
getId(): number
```

获取UI实例对象唯一标识，多实例场景下，开发者可使用此唯一标识区分多个UI实例对象，便于管理。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getId(): number--><!--Device-UIContext-getId(): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getKeyboardAvoidMode

```TypeScript
getKeyboardAvoidMode(): KeyboardAvoidMode
```

返回虚拟键盘抬起时页面的避让模式。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getKeyboardAvoidMode(): KeyboardAvoidMode--><!--Device-UIContext-getKeyboardAvoidMode(): KeyboardAvoidMode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [KeyboardAvoidMode](arkts-arkui-arkui-uicontext-keyboardavoidmode-e.md) |

## getLastFocusedUIContext

```TypeScript
static getLastFocusedUIContext(): UIContext | undefined
```

获取最近一次切换到获焦状态的UI实例的UIContext。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-static getLastFocusedUIContext(): UIContext | undefined--><!--Device-UIContext-static getLastFocusedUIContext(): UIContext | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [UIContext](../arkts-components/arkts-arkui-uicontext-t.md) |

## getLastForegroundUIContext

```TypeScript
static getLastForegroundUIContext(): UIContext | undefined
```

获取最近一次切换到前台状态的UI实例的UIContext。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-static getLastForegroundUIContext(): UIContext | undefined--><!--Device-UIContext-static getLastForegroundUIContext(): UIContext | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [UIContext](../arkts-components/arkts-arkui-uicontext-t.md) |

## getMagnifier

```TypeScript
getMagnifier(): Magnifier
```

获取[Magnifier](arkts-arkui-arkui-uicontext-magnifier-c.md)对象，可控制放大镜显示和隐藏。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getMagnifier(): Magnifier--><!--Device-UIContext-getMagnifier(): Magnifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Magnifier](arkts-arkui-arkui-uicontext-magnifier-c.md) |

## getMaxFontScale

```TypeScript
getMaxFontScale(): number
```

Get the max font scale.

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getMaxFontScale(): number--><!--Device-UIContext-getMaxFontScale(): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getMeasureUtils

```TypeScript
getMeasureUtils(): MeasureUtils
```

允许用户通过UIContext对象，获取MeasureUtils对象进行文本计算。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getMeasureUtils(): MeasureUtils--><!--Device-UIContext-getMeasureUtils(): MeasureUtils-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [MeasureUtils](arkts-arkui-arkui-uicontext-measureutils-c.md) |

## getMediaQuery

```TypeScript
getMediaQuery(): MediaQuery
```

get object mediaQuery.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getMediaQuery(): MediaQuery--><!--Device-UIContext-getMediaQuery(): MediaQuery-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [MediaQuery](arkts-arkui-arkui-uicontext-mediaquery-c.md) |

## getNavigationInfoByUniqueId

```TypeScript
getNavigationInfoByUniqueId(id: number): observer.NavigationInfo | undefined
```

Get navigation information of the frameNode with uniqueId.

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getNavigationInfoByUniqueId(id: number): observer.NavigationInfo | undefined--><!--Device-UIContext-getNavigationInfoByUniqueId(id: number): observer.NavigationInfo | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |

**返回值：**

| 类型 |
| --- |
| observer.NavigationInfo |

## getOverlayManager

```TypeScript
getOverlayManager(): OverlayManager
```

Obtains the OverlayManager object.

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getOverlayManager(): OverlayManager--><!--Device-UIContext-getOverlayManager(): OverlayManager-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [OverlayManager](arkts-arkui-arkui-uicontext-overlaymanager-c.md) |

## getOverlayManagerOptions

```TypeScript
getOverlayManagerOptions(): OverlayManagerOptions
```

Get object OverlayManagerOptions.

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getOverlayManagerOptions(): OverlayManagerOptions--><!--Device-UIContext-getOverlayManagerOptions(): OverlayManagerOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [OverlayManagerOptions](arkts-arkui-arkui-uicontext-overlaymanageroptions-i.md) |

## getPageInfoByUniqueId

```TypeScript
getPageInfoByUniqueId(id: number): PageInfo
```

通过组件的uniqueId获取该节点对应的Router和NavDestination页面信息。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getPageInfoByUniqueId(id: number): PageInfo--><!--Device-UIContext-getPageInfoByUniqueId(id: number): PageInfo-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |

**返回值：**

| 类型 |
| --- |
| [PageInfo](arkts-arkui-arkui-uicontext-pageinfo-i.md) |

## getPageRootNode

```TypeScript
getPageRootNode(): FrameNode | null
```

获取UIContext对应页面的根节点。

**起始版本：** 24

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getPageRootNode(): FrameNode | null--><!--Device-UIContext-getPageRootNode(): FrameNode | null-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [FrameNode](arkts-arkui-framenode-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [120007](../errorcode-uicontext.md#120007-实例不存在) |

## getPixelRoundMode

```TypeScript
getPixelRoundMode(): PixelRoundMode
```

获取当前应用的像素取整模式。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getPixelRoundMode(): PixelRoundMode--><!--Device-UIContext-getPixelRoundMode(): PixelRoundMode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [PixelRoundMode](arkts-arkui-pixelroundmode-e.md) |

## getPromptAction

```TypeScript
getPromptAction(): PromptAction
```

get object PromptAction.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getPromptAction(): PromptAction--><!--Device-UIContext-getPromptAction(): PromptAction-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [PromptAction](arkts-arkui-arkui-uicontext-promptaction-c.md) |

## getRouter

```TypeScript
getRouter(): Router
```

Obtains a Router object.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getRouter(): Router--><!--Device-UIContext-getRouter(): Router-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Router](arkts-arkui-system-router-router-c.md) |

## getSharedLocalStorage

```TypeScript
getSharedLocalStorage(): LocalStorage | undefined
```

获取当前stage共享的LocalStorage实例。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getSharedLocalStorage(): LocalStorage | undefined--><!--Device-UIContext-getSharedLocalStorage(): LocalStorage | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [LocalStorage](arkts-arkui-localstorage-c.md) |

## getSmartGestureController

```TypeScript
getSmartGestureController(): SmartGestureController
```

获取对象智能手势控制器。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getSmartGestureController(): SmartGestureController--><!--Device-UIContext-getSmartGestureController(): SmartGestureController-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [SmartGestureController](arkts-arkui-arkui-uicontext-smartgesturecontroller-c.md) |

## getTextMenuController

```TypeScript
getTextMenuController(): TextMenuController
```

获取[TextMenuController](arkts-arkui-arkui-uicontext-textmenucontroller-c.md)对象，可通过该对象控制文本选择菜单。

**起始版本：** 16

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本16开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getTextMenuController(): TextMenuController--><!--Device-UIContext-getTextMenuController(): TextMenuController-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [TextMenuController](arkts-arkui-arkui-uicontext-textmenucontroller-c.md) |

## getUIInspector

```TypeScript
getUIInspector(): UIInspector
```

获取UIInspector对象。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getUIInspector(): UIInspector--><!--Device-UIContext-getUIInspector(): UIInspector-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [UIInspector](arkts-arkui-arkui-uicontext-uiinspector-c.md) |

## getUIObserver

```TypeScript
getUIObserver(): UIObserver
```

获取UIObserver对象。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getUIObserver(): UIObserver--><!--Device-UIContext-getUIObserver(): UIObserver-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [UIObserver](arkts-arkui-arkui-uicontext-uiobserver-c.md) |

## getWindowHeightBreakpoint

```TypeScript
getWindowHeightBreakpoint(): HeightBreakpoint
```

获取当前实例所在窗口的高度断点。具体枚举值根据窗口高宽比确定，详见 [HeightBreakpoint](arkts-arkui-heightbreakpoint-e.md)。

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getWindowHeightBreakpoint(): HeightBreakpoint--><!--Device-UIContext-getWindowHeightBreakpoint(): HeightBreakpoint-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [HeightBreakpoint](arkts-arkui-heightbreakpoint-e.md) |

## getWindowId

```TypeScript
getWindowId(): number | undefined
```

获取当前应用实例所属的窗口ID。

> **说明：**
> 
> 若UIContext位于主应用程序进程中的[UIExtensionAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiextensionability-uiextensionability-c.md/arkts-ability-app-ability-uiextensionability-uiextensionability-c.md)内，则返回主应用程
> 序的顶层窗口ID。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getWindowId(): number | undefined--><!--Device-UIContext-getWindowId(): number | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getWindowName

```TypeScript
getWindowName(): string | undefined
```

获取当前实例所在窗口的名称。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getWindowName(): string | undefined--><!--Device-UIContext-getWindowName(): string | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| string |

## getWindowWidthBreakpoint

```TypeScript
getWindowWidthBreakpoint(): WidthBreakpoint
```

获取当前实例所在窗口的宽度断点枚举值。具体枚举值根据窗口宽度vp值确定，详见 [WidthBreakpoint](arkts-arkui-widthbreakpoint-e.md)。

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-getWindowWidthBreakpoint(): WidthBreakpoint--><!--Device-UIContext-getWindowWidthBreakpoint(): WidthBreakpoint-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [WidthBreakpoint](arkts-arkui-widthbreakpoint-e.md) |

## isAvailable

```TypeScript
isAvailable(): boolean
```

判断UIContext对象对应的UI实例是否有效。使用  
[getUIContext](../../../reference/apis-arkui/arkts-apis-window-Window.md#getuicontext10)方法获取UIContext对象。后端UI实例存在时，该UI实例有效。通过new UIContext()创建的UIContext对象无对应的UI实例；多次  
[loadContent](../../../reference/apis-arkui/arkts-apis-window-Window.md#loadcontent9)后，旧的UI实例会失效。多窗口应用场景，当窗口关闭后，该窗口的UI实例失效。总而言之，当UIContext对象没有对应的后端UI实例时，该对象是无效的。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-isAvailable(): boolean--><!--Device-UIContext-isAvailable(): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

## isEasySplit

```TypeScript
isEasySplit(): boolean
```

检查当前UI实例是否处于分栏模式。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-isEasySplit(): boolean--><!--Device-UIContext-isEasySplit(): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

## isFollowingSystemFontScale

```TypeScript
isFollowingSystemFontScale(): boolean
```

Checks whether current font scale follows the system.

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-isFollowingSystemFontScale(): boolean--><!--Device-UIContext-isFollowingSystemFontScale(): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

## keyframeAnimateTo

```TypeScript
keyframeAnimateTo(param: KeyframeAnimateParam, keyframes: Array<KeyframeState>): void
```

产生关键帧动画。该接口的使用说明请参考[keyframeAnimateTo](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-keyframeAnimateTo(param: KeyframeAnimateParam, keyframes: Array<KeyframeState>): void--><!--Device-UIContext-keyframeAnimateTo(param: KeyframeAnimateParam, keyframes: Array<KeyframeState>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| param | [KeyframeAnimateParam](../arkts-components/arkts-arkui-keyframeanimateparam-i.md) | 是 |
| keyframes | Array&lt;KeyframeState&gt; | 是 |

## lpx2px

```TypeScript
lpx2px(value: number): number
```

将lpx单位的数值转换为以px为单位的数值。

转换公式为：px值 = lpx值 × 实际屏幕宽度与逻辑宽度（通过[designWidth](../../../quick-start/module-configuration-file.md#pages标签)配置）的比值。

> **说明：**
> 
> getUIContext需在windowStage.
> [loadContent](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#loadcontent9)之后调用，确保UIContext初始化完成后
> 调用此接口，否则无法返回准确结果。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-lpx2px(value: number): number--><!--Device-UIContext-lpx2px(value: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## openBindSheet

```TypeScript
openBindSheet<T extends Object>(bindSheetContent: ComponentContent<T>, sheetOptions?: SheetOptions, targetId?: number): Promise<void>
```

创建并弹出以bindSheetContent作为内容的半模态页面，使用Promise异步回调。通过该接口弹出的半模态页面样式完全按照bindSheetContent中设置的样式显示。

> **说明：**
> 
> 1. 使用该接口时，若未传入有效的targetId，则不支持设置SheetOptions.preferType为POPUP模式、不支持设置SheetOptions.mode为EMBEDDED模式。
> 
> 2. 由于[updateBindSheet](arkts-arkui-arkui-uicontext-uicontext-c.md#updatebindsheet)和[closeBindSheet](arkts-arkui-arkui-uicontext-uicontext-c.md#closebindsheet)依赖
> bindSheetContent去更新或者关闭指定的半模态页面，开发者需自行维护传入的bindSheetContent。
> 
> 3. 不支持设置SheetOptions.UIContext。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-openBindSheet<T extends Object>(bindSheetContent: ComponentContent<T>, sheetOptions?: SheetOptions, targetId?: number): Promise<void>--><!--Device-UIContext-openBindSheet<T extends Object>(bindSheetContent: ComponentContent<T>, sheetOptions?: SheetOptions, targetId?: number): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bindSheetContent | [ComponentContent](../arkts-components/arkts-arkui-componentcontent-t.md)&lt;T&gt; | 是 |
| sheetOptions | [SheetOptions](../arkts-components/arkts-arkui-sheetoptions-i.md) | 否 |
| targetId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [120001](../errorcode-bindSheet.md#120001-内容节点对应半模态页面错误) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [120002](../errorcode-bindSheet.md#120002-内容节点对应半模态页面已存在) |
| [120005](../errorcode-bindSheet.md#120005-指定的targetid对应的节点未挂载在组件树上) |
| [120004](../errorcode-bindSheet.md#120004-指定的targetid不存在) |
| [120006](../errorcode-bindSheet.md#120006-指定的targetid对应的节点并不是page节点或navdestination节点的子节点) |

## postDelayedFrameCallback

```TypeScript
postDelayedFrameCallback(frameCallback: FrameCallback, delayTime: number): void
```

注册一个回调，在延迟一段时间后的下一帧进行渲染时执行。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-postDelayedFrameCallback(frameCallback: FrameCallback, delayTime: number): void--><!--Device-UIContext-postDelayedFrameCallback(frameCallback: FrameCallback, delayTime: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| frameCallback | [FrameCallback](arkts-arkui-arkui-uicontext-framecallback-c.md) | 是 |
| delayTime | number | 是 |

## postFrameCallback

```TypeScript
postFrameCallback(frameCallback: FrameCallback): void
```

注册一个回调，仅在下一帧渲染时调用。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-postFrameCallback(frameCallback: FrameCallback): void--><!--Device-UIContext-postFrameCallback(frameCallback: FrameCallback): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| frameCallback | [FrameCallback](arkts-arkui-arkui-uicontext-framecallback-c.md) | 是 |

## px2fp

```TypeScript
px2fp(value: number): number
```

将px单位的数值转换为以fp为单位的数值。

转换公式为：fp值 = px值 ÷ 像素密度 ÷ 字体缩放比例

像素密度：当前窗口生效的像素密度值，即虚拟屏幕的密度[VirtualScreenConfig](arkts-arkui-display-virtualscreenconfig-i.md).density。

字体缩放比例：系统设置的字体缩放系数，对应 [Configuration.fontScale](../../../reference/apis-arkui/arkui-ts/ts-types.md#configuration)。

> **说明：**
> 
> getUIContext需在windowStage.
> [loadContent](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#loadcontent9)之后调用，确保UIContext初始化完成后
> 调用此接口，否则无法返回准确结果。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-px2fp(value: number): number--><!--Device-UIContext-px2fp(value: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## px2lpx

```TypeScript
px2lpx(value: number): number
```

将px单位的数值转换为以lpx为单位的数值。

转换公式为：lpx值 = px值 ÷ 实际屏幕宽度与逻辑宽度（通过[designWidth](../../../quick-start/module-configuration-file.md#pages标签)配置）的比值。

> **说明：**
> 
> getUIContext需在windowStage.
> [loadContent](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#loadcontent9)之后调用，确保UIContext初始化完成后
> 调用此接口，否则无法返回准确结果。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-px2lpx(value: number): number--><!--Device-UIContext-px2lpx(value: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## px2vp

```TypeScript
px2vp(value: number): number
```

将px单位的数值转换为以vp为单位的数值。

转换公式为：vp值 = px值 ÷ 像素密度

像素密度：当前窗口生效的像素密度值，即虚拟屏幕的密度[VirtualScreenConfig](arkts-arkui-display-virtualscreenconfig-i.md).density。

> **说明：**
> 
> 1. getUIContext需在windowStage.
> [loadContent](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#loadcontent9)之后调用，确保UIContext初始化完成后
> 调用此接口，否则无法返回准确结果。
> 
> 2. UI实例未创建时，[像素单位](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)中的px2vp接口使用默认屏幕的虚拟像素比进行转换。在该场景下，开发者使用UIContext接口替换时，可参考
> [像素单位转换接口替换为UIContext接口](../../../ui/arkts-global-interface.md#像素单位转换接口替换为uicontext接口)。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-px2vp(value: number): number--><!--Device-UIContext-px2vp(value: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## removeLocalInputEventMonitor

```TypeScript
removeLocalInputEventMonitor(monitor: InputEventMonitor): void
```

删除本地输入事件监视器。

**重要说明**：  
-只能移除addLocalInputEventMonitor返回的Monitor对象。  
-无法通过手动构造对象来注销监视器。  
-如果传递了一个无效的对象，系统会默默地忽略它。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-removeLocalInputEventMonitor(monitor: InputEventMonitor): void--><!--Device-UIContext-removeLocalInputEventMonitor(monitor: InputEventMonitor): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [InputEventMonitor](../arkts-components/arkts-arkui-inputeventmonitor-i.md) | 是 |

## requireDynamicSyncScene

```TypeScript
requireDynamicSyncScene(id: string): Array<DynamicSyncScene>
```

请求组件的动态帧率场景，用于自定义场景相关帧率配置。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-requireDynamicSyncScene(id: string): Array<DynamicSyncScene>--><!--Device-UIContext-requireDynamicSyncScene(id: string): Array<DynamicSyncScene>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;DynamicSyncScene&gt; |

## resolveUIContext

```TypeScript
static resolveUIContext(): ResolvedUIContext
```

使用优先级策略获取带有解析策略的UIContext实例对象。

> **说明：**
> 
> 按照预定义的优先级顺序解析并返回UIContext实例和UIContext的解析策略。
> 
> 解析规则按顺序如下：
> 
> 1. 当前调用作用域中的UIContext。
> 
> 2. 如果只存在一个UI实例，则返回其UIContext。
> 
> 3. 如果存在UI实例切换到获焦状态，且最近一次切换到获焦状态的UI实例未销毁，则返回最近一次获焦UI实例的UIContext。
> 
> 4. 如果存在UI实例切换到前台状态，且最近一次切换到前台状态的UI实例未销毁，则返回最近一次切换到前台状态的UI实例的UIContext。
> 
> 5. 如果存在多个UI实例，则返回实例唯一标识的ID最大的UIContext。
> 
> 6. 如果以上条件均不满足，则返回一个无效的UIContext实例。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-static resolveUIContext(): ResolvedUIContext--><!--Device-UIContext-static resolveUIContext(): ResolvedUIContext-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [ResolvedUIContext](arkts-arkui-arkui-uicontext-resolveduicontext-c.md) |

## runScopedTask

```TypeScript
runScopedTask(callback: () => void): void
```

在当前UIContext对应的UI实例作用域内执行传入的回调函数。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-runScopedTask(callback: () => void): void--><!--Device-UIContext-runScopedTask(callback: () => void): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | () =&gt; void | 是 |

## setCustomKeyboardContinueFeature

```TypeScript
setCustomKeyboardContinueFeature(feature: CustomKeyboardContinueFeature): void
```

设置自定义键盘接续特性。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-setCustomKeyboardContinueFeature(feature: CustomKeyboardContinueFeature): void--><!--Device-UIContext-setCustomKeyboardContinueFeature(feature: CustomKeyboardContinueFeature): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| feature | [CustomKeyboardContinueFeature](arkts-arkui-arkui-uicontext-customkeyboardcontinuefeature-e.md) | 是 |

## setImageCacheCount

```TypeScript
setImageCacheCount(value: number): void
```

设置内存中缓存解码后图片的数量上限，提升再次加载同源图片的加载速度。如果不设置则默认为0，不进行缓存。缓存采用内置的LRU策略，新图片加载后，如果超过缓存上限，会删除最久未再次加载的缓存。建议根据应用内存需求，设置合理缓存数量，数字过大可能导致内存使用过高。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-setImageCacheCount(value: number): void--><!--Device-UIContext-setImageCacheCount(value: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## setImageRawDataCacheSize

```TypeScript
setImageRawDataCacheSize(value: number): void
```

设置内存中缓存解码前图片数据的大小上限，单位为字节，提升再次加载同源图片的加载速度。如果不设置则默认为0，不进行缓存。缓存采用内置的LRU策略，新图片加载后，如果解码前数据超过缓存上限，会删除最久未再次加载的图片数据缓存。建议根据应用内存需求，设置合理缓存上限，过大可能导致应用内存使用过高。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-setImageRawDataCacheSize(value: number): void--><!--Device-UIContext-setImageRawDataCacheSize(value: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## setKeyboardAvoidMode

```TypeScript
setKeyboardAvoidMode(value: KeyboardAvoidMode): void
```

控制虚拟键盘抬起时页面的避让模式。

> **说明：**
> 
> 
KeyboardAvoidMode.RESIZE模式会压缩页面大小，页面中设置百分比宽高的组件会跟随页面压缩，而直接设置宽高的组件会按设置的固定大小布局。设置KeyboardAvoidMode的RESIZE模式时，expandSa feArea([SafeAreaType.KEYBOARD],[SafeAreaEdge.BOTTOM])不生效。  
> 
> KeyboardAvoidMode.NONE模式配置页面不避让键盘，页面会被抬起的键盘遮盖。
> 
> 
setKeyboardAvoidMode针对页面生效，对于弹窗类组件不生效，比如Dialog、Popup、Menu、BindSheet、BindContentCover、Toast、OverlayManager。弹窗类组件的避让模式可以参考CustomDialogControllerOptions对象说明。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-setKeyboardAvoidMode(value: KeyboardAvoidMode): void--><!--Device-UIContext-setKeyboardAvoidMode(value: KeyboardAvoidMode): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [KeyboardAvoidMode](arkts-arkui-arkui-uicontext-keyboardavoidmode-e.md) | 是 |

## setOverlayManagerOptions

```TypeScript
setOverlayManagerOptions(options: OverlayManagerOptions): boolean
```

Init OverlayManager.

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-setOverlayManagerOptions(options: OverlayManagerOptions): boolean--><!--Device-UIContext-setOverlayManagerOptions(options: OverlayManagerOptions): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [OverlayManagerOptions](arkts-arkui-arkui-uicontext-overlaymanageroptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## setPixelRoundMode

```TypeScript
setPixelRoundMode(mode: PixelRoundMode): void
```

设置当前页面的像素取整模式。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-setPixelRoundMode(mode: PixelRoundMode): void--><!--Device-UIContext-setPixelRoundMode(mode: PixelRoundMode): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [PixelRoundMode](arkts-arkui-pixelroundmode-e.md) | 是 |

## setResourceManagerCacheMaxCountForHSP

```TypeScript
static setResourceManagerCacheMaxCountForHSP(count: number): void
```

设置HSP资源管理对象的缓存数量上限。

如果缓存的上限设置得过高，可能会导致内存开销过大，存在内存过载的风险。建议根据实际需求进行配置。

**起始版本：** 21

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-static setResourceManagerCacheMaxCountForHSP(count: number): void--><!--Device-UIContext-static setResourceManagerCacheMaxCountForHSP(count: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| count | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100101](../errorcode-uicontext.md#100101-小于0的非法值) |
| [100103](../errorcode-uicontext.md#100103-调用线程错误) |
| [100102](../errorcode-uicontext.md#100102-参数类型错误) |

## setTextSelectionClearPolicy

```TypeScript
setTextSelectionClearPolicy(policy: TextSelectionClearPolicy): void
```

设置文本组件的文本选择清除策略。默认策略：**TextSelectionClearPolicy.KEEP_ON_EXTERNAL_CLICK**。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-setTextSelectionClearPolicy(policy: TextSelectionClearPolicy): void--><!--Device-UIContext-setTextSelectionClearPolicy(policy: TextSelectionClearPolicy): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| policy | [TextSelectionClearPolicy](arkts-arkui-arkui-uicontext-textselectionclearpolicy-e.md) | 是 |

## showActionSheet

```TypeScript
showActionSheet(value: ActionSheetOptions): void
```

Shows an action sheet in the given settings.

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-showActionSheet(value: ActionSheetOptions): void--><!--Device-UIContext-showActionSheet(value: ActionSheetOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ActionSheetOptions](arkts-arkui-actionsheetoptions-i.md) | 是 |

## showAlertDialog

```TypeScript
showAlertDialog(options: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions): void
```

alertDialog display.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-showAlertDialog(options: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions): void--><!--Device-UIContext-showAlertDialog(options: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [AlertDialogParamWithConfirm](arkts-arkui-alertdialogparamwithconfirm-i.md) \| AlertDialogParamWithButtons \| [AlertDialogParamWithOptions](arkts-arkui-alertdialog-alertdialogparamwithoptions-i.md) | 是 |

## showDatePickerDialog

```TypeScript
showDatePickerDialog(options: DatePickerDialogOptions): void
```

datePickerDialog display.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-showDatePickerDialog(options: DatePickerDialogOptions): void--><!--Device-UIContext-showDatePickerDialog(options: DatePickerDialogOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DatePickerDialogOptions](../arkts-components/arkts-arkui-datepickerdialogoptions-i.md) | 是 |

## showTextPickerDialog

```TypeScript
showTextPickerDialog(options: TextPickerDialogOptions): void
```

textPickerDialog display.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-showTextPickerDialog(options: TextPickerDialogOptions): void--><!--Device-UIContext-showTextPickerDialog(options: TextPickerDialogOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TextPickerDialogOptions](../arkts-components/arkts-arkui-textpickerdialogoptions-i.md) | 是 |

## showTextPickerDialog

```TypeScript
showTextPickerDialog(style: TextPickerDialogOptions | TextPickerDialogOptionsExt): void
```

textPickerDialog display.

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-showTextPickerDialog(style: TextPickerDialogOptions | TextPickerDialogOptionsExt): void--><!--Device-UIContext-showTextPickerDialog(style: TextPickerDialogOptions | TextPickerDialogOptionsExt): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [TextPickerDialogOptions](../arkts-components/arkts-arkui-textpickerdialogoptions-i.md) \| [TextPickerDialogOptionsExt](../arkts-components/arkts-arkui-textpickerdialogoptionsext-i.md) | 是 |

## showTimePickerDialog

```TypeScript
showTimePickerDialog(options: TimePickerDialogOptions): void
```

timePickerDialog display.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-showTimePickerDialog(options: TimePickerDialogOptions): void--><!--Device-UIContext-showTimePickerDialog(options: TimePickerDialogOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TimePickerDialogOptions](../arkts-components/arkts-arkui-timepickerdialogoptions-i.md) | 是 |

## unbindTabsFromNestedScrollable

```TypeScript
unbindTabsFromNestedScrollable(tabsController: TabsController, parentScroller: Scroller, childScroller: Scroller): void
```

Unbind tabs from nested scrollable container components.

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-unbindTabsFromNestedScrollable(tabsController: TabsController, parentScroller: Scroller, childScroller: Scroller): void--><!--Device-UIContext-unbindTabsFromNestedScrollable(tabsController: TabsController, parentScroller: Scroller, childScroller: Scroller): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tabsController | [TabsController](../arkts-components/arkts-arkui-tabscontroller-c.md) | 是 |
| parentScroller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | 是 |
| childScroller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | 是 |

## unbindTabsFromScrollable

```TypeScript
unbindTabsFromScrollable(tabsController: TabsController, scroller: Scroller): void
```

Unbind tabs from scrollable container component.

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-unbindTabsFromScrollable(tabsController: TabsController, scroller: Scroller): void--><!--Device-UIContext-unbindTabsFromScrollable(tabsController: TabsController, scroller: Scroller): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tabsController | [TabsController](../arkts-components/arkts-arkui-tabscontroller-c.md) | 是 |
| scroller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | 是 |

## updateBindSheet

```TypeScript
updateBindSheet<T extends Object>(bindSheetContent: ComponentContent<T>, sheetOptions: SheetOptions, partialUpdate?: boolean): Promise<void>
```

更新bindSheetContent对应的半模态页面的样式，使用Promise异步回调。

> **说明：**
> 
> 不支持更新SheetOptions.UIContext、SheetOptions.mode、回调函数。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-updateBindSheet<T extends Object>(bindSheetContent: ComponentContent<T>, sheetOptions: SheetOptions, partialUpdate?: boolean): Promise<void>--><!--Device-UIContext-updateBindSheet<T extends Object>(bindSheetContent: ComponentContent<T>, sheetOptions: SheetOptions, partialUpdate?: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bindSheetContent | [ComponentContent](../arkts-components/arkts-arkui-componentcontent-t.md)&lt;T&gt; | 是 |
| sheetOptions | [SheetOptions](../arkts-components/arkts-arkui-sheetoptions-i.md) | 是 |
| partialUpdate | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [120001](../errorcode-bindSheet.md#120001-内容节点对应半模态页面错误) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [120003](../errorcode-bindSheet.md#120003-无法找到内容节点对应的半模态页面) |

## vp2px

```TypeScript
vp2px(value: number): number
```

将vp单位的数值转换为以px为单位的数值。

转换公式为：px值 = vp值 × 像素密度

像素密度：当前窗口生效的像素密度值，即虚拟屏幕的密度[VirtualScreenConfig](arkts-arkui-display-virtualscreenconfig-i.md).density。

> **说明：**
> 
> 1. getUIContext需在windowStage.
> [loadContent](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#loadcontent9)之后调用，确保UIContext初始化完成后
> 调用此接口，否则无法返回准确结果。
> 
> 2. UI实例未创建时，[像素单位](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)中的vp2px接口使用默认屏幕的虚拟像素比进行转换。在该场景下，开发者使用UIContext接口替换时，可参考
> [像素单位转换接口替换为UIContext接口](../../../ui/arkts-global-interface.md#像素单位转换接口替换为uicontext接口)。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIContext-vp2px(value: number): number--><!--Device-UIContext-vp2px(value: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |
