# List

## List

```TypeScript
@ComponentBuilder
export declare function List(
    options?: ListOptions,
    content_?: CustomBuilder,
): ListAttribute
```

Defines List Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @ComponentBuilder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function List(    options?: ListOptions,    content_?: CustomBuilder,): ListAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function List(    options?: ListOptions,    content_?: CustomBuilder,): ListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ListOptions](arkts-list-listoptions-i.md) | No |  |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ListAttribute](arkts-list-attribute.md) |  |


## List

```TypeScript
@Builder
export declare function List(
    style_: CustomBuilderT<ListAttribute>,
    content_?: CustomBuilder
): ListAttribute
```

Defines List Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function List(    style_: CustomBuilderT<ListAttribute>,    content_?: CustomBuilder): ListAttribute--><!--Device-unnamed-@Builderexport declare function List(    style_: CustomBuilderT<ListAttribute>,    content_?: CustomBuilder): ListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[ListAttribute](arkts-list-attribute.md)&gt; | Yes | The style to create a List. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ListAttribute](arkts-list-attribute.md) | The attribute of the List. |

