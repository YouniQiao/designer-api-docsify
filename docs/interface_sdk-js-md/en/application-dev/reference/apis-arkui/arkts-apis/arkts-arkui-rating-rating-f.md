# Rating

## Rating

```TypeScript
export declare function Rating(
    options?: RatingOptions,
    content_?: CustomBuilder,
): RatingAttribute
```

Defines Rating Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Rating(    options?: RatingOptions,    content_?: CustomBuilder,): RatingAttribute--><!--Device-unnamed-export declare function Rating(    options?: RatingOptions,    content_?: CustomBuilder,): RatingAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RatingOptions](arkts-arkui-rating-ratingoptions-i.md) | No | the options of Rating. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [RatingAttribute](arkts-arkui-rating-ratingattribute-i.md) |  |


## Rating

```TypeScript
export declare function Rating(
    style_: CustomBuilderT<RatingAttribute>,
    content_?: CustomBuilder,
): RatingAttribute
```

Defines Rating Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Rating(    style_: CustomBuilderT<RatingAttribute>,    content_?: CustomBuilder,): RatingAttribute--><!--Device-unnamed-export declare function Rating(    style_: CustomBuilderT<RatingAttribute>,    content_?: CustomBuilder,): RatingAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[RatingAttribute](arkts-arkui-rating-ratingattribute-i.md)&gt; | Yes | rating attribute instance |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [RatingAttribute](arkts-arkui-rating-ratingattribute-i.md) |  |

