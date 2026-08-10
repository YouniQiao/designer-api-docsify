# OnSslErrorEventCallback

```TypeScript
type OnSslErrorEventCallback = (sslErrorEvent: SslErrorEvent) => void
```

SSL错误事件的回调函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-type OnSslErrorEventCallback = (sslErrorEvent: SslErrorEvent) => void--><!--Device-unnamed-type OnSslErrorEventCallback = (sslErrorEvent: SslErrorEvent) => void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sslErrorEvent | [SslErrorEvent](../arkts-apis/arkts-arkweb-web-sslerrorevent-i.md) | Yes | callback information of onSslErrorEvent. |

