# ProxyRule

The ProxyRule used by insertProxyRule.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-webview-class ProxyRule--><!--Device-webview-class ProxyRule-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## getSchemeFilter

```TypeScript
getSchemeFilter(): ProxySchemeFilter
```

Returns the scheme filter used for this rule.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-ProxyRule-getSchemeFilter(): ProxySchemeFilter--><!--Device-ProxyRule-getSchemeFilter(): ProxySchemeFilter-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [ProxySchemeFilter](arkts-webview-proxyschemefilter-e.md) | The scheme filter used for this rule. |

## getUrl

```TypeScript
getUrl(): string
```

Returns the proxy URL.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-ProxyRule-getUrl(): string--><!--Device-ProxyRule-getUrl(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | The proxy URL. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getUrl')
        .onClick(() => {
          try {
            let url = this.controller.getUrl();
            console.info("url: " + url);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

