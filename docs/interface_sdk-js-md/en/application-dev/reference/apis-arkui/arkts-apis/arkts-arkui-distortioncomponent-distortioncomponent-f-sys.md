# DistortionComponent (System API)

## DistortionComponent

```TypeScript
export declare function DistortionComponent(
    options?: DistortionComponentOptions,
    content_?:CustomBuilder,
): DistortionComponentAttribute
```

Defines a DistortionComponent that provides spatial distortion visual effects.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function DistortionComponent(    options?: DistortionComponentOptions,    content_?:CustomBuilder,): DistortionComponentAttribute--><!--Device-unnamed-export declare function DistortionComponent(    options?: DistortionComponentOptions,    content_?:CustomBuilder,): DistortionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DistortionComponentOptions](arkts-arkui-distortioncomponent-distortioncomponentoptions-i-sys.md) | No | DistortionComponent Options. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No | Subcomponents of DistortionComponent. |

**Return value:**

| Type | Description |
| --- | --- |
| [DistortionComponentAttribute](arkts-arkui-distortioncomponent-distortioncomponentattribute-i-sys.md) |  |


## DistortionComponent

```TypeScript
export declare function DistortionComponent(
    style_: CustomBuilderT<DistortionComponentAttribute>,
    content_?:CustomBuilder,
): DistortionComponentAttribute
```

Defines a DistortionComponent that provides spatial distortion visual effects.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function DistortionComponent(    style_: CustomBuilderT<DistortionComponentAttribute>,    content_?:CustomBuilder,): DistortionComponentAttribute--><!--Device-unnamed-export declare function DistortionComponent(    style_: CustomBuilderT<DistortionComponentAttribute>,    content_?:CustomBuilder,): DistortionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[DistortionComponentAttribute](arkts-arkui-distortioncomponent-distortioncomponentattribute-i-sys.md)&gt; | Yes | DistortionComponent attribute instance. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No | container. |

**Return value:**

| Type | Description |
| --- | --- |
| [DistortionComponentAttribute](arkts-arkui-distortioncomponent-distortioncomponentattribute-i-sys.md) |  |

