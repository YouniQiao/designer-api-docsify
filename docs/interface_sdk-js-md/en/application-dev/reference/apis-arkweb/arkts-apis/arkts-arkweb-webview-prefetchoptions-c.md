# PrefetchOptions

PrefetchOptions is a configuration class in the ArkWeb framework for customizing web page prefetch behavior. It is set through the prefetch-related API of [prefetchPage](arkts-arkweb-webview-webviewcontroller-c.md#prefetchpage), and the customizable settings include whether to ignore Cache-Control: no-store in the response header and the minimum time interval between two prefetches.

**Since:** 21

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **PrefetchOptions** instance.

**Since:** 21

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

## ignoreCacheControlNoStore

```TypeScript
ignoreCacheControlNoStore: boolean
```

Sets whether to ignore Cache-Control: no-store in the response header.If set to true, the header is ignored; if set to false, it is not ignored.

**Type:** boolean

**Since:** 21

**System capability:** SystemCapability.Web.Webview.Core

## minTimeBetweenPrefetchesMs

```TypeScript
minTimeBetweenPrefetchesMs: number
```

Sets the minimum time interval between two web page prefetches.During each prefetch, the interval from the last prefetch is calculated. If it is less than the set value, the current prefetch is canceled.Value range: [0, 500].If set to a negative number, the default value 0 is used.Unit: ms

**Type:** number

**Since:** 21

**System capability:** SystemCapability.Web.Webview.Core
