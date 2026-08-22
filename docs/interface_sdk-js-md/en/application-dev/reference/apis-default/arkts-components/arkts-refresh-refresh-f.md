# Refresh

## Refresh

```TypeScript
@ComponentBuilder
export declare function Refresh(
    value: RefreshOptions,
    content_?: CustomBuilder,
): RefreshAttribute
```

Defines Refresh Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Refresh(    value: RefreshOptions,    content_?: CustomBuilder,): RefreshAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Refresh(    value: RefreshOptions,    content_?: CustomBuilder,): RefreshAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [RefreshOptions](arkts-refresh-refreshoptions-i.md) | Yes | value |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [RefreshAttribute](arkts-refresh-attribute.md) | The attribute of the grid |


## Refresh

```TypeScript
@Builder
export declare function Refresh(
    style_: CustomBuilderT<RefreshAttribute>,
    content_?: CustomBuilder
): RefreshAttribute
```

Defines Refresh Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Refresh(    style_: CustomBuilderT<RefreshAttribute>,    content_?: CustomBuilder): RefreshAttribute--><!--Device-unnamed-@Builderexport declare function Refresh(    style_: CustomBuilderT<RefreshAttribute>,    content_?: CustomBuilder): RefreshAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[RefreshAttribute](arkts-refresh-attribute.md)&gt; | Yes | The style to create a Refresh. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [RefreshAttribute](arkts-refresh-attribute.md) | The attribute of the Refresh. |

