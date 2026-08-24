# RowSplit

## RowSplit

```TypeScript
@ComponentBuilder
export declare function RowSplit(

    content_?: CustomBuilder,
): RowSplitAttribute
```

带分割线的子组件横向分隔布局。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @ComponentBuilder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-@ComponentBuilderexport declare function RowSplit(    content_?: CustomBuilder,): RowSplitAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function RowSplit(    content_?: CustomBuilder,): RowSplitAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | 否 | 定义子组件的Builder函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RowSplitAttribute](arkts-arkui-rowsplit-attribute.md) |  |


## RowSplit

```TypeScript
@Builder
export declare function RowSplit(
    style: CustomBuilderT<RowSplitAttribute>,
    content_?: CustomBuilder,
): RowSplitAttribute
```

Defines RowSplit Component.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-@Builderexport declare function RowSplit(    style: CustomBuilderT<RowSplitAttribute>,    content_?: CustomBuilder,): RowSplitAttribute--><!--Device-unnamed-@Builderexport declare function RowSplit(    style: CustomBuilderT<RowSplitAttribute>,    content_?: CustomBuilder,): RowSplitAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;[RowSplitAttribute](arkts-arkui-rowsplit-attribute.md)&gt; | 是 | the callback to set up component's attributes. |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | 否 | container |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RowSplitAttribute](arkts-arkui-rowsplit-attribute.md) |  |

