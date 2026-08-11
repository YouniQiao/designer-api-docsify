# DynamicNode

Define DynamicNode.

**Since:** 12

<!--Device-unnamed-declare class DynamicNode<T>--><!--Device-unnamed-declare class DynamicNode<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onMove

```TypeScript
onMove(handler: Optional<OnMoveHandler>): T
```

Invoked when data is moved during drag and drop sorting.This callback is only applicable in a List component.where each ForEach iteration generates a ListItem component.It allows you to define custom drag actions and handle various drag events.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DynamicNode-onMove(handler: Optional<OnMoveHandler>): T--><!--Device-DynamicNode-onMove(handler: Optional<OnMoveHandler>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [Optional](arkts-arkui-optional-t.md)&lt;OnMoveHandler&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onMove

```TypeScript
onMove(handler: Optional<OnMoveHandler>, eventHandler: ItemDragEventHandler): T
```

Set the move action.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DynamicNode-onMove(handler: Optional<OnMoveHandler>, eventHandler: ItemDragEventHandler): T--><!--Device-DynamicNode-onMove(handler: Optional<OnMoveHandler>, eventHandler: ItemDragEventHandler): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [Optional](arkts-arkui-optional-t.md)&lt;OnMoveHandler&gt; | Yes |
| eventHandler | [ItemDragEventHandler](arkts-arkui-itemdrageventhandler-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |
