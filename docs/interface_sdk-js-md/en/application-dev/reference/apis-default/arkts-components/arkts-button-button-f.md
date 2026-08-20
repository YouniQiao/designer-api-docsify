# Button

## Button

```TypeScript
@ComponentBuilder
export declare function Button(
    label: ResourceStr, options?: ButtonOptions, 
    content_?: CustomBuilder,
): ButtonAttribute
```

Defines Button Component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Button(    label: ResourceStr, options?: ButtonOptions,     content_?: CustomBuilder,): ButtonAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Button(    label: ResourceStr, options?: ButtonOptions,     content_?: CustomBuilder,): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| label | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) | Yes | the label of Button. |
| options | [ButtonOptions](arkts-button-buttonoptions-i.md) | No | the options of Button. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ButtonAttribute](arkts-button-attribute.md) |  |


## Button

```TypeScript
@ComponentBuilder
export declare function Button(
    options?: ButtonOptions,
    content_?: CustomBuilder,
): ButtonAttribute
```

Defines Button Component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Button(    options?: ButtonOptions,    content_?: CustomBuilder,): ButtonAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Button(    options?: ButtonOptions,    content_?: CustomBuilder,): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ButtonOptions](arkts-button-buttonoptions-i.md) | No | the options of Button. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ButtonAttribute](arkts-button-attribute.md) |  |


## Button

```TypeScript
@Builder
export declare function Button(
    style_: CustomBuilderT<ButtonAttribute>,
    content_?: CustomBuilder,
): ButtonAttribute
```

Defines Button Component.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Button(    style_: CustomBuilderT<ButtonAttribute>,    content_?: CustomBuilder,): ButtonAttribute--><!--Device-unnamed-@Builderexport declare function Button(    style_: CustomBuilderT<ButtonAttribute>,    content_?: CustomBuilder,): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[ButtonAttribute](arkts-button-attribute.md)&gt; | Yes | button attribute instance |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ButtonAttribute](arkts-button-attribute.md) |  |

