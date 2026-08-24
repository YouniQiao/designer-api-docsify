# NodeContainerAttribute

The NodeContainerAttribute.

**Inheritance/Implementation:** NodeContainerAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface NodeContainerAttribute--><!--Device-unnamed-export declare interface NodeContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(
        modifier: AttributeModifier<NodeContainerAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Sets the attribute modifier.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeContainerAttribute-attributeModifier(        modifier: AttributeModifier<NodeContainerAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-NodeContainerAttribute-attributeModifier(        modifier: AttributeModifier<NodeContainerAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[NodeContainerAttribute](arkts-nodecontainer-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes | instance of NodeController. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setNodeContainerOptions

```TypeScript
setNodeContainerOptions(controller: NodeController): this
```

Sets NodeContainer options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeContainerAttribute-setNodeContainerOptions(controller: NodeController): this--><!--Device-NodeContainerAttribute-setNodeContainerOptions(controller: NodeController): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controller | [NodeController](../arkts-apis/arkts-nodecontroller-c.md) | Yes | Instance of controller of NodeContainer. |

**Return value:**

| Type | Description |
| --- | --- |
| this | NodeContainerAttribute instance |

