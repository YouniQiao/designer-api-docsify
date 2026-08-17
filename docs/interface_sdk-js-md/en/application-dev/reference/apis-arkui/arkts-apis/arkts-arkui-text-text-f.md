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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Text(    style: CustomBuilderT<TextAttribute>,    content_?: CustomBuilder,): TextAttribute--><!--Device-unnamed-@Builderexport declare function Text(    style: CustomBuilderT<TextAttribute>,    content_?: CustomBuilder,): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | CustomBuilderT&lt;TextAttribute&gt; | Yes | Text attribute instance. |
| content_ | CustomBuilder | No | content. |

**Return value:**

| Type | Description |
| --- | --- |
| TextAttribute |  |


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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Text(    content?: string | Resource, value?: TextOptions,     content_?: CustomBuilder,): TextAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Text(    content?: string | Resource, value?: TextOptions,     content_?: CustomBuilder,): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | string \| [Resource](arkts-arkui-resource-t.md) | No |  |
| value | [TextOptions](arkts-arkui-text-textoptions-i.md) | No |  |
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| TextAttribute |  |

