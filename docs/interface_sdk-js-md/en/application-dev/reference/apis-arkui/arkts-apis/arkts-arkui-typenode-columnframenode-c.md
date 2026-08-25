# ColumnFrameNode

Define the Column type of FrameNode.

**Inheritance/Implementation:** ColumnFrameNode extends TypedFrameNode<ColumnAttribute>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(options?: ColumnOptions | ColumnOptionsV2): ColumnAttribute
```

Initialize Column FrameNode.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | ColumnOptions \| [ColumnOptionsV2](../arkts-components/arkts-arkui-columnoptionsv2-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColumnAttribute](../arkts-components/arkts-arkui-column-attribute.md) |
