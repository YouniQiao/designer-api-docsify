# createMediaSourceWithUrl

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createMediaSourceWithUrl

```TypeScript
function createMediaSourceWithUrl(url: string, headers?: Record<string, string>): MediaSource
```

创建流媒体预下载媒体来源实例方法。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-media-function createMediaSourceWithUrl(url: string, headers?: Record<string, string>): MediaSource--><!--Device-media-function createMediaSourceWithUrl(url: string, headers?: Record<string, string>): MediaSource-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | 流媒体预下载媒体来源url，支持的流媒体格式：HLS、HTTP-FLV、Dash、Https。&lt;br&gt; - 本地m3u8的fd路径。 |
| headers | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt; | No | 支持流媒体预下载HttpHeader自定义。不传时为网络请求默认的HttpHeader。<br>**Since:** 13 |

**Return value:**

| Type | Description |
| --- | --- |
| [MediaSource](arkts-media-multimedia-media-mediasource-i.md) | MediaSource返回值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. 3.Parameter verification failed. |
| 5400101 | No memory. |


## createMediaSourceWithUrl

```TypeScript
function createMediaSourceWithUrl(url: string, headers?: Record<string, string>): MediaSource | undefined
```

Creates a media source for streaming media to be pre-downloaded.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-media-function createMediaSourceWithUrl(url: string, headers?: Record<string, string>): MediaSource | undefined--><!--Device-media-function createMediaSourceWithUrl(url: string, headers?: Record<string, string>): MediaSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | : Url of the media source. The following streaming media formats are supported: HLS, HTTP-FLV, DASH, and HTTPS. |
| headers | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt; | No | : Headers attached to network request while player request data. |

**Return value:**

| Type | Description |
| --- | --- |
| [MediaSource](arkts-media-multimedia-media-mediasource-i.md) | MediaSource instance if the operation is successful; returns null otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. 3.Parameter verification failed. |
| 5400101 | No memory. |

