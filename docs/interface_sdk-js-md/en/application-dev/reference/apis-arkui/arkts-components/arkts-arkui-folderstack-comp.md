# FolderStack

**FolderStack** extends the Stack container, adding the <!--RP1-->foldable screen hover<!--RP1End--> capability. By setting child component IDs in the **upperItems** array of the [FolderStackOptions](arkts-arkui-folderstackoptions-i.md) configuration, the corresponding child components automatically avoid the fold crease area and move to the upper screen. **FolderStack** is designed for the hover status scenario of dual- fold devices, such as video playback and video conferencing apps, where the video image automatically moves to the upper screen while the control panel remains on the lower screen. This component addresses the adaptation challenges of dual-fold devices, delivering benefits such as improved user experience and simplified layout adaptation for developers.

> **NOTE** > > - The hover capability of this component is designed for <!--RP2-->dual-fold<!--RP2End--> devices and takes effect > only on dual-fold devices. You can use FoldStatus to determine the fold status of the device. > > - When the parent component of this component is an > [if/else: conditional rendering](../../../ui/rendering-control/arkts-rendering-control-ifelse.md) node, the > foldable screen hover capability becomes invalid.

## Child Components

Multiple child components are supported.

## FolderStack

```TypeScript
FolderStack(options?: FolderStackOptions)
```

A foldable screen hover layout container that extends Stack. It implements the foldable screen hover capability through the **upperItems** configuration. When the device is in hover status, the specified child components automatically move to the upper screen, while other components are stacked on the lower screen.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FolderStackOptions](arkts-arkui-folderstackoptions-i.md) | No | Configuration options of **FolderStack**, used to set the child components that need to be moved to the upper half screen in hover status. When the foldable screen hover capability is needed, specify child component IDs through the **upperItems** array. If not passed, **FolderStack** is used as a regular **Stack** component without the hover capability enabled, and **upperItems** defaults to an empty array. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [FolderStackOptions](arkts-arkui-folderstackoptions-i.md) | Configuration object for the **FolderStack** hover status, which describes the information about child components that need to be moved to the upper screen in hover status. |
| [HoverEventParam](arkts-arkui-hovereventparam-i.md) |  |
| [OnFoldStatusChangeInfo](arkts-arkui-onfoldstatuschangeinfo-i.md) | Defines the information about the fold status change, which takes effect only in landscape mode. |

### Types

| Name | Description |
| --- | --- |
| [OnFoldStatusChangeCallback](arkts-arkui-onfoldstatuschangecallback-t.md) | Triggered when the fold status changes&lt;!--RP4--&gt;, which takes effect only in landscape mode&lt;!--RP4End--&gt;. |
| [OnHoverStatusChangeCallback](arkts-arkui-onhoverstatuschangecallback-t.md) | Defines the current callback invoked when the hover state of the device changes. |
| [WindowStatusType](arkts-arkui-windowstatustype-t.md) | Enumerates the window modes. |

## Examples

```TypeScript
### Example 1: Implementing the Foldable Device Hover Capability with FolderStack

This example implements the foldable device hover capability.

Figure 1 Expanded state in landscape modeFigure 2 Half-fold state in landscape mode
```

```TypeScript
### Example 2: Dynamically Setting Attributes and Methods of the FolderStack Component Using attributeModifier

This example demonstrates how to dynamically set the onFolderStateChange and onHoverStatusChange methods of the FolderStack component using attributeModifier.
```
