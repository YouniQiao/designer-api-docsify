# @ohos.PiPWindow

The module provides basic APIs for manipulating Picture in Picture (PiP). For example, you can use the APIs to check whether the PiP feature is supported and create a PiP controller to start or stop a PiP window. PiP is mainly used in video playback, video calls, or video meetings.

> **NOTE：**
> 
> - Before &lt;!--RP2--&gt;OpenHarmony 6.0&lt;!--RP2End--&gt;, the PiP feature was supported only on phones and tablets. Starting
> from &lt;!--RP2--&gt;OpenHarmony 6.0&lt;!--RP2End--&gt;, the PiP feature is supported on phones, PCs/2-in-1 devices, tablets,
> but is unavailable on all other devices.
> 
> - For the system capability SystemCapability.Window.SessionManager, use
> [canIUse()](arkts-arkui-global-caniuse-f.md#caniuse) to check whether the device supports this system
> capability and the corresponding APIs.

**Since:** 11

<!--Device-unnamed-declare namespace PiPWindow--><!--Device-unnamed-declare namespace PiPWindow-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { PiPWindow } from 'kits/@kit.ArkUI';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [create](arkts-arkui-pipwindow-create-f.md#create) |
| [create](arkts-arkui-pipwindow-create-f.md#create-1) |
| [isPiPEnabled](arkts-arkui-pipwindow-ispipenabled-f.md#ispipenabled) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ControlEventParam](arkts-arkui-pipwindow-controleventparam-i.md) |
| [PiPConfiguration](arkts-arkui-pipwindow-pipconfiguration-i.md) |
| [PiPController](arkts-arkui-pipwindow-pipcontroller-i.md) |
| [PiPWindowInfo](arkts-arkui-pipwindow-pipwindowinfo-i.md) |
| [PiPWindowSize](arkts-arkui-pipwindow-pipwindowsize-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PiPController](arkts-arkui-pipwindow-pipcontroller-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PiPControlStatus](arkts-arkui-pipwindow-pipcontrolstatus-e.md) |
| [PiPControlType](arkts-arkui-pipwindow-pipcontroltype-e.md) |
| [PiPState](arkts-arkui-pipwindow-pipstate-e.md) |
| [PiPTemplateType](arkts-arkui-pipwindow-piptemplatetype-e.md) |
| [VideoCallControlGroup](arkts-arkui-pipwindow-videocallcontrolgroup-e.md) |
| [VideoLiveControlGroup](arkts-arkui-pipwindow-videolivecontrolgroup-e.md) |
| [VideoMeetingControlGroup](arkts-arkui-pipwindow-videomeetingcontrolgroup-e.md) |
| [VideoPlayControlGroup](arkts-arkui-pipwindow-videoplaycontrolgroup-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PiPTemplateType](arkts-arkui-pipwindow-piptemplatetype-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ControlPanelActionEventCallback](arkts-arkui-pipwindow-controlpanelactioneventcallback-t.md) |
| [PiPActionEventType](arkts-arkui-pipwindow-pipactioneventtype-t.md) |
| [PiPCallActionEvent](arkts-arkui-pipwindow-pipcallactionevent-t.md) |
| [PiPControlGroup](arkts-arkui-pipwindow-pipcontrolgroup-t.md) |
| [PiPLiveActionEvent](arkts-arkui-pipwindow-pipliveactionevent-t.md) |
| [PiPMeetingActionEvent](arkts-arkui-pipwindow-pipmeetingactionevent-t.md) |
| [PiPVideoActionEvent](arkts-arkui-pipwindow-pipvideoactionevent-t.md) |
