# ButtonFrameNode

Define the Button type of FrameNode.

**Inheritance/Implementation:** ButtonFrameNode extends TypedFrameNode<ButtonAttribute>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(): ButtonAttribute
```

Initialize Button FrameNode.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ButtonAttribute](../arkts-components/arkts-arkui-button-attribute.md) |

## initialize

```TypeScript
abstract initialize(value: ButtonOptions): ButtonAttribute
```

Initialize Button FrameNode.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ButtonOptions](arkts-arkui-button-buttonoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ButtonAttribute](../arkts-components/arkts-arkui-button-attribute.md) |

## initialize

```TypeScript
abstract initialize(label: ResourceStr, options?: ButtonOptions): ButtonAttribute
```

Initialize Button FrameNode.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| label | [ResourceStr](arkts-arkui-resourcestr-t.md) | Yes |
| options | [ButtonOptions](arkts-arkui-button-buttonoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ButtonAttribute](../arkts-components/arkts-arkui-button-attribute.md) |
