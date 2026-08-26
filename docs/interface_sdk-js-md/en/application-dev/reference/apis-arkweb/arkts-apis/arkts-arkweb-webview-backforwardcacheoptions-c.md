# BackForwardCacheOptions

Implements a **BackForwardCacheOptions** object to set back-forward cache options of the **Web** component.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

Constructs a **BackForwardCacheOptions** object.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

**Examples**

```TypeScript
// xxx.ets
import { webview, WebNetErrorList } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('response').onClick(() => {
        let response = new webview.WebSchemeHandlerResponse();
        try {
          response.setUrl("http://www.example.com")
          response.setStatus(200)
          response.setStatusText("OK")
          response.setMimeType("text/html")
          response.setEncoding("utf-8")
          response.setHeaderByName("header1", "value1", false)
          response.setNetErrorCode(WebNetErrorList.NET_OK)
          console.info("[schemeHandler] getUrl:" + response.getUrl())
          console.info("[schemeHandler] getStatus:" + response.getStatus())
          console.info("[schemeHandler] getStatusText:" + response.getStatusText())
          console.info("[schemeHandler] getMimeType:" + response.getMimeType())
          console.info("[schemeHandler] getEncoding:" + response.getEncoding())
          console.info("[schemeHandler] getHeaderByName:" + response.getHeaderByName("header1"))
          console.info("[schemeHandler] getNetErrorCode:" + response.getNetErrorCode())

        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'https://www.example.com', controller: this.controller })
    }
  }
}
```

## size

```TypeScript
size: number
```

The maximum number of pages that can be cached in a Web component.The default value is 1, and the maximum value is 50.If this parameter is set to 0 or a negative value, the back-forward cache is disabled.The Web component reclaims the cache for memory pressure.

**Type:** number

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

## timeToLive

```TypeScript
timeToLive: number
```

The time that a Web component allows a page to stay in the back-forward cache.If this parameter is set to 0 or a negative value, the back-forward cache is disabled.Default value: 600Unit: second

**Type:** number

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core
