# WaterFlow

## WaterFlow

```TypeScript
export declare function WaterFlow(
    options?: WaterFlowOptions, 
    content_?: CustomBuilder,
): WaterFlowAttribute
```

定义瀑布流组件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [WaterFlowOptions](arkts-arkui-waterflow-waterflowoptions-i.md) | 否 |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [WaterFlowAttribute](arkts-arkui-waterflow-waterflowattribute-i.md) |


## WaterFlow

```TypeScript
export declare function WaterFlow(
    style_: CustomBuilderT<WaterFlowAttribute>, 
    content_?: CustomBuilder
): WaterFlowAttribute
```

定义WaterFlow组件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style_ | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[WaterFlowAttribute](arkts-arkui-waterflow-waterflowattribute-i.md)&gt; | 是 |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [WaterFlowAttribute](arkts-arkui-waterflow-waterflowattribute-i.md) |
