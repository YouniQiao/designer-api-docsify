# VideoAttribute

Defines the Video attribute.

**Inheritance/Implementation:** VideoAttribute extends [CommonMethod](CommonMethod)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface VideoAttribute extends CommonMethod--><!--Device-unnamed-export declare interface VideoAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## analyzerConfig

```TypeScript
default analyzerConfig(config: ImageAnalyzerConfig | undefined): this
```

Set image analyzer with config.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoAttribute-default analyzerConfig(config: ImageAnalyzerConfig | undefined): this--><!--Device-VideoAttribute-default analyzerConfig(config: ImageAnalyzerConfig | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [ImageAnalyzerConfig](arkts-arkui-imagecommon-imageanalyzerconfig-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<VideoAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Call attributeModifier.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoAttribute-default attributeModifier(modifier: AttributeModifier<VideoAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-VideoAttribute-default attributeModifier(modifier: AttributeModifier<VideoAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[VideoAttribute](arkts-arkui-video-videoattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## autoPlay

```TypeScript
default autoPlay(value: boolean | undefined): this
```

Called when judging whether the video is played automatically.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoAttribute-default autoPlay(value: boolean | undefined): this--><!--Device-VideoAttribute-default autoPlay(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## controls

```TypeScript
default controls(value: boolean | undefined): this
```

Called when judging whether the control bar is displayed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoAttribute-default controls(value: boolean | undefined): this--><!--Device-VideoAttribute-default controls(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## enableAnalyzer

```TypeScript
default enableAnalyzer(enable: boolean | undefined): this
```

Enable image analyzer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoAttribute-default enableAnalyzer(enable: boolean | undefined): this--><!--Device-VideoAttribute-default enableAnalyzer(enable: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## enableShortcutKey

```TypeScript
default enableShortcutKey(enabled: boolean | undefined): this
```

Indicates whether to response shortcut key. The default value is false.If the value is true, video will respond to the shortcut keys as follows:Space key: play/pause the video.Up/Down arrow key: turn up/down volume of the video.Right/Left arrow key: fast forward/backward the video.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoAttribute-default enableShortcutKey(enabled: boolean | undefined): this--><!--Device-VideoAttribute-default enableShortcutKey(enabled: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## loop

```TypeScript
default loop(value: boolean | undefined): this
```

Called when judging whether the video is played circular.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoAttribute-default loop(value: boolean | undefined): this--><!--Device-VideoAttribute-default loop(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## muted

```TypeScript
default muted(value: boolean | undefined): this
```

Called when judging whether the video is muted.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoAttribute-default muted(value: boolean | undefined): this--><!--Device-VideoAttribute-default muted(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## objectFit

```TypeScript
default objectFit(value: ImageFit | undefined): this
```

Called when determining the zoom type of the video source.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoAttribute-default objectFit(value: ImageFit | undefined): this--><!--Device-VideoAttribute-default objectFit(value: ImageFit | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ImageFit](arkts-arkui-imagefit-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onError

```TypeScript
default onError(event: VoidCallback | ErrorCallback | undefined): this
```

Called when playback fails.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoAttribute-default onError(event: VoidCallback | ErrorCallback | undefined): this--><!--Device-VideoAttribute-default onError(event: VoidCallback | ErrorCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-errorcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onFinish

```TypeScript
default onFinish(event: VoidCallback | undefined): this
```

Called when the video playback ends.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoAttribute-default onFinish(event: VoidCallback | undefined): this--><!--Device-VideoAttribute-default onFinish(event: VoidCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onFullscreenChange

```TypeScript
default onFullscreenChange(callback: Callback<FullscreenInfo> | undefined): this
```

Called when the video enters and exits the full screen.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoAttribute-default onFullscreenChange(callback: Callback<FullscreenInfo> | undefined): this--><!--Device-VideoAttribute-default onFullscreenChange(callback: Callback<FullscreenInfo> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[FullscreenInfo](arkts-arkui-video-fullscreeninfo-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onPause

```TypeScript
default onPause(event: VoidCallback | undefined): this
```

Called when the video is paused.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoAttribute-default onPause(event: VoidCallback | undefined): this--><!--Device-VideoAttribute-default onPause(event: VoidCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onPrepared

```TypeScript
default onPrepared(callback: Callback<PreparedInfo> | undefined): this
```

Called when the video preparation is complete.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoAttribute-default onPrepared(callback: Callback<PreparedInfo> | undefined): this--><!--Device-VideoAttribute-default onPrepared(callback: Callback<PreparedInfo> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[PreparedInfo](arkts-arkui-video-preparedinfo-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onSeeked

```TypeScript
default onSeeked(callback: Callback<PlaybackInfo> | undefined): this
```

Called when the playback time information is reported after the operation progress bar is completed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoAttribute-default onSeeked(callback: Callback<PlaybackInfo> | undefined): this--><!--Device-VideoAttribute-default onSeeked(callback: Callback<PlaybackInfo> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[PlaybackInfo](arkts-arkui-video-playbackinfo-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onSeeking

```TypeScript
default onSeeking(callback: Callback<PlaybackInfo> | undefined): this
```

Called when the time information is reported when the progress bar process is operated.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoAttribute-default onSeeking(callback: Callback<PlaybackInfo> | undefined): this--><!--Device-VideoAttribute-default onSeeking(callback: Callback<PlaybackInfo> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[PlaybackInfo](arkts-arkui-video-playbackinfo-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onStart

```TypeScript
default onStart(event: VoidCallback | undefined): this
```

Called when the video is played.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoAttribute-default onStart(event: VoidCallback | undefined): this--><!--Device-VideoAttribute-default onStart(event: VoidCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onStop

```TypeScript
default onStop(event: VoidCallback | undefined): this
```

Called when the video is stopped.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoAttribute-default onStop(event: VoidCallback | undefined): this--><!--Device-VideoAttribute-default onStop(event: VoidCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onUpdate

```TypeScript
default onUpdate(callback: Callback<PlaybackInfo> | undefined): this
```

Called when the playback progress changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoAttribute-default onUpdate(callback: Callback<PlaybackInfo> | undefined): this--><!--Device-VideoAttribute-default onUpdate(callback: Callback<PlaybackInfo> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[PlaybackInfo](arkts-arkui-video-playbackinfo-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setVideoOptions

```TypeScript
default setVideoOptions(value: VideoOptions): this
```

Set Video options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoAttribute-default setVideoOptions(value: VideoOptions): this--><!--Device-VideoAttribute-default setVideoOptions(value: VideoOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [VideoOptions](arkts-arkui-video-videooptions-i.md) | Yes | Video constructor options |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the VideoAttribute. |

