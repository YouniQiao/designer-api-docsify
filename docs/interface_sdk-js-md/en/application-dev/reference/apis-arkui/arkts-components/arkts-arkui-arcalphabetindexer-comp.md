# ArcAlphabetIndexer

The **ArcAlphabetIndexer** component is an arc-shaped component designed for quick navigation through alphabetically sorted items. It can be integrated with container components to quickly locate items within the visible area.

> **NOTE**

> - This component can be used on phones, PCs, 2-in-1 devices, tablets, TVs, and wearables. In API version 22 and > earlier versions, a compilation warning will be reported when this component is used on phones, PCs, 2-in-1 > devices, tablets, and TVs, but the component can still run properly.

## Child Components

Not supported

## ArcAlphabetIndexer

```TypeScript
ArcAlphabetIndexer(info: ArcAlphabetIndexerInitInfo)
```

Creates an instance of the **ArcAlphabetIndexer** component with initialization parameters.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [ArcAlphabetIndexerInitInfo](arkts-arkui-arcalphabetindexer-comp-arcalphabetindexerinitinfo-i.md) | Yes | Initialization parameters for the **ArcAlphabetIndexer** component. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [ArcAlphabetIndexerInitInfo](arkts-arkui-arcalphabetindexer-comp-arcalphabetindexerinitinfo-i.md) | Initialization parameters for the **ArcAlphabetIndexer** component. |

### Types

| Name | Description |
| --- | --- |
| [OnSelectCallback](arkts-arkui-arcalphabetindexer-comp-onselectcallback-t.md) | Defines the callback used in [onSelect](arkts-arkui-arcalphabetindexer-comp-attribute.md#onselect). |

## Examples

```TypeScript
### Example 1: Setting Linked Control and Positioning

This example demonstrates how to link an ArcAlphabetIndexer component with an ArcList component for synchronized control and navigation.


```

```TypeScript
### Example 2: Setting Popup Display

This example uses the [popupColor](#popupcolor) and [popupBackground](#popupbackground) APIs to set the display background color and text color of the pop-up window.

Since API version 18, the popupColor and popupBackground APIs are supported.
```
