# GridItem

## GridItem

```TypeScript
export declare function GridItem(
    value?: GridItemOptions, 
    content_?: CustomBuilder,
): GridItemAttribute
```

创建网格容器中单项内容容器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function GridItem(    value?: GridItemOptions,     content_?: CustomBuilder,): GridItemAttribute--><!--Device-unnamed-export declare function GridItem(    value?: GridItemOptions,     content_?: CustomBuilder,): GridItemAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [GridItemOptions](arkts-arkui-griditem-griditemoptions-i.md) | 否 | 为GridItem提供可选参数。 |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 | 容器内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GridItemAttribute](arkts-arkui-griditem-griditemattribute-i.md) |  |


## GridItem

```TypeScript
export declare function GridItem(
    style_: CustomBuilderT<GridItemAttribute>,
    content_?: CustomBuilder
): GridItemAttribute
```

可扩展的GridItem组件的入口。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function GridItem(    style_: CustomBuilderT<GridItemAttribute>,    content_?: CustomBuilder): GridItemAttribute--><!--Device-unnamed-export declare function GridItem(    style_: CustomBuilderT<GridItemAttribute>,    content_?: CustomBuilder): GridItemAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[GridItemAttribute](arkts-arkui-griditem-griditemattribute-i.md)&gt; | 是 | The style to create a GridItem. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GridItemAttribute](arkts-arkui-griditem-griditemattribute-i.md) | The attribute of the GridItem. |

