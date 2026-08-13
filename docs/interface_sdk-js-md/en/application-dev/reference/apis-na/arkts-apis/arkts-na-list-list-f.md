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

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function List(    options?: ListOptions,    content_?: CustomBuilder,): ListAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function List(    options?: ListOptions,    content_?: CustomBuilder,): ListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ListOptions](arkts-na-list-listoptions-i.md) | No |  |
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| ListAttribute |  |


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

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function List(    style_: CustomBuilderT<ListAttribute>,    content_?: CustomBuilder): ListAttribute--><!--Device-unnamed-@Builderexport declare function List(    style_: CustomBuilderT<ListAttribute>,    content_?: CustomBuilder): ListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;ListAttribute&gt; | Yes | The style to create a List. |
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| ListAttribute | The attribute of the List. |

