# @ohos.arkui.observer

Register callbacks to observe ArkUI behavior.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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
| [offDensityUpdate](arkts-arkui-uiobserver-offdensityupdate-f.md#offdensityupdate) | Removes a callback function that was previously registered with `on()`. |
| [offDidLayout](arkts-arkui-uiobserver-offdidlayout-f.md#offdidlayout) | Removes a callback function that was previously registered with `on()`. |
| [offNavDestinationSwitch](arkts-arkui-uiobserver-offnavdestinationswitch-f.md#offnavdestinationswitch) | Removes a callback function that was previously registered with `onNavDestinationSwitch`. |
| [offNavDestinationSwitch](arkts-arkui-uiobserver-offnavdestinationswitch-f.md#offnavdestinationswitch-1) | Removes a callback function that was previously registered with `onNavDestinationSwitch`. |
| [offNavDestinationUpdate](arkts-arkui-uiobserver-offnavdestinationupdate-f.md#offnavdestinationupdate) | Removes a callback function that was previously registered with `onNavDestinationUpdate`. |
| [offNavDestinationUpdate](arkts-arkui-uiobserver-offnavdestinationupdate-f.md#offnavdestinationupdate-1) | Removes a callback function that was previously registered with `onNavDestinationUpdate`. |
| [offRouterPageUpdate](arkts-arkui-uiobserver-offrouterpageupdate-f.md#offrouterpageupdate) | Removes a callback function that was previously registered with `onRouterPageUpdate`. |
| [offScrollEvent](arkts-arkui-uiobserver-offscrollevent-f.md#offscrollevent) | Removes a callback function that was previously registered with `onScrollEvent()`. |
| [offScrollEvent](arkts-arkui-uiobserver-offscrollevent-f.md#offscrollevent-1) | Removes a callback function that was previously registered with `onScrollEvent()`. |
| [offTabContentUpdate](arkts-arkui-uiobserver-offtabcontentupdate-f.md#offtabcontentupdate) | Removes a callback function that was previously registered with `on()`. |
| [offTabContentUpdate](arkts-arkui-uiobserver-offtabcontentupdate-f.md#offtabcontentupdate-1) | Removes a callback function that was previously registered with `on()`. |
| [offWillDraw](arkts-arkui-uiobserver-offwilldraw-f.md#offwilldraw) | Removes a callback function that was previously registered with `on()`. |
| [onDensityUpdate](arkts-arkui-uiobserver-ondensityupdate-f.md#ondensityupdate) | Registers a callback function to be called when the screen density is updated. |
| [onDidLayout](arkts-arkui-uiobserver-ondidlayout-f.md#ondidlayout) | Registers a callback function to be called when the layout is done. |
| [onNavDestinationSwitch](arkts-arkui-uiobserver-onnavdestinationswitch-f.md#onnavdestinationswitch) | Registers a callback function to be called when the navigation switched to a new navDestination. |
| [onNavDestinationSwitch](arkts-arkui-uiobserver-onnavdestinationswitch-f.md#onnavdestinationswitch-1) | Registers a callback function to be called when the navigation switched to a new navDestination. |
| [onNavDestinationUpdate](arkts-arkui-uiobserver-onnavdestinationupdate-f.md#onnavdestinationupdate) | Registers a callback function to be called when the navigation destination is updated. |
| [onNavDestinationUpdate](arkts-arkui-uiobserver-onnavdestinationupdate-f.md#onnavdestinationupdate-1) | Registers a callback function to be called when the navigation destination is updated. |
| [onRouterPageUpdate](arkts-arkui-uiobserver-onrouterpageupdate-f.md#onrouterpageupdate) | Registers a callback function to be called when the router page is updated. |
| [onScrollEvent](arkts-arkui-uiobserver-onscrollevent-f.md#onscrollevent) | Registers a callback function to be called when the scroll event starts or stops. |
| [onScrollEvent](arkts-arkui-uiobserver-onscrollevent-f.md#onscrollevent-1) | Registers a callback function to be called when the scroll event starts or stops. |
| [onTabContentUpdate](arkts-arkui-uiobserver-ontabcontentupdate-f.md#ontabcontentupdate) | Registers a callback function to be called when the tabContent is showed or hidden. |
| [onTabContentUpdate](arkts-arkui-uiobserver-ontabcontentupdate-f.md#ontabcontentupdate-1) | Registers a callback function to be called when the tabContent is showed or hidden. |
| [onWillDraw](arkts-arkui-uiobserver-onwilldraw-f.md#onwilldraw) | Registers a callback function to be called when the draw command will be drawn. |

### Classes

| Name | Description |
| --- | --- |
| [DensityInfo](arkts-arkui-uiobserver-densityinfo-c.md) | Density info. |
| [RouterPageInfo](arkts-arkui-uiobserver-routerpageinfo-c.md) | Router page info. |

### Interfaces

| Name | Description |
| --- | --- |
| [NavDestinationInfo](arkts-arkui-uiobserver-navdestinationinfo-i.md) | NavDestination info. |
| [NavDestinationSwitchInfo](arkts-arkui-uiobserver-navdestinationswitchinfo-i.md) | NavDestination switch info |
| [NavDestinationSwitchObserverOptions](arkts-arkui-uiobserver-navdestinationswitchobserveroptions-i.md) | Indicates the options of NavDestination switch. |
| [NavigationInfo](arkts-arkui-uiobserver-navigationinfo-i.md) | Navigation info. |
| [ObserverOptions](arkts-arkui-uiobserver-observeroptions-i.md) | observer options. |
| [ScrollEventInfo](arkts-arkui-uiobserver-scrolleventinfo-i.md) | ScrollEvent info. |
| [TabContentInfo](arkts-arkui-uiobserver-tabcontentinfo-i.md) | TabContent info. |
| [TextChangeEventInfo](arkts-arkui-uiobserver-textchangeeventinfo-i.md) | Text change event info |
| [WindowSizeLayoutBreakpointInfo](arkts-arkui-uiobserver-windowsizelayoutbreakpointinfo-i.md) | Defines the window size layout breakpoint information.This interface provides the current breakpoint classification of the window's width and height based on the configured breakpoint thresholds. |

### Enums

| Name | Description |
| --- | --- |
| [NavDestinationState](arkts-arkui-uiobserver-navdestinationstate-e.md) | NavDestination state. |
| [RouterPageState](arkts-arkui-uiobserver-routerpagestate-e.md) | Router page state. |
| [ScrollEventType](arkts-arkui-uiobserver-scrolleventtype-e.md) | ScrollEvent type. |
| [TabContentState](arkts-arkui-uiobserver-tabcontentstate-e.md) | TabContent state. |

