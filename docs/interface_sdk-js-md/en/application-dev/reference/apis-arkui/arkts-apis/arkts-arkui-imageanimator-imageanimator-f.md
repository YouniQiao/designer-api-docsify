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

定义ImageAnimator组件。它需要在组件开始时调用setImageAnimatorOptions属性设置。并且它需要在组件属性设置结束时调用applyAttributeFinish。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ImageAnimator(style: CustomBuilderT<ImageAnimatorAttribute>): ImageAnimatorAttribute--><!--Device-unnamed-export declare function ImageAnimator(style: CustomBuilderT<ImageAnimatorAttribute>): ImageAnimatorAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;ImageAnimatorAttribute&gt; | Yes | 设置组件属性的回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageAnimatorAttribute](../arkts-components/arkts-arkui-imageanimator-attribute.md) | ImageAnimator的属性。 |

