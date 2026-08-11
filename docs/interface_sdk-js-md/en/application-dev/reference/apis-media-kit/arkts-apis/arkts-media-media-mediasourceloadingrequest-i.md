# MediaSourceLoadingRequest

The MediaSourceLoadingRequest class defines a loading request object. Applications use this object to obtain the location of the requested resource and to interact with the player for data exchange.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-media-interface MediaSourceLoadingRequest--><!--Device-media-interface MediaSourceLoadingRequest-End-->

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

Notifies the player of the current request status. After pushing all the data for a single resource, the application should send the **LOADING_ERROR_SUCCESS** state to notify the player that the resource push is complete.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MediaSourceLoadingRequest-finishLoading(uuid: long, state: LoadingRequestError): void--><!--Device-MediaSourceLoadingRequest-finishLoading(uuid: long, state: LoadingRequestError): void-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uuid | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | ID for the resource handle. The source is [SourceOpenCallback](arkts-media-media-sourceopencallback-t.md). |
| state | [LoadingRequestError](arkts-media-media-loadingrequesterror-e.md) | Yes | Request status. |

## respondData

```TypeScript
respondData(uuid: number, offset: number, buffer: ArrayBuffer): number
```

Sends data to the player.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MediaSourceLoadingRequest-respondData(uuid: number, offset: number, buffer: ArrayBuffer): number--><!--Device-MediaSourceLoadingRequest-respondData(uuid: number, offset: number, buffer: ArrayBuffer): number-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uuid | number | Yes | ID for the resource handle. The source is [SourceOpenCallback](arkts-media-media-sourceopencallback-t.md). |
| offset | number | Yes | Offset of the current media data relative to the start of the resource. The value cannot be less than 0. |
| buffer | ArrayBuffer | Yes | Media data sent to the player.&lt;br&gt;**Note：**: Do not transmit irrelevant data, as it can affect normal data parsing and playback. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Number of bytes received by the server. &lt;br&gt;- A return value less than 0 indicates failure. &lt;br&gt;- A return value of -2 indicates that the player no longer needs the current data, and the client should stop the current read process. &lt;br&gt;- A return value of -3 indicates that the player's buffer is full, and the client should wait for the next read. |

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

Sends response header information to the player. This API must be called before the first call to   
[respondData](arkts-media-media-mediasourceloadingrequest-i.md#responddata).

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MediaSourceLoadingRequest-respondHeader(uuid: long, header?: Record<string, string>, redirectUrl?: string): void--><!--Device-MediaSourceLoadingRequest-respondHeader(uuid: long, header?: Record<string, string>, redirectUrl?: string): void-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uuid | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | ID for the resource handle. The source is [SourceOpenCallback](arkts-media-media-sourceopencallback-t.md). |
| header | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt; | No | Header information in the HTTP response. The application can intersect the header fields with the fields supported by the underlying layer for parsing or directly pass in all corresponding header information.&lt;br&gt; - The following fields need to be parsed by the underlying player: Transfer-Encoding, Location, Content-Type, Content-Range, Content-Encode, Accept-Ranges, and content-length. |
| redirectUrl | string | No | Redirect URL in the HTTP response. |

## header

```TypeScript
header?: Record<string, string>
```

HTTP request header. If the header exists, the application should set the header information in the HTTP request when downloading data.

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

Resource URL, which is the path to the resource that the application needs to open.

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MediaSourceLoadingRequest-url: string--><!--Device-MediaSourceLoadingRequest-url: string-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

