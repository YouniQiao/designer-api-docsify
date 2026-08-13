# Badge

## Badge

```TypeScript
@ComponentBuilder
export declare function Badge(
    value: BadgeParamWithNumber | BadgeParamWithString, 
    content_?: CustomBuilder
): BadgeAttribute
```

Defines Badge Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Badge(    value: BadgeParamWithNumber | BadgeParamWithString,     content_?: CustomBuilder): BadgeAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Badge(    value: BadgeParamWithNumber | BadgeParamWithString,     content_?: CustomBuilder): BadgeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [BadgeParamWithNumber](arkts-na-badge-badgeparamwithnumber-i.md) \| [BadgeParamWithString](arkts-na-badge-badgeparamwithstring-i.md) | Yes | Markup component parameters of the numeric and character string types |
| content_ | CustomBuilder | No | Child component |

**Return value:**

| Type | Description |
| --- | --- |
| BadgeAttribute |  |


## Badge

```TypeScript
@Builder
export declare function Badge(
    style: CustomBuilderT<BadgeAttribute>,
    content_?: CustomBuilder,
): BadgeAttribute
```

Defines Badge Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Badge(    style: CustomBuilderT<BadgeAttribute>,    content_?: CustomBuilder,): BadgeAttribute--><!--Device-unnamed-@Builderexport declare function Badge(    style: CustomBuilderT<BadgeAttribute>,    content_?: CustomBuilder,): BadgeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | CustomBuilderT&lt;BadgeAttribute&gt; | Yes | badge attribute instance |
| content_ | CustomBuilder | No | Child component |

**Return value:**

| Type | Description |
| --- | --- |
| BadgeAttribute |  |

