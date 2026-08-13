# ArcList

## Modules to Import

```TypeScript
import { ArcListItemAttribute, ArcList, ArcListItem, ArcListAttribute } from '@kit.ArkUI';
```

## ArcList

```TypeScript
@ComponentBuilder
export declare function ArcList(
    options?: ArkListOptions,
    content_?: CustomBuilder,
): ArcListAttribute
```

Defines ArcList Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-@ComponentBuilderexport declare function ArcList(    options?: ArkListOptions,    content_?: CustomBuilder,): ArcListAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function ArcList(    options?: ArkListOptions,    content_?: CustomBuilder,): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ArkListOptions](arkts-arkui-arkui-arclist-arklistoptions-i.md) | No |  |
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |  |


## ArcList

```TypeScript
@Builder
export declare function ArcList(
    style_: CustomBuilderT<ArcListAttribute>,
    content_?: CustomBuilder
): ArcListAttribute
```

Defines ArcList Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function ArcList(    style_: CustomBuilderT<ArcListAttribute>,    content_?: CustomBuilder): ArcListAttribute--><!--Device-unnamed-@Builderexport declare function ArcList(    style_: CustomBuilderT<ArcListAttribute>,    content_?: CustomBuilder): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;[ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md)&gt; | Yes | The style to create an ArcList. |
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) | The attribute of the ArcList. |

