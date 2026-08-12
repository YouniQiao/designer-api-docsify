# ArcScrollBar

## Modules to Import

```TypeScript
import { ArcScrollBarAttribute, ArcScrollBar } from '@kit.ArkUI';
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
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcScrollBarAttribute](arkts-arkui-arkui-arcscrollbar-arcscrollbarattribute-i.md) |  |


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
| style_ | CustomBuilderT&lt;[ArcScrollBarAttribute](arkts-arkui-arkui-arcscrollbar-arcscrollbarattribute-i.md)&gt; | Yes | The style to create an ArcScrollBar. |
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcScrollBarAttribute](arkts-arkui-arkui-arcscrollbar-arcscrollbarattribute-i.md) | The attribute of the ArcScrollBar. |

