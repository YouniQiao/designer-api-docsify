# ProxyRule

The ProxyRule used by insertProxyRule.

**Since:** 15

<!--Device-webview-class ProxyRule--><!--Device-webview-class ProxyRule-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from 'kits/@kit.ArkWeb';
```

## getSchemeFilter

```TypeScript
getSchemeFilter(): ProxySchemeFilter
```

Returns the scheme filter used for this rule.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-ProxyRule-getSchemeFilter(): ProxySchemeFilter--><!--Device-ProxyRule-getSchemeFilter(): ProxySchemeFilter-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ProxySchemeFilter](arkts-arkweb-webview-proxyschemefilter-e.md) |

## getUrl

```TypeScript
getUrl(): string
```

Returns the proxy URL.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-ProxyRule-getUrl(): string--><!--Device-ProxyRule-getUrl(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |
