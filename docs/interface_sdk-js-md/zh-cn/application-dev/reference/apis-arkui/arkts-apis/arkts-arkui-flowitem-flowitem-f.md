# FlowItem

## FlowItem

```TypeScript
export declare function FlowItem(
    content_?: CustomBuilder,
): FlowItemAttribute
```

创建瀑布流子组件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [FlowItemAttribute](arkts-arkui-flowitem-flowitemattribute-i.md) |


## FlowItem

```TypeScript
export declare function FlowItem(
    style_: CustomBuilderT<FlowItemAttribute>,
    content_?: CustomBuilder
): FlowItemAttribute
```

定义FlowItem组件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style_ | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[FlowItemAttribute](arkts-arkui-flowitem-flowitemattribute-i.md)&gt; | 是 |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [FlowItemAttribute](arkts-arkui-flowitem-flowitemattribute-i.md) |
