# ScrollFrameNode

定义Scroll类型的FrameNode。

**Inheritance/Implementation:** ScrollFrameNode extends [TypedFrameNode<ScrollAttribute>](TypedFrameNode<ScrollAttribute>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-typeNode-abstract class ScrollFrameNode extends TypedFrameNode<ScrollAttribute>--><!--Device-typeNode-abstract class ScrollFrameNode extends TypedFrameNode<ScrollAttribute>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(scroller?: Scroller): ScrollAttribute
```

初始化Scroll类型的FrameNode。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollFrameNode-abstract initialize(scroller?: Scroller): ScrollAttribute--><!--Device-ScrollFrameNode-abstract initialize(scroller?: Scroller): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scroller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | No | scroll的控制器。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ScrollAttribute](../arkts-components/arkts-arkui-scroll-attribute.md) |  |

