# TypedFrameNode

Extends [FrameNode](arkts-arkui-framenode-c.md) to define a FrameNode with specific type constraints.

**Inheritance/Implementation:** TypedFrameNode extends [FrameNode](arkts-arkui-framenode-c.md)

**Since:** 12

<!--Device-unnamed-export interface TypedFrameNode<C, T> extends FrameNode--><!--Device-unnamed-export interface TypedFrameNode<C, T> extends FrameNode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attribute

```TypeScript
readonly attribute: T
```

Attribute configuration object for setting or updating common and specific attributes of the component.

**Type:** T

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TypedFrameNode-readonly attribute: T--><!--Device-TypedFrameNode-readonly attribute: T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
initialize: C
```

Construction parameters for creating a component, used to set or update the component's initial values.

**Type:** C

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TypedFrameNode-initialize: C--><!--Device-TypedFrameNode-initialize: C-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

