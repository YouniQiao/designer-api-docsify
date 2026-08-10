# OnDownloadStartEvent

定义通知主应用开始下载一个文件。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface OnDownloadStartEvent--><!--Device-unnamed-declare interface OnDownloadStartEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## contentDisposition

```TypeScript
contentDisposition: string
```

服务器返回的 Content-Disposition响应头，服务器可能返回空。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnDownloadStartEvent-contentDisposition: string--><!--Device-OnDownloadStartEvent-contentDisposition: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## contentLength

```TypeScript
contentLength: number
```

服务器返回文件的长度。单位：字节。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnDownloadStartEvent-contentLength: number--><!--Device-OnDownloadStartEvent-contentLength: number-End-->

**System capability:** SystemCapability.Web.Webview.Core

## mimetype

```TypeScript
mimetype: string
```

服务器返回内容媒体类型（MIME）信息。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnDownloadStartEvent-mimetype: string--><!--Device-OnDownloadStartEvent-mimetype: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## url

```TypeScript
url: string
```

文件下载的URL。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnDownloadStartEvent-url: string--><!--Device-OnDownloadStartEvent-url: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## userAgent

```TypeScript
userAgent: string
```

用于下载的用户代理。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnDownloadStartEvent-userAgent: string--><!--Device-OnDownloadStartEvent-userAgent: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

