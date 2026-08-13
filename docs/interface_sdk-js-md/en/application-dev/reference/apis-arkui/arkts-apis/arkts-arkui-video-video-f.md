# Video

## Video

```TypeScript
@ComponentBuilder
export declare function Video(
    value: VideoOptions
): VideoAttribute
```

Video is returned when the parameter is transferred.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Video(    value: VideoOptions): VideoAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Video(    value: VideoOptions): VideoAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [VideoOptions](arkts-arkui-video-videooptions-i.md) | Yes | The options to create a Video. |

**Return value:**

| Type | Description |
| --- | --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) | The attribute of the Video. |


## Video

```TypeScript
@Builder
export declare function Video(
    style: CustomBuilderT<VideoAttribute>
): VideoAttribute
```

Defines Video Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Video(    style: CustomBuilderT<VideoAttribute>): VideoAttribute--><!--Device-unnamed-@Builderexport declare function Video(    style: CustomBuilderT<VideoAttribute>): VideoAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | CustomBuilderT&lt;[VideoAttribute](arkts-arkui-video-videoattribute-i.md)&gt; | Yes | the callback to set up component's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |  |

