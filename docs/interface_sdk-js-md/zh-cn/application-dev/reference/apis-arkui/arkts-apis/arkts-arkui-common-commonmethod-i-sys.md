# CommonMethod

CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## advancedBlendMode

```TypeScript
default advancedBlendMode(effect: BlendMode | Blender | undefined, type?: BlendApplyType): this
```

Add a blendMode effect to the current component.Cannot be used together with the blendMode interface.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| effect | [BlendMode](arkts-arkui-common-blendmode-e.md) \| [Blender](arkts-arkui-blender-t-sys.md) \| undefined | 是 |
| type | [BlendApplyType](arkts-arkui-common-blendapplytype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## edgeLight

```TypeScript
default edgeLight(params: EdgeLightParams | undefined): this
```

Sets the edge light effect for the component.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The edge light effect creates a glowing light effect along the component's edges, starting from the specified position and extending along the edge. <br>This effect can enhance the visual appeal and highlight important components. </p>

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [EdgeLightParams](arkts-arkui-common-edgelightparams-i-sys.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## excludeFromRenderGroup

```TypeScript
default excludeFromRenderGroup(exclude: boolean | undefined): this
```

Set the component and its child components not to render off the screen following the parent component. Must be used in conjunction with renderGroup.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| exclude | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## spatialEffect

```TypeScript
default spatialEffect(params: SpatialEffectParams | undefined): this
```

Applies a spatial effect to component.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [SpatialEffectParams](arkts-arkui-common-spatialeffectparams-i-sys.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## useUnionEffect

```TypeScript
default useUnionEffect(value: boolean | undefined): this
```

Specify whether the current component participates in the fusion effect of the ancestor component UnionEffectContainer

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## useUnionEffect

```TypeScript
default useUnionEffect(value: boolean | undefined, options?: GravityCenterOptions): this
```

Specify whether the current component participates in the fusion effect of the ancestor component UnionEffectContainer

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |
| options | [GravityCenterOptions](arkts-arkui-common-gravitycenteroptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |
