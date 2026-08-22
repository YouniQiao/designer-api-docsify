# BackForwardCacheOptions

This class is used to set back forward cache options.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-webview-class BackForwardCacheOptions--><!--Device-webview-class BackForwardCacheOptions-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor()
```

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-BackForwardCacheOptions-constructor()--><!--Device-BackForwardCacheOptions-constructor()-End-->

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

## size

```TypeScript
size: int
```

Set the maximum size of pages that can cache. Default is 1, max is 50.

**类型：** int

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-BackForwardCacheOptions-size: int--><!--Device-BackForwardCacheOptions-size: int-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## timeToLive

```TypeScript
timeToLive: int
```

Set the lifetime in seconds in the BackForwardCache. The value should be an integer.Unit: seconds. Default is 600.

**类型：** int

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-BackForwardCacheOptions-timeToLive: int--><!--Device-BackForwardCacheOptions-timeToLive: int-End-->

**系统能力：** SystemCapability.Web.Webview.Core

