# @ohos.arkui.observer

Register callbacks to observe ArkUI behavior.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

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
| [offDensityUpdate](arkts-na-uiobserver-offdensityupdate-f.md) | Removes a callback function that was previously registered with `on()`. |
| [offDidLayout](arkts-na-uiobserver-offdidlayout-f.md) | Removes a callback function that was previously registered with `on()`. |
| [offNavDestinationSwitch](arkts-na-uiobserver-offnavdestinationswitch-f.md) | Removes a callback function that was previously registered with `onNavDestinationSwitch`. |
| [offNavDestinationSwitch](arkts-na-uiobserver-offnavdestinationswitch-f.md) | Removes a callback function that was previously registered with `onNavDestinationSwitch`. |
| [offNavDestinationUpdate](arkts-na-uiobserver-offnavdestinationupdate-f.md) | Removes a callback function that was previously registered with `onNavDestinationUpdate`. |
| [offNavDestinationUpdate](arkts-na-uiobserver-offnavdestinationupdate-f.md) | Removes a callback function that was previously registered with `onNavDestinationUpdate`. |
| [offRouterPageUpdate](arkts-na-uiobserver-offrouterpageupdate-f.md) | Removes a callback function that was previously registered with `onRouterPageUpdate`. |
| [offScrollEvent](arkts-na-uiobserver-offscrollevent-f.md) | Removes a callback function that was previously registered with `onScrollEvent()`. |
| [offScrollEvent](arkts-na-uiobserver-offscrollevent-f.md) | Removes a callback function that was previously registered with `onScrollEvent()`. |
| [offTabContentUpdate](arkts-na-uiobserver-offtabcontentupdate-f.md) | Removes a callback function that was previously registered with `on()`. |
| [offTabContentUpdate](arkts-na-uiobserver-offtabcontentupdate-f.md) | Removes a callback function that was previously registered with `on()`. |
| [offWillDraw](arkts-na-uiobserver-offwilldraw-f.md) | Removes a callback function that was previously registered with `on()`. |
| [onDensityUpdate](arkts-na-uiobserver-ondensityupdate-f.md) | Registers a callback function to be called when the screen density is updated. |
| [onDidLayout](arkts-na-uiobserver-ondidlayout-f.md) | Registers a callback function to be called when the layout is done. |
| [onNavDestinationSwitch](arkts-na-uiobserver-onnavdestinationswitch-f.md) | Registers a callback function to be called when the navigation switched to a new navDestination. |
| [onNavDestinationSwitch](arkts-na-uiobserver-onnavdestinationswitch-f.md) | Registers a callback function to be called when the navigation switched to a new navDestination. |
| [onNavDestinationUpdate](arkts-na-uiobserver-onnavdestinationupdate-f.md) | Registers a callback function to be called when the navigation destination is updated. |
| [onNavDestinationUpdate](arkts-na-uiobserver-onnavdestinationupdate-f.md) | Registers a callback function to be called when the navigation destination is updated. |
| [onRouterPageUpdate](arkts-na-uiobserver-onrouterpageupdate-f.md) | Registers a callback function to be called when the router page is updated. |
| [onScrollEvent](arkts-na-uiobserver-onscrollevent-f.md) | Registers a callback function to be called when the scroll event starts or stops. |
| [onScrollEvent](arkts-na-uiobserver-onscrollevent-f.md) | Registers a callback function to be called when the scroll event starts or stops. |
| [onTabContentUpdate](arkts-na-uiobserver-ontabcontentupdate-f.md) | Registers a callback function to be called when the tabContent is showed or hidden. |
| [onTabContentUpdate](arkts-na-uiobserver-ontabcontentupdate-f.md) | Registers a callback function to be called when the tabContent is showed or hidden. |
| [onWillDraw](arkts-na-uiobserver-onwilldraw-f.md) | Registers a callback function to be called when the draw command will be drawn. |

### Classes

| Name | Description |
| --- | --- |
| [DensityInfo](arkts-na-uiobserver-densityinfo-c.md) | Density info. |
| [RouterPageInfo](arkts-na-uiobserver-routerpageinfo-c.md) | Router page info. |

### Interfaces

| Name | Description |
| --- | --- |
| [NavDestinationInfo](arkts-na-uiobserver-navdestinationinfo-i.md) | NavDestination info. |
| [NavDestinationSwitchInfo](arkts-na-uiobserver-navdestinationswitchinfo-i.md) | NavDestination switch info |
| [NavDestinationSwitchObserverOptions](arkts-na-uiobserver-navdestinationswitchobserveroptions-i.md) | Indicates the options of NavDestination switch. |
| [NavigationInfo](arkts-na-uiobserver-navigationinfo-i.md) | Navigation info. |
| [ObserverOptions](arkts-na-uiobserver-observeroptions-i.md) | observer options. |
| [ScrollEventInfo](arkts-na-uiobserver-scrolleventinfo-i.md) | ScrollEvent info. |
| [TabContentInfo](arkts-na-uiobserver-tabcontentinfo-i.md) | TabContent info. |
| [TextChangeEventInfo](arkts-na-uiobserver-textchangeeventinfo-i.md) | Text change event info |
| [WindowSizeLayoutBreakpointInfo](arkts-na-uiobserver-windowsizelayoutbreakpointinfo-i.md) | Defines the window size layout breakpoint information. This interface provides the current breakpoint classification of the window's width and height based on the configured breakpoint thresholds. |

### Enums

| Name | Description |
| --- | --- |
| [NavDestinationState](arkts-na-uiobserver-navdestinationstate-e.md) | NavDestination state. |
| [RouterPageState](arkts-na-uiobserver-routerpagestate-e.md) | Router page state. |
| [ScrollEventType](arkts-na-uiobserver-scrolleventtype-e.md) | ScrollEvent type. |
| [TabContentState](arkts-na-uiobserver-tabcontentstate-e.md) | TabContent state. |

