# ImageAnimator

## ImageAnimator

```TypeScript
export declare function ImageAnimator(): ImageAnimatorAttribute
```

Defines the ImageAnimator component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ImageAnimator(): ImageAnimatorAttribute--><!--Device-unnamed-export declare function ImageAnimator(): ImageAnimatorAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [ImageAnimatorAttribute](../arkts-components/arkts-arkui-imageanimator-attribute.md) | The attribute of the ImageAnimator. |


## ImageAnimator

```TypeScript
export declare function ImageAnimator(style: CustomBuilderT<ImageAnimatorAttribute>): ImageAnimatorAttribute
```

Defines the ImageAnimator component. It requires call setImageAnimatorOptions at start of the component attribute set-up. and it requires call applyAttributeFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ImageAnimator(style: CustomBuilderT<ImageAnimatorAttribute>): ImageAnimatorAttribute--><!--Device-unnamed-export declare function ImageAnimator(style: CustomBuilderT<ImageAnimatorAttribute>): ImageAnimatorAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;ImageAnimatorAttribute&gt; | Yes | the callback to set up component's attribute. |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageAnimatorAttribute](../arkts-components/arkts-arkui-imageanimator-attribute.md) | The attribute of the ImageAnimator. |

