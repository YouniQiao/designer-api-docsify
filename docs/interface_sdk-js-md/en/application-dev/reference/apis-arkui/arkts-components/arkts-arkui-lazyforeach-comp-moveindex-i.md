# MoveIndex

```TypeScript
interface MoveIndex
```

Defines position of moved data.

**Since:** 12

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## from

```TypeScript
from: number
```

Start position of the move. The value range is [0, data source length - 1]. Rendering is abnormal when the value exceeds the value range.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## to

```TypeScript
to: number
```

Target position of the move. The value range is [0, data source length - 1]. Rendering is abnormal when the value exceeds the value range.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
