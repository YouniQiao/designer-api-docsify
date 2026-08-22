# PrefetchOptions

Defines the PrefetchOptions class.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-webview-class PrefetchOptions--><!--Device-webview-class PrefetchOptions-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor()
```

Constructor for PrefetchOptions.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-PrefetchOptions-constructor()--><!--Device-PrefetchOptions-constructor()-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**示例**

ArkTS-Dyn示例：

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
  controller: webview.WebviewController = new webview.WebviewController();
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Web, Button, Column, State, Component, Entry } from '@kit.ArkUI';
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
  controller: webview.WebviewController = new webview.WebviewController(undefined)
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

加载的html文件。

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

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-PrefetchOptions-ignoreCacheControlNoStore: boolean--><!--Device-PrefetchOptions-ignoreCacheControlNoStore: boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## minTimeBetweenPrefetchesMs

```TypeScript
minTimeBetweenPrefetchesMs: int
```

‌Set prefetch page interval limit. <p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> Unit: ms. Default 500ms (ensures only one successful prefetch within 500ms). The interval throttles prefetch frequency to balance performance and resource usage.

**类型：** int

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-PrefetchOptions-minTimeBetweenPrefetchesMs: int--><!--Device-PrefetchOptions-minTimeBetweenPrefetchesMs: int-End-->

**系统能力：** SystemCapability.Web.Webview.Core

