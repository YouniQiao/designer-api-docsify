# ExpandMode

Enum for the expand mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export enum ExpandMode--><!--Device-unnamed-export enum ExpandMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NOT_EXPAND

```TypeScript
NOT_EXPAND = 0
```

Do not expand the children of node.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExpandMode-NOT_EXPAND = 0--><!--Device-ExpandMode-NOT_EXPAND = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## EXPAND

```TypeScript
EXPAND = 1
```

Expand the children of node.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExpandMode-EXPAND = 1--><!--Device-ExpandMode-EXPAND = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## LAZY_EXPAND

```TypeScript
LAZY_EXPAND = 2
```

Expand the children of node if needed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExpandMode-LAZY_EXPAND = 2--><!--Device-ExpandMode-LAZY_EXPAND = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## LAZY_NOT_EXPAND

```TypeScript
LAZY_NOT_EXPAND = 3
```

Do not expand children of node.If the FrameNode contains LazyForEach child nodes, child nodes can be obtained directly when nodes in main tree.When nodes are not in main tree, only a node at corresponding position will be created,rather than expanding all child nodes.The child node sequence numbers are calculated based on all child nodes.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ExpandMode-LAZY_NOT_EXPAND = 3--><!--Device-ExpandMode-LAZY_NOT_EXPAND = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

