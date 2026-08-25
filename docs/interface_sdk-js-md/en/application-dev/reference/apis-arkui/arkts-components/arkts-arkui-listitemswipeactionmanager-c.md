# ListItemSwipeActionManager

Implements the swipe action menu manager for list items.

**Since:** 21

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## collapse

```TypeScript
static collapse(node: FrameNode): void
```

Collapses the swipe action menu for the specified list item.

**Since:** 21

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [FrameNode](../arkts-apis/arkts-arkui-framenode-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100023](../errorcode-node.md#100023-parameter-error) |
| [106203](../errorcode-node.md#106203-passed-node-not-mounted-to-component-tree) |

## expand

```TypeScript
static expand(node: FrameNode, direction: ListItemSwipeActionDirection): void
```

Expands the swipe action menu for the specified list item.

**Since:** 21

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| node | [FrameNode](../arkts-apis/arkts-arkui-framenode-c.md) | Yes |
| direction | [ListItemSwipeActionDirection](arkts-arkui-listitemswipeactiondirection-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100023](../errorcode-node.md#100023-parameter-error) |
| [106203](../errorcode-node.md#106203-passed-node-not-mounted-to-component-tree) |
