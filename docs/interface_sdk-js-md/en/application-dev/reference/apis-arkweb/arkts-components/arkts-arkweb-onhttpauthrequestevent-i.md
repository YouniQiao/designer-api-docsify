# OnHttpAuthRequestEvent

定义通知收到http auth认证请求。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface OnHttpAuthRequestEvent--><!--Device-unnamed-declare interface OnHttpAuthRequestEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handler

```TypeScript
handler: HttpAuthHandler
```

通知Web组件用户操作行为。

**Type:** [HttpAuthHandler](../arkts-apis/arkts-arkweb-web-httpauthhandler-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnHttpAuthRequestEvent-handler: HttpAuthHandler--><!--Device-OnHttpAuthRequestEvent-handler: HttpAuthHandler-End-->

**System capability:** SystemCapability.Web.Webview.Core

## host

```TypeScript
host: string
```

HTTP身份验证凭据应用的主机。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnHttpAuthRequestEvent-host: string--><!--Device-OnHttpAuthRequestEvent-host: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## realm

```TypeScript
realm: string
```

HTTP身份验证凭据应用的域。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnHttpAuthRequestEvent-realm: string--><!--Device-OnHttpAuthRequestEvent-realm: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

