# BackForwardCacheSupportedFeatures

BackForwardCacheSupportedFeatures是ArkWeb框架中用于选择性控制允许使用了特定Web特性的页面可以进入前进后退缓存（BFCache）的配置类。默认情况下，使用同层渲染或视频托管等特性的页面会被阻 止进入BFCache，因为浏览器无法安全地保存和恢复这些与系统控件绑定的复杂状态。通过设置该类中的属性，开发者可以显式允许这些特性的页面进入BFCache，但需注意自行维护相关系统控件的生命周期，避免造成资源泄漏。完整示例代码参考 [enableBackForwardCache](../../apis-default/arkts-apis/arkts-webview-webviewcontroller-c.md#enablebackforwardcache)。

**起始版本：** 12

<!--Device-webview-class BackForwardCacheSupportedFeatures--><!--Device-webview-class BackForwardCacheSupportedFeatures-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## constructor

```TypeScript
constructor()
```

Constructs a **BackForwardCacheSupportedFeatures** object.

**起始版本：** 12

<!--Device-BackForwardCacheSupportedFeatures-constructor()--><!--Device-BackForwardCacheSupportedFeatures-constructor()-End-->

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

## mediaTakeOver

```TypeScript
mediaTakeOver: boolean
```

是否允许使用视频托管的页面进入前进后退缓存。

如果设置为允许，需要维护为视频元素创建的系统控件的生命周期，避免造成资源泄漏。

true：允许，false：不允许。

默认值：false。

**类型：** boolean

**起始版本：** 12

<!--Device-BackForwardCacheSupportedFeatures-mediaTakeOver: boolean--><!--Device-BackForwardCacheSupportedFeatures-mediaTakeOver: boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## nativeEmbed

```TypeScript
nativeEmbed: boolean
```

是否允许使用同层渲染的页面进入前进后退缓存。

如果设置为允许，需要维护为同层渲染元素创建的系统控件的生命周期，避免造成资源泄漏。

true：允许，false：不允许。

默认值：false。

**类型：** boolean

**起始版本：** 12

<!--Device-BackForwardCacheSupportedFeatures-nativeEmbed: boolean--><!--Device-BackForwardCacheSupportedFeatures-nativeEmbed: boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

