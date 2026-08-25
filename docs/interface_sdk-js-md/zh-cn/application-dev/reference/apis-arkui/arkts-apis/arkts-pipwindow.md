# @ohos.PiPWindow

该模块提供画中画基础功能，包括判断当前系统是否支持画中画功能，以及创建画中画控制器用于启动或停止画中画等。适用于视频播放、视频通话或视频会议场景下，以小窗（画中画）模式呈现内容。

> **说明：**&gt;
> - 在<!--RP2-->OpenHarmony 6.0<!--RP2End-->之前，支持在Phone、Tablet设备使用画中画功能，其他设备不可用；从<!--RP2-->OpenHarmony 6.0&lt;!--RP2End--
&gt; &gt;开始，支持在Phone、PC/2in1、Tablet设备使用画中画功能，其他设备不可用。&gt;
> - 针对系统能力SystemCapability.Window.SessionManager，请先使用
> [canIUse()](arkts-arkui-global-caniuse-f.md)接口判断当前设备是否支持此syscap及对应接口。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.Window.SessionManager

## 导入模块

```TypeScript
import { PiPWindow } from '@kit.ArkUI';
```

## 汇总

### 函数

| 名称 |
| --- |
| [create](arkts-arkui-pipwindow-create-f.md) |
| [create](arkts-arkui-pipwindow-create-f.md) |
| [isPiPEnabled](arkts-arkui-pipwindow-ispipenabled-f.md) |

### 接口

| 名称 |
| --- |
| [ControlEventParam](arkts-arkui-pipwindow-controleventparam-i.md) |
| [PiPConfiguration](arkts-arkui-pipwindow-pipconfiguration-i.md) |
| [PiPController](arkts-arkui-pipwindow-pipcontroller-i.md) |
| [PiPWindowInfo](arkts-arkui-pipwindow-pipwindowinfo-i.md) |
| [PiPWindowSize](arkts-arkui-pipwindow-pipwindowsize-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [PiPController](arkts-arkui-pipwindow-pipcontroller-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
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
### 枚举（系统接口）

| 名称 |
| --- |
| [PiPTemplateType](arkts-arkui-pipwindow-piptemplatetype-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [ControlPanelActionEventCallback](arkts-arkui-pipwindow-controlpanelactioneventcallback-t.md) |
| [PiPActionEventType](arkts-arkui-pipwindow-pipactioneventtype-t.md) |
| [PiPCallActionEvent](arkts-arkui-pipwindow-pipcallactionevent-t.md) |
| [PiPControlGroup](arkts-arkui-pipwindow-pipcontrolgroup-t.md) |
| [PiPLiveActionEvent](arkts-arkui-pipwindow-pipliveactionevent-t.md) |
| [PiPMeetingActionEvent](arkts-arkui-pipwindow-pipmeetingactionevent-t.md) |
| [PiPVideoActionEvent](arkts-arkui-pipwindow-pipvideoactionevent-t.md) |
| [StateChangeCallback](arkts-arkui-pipwindow-statechangecallback-t.md) |
