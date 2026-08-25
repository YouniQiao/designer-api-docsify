# NodeContainer

## NodeContainer

```TypeScript
export declare function NodeContainer(
    controller: NodeController
): NodeContainerAttribute
```

创建NodeContainer组件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| controller | [NodeController](arkts-arkui-nodecontroller-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [NodeContainerAttribute](arkts-arkui-nodecontainer-nodecontainerattribute-i.md) |


## NodeContainer

```TypeScript
export declare function NodeContainer(
    style: CustomBuilderT<NodeContainerAttribute>
): NodeContainerAttribute
```

定义NodeContainer组件。需要在组件属性设置开始时调用setNodeContainerOptions，并在组件属性设置结束时调用applyAttributeFinish。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[NodeContainerAttribute](arkts-arkui-nodecontainer-nodecontainerattribute-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [NodeContainerAttribute](arkts-arkui-nodecontainer-nodecontainerattribute-i.md) |
