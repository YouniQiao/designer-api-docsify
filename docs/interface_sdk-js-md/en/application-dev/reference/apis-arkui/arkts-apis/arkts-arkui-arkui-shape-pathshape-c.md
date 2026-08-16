# PathShape

Represents a path used in the **clipShape** and **maskShape** APIs. This API inherits from [CommonShapeMethod](arkts-arkui-arkui-shape-commonshapemethod-c.md#CommonShapeMethod).

**Inheritance/Implementation:** PathShape extends CommonShapeMethod<PathShape>

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-unnamed-export declare class PathShape--><!--Device-unnamed-export declare class PathShape-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { RectShape } from 'RectShape';
import { CircleShape } from 'CircleShape';
import { EllipseShape } from 'EllipseShape';
import { PathShape } from 'PathShape';
```

## commands

```TypeScript
commands(commands: string): PathShape
```

Sets the path drawing commands.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PathShape-commands(commands: string): PathShape--><!--Device-PathShape-commands(commands: string): PathShape-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| commands | string | Yes | Path drawing commands. |

**Return value:**

| Type | Description |
| --- | --- |
| [PathShape](arkts-arkui-arkui-shape-pathshape-c.md) | PathShape** object. |

## constructor

```TypeScript
constructor(options?: PathShapeOptions)
```

A constructor used to create a **PathShape** object.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PathShape-constructor(options?: PathShapeOptions)--><!--Device-PathShape-constructor(options?: PathShapeOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PathShapeOptions](arkts-arkui-arkui-shape-pathshapeoptions-i.md) | No | Path parameters. |

