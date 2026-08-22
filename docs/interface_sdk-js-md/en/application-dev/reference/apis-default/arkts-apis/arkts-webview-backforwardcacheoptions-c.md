# BackForwardCacheOptions

This class is used to set back forward cache options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-webview-class BackForwardCacheOptions--><!--Device-webview-class BackForwardCacheOptions-End-->

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

<!--Device-BackForwardCacheOptions-constructor()--><!--Device-BackForwardCacheOptions-constructor()-End-->

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

## size

```TypeScript
size: int
```

Set the maximum size of pages that can cache. Default is 1, max is 50.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-BackForwardCacheOptions-size: int--><!--Device-BackForwardCacheOptions-size: int-End-->

**System capability:** SystemCapability.Web.Webview.Core

## timeToLive

```TypeScript
timeToLive: int
```

Set the lifetime in seconds in the BackForwardCache. The value should be an integer.Unit: seconds. Default is 600.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-BackForwardCacheOptions-timeToLive: int--><!--Device-BackForwardCacheOptions-timeToLive: int-End-->

**System capability:** SystemCapability.Web.Webview.Core

