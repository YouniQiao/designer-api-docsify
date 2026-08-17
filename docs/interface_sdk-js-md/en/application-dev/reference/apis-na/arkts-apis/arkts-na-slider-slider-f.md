# Slider

## Slider

```TypeScript
@ComponentBuilder
export declare function Slider(
    options?: SliderOptions,
    content_?: CustomBuilder,
): SliderAttribute
```

Defines Slider Component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Slider(    options?: SliderOptions,    content_?: CustomBuilder,): SliderAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Slider(    options?: SliderOptions,    content_?: CustomBuilder,): SliderAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [SliderOptions](arkts-na-slider-slideroptions-i.md) | No | The options |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [SliderAttribute](arkts-na-slider-sliderattribute-i.md) |  |


## Slider

```TypeScript
@Builder
export declare function Slider(
    style_: CustomBuilderT<SliderAttribute>,
    content_?: CustomBuilder,
): SliderAttribute
```

Defines Slider Component.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Slider(    style_: CustomBuilderT<SliderAttribute>,    content_?: CustomBuilder,): SliderAttribute--><!--Device-unnamed-@Builderexport declare function Slider(    style_: CustomBuilderT<SliderAttribute>,    content_?: CustomBuilder,): SliderAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;[SliderAttribute](arkts-na-slider-sliderattribute-i.md)&gt; | Yes | slider attribute instance |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [SliderAttribute](arkts-na-slider-sliderattribute-i.md) |  |

