# @ohos.arkui.dragController

This module provides APIs for initiating drag actions. When receiving a gesture event, such as a touch or long-press event, an application can initiate a drag action and carry drag information therein.

> **NOTE：**&gt;
> - The functionality of this module depends on UI context. This means that the APIs of this module cannot be used
> where [the UI context is ambiguous](../../../ui/arkts-global-interface.md#ambiguous-ui-context). For details, see
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md).&gt;
> - You can preview how this component looks on a real device, but not in DevEco Studio Previewer.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { dragController } from '@kit.ArkUI';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createDragAction](arkts-arkui-dragcontroller-createdragaction-f.md) |
| [executeDrag](arkts-arkui-dragcontroller-executedrag-f.md) |
| [executeDrag](arkts-arkui-dragcontroller-executedrag-f.md) |
| [getDragPreview](arkts-arkui-dragcontroller-getdragpreview-f.md) |

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DragPreview](arkts-arkui-dragcontroller-dragpreview-c.md) |
| [SpringLoadingContext](arkts-arkui-dragcontroller-springloadingcontext-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AnimationOptions](arkts-arkui-dragcontroller-animationoptions-i.md) |
| [DragAction](arkts-arkui-dragcontroller-dragaction-i.md) |
| [DragAndDropInfo](arkts-arkui-dragcontroller-draganddropinfo-i.md) |
| [DragEventParam](arkts-arkui-dragcontroller-drageventparam-i.md) |
| [DragInfo](arkts-arkui-dragcontroller-draginfo-i.md) |
| [DragSpringLoadingConfiguration](arkts-arkui-dragcontroller-dragspringloadingconfiguration-i.md) |
| [SpringLoadingDragInfos](arkts-arkui-dragcontroller-springloadingdraginfos-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DragSpringLoadingState](arkts-arkui-dragcontroller-dragspringloadingstate-e.md) |
| [DragStartRequestStatus](arkts-arkui-dragcontroller-dragstartrequeststatus-e.md) |
| [DragStatus](arkts-arkui-dragcontroller-dragstatus-e.md) |
