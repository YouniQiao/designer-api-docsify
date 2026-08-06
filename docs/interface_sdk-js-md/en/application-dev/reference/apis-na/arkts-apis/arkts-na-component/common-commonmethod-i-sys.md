# CommonMethod

CommonMethod

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface CommonMethod--><!--Device-unnamed-export declare interface CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## advancedBlendMode

```TypeScript
default advancedBlendMode(effect: BlendMode | Blender | undefined, type?: BlendApplyType): this
```

Add a blendMode effect to the current component.Cannot be used together with the blendMode interface.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default advancedBlendMode(effect: BlendMode | Blender | undefined, type?: BlendApplyType): this--><!--Device-CommonMethod-default advancedBlendMode(effect: BlendMode | Blender | undefined, type?: BlendApplyType): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| effect | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| Blender \| undefined | Yes | When the effect type is BlendMode type, define Different hybrid modes. |
| type | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Different blend apply type Default value: BlendApplyType.FAST. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## edgeLight

```TypeScript
default edgeLight(params: EdgeLightParams | undefined): this
```

Sets the edge light effect for the component. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_: \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_The edge light effect creates a glowing light effect along the component's edges, starting from the specified position and extending along the edge. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_This effect can enhance the visual appeal and highlight important components. \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default edgeLight(params: EdgeLightParams | undefined): this--><!--Device-CommonMethod-default edgeLight(params: EdgeLightParams | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | Edge light effect parameters.Defines the position, length, intensity, color, and thickness of the light effect.If params is undefined, the edge light effect is removed. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## excludeFromRenderGroup

```TypeScript
default excludeFromRenderGroup(exclude: boolean | undefined): this
```

Set the component and its child components not to render off the screen following the parent component. Must be used in conjunction with renderGroup.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default excludeFromRenderGroup(exclude: boolean | undefined): this--><!--Device-CommonMethod-default excludeFromRenderGroup(exclude: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| exclude | boolean \| undefined | Yes | Whether the component and its child components are not rendered off the screen following the parent component.True means to not follow the parent component.Default value: false.Undefined means to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## spatialEffect

```TypeScript
default spatialEffect(params: SpatialEffectParams | undefined): this
```

Applies a spatial effect to component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default spatialEffect(params: SpatialEffectParams | undefined): this--><!--Device-CommonMethod-default spatialEffect(params: SpatialEffectParams | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | Spatial effect parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## useUnionEffect

```TypeScript
default useUnionEffect(value: boolean | undefined): this
```

Specify whether the current component participates in the fusion effect of the ancestor component UnionEffectContainer

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default useUnionEffect(value: boolean | undefined): this--><!--Device-CommonMethod-default useUnionEffect(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | Whether the component participates in the fusion effect of the ancestor component **UnionEffectContainer**.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value **true** means that the component participates in the fusion effect of the ancestor component **UnionEffectContainer**, and **false** means the opposite.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_Default value: **false**. Undefined means to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| this | return the component attribute. |

## useUnionEffect

```TypeScript
default useUnionEffect(value: boolean | undefined, options?: GravityCenterOptions): this
```

Specify whether the current component participates in the fusion effect of the ancestor component UnionEffectContainer

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default useUnionEffect(value: boolean | undefined, options?: GravityCenterOptions): this--><!--Device-CommonMethod-default useUnionEffect(value: boolean | undefined, options?: GravityCenterOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | Whether the component participates in the fusion effect of the ancestor component **UnionEffectContainer**.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value **true** means that the component participates in the fusion effect of the ancestor component **UnionEffectContainer**, and **false** means the opposite.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_Default value: **false**. Undefined means to default value. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Gravitational center parameter.This parameter must be used together with UnionMode.GRAVITY\_\_\_ESCAPED\_UNDERSCORE\_\_\_UNION. |

**Return value:**

| Type | Description |
| --- | --- |
| this | return the component attribute. |

