# BackForwardCacheSupportedFeatures

This class is used to enable back forward cache supported features.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-webview-class BackForwardCacheSupportedFeatures--><!--Device-webview-class BackForwardCacheSupportedFeatures-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-BackForwardCacheSupportedFeatures-constructor()--><!--Device-BackForwardCacheSupportedFeatures-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Examples**

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

Whether cache the pages that use media take over. Default is false;

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-BackForwardCacheSupportedFeatures-mediaTakeOver: boolean--><!--Device-BackForwardCacheSupportedFeatures-mediaTakeOver: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## nativeEmbed

```TypeScript
nativeEmbed: boolean
```

Whether cache the pages that use native embed. Default is false;

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-BackForwardCacheSupportedFeatures-nativeEmbed: boolean--><!--Device-BackForwardCacheSupportedFeatures-nativeEmbed: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

