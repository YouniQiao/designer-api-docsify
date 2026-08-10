# ColumnFrameNode

定义Column 类型的FrameNode。

**Inheritance/Implementation:** ColumnFrameNode extends [TypedFrameNode<ColumnAttribute>](TypedFrameNode<ColumnAttribute>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-typeNode-abstract class ColumnFrameNode extends TypedFrameNode<ColumnAttribute>--><!--Device-typeNode-abstract class ColumnFrameNode extends TypedFrameNode<ColumnAttribute>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(options?: ColumnOptions | ColumnOptionsV2): ColumnAttribute
```

初始化Column类型的FrameNode。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColumnFrameNode-abstract initialize(options?: ColumnOptions | ColumnOptionsV2): ColumnAttribute--><!--Device-ColumnFrameNode-abstract initialize(options?: ColumnOptions | ColumnOptionsV2): ColumnAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ColumnOptions](../arkts-components/arkts-arkui-columnoptions-i.md) \| ColumnOptionsV2 | No | Column节点的选项。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ColumnAttribute](../arkts-components/arkts-arkui-column-attribute.md) |  |

