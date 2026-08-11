# Badge

## Badge

```TypeScript
export declare function Badge(
    value: BadgeParamWithNumber | BadgeParamWithString, 
    content_?: CustomBuilder
): BadgeAttribute
```

Defines Badge Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Badge(    value: BadgeParamWithNumber | BadgeParamWithString,     content_?: CustomBuilder): BadgeAttribute--><!--Device-unnamed-export declare function Badge(    value: BadgeParamWithNumber | BadgeParamWithString,     content_?: CustomBuilder): BadgeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [BadgeParamWithNumber](arkts-arkui-badge-badgeparamwithnumber-i.md) \| BadgeParamWithString | Yes | Markup component parameters of the numeric and character string types |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | Child component |

**Return value:**

| Type | Description |
| --- | --- |
| [BadgeAttribute](../arkts-components/arkts-arkui-badge-attribute.md) |  |


## Badge

```TypeScript
export declare function Badge(
    style: CustomBuilderT<BadgeAttribute>,
    content_?: CustomBuilder,
): BadgeAttribute
```

Defines Badge Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Badge(    style: CustomBuilderT<BadgeAttribute>,    content_?: CustomBuilder,): BadgeAttribute--><!--Device-unnamed-export declare function Badge(    style: CustomBuilderT<BadgeAttribute>,    content_?: CustomBuilder,): BadgeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;BadgeAttribute&gt; | Yes | badge attribute instance |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | Child component |

**Return value:**

| Type | Description |
| --- | --- |
| [BadgeAttribute](../arkts-components/arkts-arkui-badge-attribute.md) |  |

