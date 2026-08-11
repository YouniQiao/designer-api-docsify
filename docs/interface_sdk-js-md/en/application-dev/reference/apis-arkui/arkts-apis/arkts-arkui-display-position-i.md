# Position

Describes a coordinate position. In the global coordinate system, the origin is the top-left corner of the primary screen. In the relative coordinate system, the origin is the top-left corner of the specified screen.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-display-interface Position--><!--Device-display-interface Position-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## x

```TypeScript
x: long
```

X coordinate relative to the origin, measured in px. The value must be a 32-bit signed integer, and floating-point numbers are rounded down.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Position-x: long--><!--Device-Position-x: long-End-->

**System capability:** SystemCapability.Window.SessionManager

## y

```TypeScript
y: long
```

Y coordinate relative to the origin, measured in px. The value must be a 32-bit signed integer, and floating-point numbers are rounded down.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Position-y: long--><!--Device-Position-y: long-End-->

**System capability:** SystemCapability.Window.SessionManager

