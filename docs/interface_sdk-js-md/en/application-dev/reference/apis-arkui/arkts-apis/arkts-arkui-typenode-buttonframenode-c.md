# ButtonFrameNode

Define the Button type of FrameNode.

**Inheritance/Implementation:** ButtonFrameNode extends [TypedFrameNode<ButtonAttribute>](TypedFrameNode<ButtonAttribute>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-typeNode-abstract class ButtonFrameNode extends TypedFrameNode<ButtonAttribute>--><!--Device-typeNode-abstract class ButtonFrameNode extends TypedFrameNode<ButtonAttribute>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(): ButtonAttribute
```

Initialize Button FrameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ButtonFrameNode-abstract initialize(): ButtonAttribute--><!--Device-ButtonFrameNode-abstract initialize(): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [ButtonAttribute](../arkts-components/arkts-arkui-button-attribute.md) |  |

## initialize

```TypeScript
abstract initialize(value: ButtonOptions): ButtonAttribute
```

Initialize Button FrameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ButtonFrameNode-abstract initialize(value: ButtonOptions): ButtonAttribute--><!--Device-ButtonFrameNode-abstract initialize(value: ButtonOptions): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ButtonOptions](../arkts-components/arkts-arkui-buttonoptions-i.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ButtonAttribute](../arkts-components/arkts-arkui-button-attribute.md) |  |

## initialize

```TypeScript
abstract initialize(label: ResourceStr, options?: ButtonOptions): ButtonAttribute
```

Initialize Button FrameNode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ButtonFrameNode-abstract initialize(label: ResourceStr, options?: ButtonOptions): ButtonAttribute--><!--Device-ButtonFrameNode-abstract initialize(label: ResourceStr, options?: ButtonOptions): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| label | [ResourceStr](arkts-arkui-resourcestr-t.md) | Yes |  |
| options | [ButtonOptions](../arkts-components/arkts-arkui-buttonoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ButtonAttribute](../arkts-components/arkts-arkui-button-attribute.md) |  |

