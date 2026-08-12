# deleteWebAdInterface

## deleteWebAdInterface

```TypeScript
function deleteWebAdInterface(controller: web_webview.WebviewController, needRefresh: boolean): void
```

删除通过registerWebAdInterface注入的广告JavaScript对象（该接口仅对部分系统预置应用开放）。

**起始版本：** 16

**原子化服务API：** 从API版本16开始，该接口支持在原子化服务API中使用。

<!--Device-advertising-function deleteWebAdInterface(controller: web_webview.WebviewController, needRefresh: boolean): void--><!--Device-advertising-function deleteWebAdInterface(controller: web_webview.WebviewController, needRefresh: boolean): void-End-->

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| controller | web_webview.WebviewController | 是 |
| needRefresh | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [21800001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ads-kit/errorcode-ads.md#21800001-系统内部错误) |

## 示例

```TypeScript
import { advertising } from '@kit.AdsKit';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  private webViewController: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('deleteWebAdInterface')
        .onClick(() => {
          advertising.deleteWebAdInterface(this.webViewController, true);
        })

      Web({ src: 'https://www.example.com', controller: this.webViewController })
    }
    .width('100%')
    .height('100%')
  }
}
```
