# ArcListItem

## Modules to Import

```TypeScript
import { ArcList, ArcListItem, ArcListAttribute, ArcListItemAttribute } from '@kit.ArkUI';
```

## ArcListItem

```TypeScript
@ComponentBuilder
export declare function ArcListItem(
    content_?: CustomBuilder,
): ArcListItemAttribute
```

Defines ArcListItem Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-@ComponentBuilderexport declare function ArcListItem(    content_?: CustomBuilder,): ArcListItemAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function ArcListItem(    content_?: CustomBuilder,): ArcListItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcListItemAttribute](arkts-arkui-arkui-arclist-arclistitemattribute-i.md) |  |


## ArcListItem

```TypeScript
@Builder
export declare function ArcListItem(
    style_: CustomBuilderT<ArcListItemAttribute>,
    content_?: CustomBuilder
): ArcListItemAttribute
```

Defines ArcListItem Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function ArcListItem(    style_: CustomBuilderT<ArcListItemAttribute>,    content_?: CustomBuilder): ArcListItemAttribute--><!--Device-unnamed-@Builderexport declare function ArcListItem(    style_: CustomBuilderT<ArcListItemAttribute>,    content_?: CustomBuilder): ArcListItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;[ArcListItemAttribute](arkts-arkui-arkui-arclist-arclistitemattribute-i.md)&gt; | Yes | The style to create an ArcListItem. |
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcListItemAttribute](arkts-arkui-arkui-arclist-arclistitemattribute-i.md) | The attribute of the ArcListItem. |

