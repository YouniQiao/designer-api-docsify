# TextFrameNode

定义Text类型的FrameNode。

**Inheritance/Implementation:** TextFrameNode extends [TypedFrameNode<TextAttribute>](TypedFrameNode<TextAttribute>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-typeNode-abstract class TextFrameNode extends TypedFrameNode<TextAttribute>--><!--Device-typeNode-abstract class TextFrameNode extends TypedFrameNode<TextAttribute>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(content?: string | Resource, value?: TextOptions): TextAttribute
```

初始化Text类型的FrameNode。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextFrameNode-abstract initialize(content?: string | Resource, value?: TextOptions): TextAttribute--><!--Device-TextFrameNode-abstract initialize(content?: string | Resource, value?: TextOptions): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | string \| Resource | No |  |
| value | [TextOptions](../arkts-components/arkts-arkui-textoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [TextAttribute](../arkts-components/arkts-arkui-text-attribute.md) |  |

