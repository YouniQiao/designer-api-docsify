# LazyDynamicLayout

## Modules to Import

```TypeScript
```

## LazyDynamicLayout

```TypeScript
@ComponentBuilder
export declare function LazyDynamicLayout (
    algorithm: LazyLayoutAlgorithm,
    content_: CustomBuilder,
): LazyDynamicLayoutAttribute
```

Defines LazyDynamicLayout Component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Decorator:** @ComponentBuilder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function LazyDynamicLayout (    algorithm: LazyLayoutAlgorithm,    content_: CustomBuilder,): LazyDynamicLayoutAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function LazyDynamicLayout (    algorithm: LazyLayoutAlgorithm,    content_: CustomBuilder,): LazyDynamicLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| algorithm | [LazyLayoutAlgorithm](arkts-lazylayoutalgorithm-i.md) | Yes | Lazy layout algorithm. |
| content_ | CustomBuilder | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyDynamicLayoutAttribute](../../apis-arkui/arkts-apis/arkts-arkui-arkui-components-arklazydynamiclayout-lazydynamiclayoutattribute-c.md) |  |


## LazyDynamicLayout

```TypeScript
@Builder
export declare function LazyDynamicLayout(
    style_: CustomBuilderT<LazyDynamicLayoutAttribute>,
    content_?: CustomBuilder
): LazyDynamicLayoutAttribute
```

Defines LazyDynamicLayout Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function LazyDynamicLayout(    style_: CustomBuilderT<LazyDynamicLayoutAttribute>,    content_?: CustomBuilder): LazyDynamicLayoutAttribute--><!--Device-unnamed-@Builderexport declare function LazyDynamicLayout(    style_: CustomBuilderT<LazyDynamicLayoutAttribute>,    content_?: CustomBuilder): LazyDynamicLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;[LazyDynamicLayoutAttribute](../../apis-arkui/arkts-apis/arkts-arkui-arkui-components-arklazydynamiclayout-lazydynamiclayoutattribute-c.md)&gt; | Yes | The style to create a LazyDynamicLayout. |
| content_ | CustomBuilder | No | content |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyDynamicLayoutAttribute](../../apis-arkui/arkts-apis/arkts-arkui-arkui-components-arklazydynamiclayout-lazydynamiclayoutattribute-c.md) | The attribute of the LazyDynamicLayout. |

