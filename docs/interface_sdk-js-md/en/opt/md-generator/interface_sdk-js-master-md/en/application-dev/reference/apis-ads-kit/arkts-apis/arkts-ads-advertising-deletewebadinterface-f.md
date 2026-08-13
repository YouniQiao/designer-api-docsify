# deleteWebAdInterface

## Modules to Import

```TypeScript
import { advertising } from '@kit.AdsKit';
```

## deleteWebAdInterface

```TypeScript
function deleteWebAdInterface(controller: web_webview.WebviewController, needRefresh: boolean): void
```

Deletes the ad JavaScript object injected through **registerWebAdInterface** (this API is only open to some pre-installed system applications).

**Since:** 16

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 16.

<!--Device-advertising-function deleteWebAdInterface(controller: web_webview.WebviewController, needRefresh: boolean): void--><!--Device-advertising-function deleteWebAdInterface(controller: web_webview.WebviewController, needRefresh: boolean): void-End-->

**System capability:** SystemCapability.Advertising.Ads

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| controller | web_webview.WebviewController | Yes |
| needRefresh | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [21800001](../errorcode-ads.md#21800001-internal-system-error) |

## Examples

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
