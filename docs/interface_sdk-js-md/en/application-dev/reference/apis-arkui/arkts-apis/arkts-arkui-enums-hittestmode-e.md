# HitTestMode

Defines the hit test mode.@enum { number }

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Default

```TypeScript
Default = 0
```

Both self and children nodes respond to the hit test for touch events, but block hit test of the other nodes which is masked by this node.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Block

```TypeScript
Block = 1
```

Self respond to the hit test for touch events, but block hit test of children and other nodes which is masked by this node.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Transparent

```TypeScript
Transparent = 2
```

Self and children respond to the hit test for touch events, and allow hit test of other nodes which is masked by this node.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## None

```TypeScript
None = 3
```

Self not respond to the hit test for touch events, but children respond to the hit test for touch events.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## BLOCK_HIERARCHY

```TypeScript
BLOCK_HIERARCHY = 4
```

Blocks all lower-priority siblings and parent nodes from receiving the event.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## BLOCK_DESCENDANTS

```TypeScript
BLOCK_DESCENDANTS = 5
```

Self not respond to the hit test for touch events, and all descendants (children, grandchildren, etc.) not respond to the hit test for touch events too.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
