# @ohos.arkui.observer

Provides APIs for listening for UI component behavior changes. > **NOTE：**> > - UIObserver can only listen for relevant information within the current process and does not support obtaining > information in cross-process scenarios&lt;!--Del--&gt; such as UIExtensionComponent&lt;!-- &gt; DelEnd-->.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace uiObserver--><!--Device-unnamed-declare namespace uiObserver-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { uiObserver } from '@kit.ArkUI';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [off_densityUpdate](arkts-arkui-uiobserver-offdensityupdate-f.md#off_densityUpdate) |
| [off_didLayout](arkts-arkui-uiobserver-offdidlayout-f.md#off_didLayout) |
| [off_navDestinationSwitch](arkts-arkui-uiobserver-offnavdestinationswitch-f.md#off_navDestinationSwitch) |
| [off_navDestinationSwitch](arkts-arkui-uiobserver-offnavdestinationswitch-f.md#off_navDestinationSwitch) |
| [off_navDestinationUpdate](arkts-arkui-uiobserver-offnavdestinationupdate-f.md#off_navDestinationUpdate) |
| [off_navDestinationUpdate](arkts-arkui-uiobserver-offnavdestinationupdate-f.md#off_navDestinationUpdate) |
| [off_routerPageUpdate](arkts-arkui-uiobserver-offrouterpageupdate-f.md#off_routerPageUpdate) |
| [off_scrollEvent](arkts-arkui-uiobserver-offscrollevent-f.md#off_scrollEvent) |
| [off_scrollEvent](arkts-arkui-uiobserver-offscrollevent-f.md#off_scrollEvent) |
| [off_tabContentUpdate](arkts-arkui-uiobserver-offtabcontentupdate-f.md#off_tabContentUpdate) |
| [off_tabContentUpdate](arkts-arkui-uiobserver-offtabcontentupdate-f.md#off_tabContentUpdate) |
| [off_willDraw](arkts-arkui-uiobserver-offwilldraw-f.md#off_willDraw) |
| [on_densityUpdate](arkts-arkui-uiobserver-ondensityupdate-f.md#on_densityUpdate) |
| [on_didLayout](arkts-arkui-uiobserver-ondidlayout-f.md#on_didLayout) |
| [on_navDestinationSwitch](arkts-arkui-uiobserver-onnavdestinationswitch-f.md#on_navDestinationSwitch) |
| [on_navDestinationSwitch](arkts-arkui-uiobserver-onnavdestinationswitch-f.md#on_navDestinationSwitch) |
| [on_navDestinationUpdate](arkts-arkui-uiobserver-onnavdestinationupdate-f.md#on_navDestinationUpdate) |
| [on_navDestinationUpdate](arkts-arkui-uiobserver-onnavdestinationupdate-f.md#on_navDestinationUpdate) |
| [on_routerPageUpdate](arkts-arkui-uiobserver-onrouterpageupdate-f.md#on_routerPageUpdate) |
| [on_scrollEvent](arkts-arkui-uiobserver-onscrollevent-f.md#on_scrollEvent) |
| [on_scrollEvent](arkts-arkui-uiobserver-onscrollevent-f.md#on_scrollEvent) |
| [on_tabContentUpdate](arkts-arkui-uiobserver-ontabcontentupdate-f.md#on_tabContentUpdate) |
| [on_tabContentUpdate](arkts-arkui-uiobserver-ontabcontentupdate-f.md#on_tabContentUpdate) |
| [on_willDraw](arkts-arkui-uiobserver-onwilldraw-f.md#on_willDraw) |

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
