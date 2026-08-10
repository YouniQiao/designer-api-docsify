# ControlEventParam

画中画控制面板控件动作回调的参数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 26.0.0.

<!--Device-PiPWindow-interface ControlEventParam--><!--Device-PiPWindow-interface ControlEventParam-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { PiPWindow } from 'kits/@kit.ArkUI';
```

## controlType

```TypeScript
controlType: PiPControlType
```

回调画中画控制面板控件动作事件类型。应用依据控件类型做相应处理，如视频模板中暂停/播放控件被点击时，需要开始或停止视频。

**Type:** [PiPControlType](arkts-arkui-pipwindow-pipcontroltype-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ControlEventParam-controlType: PiPControlType--><!--Device-ControlEventParam-controlType: PiPControlType-End-->

**System capability:** SystemCapability.Window.SessionManager

## status

```TypeScript
status?: PiPControlStatus
```

表示可切换状态的控件当前的状态，如具备打开和关闭两种状态的麦克风控件组、摄像头控件组和静音控件组，打开为PiPControlStatus.PLAY，关闭为PiPControlStatus.PAUSE。如不具备开/关和播放/暂停状态的挂断控件默认返回值为-1。

**Type:** [PiPControlStatus](arkts-arkui-pipwindow-pipcontrolstatus-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ControlEventParam-status?: PiPControlStatus--><!--Device-ControlEventParam-status?: PiPControlStatus-End-->

**System capability:** SystemCapability.Window.SessionManager

