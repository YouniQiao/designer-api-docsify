# Constants

## ArcList

```TypeScript
export declare const ArcList: ArcListInterface
```

The **ArcList** component is a circular layout container that displays a series of list items in an arc shape. It is suitable for presenting homogeneous data, such as images and text, in a continuous, multi-row format. &gt; **NOTE：**&gt; - This component is supported since API version 18. Updates will be marked with a &gt; superscript to indicate their earliest API version. &gt; &gt; - This component can be used on phones, PCs, 2-in-1 devices, tablets, TVs, and wearables. &gt; In API version 22 and earlier versions, a compilation warning will be reported when this &gt; component is used on phones, PCs, 2-in-1 devices, tablets, and TVs, but the component can &gt; still run properly.

### Child Components Only the ArcListItem component is supported.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-export declare const ArcList: ArcListInterface--><!--Device-unnamed-export declare const ArcList: ArcListInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## ArcListInstance

```TypeScript
export declare const ArcListInstance: ArcListAttribute
```

Defines ArcList Component instance.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-export declare const ArcListInstance: ArcListAttribute--><!--Device-unnamed-export declare const ArcListInstance: ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## ArcListItem

```TypeScript
export declare const ArcListItem: ArcListItemInterface
```

The **ArcListItem** component is used to display individual child components in an ArcList component and must be used in conjunction with **ArcList**. &gt; **NOTE：**&gt; - This component can be used only as a child of ArcList. &gt; &gt; - When this component is used with &gt; [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md), its child components are &gt; created when it is created. When this component is used with &gt; [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md) or &gt; [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md), or when the parent component is &gt; ArcList, its child components are created when it is laid out. &gt; &gt; - This component can be used on phones, PCs, 2-in-1 devices, tablets, TVs, and wearables. In API version 22 and &gt; earlier versions, a compilation warning will be reported when this component is used on phones, PCs, 2-in-1 devices &gt; , tablets, and TVs, but the component can still run properly.

### Child Components This component can contain a single child component.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-export declare const ArcListItem: ArcListItemInterface--><!--Device-unnamed-export declare const ArcListItem: ArcListItemInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## ArcListItemInstance

```TypeScript
export declare const ArcListItemInstance: ArcListItemAttribute
```

Defines ArcListItem Component instance.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-export declare const ArcListItemInstance: ArcListItemAttribute--><!--Device-unnamed-export declare const ArcListItemInstance: ArcListItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

