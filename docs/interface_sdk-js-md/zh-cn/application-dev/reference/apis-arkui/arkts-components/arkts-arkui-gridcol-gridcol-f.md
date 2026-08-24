# GridCol

## GridCol

```TypeScript
@ComponentBuilder
export declare function GridCol(
    option?: GridColOptions, 
    content_?: CustomBuilder,
): GridColAttribute
```

栅格列布局组件。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @ComponentBuilder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-@ComponentBuilderexport declare function GridCol(    option?: GridColOptions,     content_?: CustomBuilder,): GridColAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function GridCol(    option?: GridColOptions,     content_?: CustomBuilder,): GridColAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [GridColOptions](arkts-arkui-gridcol-gridcoloptions-i.md) | 否 | 栅格布局子组件参数。 |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | 否 | container |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GridColAttribute](arkts-arkui-gridcol-attribute.md) |  |


## GridCol

```TypeScript
@Builder
export declare function GridCol(
    style: CustomBuilderT<GridColAttribute>,
    content_?: CustomBuilder,
): GridColAttribute
```

Defines GridCol Component.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-@Builderexport declare function GridCol(    style: CustomBuilderT<GridColAttribute>,    content_?: CustomBuilder,): GridColAttribute--><!--Device-unnamed-@Builderexport declare function GridCol(    style: CustomBuilderT<GridColAttribute>,    content_?: CustomBuilder,): GridColAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;[GridColAttribute](arkts-arkui-gridcol-attribute.md)&gt; | 是 | the callback to set up component's attributes. |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | 否 | container |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GridColAttribute](arkts-arkui-gridcol-attribute.md) |  |

