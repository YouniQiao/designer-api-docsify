# NodeContent

**NodeContent** is the ArkUI-provided manager for ContentSlot.

> **NOTE：**&gt;
> - **NodeContent** objects do not support JSON serialization.

**Inheritance/Implementation:** NodeContent extends Content

**Since:** 12

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addFrameNode

```TypeScript
addFrameNode(node: FrameNode): void
```

Adds a FrameNode to this **NodeContent** object.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100025](../errorcode-node.md#100025-invalid-parameter-value) |

## constructor

```TypeScript
constructor()
```

A constructor used to create a **NodeContent** object.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## removeFrameNode

```TypeScript
removeFrameNode(node: FrameNode): void
```

Removes a FrameNode from this **NodeContent** object.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes |
