# GridFrameNode

定义Grid类型的FrameNode。

**Inheritance/Implementation:** GridFrameNode extends [TypedFrameNode<GridAttribute>](TypedFrameNode<GridAttribute>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-typeNode-abstract class GridFrameNode extends TypedFrameNode<GridAttribute>--><!--Device-typeNode-abstract class GridFrameNode extends TypedFrameNode<GridAttribute>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(scroller?: Scroller, layoutOptions?: GridLayoutOptions): GridAttribute
```

初始化Grid类型的FrameNode。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridFrameNode-abstract initialize(scroller?: Scroller, layoutOptions?: GridLayoutOptions): GridAttribute--><!--Device-GridFrameNode-abstract initialize(scroller?: Scroller, layoutOptions?: GridLayoutOptions): GridAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scroller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | No | grid的控制器。 |
| layoutOptions | [GridLayoutOptions](../arkts-components/arkts-arkui-gridlayoutoptions-i.md) | No | Grid布局选项。 |

**Return value:**

| Type | Description |
| --- | --- |
| [GridAttribute](../arkts-components/arkts-arkui-grid-attribute.md) |  |

