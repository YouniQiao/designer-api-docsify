# Text

## Text

```TypeScript
@Builder
export declare function Text(
    style: CustomBuilderT<TextAttribute>,
    content_?: CustomBuilder,
): TextAttribute
```

Defines Text Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Text(    style: CustomBuilderT<TextAttribute>,    content_?: CustomBuilder,): TextAttribute--><!--Device-unnamed-@Builderexport declare function Text(    style: CustomBuilderT<TextAttribute>,    content_?: CustomBuilder,): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;[TextAttribute](arkts-arkui-text-attribute.md)&gt; | Yes | Text attribute instance. |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No | content. |

**Return value:**

| Type | Description |
| --- | --- |
| [TextAttribute](arkts-arkui-text-attribute.md) |  |


## Text

```TypeScript
@ComponentBuilder
export declare function Text(
    content?: string | Resource, value?: TextOptions, 
    content_?: CustomBuilder,
): TextAttribute
```

Defines Text Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @ComponentBuilder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Text(    content?: string | Resource, value?: TextOptions,     content_?: CustomBuilder,): TextAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Text(    content?: string | Resource, value?: TextOptions,     content_?: CustomBuilder,): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | string \| [Resource](../arkts-apis/arkts-arkui-resource-t.md) | No |  |
| value | [TextOptions](arkts-arkui-text-textoptions-i.md) | No |  |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [TextAttribute](arkts-arkui-text-attribute.md) |  |

