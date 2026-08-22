# Radio

## Radio

```TypeScript
@ComponentBuilder
export declare function Radio(
    options: RadioOptions,
    content_?: CustomBuilder,
): RadioAttribute
```

Defines Radio Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Radio(    options: RadioOptions,    content_?: CustomBuilder,): RadioAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Radio(    options: RadioOptions,    content_?: CustomBuilder,): RadioAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RadioOptions](arkts-radio-radiooptions-i.md) | Yes | the options of Radio. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [RadioAttribute](arkts-radio-attribute.md) |  |


## Radio

```TypeScript
@Builder
export declare function Radio(
    style_: CustomBuilderT<RadioAttribute>,
    content_?: CustomBuilder,
): RadioAttribute
```

Defines Radio Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Radio(    style_: CustomBuilderT<RadioAttribute>,    content_?: CustomBuilder,): RadioAttribute--><!--Device-unnamed-@Builderexport declare function Radio(    style_: CustomBuilderT<RadioAttribute>,    content_?: CustomBuilder,): RadioAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[RadioAttribute](arkts-radio-attribute.md)&gt; | Yes | radio attribute instance |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [RadioAttribute](arkts-radio-attribute.md) |  |

