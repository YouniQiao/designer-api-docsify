# AVCastController

在投播建立后，调用[avSession.AVSession.getAVCastController](arkts-avsession-avsession-avsession-i.md#getavcastcontroller)后， 返回会话控制器实例。控制器可查看会话ID，并可完成对会话发送命令及事件， 获取会话元数据，播放状态信息等操作。

> **说明：**&gt;
> - 本Interface首批接口从API version 10开始支持。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

## 导入模块

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## getAVPlaybackState

```TypeScript
getAVPlaybackState(callback: AsyncCallback<AVPlaybackState>): void
```

获取当前的远端播放状态。结果通过callback异步回调方式返回。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## getAVPlaybackState

```TypeScript
getAVPlaybackState(): Promise<AVPlaybackState>
```

获取当前的远端播放状态。结果通过Promise异步回调方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## getCurrentItem

```TypeScript
getCurrentItem(callback: AsyncCallback<AVQueueItem>): void
```

获取当前投播的资源信息。结果通过callback异步回调方式返回。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## getCurrentItem

```TypeScript
getCurrentItem(): Promise<AVQueueItem>
```

获取当前投播的资源信息。结果通过Promise异步回调方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## getRecommendedResolutionLevel

```TypeScript
getRecommendedResolutionLevel(decoderType: DecoderType): Promise<ResolutionLevel>
```

通过传递解码方式，获取推荐的分辨率。使用Promise异步回调。

**起始版本：** 19

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| decoderType | [DecoderType](arkts-avsession-avsession-decodertype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ResolutionLevel](arkts-avsession-avsession-resolutionlevel-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## getSupportedDecoders

```TypeScript
getSupportedDecoders(): Promise<Array<DecoderType>>
```

获取当前远端设备的解码方式。使用Promise异步回调。

**起始版本：** 19

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[DecoderType](arkts-avsession-avsession-decodertype-e.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## getSupportedHdrCapabilities

```TypeScript
getSupportedHdrCapabilities(): Promise<Array<hdrCapability.HDRFormat>>
```

获取当前的远端设备所支持的HDR能力。使用Promise异步回调。

**起始版本：** 19

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;hdrCapability.HDRFormat & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## getSupportedPlaySpeeds

```TypeScript
getSupportedPlaySpeeds(): Promise<Array<number>>
```

获取当前的远端设备所支持倍速播放列表，仅支持使用cast+协议连接的设备。使用Promise异步回调。

**起始版本：** 19

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## getValidCommands

```TypeScript
getValidCommands(callback: AsyncCallback<Array<AVCastControlCommandType>>): void
```

获取当前支持的命令。结果通过callback异步回调方式返回。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AVCastControlCommandType](arkts-avsession-avsession-avcastcontrolcommandtype-t.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## getValidCommands

```TypeScript
getValidCommands(): Promise<Array<AVCastControlCommandType>>
```

获取当前支持的命令。结果通过Promise异步回调方式返回。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[AVCastControlCommandType](arkts-avsession-avsession-avcastcontrolcommandtype-t.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## off('playbackStateChange')

```TypeScript
off(type: 'playbackStateChange', callback?: (state: AVPlaybackState) => void): void
```

取消播放状态变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'playbackStateChange' | 是 |
| callback | (state: AVPlaybackState) = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## off('mediaItemChange')

```TypeScript
off(type: 'mediaItemChange'): void
```

取消设置投播当前播放媒体内容事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'mediaItemChange' | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## off('playNext')

```TypeScript
off(type: 'playNext'): void
```

取消设置播放下一首资源事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'playNext' | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## off('playPrevious')

```TypeScript
off(type: 'playPrevious'): void
```

取消设置播放上一首资源事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'playPrevious' | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## off('requestPlay')

```TypeScript
off(type: 'requestPlay', callback?: Callback<AVQueueItem>): void
```

取消设置请求播放事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'requestPlay' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## off('endOfStream')

```TypeScript
off(type: 'endOfStream', callback?: Callback<void>): void
```

取消设置播放结束事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'endOfStream' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## off('seekDone')

```TypeScript
off(type: 'seekDone'): void
```

取消设置seek结束事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'seekDone' | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## off('validCommandChange')

```TypeScript
off(type: 'validCommandChange', callback?: Callback<Array<AVCastControlCommandType>>)
```

取消会话有效命令变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'validCommandChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AVCastControlCommandType](arkts-avsession-avsession-avcastcontrolcommandtype-t.md)&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## off('videoSizeChange')

```TypeScript
off(type: 'videoSizeChange'): void
```

取消视频尺寸事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'videoSizeChange' | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## off('error')

```TypeScript
off(type: 'error'): void
```

取消播放的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400101](../../apis-media-kit/errorcode-media.md#5400101-内存分配失败) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [5400104](../../apis-media-kit/errorcode-media.md#5400104-操作超时) |
| [5400105](../../apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |
| [5400106](../../apis-media-kit/errorcode-media.md#5400106-不支持的规格) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## off('castControlGenericError')

```TypeScript
off(type: 'castControlGenericError', callback?: ErrorCallback): void
```

取消投播通用的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'castControlGenericError' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('castControlIoError')

```TypeScript
off(type: 'castControlIoError', callback?: ErrorCallback): void
```

取消投播输入/输出的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'castControlIoError' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('castControlParsingError')

```TypeScript
off(type: 'castControlParsingError', callback?: ErrorCallback): void
```

取消投播解析的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'castControlParsingError' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('castControlDecodingError')

```TypeScript
off(type: 'castControlDecodingError', callback?: ErrorCallback): void
```

取消投播解码的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'castControlDecodingError' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('castControlAudioRendererError')

```TypeScript
off(type: 'castControlAudioRendererError', callback?: ErrorCallback): void
```

取消投播音频渲染器的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'castControlAudioRendererError' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('castControlDrmError')

```TypeScript
off(type: 'castControlDrmError', callback?: ErrorCallback): void
```

取消投播drm的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'castControlDrmError' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('keyRequest')

```TypeScript
off(type: 'keyRequest', callback?: KeyRequestCallback): void
```

取消许可证请求事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyRequest' | 是 |
| callback | [KeyRequestCallback](arkts-avsession-avsession-keyrequestcallback-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## off('customDataChange')

```TypeScript
off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void
```

取消对自定义数据的监听。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'customDataChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Object&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## on('playbackStateChange')

```TypeScript
on(type: 'playbackStateChange', filter: Array<keyof AVPlaybackState> | 'all', callback: (state: AVPlaybackState) => void): void
```

设置播放状态变化的监听事件。使用callback异步回调。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'playbackStateChange' | 是 |
| filter | Array & lt;keyof AVPlaybackState & gt; \ | 'all' | 是 |
| callback | (state: AVPlaybackState) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## on('mediaItemChange')

```TypeScript
on(type: 'mediaItemChange', callback: Callback<AVQueueItem>): void
```

设置投播当前播放媒体内容的监听事件。使用callback异步回调。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'mediaItemChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## on('playNext')

```TypeScript
on(type: 'playNext', callback: Callback<void>): void
```

设置播放下一首资源的监听事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'playNext' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## on('playPrevious')

```TypeScript
on(type: 'playPrevious', callback: Callback<void>): void
```

设置播放上一首资源的监听事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'playPrevious' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## on('requestPlay')

```TypeScript
on(type: 'requestPlay', callback: Callback<AVQueueItem>): void
```

设置请求播放的监听事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'requestPlay' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## on('endOfStream')

```TypeScript
on(type: 'endOfStream', callback: Callback<void>): void
```

设置播放结束的监听事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'endOfStream' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## on('seekDone')

```TypeScript
on(type: 'seekDone', callback: Callback<number>): void
```

设置seek结束的监听事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'seekDone' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## on('validCommandChange')

```TypeScript
on(type: 'validCommandChange', callback: Callback<Array<AVCastControlCommandType>>)
```

会话支持的有效命令变化监听事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'validCommandChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AVCastControlCommandType](arkts-avsession-avsession-avcastcontrolcommandtype-t.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600103](../errorcode-avsession.md#6600103-会话控制器不存在) |

## on('videoSizeChange')

```TypeScript
on(type: 'videoSizeChange', callback: (width: number, height: number) => void): void
```

媒体控制器监听视频尺寸变化变化的事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'videoSizeChange' | 是 |
| callback | (width: number, height: number) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

监听远端播放器的错误事件，该事件仅用于错误提示，不需要用户停止播控动作。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'error' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400101](../../apis-media-kit/errorcode-media.md#5400101-内存分配失败) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [5400104](../../apis-media-kit/errorcode-media.md#5400104-操作超时) |
| [5400105](../../apis-media-kit/errorcode-media.md#5400105-播放服务死亡) |
| [5400106](../../apis-media-kit/errorcode-media.md#5400106-不支持的规格) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## on('castControlGenericError')

```TypeScript
on(type: 'castControlGenericError', callback: ErrorCallback): void
```

监听投播通用错误事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'castControlGenericError' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6611000](../errorcode-avsession.md#6611000-投播控制器出现未知错误) |
| [6611001](../errorcode-avsession.md#6611001-远端设备出现未知错误) |
| [6611002](../errorcode-avsession.md#6611002-加载位置超过投播视频的总进度) |
| [6611003](../errorcode-avsession.md#6611003-投播控制器加载超时) |
| [6611004](../errorcode-avsession.md#6611004-运行时检查失败) |
| [6611100](../errorcode-avsession.md#6611100-跨设备数据传输被锁定) |
| [6611101](../errorcode-avsession.md#6611101-不支持当前进度条模式) |
| [6611102](../errorcode-avsession.md#6611102-非法seek目标) |
| [6611103](../errorcode-avsession.md#6611103-不支持当前播放模式) |
| [6611104](../errorcode-avsession.md#6611104-不支持当前播放速度) |
| [6611105](../errorcode-avsession.md#6611105-设备吊销) |
| [6611106](../errorcode-avsession.md#6611106-传入非法参数) |
| [6611107](../errorcode-avsession.md#6611107-内存分配失败) |
| [6611108](../errorcode-avsession.md#6611108-不允许进行当前操作) |

## on('castControlIoError')

```TypeScript
on(type: 'castControlIoError', callback: ErrorCallback): void
```

监听投播输入/输出的错误事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'castControlIoError' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6612000](../errorcode-avsession.md#6612000-未知的输入输出错误) |
| [6612001](../errorcode-avsession.md#6612001-网络连接失败) |
| [6612002](../errorcode-avsession.md#6612002-网络超时) |
| [6612003](../errorcode-avsession.md#6612003-无效content-typehttp头) |
| [6612004](../errorcode-avsession.md#6612004-http服务器返回异常的http响应状态码) |
| [6612005](../errorcode-avsession.md#6612005-文件不存在) |
| [6612006](../errorcode-avsession.md#6612006-缺少执行io操作的权限) |
| [6612007](../errorcode-avsession.md#6612007-网络安全配置不允许此操作) |
| [6612008](../errorcode-avsession.md#6612008-读取数据超出数据范围) |
| [6612100](../errorcode-avsession.md#6612100-缺少可播放的媒体资源) |
| [6612101](../errorcode-avsession.md#6612101-媒体资源无法被读取) |
| [6612102](../errorcode-avsession.md#6612102-资源正在使用) |
| [6612103](../errorcode-avsession.md#6612103-内容使用有效期已过) |
| [6612104](../errorcode-avsession.md#6612104-不允许使用请求的内容) |
| [6612105](../errorcode-avsession.md#6612105-无法验证允许使用的内容) |
| [6612106](../errorcode-avsession.md#6612106-资源使用频繁) |
| [6612107](../errorcode-avsession.md#6612107-本端向远端发送资源包失败) |

## on('castControlParsingError')

```TypeScript
on(type: 'castControlParsingError', callback: ErrorCallback): void
```

监听投播解析的错误事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'castControlParsingError' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6613000](../errorcode-avsession.md#6613000-未知解析错误) |
| [6613001](../errorcode-avsession.md#6613001-非法类型) |
| [6613002](../errorcode-avsession.md#6613002-相关媒体清单的解析错误) |
| [6613003](../errorcode-avsession.md#6613003-不支持该媒体格式) |
| [6613004](../errorcode-avsession.md#6613004-媒体清单中不支持此功能) |

## on('castControlDecodingError')

```TypeScript
on(type: 'castControlDecodingError', callback: ErrorCallback): void
```

监听投播解码的错误事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'castControlDecodingError' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6614000](../errorcode-avsession.md#6614000-未知的解码错误) |
| [6614001](../errorcode-avsession.md#6614001-解码器初始化失败) |
| [6614002](../errorcode-avsession.md#6614002-解码器查询失败) |
| [6614003](../errorcode-avsession.md#6614003-解码媒体样本时失败) |
| [6614004](../errorcode-avsession.md#6614004-所需解码的内容格式超出设备能力) |
| [6614005](../errorcode-avsession.md#6614005-解码不支持的内容格式) |

## on('castControlAudioRendererError')

```TypeScript
on(type: 'castControlAudioRendererError', callback: ErrorCallback): void
```

监听投播音频渲染器的错误事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'castControlAudioRendererError' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6615000](../errorcode-avsession.md#6615000-音频渲染器相关的未知错误) |
| [6615001](../errorcode-avsession.md#6615001-音频渲染器初始化异常) |
| [6615002](../errorcode-avsession.md#6615002-音频渲染器写数据异常) |

## on('castControlDrmError')

```TypeScript
on(type: 'castControlDrmError', callback: ErrorCallback): void
```

监听投播drm的错误事件。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'castControlDrmError' | 是 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6616000](../errorcode-avsession.md#6616000-drm相关的未知错误) |
| [6616001](../errorcode-avsession.md#6616001-设备不支持所选的drm保护方案) |
| [6616002](../errorcode-avsession.md#6616002-调配设备时出现故障) |
| [6616003](../errorcode-avsession.md#6616003-尝试播放不兼容的drm保护内容) |
| [6616004](../errorcode-avsession.md#6616004-许可证获取失败) |
| [6616005](../errorcode-avsession.md#6616005-许可证策略不允许的操作) |
| [6616006](../errorcode-avsession.md#6616006-drm系统错误) |
| [6616007](../errorcode-avsession.md#6616007-设备已吊销drm权限) |
| [6616008](../errorcode-avsession.md#6616008-已过期的drm许可证被加载到打开的drm会话中) |
| [6616100](../errorcode-avsession.md#6616100-drm进程密钥响应错误) |

## on('keyRequest')

```TypeScript
on(type: 'keyRequest', callback: KeyRequestCallback): void
```

在线DRM资源投播时，设置许可证请求的事件监听。每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyRequest' | 是 |
| callback | [KeyRequestCallback](arkts-avsession-avsession-keyrequestcallback-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## on('customDataChange')

```TypeScript
on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void
```

注册从远端设备发送的自定义数据的监听器。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'customDataChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Object&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## prepare

```TypeScript
prepare(item: AVQueueItem, callback: AsyncCallback<void>): void
```

准备播放媒体资源，即进行播放资源的加载和缓冲。结果通过callback异步回调方式返回。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| item | [AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600109](../errorcode-avsession.md#6600109-远端会话不存在) |

## prepare

```TypeScript
prepare(item: AVQueueItem): Promise<void>
```

准备播放媒体资源，即进行播放资源的加载和缓冲。结果通过Promise异步回调方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| item | [AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600109](../errorcode-avsession.md#6600109-远端会话不存在) |

## processMediaKeyResponse

```TypeScript
processMediaKeyResponse(assetId: string, response: Uint8Array): Promise<void>
```

在线DRM资源投播时，处理许可证响应。结果通过Promise异步回调方式返回。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assetId | string | 是 |
| response | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

销毁当前controller，结果通过callback异步回调方式返回。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## release

```TypeScript
release(): Promise<void>
```

销毁当前controller。结果通过Promise异步回调方式返回。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## sendControlCommand

```TypeScript
sendControlCommand(command: AVCastControlCommand, callback: AsyncCallback<void>): void
```

通过会话控制器发送命令到其对应的会话。结果通过callback异步回调方式返回。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| command | [AVCastControlCommand](arkts-avsession-avsession-avcastcontrolcommand-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600105](../errorcode-avsession.md#6600105-无效会话命令) |
| [6600109](../errorcode-avsession.md#6600109-远端会话不存在) |

## sendControlCommand

```TypeScript
sendControlCommand(command: AVCastControlCommand): Promise<void>
```

通过控制器发送命令到其对应的会话。结果通过Promise异步回调方式返回。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| command | [AVCastControlCommand](arkts-avsession-avsession-avcastcontrolcommand-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600105](../errorcode-avsession.md#6600105-无效会话命令) |
| [6600109](../errorcode-avsession.md#6600109-远端会话不存在) |

## sendCustomData

```TypeScript
sendCustomData(data: Record<string, Object>): Promise<void>
```

发送私有数据到远端设备。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | Record & lt;string, Object & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

## start

```TypeScript
start(item: AVQueueItem, callback: AsyncCallback<void>): void
```

启动播放某个媒体资源。结果通过callback异步回调方式返回。

> **说明：**&gt;
> 在音视频投播场景下，当应用程序顺序调用
> [prepare](#prepare)和start接口，且
> assetId不变时，如果prepare已经传入有效的mediaUri或fdSrc，则start接口将复用prepare阶段的完整的AVMediaDescription对象信息。

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| item | [AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600109](../errorcode-avsession.md#6600109-远端会话不存在) |

## start

```TypeScript
start(item: AVQueueItem): Promise<void>
```

启动播放某个媒体资源。结果通过Promise异步回调方式返回。

> **说明：**&gt;
> 在音视频投播场景下，当应用程序顺序调用
> [prepare](#prepare)和start接口，且
> assetId不变时，如果prepare已经传入有效的mediaUri或fdSrc，则start接口将复用prepare阶段的完整的AVMediaDescription对象信息。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| item | [AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600109](../errorcode-avsession.md#6600109-远端会话不存在) |

## update

```TypeScript
update(item: AVQueueItem): Promise<void>
```

更新投播媒体信息

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| item | [AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600109](../errorcode-avsession.md#6600109-远端会话不存在) |
