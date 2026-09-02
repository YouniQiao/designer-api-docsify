# ProxyRule

ProxyRule is a class for read-only proxy rule information in the ArkWeb framework, obtained through the [getProxyRules](arkts-arkweb-webview-proxyconfig-c.md#getproxyrules) method. When a developer configures proxy rules through ProxyConfig, the configured rule list can be obtained through getProxyRules, with each rule corresponding to a ProxyRule object used to query the detailed information of the rule.

ProxyRule provides two methods: getSchemeFilter is used to obtain the protocol filter corresponding to the proxy rule (such as MATCH_ALL_SCHEMES, MATCH_HTTP, MATCH_HTTPS, etc.), and getUrl is used to obtain the proxy server URL information specified in the proxy rule. The ProxyRule object is read-only, created by the system when configuring proxy rules, and the app can only query its content but cannot modify it.

**Since:** 15

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## getSchemeFilter

```TypeScript
getSchemeFilter(): ProxySchemeFilter
```

Obtains the **ProxySchemeFilter** information in the proxy rule.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [ProxySchemeFilter](arkts-arkweb-webview-proxyschemefilter-e.md) | ProxySchemeFilter** in the proxy rule. |

**Examples**

For details about the sample code, see [removeProxyOverride](./arkts-apis-webview-ProxyController.md#removeproxyoverride).

## getUrl

```TypeScript
getUrl(): string
```

Obtains the URL specified in the proxy rule.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | URL information of the proxy in the proxy rule. |

**Examples**

For details about the sample code, see [removeProxyOverride](./arkts-apis-webview-ProxyController.md#removeproxyoverride).

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();

  build() {
    Column() {
      Button('setDownloadDelegate')
        .onClick(() => {
          try {
            this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
              console.info("will start a download, url:" + webDownloadItem.getUrl());
              // Pass in a download path and start the download.
              webDownloadItem.start("/data/storage/el2/base/cache/web/" + webDownloadItem.getSuggestedFileName());
            })
            this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
              console.info("download update percent complete: " + webDownloadItem.getPercentComplete());
            })
            this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
              console.error("download failed guid: " + webDownloadItem.getGuid());
            })
            this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
              console.info("download finish guid: " + webDownloadItem.getGuid());
            })
            this.controller.setDownloadDelegate(this.delegate);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('startDownload')
        .onClick(() => {
          try {
            this.controller.startDownload('https://www.example.com');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

For details about the sample code, see constructor.

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
