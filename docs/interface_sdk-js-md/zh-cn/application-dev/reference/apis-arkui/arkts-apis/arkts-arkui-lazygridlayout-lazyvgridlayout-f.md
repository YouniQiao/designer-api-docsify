# LazyVGridLayout

## LazyVGridLayout

```TypeScript
export declare function LazyVGridLayout(
    content_?: CustomBuilder,
): LazyVGridLayoutAttribute
```

创建垂直方向懒加载网格布局容器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function LazyVGridLayout(    content_?: CustomBuilder,): LazyVGridLayoutAttribute--><!--Device-unnamed-export declare function LazyVGridLayout(    content_?: CustomBuilder,): LazyVGridLayoutAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 | 容器内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LazyVGridLayoutAttribute](arkts-arkui-lazygridlayout-lazyvgridlayoutattribute-i.md) | 返回LazyVGridLayout组件的属性。 |


## LazyVGridLayout

```TypeScript
export declare function LazyVGridLayout(
    style_: CustomBuilderT<LazyVGridLayoutAttribute>,
    content_?: CustomBuilder
): LazyVGridLayoutAttribute
```

定义LazyVGridLayout组件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function LazyVGridLayout(    style_: CustomBuilderT<LazyVGridLayoutAttribute>,    content_?: CustomBuilder): LazyVGridLayoutAttribute--><!--Device-unnamed-export declare function LazyVGridLayout(    style_: CustomBuilderT<LazyVGridLayoutAttribute>,    content_?: CustomBuilder): LazyVGridLayoutAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[LazyVGridLayoutAttribute](arkts-arkui-lazygridlayout-lazyvgridlayoutattribute-i.md)&gt; | 是 | 创建LazyVGridLayout的样式 |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LazyVGridLayoutAttribute](arkts-arkui-lazygridlayout-lazyvgridlayoutattribute-i.md) | LazyVGridLayout的属性。 |

