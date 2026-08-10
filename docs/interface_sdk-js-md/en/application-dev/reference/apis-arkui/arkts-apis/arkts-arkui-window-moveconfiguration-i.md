# MoveConfiguration

窗口移动选项。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-window-interface MoveConfiguration--><!--Device-window-interface MoveConfiguration-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## displayId

```TypeScript
displayId?: long
```

目标屏幕ID，该参数应为整数，输入非整数时将向下取整。默认值为undefined。填入该参数时，将移动到相对于目标屏幕左上角的指定位置。此参数不传、传undefined或传入目标屏幕ID不存在时，将移动到相对于当前屏幕左上角的指定位置。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-MoveConfiguration-displayId?: long--><!--Device-MoveConfiguration-displayId?: long-End-->

**System capability:** SystemCapability.Window.SessionManager

