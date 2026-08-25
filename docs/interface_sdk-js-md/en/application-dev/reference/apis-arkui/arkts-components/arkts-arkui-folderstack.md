# FolderStack

**FolderStack** extends the Stack container, adding the <!--RP1-->foldable phone hover<!--RP1End--> capability. Child components specified in the **upperItems** array of [FolderStackOptions](arkts-arkui-folderstackoptions-i.md) automatically avoid the screen crease area and reposition to the upper display.> **NOTE**>> The hover capability is designed for and only works on <!--RP2-->dual-fold devices<!--RP2End-->.>> When the component's parent is an> [if/else conditional render](../../../ui/rendering-control/arkts-rendering-control-ifelse.md) node, the foldable> hover feature is disabled.>> **Child Components**>> Multiple child components are supported.

## FolderStack

```TypeScript
FolderStack(options?: FolderStackOptions)
```

Defines the constructor of FolderStack component.

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FolderStackOptions](arkts-arkui-folderstackoptions-i.md) | No |

## Summary

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [OnFoldStatusChangeCallback](arkts-arkui-onfoldstatuschangecallback-t.md) |
| [OnHoverStatusChangeCallback](arkts-arkui-onhoverstatuschangecallback-t.md) |
| [WindowStatusType](arkts-arkui-windowstatustype-t.md) |
