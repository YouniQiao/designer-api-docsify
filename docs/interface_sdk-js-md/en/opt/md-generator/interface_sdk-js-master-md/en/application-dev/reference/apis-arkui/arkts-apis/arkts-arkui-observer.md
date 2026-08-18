# @ohos.arkui.observer

Provides APIs for listening for UI component behavior changes. > **NOTE：**> > - UIObserver can only listen for relevant information within the current process and does not support obtaining > information in cross-process scenarios&lt;!--Del--&gt; such as UIExtensionComponent&lt;!-- &gt; DelEnd-->.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace uiObserver--><!--Device-unnamed-declare namespace uiObserver-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [off_densityUpdate](arkts-arkui-uiobserver-offdensityupdate-f.md#offdensityupdate) |
| [off_didLayout](arkts-arkui-uiobserver-offdidlayout-f.md#offdidlayout) |
| [off_navDestinationSwitch](arkts-arkui-uiobserver-offnavdestinationswitch-f.md#offnavdestinationswitch) |
| [off_navDestinationSwitch](arkts-arkui-uiobserver-offnavdestinationswitch-f.md#offnavdestinationswitch-1) |
| [off_navDestinationUpdate](arkts-arkui-uiobserver-offnavdestinationupdate-f.md#offnavdestinationupdate) |
| [off_navDestinationUpdate](arkts-arkui-uiobserver-offnavdestinationupdate-f.md#offnavdestinationupdate-1) |
| [off_routerPageUpdate](arkts-arkui-uiobserver-offrouterpageupdate-f.md#offrouterpageupdate) |
| [off_scrollEvent](arkts-arkui-uiobserver-offscrollevent-f.md#offscrollevent) |
| [off_scrollEvent](arkts-arkui-uiobserver-offscrollevent-f.md#offscrollevent-1) |
| [off_tabContentUpdate](arkts-arkui-uiobserver-offtabcontentupdate-f.md#offtabcontentupdate) |
| [off_tabContentUpdate](arkts-arkui-uiobserver-offtabcontentupdate-f.md#offtabcontentupdate-1) |
| [off_willDraw](arkts-arkui-uiobserver-offwilldraw-f.md#offwilldraw) |
| [on_densityUpdate](arkts-arkui-uiobserver-ondensityupdate-f.md#ondensityupdate) |
| [on_didLayout](arkts-arkui-uiobserver-ondidlayout-f.md#ondidlayout) |
| [on_navDestinationSwitch](arkts-arkui-uiobserver-onnavdestinationswitch-f.md#onnavdestinationswitch) |
| [on_navDestinationSwitch](arkts-arkui-uiobserver-onnavdestinationswitch-f.md#onnavdestinationswitch-1) |
| [on_navDestinationUpdate](arkts-arkui-uiobserver-onnavdestinationupdate-f.md#onnavdestinationupdate) |
| [on_navDestinationUpdate](arkts-arkui-uiobserver-onnavdestinationupdate-f.md#onnavdestinationupdate-1) |
| [on_routerPageUpdate](arkts-arkui-uiobserver-onrouterpageupdate-f.md#onrouterpageupdate) |
| [on_scrollEvent](arkts-arkui-uiobserver-onscrollevent-f.md#onscrollevent) |
| [on_scrollEvent](arkts-arkui-uiobserver-onscrollevent-f.md#onscrollevent-1) |
| [on_tabContentUpdate](arkts-arkui-uiobserver-ontabcontentupdate-f.md#ontabcontentupdate) |
| [on_tabContentUpdate](arkts-arkui-uiobserver-ontabcontentupdate-f.md#ontabcontentupdate-1) |
| [on_willDraw](arkts-arkui-uiobserver-onwilldraw-f.md#onwilldraw) |

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DensityInfo](arkts-arkui-uiobserver-densityinfo-c.md) |
| [RouterPageInfo](arkts-arkui-uiobserver-routerpageinfo-c.md) |
| [WindowSizeLayoutBreakpointInfo](arkts-arkui-uiobserver-windowsizelayoutbreakpointinfo-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NavDestinationInfo](arkts-arkui-uiobserver-navdestinationinfo-i.md) |
| [NavDestinationSwitchInfo](arkts-arkui-uiobserver-navdestinationswitchinfo-i.md) |
| [NavDestinationSwitchObserverOptions](arkts-arkui-uiobserver-navdestinationswitchobserveroptions-i.md) |
| [NavigationInfo](arkts-arkui-uiobserver-navigationinfo-i.md) |
| [ObserverOptions](arkts-arkui-uiobserver-observeroptions-i.md) |
| [ScrollEventInfo](arkts-arkui-uiobserver-scrolleventinfo-i.md) |
| [TabContentInfo](arkts-arkui-uiobserver-tabcontentinfo-i.md) |
| [TextChangeEventInfo](arkts-arkui-uiobserver-textchangeeventinfo-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NavDestinationState](arkts-arkui-uiobserver-navdestinationstate-e.md) |
| [RouterPageState](arkts-arkui-uiobserver-routerpagestate-e.md) |
| [ScrollEventType](arkts-arkui-uiobserver-scrolleventtype-e.md) |
| [TabContentState](arkts-arkui-uiobserver-tabcontentstate-e.md) |
