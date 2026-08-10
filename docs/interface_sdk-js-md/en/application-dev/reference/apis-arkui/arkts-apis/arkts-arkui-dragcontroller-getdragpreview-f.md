# getDragPreview

## Modules to Import

```TypeScript
import { dragController } from 'kits/@kit.ArkUI';
```

## getDragPreview

```TypeScript
function getDragPreview(): DragPreview
```

返回一个代表拖拽背板的对象。

> **说明：**
> 
> 从API version 11开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [getDragController](arkts-arkui-arkui-uicontext-uicontext-c.md#getdragcontroller)方法获取当前UI
> 上下文关联的[DragController](arkts-arkui-arkui-uicontext-dragcontroller-c.md)对象。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** 18

**Substitutes:** ohos.arkui.UIContext.DragController#getDragPreview

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-dragController-function getDragPreview(): DragPreview--><!--Device-dragController-function getDragPreview(): DragPreview-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [DragPreview](arkts-arkui-dragcontroller-dragpreview-c.md) | 一个代表拖拽背板的对象，提供背板样式设置的接口，在OnDrop和OnDragEnd回调中使用不生效。 |

