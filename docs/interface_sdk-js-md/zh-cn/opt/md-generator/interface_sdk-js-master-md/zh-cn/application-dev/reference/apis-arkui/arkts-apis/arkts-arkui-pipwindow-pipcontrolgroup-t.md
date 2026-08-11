# PiPControlGroup

```TypeScript
type PiPControlGroup = VideoPlayControlGroup | VideoCallControlGroup | VideoMeetingControlGroup
    | VideoLiveControlGroup
```

画中画控制面板的可选控件组列表，应用可以配置是否显示可选控件。使用时必须和[PiPTemplateType](arkts-arkui-pipwindow-piptemplatetype-e.md)对应，否则  
[create](arkts-arkui-pipwindow-create-f.md#create)接口抛出401错误码。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-PiPWindow-type PiPControlGroup = VideoPlayControlGroup | VideoCallControlGroup | VideoMeetingControlGroup    | VideoLiveControlGroup--><!--Device-PiPWindow-type PiPControlGroup = VideoPlayControlGroup | VideoCallControlGroup | VideoMeetingControlGroup    | VideoLiveControlGroup-End-->

**系统能力：** SystemCapability.Window.SessionManager

| 类型 |
| --- |
| [VideoPlayControlGroup](arkts-arkui-pipwindow-videoplaycontrolgroup-e.md) |
| [VideoCallControlGroup](arkts-arkui-pipwindow-videocallcontrolgroup-e.md) |
| [VideoMeetingControlGroup](arkts-arkui-pipwindow-videomeetingcontrolgroup-e.md) |
| [VideoLiveControlGroup](arkts-arkui-pipwindow-videolivecontrolgroup-e.md) |
