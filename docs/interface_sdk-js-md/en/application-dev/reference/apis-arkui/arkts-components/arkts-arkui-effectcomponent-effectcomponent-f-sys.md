# EffectComponent (System API)

## EffectComponent

```TypeScript
@ComponentBuilder
export declare function EffectComponent(
    options?: EffectComponentOptions,
    content_?: CustomBuilder,
): EffectComponentAttribute
```

Defines EffectComponent Component

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function EffectComponent(    options?: EffectComponentOptions,    content_?: CustomBuilder,): EffectComponentAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function EffectComponent(    options?: EffectComponentOptions,    content_?: CustomBuilder,): EffectComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [EffectComponentOptions](arkts-arkui-effectcomponent-effectcomponentoptions-i-sys.md) | No | The options to create an EffectComponent. |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No | Subcomponents of EffectComponent |

**Return value:**

| Type | Description |
| --- | --- |
| [EffectComponentAttribute](arkts-arkui-effectcomponent-attribute.md) |  |


## EffectComponent

```TypeScript
@Builder
export declare function EffectComponent(
    style_: CustomBuilderT<EffectComponentAttribute>,
    content_?: CustomBuilder,
): EffectComponentAttribute
```

Defines EffectComponent

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function EffectComponent(    style_: CustomBuilderT<EffectComponentAttribute>,    content_?: CustomBuilder,): EffectComponentAttribute--><!--Device-unnamed-@Builderexport declare function EffectComponent(    style_: CustomBuilderT<EffectComponentAttribute>,    content_?: CustomBuilder,): EffectComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;[EffectComponentAttribute](arkts-arkui-effectcomponent-attribute.md)&gt; | Yes | EffectComponent attribute instance |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [EffectComponentAttribute](arkts-arkui-effectcomponent-attribute.md) |  |

