# BackForwardCacheSupportedFeatures

BackForwardCacheSupportedFeatures is a configuration class in the ArkWeb framework used to selectively allow pages that use specific web features to enter the Back/Forward Cache (BFCache). By default, pages using features such as native embed or media takeover are blocked from entering BFCache, because the browser cannot safely save and restore these complex states bound to system controls. By setting the properties in this class, developers can explicitly allow pages with these features to enter BFCache, but they must manage the lifecycle of the related system controls themselves to avoid resource leaks. For the complete sample code, see [enableBackForwardCache](../../apis-default/arkts-apis/arkts-webview-webviewcontroller-c.md#enablebackforwardcache).

**Since:** 12

<!--Device-webview-class BackForwardCacheSupportedFeatures--><!--Device-webview-class BackForwardCacheSupportedFeatures-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## constructor

```TypeScript
constructor()
```

Constructs a **BackForwardCacheSupportedFeatures** object.

**Since:** 12

<!--Device-BackForwardCacheSupportedFeatures-constructor()--><!--Device-BackForwardCacheSupportedFeatures-constructor()-End-->

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

## mediaTakeOver

```TypeScript
mediaTakeOver: boolean
```

Whether to allow pages using media takeover to enter the back-forward cache.If allowed, you need to maintain the lifecycle of system controls created for video elements to avoid resource leaks.true: allowed; false: not allowed.Default value: false.

**Type:** boolean

**Since:** 12

<!--Device-BackForwardCacheSupportedFeatures-mediaTakeOver: boolean--><!--Device-BackForwardCacheSupportedFeatures-mediaTakeOver: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## nativeEmbed

```TypeScript
nativeEmbed: boolean
```

Whether to allow pages using native embed to enter the back-forward cache.If allowed, you need to maintain the lifecycle of system controls created for native embed elements to avoid resource leaks.true: allowed; false: not allowed.Default value: false.

**Type:** boolean

**Since:** 12

<!--Device-BackForwardCacheSupportedFeatures-nativeEmbed: boolean--><!--Device-BackForwardCacheSupportedFeatures-nativeEmbed: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

