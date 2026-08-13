# PiPControlGroup

```TypeScript
type PiPControlGroup = VideoPlayControlGroup | VideoCallControlGroup | VideoMeetingControlGroup
    | VideoLiveControlGroup
```

Describes the optional component groups of the PiP controller. An application can configure whether to display these optional components. This API must match [PiPTemplateType](arkts-arkui-pipwindow-piptemplatetype-e.md#PiPTemplateType) when being used. Otherwise, the [create](arkts-arkui-pipwindow-create-f.md#create) API returns error code 401.

**Since:** 26.0.0

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-PiPWindow-type PiPControlGroup = VideoPlayControlGroup | VideoCallControlGroup | VideoMeetingControlGroup    | VideoLiveControlGroup--><!--Device-PiPWindow-type PiPControlGroup = VideoPlayControlGroup | VideoCallControlGroup | VideoMeetingControlGroup    | VideoLiveControlGroup-End-->

**System capability:** SystemCapability.Window.SessionManager

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [VideoPlayControlGroup](arkts-arkui-pipwindow-videoplaycontrolgroup-e.md) |
| [VideoCallControlGroup](arkts-arkui-pipwindow-videocallcontrolgroup-e.md) |
| [VideoMeetingControlGroup](arkts-arkui-pipwindow-videomeetingcontrolgroup-e.md) |
| [VideoLiveControlGroup](arkts-arkui-pipwindow-videolivecontrolgroup-e.md) |
