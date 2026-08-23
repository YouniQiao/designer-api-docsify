# NodeContainerAttribute

The NodeContainerAttribute.

**继承/实现关系：** NodeContainerAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare interface NodeContainerAttribute--><!--Device-unnamed-export declare interface NodeContainerAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(
        modifier: AttributeModifier<NodeContainerAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置属性修饰符。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NodeContainerAttribute-attributeModifier(        modifier: AttributeModifier<NodeContainerAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-NodeContainerAttribute-attributeModifier(        modifier: AttributeModifier<NodeContainerAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[NodeContainerAttribute](arkts-nodecontainer-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 | NodeController的实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## setNodeContainerOptions

```TypeScript
setNodeContainerOptions(controller: NodeController): this
```

设置NodeContainer选项。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NodeContainerAttribute-setNodeContainerOptions(controller: NodeController): this--><!--Device-NodeContainerAttribute-setNodeContainerOptions(controller: NodeController): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | [NodeController](../../apis-arkui/arkts-apis/arkts-arkui-nodecontroller-c.md) | 是 | NodeContainer的控制器实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | NodeContainerAttribute实例。 |

