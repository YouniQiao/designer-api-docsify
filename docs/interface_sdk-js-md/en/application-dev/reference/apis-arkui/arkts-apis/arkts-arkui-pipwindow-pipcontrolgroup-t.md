# PiPControlGroup

```TypeScript
type PiPControlGroup = VideoPlayControlGroup | VideoCallControlGroup | VideoMeetingControlGroup
    | VideoLiveControlGroup
```

Describes the optional component groups of the PiP controller. An application can configure whether to display these optional components. This API must match [PiPTemplateType]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ when being used.Otherwise, the [create]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ API returns error code 401.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPWindow-type PiPControlGroup = VideoPlayControlGroup | VideoCallControlGroup | VideoMeetingControlGroup    | VideoLiveControlGroup--><!--Device-PiPWindow-type PiPControlGroup = VideoPlayControlGroup | VideoCallControlGroup | VideoMeetingControlGroup    | VideoLiveControlGroup-End-->

**System capability:** SystemCapability.Window.SessionManager

| Type | Description |
| --- | --- |
| VideoPlayControlGroup | Video playback component group. |
| VideoCallControlGroup | Video call component group. |
| VideoMeetingControlGroup | Video meeting component group. |
| VideoLiveControlGroup | Live video component group. |

