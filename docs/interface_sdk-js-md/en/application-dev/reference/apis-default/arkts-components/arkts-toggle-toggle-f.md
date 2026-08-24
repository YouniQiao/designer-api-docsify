# Toggle

## Toggle

```TypeScript
@ComponentBuilder
export declare function Toggle(
    options: ToggleOptions,
    content_?: CustomBuilder,
): ToggleAttribute
```

Defines Toggle Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @ComponentBuilder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Toggle(    options: ToggleOptions,    content_?: CustomBuilder,): ToggleAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Toggle(    options: ToggleOptions,    content_?: CustomBuilder,): ToggleAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToggleOptions](arkts-toggle-toggleoptions-i.md) | Yes | the options of Toggle. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ToggleAttribute](arkts-toggle-attribute.md) |  |


## Toggle

```TypeScript
@Builder
export declare function Toggle(
    style_: CustomBuilderT<ToggleAttribute>,
    content_?: CustomBuilder,
): ToggleAttribute
```

Defines Toggle Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Toggle(    style_: CustomBuilderT<ToggleAttribute>,    content_?: CustomBuilder,): ToggleAttribute--><!--Device-unnamed-@Builderexport declare function Toggle(    style_: CustomBuilderT<ToggleAttribute>,    content_?: CustomBuilder,): ToggleAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[ToggleAttribute](arkts-toggle-attribute.md)&gt; | Yes | toggle attribute instance |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ToggleAttribute](arkts-toggle-attribute.md) |  |

