# WindowAnchorInfo (System API)

一级子窗与主窗保持相对位置的窗口锚点参数信息。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-window-interface WindowAnchorInfo--><!--Device-window-interface WindowAnchorInfo-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## anchorType

```TypeScript
anchorType: WindowAnchor
```

一级子窗与主窗保持相对位置不变时的窗口锚点枚举。

**Type:** [WindowAnchor](arkts-arkui-window-windowanchor-e.md)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowAnchorInfo-anchorType: WindowAnchor--><!--Device-WindowAnchorInfo-anchorType: WindowAnchor-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## offsetX

```TypeScript
offsetX?: int
```

一级子窗锚点与主窗锚点位置的X轴偏移量，单位为px。仅支持整数输入，浮点数向下取整，默认值为0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** 0

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowAnchorInfo-offsetX?: int--><!--Device-WindowAnchorInfo-offsetX?: int-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

## offsetY

```TypeScript
offsetY?: int
```

一级子窗锚点与主窗锚点位置的Y轴偏移量，单位为px。仅支持整数输入，浮点数向下取整，默认值为0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** 0

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowAnchorInfo-offsetY?: int--><!--Device-WindowAnchorInfo-offsetY?: int-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

