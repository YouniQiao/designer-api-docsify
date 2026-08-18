# MediaSourceLoadingRequest

The MediaSourceLoadingRequest class defines a loading request object. Applications use this object to obtain the location of the requested resource and to interact with the player for data exchange.

**Since:** 23

<!--Device-media-interface MediaSourceLoadingRequest--><!--Device-media-interface MediaSourceLoadingRequest-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## Modules to Import

```TypeScript
```

## finishLoading

```TypeScript
finishLoading(uuid: number, state: LoadingRequestError): void
```

Notifies the player of the current request status. After pushing all the data for a single resource, the application should send the **LOADING_ERROR_SUCCESS** state to notify the player that the resource push is complete.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MediaSourceLoadingRequest-finishLoading(uuid: long, state: LoadingRequestError): void--><!--Device-MediaSourceLoadingRequest-finishLoading(uuid: long, state: LoadingRequestError): void-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uuid | number | Yes |
| state | [LoadingRequestError](arkts-media-media-loadingrequesterror-e.md) | Yes |

## respondData

```TypeScript
respondData(uuid: number, offset: number, buffer: ArrayBuffer): number
```

Sends data to the player.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MediaSourceLoadingRequest-respondData(uuid: number, offset: number, buffer: ArrayBuffer): number--><!--Device-MediaSourceLoadingRequest-respondData(uuid: number, offset: number, buffer: ArrayBuffer): number-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uuid | number | Yes |
| offset | number | Yes |
| buffer | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## respondData

```TypeScript
respondData(uuid: number, offset: number, buffer: ArrayBuffer): number | undefined
```

The interface for application used to send requested data to AVPlayer.

**Since:** 23

<!--Device-MediaSourceLoadingRequest-respondData(uuid: long, offset: long, buffer: ArrayBuffer): int | undefined--><!--Device-MediaSourceLoadingRequest-respondData(uuid: long, offset: long, buffer: ArrayBuffer): int | undefined-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uuid | number | Yes |
| offset | number | Yes |
| buffer | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## respondHeader

```TypeScript
respondHeader(uuid: number, header?: Record<string, string>, redirectUrl?: string): void
```

Sends response header information to the player. This API must be called before the first call to [respondData](#responddata).

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MediaSourceLoadingRequest-respondHeader(uuid: long, header?: Record<string, string>, redirectUrl?: string): void--><!--Device-MediaSourceLoadingRequest-respondHeader(uuid: long, header?: Record<string, string>, redirectUrl?: string): void-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uuid | number | Yes |
| [header](#header) | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, string&gt; | No |
| redirectUrl | string | No |

## header

```TypeScript
header?: Record<string, string>
```

HTTP request header. If the header exists, the application should set the header information in the HTTP request when downloading data.

**Type:** [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, string&gt;

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MediaSourceLoadingRequest-header?: Record<string, string>--><!--Device-MediaSourceLoadingRequest-header?: Record<string, string>-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## url

```TypeScript
url: string
```

Resource URL, which is the path to the resource that the application needs to open.

**Type:** string

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MediaSourceLoadingRequest-url: string--><!--Device-MediaSourceLoadingRequest-url: string-End-->

**System capability:** SystemCapability.Multimedia.Media.Core
