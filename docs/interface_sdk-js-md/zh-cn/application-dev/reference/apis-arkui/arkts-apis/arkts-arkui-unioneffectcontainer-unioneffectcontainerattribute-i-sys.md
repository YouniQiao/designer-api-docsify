# UnionEffectContainerAttribute（系统接口）

UnionEffectContainer属性，支持通用属性，支持宽高设置。

**继承/实现关系：** UnionEffectContainerAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<UnionEffectContainerAttribute>
        | AttributeModifier<CommonMethod> | undefined): this
```

Sets the attribute modifier for UnionEffectContainer.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[UnionEffectContainerAttribute](arkts-arkui-unioneffectcontainer-unioneffectcontainerattribute-i-sys.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## pointLight

```TypeScript
default pointLight(light: PointLightStyle): this
```

设置点光源样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| light | [PointLightStyle](../arkts-components/arkts-arkui-pointlightstyle-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## setUnionEffectContainerOptions

```TypeScript
default setUnionEffectContainerOptions(options?: UnionEffectContainerOptions): this
```

Set UnionEffectContainer options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [UnionEffectContainerOptions](arkts-arkui-unioneffectcontainer-unioneffectcontaineroptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [UnionEffectContainerAttribute](arkts-arkui-unioneffectcontainer-unioneffectcontainerattribute-i-sys.md) |

## unionMode

```TypeScript
default unionMode(mode: UnionMode | undefined): this
```

设置融合效果模式。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [UnionMode](arkts-arkui-unioneffectcontainer-unionmode-e-sys.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |
