# MediaSourceLoadingRequest

The MediaSourceLoadingRequest class defines a loading request object. Applications use this object to obtain the location of the requested resource and to interact with the player for data exchange.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-media-interface MediaSourceLoadingRequest--><!--Device-media-interface MediaSourceLoadingRequest-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## finishLoading

ArkTS-Dyn:
```TypeScript
finishLoading(uuid: number, state: LoadingRequestError): void
```

ArkTS-Sta:
```TypeScript
finishLoading(uuid: long, state: LoadingRequestError): void
```

Notifies the player of the current request status. After pushing all the data for a single resource, the application should send the **LOADING\_ERROR\_SUCCESS** state to notify the player that the resource push is complete.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MediaSourceLoadingRequest-finishLoading(uuid: long, state: LoadingRequestError): void--><!--Device-MediaSourceLoadingRequest-finishLoading(uuid: long, state: LoadingRequestError): void-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uuid | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long | Yes | ID for the resource handle. The source is [SourceOpenCallback]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| state | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Request status. |

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
| uuid | number | Yes | ID for the resource handle. The source is [SourceOpenCallback]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| offset | number | Yes | Offset of the current media data relative to the start of the resource. The value cannot be less than 0. |
| buffer | ArrayBuffer | Yes | Media data sent to the player.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_**Note**: Do not transmit irrelevant data, as it can affect normal data parsing and playback. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Number of bytes received by the server. |

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
| int | - accept bytes for current read. The value less than zero means failed. |

## respondHeader

ArkTS-Dyn:
```TypeScript
respondHeader(uuid: number, header?: Record<string, string>, redirectUrl?: string): void
```

ArkTS-Sta:
```TypeScript
respondHeader(uuid: long, header?: Record<string, string>, redirectUrl?: string): void
```

Sends response header information to the player. This API must be called before the first call to [respondData]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MediaSourceLoadingRequest-respondHeader(uuid: long, header?: Record<string, string>, redirectUrl?: string): void--><!--Device-MediaSourceLoadingRequest-respondHeader(uuid: long, header?: Record<string, string>, redirectUrl?: string): void-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uuid | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long | Yes | ID for the resource handle. The source is [SourceOpenCallback]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| header | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string, string&gt; | No | Header information in the HTTP response. The application can intersect the header fields with the fields supported by the underlying layer for parsing or directly pass in all corresponding header information.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ - The following fields need to be parsed by the underlying player:Transfer-Encoding, Location, Content-Type, Content-Range, Content-Encode, Accept-Ranges, and content-length. |
| redirectUrl | string | No | Redirect URL in the HTTP response. |

## header

```TypeScript
header?: Record<string, string>
```

HTTP request header. If the header exists, the application should set the header information in the HTTP request when downloading data.

**Type:** Record&lt;string, string&gt;

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

