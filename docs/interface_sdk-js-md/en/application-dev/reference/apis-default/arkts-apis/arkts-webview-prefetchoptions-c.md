# PrefetchOptions

Defines the PrefetchOptions class.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-webview-class PrefetchOptions--><!--Device-webview-class PrefetchOptions-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

Constructor for PrefetchOptions.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-PrefetchOptions-constructor()--><!--Device-PrefetchOptions-constructor()-End-->

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

## ignoreCacheControlNoStore

```TypeScript
ignoreCacheControlNoStore: boolean
```

Set whether to ignore Cache-Control: no-store‌. <p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> This setting controls whether prefetch operations bypass the HTTP Cache-Control: no-store directive. Important‌: Default behavior (false) aligns with HTTP security standards. Overriding (true) requires explicit risk assessment for non-sensitive resources.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-PrefetchOptions-ignoreCacheControlNoStore: boolean--><!--Device-PrefetchOptions-ignoreCacheControlNoStore: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## minTimeBetweenPrefetchesMs

```TypeScript
minTimeBetweenPrefetchesMs: int
```

‌Set prefetch page interval limit. <p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> Unit: ms. Default 500ms (ensures only one successful prefetch within 500ms). The interval throttles prefetch frequency to balance performance and resource usage.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-PrefetchOptions-minTimeBetweenPrefetchesMs: int--><!--Device-PrefetchOptions-minTimeBetweenPrefetchesMs: int-End-->

**System capability:** SystemCapability.Web.Webview.Core

