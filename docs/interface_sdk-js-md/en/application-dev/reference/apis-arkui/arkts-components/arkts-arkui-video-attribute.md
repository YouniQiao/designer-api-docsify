# Video properties/events

In addition to the [universal attributes](arkts-arkui-commonmethod-c.md), the following attributes are supported.

In addition to the [universal events](arkts-arkui-commonmethod-c.md), the following events are supported.

**Inheritance/Implementation:** VideoAttribute extends CommonMethod<VideoAttribute>

**Since:** 7

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## analyzerConfig

```TypeScript
analyzerConfig(config: ImageAnalyzerConfig)
```

Sets the AI image analysis types, including subject recognition, text recognition, and object lookup. This attribute can be dynamically set using attributeModifier.

> **NOTE：**
> 
> This API can be called within attributeModifier since API version 20.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [ImageAnalyzerConfig](../arkts-apis/arkts-arkui-imageanalyzerconfig-i.md) | Yes | AI image analysis types. |

## autoPlay

```TypeScript
autoPlay(value: boolean)
```

Sets whether to enable autoplay. This attribute can be dynamically set using attributeModifier.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | Whether to enable autoplay.   **true**: Enable autoplay.   **false**: Disable autoplay.Default value: **false**. |

## controls

```TypeScript
controls(value: boolean)
```

Sets whether to display the video playback control bar. This attribute can be dynamically set using attributeModifier.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | Whether to display the video playback control bar.   **true**: Display the video playback control bar.   **false**: Do not display the video playback control bar.Default value: **true |

## enableAnalyzer

```TypeScript
enableAnalyzer(enable: boolean)
```

Sets whether to enable the AI image analyzer, which supports subject recognition, text recognition, and object lookup. This attribute can be dynamically set using attributeModifier.

After this feature is enabled, the video automatically enters an analysis state to process the current frame when playback is paused, and exits the analysis state when playback is resumed.

Note that if this attribute and the overlay attribute are both set, [CustomBuilder](arkts-arkui-custombuilder-t.md) specified in [overlay](arkts-arkui-commonmethod-c.md) has no effect.

> **NOTE：**
> 
> This API can be called within attributeModifier since API version 20.

After this feature is enabled, the video automatically enters an analysis state to process the current frame when playback is paused, and exits the analysis state when playback is resumed.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | Whether to enable the AI image analyzer.   **true**: Enable the AI image analyzer. **false**: Disable the AI image analyzer.Default value: **false |

## enableShortcutKey

```TypeScript
enableShortcutKey(enabled: boolean)
```

Sets whether the component responds to keyboard shortcuts when it has focus. This attribute can be dynamically set using attributeModifier.

Currently, the component can respond to the following keys when it is in focus: spacebar for playing or pausing the video, up or down arrow key for adjusting the video volume, and left or right arrow key for fast forwarding or rewinding the video.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Whether the component responds to keyboard shortcuts when it has focus.   **true**: The component responds to keyboard shortcuts when it has focus.   **false**: The component does not respond to keyboard shortcuts when it has focus.Default value: **false**. |

## loop

```TypeScript
loop(value: boolean)
```

Sets whether to repeat the video. This attribute can be dynamically set using attributeModifier.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | Whether to repeat the video.   **true**: Repeat the video.   **false**: Do not repeat the video.Default value: **false**. |

## muted

```TypeScript
muted(value: boolean)
```

Sets whether to mute the video. This attribute can be dynamically set using attributeModifier.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | Whether to mute the video.   **true**: Mute the video.   **false**: Unmute the video.Default value: **false**. |

## objectFit

```TypeScript
objectFit(value: ImageFit)
```

Sets the fill mode for the video content. This attribute can be dynamically set using attributeModifier.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ImageFit](../arkts-apis/arkts-arkui-imagefit-e.md) | Yes | Fill mode of the video content.Default value: **Cover**Constraints: The enumerated value **Matrix** in **ImageFit** is not supported and will behave as **Cover**.Invalid values, including **undefined**, **null**, and values outside the [ImageFit](../arkts-apis/arkts-arkui-imagefit-e.md) enumeration range, will result in an effect the same as **Cover**. |

## onError

```TypeScript
onError(event: VoidCallback | import('../api/@ohos.base').ErrorCallback)
```

Called when playback fails.

**Since:** 7

**Decorator:** @ohos

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](../arkts-apis/arkts-arkui-voidcallback-t.md) \| import('../api/@ohos.base').ErrorCallback | Yes | [since 7 - 19] |

## onFinish

```TypeScript
onFinish(event: VoidCallback)
```

Called when the video playback ends. Anonymous Object Rectification.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](../arkts-apis/arkts-arkui-voidcallback-t.md) | Yes | [since 7 - 17] |

## onFullscreenChange

```TypeScript
onFullscreenChange(callback: Callback<FullscreenInfo>)
```

Called when the video enters and exits the full screen. Anonymous Object Rectification.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[FullscreenInfo](arkts-arkui-fullscreeninfo-i.md)&gt; | Yes | [since 7 - 17] |

## onPause

```TypeScript
onPause(event: VoidCallback)
```

Called when the video is paused. Anonymous Object Rectification.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](../arkts-apis/arkts-arkui-voidcallback-t.md) | Yes | [since 7 - 17] |

## onPrepared

```TypeScript
onPrepared(callback: Callback<PreparedInfo>)
```

Called when the video preparation is complete. Anonymous Object Rectification.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[PreparedInfo](arkts-arkui-preparedinfo-i.md)&gt; | Yes | [since 7 - 17] |

## onSeeked

```TypeScript
onSeeked(callback: Callback<PlaybackInfo>)
```

Called when the playback time information is reported after the operation progress bar is completed. Anonymous Object Rectification.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[PlaybackInfo](arkts-arkui-playbackinfo-i.md)&gt; | Yes | [since 7 - 17] |

## onSeeking

```TypeScript
onSeeking(callback: Callback<PlaybackInfo>)
```

Called when the time information is reported when the progress bar process is operated. Anonymous Object Rectification.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[PlaybackInfo](arkts-arkui-playbackinfo-i.md)&gt; | Yes | [since 7 - 17] |

## onStart

```TypeScript
onStart(event: VoidCallback)
```

Called when the video is played. Anonymous Object Rectification.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](../arkts-apis/arkts-arkui-voidcallback-t.md) | Yes | [since 7 - 17] |

## onStop

```TypeScript
onStop(event: Callback<void>)
```

Called when the video is stopped.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | Callback&lt;void&gt; | Yes |  |

## onUpdate

```TypeScript
onUpdate(callback: Callback<PlaybackInfo>)
```

Called when the playback progress changes. Anonymous Object Rectification.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[PlaybackInfo](arkts-arkui-playbackinfo-i.md)&gt; | Yes | [since 7 - 17] |
