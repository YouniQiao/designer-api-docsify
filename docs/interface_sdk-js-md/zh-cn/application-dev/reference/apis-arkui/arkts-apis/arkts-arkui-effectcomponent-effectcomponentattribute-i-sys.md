# EffectComponentAttribute（系统接口）

Define the EffectComponentAttribute.

**继承/实现关系：** EffectComponentAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## alwaysSnapshot

```TypeScript
alwaysSnapshot(enable: boolean | undefined): this
```

Use snapshot when Effect Component have no visual effect.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [EffectComponentAttribute](arkts-arkui-effectcomponent-effectcomponentattribute-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<EffectComponentAttribute>
      | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier for EffectComponent.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[EffectComponentAttribute](arkts-arkui-effectcomponent-effectcomponentattribute-i-sys.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [EffectComponentAttribute](arkts-arkui-effectcomponent-effectcomponentattribute-i-sys.md) |

## setEffectComponentOptions

```TypeScript
default setEffectComponentOptions(options?: EffectComponentOptions): this
```

Set EffectComponent options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [EffectComponentOptions](arkts-arkui-effectcomponent-effectcomponentoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [EffectComponentAttribute](arkts-arkui-effectcomponent-effectcomponentattribute-i-sys.md) |
