# TouchTestStrategy

Defines the touch test strategy object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum TouchTestStrategy--><!--Device-unnamed-export declare enum TouchTestStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DEFAULT

```TypeScript
DEFAULT = 0
```

Custom dispatch has no effect; the system distributes events based on the hit status of the current node.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchTestStrategy-DEFAULT = 0--><!--Device-TouchTestStrategy-DEFAULT = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## FORWARD_COMPETITION

```TypeScript
FORWARD_COMPETITION = 1
```

The specified event is forwarded to a particular child node, and the system determines whether to distribute the event to other sibling nodes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchTestStrategy-FORWARD_COMPETITION = 1--><!--Device-TouchTestStrategy-FORWARD_COMPETITION = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## FORWARD

```TypeScript
FORWARD = 2
```

The specified event is forwarded to a particular child node, and the system no longer distributes the event to other sibling nodes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TouchTestStrategy-FORWARD = 2--><!--Device-TouchTestStrategy-FORWARD = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

