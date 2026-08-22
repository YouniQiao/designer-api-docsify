# ImageAnimator

## ImageAnimator

```TypeScript
@ComponentBuilder
export declare function ImageAnimator(): ImageAnimatorAttribute
```

Defines the ImageAnimator component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function ImageAnimator(): ImageAnimatorAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function ImageAnimator(): ImageAnimatorAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [ImageAnimatorAttribute](arkts-imageanimator-attribute.md) | The attribute of the ImageAnimator. |


## ImageAnimator

```TypeScript
@Builder
export declare function ImageAnimator(style: CustomBuilderT<ImageAnimatorAttribute>): ImageAnimatorAttribute
```

Defines the ImageAnimator component. It requires call setImageAnimatorOptions at start of the component attribute set-up. and it requires call applyAttributeFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function ImageAnimator(style: CustomBuilderT<ImageAnimatorAttribute>): ImageAnimatorAttribute--><!--Device-unnamed-@Builderexport declare function ImageAnimator(style: CustomBuilderT<ImageAnimatorAttribute>): ImageAnimatorAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[ImageAnimatorAttribute](arkts-imageanimator-attribute.md)&gt; | Yes | the callback to set up component's attribute. |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageAnimatorAttribute](arkts-imageanimator-attribute.md) | The attribute of the ImageAnimator. |

