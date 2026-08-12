# LazyVGridLayout

## LazyVGridLayout

```TypeScript
export declare function LazyVGridLayout(
    content_?: CustomBuilder,
): LazyVGridLayoutAttribute
```

Defines LazyVGridLayout Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function LazyVGridLayout(    content_?: CustomBuilder,): LazyVGridLayoutAttribute--><!--Device-unnamed-export declare function LazyVGridLayout(    content_?: CustomBuilder,): LazyVGridLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyVGridLayoutAttribute](arkts-arkui-lazygridlayout-lazyvgridlayoutattribute-i.md) | The attribute of the grid |


## LazyVGridLayout

```TypeScript
export declare function LazyVGridLayout(
    style_: CustomBuilderT<LazyVGridLayoutAttribute>,
    content_?: CustomBuilder
): LazyVGridLayoutAttribute
```

Defines LazyVGridLayout Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function LazyVGridLayout(    style_: CustomBuilderT<LazyVGridLayoutAttribute>,    content_?: CustomBuilder): LazyVGridLayoutAttribute--><!--Device-unnamed-export declare function LazyVGridLayout(    style_: CustomBuilderT<LazyVGridLayoutAttribute>,    content_?: CustomBuilder): LazyVGridLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[LazyVGridLayoutAttribute](arkts-arkui-lazygridlayout-lazyvgridlayoutattribute-i.md)&gt; | Yes | The style to create a LazyVGridLayout. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyVGridLayoutAttribute](arkts-arkui-lazygridlayout-lazyvgridlayoutattribute-i.md) | The attribute of the LazyVGridLayout. |

