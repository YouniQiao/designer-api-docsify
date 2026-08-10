# XComponentFrameNode

定义XComponent 类型的FrameNode。

**Inheritance/Implementation:** XComponentFrameNode extends [TypedFrameNode<XComponentAttribute>](TypedFrameNode<XComponentAttribute>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-typeNode-abstract class XComponentFrameNode extends TypedFrameNode<XComponentAttribute>--><!--Device-typeNode-abstract class XComponentFrameNode extends TypedFrameNode<XComponentAttribute>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(value: XComponentParameters): XComponentAttribute
```

初始化XComponent类型的FrameNode。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentFrameNode-abstract initialize(value: XComponentParameters): XComponentAttribute--><!--Device-XComponentFrameNode-abstract initialize(value: XComponentParameters): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [XComponentParameters](arkts-arkui-xcomponent-xcomponentparameters-i.md) | Yes | xcomponent节点的选项。 |

**Return value:**

| Type | Description |
| --- | --- |
| [XComponentAttribute](../arkts-components/arkts-arkui-xcomponent-attribute.md) |  |

## initialize

```TypeScript
abstract initialize(value: XComponentOptions): XComponentAttribute
```

初始化XComponent类型的FrameNode。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentFrameNode-abstract initialize(value: XComponentOptions): XComponentAttribute--><!--Device-XComponentFrameNode-abstract initialize(value: XComponentOptions): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [XComponentOptions](../arkts-components/arkts-arkui-xcomponentoptions-i.md) | Yes | xcomponent节点的选项。 |

**Return value:**

| Type | Description |
| --- | --- |
| [XComponentAttribute](../arkts-components/arkts-arkui-xcomponent-attribute.md) |  |

## initialize

```TypeScript
abstract initialize(params: NativeXComponentParameters): XComponentAttribute
```

初始化XComponent类型的FrameNode。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentFrameNode-abstract initialize(params: NativeXComponentParameters): XComponentAttribute--><!--Device-XComponentFrameNode-abstract initialize(params: NativeXComponentParameters): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [NativeXComponentParameters](../arkts-components/arkts-arkui-nativexcomponentparameters-i.md) | Yes | 用于原生开发的 XComponent 的构造参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [XComponentAttribute](../arkts-components/arkts-arkui-xcomponent-attribute.md) |  |

