# Flex

## Flex

```TypeScript
export declare function Flex(
    value?: FlexOptions,
    content_?: CustomBuilder,
): FlexAttribute
```

Flex布局容器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function Flex(    value?: FlexOptions,    content_?: CustomBuilder,): FlexAttribute--><!--Device-unnamed-export declare function Flex(    value?: FlexOptions,    content_?: CustomBuilder,): FlexAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [FlexOptions](arkts-arkui-flex-flexoptions-i.md) | 否 | 弹性布局子组件参数。 |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 | container |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FlexAttribute](arkts-arkui-flex-flexattribute-i.md) |  |


## Flex

```TypeScript
export declare function Flex(
    style: CustomBuilderT<FlexAttribute>,
    content_?: CustomBuilder,
): FlexAttribute
```

Defines Flex Component.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function Flex(    style: CustomBuilderT<FlexAttribute>,    content_?: CustomBuilder,): FlexAttribute--><!--Device-unnamed-export declare function Flex(    style: CustomBuilderT<FlexAttribute>,    content_?: CustomBuilder,): FlexAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[FlexAttribute](arkts-arkui-flex-flexattribute-i.md)&gt; | 是 | the callback to set up component's attributes. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 | container |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FlexAttribute](arkts-arkui-flex-flexattribute-i.md) |  |

