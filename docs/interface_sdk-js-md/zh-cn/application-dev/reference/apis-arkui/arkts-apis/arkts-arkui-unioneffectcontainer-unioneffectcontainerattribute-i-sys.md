# UnionEffectContainerAttribute（系统接口）

UnionEffectContainer属性，支持通用属性，支持宽高设置。

**继承/实现关系：** UnionEffectContainerAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface UnionEffectContainerAttribute extends CommonMethod--><!--Device-unnamed-export declare interface UnionEffectContainerAttribute extends CommonMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<UnionEffectContainerAttribute>
        | AttributeModifier<CommonMethod> | undefined): this
```

Sets the attribute modifier for UnionEffectContainer.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UnionEffectContainerAttribute-default attributeModifier(modifier: AttributeModifier<UnionEffectContainerAttribute>        | AttributeModifier<CommonMethod> | undefined): this--><!--Device-UnionEffectContainerAttribute-default attributeModifier(modifier: AttributeModifier<UnionEffectContainerAttribute>        | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;UnionEffectContainerAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## pointLight

```TypeScript
default pointLight(light: PointLightStyle): this
```

设置点光源样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UnionEffectContainerAttribute-default pointLight(light: PointLightStyle): this--><!--Device-UnionEffectContainerAttribute-default pointLight(light: PointLightStyle): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| light | [PointLightStyle](../arkts-components/arkts-arkui-pointlightstyle-i-sys.md) | 是 | 点光源样式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## setUnionEffectContainerOptions

```TypeScript
default setUnionEffectContainerOptions(options?: UnionEffectContainerOptions): this
```

Set UnionEffectContainer options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UnionEffectContainerAttribute-default setUnionEffectContainerOptions(options?: UnionEffectContainerOptions): this--><!--Device-UnionEffectContainerAttribute-default setUnionEffectContainerOptions(options?: UnionEffectContainerOptions): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [UnionEffectContainerOptions](arkts-arkui-unioneffectcontainer-unioneffectcontaineroptions-i-sys.md) | 否 | The options to create an UnionEffectContainer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns instance of UnionEffectContainerAttribute. |

## unionMode

```TypeScript
default unionMode(mode: UnionMode | undefined): this
```

设置融合效果模式。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UnionEffectContainerAttribute-default unionMode(mode: UnionMode | undefined): this--><!--Device-UnionEffectContainerAttribute-default unionMode(mode: UnionMode | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [UnionMode](../arkts-components/arkts-arkui-unionmode-e-sys.md) \| undefined | 是 | 融合效果模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

