# @ohos.arkui.UIContext

## Modules to Import

```TypeScript
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [BackPressActionProposal](arkts-arkui-uicontext-backpressactionproposal-c.md) | Class BackPressActionProposal. |
| [BaseGestureHandlingProposal](arkts-arkui-uicontext-basegesturehandlingproposal-c.md) | Class BaseGestureHandlingProposal. |
| [ClickActionProposal](arkts-arkui-uicontext-clickactionproposal-c.md) | Class ClickActionProposal. |
| [ComponentSnapshot](arkts-arkui-uicontext-componentsnapshot-c.md) | class ComponentSnapshot |
| [ComponentUtils](arkts-arkui-uicontext-componentutils-c.md) | class ComponentUtils |
| [ContextMenuController](arkts-arkui-uicontext-contextmenucontroller-c.md) | class ContextMenuController |
| [CursorController](arkts-arkui-uicontext-cursorcontroller-c.md) | class CursorController |
| [DragController](arkts-arkui-uicontext-dragcontroller-c.md) | class DragController |
| [DynamicSyncScene](arkts-arkui-uicontext-dynamicsyncscene-c.md) | Represents a dynamic synchronization scene. |
| [FocusController](arkts-arkui-uicontext-focuscontroller-c.md) | class FocusController |
| [Font](arkts-arkui-uicontext-font-c.md) | class Font |
| [FrameCallback](arkts-arkui-uicontext-framecallback-c.md) | Class FrameCallback |
| [GestureHandlingResolution](arkts-arkui-uicontext-gesturehandlingresolution-c.md) | Class GestureHandlingResolution. Represents the developer's decision result for smart gesture handling. |
| [Magnifier](arkts-arkui-uicontext-magnifier-c.md) | Provides the method for magnifier capabilities. |
| [MarqueeDynamicSyncScene](arkts-arkui-uicontext-marqueedynamicsyncscene-c.md) | Represents a dynamic synchronization scene of Marquee. |
| [MeasureUtils](arkts-arkui-uicontext-measureutils-c.md) | class MeasureUtils |
| [MediaQuery](arkts-arkui-uicontext-mediaquery-c.md) | class MediaQuery |
| [NoneActionProposal](arkts-arkui-uicontext-noneactionproposal-c.md) | Class NoneActionProposal. |
| [OverlayManager](arkts-arkui-uicontext-overlaymanager-c.md) | class OverlayManager |
| [PageSwitchActionProposal](arkts-arkui-uicontext-pageswitchactionproposal-c.md) | Class PageSwitchActionProposal. The default page switch direction is forward. |
| [PromptAction](arkts-arkui-uicontext-promptaction-c.md) | class PromptAction |
| [ResolvedUIContext](arkts-arkui-uicontext-resolveduicontext-c.md) | Defines the result of UIContext.resolveUIContext. This class is a subclass of UIContext and additionally provides the strategy used to obtain this UIContext. @extends UIContext |
| [Router](arkts-arkui-uicontext-router-c.md) | class Router |
| [ScrollActionProposal](arkts-arkui-uicontext-scrollactionproposal-c.md) | Class ScrollActionProposal. The default scroll direction is forward. |
| [SelectActionProposal](arkts-arkui-uicontext-selectactionproposal-c.md) | Class SelectActionProposal. |
| [SmartGestureController](arkts-arkui-uicontext-smartgesturecontroller-c.md) | Class SmartGestureController. |
| [SwiperDynamicSyncScene](arkts-arkui-uicontext-swiperdynamicsyncscene-c.md) | Represents a dynamic synchronization scene of Swiper. |
| [TargetedGestureProposal](arkts-arkui-uicontext-targetedgestureproposal-c.md) | Class TargetedGestureProposal. |
| [TextMenuController](arkts-arkui-uicontext-textmenucontroller-c.md) | class TextMenuController |
| [UIContext](arkts-arkui-uicontext-uicontext-c.md) | class UIContext |
| [UIInspector](arkts-arkui-uicontext-uiinspector-c.md) | Provides APIs for registering the component layout and drawing display completion callbacks. |
| [UIObserver](arkts-arkui-uicontext-uiobserver-c.md) | Register callbacks to observe ArkUI behavior. |

<!--Del-->
### Classes(System API)

| Name | Description |
| --- | --- |
| [ComponentSnapshot](arkts-arkui-uicontext-componentsnapshot-c-sys.md) | class ComponentSnapshot |
| [DragController](arkts-arkui-uicontext-dragcontroller-c-sys.md) | class DragController |
| [UIContext](arkts-arkui-uicontext-uicontext-c-sys.md) | class UIContext |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [AtomicServiceBar](arkts-arkui-uicontext-atomicservicebar-i.md) | interface AtomicServiceBar @interface AtomicServiceBar |
| [GestureObserverConfigs](arkts-arkui-uicontext-gestureobserverconfigs-i.md) | The observer options for global gesture listener. |
| [GestureTriggerInfo](arkts-arkui-uicontext-gesturetriggerinfo-i.md) | The information when one gesture specific callback is triggered. |
| [OrderOverlayOptions](arkts-arkui-uicontext-orderoverlayoptions-i.md) | Options for opening an overlay with order. |
| [OverlayManagerOptions](arkts-arkui-uicontext-overlaymanageroptions-i.md) | the property of OverlayManager. |
| [PageInfo](arkts-arkui-uicontext-pageinfo-i.md) | Defines the PageInfo type. The value of routerPageInfo indicates the information of the router page, or undefined if the frameNode does not have router page information. And the value of navDestinationInfo indicates the information of the navDestination, or undefined if the frameNode does not have navDestination information. |
| [SwiperContentInfo](arkts-arkui-uicontext-swipercontentinfo-i.md) | The information returned when the Swiper content changes. |
| [SwiperItemInfo](arkts-arkui-uicontext-swiperiteminfo-i.md) | The information of changed SwiperItem. |
| [TargetInfo](arkts-arkui-uicontext-targetinfo-i.md) | Defines the target info. |

### Enums

| Name | Description |
| --- | --- |
| [CustomKeyboardContinueFeature](arkts-arkui-uicontext-customkeyboardcontinuefeature-e.md) | Enum of CustomKeyboardContinueFeature |
| [GestureActionPhase](arkts-arkui-uicontext-gestureactionphase-e.md) | This is an enumeration type representing the gesture callback phases to be triggered, corresponding to the action callbacks defined in gesture.d.ts. Therefore, not all gesture types have all the following phase definitions. For example, SwipeGesture only has one callback named onAction, so it also only has one enumeration type, which is WILL_START. |
| [GestureListenerType](arkts-arkui-uicontext-gesturelistenertype-e.md) | This is an enumeration type indicating what kind of gesture you want to monitor for. |
| [KeyboardAvoidMode](arkts-arkui-uicontext-keyboardavoidmode-e.md) | Enum of KeyBoardAvoidMethodType |
| [MarqueeDynamicSyncSceneType](arkts-arkui-uicontext-marqueedynamicsyncscenetype-e.md) | Enum of scene type for Marquee |
| [NodeRenderState](arkts-arkui-uicontext-noderenderstate-e.md) | An enumeration type that identifies the current node's rendering state. The UI components used in the application are automatically managed by the system and controlled for participation in graphical rendering by either mounting them onto the render tree or removing them from it. Only nodes that participate in graphical rendering have the potential to be displayed. However, participating in rendering does not equal to the node's visibility, as there may be many occlusion scenarios in the actual implementation of the application. Nevertheless, if a node does not participate in rendering, it will definitely not be visible. |
| [ResolveStrategy](arkts-arkui-uicontext-resolvestrategy-e.md) | Enum of strategy of resolved UIContext. @enum { number } strategy of resolved UIContext. |
| [SwiperDynamicSyncSceneType](arkts-arkui-uicontext-swiperdynamicsyncscenetype-e.md) | Enum of SwiperDynamicSyncSceneType |
| [TextSelectionClearPolicy](arkts-arkui-uicontext-textselectionclearpolicy-e.md) | Enum of TextSelectionClearPolicy |

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

