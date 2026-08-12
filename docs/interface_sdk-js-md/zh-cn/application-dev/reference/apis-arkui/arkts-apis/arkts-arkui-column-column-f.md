# Column

## Column

```TypeScript
export declare function Column(
    options?: ColumnOptions | ColumnOptions | ColumnOptionsV2,
    content_?: CustomBuilder,
): ColumnAttribute
```

沿垂直方向布局的容器。

> **说明：**
> 
> Column未设置高度或宽度时，在主轴或交叉轴方向上自适应子组件大小。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function Column(    options?: ColumnOptions | ColumnOptions | ColumnOptionsV2,    content_?: CustomBuilder,): ColumnAttribute--><!--Device-unnamed-export declare function Column(    options?: ColumnOptions | ColumnOptions | ColumnOptionsV2,    content_?: CustomBuilder,): ColumnAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ColumnOptions](arkts-arkui-column-columnoptions-i.md) \| [ColumnOptions](arkts-arkui-column-columnoptions-i.md) \| [ColumnOptionsV2](arkts-arkui-column-columnoptionsv2-i.md) | 否 | Column options. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 | container |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColumnAttribute](arkts-arkui-column-columnattribute-i.md) |  |


## Column

```TypeScript
export declare function Column(
    style: CustomBuilderT<ColumnAttribute>,
    content_?: CustomBuilder,
): ColumnAttribute
```

Defines Column Component.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function Column(    style: CustomBuilderT<ColumnAttribute>,    content_?: CustomBuilder,): ColumnAttribute--><!--Device-unnamed-export declare function Column(    style: CustomBuilderT<ColumnAttribute>,    content_?: CustomBuilder,): ColumnAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[ColumnAttribute](arkts-arkui-column-columnattribute-i.md)&gt; | 是 | the callback to set up component's attributes. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 | container |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColumnAttribute](arkts-arkui-column-columnattribute-i.md) |  |

