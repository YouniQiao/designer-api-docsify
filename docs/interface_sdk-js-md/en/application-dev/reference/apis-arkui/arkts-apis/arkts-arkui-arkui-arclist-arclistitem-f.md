# ArcListItem

## Modules to Import

```TypeScript
import { ArcListItemAttribute, ArcList, ArcListItem, ArcListAttribute } from '@kit.ArkUI';
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

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-@ComponentBuilderexport declare function ArcListItem(    content_?: CustomBuilder,): ArcListItemAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function ArcListItem(    content_?: CustomBuilder,): ArcListItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| ArcListItemAttribute |  |


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

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function ArcListItem(    style_: CustomBuilderT<ArcListItemAttribute>,    content_?: CustomBuilder): ArcListItemAttribute--><!--Device-unnamed-@Builderexport declare function ArcListItem(    style_: CustomBuilderT<ArcListItemAttribute>,    content_?: CustomBuilder): ArcListItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;ArcListItemAttribute&gt; | Yes | The style to create an ArcListItem. |
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| ArcListItemAttribute | The attribute of the ArcListItem. |

