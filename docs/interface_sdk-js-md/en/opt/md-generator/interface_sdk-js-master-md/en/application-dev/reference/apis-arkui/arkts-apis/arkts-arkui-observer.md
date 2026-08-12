# @ohos.arkui.observer

Provides APIs for listening for UI component behavior changes.

> **NOTE：**
> 
> - UIObserver can only listen for relevant information within the current process and does not support obtaining
> information in cross-process scenarios&lt;!--Del--&gt; such as [UIExtensionComponent](ui_extension_component)&lt;!--
&gt; DelEnd-->.

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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [off](arkts-arkui-uiobserver-off-f.md#off) |
| [off](arkts-arkui-uiobserver-off-f.md#off-1) |
| [off](arkts-arkui-uiobserver-off-f.md#off-2) |
| [off](arkts-arkui-uiobserver-off-f.md#off-3) |
| [off](arkts-arkui-uiobserver-off-f.md#off-4) |
| [off](arkts-arkui-uiobserver-off-f.md#off-5) |
| [off](arkts-arkui-uiobserver-off-f.md#off-6) |
| [off](arkts-arkui-uiobserver-off-f.md#off-7) |
| [off](arkts-arkui-uiobserver-off-f.md#off-8) |
| [off](arkts-arkui-uiobserver-off-f.md#off-9) |
| [off](arkts-arkui-uiobserver-off-f.md#off-10) |
| [off](arkts-arkui-uiobserver-off-f.md#off-11) |
| [on](arkts-arkui-uiobserver-on-f.md#on) |
| [on](arkts-arkui-uiobserver-on-f.md#on-1) |
| [on](arkts-arkui-uiobserver-on-f.md#on-2) |
| [on](arkts-arkui-uiobserver-on-f.md#on-3) |
| [on](arkts-arkui-uiobserver-on-f.md#on-4) |
| [on](arkts-arkui-uiobserver-on-f.md#on-5) |
| [on](arkts-arkui-uiobserver-on-f.md#on-6) |
| [on](arkts-arkui-uiobserver-on-f.md#on-7) |
| [on](arkts-arkui-uiobserver-on-f.md#on-8) |
| [on](arkts-arkui-uiobserver-on-f.md#on-9) |
| [on](arkts-arkui-uiobserver-on-f.md#on-10) |
| [on](arkts-arkui-uiobserver-on-f.md#on-11) | Subscribes to **Navigation** component page switching events. Compared with  [uiObserver.on](uiObserver.on( type: 'navDestinationSwitch', context: UIAbilityContext \|

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
| [RouterPageState](arkts-arkui-uiobserver-routerpagestate-e.md) | Enumerates the states of a page during routing. **RouterPageState** is used in  [RouterPageInfo](arkts-arkui-uiobserver-routerpageinfo-c.md#RouterPageInfo) as the callback parameter for passive observation via  [routerPageUpdate](uiObserver.on(type: 'routerPageUpdate', context: UIAbilityContext \|
| [ScrollEventType](arkts-arkui-uiobserver-scrolleventtype-e.md) |
| [TabContentState](arkts-arkui-uiobserver-tabcontentstate-e.md) |
