# ProxyRule

The ProxyRule used by insertProxyRule.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-webview-class ProxyRule--><!--Device-webview-class ProxyRule-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
```

## getSchemeFilter

```TypeScript
getSchemeFilter(): ProxySchemeFilter
```

Returns the scheme filter used for this rule.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-ProxyRule-getSchemeFilter(): ProxySchemeFilter--><!--Device-ProxyRule-getSchemeFilter(): ProxySchemeFilter-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ProxySchemeFilter](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-proxyschemefilter-e.md) | The scheme filter used for this rule. |

## getUrl

```TypeScript
getUrl(): string
```

Returns the proxy URL.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-ProxyRule-getUrl(): string--><!--Device-ProxyRule-getUrl(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | The proxy URL. |

**示例**

ArkTS-Dyn示例：

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getUrl')
        .onClick(() => {
          try {
            let url = this.controller.getUrl();
            console.info("url: " + url);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { Web, Column, Component, Entry, Button } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@ohos.base';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Button('getUrl')
        .onClick(() => {
          try {
            let url = this.controller.getUrl();
            console.info("url: " + url);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

