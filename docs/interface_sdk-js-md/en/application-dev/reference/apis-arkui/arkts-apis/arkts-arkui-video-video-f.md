# Video

## Video

```TypeScript
export declare function Video(
    value: VideoOptions
): VideoAttribute
```

用于播放视频文件并控制其播放状态的组件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Video(    value: VideoOptions): VideoAttribute--><!--Device-unnamed-export declare function Video(    value: VideoOptions): VideoAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [VideoOptions](../arkts-components/arkts-arkui-videooptions-i.md) | Yes | 视频信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) | The attribute of the Video. |


## Video

```TypeScript
export declare function Video(
    style: CustomBuilderT<VideoAttribute>
): VideoAttribute
```

Defines Video Component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Video(    style: CustomBuilderT<VideoAttribute>): VideoAttribute--><!--Device-unnamed-export declare function Video(    style: CustomBuilderT<VideoAttribute>): VideoAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;VideoAttribute&gt; | Yes | the callback to set up component's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [VideoAttribute](arkts-arkui-video-videoattribute-i.md) |  |

