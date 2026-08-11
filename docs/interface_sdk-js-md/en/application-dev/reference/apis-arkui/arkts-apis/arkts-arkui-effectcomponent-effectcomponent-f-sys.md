# EffectComponent (System API)

## EffectComponent

```TypeScript
export declare function EffectComponent(
    options?: EffectComponentOptions,
    content_?: CustomBuilder,
): EffectComponentAttribute
```

Defines EffectComponent Component

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function EffectComponent(    options?: EffectComponentOptions,    content_?: CustomBuilder,): EffectComponentAttribute--><!--Device-unnamed-export declare function EffectComponent(    options?: EffectComponentOptions,    content_?: CustomBuilder,): EffectComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [EffectComponentOptions](arkts-arkui-effectcomponent-effectcomponentoptions-i-sys.md) | No | The options to create an EffectComponent. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | Subcomponents of EffectComponent |

**Return value:**

| Type | Description |
| --- | --- |
| [EffectComponentAttribute](../arkts-components/arkts-arkui-effectcomponent-attribute.md) |  |


## EffectComponent

```TypeScript
export declare function EffectComponent(
    style_: CustomBuilderT<EffectComponentAttribute>,
    content_?: CustomBuilder,
): EffectComponentAttribute
```

Defines EffectComponent

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function EffectComponent(    style_: CustomBuilderT<EffectComponentAttribute>,    content_?: CustomBuilder,): EffectComponentAttribute--><!--Device-unnamed-export declare function EffectComponent(    style_: CustomBuilderT<EffectComponentAttribute>,    content_?: CustomBuilder,): EffectComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;EffectComponentAttribute&gt; | Yes | EffectComponent attribute instance |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [EffectComponentAttribute](../arkts-components/arkts-arkui-effectcomponent-attribute.md) |  |

