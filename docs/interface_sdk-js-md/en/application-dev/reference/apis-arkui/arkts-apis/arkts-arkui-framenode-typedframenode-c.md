# TypedFrameNode

TypedFrameNode继承自[FrameNode](arkts-arkui-framenode-framenodeoptions-i.md)，用于声明具体类型的FrameNode。

> **说明：**
> 
> [commonAttribute](arkts-arkui-framenode-c.md#commonattribute)仅在CustomFrameNode上生效，TypedFrameNode上commonAttribute行为未定义。建议使用
> [attribute](../../../reference/apis-arkui/js-apis-arkui-frameNode-static.md#属性)接口而非
> [commonAttribute](arkts-arkui-framenode-c.md#commonattribute)接口进行通用属性设置，如node.attribute.backgroundColor(Color.Pink)。

**Inheritance/Implementation:** TypedFrameNode extends [FrameNode](arkts-arkui-framenode-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare abstract class TypedFrameNode<T> extends FrameNode--><!--Device-unnamed-export declare abstract class TypedFrameNode<T> extends FrameNode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attribute

```TypeScript
get attribute(): T
```

获取FrameNode的实例属性以设置属性。

> **说明：**
> 
> [commonAttribute](arkts-arkui-framenode-c.md#commonattribute)仅在CustomFrameNode上生效，TypedFrameNode上commonAttribute行为未定义。建议使用
> [attribute](../../../reference/apis-arkui/js-apis-arkui-frameNode-static.md#属性)接口而非
> [commonAttribute](arkts-arkui-framenode-c.md#commonattribute)接口进行通用属性设置，如node.attribute.backgroundColor(Color.Pink)。

**Type:** T

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TypedFrameNode-get attribute(): T--><!--Device-TypedFrameNode-get attribute(): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

