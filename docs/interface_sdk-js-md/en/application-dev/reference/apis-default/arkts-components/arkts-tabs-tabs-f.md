# Tabs

## Tabs

```TypeScript
@ComponentBuilder
export declare function Tabs(
    options?: TabsOptions, 
    content_?: CustomBuilder,
): TabsAttribute
```

Defines Tabs Component

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Tabs(    options?: TabsOptions,     content_?: CustomBuilder,): TabsAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Tabs(    options?: TabsOptions,     content_?: CustomBuilder,): TabsAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TabsOptions](arkts-tabs-tabsoptions-i.md) | No | tabs constructor options |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [TabsAttribute](arkts-tabs-attribute.md) |  |


## Tabs

```TypeScript
@Builder
export declare function Tabs(
 style_: CustomBuilderT<TabsAttribute>,
 content_?: CustomBuilder,
): TabsAttribute
```

Defines Tabs Component

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Tabs( style_: CustomBuilderT<TabsAttribute>, content_?: CustomBuilder,): TabsAttribute--><!--Device-unnamed-@Builderexport declare function Tabs( style_: CustomBuilderT<TabsAttribute>, content_?: CustomBuilder,): TabsAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[TabsAttribute](arkts-tabs-attribute.md)&gt; | Yes | tabs attribute instance |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [TabsAttribute](arkts-tabs-attribute.md) |  |

