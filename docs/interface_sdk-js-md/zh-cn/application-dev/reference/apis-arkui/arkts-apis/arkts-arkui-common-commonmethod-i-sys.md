# CommonMethod

CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface CommonMethod--><!--Device-unnamed-export declare interface CommonMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## advancedBlendMode

```TypeScript
default advancedBlendMode(effect: BlendMode | Blender | undefined, type?: BlendApplyType): this
```

Add a blendMode effect to the current component.Cannot be used together with the blendMode interface.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CommonMethod-default advancedBlendMode(effect: BlendMode | Blender | undefined, type?: BlendApplyType): this--><!--Device-CommonMethod-default advancedBlendMode(effect: BlendMode | Blender | undefined, type?: BlendApplyType): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| effect | [BlendMode](arkts-arkui-common-blendmode-e.md) \| [Blender](arkts-arkui-blender-t-sys.md) \| undefined | 是 | When the effect type is BlendMode type, define Different hybrid modes. |
| type | [BlendApplyType](arkts-arkui-common-blendapplytype-e.md) | 否 | Different blend apply type Default value: BlendApplyType.FAST. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## edgeLight

```TypeScript
default edgeLight(params: EdgeLightParams | undefined): this
```

Sets the edge light effect for the component.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;The edge light effect creates a glowing light effect along the component's edges,starting from the specified position and extending along the edge.&lt;br&gt;This effect can enhance the visual appeal and highlight important components.&lt;/p&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CommonMethod-default edgeLight(params: EdgeLightParams | undefined): this--><!--Device-CommonMethod-default edgeLight(params: EdgeLightParams | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [EdgeLightParams](arkts-arkui-common-edgelightparams-i-sys.md) \| undefined | 是 | Edge light effect parameters. Defines the position, length, intensity, color, and thickness of the light effect. If params is undefined, the edge light effect is removed. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## excludeFromRenderGroup

```TypeScript
default excludeFromRenderGroup(exclude: boolean | undefined): this
```

Set the component and its child components not to render off the screen following the parent component.Must be used in conjunction with renderGroup.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CommonMethod-default excludeFromRenderGroup(exclude: boolean | undefined): this--><!--Device-CommonMethod-default excludeFromRenderGroup(exclude: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| exclude | boolean \| undefined | 是 | Whether the component and its child components are not rendered off the screen following the parent component. True means to not follow the parent component. Default value: false. Undefined means to default value. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## spatialEffect

```TypeScript
default spatialEffect(params: SpatialEffectParams | undefined): this
```

Applies a spatial effect to component.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CommonMethod-default spatialEffect(params: SpatialEffectParams | undefined): this--><!--Device-CommonMethod-default spatialEffect(params: SpatialEffectParams | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [SpatialEffectParams](arkts-arkui-common-spatialeffectparams-i-sys.md) \| undefined | 是 | Spatial effect parameters. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## useUnionEffect

```TypeScript
default useUnionEffect(value: boolean | undefined): this
```

Specify whether the current component participates in the fusion effect of the ancestor component UnionEffectContainer

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CommonMethod-default useUnionEffect(value: boolean | undefined): this--><!--Device-CommonMethod-default useUnionEffect(value: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 | Whether the component participates in the fusion effect of the ancestor component **UnionEffectContainer**.&lt;br&gt;The value **true** means that the component participates in the fusion effect of the ancestor component **UnionEffectContainer**, and **false** means the opposite. &lt;br&gt;Default value: **false**. Undefined means to default value. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | return the component attribute. |

## useUnionEffect

```TypeScript
default useUnionEffect(value: boolean | undefined, options?: GravityCenterOptions): this
```

Specify whether the current component participates in the fusion effect of the ancestor component UnionEffectContainer

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CommonMethod-default useUnionEffect(value: boolean | undefined, options?: GravityCenterOptions): this--><!--Device-CommonMethod-default useUnionEffect(value: boolean | undefined, options?: GravityCenterOptions): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 | Whether the component participates in the fusion effect of the ancestor component **UnionEffectContainer**.&lt;br&gt;The value **true** means that the component participates in the fusion effect of the ancestor component **UnionEffectContainer**, and **false** means the opposite. &lt;br&gt;Default value: **false**. Undefined means to default value. |
| options | [GravityCenterOptions](arkts-arkui-common-gravitycenteroptions-i-sys.md) | 否 | Gravitational center parameter. This parameter must be used together with UnionMode.GRAVITY_UNION. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | return the component attribute. |

