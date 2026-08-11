# Divider

## Divider

```TypeScript
export declare function Divider(): DividerAttribute
```

提供分割线组件，分割不同内容块/内容元素。

> **说明：**
> 
> 如果出现分割线粗细不一或者消失的问题，请参考
> [组件级像素取整常见问题](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-pixelRoundForComponent.md#常见问题)。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function Divider(): DividerAttribute--><!--Device-unnamed-export declare function Divider(): DividerAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DividerAttribute](../arkts-components/arkts-arkui-divider-attribute.md) |  |


## Divider

```TypeScript
export declare function Divider(
    style: CustomBuilderT<DividerAttribute>
): DividerAttribute
```

Defines Divider Component.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function Divider(    style: CustomBuilderT<DividerAttribute>): DividerAttribute--><!--Device-unnamed-export declare function Divider(    style: CustomBuilderT<DividerAttribute>): DividerAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;DividerAttribute&gt; | 是 | the callback to set up component's attributes. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DividerAttribute](../arkts-components/arkts-arkui-divider-attribute.md) |  |

