# Rating

## Rating

```TypeScript
@ComponentBuilder
export declare function Rating(
    options?: RatingOptions,
    content_?: CustomBuilder,
): RatingAttribute
```

Defines Rating Component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Rating(    options?: RatingOptions,    content_?: CustomBuilder,): RatingAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Rating(    options?: RatingOptions,    content_?: CustomBuilder,): RatingAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RatingOptions](arkts-rating-ratingoptions-i.md) | No | the options of Rating. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [RatingAttribute](arkts-rating-attribute.md) |  |


## Rating

```TypeScript
@Builder
export declare function Rating(
    style_: CustomBuilderT<RatingAttribute>,
    content_?: CustomBuilder,
): RatingAttribute
```

Defines Rating Component.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Rating(    style_: CustomBuilderT<RatingAttribute>,    content_?: CustomBuilder,): RatingAttribute--><!--Device-unnamed-@Builderexport declare function Rating(    style_: CustomBuilderT<RatingAttribute>,    content_?: CustomBuilder,): RatingAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[RatingAttribute](arkts-rating-attribute.md)&gt; | Yes | rating attribute instance |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [RatingAttribute](arkts-rating-attribute.md) |  |

