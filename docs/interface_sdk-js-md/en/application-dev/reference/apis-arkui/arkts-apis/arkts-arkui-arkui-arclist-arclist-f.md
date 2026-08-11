# ArcList

## Modules to Import

```TypeScript
import { ArcListItemAttribute, ArcList, ArcListItem, ArcListAttribute } from 'kits/@kit.ArkUI';
```

## ArcList

```TypeScript
export declare function ArcList(
    options?: ArkListOptions,
    content_?: CustomBuilder,
): ArcListAttribute
```

Defines ArcList Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare function ArcList(    options?: ArkListOptions,    content_?: CustomBuilder,): ArcListAttribute--><!--Device-unnamed-export declare function ArcList(    options?: ArkListOptions,    content_?: CustomBuilder,): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ArkListOptions](arkts-arkui-arkui-arclist-arklistoptions-i.md) | No |  |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |  |


## ArcList

```TypeScript
export declare function ArcList(
    style_: CustomBuilderT<ArcListAttribute>,
    content_?: CustomBuilder
): ArcListAttribute
```

Defines ArcList Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ArcList(    style_: CustomBuilderT<ArcListAttribute>,    content_?: CustomBuilder): ArcListAttribute--><!--Device-unnamed-export declare function ArcList(    style_: CustomBuilderT<ArcListAttribute>,    content_?: CustomBuilder): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;ArcListAttribute&gt; | Yes | The style to create an ArcList. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) | The attribute of the ArcList. |

