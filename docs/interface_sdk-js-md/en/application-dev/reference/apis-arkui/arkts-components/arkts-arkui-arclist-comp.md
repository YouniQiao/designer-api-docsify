# ArcList

The **ArcList** component is a circular layout container that displays a series of list items in an arc shape. It is suitable for presenting homogeneous data, such as images and text, in a continuous, multi-row format.

> **NOTE**

> - This component is supported since API version 18. Updates will be marked with a > superscript to indicate their earliest API version. > > - This component can be used on phones, PCs, 2-in-1 devices, tablets, TVs, and wearables. > In API version 22 and earlier versions, a compilation warning will be reported when this > component is used on phones, PCs, 2-in-1 devices, tablets, and TVs, but the component can > still run properly.

## Child Components

Only the [ArcListItem](#ohosarkuiarclist) component is supported.

## ArcList

```TypeScript
ArcList(options?: ArkListOptions)
```

Creates an **ArcList** component instance with specified configuration options.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ArkListOptions](arkts-arkui-arclist-comp-arklistoptions-i.md) | No |  |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [ArcListItemInterface](arkts-arkui-arclist-comp-arclistiteminterface-i.md) | The **ArcListItem** component is used to display individual child components in an [ArcList](#ohosarkuiarclist) component and must be used in conjunction with **ArcList**. |
| [ArkListOptions](arkts-arkui-arclist-comp-arklistoptions-i.md) | Provides basic parameters for creating an **ArcList** component. |

### Types

| Name | Description |
| --- | --- |
| [ArcScrollIndexHandler](arkts-arkui-arclist-comp-arcscrollindexhandler-t.md) | Represents the callback triggered when a child component enters or leaves the visible area of the **ArcList** component. |

## Examples

```TypeScript
This example demonstrates an ArcList component with a header component and auto-scaling child items.
```
