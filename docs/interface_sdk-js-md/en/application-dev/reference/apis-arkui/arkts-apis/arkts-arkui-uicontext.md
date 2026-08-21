# @ohos.arkui.UIContext

## Modules to Import

```TypeScript
import { AtomicServiceBar, ComponentUtils, ContextMenuController, CursorController, DialogPresenter, DragController, Font, KeyboardAvoidMode, MediaQuery, OverlayManager, PromptAction, Router, UIContext, UIInspector, UIObserver, PageInfo, SwiperDynamicSyncScene, SwiperDynamicSyncSceneType, MarqueeDynamicSyncScene, MarqueeDynamicSyncSceneType, MeasureUtils, FrameCallback, OverlayManagerOptions, TargetInfo, TextMenuController, NodeIdentity, NodeRenderState, NodeRenderStateChangeCallback, Magnifier, ResolvedUIContext, TextSelectionClearPolicy, CustomKeyboardContinueFeature, BackgroundLuminanceSamplingConfigs, LuminanceSampler } from '@kit.ArkUI';
import { GestureListenerType, GestureActionPhase, GestureTriggerInfo, GestureObserverConfigs, GestureListenerCallback } from '@kit.ArkUI';
import { SwiperContentInfo, SwiperItemInfo } from '@kit.ArkUI';
import { BackPressActionProposal, BaseGestureHandlingProposal, ClickActionProposal, GestureHandlingResolution, NoneActionProposal, PageSwitchActionProposal, ScrollActionProposal, SelectActionProposal, SmartGestureController, TargetedGestureProposal } from '@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [BackPressActionProposal](arkts-arkui-arkuiuicontext-backpressactionproposal-c.md) | Smart gesture back press action handling. When dynamically customizing smart gesture behavior through the [registerMonitor](arkts-arkui-arkuiuicontext-smartgesturecontroller-c.md#registermonitor) API, setting the return value [GestureHandlingResolution](arkts-arkui-arkuiuicontext-gesturehandlingresolution-c.md)'s **selectedProposal** to an object of this type navigates back to the previous page. |
| [BaseGestureHandlingProposal](arkts-arkui-arkuiuicontext-basegesturehandlingproposal-c.md) | Base class for smart gesture handling. When dynamically customizing smart gesture behavior through the [registerMonitor](arkts-arkui-arkuiuicontext-smartgesturecontroller-c.md#registermonitor) API, the callback parameter type is an instance of a specific subclass type. |
| [ClickActionProposal](arkts-arkui-arkuiuicontext-clickactionproposal-c.md) | Smart gesture click action handling. When dynamically customizing smart gesture behavior through the [registerMonitor](arkts-arkui-arkuiuicontext-smartgesturecontroller-c.md#registermonitor) API, setting the return value [GestureHandlingResolution](arkts-arkui-arkuiuicontext-gesturehandlingresolution-c.md)'s **selectedProposal** to an object of this type triggers a click operation on the target component. |
| [ComponentSnapshot](arkts-arkui-arkuiuicontext-componentsnapshot-c.md) | Provides APIs for obtaining component snapshots, including snapshots of components that have been loaded and snapshots of components that have not been loaded yet. |
| [ComponentUtils](arkts-arkui-arkuiuicontext-componentutils-c.md) | Provides API for obtaining the coordinates and size of the drawing area of a component. |
| [ContextMenuController](arkts-arkui-arkuiuicontext-contextmenucontroller-c.md) | Provides the capability to control the closing of context menus. |
| [CursorController](arkts-arkui-arkuiuicontext-cursorcontroller-c.md) | Provides the capability to set cursor styles. |
| [DialogPresenter](arkts-arkui-arkuiuicontext-dialogpresenter-c.md) | Provides unified dialog APIs. |
| [DragController](arkts-arkui-arkuiuicontext-dragcontroller-c.md) | Provides APIs for initiating drag actions. When receiving a gesture event, such as a touch or long-press event, an application can initiate a drag action and carry drag information therein. |
| [DynamicSyncScene](arkts-arkui-arkuiuicontext-dynamicsyncscene-c.md) | Represents a dynamic synchronization scene. |
| [FocusController](arkts-arkui-arkuiuicontext-focuscontroller-c.md) | Provides capabilities to control focus, including features such as clearing, moving, and activating focus. |
| [Font](arkts-arkui-arkuiuicontext-font-c.md) | Provides APIs for registering custom fonts. |
| [FrameCallback](arkts-arkui-arkuiuicontext-framecallback-c.md) | Implements the API for setting the task that needs to be executed during the next frame rendering. |
| [GestureHandlingResolution](arkts-arkui-arkuiuicontext-gesturehandlingresolution-c.md) | Class for declaring the result of smart gesture handling. |
| [Magnifier](arkts-arkui-arkuiuicontext-magnifier-c.md) | Provides the capability of displaying and hiding of the magnifier. The magnifier enlarges the component content for you to view the component details. |
| [MarqueeDynamicSyncScene](arkts-arkui-arkuiuicontext-marqueedynamicsyncscene-c.md) | Represents a dynamic synchronization scene of Marquee. |
| [MeasureUtils](arkts-arkui-arkuiuicontext-measureutils-c.md) | Provides APIs for measuring text metrics, such as text height and width. |
| [MediaQuery](arkts-arkui-arkuiuicontext-mediaquery-c.md) | class MediaQuery |
| [NoneActionProposal](arkts-arkui-arkuiuicontext-noneactionproposal-c.md) | Smart gesture no-op action handling. When dynamically customizing smart gesture behavior through the [registerMonitor](arkts-arkui-arkuiuicontext-smartgesturecontroller-c.md#registermonitor) API, setting the return value [GestureHandlingResolution](arkts-arkui-arkuiuicontext-gesturehandlingresolution-c.md)'s **selectedProposal** to an object of this type triggers no action. |
| [OverlayManager](arkts-arkui-arkuiuicontext-overlaymanager-c.md) | Provides the capability to draw overlays. |
| [PageSwitchActionProposal](arkts-arkui-arkuiuicontext-pageswitchactionproposal-c.md) | Smart gesture page switch action handling. The default direction is forward page switching, including right and down. When dynamically customizing smart gesture behavior through the [registerMonitor](arkts-arkui-arkuiuicontext-smartgesturecontroller-c.md#registermonitor) API, setting the return value [GestureHandlingResolution](arkts-arkui-arkuiuicontext-gesturehandlingresolution-c.md)'s **selectedProposal** to an object of this type triggers a page switching operation on the target component. |
| [PromptAction](arkts-arkui-arkuiuicontext-promptaction-c.md) | Provides APIs to create and display toasts, dialog boxes, action menus, and custom popups. |
| [ResolvedUIContext](arkts-arkui-arkuiuicontext-resolveduicontext-c.md) | *ResolvedUIContext** instance object. |
| [Router](arkts-arkui-arkuiuicontext-router-c.md) | Provides APIs to access pages through URLs. You can use the APIs to navigate to a specified page in an application, replace the current page with another one in the same application, and return to the previous page or a specified page. |
| [ScrollActionProposal](arkts-arkui-arkuiuicontext-scrollactionproposal-c.md) | Smart gesture scroll action handling. The default direction is forward scrolling, including right and down. When dynamically customizing smart gesture behavior through the [registerMonitor](arkts-arkui-arkuiuicontext-smartgesturecontroller-c.md#registermonitor) API, setting the return value [GestureHandlingResolution](arkts-arkui-arkuiuicontext-gesturehandlingresolution-c.md)'s **selectedProposal** to an object of this type triggers a scroll operation on the target component. |
| [SelectActionProposal](arkts-arkui-arkuiuicontext-selectactionproposal-c.md) | Smart gesture selection action handling. When dynamically customizing smart gesture behavior through the [registerMonitor](arkts-arkui-arkuiuicontext-smartgesturecontroller-c.md#registermonitor) API, setting the return value [GestureHandlingResolution](arkts-arkui-arkuiuicontext-gesturehandlingresolution-c.md)'s **selectedProposal** to an object of this type causes the target component to be selected. |
| [SmartGestureController](arkts-arkui-arkuiuicontext-smartgesturecontroller-c.md) | Provides the capability to enable smart gestures, monitor them, control the selection state, and dynamically determine smart gesture behavior. |
| [SwiperDynamicSyncScene](arkts-arkui-arkuiuicontext-swiperdynamicsyncscene-c.md) | Provides frame rate configuration APIs for the **Swiper** component. |
| [TargetedGestureProposal](arkts-arkui-arkuiuicontext-targetedgestureproposal-c.md) | Base class for smart gesture handling with a target node. |
| [TextMenuController](arkts-arkui-arkuiuicontext-textmenucontroller-c.md) | Provides the capability to control text menus. |
| [UIContext](arkts-arkui-arkuiuicontext-uicontext-c.md) | Implements a **UIContext** instance. |
| [UIInspector](arkts-arkui-arkuiuicontext-uiinspector-c.md) | Provides APIs for registering the component layout and drawing display completion callbacks. |
| [UIObserver](arkts-arkui-arkuiuicontext-uiobserver-c.md) | Provides APIs for listening for UI component behavior changes. |

<!--Del-->
### Classes(System API)

| Name | Description |
| --- | --- |
| [ComponentSnapshot](arkts-arkui-arkuiuicontext-componentsnapshot-c-sys.md) | Provides APIs for obtaining component snapshots, including snapshots of components that have been loaded and snapshots of components that have not been loaded yet. |
| [DragController](arkts-arkui-arkuiuicontext-dragcontroller-c-sys.md) | Provides APIs for initiating drag actions. When receiving a gesture event, such as a touch or long-press event, an application can initiate a drag action and carry drag information therein. |
| [LuminanceSampler](arkts-arkui-arkuiuicontext-luminancesampler-c-sys.md) | Sets the background luminance color picking parameters, registers the luminance change listening callback, and unregisters the listening callback. |
| [UIContext](arkts-arkui-arkuiuicontext-uicontext-c-sys.md) | Implements a **UIContext** instance. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [AtomicServiceBar](arkts-arkui-arkuiuicontext-atomicservicebar-i.md) | interface AtomicServiceBar |
| [GestureObserverConfigs](arkts-arkui-arkuiuicontext-gestureobserverconfigs-i.md) | Specifies the gesture callback phases to listen for (passing an empty array will be ineffective). Notifications are sent only when the gesture triggers the specified phases. |
| [GestureTriggerInfo](arkts-arkui-arkuiuicontext-gesturetriggerinfo-i.md) | Defines the information provided when a specific gesture callback is triggered. |
| [OrderOverlayOptions](arkts-arkui-arkuiuicontext-orderoverlayoptions-i.md) | Options for opening an overlay with order. |
| [OverlayManagerOptions](arkts-arkui-arkuiuicontext-overlaymanageroptions-i.md) | Provides the parameters used for initializing [OverlayManager](arkts-arkui-arkuiuicontext-uicontext-c.md). |
| [PageInfo](arkts-arkui-arkuiuicontext-pageinfo-i.md) | Represents the page information of the router or navigation destination. If there is no related page information, **undefined** is returned. |
| [SwiperContentInfo](arkts-arkui-arkuiuicontext-swipercontentinfo-i.md) | Provides content area information of the **Swiper** component. |
| [SwiperItemInfo](arkts-arkui-arkuiuicontext-swiperiteminfo-i.md) | Provides information about **Swiper** child components. |
| [TargetInfo](arkts-arkui-arkuiuicontext-targetinfo-i.md) | Specifies the target node for component binding. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [BackgroundLuminanceSamplingConfigs](arkts-arkui-arkuiuicontext-backgroundluminancesamplingconfigs-i-sys.md) | Sets the background luminance sampling parameters. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [CustomKeyboardContinueFeature](arkts-arkui-arkuiuicontext-customkeyboardcontinuefeature-e.md) | Enum of CustomKeyboardContinueFeature |
| [GestureActionPhase](arkts-arkui-arkuiuicontext-gestureactionphase-e.md) | Enumerates triggering phases of gesture callbacks, corresponding to the action callbacks defined in **gesture.d.ts**. However, different gesture types support different phases (for example, **SwipeGesture** only includes the **WILL_START** enumerated value). |
| [GestureListenerType](arkts-arkui-arkuiuicontext-gesturelistenertype-e.md) | Enumerates the types of gestures to be listened for. |
| [KeyboardAvoidMode](arkts-arkui-arkuiuicontext-keyboardavoidmode-e.md) | Enumerates the modes in which the layout responds when the keyboard is displayed. |
| [MarqueeDynamicSyncSceneType](arkts-arkui-arkuiuicontext-marqueedynamicsyncscenetype-e.md) | Enum of scene type for Marquee |
| [NodeRenderState](arkts-arkui-arkuiuicontext-noderenderstate-e.md) | An enumeration type that identifies the current node's rendering state. The UI components used in the application are automatically managed by the system and controlled for participation in graphical rendering by either mounting them onto the render tree or removing them from it. Only nodes that participate in graphical rendering have the potential to be displayed. However, participating in rendering does not equal to the node's visibility, as there may be many occlusion scenarios in the actual implementation of the application. Nevertheless, if a node does not participate in rendering, it will definitely not be visible. |
| [ResolveStrategy](arkts-arkui-arkuiuicontext-resolvestrategy-e.md) | Enumerates resolution strategies for **UIContext** objects. |
| [SwiperDynamicSyncSceneType](arkts-arkui-arkuiuicontext-swiperdynamicsyncscenetype-e.md) | Enum of SwiperDynamicSyncSceneType |
| [TextSelectionClearPolicy](arkts-arkui-arkuiuicontext-textselectionclearpolicy-e.md) | Enum of TextSelectionClearPolicy |

### Types

| Name | Description |
| --- | --- |
| [ClickEventListenerCallback](arkts-arkui-clickeventlistenercallback-t.md) | Defines the callback type for listening for click events in **UIObserver**. |
| [Context](arkts-arkui-context-t.md) | The base context of an ability or an application. It allows access to application-specific resources. |
| [CustomBuilderWithId](arkts-arkui-custombuilderwithid-t.md) | Defines a type that can be used for component attributes and method parameters to customize the UI description and generate custom components with a specific component ID. |
| [GestureEventListenerCallback](arkts-arkui-gestureeventlistenercallback-t.md) | Defines the callback type for gesture event listeners in **UIObserver**. |
| [GestureListenerCallback](arkts-arkui-gesturelistenercallback-t.md) | Defines the callback type for listening for specific gesture trigger information in **UIObserver**. |
| [NodeIdentity](arkts-arkui-nodeidentity-t.md) | Defines the type can be used for identiting the node, for the string type, it's the inspector id set through .id attribute, and for the number type, it's the unique ID got from the FrameNode by [getUniqueId](../../apis-default/arkts-apis/arkts-framenode-c.md#getuniqueid) method. |
| [NodeRenderStateChangeCallback](arkts-arkui-noderenderstatechangecallback-t.md) | Defines the callback type for listening for the rendering state of a specific node in **UIObserver**. |
| [OnOverlayBackPressCallback](arkts-arkui-onoverlaybackpresscallback-t.md) | Defines the callback type for intercepting a back-press event on an overlay. |
| [PanListenerCallback](arkts-arkui-panlistenercallback-t.md) | Defines a callback for pan gesture events. |
| [PointerStyle](arkts-arkui-pointerstyle-t.md) | Defines the pointer style. |

