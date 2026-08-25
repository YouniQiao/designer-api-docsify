# executeDrag

## Modules to Import

```TypeScript
import { dragController } from 'kits/@kit.ArkUI';
```

## executeDrag

```TypeScript
function executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: DragInfo,
    callback: AsyncCallback<DragEventParam>): void
```

Initiates a drag action, with the object to be dragged and the drag information passed in. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> Since API version 11, you can use the [getDragController](arkts-arkui-arkui-uicontext-uicontext-c.md#getdragcontroller) API in
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [DragController](arkts-arkui-arkui-uicontext-dragcontroller-c.md) object
> associated with the current UI context.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** executeDrag

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| custom | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| [DragItemInfo](../arkts-components/arkts-arkui-dragiteminfo-i.md) | Yes |
| dragInfo | [DragInfo](arkts-arkui-dragcontroller-draginfo-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DragEventParam](arkts-arkui-dragcontroller-drageventparam-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |


## executeDrag

```TypeScript
function executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: DragInfo): Promise<DragEventParam>
```

Initiates a drag action, with the object to be dragged and the drag information passed in. This API uses a promise to return the result.

> **NOTE：**&gt;
> Since API version 11, you can use the [getDragController](arkts-arkui-arkui-uicontext-uicontext-c.md#getdragcontroller) API in
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [DragController](arkts-arkui-arkui-uicontext-dragcontroller-c.md) object
> associated with the current UI context.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** executeDrag

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| custom | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| [DragItemInfo](../arkts-components/arkts-arkui-dragiteminfo-i.md) | Yes |
| dragInfo | [DragInfo](arkts-arkui-dragcontroller-draginfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;{ event: DragEvent, extraParams: string |
| Promise&lt;[DragEventParam](arkts-arkui-dragcontroller-drageventparam-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |
