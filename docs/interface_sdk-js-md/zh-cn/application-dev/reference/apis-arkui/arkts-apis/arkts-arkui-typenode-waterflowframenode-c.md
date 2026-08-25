# WaterFlowFrameNode

定义WaterFlow类型的FrameNode。

**继承/实现关系：** WaterFlowFrameNode extends TypedFrameNode<WaterFlowAttribute>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(options?: WaterFlowOptions): WaterFlowAttribute
```

初始化WaterFlow类型的FrameNode。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [WaterFlowOptions](../arkts-components/arkts-arkui-waterflowoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [WaterFlowAttribute](arkts-arkui-waterflow-waterflowattribute-i.md) |
