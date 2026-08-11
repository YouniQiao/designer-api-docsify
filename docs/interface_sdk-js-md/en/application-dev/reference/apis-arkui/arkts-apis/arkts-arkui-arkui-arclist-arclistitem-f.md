# ArcListItem

## Modules to Import

```TypeScript
import { ArcListItemAttribute, ArcList, ArcListItem, ArcListAttribute } from 'kits/@kit.ArkUI';
```

## ArcListItem

```TypeScript
export declare function ArcListItem(
    content_?: CustomBuilder,
): ArcListItemAttribute
```

Defines ArcListItem Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare function ArcListItem(    content_?: CustomBuilder,): ArcListItemAttribute--><!--Device-unnamed-export declare function ArcListItem(    content_?: CustomBuilder,): ArcListItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcListItemAttribute](arkts-arkui-arkui-arclist-arclistitemattribute-c.md) |  |


## ArcListItem

```TypeScript
export declare function ArcListItem(
    style_: CustomBuilderT<ArcListItemAttribute>,
    content_?: CustomBuilder
): ArcListItemAttribute
```

Defines ArcListItem Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ArcListItem(    style_: CustomBuilderT<ArcListItemAttribute>,    content_?: CustomBuilder): ArcListItemAttribute--><!--Device-unnamed-export declare function ArcListItem(    style_: CustomBuilderT<ArcListItemAttribute>,    content_?: CustomBuilder): ArcListItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;ArcListItemAttribute&gt; | Yes | The style to create an ArcListItem. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcListItemAttribute](arkts-arkui-arkui-arclist-arclistitemattribute-c.md) | The attribute of the ArcListItem. |

