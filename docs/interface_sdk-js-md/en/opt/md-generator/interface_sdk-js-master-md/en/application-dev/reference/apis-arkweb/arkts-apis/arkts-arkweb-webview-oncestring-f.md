# once_string

## Modules to Import

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## once_string

```TypeScript
function once(type: string, callback: Callback<void>): void
```

Registers a one-time callback for web events of the specified type. Currently, only **webInited** is supported. This callback is triggered when the Web engine initialization is complete. When the first **Web** component is loaded in an application, the web engine is initialized. When other **Web** components are loaded in the same application, **once()** is not triggered. When the first **Web** component is loaded after the last **Web** component is destroyed in the application, the web engine will be initialized again.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-webview-function once(type: string, callback: Callback<void>): void--><!--Device-webview-function once(type: string, callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

webview.once("webInited", () => {
  console.info("configCookieSync");
  webview.WebCookieManager.configCookieSync("https://www.example.com", "a=b");
})

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```
