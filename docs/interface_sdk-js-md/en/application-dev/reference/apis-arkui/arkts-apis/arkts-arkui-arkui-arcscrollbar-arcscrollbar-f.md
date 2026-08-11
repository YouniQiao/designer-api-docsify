# ArcScrollBar

## Modules to Import

```TypeScript
import { ArcScrollBarAttribute, ArcScrollBar } from 'kits/@kit.ArkUI';
```

## ArcScrollBar

```TypeScript
export declare function ArcScrollBar(
    options: ArcScrollBarOptions,
    content_?: CustomBuilder,
): ArcScrollBarAttribute
```

Defines ArcScrollBar Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare function ArcScrollBar(    options: ArcScrollBarOptions,    content_?: CustomBuilder,): ArcScrollBarAttribute--><!--Device-unnamed-export declare function ArcScrollBar(    options: ArcScrollBarOptions,    content_?: CustomBuilder,): ArcScrollBarAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ArcScrollBarOptions](arkts-arkui-arkui-arcscrollbar-arcscrollbaroptions-i.md) | Yes |  |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcScrollBarAttribute](arkts-arkui-arkui-arcscrollbar-arcscrollbarattribute-c.md) |  |


## ArcScrollBar

```TypeScript
export declare function ArcScrollBar(
    style_: CustomBuilderT<ArcScrollBarAttribute>,
    content_?: CustomBuilder
): ArcScrollBarAttribute
```

Defines ArcScrollBar Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ArcScrollBar(    style_: CustomBuilderT<ArcScrollBarAttribute>,    content_?: CustomBuilder): ArcScrollBarAttribute--><!--Device-unnamed-export declare function ArcScrollBar(    style_: CustomBuilderT<ArcScrollBarAttribute>,    content_?: CustomBuilder): ArcScrollBarAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;ArcScrollBarAttribute&gt; | Yes | The style to create an ArcScrollBar. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcScrollBarAttribute](arkts-arkui-arkui-arcscrollbar-arcscrollbarattribute-c.md) | The attribute of the ArcScrollBar. |

