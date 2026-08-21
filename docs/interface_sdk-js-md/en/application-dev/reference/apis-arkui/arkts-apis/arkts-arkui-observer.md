# @ohos.arkui.observer

Provides APIs for listening for UI component behavior changes.

> **NOTE：**
> 
> - UIObserver can only listen for relevant information within the current process and does not support obtaining
> information in cross-process scenarios<!--Del--
> such as UIExtensionComponent<!--
> DelEnd-->.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace uiObserver--><!--Device-unnamed-declare namespace uiObserver-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { uiObserver } from '@kit.ArkUI';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [off_densityUpdate](arkts-arkui-uiobserver-offdensityupdate-f.md#offdensityupdate) | Unregisters the listener for screen pixel density changes. |
| [off_didLayout](arkts-arkui-uiobserver-offdidlayout-f.md#offdidlayout) | Unregisters the listener for layout completion status in each frame. |
| [off_navDestinationSwitch](arkts-arkui-uiobserver-offnavdestinationswitch-f.md#offnavdestinationswitch) | Unsubscribes from **Navigation** component page switching events. |
| [off_navDestinationSwitch](arkts-arkui-uiobserver-offnavdestinationswitch-f.md#offnavdestinationswitch) | Unsubscribes from **Navigation** component page switching events. Compared with [uiObserver.off](arkts-arkui-uiobserver-offnavdestinationupdate-f.md#offnavdestinationupdate), this API supports the **observerOptions** parameter, which enables you to configure observation options. |
| [off_navDestinationUpdate](arkts-arkui-uiobserver-offnavdestinationupdate-f.md#offnavdestinationupdate) | Unsubscribes from status changes of the **NavDestination** component. Compared with [uiObserver.off](arkts-arkui-uiobserver-offnavdestinationupdate-f.md#offnavdestinationupdate), this API supports the **options** parameter, which enables you to specify the ID of the target **Navigation** component to observe. |
| [off_navDestinationUpdate](arkts-arkui-uiobserver-offnavdestinationupdate-f.md#offnavdestinationupdate) | Unsubscribes from status changes of the **NavDestination** component. |
| [off_routerPageUpdate](arkts-arkui-uiobserver-offrouterpageupdate-f.md#offrouterpageupdate) | Unsubscribes from state changes of the page during routing. |
| [off_scrollEvent](arkts-arkui-uiobserver-offscrollevent-f.md#offscrollevent) | Removes a callback function that was previously registered with `on()`. |
| [off_scrollEvent](arkts-arkui-uiobserver-offscrollevent-f.md#offscrollevent) | Removes a callback function that was previously registered with `on()`. |
| [off_tabContentUpdate](arkts-arkui-uiobserver-offtabcontentupdate-f.md#offtabcontentupdate) | Unsubscribes from **TabContent** page switching events for the specified **Tabs** component identified by its ID. |
| [off_tabContentUpdate](arkts-arkui-uiobserver-offtabcontentupdate-f.md#offtabcontentupdate) | Unsubscribes from the **TabContent** switching event. |
| [off_willDraw](arkts-arkui-uiobserver-offwilldraw-f.md#offwilldraw) | Unregisters the listener for drawing instruction dispatch in each frame. |
| [on_densityUpdate](arkts-arkui-uiobserver-ondensityupdate-f.md#ondensityupdate) | Listens for screen pixel density changes. |
| [on_didLayout](arkts-arkui-uiobserver-ondidlayout-f.md#ondidlayout) | Listens for layout completion status in each frame. |
| [on_navDestinationSwitch](arkts-arkui-uiobserver-onnavdestinationswitch-f.md#onnavdestinationswitch) | Subscribes to **Navigation** component page switching events. |
| [on_navDestinationSwitch](arkts-arkui-uiobserver-onnavdestinationswitch-f.md#onnavdestinationswitch) | Subscribes to **Navigation** component page switching events. Compared with [uiObserver.on](arkts-arkui-uiobserver-onnavdestinationupdate-f.md#onnavdestinationupdate), this API supports the **observerOptions** parameter, which enables you to configure observation options. |
| [on_navDestinationUpdate](arkts-arkui-uiobserver-onnavdestinationupdate-f.md#onnavdestinationupdate) | Subscribes to status changes of the **NavDestination** component. Compared with [uiObserver.on](arkts-arkui-uiobserver-onnavdestinationupdate-f.md#onnavdestinationupdate), this API supports the **options** parameter, which enables you to specify the ID of the target **Navigation** component to observe. |
| [on_navDestinationUpdate](arkts-arkui-uiobserver-onnavdestinationupdate-f.md#onnavdestinationupdate) | Subscribes to status changes of the **NavDestination** component. |
| [on_routerPageUpdate](arkts-arkui-uiobserver-onrouterpageupdate-f.md#onrouterpageupdate) | Subscribes to state changes of the page during routing. |
| [on_scrollEvent](arkts-arkui-uiobserver-onscrollevent-f.md#onscrollevent) | Registers a callback function to be called when the scroll event start or stop. |
| [on_scrollEvent](arkts-arkui-uiobserver-onscrollevent-f.md#onscrollevent) | Registers a callback function to be called when the scroll event start or stop. |
| [on_tabContentUpdate](arkts-arkui-uiobserver-ontabcontentupdate-f.md#ontabcontentupdate) | Subscribes to **TabContent** page switching events for the specified **Tabs** component identified by its ID. Unlike [on('tabChange')](arkts-arkui-arkuiuicontext-uiobserver-c.md#onnavdestinationupdate), this API does not support listening for the initial tab display event when the **Tabs** component is initialized. |
| [on_tabContentUpdate](arkts-arkui-uiobserver-ontabcontentupdate-f.md#ontabcontentupdate) | Subscribes to **TabContent** switch events. Unlike [on('tabChange')](arkts-arkui-arkuiuicontext-uiobserver-c.md#onnavdestinationupdate), this API does not support listening for the initial tab display event when the **Tabs** component is initialized. |
| [on_willDraw](arkts-arkui-uiobserver-onwilldraw-f.md#onwilldraw) | Listens for drawing instruction dispatch in each frame. |

### Classes

| Name | Description |
| --- | --- |
| [DensityInfo](arkts-arkui-uiobserver-densityinfo-c.md) | Provides the information contained in the callback when the screen pixel density changes. |
| [RouterPageInfo](arkts-arkui-uiobserver-routerpageinfo-c.md) | Provides the information contained in **RouterPageInfo**, returned by the system to developers. |
| [WindowSizeLayoutBreakpointInfo](arkts-arkui-uiobserver-windowsizelayoutbreakpointinfo-c.md) | Provides information about window size layout breakpoint changes. |

### Interfaces

| Name | Description |
| --- | --- |
| [NavDestinationInfo](arkts-arkui-uiobserver-navdestinationinfo-i.md) | Information about the **NavDestination** component, returned by the system to developers. |
| [NavDestinationSwitchInfo](arkts-arkui-uiobserver-navdestinationswitchinfo-i.md) | Provides the information about page switching of the **Navigation** component. |
| [NavDestinationSwitchObserverOptions](arkts-arkui-uiobserver-navdestinationswitchobserveroptions-i.md) | Provides the observer options for the page switching event of the **Navigation** component. |
| [NavigationInfo](arkts-arkui-uiobserver-navigationinfo-i.md) | Provides information about the **Navigation** component. |
| [ObserverOptions](arkts-arkui-uiobserver-observeroptions-i.md) | Describes the observer options. |
| [ScrollEventInfo](arkts-arkui-uiobserver-scrolleventinfo-i.md) | ScrollEvent info. |
| [TabContentInfo](arkts-arkui-uiobserver-tabcontentinfo-i.md) | Provides the **TabContent** switching information. |
| [TextChangeEventInfo](arkts-arkui-uiobserver-textchangeeventinfo-i.md) | Text change event info |

### Enums

| Name | Description |
| --- | --- |
| [NavDestinationState](arkts-arkui-uiobserver-navdestinationstate-e.md) | Describes the state of the **NavDestination** component. |
| [RouterPageState](arkts-arkui-uiobserver-routerpagestate-e.md) | Enumerates the states of a page during routing. **RouterPageState** is used in [RouterPageInfo](../../apis-default/arkts-apis/arkts-uiobserver-routerpageinfo-c.md) as the callback parameter for passive observation via [routerPageUpdate](arkts-arkui-uiobserver-onnavdestinationupdate-f.md#onnavdestinationupdate). |
| [ScrollEventType](arkts-arkui-uiobserver-scrolleventtype-e.md) | ScrollEvent type. |
| [TabContentState](arkts-arkui-uiobserver-tabcontentstate-e.md) | TabContent state. |

