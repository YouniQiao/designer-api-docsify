# TypedFrameNode

TypedFrameNode继承自[FrameNode](arkts-arkui-framenode-c.md)，用于声明具体类型的FrameNode，支持Text、Image、Button、Column等多种组件类型，适用于通过代码动态创建具体类型组件节点的场景。

**Inheritance/Implementation:** TypedFrameNode extends [FrameNode](arkts-arkui-framenode-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-export interface TypedFrameNode<C, T> extends FrameNode--><!--Device-unnamed-export interface TypedFrameNode<C, T> extends FrameNode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attribute

```TypeScript
readonly attribute: T
```

该接口用于获取对应组件的属性设置对象，以设置/更新组件的通用、私有属性。

**Type:** T

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TypedFrameNode-readonly attribute: T--><!--Device-TypedFrameNode-readonly attribute: T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
initialize: C
```

该接口用于传入对应组件的构造参数，以设置/更新组件的初始值。

**Type:** C

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TypedFrameNode-initialize: C--><!--Device-TypedFrameNode-initialize: C-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

