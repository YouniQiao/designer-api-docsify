# LazyVGridLayout

## LazyVGridLayout

```TypeScript
export declare function LazyVGridLayout(
    content_?: CustomBuilder,
): LazyVGridLayoutAttribute
```

创建垂直方向懒加载网格布局容器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function LazyVGridLayout(    content_?: CustomBuilder,): LazyVGridLayoutAttribute--><!--Device-unnamed-export declare function LazyVGridLayout(    content_?: CustomBuilder,): LazyVGridLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 容器内容。 |

**Return value:**

| Type | Description |
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

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function LazyVGridLayout(    style_: CustomBuilderT<LazyVGridLayoutAttribute>,    content_?: CustomBuilder): LazyVGridLayoutAttribute--><!--Device-unnamed-export declare function LazyVGridLayout(    style_: CustomBuilderT<LazyVGridLayoutAttribute>,    content_?: CustomBuilder): LazyVGridLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;LazyVGridLayoutAttribute&gt; | Yes | 创建LazyVGridLayout的样式 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyVGridLayoutAttribute](arkts-arkui-lazygridlayout-lazyvgridlayoutattribute-i.md) | LazyVGridLayout的属性。 |

