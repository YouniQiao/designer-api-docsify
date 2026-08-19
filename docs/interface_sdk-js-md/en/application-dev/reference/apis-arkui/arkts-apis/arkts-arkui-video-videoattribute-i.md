# VideoAttribute

Defines the Video attribute.

**Inheritance/Implementation:** VideoAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface VideoAttribute--><!--Device-unnamed-export declare interface VideoAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## analyzerConfig

```TypeScript
analyzerConfig(config: ImageAnalyzerConfig | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-VideoAttribute-analyzerConfig(config: ImageAnalyzerConfig | undefined): this--><!--Device-VideoAttribute-analyzerConfig(config: ImageAnalyzerConfig | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [ImageAnalyzerConfig](../../apis-na/arkts-apis/arkts-na-imagecommon-imageanalyzerconfig-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<VideoAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-VideoAttribute-attributeModifier(modifier: AttributeModifier<VideoAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-VideoAttribute-attributeModifier(modifier: AttributeModifier<VideoAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[VideoAttribute](arkts-arkui-video-videoattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## autoPlay

```TypeScript
autoPlay(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-VideoAttribute-autoPlay(value: boolean | undefined): this--><!--Device-VideoAttribute-autoPlay(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## controls

```TypeScript
controls(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-VideoAttribute-controls(value: boolean | undefined): this--><!--Device-VideoAttribute-controls(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableAnalyzer

```TypeScript
enableAnalyzer(enable: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-VideoAttribute-enableAnalyzer(enable: boolean | undefined): this--><!--Device-VideoAttribute-enableAnalyzer(enable: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableShortcutKey

```TypeScript
enableShortcutKey(enabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-VideoAttribute-enableShortcutKey(enabled: boolean | undefined): this--><!--Device-VideoAttribute-enableShortcutKey(enabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## loop

```TypeScript
loop(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-VideoAttribute-loop(value: boolean | undefined): this--><!--Device-VideoAttribute-loop(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## muted

```TypeScript
muted(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-VideoAttribute-muted(value: boolean | undefined): this--><!--Device-VideoAttribute-muted(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## objectFit

```TypeScript
objectFit(value: ImageFit | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-VideoAttribute-objectFit(value: ImageFit | undefined): this--><!--Device-VideoAttribute-objectFit(value: ImageFit | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ImageFit](arkts-arkui-imagefit-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onError

```TypeScript
onError(event: VoidCallback | ErrorCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-VideoAttribute-onError(event: VoidCallback | ErrorCallback | undefined): this--><!--Device-VideoAttribute-onError(event: VoidCallback | ErrorCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-errorcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onFinish

```TypeScript
onFinish(event: VoidCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-VideoAttribute-onFinish(event: VoidCallback | undefined): this--><!--Device-VideoAttribute-onFinish(event: VoidCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onFullscreenChange

```TypeScript
onFullscreenChange(callback: Callback<FullscreenInfo> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-VideoAttribute-onFullscreenChange(callback: Callback<FullscreenInfo> | undefined): this--><!--Device-VideoAttribute-onFullscreenChange(callback: Callback<FullscreenInfo> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[FullscreenInfo](arkts-arkui-video-fullscreeninfo-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onPause

```TypeScript
onPause(event: VoidCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-VideoAttribute-onPause(event: VoidCallback | undefined): this--><!--Device-VideoAttribute-onPause(event: VoidCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onPrepared

```TypeScript
onPrepared(callback: Callback<PreparedInfo> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-VideoAttribute-onPrepared(callback: Callback<PreparedInfo> | undefined): this--><!--Device-VideoAttribute-onPrepared(callback: Callback<PreparedInfo> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[PreparedInfo](arkts-arkui-video-preparedinfo-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onSeeked

```TypeScript
onSeeked(callback: Callback<PlaybackInfo> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-VideoAttribute-onSeeked(callback: Callback<PlaybackInfo> | undefined): this--><!--Device-VideoAttribute-onSeeked(callback: Callback<PlaybackInfo> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[PlaybackInfo](arkts-arkui-video-playbackinfo-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onSeeking

```TypeScript
onSeeking(callback: Callback<PlaybackInfo> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-VideoAttribute-onSeeking(callback: Callback<PlaybackInfo> | undefined): this--><!--Device-VideoAttribute-onSeeking(callback: Callback<PlaybackInfo> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[PlaybackInfo](arkts-arkui-video-playbackinfo-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onStart

```TypeScript
onStart(event: VoidCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-VideoAttribute-onStart(event: VoidCallback | undefined): this--><!--Device-VideoAttribute-onStart(event: VoidCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onStop

```TypeScript
onStop(event: VoidCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-VideoAttribute-onStop(event: VoidCallback | undefined): this--><!--Device-VideoAttribute-onStop(event: VoidCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onUpdate

```TypeScript
onUpdate(callback: Callback<PlaybackInfo> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-VideoAttribute-onUpdate(callback: Callback<PlaybackInfo> | undefined): this--><!--Device-VideoAttribute-onUpdate(callback: Callback<PlaybackInfo> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[PlaybackInfo](arkts-arkui-video-playbackinfo-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setVideoOptions

```TypeScript
setVideoOptions(value: VideoOptions): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-VideoAttribute-setVideoOptions(value: VideoOptions): this--><!--Device-VideoAttribute-setVideoOptions(value: VideoOptions): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [VideoOptions](arkts-arkui-video-videooptions-i.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## surfaceBackgroundColor

```TypeScript
surfaceBackgroundColor(color: ColorMetrics | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-VideoAttribute-surfaceBackgroundColor(color: ColorMetrics | undefined): this--><!--Device-VideoAttribute-surfaceBackgroundColor(color: ColorMetrics | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [ColorMetrics](arkts-arkui-colormetrics-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## default

```TypeScript
default
```

Call attributeModifier.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VideoAttribute-default--><!--Device-VideoAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

