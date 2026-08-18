# CommonMethod

CommonMethod.

**起始版本：** 11

<!--Device-unnamed-declare class CommonMethod--><!--Device-unnamed-declare class CommonMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## advancedBlendMode

```TypeScript
advancedBlendMode(effect: BlendMode | Blender, type?: BlendApplyType): T
```

将当前组件的内容（包含子节点内容）与下方画布（可能为离屏画布）已有内容进行混合。不能与 [blendMode](arkts-arkui-commonmethod-c.md#blendmode)接口同时使用。

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从API版本13开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-advancedBlendMode(effect: BlendMode | Blender, type?: BlendApplyType): T--><!--Device-CommonMethod-advancedBlendMode(effect: BlendMode | Blender, type?: BlendApplyType): T-End-->

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| effect | [BlendMode](arkts-arkui-blendmode-e.md) \| [Blender](arkts-arkui-blender-t-sys.md) | 是 |
| type | [BlendApplyType](arkts-arkui-blendapplytype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## constructor

```TypeScript
constructor()
```

constructor.

**起始版本：** 9

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-constructor()--><!--Device-CommonMethod-constructor()-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## edgeLight

```TypeScript
edgeLight(params: EdgeLightParams | undefined): T
```

为组件添加边缘流光效果。边缘流光效果会在组件的边缘创建发光效果，从指定位置开始并沿边缘延伸，此效果可以增强组件的视觉吸引力并突出显示重要组件。 > **说明：** > > - 仅设置edgeLight不会产生边缘流光效果，需结合 > [animateTo](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#animateto)更改position参数达到流光效果。可参考 > [示例4（设置组件边缘流光效果）](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-image-effect-sys.md#示例4设置组件边缘流光效果)。 > > > - 当position参数以对角线方式变更时，边缘流光将沿倾斜角45°的方式运行。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CommonMethod-edgeLight(params: EdgeLightParams | undefined): T--><!--Device-CommonMethod-edgeLight(params: EdgeLightParams | undefined): T-End-->

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [EdgeLightParams](arkts-arkui-edgelightparams-i-sys.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## excludeFromRenderGroup

```TypeScript
excludeFromRenderGroup(exclude: boolean | undefined): T
```

设置当前组件和其子组件是否从祖先组件的节点组中剔除。需搭配祖先组件设置节点组[renderGroup](arkts-arkui-commonmethod-c.md#rendergroup)属性使 用，单独使用无效果。 从节点组剔除后，当前组件和子组件不再影响祖先组件的离屏画布，不会引起节点组的缓存失效，从而达到复用节点组缓存的目的。如果当前组件的显示区域只占节点组绘制内容显示区域的一部分，且当前组件及子组件的显示效果频繁更新，设置 excludeFromRenderGroup属性有助于绘制性能优化。 不设置该属性时，默认当前组件和其子组件不从祖先组件的节点组中剔除。 > **说明：** > > 设置excludeFromRenderGroup为true的组件及其子组件的绘制内容不能超过该组件本身的边界范围，否则会出现显示内容被裁剪的问题。例如当子组件通过 > [translate](arkts-arkui-commonmethod-c.md#translate)或 > [scale](arkts-arkui-commonmethod-c.md#scale)等属性导致子组件超出当前组件范围，或当前组件上有 > [shadow](arkts-arkui-commonmethod-c.md#shadow)、 > [pixelStretchEffect](arkts-arkui-commonmethod-c.md#pixelstretcheffect)等属性导致当前组件的绘制内容超出组件 > 边界时，可能出现显示内容被裁剪的问题。此类场景不应设置excludeFromRenderGroup属性为true。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CommonMethod-excludeFromRenderGroup(exclude: boolean | undefined): T--><!--Device-CommonMethod-excludeFromRenderGroup(exclude: boolean | undefined): T-End-->

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| exclude | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## spatialEffect

```TypeScript
spatialEffect(params: SpatialEffectParams | undefined): T
```

将空间效果应用于组件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-spatialEffect(params: SpatialEffectParams | undefined): T--><!--Device-CommonMethod-spatialEffect(params: SpatialEffectParams | undefined): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [SpatialEffectParams](arkts-arkui-spatialeffectparams-i-sys.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## useUnionEffect

```TypeScript
useUnionEffect(value: boolean | undefined): T
```

指定当前组件是否参与祖先组件UnionEffectContainer的融合效果

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CommonMethod-useUnionEffect(value: boolean | undefined): T--><!--Device-CommonMethod-useUnionEffect(value: boolean | undefined): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## useUnionEffect

```TypeScript
useUnionEffect(value: boolean | undefined, options?: GravityCenterOptions): T
```

指定当前组件是否参与祖先组件UnionEffectContainer的融合效果

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CommonMethod-useUnionEffect(value: boolean | undefined, options?: GravityCenterOptions): T--><!--Device-CommonMethod-useUnionEffect(value: boolean | undefined, options?: GravityCenterOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |
| options | [GravityCenterOptions](arkts-arkui-gravitycenteroptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |
