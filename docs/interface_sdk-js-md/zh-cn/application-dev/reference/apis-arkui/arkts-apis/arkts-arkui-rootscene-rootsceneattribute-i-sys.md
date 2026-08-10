# RootSceneAttribute（系统接口）

Defines the attribute functions of RootScene.

**继承/实现关系：** RootSceneAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface RootSceneAttribute extends CommonMethod--><!--Device-unnamed-export declare interface RootSceneAttribute extends CommonMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## attributeModifier

```TypeScript
default attributeModifier(modifier:
    AttributeModifier<RootSceneAttribute> | AttributeModifier<CommonMethod> | undefined) : this
```

Set the attribute modifier

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RootSceneAttribute-default attributeModifier(modifier:    AttributeModifier<RootSceneAttribute> | AttributeModifier<CommonMethod> | undefined) : this--><!--Device-RootSceneAttribute-default attributeModifier(modifier:    AttributeModifier<RootSceneAttribute> | AttributeModifier<CommonMethod> | undefined) : this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;RootSceneAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

