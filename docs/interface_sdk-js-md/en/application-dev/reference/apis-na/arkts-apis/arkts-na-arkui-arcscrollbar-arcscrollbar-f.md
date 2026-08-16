# ArcScrollBar

## ArcScrollBar

```TypeScript
@ComponentBuilder
export declare function ArcScrollBar(
    options: ArcScrollBarOptions,
    content_?: CustomBuilder,
): ArcScrollBarAttribute
```

Defines ArcScrollBar Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-@ComponentBuilderexport declare function ArcScrollBar(    options: ArcScrollBarOptions,    content_?: CustomBuilder,): ArcScrollBarAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function ArcScrollBar(    options: ArcScrollBarOptions,    content_?: CustomBuilder,): ArcScrollBarAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ArcScrollBarOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-arcscrollbar-arcscrollbaroptions-i.md) | Yes |  |
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| ArcScrollBarAttribute |  |


## ArcScrollBar

```TypeScript
@Builder
export declare function ArcScrollBar(
    style_: CustomBuilderT<ArcScrollBarAttribute>,
    content_?: CustomBuilder
): ArcScrollBarAttribute
```

Defines ArcScrollBar Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function ArcScrollBar(    style_: CustomBuilderT<ArcScrollBarAttribute>,    content_?: CustomBuilder): ArcScrollBarAttribute--><!--Device-unnamed-@Builderexport declare function ArcScrollBar(    style_: CustomBuilderT<ArcScrollBarAttribute>,    content_?: CustomBuilder): ArcScrollBarAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;ArcScrollBarAttribute&gt; | Yes | The style to create an ArcScrollBar. |
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| ArcScrollBarAttribute | The attribute of the ArcScrollBar. |

