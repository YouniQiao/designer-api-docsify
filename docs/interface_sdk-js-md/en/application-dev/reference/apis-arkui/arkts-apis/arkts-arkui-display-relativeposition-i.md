# RelativePosition

相对坐标系下的坐标位置，以displayId对应的屏幕左上角为原点。

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

相对坐标所对应的屏幕ID，仅支持整数输入，且需大于等于0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RelativePosition-displayId: long--><!--Device-RelativePosition-displayId: long-End-->

**System capability:** SystemCapability.Window.SessionManager

## position

```TypeScript
position: Position
```

以displayId所指定屏幕左上角为原点的坐标值。

**Type:** [Position](arkts-arkui-display-position-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RelativePosition-position: Position--><!--Device-RelativePosition-position: Position-End-->

**System capability:** SystemCapability.Window.SessionManager

