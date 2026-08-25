# ParticleAttribute

除支持通用属性外还支持以下属性：

**继承/实现关系：** ParticleAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<ParticleAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Add particle attribute modifier.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ParticleAttribute](arkts-arkui-particle-particleattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ParticleAttribute](arkts-arkui-particle-particleattribute-i.md) |

## disturbanceFields

```TypeScript
default disturbanceFields(fields: Array<DisturbanceFieldOptions> | undefined): this
```

设置扰动场。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [fields](../../apis-arkdata/arkts-apis/arkts-arkdata-cloudextension-table-i-sys.md) | Array&lt;[DisturbanceFieldOptions](arkts-arkui-particle-disturbancefieldoptions-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ParticleAttribute](arkts-arkui-particle-particleattribute-i.md) |

## emitter

```TypeScript
default emitter(value: Array<EmitterProperty> | undefined): this
```

支持发射器位置动态更新。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;[EmitterProperty](arkts-arkui-particle-emitterproperty-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ParticleAttribute](arkts-arkui-particle-particleattribute-i.md) |

## rippleFields

```TypeScript
default rippleFields(fields: Array<RippleFieldOptions> | undefined): this
```

设置粒子波动场。波动场会对影响范围内的粒子施加按波形变化的力，产生类似波纹扩散的效果。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [fields](../../apis-arkdata/arkts-apis/arkts-arkdata-cloudextension-table-i-sys.md) | Array&lt;[RippleFieldOptions](arkts-arkui-particle-ripplefieldoptions-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## setParticleOptions

```TypeScript
default setParticleOptions(particles: Particles): this
```

Set Particle options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| particles | [Particles](arkts-arkui-particle-particles-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ParticleAttribute](arkts-arkui-particle-particleattribute-i.md) |

## velocityFields

```TypeScript
default velocityFields(fields: Array<VelocityFieldOptions> | undefined): this
```

设置粒子速度场。速度场会对影响范围内的粒子施加一个力，使粒子在原有速度的基础上叠加速度场指定的速度。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [fields](../../apis-arkdata/arkts-apis/arkts-arkdata-cloudextension-table-i-sys.md) | Array&lt;[VelocityFieldOptions](arkts-arkui-particle-velocityfieldoptions-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |
