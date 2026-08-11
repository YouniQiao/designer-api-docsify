# PathShape

Defines a path drawing class.

**Inheritance/Implementation:** PathShape extends [CommonShapeMethod](arkts-arkui-arkui-shape-commonshapemethod-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class PathShape extends CommonShapeMethod--><!--Device-unnamed-export declare class PathShape extends CommonShapeMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { RectShape, CircleShape, EllipseShape, PathShape } from 'kits/@kit.ArkUI';
```

## commands

```TypeScript
commands(commands: string): this
```

Sets the commands for drawing the PathShape.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PathShape-commands(commands: string): this--><!--Device-PathShape-commands(commands: string): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| commands | string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## constructor

```TypeScript
constructor(options?: PathShapeOptions)
```

Constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PathShape-constructor(options?: PathShapeOptions)--><!--Device-PathShape-constructor(options?: PathShapeOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PathShapeOptions](arkts-arkui-arkui-shape-pathshapeoptions-i.md) | No |  |

