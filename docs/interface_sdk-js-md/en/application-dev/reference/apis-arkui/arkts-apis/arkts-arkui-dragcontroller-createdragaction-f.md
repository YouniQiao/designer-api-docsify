# createDragAction

## Modules to Import

```TypeScript
import { dragController } from 'kits/@kit.ArkUI';
```

## createDragAction

```TypeScript
function createDragAction(customArray: Array<CustomBuilder | DragItemInfo>, dragInfo: DragInfo): DragAction
```

Initiates a drag action, with the object to be dragged and the drag information passed in. This API uses a promise to return the result.

> **NOTE：**&gt;
> - Since API version 11, you can use the
> [getDragController](arkts-arkui-arkui-uicontext-uicontext-c.md#getdragcontroller) API in
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the
> [DragController](arkts-arkui-arkui-uicontext-dragcontroller-c.md) object associated with the current UI context.&gt;
> - For optimal drag and drop performance, limit the number of drag previews.

**Since:** 11

**Deprecated since:** 18

**Substitutes:** createDragAction

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| customArray | Array&lt;[CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| [DragItemInfo](../arkts-components/arkts-arkui-dragiteminfo-i.md)&gt; | Yes |
| dragInfo | [DragInfo](arkts-arkui-dragcontroller-draginfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DragAction](arkts-arkui-dragcontroller-dragaction-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |
