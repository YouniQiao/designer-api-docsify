# Tabs

## Tabs

```TypeScript
export declare function Tabs(
    options?: TabsOptions, 
    content_?: CustomBuilder,
): TabsAttribute
```

Defines Tabs Component

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Tabs(    options?: TabsOptions,     content_?: CustomBuilder,): TabsAttribute--><!--Device-unnamed-export declare function Tabs(    options?: TabsOptions,     content_?: CustomBuilder,): TabsAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TabsOptions](arkts-arkui-tabs-tabsoptions-i.md) | No | tabs constructor options |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [TabsAttribute](../arkts-components/arkts-arkui-tabs-attribute.md) |  |


## Tabs

```TypeScript
export declare function Tabs(
 style_: CustomBuilderT<TabsAttribute>,
 content_?: CustomBuilder,
): TabsAttribute
```

Defines Tabs Component

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Tabs( style_: CustomBuilderT<TabsAttribute>, content_?: CustomBuilder,): TabsAttribute--><!--Device-unnamed-export declare function Tabs( style_: CustomBuilderT<TabsAttribute>, content_?: CustomBuilder,): TabsAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;TabsAttribute&gt; | Yes | tabs attribute instance |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [TabsAttribute](../arkts-components/arkts-arkui-tabs-attribute.md) |  |

