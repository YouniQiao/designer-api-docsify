# XComponentFrameNode

Defines the XComponent type of FrameNode.

**Inheritance/Implementation:** XComponentFrameNode extends [TypedFrameNode<XComponentAttribute>](TypedFrameNode<XComponentAttribute>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-typeNode-abstract class XComponentFrameNode extends TypedFrameNode<XComponentAttribute>--><!--Device-typeNode-abstract class XComponentFrameNode extends TypedFrameNode<XComponentAttribute>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(value: XComponentParameters): XComponentAttribute
```

Initialize XComponent FrameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentFrameNode-abstract initialize(value: XComponentParameters): XComponentAttribute--><!--Device-XComponentFrameNode-abstract initialize(value: XComponentParameters): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [XComponentParameters](arkts-arkui-xcomponent-xcomponentparameters-i.md) | Yes | Indicates the options of the xcomponent. |

**Return value:**

| Type | Description |
| --- | --- |
| XComponentAttribute |  |

## initialize

```TypeScript
abstract initialize(value: XComponentOptions): XComponentAttribute
```

Initialize XComponent FrameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentFrameNode-abstract initialize(value: XComponentOptions): XComponentAttribute--><!--Device-XComponentFrameNode-abstract initialize(value: XComponentOptions): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | XComponentOptions | Yes | Indicates the options of the xcomponent. |

**Return value:**

| Type | Description |
| --- | --- |
| XComponentAttribute |  |

## initialize

```TypeScript
abstract initialize(params: NativeXComponentParameters): XComponentAttribute
```

Initialize XComponent FrameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentFrameNode-abstract initialize(params: NativeXComponentParameters): XComponentAttribute--><!--Device-XComponentFrameNode-abstract initialize(params: NativeXComponentParameters): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | NativeXComponentParameters | Yes | Indicates the constructor parameters of the xcomponent for native developing. |

**Return value:**

| Type | Description |
| --- | --- |
| XComponentAttribute |  |

