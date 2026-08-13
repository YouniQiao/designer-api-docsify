# PathShape

Represents a path used in the **clipShape** and **maskShape** APIs. This API inherits from [CommonShapeMethod](arkts-arkui-arkui-shape-commonshapemethod-c.md#CommonShapeMethod).

**Inheritance/Implementation:** PathShape extends CommonShapeMethod<PathShape>

**Since:** 12

**Deprecated since:** -1

<!--Device-unnamed-export declare class PathShape--><!--Device-unnamed-export declare class PathShape-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { RectShape, CircleShape, EllipseShape, PathShape } from '@kit.ArkUI';
```

## commands

```TypeScript
commands(commands: string): PathShape
```

Sets the path drawing commands.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PathShape-commands(commands: string): PathShape--><!--Device-PathShape-commands(commands: string): PathShape-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [commands](#commands) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PathShape](arkts-arkui-arkui-shape-pathshape-c.md) |

## constructor

```TypeScript
constructor(options?: PathShapeOptions)
```

A constructor used to create a **PathShape** object.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-PathShape-constructor(options?: PathShapeOptions)--><!--Device-PathShape-constructor(options?: PathShapeOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [PathShapeOptions](arkts-arkui-arkui-shape-pathshapeoptions-i.md) | No |
