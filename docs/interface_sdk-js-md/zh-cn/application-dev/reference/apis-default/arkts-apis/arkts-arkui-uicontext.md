# @ohos.arkui.UIContext

## 导入模块

```TypeScript
```

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [BackPressActionProposal](arkts-arkui-uicontext-backpressactionproposal-c.md) | 类BackPressActionProposal。 |
| [BaseGestureHandlingProposal](arkts-arkui-uicontext-basegesturehandlingproposal-c.md) | 类BaseGestureHandlingProposal。 |
| [ClickActionProposal](arkts-arkui-uicontext-clickactionproposal-c.md) | 类ClickActionProposal。 |
| [ComponentSnapshot](arkts-arkui-uicontext-componentsnapshot-c.md) | class ComponentSnapshot |
| [ComponentUtils](arkts-arkui-uicontext-componentutils-c.md) | class ComponentUtils |
| [ContextMenuController](arkts-arkui-uicontext-contextmenucontroller-c.md) | 提供控制菜单关闭的能力。 |
| [CursorController](arkts-arkui-uicontext-cursorcontroller-c.md) | class CursorController |
| [DialogPresenter](arkts-arkui-uicontext-dialogpresenter-c.md) | 提供统一的对话框接口。 |
| [DragController](arkts-arkui-uicontext-dragcontroller-c.md) | class DragController |
| [DynamicSyncScene](arkts-arkui-uicontext-dynamicsyncscene-c.md) | Represents a dynamic synchronization scene. |
| [FocusController](arkts-arkui-uicontext-focuscontroller-c.md) | class FocusController |
| [Font](arkts-arkui-uicontext-font-c.md) | class Font |
| [FrameCallback](arkts-arkui-uicontext-framecallback-c.md) | Class FrameCallback |
| [GestureHandlingResolution](arkts-arkui-uicontext-gesturehandlingresolution-c.md) | 类手势处理解决方案。表示开发者对智能手势处理的决策结果。 |
| [Magnifier](arkts-arkui-uicontext-magnifier-c.md) | 提供控制放大镜的能力。 |
| [MarqueeDynamicSyncScene](arkts-arkui-uicontext-marqueedynamicsyncscene-c.md) | Represents a dynamic synchronization scene of Marquee.@extends DynamicSyncScene |
| [MeasureUtils](arkts-arkui-uicontext-measureutils-c.md) | class MeasureUtils |
| [MediaQuery](arkts-arkui-uicontext-mediaquery-c.md) | class MediaQuery |
| [NoneActionProposal](arkts-arkui-uicontext-noneactionproposal-c.md) | 类NoneActionProposal。 |
| [OverlayManager](arkts-arkui-uicontext-overlaymanager-c.md) | 提供绘制浮层的能力。 |
| [PageSwitchActionProposal](arkts-arkui-uicontext-pageswitchactionproposal-c.md) | 类PageSwitchActionProposal。默认的页面切换方向为前进。 |
| [PromptAction](arkts-arkui-uicontext-promptaction-c.md) | 创建并显示即时反馈、对话框、操作菜单以及自定义弹窗。 |
| [ResolvedUIContext](arkts-arkui-uicontext-resolveduicontext-c.md) | UIContext.resolveUIContext接口的返回值类型，属于UIContext类型的子类，额外包含获取该UIContext的解析策略。@extends UIContext |
| [Router](arkts-arkui-uicontext-router-c.md) | 提供通过不同的url访问不同的页面，包括跳转到应用内的指定页面、同应用内的某个页面替换当前页面、返回上一页面或指定的页面等。 |
| [ScrollActionProposal](arkts-arkui-uicontext-scrollactionproposal-c.md) | 类ScrollActionProposal。默认滚动方向为向前。 |
| [SelectActionProposal](arkts-arkui-uicontext-selectactionproposal-c.md) | 类SelectActionProposal。 |
| [SmartGestureController](arkts-arkui-uicontext-smartgesturecontroller-c.md) | 类SmartGestureController。 |
| [SwiperDynamicSyncScene](arkts-arkui-uicontext-swiperdynamicsyncscene-c.md) | 提供Swiper组件动态帧率场景的相关配置，适用于为动画过渡和手势跟手等不同交互场景设置差异化帧率范围，以兼顾流畅度和功耗，继承自[DynamicSyncScene](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-dynamicsyncscene-c.md)。@extends DynamicSyncScene |
| [TargetedGestureProposal](arkts-arkui-uicontext-targetedgestureproposal-c.md) | 类TargetedGestureProposal。 |
| [TextMenuController](arkts-arkui-uicontext-textmenucontroller-c.md) | class TextMenuController |
| [UIContext](arkts-arkui-uicontext-uicontext-c.md) | UIContext类 |
| [UIInspector](arkts-arkui-uicontext-uiinspector-c.md) | 提供注册组件布局和组件绘制送显完成回调通知的能力。送显指节点的绘制命令发送到图形服务并完成显示。例如，开发者可在组件布局完成后获取组件精确尺寸，或在送显完成后执行截图、动画同步等操作，适用于需要精确感知组件布局和绘制时机的场景。 |
| [UIObserver](arkts-arkui-uicontext-uiobserver-c.md) | 注册回调来观察ArkUI的行为。 |

<!--Del-->
### 类（系统接口）

| 名称 | 说明 |
| --- | --- |
| [ComponentSnapshot](arkts-arkui-uicontext-componentsnapshot-c-sys.md) | class ComponentSnapshot |
| [DragController](arkts-arkui-uicontext-dragcontroller-c-sys.md) | class DragController |
| [UIContext](arkts-arkui-uicontext-uicontext-c-sys.md) | UIContext类 |
<!--DelEnd-->

### 接口

| 名称 | 说明 |
| --- | --- |
| [AtomicServiceBar](arkts-arkui-uicontext-atomicservicebar-i.md) | 原子化服务栏@interface AtomicServiceBar |
| [GestureObserverConfigs](arkts-arkui-uicontext-gestureobserverconfigs-i.md) | 该参数用于指定需要监听的手势回调阶段（传入空数组将无效），仅当手势触发指定阶段时才会发送通知。@interface GestureObserverConfigs |
| [GestureTriggerInfo](arkts-arkui-uicontext-gesturetriggerinfo-i.md) | 特定手势回调函数触发时的信息。@interface GestureTriggerInfo |
| [OrderOverlayOptions](arkts-arkui-uicontext-orderoverlayoptions-i.md) | 使用顺序打开浮层的选项。@interface OrderOverlayOptions |
| [OverlayManagerOptions](arkts-arkui-uicontext-overlaymanageroptions-i.md) | 初始化[OverlayManager](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md)时所用参数。@interface OverlayManagerOptions |
| [PageInfo](arkts-arkui-uicontext-pageinfo-i.md) | Router和NavDestination等页面信息，若无对应的Router或NavDestination页面信息，则对应属性为undefined。@interface PageInfo |
| [SwiperContentInfo](arkts-arkui-uicontext-swipercontentinfo-i.md) | Swiper组件的内容区信息。@interface SwiperContentInfo |
| [SwiperItemInfo](arkts-arkui-uicontext-swiperiteminfo-i.md) | Swiper子组件的信息。@interface SwiperContentInfo |
| [TargetInfo](arkts-arkui-uicontext-targetinfo-i.md) | 指定组件绑定的目标节点。@interface TargetInfo |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [CustomKeyboardContinueFeature](arkts-arkui-uicontext-customkeyboardcontinuefeature-e.md) | 自定义键盘接续特性的枚举。@enum { int } CustomKeyboardContinueFeature |
| [GestureActionPhase](arkts-arkui-uicontext-gestureactionphase-e.md) | 表示触发的手势回调阶段的枚举类型，对应 the action callbacks defined in gesture.d.ts. Therefore, not all gesture types have all the following phase definitions. For example, SwipeGesture only has one callback named onAction, so it also only has one enumeration type, which is WILL_START.@enum { number } GestureActionPhase |
| [GestureListenerType](arkts-arkui-uicontext-gesturelistenertype-e.md) | 表示需要监听的手势类型的枚举。@enum { number } GestureListenerType |
| [KeyboardAvoidMode](arkts-arkui-uicontext-keyboardavoidmode-e.md) | Enum of KeyBoardAvoidMethodType@enum { number } KeyBoardAvoidMethodType |
| [MarqueeDynamicSyncSceneType](arkts-arkui-uicontext-marqueedynamicsyncscenetype-e.md) | Enum of scene type for Marquee@enum { number } MarqueeDynamicSyncSceneType |
| [NodeRenderState](arkts-arkui-uicontext-noderenderstate-e.md) | An enumeration type that identifies the current node's rendering state. The UI components used in the application are automatically managed by the system and controlled for participation in graphical rendering by either mounting them onto the render tree or removing them from it. Only nodes that participate in graphical rendering have the potential to be displayed. However, participating in rendering does not equal to the node's visibility, as there may be many occlusion scenarios in the actual implementation of the application. Nevertheless, if a node does not participate in rendering, it will definitely not be visible.@enum { number } NodeRenderState |
| [ResolveStrategy](arkts-arkui-uicontext-resolvestrategy-e.md) | UIContext解析策略枚举@enum { number } strategy of resolved UIContext. |
| [SwiperDynamicSyncSceneType](arkts-arkui-uicontext-swiperdynamicsyncscenetype-e.md) | Enum of SwiperDynamicSyncSceneType@enum { number } SwiperDynamicSyncSceneType |
| [TextSelectionClearPolicy](arkts-arkui-uicontext-textselectionclearpolicy-e.md) | TextSelectionClearPolicy的枚举 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [ClickEventListenerCallback](arkts-clickeventlistenercallback-t.md) | 定义UIObserver监听点击事件时使用的回调类型。 event表示点击事件的信息。 node表示接收事件的frameNode。 |
| [Context](arkts-context-t.md) | ability或application的基础上下文。可用于访问 application-specific resources. |
| [CustomBuilderWithId](arkts-custombuilderwithid-t.md) | 定义带id的自定义构建器。 |
| [GestureEventListenerCallback](arkts-gestureeventlistenercallback-t.md) | 定义UIObserver监听手势时使用的回调类型。 event表示手势的信息。 node表示接收事件的frameNode。 |
| [GestureListenerCallback](arkts-gesturelistenercallback-t.md) | 定义UIObserver监听指定手势触发信息时使用的回调类型。 |
| [NodeIdentity](arkts-nodeidentity-t.md) | 定义可用于标识节点的类型，string类型时为inspector id，number类型时为系统分配的唯一id。 set through .id attribute, and for the int type, it's the unique ID got from the FrameNode by getUniqueID method. |
| [NodeRenderStateChangeCallback](arkts-noderenderstatechangecallback-t.md) | 定义UIObserver监听指定节点渲染状态时使用的回调类型。 |
| [OnOverlayBackPressCallback](arkts-onoverlaybackpresscallback-t.md) | 定义用于拦截overlay上返回按键事件的回调类型。 |
| [PanListenerCallback](arkts-panlistenercallback-t.md) | 定义UIObserver监听拖拽事件时使用的回调类型。 event表示拖拽事件的信息。 node表示接收事件的frameNode。 |
| [PointerStyle](arkts-pointerstyle-t.md) | Pointer style. |

