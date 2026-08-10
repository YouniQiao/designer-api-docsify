# AVCastController

在投播建立后，调用[avSession.getAVCastController](arkts-avsession-avsession-getavcastcontroller-f-sys.md#getavcastcontroller)后，返回会话控制器实例。控制器可查看会话ID，并可完成对会话发送命令及事件，获取会话元数据，播放状态信息等操作。

> **说明：**
> 
> - 本Interface首批接口从API version 10开始支持。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-avSession-interface AVCastController--><!--Device-avSession-interface AVCastController-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## getAVPlaybackState

```TypeScript
getAVPlaybackState(callback: AsyncCallback<AVPlaybackState>): void
```

获取当前的远端播放状态。结果通过callback异步回调方式返回。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-AVCastController-getAVPlaybackState(callback: AsyncCallback<AVPlaybackState>): void--><!--Device-AVCastController-getAVPlaybackState(callback: AsyncCallback<AVPlaybackState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AVPlaybackState&gt; | Yes | 回调函数，返回远端播放状态。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## getAVPlaybackState

```TypeScript
getAVPlaybackState(): Promise<AVPlaybackState>
```

获取当前的远端播放状态。结果通过Promise异步回调方式返回。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-getAVPlaybackState(): Promise<AVPlaybackState>--><!--Device-AVCastController-getAVPlaybackState(): Promise<AVPlaybackState>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AVPlaybackState&gt; | Promise对象。返回远端播放状态。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## getCurrentItem

```TypeScript
getCurrentItem(callback: AsyncCallback<AVQueueItem>): void
```

获取当前投播的资源信息。结果通过callback异步回调方式返回。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-AVCastController-getCurrentItem(callback: AsyncCallback<AVQueueItem>): void--><!--Device-AVCastController-getCurrentItem(callback: AsyncCallback<AVQueueItem>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AVQueueItem&gt; | Yes | 回调函数。当命令发送成功，err为undefined，否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## getCurrentItem

```TypeScript
getCurrentItem(): Promise<AVQueueItem>
```

获取当前投播的资源信息。结果通过Promise异步回调方式返回。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-getCurrentItem(): Promise<AVQueueItem>--><!--Device-AVCastController-getCurrentItem(): Promise<AVQueueItem>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AVQueueItem&gt; | Promise对象，返回当前的播放资源，否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## getRecommendedResolutionLevel

```TypeScript
getRecommendedResolutionLevel(decoderType: DecoderType): Promise<ResolutionLevel>
```

通过传递解码方式，获取推荐的分辨率。使用Promise异步回调。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AVCastController-getRecommendedResolutionLevel(decoderType: DecoderType): Promise<ResolutionLevel>--><!--Device-AVCastController-getRecommendedResolutionLevel(decoderType: DecoderType): Promise<ResolutionLevel>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| decoderType | [DecoderType](arkts-avsession-avsession-decodertype-e.md) | Yes | 设备所支持的解码格式。 &lt;br&gt;设备所支持的解码格式包括： &lt;br&gt;'OH_AVCODEC_MIMETYPE_VIDEO_AVC'：VIDEO AVC， &lt;br&gt;'OH_AVCODEC_MIMETYPE_VIDEO_HEVC'：VIDEO HEVC， &lt;br&gt;'OH_AVCODEC_MIMETYPE_AUDIO_VIVID'：AUDIO AV3A。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ResolutionLevel&gt; | Promise对象。返回远端设备推荐的分辨率。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## getSupportedDecoders

```TypeScript
getSupportedDecoders(): Promise<Array<DecoderType>>
```

获取当前远端设备的解码方式。使用Promise异步回调。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AVCastController-getSupportedDecoders(): Promise<Array<DecoderType>>--><!--Device-AVCastController-getSupportedDecoders(): Promise<Array<DecoderType>>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;DecoderType&gt;&gt; | Promise对象。返回远端设备所支持的解码能力列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## getSupportedHdrCapabilities

```TypeScript
getSupportedHdrCapabilities(): Promise<Array<hdrCapability.HDRFormat>>
```

获取当前的远端设备所支持的HDR能力。使用Promise异步回调。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AVCastController-getSupportedHdrCapabilities(): Promise<Array<hdrCapability.HDRFormat>>--><!--Device-AVCastController-getSupportedHdrCapabilities(): Promise<Array<hdrCapability.HDRFormat>>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;hdrCapability.HDRFormat&gt;&gt; | Promise对象。返回远端设备所支持的HDR能力。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## getSupportedPlaySpeeds

ArkTS-Dyn:
```TypeScript
getSupportedPlaySpeeds(): Promise<Array<number>>
```

ArkTS-Sta:
```TypeScript
getSupportedPlaySpeeds(): Promise<Array<double>>
```

获取当前的远端设备所支持倍速播放列表，仅支持使用cast+协议连接的设备。使用Promise异步回调。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AVCastController-getSupportedPlaySpeeds(): Promise<Array<double>>--><!--Device-AVCastController-getSupportedPlaySpeeds(): Promise<Array<double>>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;Array&lt;number&gt;&gt;  <br>ArkTS-Sta：Promise&lt;Array&lt;double&gt;&gt; | Promise对象。返回远端设备所支持的倍速播放列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## getValidCommands

```TypeScript
getValidCommands(callback: AsyncCallback<Array<AVCastControlCommandType>>): void
```

获取当前支持的命令。结果通过callback异步回调方式返回。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AVCastController-getValidCommands(callback: AsyncCallback<Array<AVCastControlCommandType>>): void--><!--Device-AVCastController-getValidCommands(callback: AsyncCallback<Array<AVCastControlCommandType>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;AVCastControlCommandType&gt;&gt; | Yes | 回调函数。返回当前支持的命令。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception. |

## getValidCommands

```TypeScript
getValidCommands(): Promise<Array<AVCastControlCommandType>>
```

获取当前支持的命令。结果通过Promise异步回调方式返回。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AVCastController-getValidCommands(): Promise<Array<AVCastControlCommandType>>--><!--Device-AVCastController-getValidCommands(): Promise<Array<AVCastControlCommandType>>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;AVCastControlCommandType&gt;&gt; | Promise对象，返回当前支持的命令。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception. |

## off('playbackStateChange')

```TypeScript
off(type: 'playbackStateChange', callback?: (state: AVPlaybackState) => void): void
```

取消播放状态变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-off(type: 'playbackStateChange', callback?: (state: AVPlaybackState) => void): void--><!--Device-AVCastController-off(type: 'playbackStateChange', callback?: (state: AVPlaybackState) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'playbackStateChange' | Yes |  |
| callback | (state: AVPlaybackState) =&gt; void | No | 回调函数，参数state是变化后的播放状态。 &lt;br&gt;该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception |

## off('mediaItemChange')

```TypeScript
off(type: 'mediaItemChange'): void
```

取消设置投播当前播放媒体内容事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-off(type: 'mediaItemChange'): void--><!--Device-AVCastController-off(type: 'mediaItemChange'): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'mediaItemChange' | Yes | 取消对应的监听事件，支持事件`'mediaItemChange'`。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception |

## off('playNext')

```TypeScript
off(type: 'playNext'): void
```

取消设置播放下一首资源事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-off(type: 'playNext'): void--><!--Device-AVCastController-off(type: 'playNext'): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'playNext' | Yes | 取消对应的监听事件，支持事件`'playNext'`。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception |

## off('playPrevious')

```TypeScript
off(type: 'playPrevious'): void
```

取消设置播放上一首资源事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-off(type: 'playPrevious'): void--><!--Device-AVCastController-off(type: 'playPrevious'): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'playPrevious' | Yes | 取消对应的监听事件，支持事件`'playPrevious'`。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception |

## off('requestPlay')

```TypeScript
off(type: 'requestPlay', callback?: Callback<AVQueueItem>): void
```

取消设置请求播放事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-AVCastController-off(type: 'requestPlay', callback?: Callback<AVQueueItem>): void--><!--Device-AVCastController-off(type: 'requestPlay', callback?: Callback<AVQueueItem>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'requestPlay' | Yes | 取消对应的监听事件，支持事件`'requestPlay'`。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AVQueueItem&gt; | No | 回调函数，参数AVQueueItem是当前正在播放的媒体内容。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可 选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception |

## off('endOfStream')

```TypeScript
off(type: 'endOfStream', callback?: Callback<void>): void
```

取消设置播放结束事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-AVCastController-off(type: 'endOfStream', callback?: Callback<void>): void--><!--Device-AVCastController-off(type: 'endOfStream', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'endOfStream' | Yes | 取消对应的监听事件，支持事件`'endOfStream'`。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception |

## off('seekDone')

```TypeScript
off(type: 'seekDone'): void
```

取消设置seek结束事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-off(type: 'seekDone'): void--><!--Device-AVCastController-off(type: 'seekDone'): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'seekDone' | Yes | 取消对应的监听事件，支持事件`'seekDone'`。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception |

## off('validCommandChange')

```TypeScript
off(type: 'validCommandChange', callback?: Callback<Array<AVCastControlCommandType>>)
```

取消会话有效命令变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-AVCastController-off(type: 'validCommandChange', callback?: Callback<Array<AVCastControlCommandType>>)--><!--Device-AVCastController-off(type: 'validCommandChange', callback?: Callback<Array<AVCastControlCommandType>>)-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'validCommandChange' | Yes | 取消对应的监听事件，支持事件`'validCommandChange'`。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;AVCastControlCommandType&gt;&gt; | No | 回调函数。参数commands是有效命令的集合。 &lt;br&gt;该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

## off('videoSizeChange')

```TypeScript
off(type: 'videoSizeChange'): void
```

取消视频尺寸事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-AVCastController-off(type: 'videoSizeChange'): void--><!--Device-AVCastController-off(type: 'videoSizeChange'): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'videoSizeChange' | Yes | 事件回调类型，支持事件`'videoSizeChange'`：当检测到会话的合法命令发生改变时，触发该事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception |

## Examples

```TypeScript
avCastController.off('videoSizeChange');
```

## off('error')

```TypeScript
off(type: 'error'): void
```

取消播放的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-off(type: 'error'): void--><!--Device-AVCastController-off(type: 'error'): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | 错误事件回调类型，取消注册的事件：'error'。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception |
| 5400102 | Operation not allowed. |
| 5400103 | I/O error. |
| 5400101 | No memory. |
| 5400106 | Unsupport format. |
| 5400104 | Time out. |
| 5400105 | Service died. |

## off('castControlGenericError')

```TypeScript
off(type: 'castControlGenericError', callback?: ErrorCallback): void
```

取消投播通用的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-off(type: 'castControlGenericError', callback?: ErrorCallback): void--><!--Device-AVCastController-off(type: 'castControlGenericError', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'castControlGenericError' | Yes | 取消对应的监听事件，支持的事件是'castControlGenericError'。 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

## off('castControlIoError')

```TypeScript
off(type: 'castControlIoError', callback?: ErrorCallback): void
```

取消投播输入/输出的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-off(type: 'castControlIoError', callback?: ErrorCallback): void--><!--Device-AVCastController-off(type: 'castControlIoError', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'castControlIoError' | Yes | 取消对应的监听事件，支持的事件是'castControlIoError'。 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

## off('castControlParsingError')

```TypeScript
off(type: 'castControlParsingError', callback?: ErrorCallback): void
```

取消投播解析的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-off(type: 'castControlParsingError', callback?: ErrorCallback): void--><!--Device-AVCastController-off(type: 'castControlParsingError', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'castControlParsingError' | Yes | 取消对应的监听事件，支持的事件是'castControlParsingError'。 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

## off('castControlDecodingError')

```TypeScript
off(type: 'castControlDecodingError', callback?: ErrorCallback): void
```

取消投播解码的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-off(type: 'castControlDecodingError', callback?: ErrorCallback): void--><!--Device-AVCastController-off(type: 'castControlDecodingError', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'castControlDecodingError' | Yes | 取消对应的监听事件，支持的事件是'castControlDecodingError'。 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

## off('castControlAudioRendererError')

```TypeScript
off(type: 'castControlAudioRendererError', callback?: ErrorCallback): void
```

取消投播音频渲染器的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-off(type: 'castControlAudioRendererError', callback?: ErrorCallback): void--><!--Device-AVCastController-off(type: 'castControlAudioRendererError', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'castControlAudioRendererError' | Yes | 取消对应的监听事件，支持的事件是'castControlAudioRendererError'。 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

## off('castControlDrmError')

```TypeScript
off(type: 'castControlDrmError', callback?: ErrorCallback): void
```

取消投播drm的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-off(type: 'castControlDrmError', callback?: ErrorCallback): void--><!--Device-AVCastController-off(type: 'castControlDrmError', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'castControlDrmError' | Yes | 取消对应的监听事件，支持的事件是'castControlDrmError'。 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

## off('keyRequest')

```TypeScript
off(type: 'keyRequest', callback?: KeyRequestCallback): void
```

取消许可证请求事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-off(type: 'keyRequest', callback?: KeyRequestCallback): void--><!--Device-AVCastController-off(type: 'keyRequest', callback?: KeyRequestCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyRequest' | Yes | 取消对应的监听事件，支持的事件是`'keyRequest'`。 |
| callback | [KeyRequestCallback](arkts-avsession-avsession-keyrequestcallback-t.md) | No | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception |

## off('customDataChange')

```TypeScript
off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void
```

取消对自定义数据的监听。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AVCastController-off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void--><!--Device-AVCastController-off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'customDataChange' | Yes | 取消对应的监听事件，支持的事件是'customDataChange'。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Object&gt;&gt; | No | 注册监听事件时的回调函数。该参数为可选参数，若不填写该参数，则认为取消会话所有与此事件相关的监听。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## offCastControlAudioRendererError

```TypeScript
offCastControlAudioRendererError(callback?: ErrorCallback): void
```

Unregister listeners for cast control audio renderer error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-offCastControlAudioRendererError(callback?: ErrorCallback): void--><!--Device-AVCastController-offCastControlAudioRendererError(callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | Callback used to listen for the cast control error event. |

## offCastControlDecodingError

```TypeScript
offCastControlDecodingError(callback?: ErrorCallback): void
```

Unregister listeners for cast control decoding error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-offCastControlDecodingError(callback?: ErrorCallback): void--><!--Device-AVCastController-offCastControlDecodingError(callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | Callback used to listen for the cast control error event. |

## offCastControlDrmError

```TypeScript
offCastControlDrmError(callback?: ErrorCallback): void
```

Unregister listeners for cast control drm error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-offCastControlDrmError(callback?: ErrorCallback): void--><!--Device-AVCastController-offCastControlDrmError(callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | Callback used to listen for the cast control error event. |

## offCastControlGenericError

```TypeScript
offCastControlGenericError(callback?: ErrorCallback): void
```

Unregister listeners for cast control generic error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-offCastControlGenericError(callback?: ErrorCallback): void--><!--Device-AVCastController-offCastControlGenericError(callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | Callback used to listen for the cast control error event. |

## offCastControlIoError

```TypeScript
offCastControlIoError(callback?: ErrorCallback): void
```

Unregister listeners for cast control input/output error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-offCastControlIoError(callback?: ErrorCallback): void--><!--Device-AVCastController-offCastControlIoError(callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | Callback used to listen for the cast control error event. |

## offCastControlParsingError

```TypeScript
offCastControlParsingError(callback?: ErrorCallback): void
```

Unregister listeners for cast control parsing error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-offCastControlParsingError(callback?: ErrorCallback): void--><!--Device-AVCastController-offCastControlParsingError(callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No | Callback used to listen for the cast control error event. |

## offCustomDataChange

```TypeScript
offCustomDataChange(callback?: Callback<Record<string, Object>>): void
```

Unregister listener for custom data sent from remote device.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-offCustomDataChange(callback?: Callback<Record<string, Object>>): void--><!--Device-AVCastController-offCustomDataChange(callback?: Callback<Record<string, Object>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Object&gt;&gt; | No | Callback used to retrieve custom data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## offEndOfStream

```TypeScript
offEndOfStream(callback?: NoParamCallback): void
```

Unregister endOfStream state callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-offEndOfStream(callback?: NoParamCallback): void--><!--Device-AVCastController-offEndOfStream(callback?: NoParamCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | No | Used to handle 'endOfStream' command |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## offError

```TypeScript
offError(): void
```

Unregister listens for playback error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-offError(): void--><!--Device-AVCastController-offError(): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |
| 5400102 | Operation not allowed. |
| 5400103 | I/O error. |
| 5400101 | No memory. |
| 5400106 | Unsupport format. |
| 5400104 | Time out. |
| 5400105 | Service died. |

## offKeyRequest

```TypeScript
offKeyRequest(callback?: KeyRequestCallback): void
```

Unregister listener for drm key request.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-offKeyRequest(callback?: KeyRequestCallback): void--><!--Device-AVCastController-offKeyRequest(callback?: KeyRequestCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [KeyRequestCallback](arkts-avsession-avsession-keyrequestcallback-t.md) | No | Callback used to request drm key. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## offMediaItemChange

```TypeScript
offMediaItemChange(): void
```

Unregister listener for current media item playback events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-offMediaItemChange(): void--><!--Device-AVCastController-offMediaItemChange(): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## offPlayNext

```TypeScript
offPlayNext(): void
```

Unregister playback command callback sent by remote side or media center.When canceling the callback, need to update the supported commands list.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-offPlayNext(): void--><!--Device-AVCastController-offPlayNext(): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## offPlayPrevious

```TypeScript
offPlayPrevious(): void
```

Unregister playback command callback sent by remote side or media center.When canceling the callback, need to update the supported commands list.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-offPlayPrevious(): void--><!--Device-AVCastController-offPlayPrevious(): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## offPlaybackStateChange

```TypeScript
offPlaybackStateChange(callback?: Callback<AVPlaybackState>): void
```

Unregister playback state changed callback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-offPlaybackStateChange(callback?: Callback<AVPlaybackState>): void--><!--Device-AVCastController-offPlaybackStateChange(callback?: Callback<AVPlaybackState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AVPlaybackState&gt; | No | The callback used to handle playback state changed event. The callback function provides the {@link AVPlaybackState} parameter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## offRequestPlay

```TypeScript
offRequestPlay(callback?: Callback<AVQueueItem>): void
```

Unregister requested playback command callback sent by remote side or media center.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-offRequestPlay(callback?: Callback<AVQueueItem>): void--><!--Device-AVCastController-offRequestPlay(callback?: Callback<AVQueueItem>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AVQueueItem&gt; | No | Used to handle 'requestPlay' command |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## offSeekDone

```TypeScript
offSeekDone(): void
```

Unregister listens for playback events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-offSeekDone(): void--><!--Device-AVCastController-offSeekDone(): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## offValidCommandChange

```TypeScript
offValidCommandChange(callback?: Callback<Array<AVCastControlCommandType>>): void
```

Unregister the valid commands of the casted session changed callback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-offValidCommandChange(callback?: Callback<Array<AVCastControlCommandType>>): void--><!--Device-AVCastController-offValidCommandChange(callback?: Callback<Array<AVCastControlCommandType>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;AVCastControlCommandType&gt;&gt; | No | The callback used to handle the changes. The callback function provides an array of AVCastControlCommandType. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

## offVideoSizeChange

```TypeScript
offVideoSizeChange(): void
```

Unregister listener for video size change event, used at remote side.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-offVideoSizeChange(): void--><!--Device-AVCastController-offVideoSizeChange(): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## on('playbackStateChange')

```TypeScript
on(type: 'playbackStateChange', filter: Array<keyof AVPlaybackState> | 'all', callback: (state: AVPlaybackState) => void): void
```

设置播放状态变化的监听事件。使用callback异步回调。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-on(type: 'playbackStateChange', filter: Array<keyof AVPlaybackState> | 'all', callback: (state: AVPlaybackState) => void): void--><!--Device-AVCastController-on(type: 'playbackStateChange', filter: Array<keyof AVPlaybackState> | 'all', callback: (state: AVPlaybackState) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'playbackStateChange' | Yes |  |
| filter | Array&lt;keyof AVPlaybackState&gt; \| 'all' | Yes | 'all'表示关注播放状态所有字段变化；Array&lt;keyof AVPlaybackState&gt;表示关注 Array中的字段变化。 |
| callback | (state: AVPlaybackState) =&gt; void | Yes | 回调函数，参数state是变化后的播放状态。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception |

## on('mediaItemChange')

```TypeScript
on(type: 'mediaItemChange', callback: Callback<AVQueueItem>): void
```

设置投播当前播放媒体内容的监听事件。使用callback异步回调。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-on(type: 'mediaItemChange', callback: Callback<AVQueueItem>): void--><!--Device-AVCastController-on(type: 'mediaItemChange', callback: Callback<AVQueueItem>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'mediaItemChange' | Yes | 事件回调类型，支持事件`'mediaItemChange'`：当播放的媒体内容变化时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AVQueueItem&gt; | Yes | 回调函数，参数AVQueueItem是当前正在播放的媒体内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception |

## on('playNext')

```TypeScript
on(type: 'playNext', callback: Callback<void>): void
```

设置播放下一首资源的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-on(type: 'playNext', callback: Callback<void>): void--><!--Device-AVCastController-on(type: 'playNext', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'playNext' | Yes | 事件回调类型，支持事件`'playNext'`：当播放下一首状态变化时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | 回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception |

## on('playPrevious')

```TypeScript
on(type: 'playPrevious', callback: Callback<void>): void
```

设置播放上一首资源的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-on(type: 'playPrevious', callback: Callback<void>): void--><!--Device-AVCastController-on(type: 'playPrevious', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'playPrevious' | Yes | 事件回调类型，支持事件`'playPrevious'`：当播放上一首状态变化时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | 回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception |

## on('requestPlay')

```TypeScript
on(type: 'requestPlay', callback: Callback<AVQueueItem>): void
```

设置请求播放的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-AVCastController-on(type: 'requestPlay', callback: Callback<AVQueueItem>): void--><!--Device-AVCastController-on(type: 'requestPlay', callback: Callback<AVQueueItem>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'requestPlay' | Yes | 事件回调类型，支持事件`'requestPlay'`：当请求播放状态变化时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AVQueueItem&gt; | Yes | 回调函数，参数AVQueueItem是当前正在播放的媒体内容。当监听事件注册成功，err为undefined，否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception |

## on('endOfStream')

```TypeScript
on(type: 'endOfStream', callback: Callback<void>): void
```

设置播放结束的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-AVCastController-on(type: 'endOfStream', callback: Callback<void>): void--><!--Device-AVCastController-on(type: 'endOfStream', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'endOfStream' | Yes | 事件回调类型，支持事件`'endOfStream'`：当资源播放结束时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | 回调函数。当监听事件注册成功，err为undefined，否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception |

## on('seekDone')

```TypeScript
on(type: 'seekDone', callback: Callback<int>): void
```

设置seek结束的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-on(type: 'seekDone', callback: Callback<int>): void--><!--Device-AVCastController-on(type: 'seekDone', callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'seekDone' | Yes | 事件回调类型，支持事件`'seekDone'`：当seek结束时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | Yes | 回调函数，返回seek后播放的位置。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception |

## on('validCommandChange')

```TypeScript
on(type: 'validCommandChange', callback: Callback<Array<AVCastControlCommandType>>)
```

会话支持的有效命令变化监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-AVCastController-on(type: 'validCommandChange', callback: Callback<Array<AVCastControlCommandType>>)--><!--Device-AVCastController-on(type: 'validCommandChange', callback: Callback<Array<AVCastControlCommandType>>)-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'validCommandChange' | Yes | 事件回调类型，支持事件`'validCommandChange'`：当检测到会话的合法命令发生改变时，触发该事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;AVCastControlCommandType&gt;&gt; | Yes | 回调函数。参数commands是有效命令的集合。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

## on('videoSizeChange')

```TypeScript
on(type: 'videoSizeChange', callback: (width: int, height: int) => void): void
```

媒体控制器监听视频尺寸变化变化的事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-AVCastController-on(type: 'videoSizeChange', callback: (width: int, height: int) => void): void--><!--Device-AVCastController-on(type: 'videoSizeChange', callback: (width: int, height: int) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'videoSizeChange' | Yes | 事件回调类型，支持事件`'videoSizeChange'`：当检测到会话的合法命令发生改变时，触发该事件。 |
| callback | (width: int, height: int) =&gt; void | Yes | 回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception |

## Examples

```TypeScript
avCastController.on('videoSizeChange', (width: number, height: number) => {
  console.info(`width : ${width} `);
  console.info(`height: ${height} `);
});
```

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

监听远端播放器的错误事件，该事件仅用于错误提示，不需要用户停止播控动作。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-on(type: 'error', callback: ErrorCallback): void--><!--Device-AVCastController-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | 错误事件回调类型，支持的事件：'error'，用户操作和系统都会触发此事件。 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | 错误事件回调方法：远端播放过程中发生的错误，会提供错误码ID和错误信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception |
| 5400102 | Operation not allowed. |
| 5400103 | I/O error. |
| 5400101 | No memory. |
| 5400106 | Unsupport format. |
| 5400104 | Time out. |
| 5400105 | Service died. |

## on('castControlGenericError')

```TypeScript
on(type: 'castControlGenericError', callback: ErrorCallback): void
```

监听投播通用错误事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-on(type: 'castControlGenericError', callback: ErrorCallback): void--><!--Device-AVCastController-on(type: 'castControlGenericError', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'castControlGenericError' | Yes | 错误事件回调类型，支持的事件：'castControlGenericError'。 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | 投播通用错误事件回调方法。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6611108 | Operation is not allowed. |
| 6611104 | The specified playback speed is not supported. |
| 6611105 | The action failed because either the media source device or the media sink device has been revoked. |
| 6611106 | The parameter is invalid, for example, the url is illegal to play. |
| 6611107 | Allocation of memory failed. |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 6611004 | The runtime check failed. |
| 6611100 | Cross-device data transmission is locked. |
| 6611101 | The specified seek mode is not supported. |
| 6611102 | The position to seek to is out of the range of the media asset or the specified seek mode is not supported. |
| 6611103 | The specified playback mode is not supported. |
| 6611000 | The error code for cast control is unspecified. |
| 6611001 | An unspecified error occurs in the remote player. |
| 6611002 | The playback position falls behind the live window. |
| 6611003 | The process of cast control times out. |

## on('castControlIoError')

```TypeScript
on(type: 'castControlIoError', callback: ErrorCallback): void
```

监听投播输入/输出的错误事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-on(type: 'castControlIoError', callback: ErrorCallback): void--><!--Device-AVCastController-on(type: 'castControlIoError', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'castControlIoError' | Yes | 错误事件回调类型，支持的事件：'castControlIoError'。 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | 投播输入/输出的错误事件回调方法。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6612004 | The HTTP server returns an unexpected HTTP response status code. |
| 6612100 | The media does not contain any contents that can be played. |
| 6612005 | The file does not exist. |
| 6612101 | The media cannot be read, for example, because of dust or scratches. |
| 6612006 | No permission is granted to perform the IO operation. |
| 6612102 | This resource is already in use. |
| 6612007 | Access to cleartext HTTP traffic is not allowed by the app's network security configuration. |
| 6612103 | The content using the validity interval has expired. |
| 6612000 | An unspecified input/output error occurs. |
| 6612001 | Network connection failure. |
| 6612002 | Network timeout. |
| 6612003 | Invalid "Content-Type" HTTP header. |
| 6612008 | Reading data out of the data bound. |
| 6612104 | Using the requested content to play is not allowed. |
| 6612105 | The use of the allowed content cannot be verified. |
| 6612106 | The number of times this content has been used as requested has reached the maximum allowed number of uses. |
| 6612107 | An error occurs when sending packet from source device to sink device. |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

## on('castControlParsingError')

```TypeScript
on(type: 'castControlParsingError', callback: ErrorCallback): void
```

监听投播解析的错误事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-on(type: 'castControlParsingError', callback: ErrorCallback): void--><!--Device-AVCastController-on(type: 'castControlParsingError', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'castControlParsingError' | Yes | 错误事件回调类型，支持的事件：'castControlParsingError'。 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | 投播解析的错误事件回调方法。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 6613004 | Unsupported feature in the media manifest. |
| 6613000 | Unspecified error related to content parsing. |
| 6613001 | Parsing error associated with media container format bit streams. |
| 6613002 | Parsing error associated with the media manifest. |
| 6613003 | An error occurs when attempting to extract a file with an unsupported media container format or an unsupported media container feature. |

## on('castControlDecodingError')

```TypeScript
on(type: 'castControlDecodingError', callback: ErrorCallback): void
```

监听投播解码的错误事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-on(type: 'castControlDecodingError', callback: ErrorCallback): void--><!--Device-AVCastController-on(type: 'castControlDecodingError', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'castControlDecodingError' | Yes | 错误事件回调类型，支持的事件：'castControlDecodingError'。 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | 投播解码的错误事件回调方法。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6614004 | The format of the content to decode exceeds the capabilities of the device. |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 6614005 | The format of the content to decode is not supported. |
| 6614000 | Unspecified decoding error. |
| 6614001 | Decoder initialization failed. |
| 6614002 | Decoder query failed. |
| 6614003 | Decoding the media samples failed. |

## on('castControlAudioRendererError')

```TypeScript
on(type: 'castControlAudioRendererError', callback: ErrorCallback): void
```

监听投播音频渲染器的错误事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-on(type: 'castControlAudioRendererError', callback: ErrorCallback): void--><!--Device-AVCastController-on(type: 'castControlAudioRendererError', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'castControlAudioRendererError' | Yes | 错误事件回调类型，支持的事件：'castControlAudioRendererError'。 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | 投播音频渲染器的错误事件回调方法。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 6615000 | Unspecified errors related to the audio renderer. |
| 6615001 | Initializing the audio renderer failed. |
| 6615002 | The audio renderer fails to write data. |

## on('castControlDrmError')

```TypeScript
on(type: 'castControlDrmError', callback: ErrorCallback): void
```

监听投播drm的错误事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AVCastController-on(type: 'castControlDrmError', callback: ErrorCallback): void--><!--Device-AVCastController-on(type: 'castControlDrmError', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'castControlDrmError' | Yes | 错误事件回调类型，支持的事件：'castControlDrmError'。 |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | 投播drm的错误事件回调方法。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6616004 | Failed to obtain a license. |
| 6616100 | An error occurs when the DRM processes the key response. |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 6616005 | The operation is disallowed by the license policy. |
| 6616006 | An error occurs in the DRM system. |
| 6616007 | The device has revoked DRM privileges. |
| 6616000 | Unspecified error related to DRM. |
| 6616001 | The chosen DRM protection scheme is not supported by the device. |
| 6616002 | Device provisioning failed. |
| 6616003 | The DRM-protected content to play is incompatible. |
| 6616008 | The DRM license being loaded into the open DRM session has expired. |

## on('keyRequest')

```TypeScript
on(type: 'keyRequest', callback: KeyRequestCallback): void
```

在线DRM资源投播时，设置许可证请求的事件监听。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-on(type: 'keyRequest', callback: KeyRequestCallback): void--><!--Device-AVCastController-on(type: 'keyRequest', callback: KeyRequestCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyRequest' | Yes | 事件回调类型，支持事件`'keyRequest'`：当DRM资源播放需要许可证时，触发该事件。 |
| callback | [KeyRequestCallback](arkts-avsession-avsession-keyrequestcallback-t.md) | Yes | 回调函数，媒体资源及许可证请求数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception |

## on('customDataChange')

```TypeScript
on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void
```

注册从远端设备发送的自定义数据的监听器。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AVCastController-on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void--><!--Device-AVCastController-on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'customDataChange' | Yes | 事件回调类型，支持'customDataChange'事件。媒体提供方发送自定义数据时触发。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Object&gt;&gt; | Yes | 回调函数，用于接收自定义数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## onCastControlAudioRendererError

```TypeScript
onCastControlAudioRendererError(callback: ErrorCallback): void
```

Register listeners for cast control audio renderer error error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-onCastControlAudioRendererError(callback: ErrorCallback): void--><!--Device-AVCastController-onCastControlAudioRendererError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | Callback used to listen for the cast control error event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6615000 | Unspecified errors related to the audio renderer. |
| 6615001 | Initializing the audio renderer failed. |
| 6615002 | The audio renderer fails to write data. |

## onCastControlDecodingError

```TypeScript
onCastControlDecodingError(callback: ErrorCallback): void
```

Register listeners for cast control decoding error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-onCastControlDecodingError(callback: ErrorCallback): void--><!--Device-AVCastController-onCastControlDecodingError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | Callback used to listen for the cast control error event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6614004 | The format of the content to decode exceeds the capabilities of the device. |
| 6614005 | The format of the content to decode is not supported. |
| 6614000 | Unspecified decoding error. |
| 6614001 | Decoder initialization failed. |
| 6614002 | Decoder query failed. |
| 6614003 | Decoding the media samples failed. |

## onCastControlDrmError

```TypeScript
onCastControlDrmError(callback: ErrorCallback): void
```

Register listeners for cast control drm error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-onCastControlDrmError(callback: ErrorCallback): void--><!--Device-AVCastController-onCastControlDrmError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | Callback used to listen for the cast control error event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6616004 | Failed to obtain a license. |
| 6616100 | An error occurs when the DRM processes the key response. |
| 6616005 | The operation is disallowed by the license policy. |
| 6616006 | An error occurs in the DRM system. |
| 6616007 | The device has revoked DRM privileges. |
| 6616000 | Unspecified error related to DRM. |
| 6616001 | The chosen DRM protection scheme is not supported by the device. |
| 6616002 | Device provisioning failed. |
| 6616003 | The DRM-protected content to play is incompatible. |
| 6616008 | The DRM license being loaded into the open DRM session has expired. |

## onCastControlGenericError

```TypeScript
onCastControlGenericError(callback: ErrorCallback): void
```

Register listeners for cast control generic error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-onCastControlGenericError(callback: ErrorCallback): void--><!--Device-AVCastController-onCastControlGenericError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | Callback used to listen for the cast control error event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6611108 | Operation is not allowed. |
| 6611104 | The specified playback speed is not supported. |
| 6611105 | The action failed because either the media source device or the media sink device has been revoked. |
| 6611106 | The parameter is invalid, for example, the url is illegal to play. |
| 6611107 | Allocation of memory failed. |
| 6611004 | The runtime check failed. |
| 6611100 | Cross-device data transmission is locked. |
| 6611101 | The specified seek mode is not supported. |
| 6611102 | The position to seek to is out of the range of the media asset or the specified seek mode is not supported. |
| 6611103 | The specified playback mode is not supported. |
| 6611000 | The error code for cast control is unspecified. |
| 6611001 | An unspecified error occurs in the remote player. |
| 6611002 | The playback position falls behind the live window. |
| 6611003 | The process of cast control times out. |

## onCastControlIoError

```TypeScript
onCastControlIoError(callback: ErrorCallback): void
```

Register listeners for cast control input/output error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-onCastControlIoError(callback: ErrorCallback): void--><!--Device-AVCastController-onCastControlIoError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | Callback used to listen for the cast control error event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6612004 | The HTTP server returns an unexpected HTTP response status code. |
| 6612100 | The media does not contain any contents that can be played. |
| 6612005 | The file does not exist. |
| 6612101 | The media cannot be read, for example, because of dust or scratches. |
| 6612006 | No permission is granted to perform the IO operation. |
| 6612102 | This resource is already in use. |
| 6612007 | Access to cleartext HTTP traffic is not allowed by the app's network security configuration. |
| 6612103 | The content using the validity interval has expired. |
| 6612000 | An unspecified input/output error occurs. |
| 6612001 | Network connection failure. |
| 6612002 | Network timeout. |
| 6612003 | Invalid "Content-Type" HTTP header. |
| 6612008 | Reading data out of the data bound. |
| 6612104 | Using the requested content to play is not allowed. |
| 6612105 | The use of the allowed content cannot be verified. |
| 6612106 | The number of times this content has been used as requested has reached the maximum allowed number of uses. |
| 6612107 | An error occurs when sending packet from source device to sink device. |

## onCastControlParsingError

```TypeScript
onCastControlParsingError(callback: ErrorCallback): void
```

Register listeners for cast control parsing error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-onCastControlParsingError(callback: ErrorCallback): void--><!--Device-AVCastController-onCastControlParsingError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | Callback used to listen for the cast control error event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6613004 | Unsupported feature in the media manifest. |
| 6613000 | Unspecified error related to content parsing. |
| 6613001 | Parsing error associated with media container format bit streams. |
| 6613002 | Parsing error associated with the media manifest. |
| 6613003 | An error occurs when attempting to extract a file with an unsupported media container format or an unsupported media container feature. |

## onCustomDataChange

```TypeScript
onCustomDataChange(callback: Callback<Record<string, Object>>): void
```

Register listener for custom data sent from remote device.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-onCustomDataChange(callback: Callback<Record<string, Object>>): void--><!--Device-AVCastController-onCustomDataChange(callback: Callback<Record<string, Object>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Object&gt;&gt; | Yes | Callback used to retrieve custom data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## onEndOfStream

```TypeScript
onEndOfStream(callback: NoParamCallback): void
```

Register endOfStream state callback.Application needs update the new media resource when receive these commands by using playItem.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-onEndOfStream(callback: NoParamCallback): void--><!--Device-AVCastController-onEndOfStream(callback: NoParamCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | Yes | Used to handle 'endOfStream' command |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## onError

```TypeScript
onError(callback: ErrorCallback): void
```

Register listeners for playback error events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-onError(callback: ErrorCallback): void--><!--Device-AVCastController-onError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | Callback used to listen for the playback error event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |
| 5400102 | Operation not allowed. |
| 5400103 | I/O error. |
| 5400101 | No memory. |
| 5400106 | Unsupport format. |
| 5400104 | Time out. |
| 5400105 | Service died. |

## onKeyRequest

```TypeScript
onKeyRequest(callback: KeyRequestCallback): void
```

Register listener for drm key request.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-onKeyRequest(callback: KeyRequestCallback): void--><!--Device-AVCastController-onKeyRequest(callback: KeyRequestCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [KeyRequestCallback](arkts-avsession-avsession-keyrequestcallback-t.md) | Yes | Callback used to request drm key. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## onMediaItemChange

```TypeScript
onMediaItemChange(callback: Callback<AVQueueItem>): void
```

Register listener for current media item playback events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-onMediaItemChange(callback: Callback<AVQueueItem>): void--><!--Device-AVCastController-onMediaItemChange(callback: Callback<AVQueueItem>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AVQueueItem&gt; | Yes | Callback used to listen for current item changed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## onPlayNext

```TypeScript
onPlayNext(callback: NoParamCallback): void
```

Register playback command callback sent by remote side or media center.Application needs update the new media resource when receive these commands by using playItem.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-onPlayNext(callback: NoParamCallback): void--><!--Device-AVCastController-onPlayNext(callback: NoParamCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | Yes | Used to handle 'playNext' command |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## onPlayPrevious

```TypeScript
onPlayPrevious(callback: NoParamCallback): void
```

Register playback command callback sent by remote side or media center.Application needs update the new media resource when receive these commands by using playItem.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-onPlayPrevious(callback: NoParamCallback): void--><!--Device-AVCastController-onPlayPrevious(callback: NoParamCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | Yes | Used to handle 'playPrevious' command |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## onPlaybackStateChange

```TypeScript
onPlaybackStateChange(filter: Array<string>, callback: Callback<AVPlaybackState>): void
```

Register playback state changed callback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-onPlaybackStateChange(filter: Array<string>, callback: Callback<AVPlaybackState>): void--><!--Device-AVCastController-onPlaybackStateChange(filter: Array<string>, callback: Callback<AVPlaybackState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | Array&lt;string&gt; | Yes | The properties of {@link AVPlaybackState} that you cared about |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AVPlaybackState&gt; | Yes | The callback used to handle playback state changed event. The callback function provides the {@link AVPlaybackState} parameter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## onPlaybackStateChangeAll

```TypeScript
onPlaybackStateChangeAll(callback: Callback<AVPlaybackState>): void
```

Register playback state changed callback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-onPlaybackStateChangeAll(callback: Callback<AVPlaybackState>): void--><!--Device-AVCastController-onPlaybackStateChangeAll(callback: Callback<AVPlaybackState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AVPlaybackState&gt; | Yes | The callback used to handle playback state changed event. The callback function provides the {@link AVPlaybackState} parameter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## onRequestPlay

```TypeScript
onRequestPlay(callback: Callback<AVQueueItem>): void
```

Register requested playback command callback sent by remote side or media center.The AVQueueItem may include the requested assetId, starting position and other configurations.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-onRequestPlay(callback: Callback<AVQueueItem>): void--><!--Device-AVCastController-onRequestPlay(callback: Callback<AVQueueItem>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AVQueueItem&gt; | Yes | Used to handle 'requestPlay' command |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## onSeekDone

```TypeScript
onSeekDone(callback: Callback<int>): void
```

Register listens for playback events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-onSeekDone(callback: Callback<int>): void--><!--Device-AVCastController-onSeekDone(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | Yes | Callback used to listen for the playback seekDone event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## onValidCommandChange

```TypeScript
onValidCommandChange(callback: Callback<Array<AVCastControlCommandType>>): void
```

Register the valid commands of the casted session changed callback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-onValidCommandChange(callback: Callback<Array<AVCastControlCommandType>>): void--><!--Device-AVCastController-onValidCommandChange(callback: Callback<Array<AVCastControlCommandType>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;AVCastControlCommandType&gt;&gt; | Yes | The callback used to handle the changes. The callback function provides an array of AVCastControlCommandType. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

## onVideoSizeChange

```TypeScript
onVideoSizeChange(callback: VideoSizeEvent): void
```

Register listener for video size change event, used at remote side.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastController-onVideoSizeChange(callback: VideoSizeEvent): void--><!--Device-AVCastController-onVideoSizeChange(callback: VideoSizeEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VideoSizeEvent](arkts-avsession-avsession-videosizeevent-t.md) | Yes | Callback used to return video size. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |

## prepare

```TypeScript
prepare(item: AVQueueItem, callback: AsyncCallback<void>): void
```

准备播放媒体资源，即进行播放资源的加载和缓冲。结果通过callback异步回调方式返回。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-AVCastController-prepare(item: AVQueueItem, callback: AsyncCallback<void>): void--><!--Device-AVCastController-prepare(item: AVQueueItem, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item | [AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md) | Yes | 播放列表中单项的相关属性。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当命令发送成功，err为undefined，否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception |
| 6600109 | The remote connection is not established |

## prepare

```TypeScript
prepare(item: AVQueueItem): Promise<void>
```

准备播放媒体资源，即进行播放资源的加载和缓冲。结果通过Promise异步回调方式返回。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-prepare(item: AVQueueItem): Promise<void>--><!--Device-AVCastController-prepare(item: AVQueueItem): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item | [AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md) | Yes | 播放列表中单项的相关属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当命令发送成功，无返回结果，否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception |
| 6600109 | The remote connection is not established |

## processMediaKeyResponse

```TypeScript
processMediaKeyResponse(assetId: string, response: Uint8Array): Promise<void>
```

在线DRM资源投播时，处理许可证响应。结果通过Promise异步回调方式返回。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-processMediaKeyResponse(assetId: string, response: Uint8Array): Promise<void>--><!--Device-AVCastController-processMediaKeyResponse(assetId: string, response: Uint8Array): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| assetId | string | Yes | 媒体ID。 |
| response | Uint8Array | Yes | 许可证响应。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，当处理许可证响应成功，无返回结果，否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

销毁当前controller，结果通过callback异步回调方式返回。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AVCastController-release(callback: AsyncCallback<void>): void--><!--Device-AVCastController-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当命令执行成功，err为undefined，否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception. |

## release

```TypeScript
release(): Promise<void>
```

销毁当前controller。结果通过Promise异步回调方式返回。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-release(): Promise<void>--><!--Device-AVCastController-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，controller销毁成功，无结果返回，否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception. |

## sendControlCommand

```TypeScript
sendControlCommand(command: AVCastControlCommand, callback: AsyncCallback<void>): void
```

通过会话控制器发送命令到其对应的会话。结果通过callback异步回调方式返回。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-AVCastController-sendControlCommand(command: AVCastControlCommand, callback: AsyncCallback<void>): void--><!--Device-AVCastController-sendControlCommand(command: AVCastControlCommand, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| command | [AVCastControlCommand](arkts-avsession-avsession-avcastcontrolcommand-i.md) | Yes | 会话的相关命令和命令相关参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当命令发送成功，err为undefined，否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception |
| 6600109 | The remote connection is not established |
| 6600105 | Invalid session command |

## sendControlCommand

```TypeScript
sendControlCommand(command: AVCastControlCommand): Promise<void>
```

通过控制器发送命令到其对应的会话。结果通过Promise异步回调方式返回。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-sendControlCommand(command: AVCastControlCommand): Promise<void>--><!--Device-AVCastController-sendControlCommand(command: AVCastControlCommand): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| command | [AVCastControlCommand](arkts-avsession-avsession-avcastcontrolcommand-i.md) | Yes | 会话的相关命令和命令相关参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当命令发送成功，无返回结果，否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception |
| 6600109 | The remote connection is not established |
| 6600105 | Invalid session command |

## sendCustomData

```TypeScript
sendCustomData(data: Record<string, Object>): Promise<void>
```

发送私有数据到远端设备。使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AVCastController-sendCustomData(data: Record<string, Object>): Promise<void>--><!--Device-AVCastController-sendCustomData(data: Record<string, Object>): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt; | Yes | 应用程序填充的自定义数据。 &lt;br&gt;服务端仅解析key：string为'customData'，且Object为string类型的对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception. |

## start

```TypeScript
start(item: AVQueueItem, callback: AsyncCallback<void>): void
```

启动播放某个媒体资源。结果通过callback异步回调方式返回。

> **说明：**
> 
> 在音视频投播场景下，当应用程序顺序调用
> [prepare](arkts-avsession-avsession-avcastcontroller-i.md#prepare)和start接口，且
> assetId不变时，如果prepare已经传入有效的mediaUri或fdSrc，则start接口将复用prepare阶段的完整的AVMediaDescription对象信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-AVCastController-start(item: AVQueueItem, callback: AsyncCallback<void>): void--><!--Device-AVCastController-start(item: AVQueueItem, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item | [AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md) | Yes | 播放列表中单项的相关属性。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当命令发送成功，err为undefined，否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception |
| 6600109 | The remote connection is not established |

## start

```TypeScript
start(item: AVQueueItem): Promise<void>
```

启动播放某个媒体资源。结果通过Promise异步回调方式返回。

> **说明：**
> 
> 在音视频投播场景下，当应用程序顺序调用
> [prepare](arkts-avsession-avsession-avcastcontroller-i.md#prepare)和start接口，且
> assetId不变时，如果prepare已经传入有效的mediaUri或fdSrc，则start接口将复用prepare阶段的完整的AVMediaDescription对象信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastController-start(item: AVQueueItem): Promise<void>--><!--Device-AVCastController-start(item: AVQueueItem): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item | [AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md) | Yes | 播放列表中单项的相关属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当命令发送成功，无返回结果，否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception |
| 6600109 | The remote connection is not established |

## update

```TypeScript
update(item: AVQueueItem): Promise<void>
```

更新投播媒体信息

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVCastController-update(item: AVQueueItem): Promise<void>--><!--Device-AVCastController-update(item: AVQueueItem): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item | [AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md) | Yes | 媒体信息item |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 通过promise回调成功 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception |
| 6600109 | The remote connection is not established |

