# List

## List

```TypeScript
export declare function List(
    options?: ListOptions,
    content_?: CustomBuilder,
): ListAttribute
```

Defines List Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function List(    options?: ListOptions,    content_?: CustomBuilder,): ListAttribute--><!--Device-unnamed-export declare function List(    options?: ListOptions,    content_?: CustomBuilder,): ListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ListOptions](../arkts-components/arkts-arkui-listoptions-i.md) | No |  |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ListAttribute](arkts-arkui-list-listattribute-i.md) |  |


## List

```TypeScript
export declare function List(
    style_: CustomBuilderT<ListAttribute>,
    content_?: CustomBuilder
): ListAttribute
```

Defines List Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function List(    style_: CustomBuilderT<ListAttribute>,    content_?: CustomBuilder): ListAttribute--><!--Device-unnamed-export declare function List(    style_: CustomBuilderT<ListAttribute>,    content_?: CustomBuilder): ListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;ListAttribute&gt; | Yes | The style to create a List. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ListAttribute](arkts-arkui-list-listattribute-i.md) | The attribute of the List. |

