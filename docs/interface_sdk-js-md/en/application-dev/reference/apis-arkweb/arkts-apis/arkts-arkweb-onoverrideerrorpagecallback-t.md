# OnOverrideErrorPageCallback

```TypeScript
export type OnOverrideErrorPageCallback = (errorPageEvent: OnErrorReceiveEvent) => string
```

The callback of onOverrideErrorPage.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export type OnOverrideErrorPageCallback = (errorPageEvent: OnErrorReceiveEvent) => string--><!--Device-unnamed-export type OnOverrideErrorPageCallback = (errorPageEvent: OnErrorReceiveEvent) => string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| errorPageEvent | [OnErrorReceiveEvent](arkts-arkweb-web-onerrorreceiveevent-i.md) | Yes | The information of error. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Return an HTML text content encoded in Base64. |

