# DistortionComponent (System API)

## DistortionComponent

```TypeScript
@ComponentBuilder
export declare function DistortionComponent(
    options?: DistortionComponentOptions,
    content_?:CustomBuilder,
): DistortionComponentAttribute
```

Defines a DistortionComponent that provides spatial distortion visual effects.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function DistortionComponent(    options?: DistortionComponentOptions,    content_?:CustomBuilder,): DistortionComponentAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function DistortionComponent(    options?: DistortionComponentOptions,    content_?:CustomBuilder,): DistortionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DistortionComponentOptions](arkts-na-distortioncomponent-distortioncomponentoptions-i-sys.md) | No | DistortionComponent Options. |
| content_ | CustomBuilder | No | Subcomponents of DistortionComponent. |

**Return value:**

| Type | Description |
| --- | --- |
| [DistortionComponentAttribute](arkts-na-distortioncomponent-distortioncomponentattribute-i.md) |  |


## DistortionComponent

```TypeScript
@Builder
export declare function DistortionComponent(
    style_: CustomBuilderT<DistortionComponentAttribute>,
    content_?:CustomBuilder,
): DistortionComponentAttribute
```

Defines a DistortionComponent that provides spatial distortion visual effects.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function DistortionComponent(    style_: CustomBuilderT<DistortionComponentAttribute>,    content_?:CustomBuilder,): DistortionComponentAttribute--><!--Device-unnamed-@Builderexport declare function DistortionComponent(    style_: CustomBuilderT<DistortionComponentAttribute>,    content_?:CustomBuilder,): DistortionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;[DistortionComponentAttribute](arkts-na-distortioncomponent-distortioncomponentattribute-i.md)&gt; | Yes | DistortionComponent attribute instance. |
| content_ | CustomBuilder | No | container. |

**Return value:**

| Type | Description |
| --- | --- |
| [DistortionComponentAttribute](arkts-na-distortioncomponent-distortioncomponentattribute-i.md) |  |

