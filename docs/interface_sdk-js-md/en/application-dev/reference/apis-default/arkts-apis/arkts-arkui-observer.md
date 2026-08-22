# @ohos.arkui.observer

Register callbacks to observe ArkUI behavior.

@namespace uiObserver

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace uiObserver--><!--Device-unnamed-declare namespace uiObserver-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [offDensityUpdate](arkts-uiobserver-offdensityupdate-f.md) | Removes a callback function that was previously registered with `on()`. |
| [offDidLayout](arkts-uiobserver-offdidlayout-f.md) | Removes a callback function that was previously registered with `on()`. |
| [offNavDestinationSwitch](arkts-uiobserver-offnavdestinationswitch-f.md) | Removes a callback function that was previously registered with `onNavDestinationSwitch`. |
| [offNavDestinationSwitch](arkts-uiobserver-offnavdestinationswitch-f.md) | Removes a callback function that was previously registered with `onNavDestinationSwitch`. |
| [offNavDestinationUpdate](arkts-uiobserver-offnavdestinationupdate-f.md) | Removes a callback function that was previously registered with `onNavDestinationUpdate`. |
| [offNavDestinationUpdate](arkts-uiobserver-offnavdestinationupdate-f.md) | Removes a callback function that was previously registered with `onNavDestinationUpdate`. |
| [offRouterPageUpdate](arkts-uiobserver-offrouterpageupdate-f.md) | Removes a callback function that was previously registered with `onRouterPageUpdate`. |
| [offScrollEvent](arkts-uiobserver-offscrollevent-f.md) | Removes a callback function that was previously registered with `onScrollEvent()`. |
| [offScrollEvent](arkts-uiobserver-offscrollevent-f.md) | Removes a callback function that was previously registered with `onScrollEvent()`. |
| [offTabContentUpdate](arkts-uiobserver-offtabcontentupdate-f.md) | Removes a callback function that was previously registered with `on()`. |
| [offTabContentUpdate](arkts-uiobserver-offtabcontentupdate-f.md) | Removes a callback function that was previously registered with `on()`. |
| [offWillDraw](arkts-uiobserver-offwilldraw-f.md) | Removes a callback function that was previously registered with `on()`. |
| [onDensityUpdate](arkts-uiobserver-ondensityupdate-f.md) | Registers a callback function to be called when the screen density is updated. |
| [onDidLayout](arkts-uiobserver-ondidlayout-f.md) | Registers a callback function to be called when the layout is done. |
| [onNavDestinationSwitch](arkts-uiobserver-onnavdestinationswitch-f.md) | Registers a callback function to be called when the navigation switched to a new navDestination. |
| [onNavDestinationSwitch](arkts-uiobserver-onnavdestinationswitch-f.md) | Registers a callback function to be called when the navigation switched to a new navDestination. |
| [onNavDestinationUpdate](arkts-uiobserver-onnavdestinationupdate-f.md) | Registers a callback function to be called when the navigation destination is updated. |
| [onNavDestinationUpdate](arkts-uiobserver-onnavdestinationupdate-f.md) | Registers a callback function to be called when the navigation destination is updated. |
| [onRouterPageUpdate](arkts-uiobserver-onrouterpageupdate-f.md) | Registers a callback function to be called when the router page is updated. |
| [onScrollEvent](arkts-uiobserver-onscrollevent-f.md) | Registers a callback function to be called when the scroll event starts or stops. |
| [onScrollEvent](arkts-uiobserver-onscrollevent-f.md) | Registers a callback function to be called when the scroll event starts or stops. |
| [onTabContentUpdate](arkts-uiobserver-ontabcontentupdate-f.md) | Registers a callback function to be called when the tabContent is showed or hidden. |
| [onTabContentUpdate](arkts-uiobserver-ontabcontentupdate-f.md) | Registers a callback function to be called when the tabContent is showed or hidden. |
| [onWillDraw](arkts-uiobserver-onwilldraw-f.md) | Registers a callback function to be called when the draw command will be drawn. |

### Classes

| Name | Description |
| --- | --- |
| [DensityInfo](arkts-uiobserver-densityinfo-c.md) | Density info. |
| [RouterPageInfo](arkts-uiobserver-routerpageinfo-c.md) | Router page info. |

### Interfaces

| Name | Description |
| --- | --- |
| [NavDestinationInfo](arkts-uiobserver-navdestinationinfo-i.md) | NavDestination info. |
| [NavDestinationSwitchInfo](arkts-uiobserver-navdestinationswitchinfo-i.md) | NavDestination switch info |
| [NavDestinationSwitchObserverOptions](arkts-uiobserver-navdestinationswitchobserveroptions-i.md) | Indicates the options of NavDestination switch. |
| [NavigationInfo](arkts-uiobserver-navigationinfo-i.md) | Navigation info. |
| [ObserverOptions](arkts-uiobserver-observeroptions-i.md) | observer options. |
| [ScrollEventInfo](arkts-uiobserver-scrolleventinfo-i.md) | ScrollEvent info. |
| [TabContentInfo](arkts-uiobserver-tabcontentinfo-i.md) | TabContent info. |
| [TextChangeEventInfo](arkts-uiobserver-textchangeeventinfo-i.md) | Text change event info |
| [WindowSizeLayoutBreakpointInfo](arkts-uiobserver-windowsizelayoutbreakpointinfo-i.md) | Defines the window size layout breakpoint information. This interface provides the current breakpoint classification of the window's width and height based on the configured breakpoint thresholds. |

### Enums

| Name | Description |
| --- | --- |
| [NavDestinationState](arkts-uiobserver-navdestinationstate-e.md) | NavDestination state. |
| [RouterPageState](arkts-uiobserver-routerpagestate-e.md) | Router page state. |
| [ScrollEventType](arkts-uiobserver-scrolleventtype-e.md) | ScrollEvent type. |
| [TabContentState](arkts-uiobserver-tabcontentstate-e.md) | TabContent state. |

