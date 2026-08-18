# CommonMethod

CommonMethod.

**Since:** 11

<!--Device-unnamed-declare class CommonMethod--><!--Device-unnamed-declare class CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## advancedBlendMode

```TypeScript
advancedBlendMode(effect: BlendMode | Blender, type?: BlendApplyType): T
```

Defines how the component's content (including the content of it child components) is blended with the existing content on the canvas (possibly offscreen canvas) below. This API cannot be used with [blendMode](arkts-arkui-commonmethod-c.md#blendmode).

**Since:** 13

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 13.

<!--Device-CommonMethod-advancedBlendMode(effect: BlendMode | Blender, type?: BlendApplyType): T--><!--Device-CommonMethod-advancedBlendMode(effect: BlendMode | Blender, type?: BlendApplyType): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| effect | [BlendMode](arkts-arkui-blendmode-e.md) \| [Blender](arkts-arkui-blender-t-sys.md) | Yes |
| type | [BlendApplyType](arkts-arkui-blendapplytype-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## constructor

```TypeScript
constructor()
```

constructor.

**Since:** 9

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-constructor()--><!--Device-CommonMethod-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## edgeLight

```TypeScript
edgeLight(params: EdgeLightParams | undefined): T
```

Sets the edge light effect for the component. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The edge light effect creates a glowing light effect along the component's edges, starting from the specified position and extending along the edge. <br>This effect can enhance the visual appeal and highlight important components. &lt;/p&gt;

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-edgeLight(params: EdgeLightParams | undefined): T--><!--Device-CommonMethod-edgeLight(params: EdgeLightParams | undefined): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| params | [EdgeLightParams](arkts-arkui-edgelightparams-i-sys.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## excludeFromRenderGroup

```TypeScript
excludeFromRenderGroup(exclude: boolean | undefined): T
```

Sets whether the current component and its child components are removed from the render group of the ancestor component. If this attribute is used alone, no effect is achieved. It must be used with the [renderGroup](arkts-arkui-commonmethod-c.md#rendergroup) attribute of the ancestor component. Removing the current component and its children from the render group does not affect the offscreen canvas of the ancestor component, and the cache of the render group is still valid. In this way, the render group cache can be reused. If the display area of the current component occupies only a part of the display area of the render group drawing content, and the display effect of the current component and its children is frequently updated, setting **excludeFromRenderGroup** helps optimize the drawing performance. If this attribute is not set, the current component and its children are not removed from the render group of the ancestor component by default. > **NOTE：**> > The drawing content of the component with **excludeFromRenderGroup** set to **true** and its children cannot the > component's own boundary range. Otherwise, the displayed content may be clipped. For example, if the child > component exceeds the boundary range of the current component due to attributes such as > [translate](arkts-arkui-commonmethod-c.md#translate) or > [scale](arkts-arkui-commonmethod-c.md#scale), or the drawing content extend beyond its boundaries > because the current component has attributes such as > [shadow](arkts-arkui-commonmethod-c.md#shadow) and > [pixelStretchEffect](arkts-arkui-commonmethod-c.md#pixelstretcheffect), the displayed > content may be clipped. In such scenarios, **excludeFromRenderGroup** should not be set to **true**.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-excludeFromRenderGroup(exclude: boolean | undefined): T--><!--Device-CommonMethod-excludeFromRenderGroup(exclude: boolean | undefined): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| exclude | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## spatialEffect

```TypeScript
spatialEffect(params: SpatialEffectParams | undefined): T
```

Applies a spatial effect to component.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CommonMethod-spatialEffect(params: SpatialEffectParams | undefined): T--><!--Device-CommonMethod-spatialEffect(params: SpatialEffectParams | undefined): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| params | [SpatialEffectParams](arkts-arkui-spatialeffectparams-i-sys.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## systemMaterial

```TypeScript
systemMaterial(material: SystemUiMaterial | undefined): T
```

Sets the system material for a component. Different system materials have different attribute effects. This API affects the background color ([backgroundColor](arkts-arkui-commonmethod-c.md#backgroundcolor)), border color ([borderColor](arkts-arkui-commonmethod-c.md#bordercolor)), border width ([borderWidth](arkts-arkui-commonmethod-c.md#borderwidth) ), and shadow ([shadow](arkts-arkui-commonmethod-c.md#shadow)). You are advised not to use this API together with the aforementioned APIs. For details about the example, see [Setting the System Material](../../../reference/apis-arkui/arkts-apis-uimaterial-sys.md#example-1-setting-the-system-material).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-CommonMethod-systemMaterial(material: SystemUiMaterial | undefined): T--><!--Device-CommonMethod-systemMaterial(material: SystemUiMaterial | undefined): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| material | [SystemUiMaterial](arkts-arkui-systemuimaterial-t-sys.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## useUnionEffect

```TypeScript
useUnionEffect(value: boolean | undefined): T
```

Specify whether the current component participates in the fusion effect of the ancestor component UnionEffectContainer

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-useUnionEffect(value: boolean | undefined): T--><!--Device-CommonMethod-useUnionEffect(value: boolean | undefined): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## useUnionEffect

```TypeScript
useUnionEffect(value: boolean | undefined, options?: GravityCenterOptions): T
```

Specify whether the current component participates in the fusion effect of the ancestor component UnionEffectContainer

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-useUnionEffect(value: boolean | undefined, options?: GravityCenterOptions): T--><!--Device-CommonMethod-useUnionEffect(value: boolean | undefined, options?: GravityCenterOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean \| undefined | Yes |
| options | [GravityCenterOptions](arkts-arkui-gravitycenteroptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |
