# HttpAuthHandler

HttpAuthHandler is a handler class used by the Web component to process HTTP authentication requests. When the server returns 401 Unauthorized to request authentication, the Web component obtains an HttpAuthHandler instance through the onHttpAuthRequest event callback, and the app decides whether to provide authentication credentials. For sample code, see [onHttpAuthRequest](arkts-arkweb-web-attribute.md#onhttpauthrequest).

**Since:** 9

<!--Device-unnamed-declare class HttpAuthHandler--><!--Device-unnamed-declare class HttpAuthHandler-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@kit.ArkWeb';
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
import { webNativeMessagingExtensionManager } from '@kit.ArkWeb';
import { webview } from '@kit.ArkWeb';
import { WebNativeMessagingExtensionContext } from '@kit.ArkWeb';
```

## cancel

```TypeScript
cancel(): void
```

Cancels HTTP authentication as requested by the user.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HttpAuthHandler-cancel(): void--><!--Device-HttpAuthHandler-cancel(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onDataResubmitted((event) => {
          console.info('onDataResubmitted');
          event.handler.cancel();
        })
    }
  }
}
```

## confirm

```TypeScript
confirm(userName: string, password: string): boolean
```

Performs HTTP authentication with the user name and password provided by the user.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HttpAuthHandler-confirm(userName: string, password: string): boolean--><!--Device-HttpAuthHandler-confirm(userName: string, password: string): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userName | string | Yes | HTTP authentication user name, which must be a non-empty string. |
| password | string | Yes | HTTP authentication password, which must be a non-empty string. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if authentication succeeds; returns **false** otherwise. |

## constructor

```TypeScript
constructor()
```

Constructs an **HttpAuthHandler**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HttpAuthHandler-constructor()--><!--Device-HttpAuthHandler-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isHttpAuthInfoSaved

```TypeScript
isHttpAuthInfoSaved(): boolean
```

Checks whether the credentials stored for the current host are applicable. The credentials are not applicable if they have been rejected by the server in the current request.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HttpAuthHandler-isHttpAuthInfoSaved(): boolean--><!--Device-HttpAuthHandler-isHttpAuthInfoSaved(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the stored credentials are applicable; false otherwise. |

