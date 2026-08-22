# BackForwardCacheOptions

BackForwardCacheOptions是ArkWeb框架中用于配置Web组件前进后退缓存（BFCache）行为的参数类。BFCache是一种页面缓存机制，当用户在浏览历史中前进或后退时，可将页面完整快照（包括 JavaScript状态）缓存起来，实现瞬时加载效果，显著提升用户体验。通过BackForwardCacheOptions，开发者可以控制每个Web组件允许缓存的最大页面个数以及页面在缓存中的最长停留时间。

**起始版本：** 12

<!--Device-webview-class BackForwardCacheOptions--><!--Device-webview-class BackForwardCacheOptions-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## constructor

```TypeScript
constructor()
```

BackForwardCacheOptions的构造函数。

**起始版本：** 12

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
size: number
```

设置每个Web组件允许缓存的最大页面个数。

默认为1，最大可设置为50。

设置为0或负数时，前进后退缓存功能不生效。

Web组件会根据内存压力对缓存进行回收。

**类型：** number

**起始版本：** 12

<!--Device-BackForwardCacheOptions-size: number--><!--Device-BackForwardCacheOptions-size: number-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## timeToLive

```TypeScript
timeToLive: number
```

设置每个Web组件允许页面在前进后退缓存中停留的时间。

设置为0或负数时，前进后退缓存功能不生效。

默认值：600。

**类型：** number

**起始版本：** 12

<!--Device-BackForwardCacheOptions-timeToLive: number--><!--Device-BackForwardCacheOptions-timeToLive: number-End-->

**系统能力：** SystemCapability.Web.Webview.Core

