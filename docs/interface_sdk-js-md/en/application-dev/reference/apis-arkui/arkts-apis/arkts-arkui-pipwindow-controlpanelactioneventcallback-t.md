# ControlPanelActionEventCallback

```TypeScript
type ControlPanelActionEventCallback = (event: PiPActionEventType, status?: int) => void
```

描述画中画控制面板控件动作事件回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PiPWindow-type ControlPanelActionEventCallback = (event: PiPActionEventType, status?: int) => void--><!--Device-PiPWindow-type ControlPanelActionEventCallback = (event: PiPActionEventType, status?: int) => void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [PiPActionEventType](arkts-arkui-pipwindow-pipactioneventtype-t.md) | Yes | 回调画中画控制面板控件动作事件类型。<br/>应用依据控件动作事件做相应处理，如触发'playbackStateChanged'事件时，需要开始或停止视频 。 |
| status | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 表示可切换状态的控件当前的状态，如具备打开和关闭两种状态的麦克风控件组、摄像头控件组和静音控件组，打开为1，关闭为0。其余控件该参数返回默认值-1。 取值限定为整数 |

