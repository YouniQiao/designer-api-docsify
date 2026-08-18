# SingleLineConfig

Represents the single-line display mode. In single-line mode, the component does not provide functions for viewing a larger image. The component does not support callbacks related to large images, and the PickerController does not support APIs related to large images, making API calls ineffective.

**Since:** 20

<!--Device-unnamed-export declare class SingleLineConfig--><!--Device-unnamed-export declare class SingleLineConfig-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
```

## itemBorderRadius

```TypeScript
itemBorderRadius?: Length | BorderRadiuses | LocalizedBorderRadiuses
```

Rounded corner radius for grid items.

**Type:** [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| BorderRadiuses \| [LocalizedBorderRadiuses](../../apis-arkui/arkts-apis/arkts-arkui-localizedborderradiuses-i.md)

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SingleLineConfig-itemBorderRadius?: Length | BorderRadiuses | LocalizedBorderRadiuses--><!--Device-SingleLineConfig-itemBorderRadius?: Length | BorderRadiuses | LocalizedBorderRadiuses-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## itemDisplayRatio

```TypeScript
itemDisplayRatio?: ItemDisplayRatio
```

Aspect ratio for grid display. Both 1:1 and the original image aspect ratio are supported. The default value is 1: 1.

**Type:** [ItemDisplayRatio](arkts-medialibrary-file-photopickercomponent-itemdisplayratio-e.md)

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SingleLineConfig-itemDisplayRatio?: ItemDisplayRatio--><!--Device-SingleLineConfig-itemDisplayRatio?: ItemDisplayRatio-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## itemGap

```TypeScript
itemGap?: Length
```

Spacing between grid items.

**Type:** [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md)

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SingleLineConfig-itemGap?: Length--><!--Device-SingleLineConfig-itemGap?: Length-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core
