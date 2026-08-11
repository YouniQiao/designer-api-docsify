# Button

## Button

```TypeScript
export declare function Button(
    label: ResourceStr, options?: ButtonOptions, 
    content_?: CustomBuilder,
): ButtonAttribute
```

Defines Button Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Button(    label: ResourceStr, options?: ButtonOptions,     content_?: CustomBuilder,): ButtonAttribute--><!--Device-unnamed-export declare function Button(    label: ResourceStr, options?: ButtonOptions,     content_?: CustomBuilder,): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| label | [ResourceStr](arkts-arkui-resourcestr-t.md) | Yes | the label of Button. |
| options | [ButtonOptions](arkts-arkui-button-buttonoptions-i.md) | No | the options of Button. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ButtonAttribute](../arkts-components/arkts-arkui-button-attribute.md) |  |


## Button

```TypeScript
export declare function Button(
    options?: ButtonOptions,
    content_?: CustomBuilder,
): ButtonAttribute
```

Defines Button Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Button(    options?: ButtonOptions,    content_?: CustomBuilder,): ButtonAttribute--><!--Device-unnamed-export declare function Button(    options?: ButtonOptions,    content_?: CustomBuilder,): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ButtonOptions](arkts-arkui-button-buttonoptions-i.md) | No | the options of Button. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ButtonAttribute](../arkts-components/arkts-arkui-button-attribute.md) |  |


## Button

```TypeScript
export declare function Button(
    style_: CustomBuilderT<ButtonAttribute>,
    content_?: CustomBuilder,
): ButtonAttribute
```

Defines Button Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Button(    style_: CustomBuilderT<ButtonAttribute>,    content_?: CustomBuilder,): ButtonAttribute--><!--Device-unnamed-export declare function Button(    style_: CustomBuilderT<ButtonAttribute>,    content_?: CustomBuilder,): ButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;ButtonAttribute&gt; | Yes | button attribute instance |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ButtonAttribute](../arkts-components/arkts-arkui-button-attribute.md) |  |

