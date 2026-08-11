# RelativePosition

Describes a coordinate position in the relative coordinate system, with the origin in the top-left corner of the screen specified by **displayId**.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-display-interface RelativePosition--><!--Device-display-interface RelativePosition-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## displayId

```TypeScript
displayId: long
```

Display ID for the relative coordinates. Only integers are supported, and the value must be greater than or equal to 0.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RelativePosition-displayId: long--><!--Device-RelativePosition-displayId: long-End-->

**System capability:** SystemCapability.Window.SessionManager

## position

```TypeScript
position: Position
```

Coordinates with the top-left corner of the screen specified by **displayId** as the origin.

**Type:** [Position](arkts-arkui-display-position-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RelativePosition-position: Position--><!--Device-RelativePosition-position: Position-End-->

**System capability:** SystemCapability.Window.SessionManager

