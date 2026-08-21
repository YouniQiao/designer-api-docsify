# @ohos.arkui.UIContext

## Modules to Import

```TypeScript
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [BackPressActionProposal](arkts-arkuiuicontext-backpressactionproposal-c.md) | Class BackPressActionProposal. |
| [BaseGestureHandlingProposal](arkts-arkuiuicontext-basegesturehandlingproposal-c.md) | Class BaseGestureHandlingProposal. |
| [ClickActionProposal](arkts-arkuiuicontext-clickactionproposal-c.md) | Class ClickActionProposal. |
| [ComponentSnapshot](arkts-arkuiuicontext-componentsnapshot-c.md) | class ComponentSnapshot |
| [ComponentUtils](arkts-arkuiuicontext-componentutils-c.md) | class ComponentUtils |
| [ContextMenuController](arkts-arkuiuicontext-contextmenucontroller-c.md) | class ContextMenuController |
| [CursorController](arkts-arkuiuicontext-cursorcontroller-c.md) | class CursorController |
| [DragController](arkts-arkuiuicontext-dragcontroller-c.md) | class DragController |
| [DynamicSyncScene](arkts-arkuiuicontext-dynamicsyncscene-c.md) | Represents a dynamic synchronization scene. |
| [FocusController](arkts-arkuiuicontext-focuscontroller-c.md) | class FocusController |
| [Font](arkts-arkuiuicontext-font-c.md) | class Font |
| [FrameCallback](arkts-arkuiuicontext-framecallback-c.md) | Class FrameCallback |
| [GestureHandlingResolution](arkts-arkuiuicontext-gesturehandlingresolution-c.md) | Class GestureHandlingResolution. Represents the developer's decision result for smart gesture handling. |
| [Magnifier](arkts-arkuiuicontext-magnifier-c.md) | Provides the method for magnifier capabilities. |
| [MarqueeDynamicSyncScene](arkts-arkuiuicontext-marqueedynamicsyncscene-c.md) | Represents a dynamic synchronization scene of Marquee. |
| [MeasureUtils](arkts-arkuiuicontext-measureutils-c.md) | class MeasureUtils |
| [MediaQuery](arkts-arkuiuicontext-mediaquery-c.md) | class MediaQuery |
| [NoneActionProposal](arkts-arkuiuicontext-noneactionproposal-c.md) | Class NoneActionProposal. |
| [OverlayManager](arkts-arkuiuicontext-overlaymanager-c.md) | class OverlayManager |
| [PageSwitchActionProposal](arkts-arkuiuicontext-pageswitchactionproposal-c.md) | Class PageSwitchActionProposal. The default page switch direction is forward. |
| [PromptAction](arkts-arkuiuicontext-promptaction-c.md) | class PromptAction |
| [ResolvedUIContext](arkts-arkuiuicontext-resolveduicontext-c.md) | Defines the result of UIContext.resolveUIContext. This class is a subclass of UIContext and additionally provides the strategy used to obtain this UIContext. @extends UIContext |
| [Router](arkts-arkuiuicontext-router-c.md) | class Router |
| [ScrollActionProposal](arkts-arkuiuicontext-scrollactionproposal-c.md) | Class ScrollActionProposal. The default scroll direction is forward. |
| [SelectActionProposal](arkts-arkuiuicontext-selectactionproposal-c.md) | Class SelectActionProposal. |
| [SmartGestureController](arkts-arkuiuicontext-smartgesturecontroller-c.md) | Class SmartGestureController. |
| [SwiperDynamicSyncScene](arkts-arkuiuicontext-swiperdynamicsyncscene-c.md) | Represents a dynamic synchronization scene of Swiper. |
| [TargetedGestureProposal](arkts-arkuiuicontext-targetedgestureproposal-c.md) | Class TargetedGestureProposal. |
| [TextMenuController](arkts-arkuiuicontext-textmenucontroller-c.md) | class TextMenuController |
| [UIContext](arkts-arkuiuicontext-uicontext-c.md) | class UIContext |
| [UIInspector](arkts-arkuiuicontext-uiinspector-c.md) | Provides APIs for registering the component layout and drawing display completion callbacks. |
| [UIObserver](arkts-arkuiuicontext-uiobserver-c.md) | Register callbacks to observe ArkUI behavior. |

<!--Del-->
### Classes(System API)

| Name | Description |
| --- | --- |
| [ComponentSnapshot](arkts-arkuiuicontext-componentsnapshot-c-sys.md) | class ComponentSnapshot |
| [DragController](arkts-arkuiuicontext-dragcontroller-c-sys.md) | class DragController |
| [UIContext](arkts-arkuiuicontext-uicontext-c-sys.md) | class UIContext |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [AtomicServiceBar](arkts-arkuiuicontext-atomicservicebar-i.md) | interface AtomicServiceBar @interface AtomicServiceBar |
| [GestureObserverConfigs](arkts-arkuiuicontext-gestureobserverconfigs-i.md) | The observer options for global gesture listener. |
| [GestureTriggerInfo](arkts-arkuiuicontext-gesturetriggerinfo-i.md) | The information when one gesture specific callback is triggered. |
| [OrderOverlayOptions](arkts-arkuiuicontext-orderoverlayoptions-i.md) | Options for opening an overlay with order. |
| [OverlayManagerOptions](arkts-arkuiuicontext-overlaymanageroptions-i.md) | the property of OverlayManager. |
| [PageInfo](arkts-arkuiuicontext-pageinfo-i.md) | Defines the PageInfo type. The value of routerPageInfo indicates the information of the router page, or undefined if the frameNode does not have router page information. And the value of navDestinationInfo indicates the information of the navDestination, or undefined if the frameNode does not have navDestination information. |
| [SwiperContentInfo](arkts-arkuiuicontext-swipercontentinfo-i.md) | The information returned when the Swiper content changes. |
| [SwiperItemInfo](arkts-arkuiuicontext-swiperiteminfo-i.md) | The information of changed SwiperItem. |
| [TargetInfo](arkts-arkuiuicontext-targetinfo-i.md) | Defines the target info. |

### Enums

| Name | Description |
| --- | --- |
| [CustomKeyboardContinueFeature](arkts-arkuiuicontext-customkeyboardcontinuefeature-e.md) | Enum of CustomKeyboardContinueFeature |
| [GestureActionPhase](arkts-arkuiuicontext-gestureactionphase-e.md) | This is an enumeration type representing the gesture callback phases to be triggered, corresponding to the action callbacks defined in gesture.d.ts. Therefore, not all gesture types have all the following phase definitions. For example, SwipeGesture only has one callback named onAction, so it also only has one enumeration type, which is WILL_START. |
| [GestureListenerType](arkts-arkuiuicontext-gesturelistenertype-e.md) | This is an enumeration type indicating what kind of gesture you want to monitor for. |
| [KeyboardAvoidMode](arkts-arkuiuicontext-keyboardavoidmode-e.md) | Enum of KeyBoardAvoidMethodType |
| [MarqueeDynamicSyncSceneType](arkts-arkuiuicontext-marqueedynamicsyncscenetype-e.md) | Enum of scene type for Marquee |
| [NodeRenderState](arkts-arkuiuicontext-noderenderstate-e.md) | An enumeration type that identifies the current node's rendering state. The UI components used in the application are automatically managed by the system and controlled for participation in graphical rendering by either mounting them onto the render tree or removing them from it. Only nodes that participate in graphical rendering have the potential to be displayed. However, participating in rendering does not equal to the node's visibility, as there may be many occlusion scenarios in the actual implementation of the application. Nevertheless, if a node does not participate in rendering, it will definitely not be visible. |
| [ResolveStrategy](arkts-arkuiuicontext-resolvestrategy-e.md) | Enum of strategy of resolved UIContext. @enum { number } strategy of resolved UIContext. |
| [SwiperDynamicSyncSceneType](arkts-arkuiuicontext-swiperdynamicsyncscenetype-e.md) | Enum of SwiperDynamicSyncSceneType |
| [TextSelectionClearPolicy](arkts-arkuiuicontext-textselectionclearpolicy-e.md) | Enum of TextSelectionClearPolicy |

### Types

| Name | Description |
| --- | --- |
| [ClickEventListenerCallback](arkts-clickeventlistenercallback-t.md) | Defines the callback type used in UIObserver watch click event. The value of event indicates the information of ClickEvent. The value of node indicates the frameNode which will receive the event. |
| [Context](arkts-context-t.md) | The base context of an ability or an application. It allows access to application-specific resources. |
| [CustomBuilderWithId](arkts-custombuilderwithid-t.md) | Defines the custom builder with id. |
| [GestureEventListenerCallback](arkts-gestureeventlistenercallback-t.md) | Defines the callback type used in UIObserver watch gesture. The value of event indicates the information of gesture. The value of node indicates the frameNode which will receive the event. |
| [GestureListenerCallback](arkts-gesturelistenercallback-t.md) | Defines the callback type used in UIObserver to monitor specific gesture triggered information. |
| [NodeIdentity](arkts-nodeidentity-t.md) | Defines the type can be used for identiting the node, for the string type, it's the inspector id set through .id attribute, and for the int type, it's the unique ID got from the FrameNode by getUniqueID method. |
| [NodeRenderStateChangeCallback](arkts-noderenderstatechangecallback-t.md) | Defines the callback type used in UIObserver to monitor one specific node's render state. |
| [OnOverlayBackPressCallback](arkts-onoverlaybackpresscallback-t.md) | Defines the callback type for intercepting a back-press event on an overlay. |
| [PanListenerCallback](arkts-panlistenercallback-t.md) | Defines the callback type used in UIObserver watch pan event. The value of event indicates the information of pan event. The value of node indicates the frameNode which will receive the event. |
| [PointerStyle](arkts-pointerstyle-t.md) | Pointer style. |

