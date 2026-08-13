# PiPControlGroup

```TypeScript
type PiPControlGroup = VideoPlayControlGroup | VideoCallControlGroup | VideoMeetingControlGroup
    | VideoLiveControlGroup
```

Describes the optional component groups of the PiP controller. An application can configure whether to display these optional components. This API must match [PiPTemplateType](arkts-arkui-pipwindow-piptemplatetype-e.md#PiPTemplateType) when being used. Otherwise, the [create](arkts-arkui-pipwindow-create-f.md#create) API returns error code 401.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-PiPWindow-type PiPControlGroup = VideoPlayControlGroup | VideoCallControlGroup | VideoMeetingControlGroup    | VideoLiveControlGroup--><!--Device-PiPWindow-type PiPControlGroup = VideoPlayControlGroup | VideoCallControlGroup | VideoMeetingControlGroup    | VideoLiveControlGroup-End-->

**System capability:** SystemCapability.Window.SessionManager

| Type | Description |
| --- | --- |
| VideoPlayControlGroup | Video playback component group. |
| VideoCallControlGroup | Video call component group. |
| VideoMeetingControlGroup | Video meeting component group. |
| VideoLiveControlGroup | Live video component group. |

