# PrefetchOptions

PrefetchOptions is a configuration class in the ArkWeb framework for customizing web page prefetch behavior. It is set through the prefetch-related API of [prefetchPage](../../apis-default/arkts-apis/arkts-webview-webviewcontroller-c.md#prefetchpage), and the customizable settings include whether to ignore Cache-Control: no-store in the response header and the minimum time interval between two prefetches.

**Since:** 21

<!--Device-webview-class PrefetchOptions--><!--Device-webview-class PrefetchOptions-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **PrefetchOptions** instance.

**Since:** 21

<!--Device-PrefetchOptions-constructor()--><!--Device-PrefetchOptions-constructor()-End-->

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
  schemeHandler: webview.WebSchemeHandler = new webview.WebSchemeHandler();

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
          console.info("[schemeHandler] getHeaderByValue:" + response.getHeaderByName("header1"))
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

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class WebObj {
  constructor() {
  }

  webTest(): string {
    console.info('Web test');
    return "Web test";
  }

  webString(): void {
    console.info('Web test toString');
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController()
  @State webTestObj: WebObj = new WebObj();

  build() {
    Column() {
      Button('refresh')
        .onClick(() => {
          try {
            this.controller.refresh();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('deleteJavaScriptRegister')
        .onClick(() => {
          try {
            this.controller.deleteJavaScriptRegister("objTestName");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: '', controller: this.controller })
        .javaScriptAccess(true)
        .onControllerAttached(() => {
          this.controller.loadUrl($rawfile("index.html"));
          this.controller.registerJavaScriptProxy(this.webTestObj, "objTestName", ["webTest", "webString"]);
        })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
    <head>
      <meta charset="utf-8">
    </head>
    <body>
      <button type="button" onclick="htmlTest()">Click Me!</button>
      <p id="demo"></p>
      <p id="webDemo"></p>
      <script type="text/javascript">
        function htmlTest() {
          // This function call expects to return "Web test"
          let webStr = objTestName.webTest();
          document.getElementById("webDemo").innerHTML=webStr;
          console.info('objTestName.webTest result:'+ webStr)
        }
      </script>
    </body>
</html>
```

## ignoreCacheControlNoStore

```TypeScript
ignoreCacheControlNoStore: boolean
```

Sets whether to ignore Cache-Control: no-store in the response header.

If set to true, the header is ignored; if set to false, it is not ignored.

**Type:** boolean

**Since:** 21

<!--Device-PrefetchOptions-ignoreCacheControlNoStore: boolean--><!--Device-PrefetchOptions-ignoreCacheControlNoStore: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## minTimeBetweenPrefetchesMs

```TypeScript
minTimeBetweenPrefetchesMs: number
```

Sets the minimum time interval between two web page prefetches.

During each prefetch, the interval from the last prefetch is calculated. If it is less than the set value, the current prefetch is canceled.

Value range: [0, 500].

If set to a negative number, the default value 0 is used.

Unit: ms

**Type:** number

**Since:** 21

<!--Device-PrefetchOptions-minTimeBetweenPrefetchesMs: number--><!--Device-PrefetchOptions-minTimeBetweenPrefetchesMs: number-End-->

**System capability:** SystemCapability.Web.Webview.Core

