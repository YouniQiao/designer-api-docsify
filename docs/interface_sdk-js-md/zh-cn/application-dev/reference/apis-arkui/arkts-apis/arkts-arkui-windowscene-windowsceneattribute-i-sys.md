# WindowSceneAttribute（系统接口）

The WindowSceneAttribute

**继承/实现关系：** WindowSceneAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface WindowSceneAttribute extends CommonMethod--><!--Device-unnamed-export declare interface WindowSceneAttribute extends CommonMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## attractionEffect

```TypeScript
default attractionEffect(destination: Position | undefined, fraction: double | undefined): this
```

Set the attraction deformation effect of WindowScene.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WindowSceneAttribute-default attractionEffect(destination: Position | undefined, fraction: double | undefined): this--><!--Device-WindowSceneAttribute-default attractionEffect(destination: Position | undefined, fraction: double | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| destination | [Position](arkts-arkui-position-i.md) \| undefined | 是 | The position of the attraction target point in the component coordinate system. |
| fraction | double \| undefined | 是 | indicates the fraction of WindowScene. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## attributeModifier

```TypeScript
default attributeModifier(modifier:
    AttributeModifier<WindowSceneAttribute> | AttributeModifier<CommonMethod> | undefined) : this
```

Set the attribute modifier

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WindowSceneAttribute-default attributeModifier(modifier:    AttributeModifier<WindowSceneAttribute> | AttributeModifier<CommonMethod> | undefined) : this--><!--Device-WindowSceneAttribute-default attributeModifier(modifier:    AttributeModifier<WindowSceneAttribute> | AttributeModifier<CommonMethod> | undefined) : this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;WindowSceneAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

