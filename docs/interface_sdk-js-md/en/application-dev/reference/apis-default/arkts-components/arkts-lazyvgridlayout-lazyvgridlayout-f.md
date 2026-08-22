# LazyVGridLayout

## LazyVGridLayout

```TypeScript
@ComponentBuilder
export declare function LazyVGridLayout(
    content_?: CustomBuilder,
): LazyVGridLayoutAttribute
```

Defines LazyVGridLayout Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function LazyVGridLayout(    content_?: CustomBuilder,): LazyVGridLayoutAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function LazyVGridLayout(    content_?: CustomBuilder,): LazyVGridLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyVGridLayoutAttribute](arkts-lazyvgridlayout-attribute.md) | The attribute of the grid |


## LazyVGridLayout

```TypeScript
@Builder
export declare function LazyVGridLayout(
    style_: CustomBuilderT<LazyVGridLayoutAttribute>,
    content_?: CustomBuilder
): LazyVGridLayoutAttribute
```

Defines LazyVGridLayout Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function LazyVGridLayout(    style_: CustomBuilderT<LazyVGridLayoutAttribute>,    content_?: CustomBuilder): LazyVGridLayoutAttribute--><!--Device-unnamed-@Builderexport declare function LazyVGridLayout(    style_: CustomBuilderT<LazyVGridLayoutAttribute>,    content_?: CustomBuilder): LazyVGridLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[LazyVGridLayoutAttribute](arkts-lazyvgridlayout-attribute.md)&gt; | Yes | The style to create a LazyVGridLayout. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyVGridLayoutAttribute](arkts-lazyvgridlayout-attribute.md) | The attribute of the LazyVGridLayout. |

