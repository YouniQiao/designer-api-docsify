# MediaSourceLoadingRequest

用于定义加载请求的对象。应用程序通过该对象来获取请求的资源位置，通过该对象和播放器进行数据交互。 > **说明：** > > - 本Interface首批接口从API version 18开始支持。

**起始版本：** 23

<!--Device-unnamed-interface MediaSourceLoadingRequest--><!--Device-unnamed-interface MediaSourceLoadingRequest-End-->

**系统能力：** SystemCapability.Multimedia.Media.Core

## 导入模块

```TypeScript
```

## finishLoading

```TypeScript
finishLoading(uuid: number, state: LoadingRequestError): void
```

应用程序用于通知播放器当前请求状态的接口。针对服务侧请求的单个资源，推送完全部资源后需要发送LOADING_ERROR_SUCCESS状态告知该资源推送结束。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-MediaSourceLoadingRequest-finishLoading(uuid: long, state: LoadingRequestError): void--><!--Device-MediaSourceLoadingRequest-finishLoading(uuid: long, state: LoadingRequestError): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uuid | number | 是 |
| state | [LoadingRequestError](arkts-media-multimedia-media-loadingrequesterror-e.md) | 是 |

## respondData

```TypeScript
respondData(uuid: number, offset: number, buffer: ArrayBuffer): number
```

用于应用程序向播放器发送数据。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-MediaSourceLoadingRequest-respondData(uuid: number, offset: number, buffer: ArrayBuffer): number--><!--Device-MediaSourceLoadingRequest-respondData(uuid: number, offset: number, buffer: ArrayBuffer): number-End-->

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uuid | number | 是 |
| offset | number | 是 |
| buffer | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## respondData

```TypeScript
respondData(uuid: number, offset: number, buffer: ArrayBuffer): number | undefined
```

The interface for application used to send requested data to AVPlayer.

**起始版本：** 23

<!--Device-MediaSourceLoadingRequest-respondData(uuid: long, offset: long, buffer: ArrayBuffer): int | undefined--><!--Device-MediaSourceLoadingRequest-respondData(uuid: long, offset: long, buffer: ArrayBuffer): int | undefined-End-->

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uuid | number | 是 |
| offset | number | 是 |
| buffer | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## respondHeader

```TypeScript
respondHeader(uuid: number, header?: Record<string, string>, redirectUrl?: string): void
```

用于应用程序向播放器发送响应头信息，应在第一次调用 [respondData](#responddata) 方法之前调用。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-MediaSourceLoadingRequest-respondHeader(uuid: long, header?: Record<string, string>, redirectUrl?: string): void--><!--Device-MediaSourceLoadingRequest-respondHeader(uuid: long, header?: Record<string, string>, redirectUrl?: string): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uuid | number | 是 |
| [header](#header) | Record & lt;string, string & gt; | 否 |
| redirectUrl | string | 否 |

## header

```TypeScript
header?: Record<string, string>
```

网络请求标头，如果存在，需要应用在下载数据时将头信息设置到HTTP请求中。

**类型：** Record&lt;string, string&gt;

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-MediaSourceLoadingRequest-header?: Record<string, string>--><!--Device-MediaSourceLoadingRequest-header?: Record<string, string>-End-->

**系统能力：** SystemCapability.Multimedia.Media.Core

## url

```TypeScript
url: string
```

资源URL，需要应用程序打开的资源路径。

**类型：** string

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-MediaSourceLoadingRequest-url: string--><!--Device-MediaSourceLoadingRequest-url: string-End-->

**系统能力：** SystemCapability.Multimedia.Media.Core
