# MediaSourceLoadingRequest

用于定义加载请求的对象。应用程序通过该对象来获取请求的资源位置，通过该对象和播放器进行数据交互。

> **说明：**
> 
> - 本Interface首批接口从API version 18开始支持。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-unnamed-interface MediaSourceLoadingRequest--><!--Device-unnamed-interface MediaSourceLoadingRequest-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## finishLoading

ArkTS-Dyn:
```TypeScript
finishLoading(uuid: number, state: LoadingRequestError): void
```

ArkTS-Sta:
```TypeScript
finishLoading(uuid: long, state: LoadingRequestError): void
```

应用程序用于通知播放器当前请求状态的接口。针对服务侧请求的单个资源，推送完全部资源后需要发送LOADING_ERROR_SUCCESS状态告知该资源推送结束。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MediaSourceLoadingRequest-finishLoading(uuid: long, state: LoadingRequestError): void--><!--Device-MediaSourceLoadingRequest-finishLoading(uuid: long, state: LoadingRequestError): void-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uuid | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 资源句柄的标识。来源是[SourceOpenCallback](@ohos.multimedia.media:media.SourceOpenCallback)。 |
| state | [LoadingRequestError](arkts-media-multimedia-media-loadingrequesterror-e.md) | Yes | 请求的状态。 |

## respondData

```TypeScript
respondData(uuid: number, offset: number, buffer: ArrayBuffer): number
```

用于应用程序向播放器发送数据。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MediaSourceLoadingRequest-respondData(uuid: number, offset: number, buffer: ArrayBuffer): number--><!--Device-MediaSourceLoadingRequest-respondData(uuid: number, offset: number, buffer: ArrayBuffer): number-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uuid | number | Yes | 资源句柄的标识。来源是[SourceOpenCallback](@ohos.multimedia.media:media.SourceOpenCallback)。 |
| offset | number | Yes | 当前媒体数据相对于资源起始位置的偏移量。offset不能小于0。 |
| buffer | ArrayBuffer | Yes | 响应播放器的媒体数据。&lt;br/&gt;**注意：** 不要传输无关数据，会影响正常数据解析和播放。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 当前服务端接受的字节数。 &lt;br&gt;- 返回值小于0表示操作失败。 &lt;br&gt;- 返回值为-2时，表示播放器不再需要当前数据，客户端应停止当前读取过程。 &lt;br&gt;- 返回值为-3时，表示播放器的缓冲区已满，客户端应等待下一次读取。 |

## respondData

```TypeScript
respondData(uuid: long, offset: long, buffer: ArrayBuffer): int | undefined
```

The interface for application used to send requested data to AVPlayer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-MediaSourceLoadingRequest-respondData(uuid: long, offset: long, buffer: ArrayBuffer): int | undefined--><!--Device-MediaSourceLoadingRequest-respondData(uuid: long, offset: long, buffer: ArrayBuffer): int | undefined-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uuid | long | Yes | ID for the resource handle. |
| offset | long | Yes | Offset of the current media data relative to the start of the resource. |
| buffer | ArrayBuffer | Yes | Media data sent to the player. |

**Return value:**

| Type | Description |
| --- | --- |
| int | accept bytes for current read. The value less than zero means failed. -2, means player need current data any more, the client should stop current read process. -3, means player buffer is full, the client should wait for next read. |

## respondHeader

ArkTS-Dyn:
```TypeScript
respondHeader(uuid: number, header?: Record<string, string>, redirectUrl?: string): void
```

ArkTS-Sta:
```TypeScript
respondHeader(uuid: long, header?: Record<string, string>, redirectUrl?: string): void
```

用于应用程序向播放器发送响应头信息，应在第一次调用  
[respondData](media.MediaSourceLoadingRequest.respondData(uuid: number, offset: number, buffer: ArrayBuffer))方法之前调用。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MediaSourceLoadingRequest-respondHeader(uuid: long, header?: Record<string, string>, redirectUrl?: string): void--><!--Device-MediaSourceLoadingRequest-respondHeader(uuid: long, header?: Record<string, string>, redirectUrl?: string): void-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uuid | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 资源句柄的标识。来源是[SourceOpenCallback](@ohos.multimedia.media:media.SourceOpenCallback)。 |
| header | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt; | No | HTTP响应中的头部信息。应用可将头部信息字段与底层支持解析字段取交集传递或直接传入对应的所有头部信息。&lt;br&gt; - 底层播放需要解析的 字段包括Transfer-Encoding、Location、Content-Type、Content-Range、Content-Encode、Accept-Ranges、content-length。 |
| redirectUrl | string | No | 如果存在，为HTTP响应中的重定向URL。 |

## header

```TypeScript
header?: Record<string, string>
```

网络请求标头，如果存在，需要应用在下载数据时将头信息设置到HTTP请求中。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MediaSourceLoadingRequest-header?: Record<string, string>--><!--Device-MediaSourceLoadingRequest-header?: Record<string, string>-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## url

```TypeScript
url: string
```

资源URL，需要应用程序打开的资源路径。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MediaSourceLoadingRequest-url: string--><!--Device-MediaSourceLoadingRequest-url: string-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

