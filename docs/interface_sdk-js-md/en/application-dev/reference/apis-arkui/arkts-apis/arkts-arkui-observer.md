# @ohos.arkui.observer

Provides APIs for listening for UI component behavior changes.

> **NOTE：**&gt;
> - UIObserver can only listen for relevant information within the current process and does not support obtaining
> information in cross-process scenarios<!--Del--
> such as UIExtensionComponent<!--
> DelEnd-->.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { uiObserver } from '@kit.ArkUI';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [off](arkts-arkui-uiobserver-off-f.md#offnavdestinationupdate) |
| [off](arkts-arkui-uiobserver-off-f.md#offnavdestinationupdate) |
| [off](arkts-arkui-uiobserver-off-f.md#offscrollevent) |
| [off](arkts-arkui-uiobserver-off-f.md#offscrollevent) |
| [off](arkts-arkui-uiobserver-off-f.md#offrouterpageupdate) |
| [off](arkts-arkui-uiobserver-off-f.md#offdensityupdate) |
| [off](arkts-arkui-uiobserver-off-f.md#offwilldraw) |
| [off](arkts-arkui-uiobserver-off-f.md#offdidlayout) |
| [off](arkts-arkui-uiobserver-off-f.md#offtabcontentupdate) |
| [off](arkts-arkui-uiobserver-off-f.md#offtabcontentupdate) |
| [off](arkts-arkui-uiobserver-off-f.md#offnavdestinationswitch) |
| [off](arkts-arkui-uiobserver-off-f.md#offnavdestinationswitch) |
| [offDensityUpdate](arkts-arkui-uiobserver-offdensityupdate-f.md) |
| [offDidLayout](arkts-arkui-uiobserver-offdidlayout-f.md) |
| [offNavDestinationSwitch](arkts-arkui-uiobserver-offnavdestinationswitch-f.md) |
| [offNavDestinationSwitch](arkts-arkui-uiobserver-offnavdestinationswitch-f.md) |
| [offNavDestinationUpdate](arkts-arkui-uiobserver-offnavdestinationupdate-f.md) |
| [offNavDestinationUpdate](arkts-arkui-uiobserver-offnavdestinationupdate-f.md) |
| [offRouterPageUpdate](arkts-arkui-uiobserver-offrouterpageupdate-f.md) |
| [offScrollEvent](arkts-arkui-uiobserver-offscrollevent-f.md) |
| [offScrollEvent](arkts-arkui-uiobserver-offscrollevent-f.md) |
| [offTabContentUpdate](arkts-arkui-uiobserver-offtabcontentupdate-f.md) |
| [offTabContentUpdate](arkts-arkui-uiobserver-offtabcontentupdate-f.md) |
| [offWillDraw](arkts-arkui-uiobserver-offwilldraw-f.md) |
| [on](arkts-arkui-uiobserver-on-f.md#onnavdestinationupdate) |
| [on](arkts-arkui-uiobserver-on-f.md#onnavdestinationupdate) |
| [on](arkts-arkui-uiobserver-on-f.md#onscrollevent) |
| [on](arkts-arkui-uiobserver-on-f.md#onscrollevent) |
| [on](arkts-arkui-uiobserver-on-f.md#onrouterpageupdate) |
| [on](arkts-arkui-uiobserver-on-f.md#ondensityupdate) |
| [on](arkts-arkui-uiobserver-on-f.md#onwilldraw) |
| [on](arkts-arkui-uiobserver-on-f.md#ondidlayout) |
| [on](arkts-arkui-uiobserver-on-f.md#ontabcontentupdate) |
| [on](arkts-arkui-uiobserver-on-f.md#ontabcontentupdate) |
| [on](arkts-arkui-uiobserver-on-f.md#onnavdestinationswitch) |
| [on](arkts-arkui-uiobserver-on-f.md#onnavdestinationswitch) |
| [onDensityUpdate](arkts-arkui-uiobserver-ondensityupdate-f.md) |
| [onDidLayout](arkts-arkui-uiobserver-ondidlayout-f.md) |
| [onNavDestinationSwitch](arkts-arkui-uiobserver-onnavdestinationswitch-f.md) |
| [onNavDestinationSwitch](arkts-arkui-uiobserver-onnavdestinationswitch-f.md) |
| [onNavDestinationUpdate](arkts-arkui-uiobserver-onnavdestinationupdate-f.md) |
| [onNavDestinationUpdate](arkts-arkui-uiobserver-onnavdestinationupdate-f.md) |
| [onRouterPageUpdate](arkts-arkui-uiobserver-onrouterpageupdate-f.md) |
| [onScrollEvent](arkts-arkui-uiobserver-onscrollevent-f.md) |
| [onScrollEvent](arkts-arkui-uiobserver-onscrollevent-f.md) |
| [onTabContentUpdate](arkts-arkui-uiobserver-ontabcontentupdate-f.md) |
| [onTabContentUpdate](arkts-arkui-uiobserver-ontabcontentupdate-f.md) |
| [onWillDraw](arkts-arkui-uiobserver-onwilldraw-f.md) |

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
| [WindowSizeLayoutBreakpointInfo](arkts-arkui-uiobserver-windowsizelayoutbreakpointinfo-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NavDestinationState](arkts-arkui-uiobserver-navdestinationstate-e.md) |
| [RouterPageState](arkts-arkui-uiobserver-routerpagestate-e.md) |
| [ScrollEventType](arkts-arkui-uiobserver-scrolleventtype-e.md) |
| [TabContentState](arkts-arkui-uiobserver-tabcontentstate-e.md) |
