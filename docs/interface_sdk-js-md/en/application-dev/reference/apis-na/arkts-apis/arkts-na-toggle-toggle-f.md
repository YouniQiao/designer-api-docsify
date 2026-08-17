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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Toggle(    options: ToggleOptions,    content_?: CustomBuilder,): ToggleAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Toggle(    options: ToggleOptions,    content_?: CustomBuilder,): ToggleAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToggleOptions](arkts-na-toggle-toggleoptions-i.md) | Yes | the options of Toggle. |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ToggleAttribute](arkts-na-toggle-toggleattribute-i.md) |  |


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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Toggle(    style_: CustomBuilderT<ToggleAttribute>,    content_?: CustomBuilder,): ToggleAttribute--><!--Device-unnamed-@Builderexport declare function Toggle(    style_: CustomBuilderT<ToggleAttribute>,    content_?: CustomBuilder,): ToggleAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;[ToggleAttribute](arkts-na-toggle-toggleattribute-i.md)&gt; | Yes | toggle attribute instance |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ToggleAttribute](arkts-na-toggle-toggleattribute-i.md) |  |

