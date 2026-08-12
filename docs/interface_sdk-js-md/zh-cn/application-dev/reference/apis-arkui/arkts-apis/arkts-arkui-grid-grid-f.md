# Grid

## Grid

```TypeScript
export declare function Grid(
    scroller?: Scroller, layoutOptions?: GridLayoutOptions, 
    content_?: CustomBuilder,
): GridAttribute
```

创建网格容器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function Grid(    scroller?: Scroller, layoutOptions?: GridLayoutOptions,     content_?: CustomBuilder,): GridAttribute--><!--Device-unnamed-export declare function Grid(    scroller?: Scroller, layoutOptions?: GridLayoutOptions,     content_?: CustomBuilder,): GridAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scroller | [Scroller](../arkts-components/arkts-arkui-scroller-c.md) | 否 | 可滚动组件的控制器，与可滚动组件进行绑定。 |
| layoutOptions | [GridLayoutOptions](arkts-arkui-grid-gridlayoutoptions-i.md) | 否 | Grid布局选项。 |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 | Grid子组件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GridAttribute](arkts-arkui-grid-gridattribute-i.md) |  |


## Grid

```TypeScript
export declare function Grid(
    style_: CustomBuilderT<GridAttribute>,
    content_?: CustomBuilder
): GridAttribute
```

可扩展Grid组件入口。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function Grid(    style_: CustomBuilderT<GridAttribute>,    content_?: CustomBuilder): GridAttribute--><!--Device-unnamed-export declare function Grid(    style_: CustomBuilderT<GridAttribute>,    content_?: CustomBuilder): GridAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[GridAttribute](arkts-arkui-grid-gridattribute-i.md)&gt; | 是 | The style to create a Grid. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GridAttribute](arkts-arkui-grid-gridattribute-i.md) | The attribute of the Grid. |

