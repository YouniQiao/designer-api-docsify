# ArcListInterface

The **ArcList** component is a circular layout container that displays a series of list items in an arc shape. It is suitable for presenting homogeneous data, such as images and text, in a continuous, multi-row format.

**Since:** 18

<!--Device-unnamed-export interface ArcListInterface--><!--Device-unnamed-export interface ArcListInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcList, ArcListItem, ArcListAttribute, ArcListItemAttribute } from '@kit.ArkUI';
```

## constructor

```TypeScript
(options?: ArkListOptions): ArcListAttribute
```

Creates an **ArcList** component instance with specified configuration options.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcListInterface-(options?: ArkListOptions): ArcListAttribute--><!--Device-ArcListInterface-(options?: ArkListOptions): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ArkListOptions](arkts-arkui-arkuiarclist-arklistoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcListAttribute](arkts-arkui-arkuiarclist-arclistattribute-c.md) |  |

