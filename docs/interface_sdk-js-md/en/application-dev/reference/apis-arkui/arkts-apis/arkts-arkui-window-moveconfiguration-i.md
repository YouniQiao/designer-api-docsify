# MoveConfiguration

Describes the window movement configuration.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-window-interface MoveConfiguration--><!--Device-window-interface MoveConfiguration-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from 'window';
```

## displayId

```TypeScript
displayId?: long
```

Target display ID. The value must be an integer. If a non-integer is passed in, the value is rounded down. If this parameter is passed in, the window is positioned relative to the top-left corner of the target display. If this parameter is left empty or the target display ID does not exist, the window is positioned relative to the top-left corner of the current display.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MoveConfiguration-displayId?: long--><!--Device-MoveConfiguration-displayId?: long-End-->

**System capability:** SystemCapability.Window.SessionManager

