# WebviewController

WebviewController can control various behaviors of Web components (including page navigation, declaring cycle state, JavaScript interaction and so on). A WebviewController object can only control one Web component, and methods on the Webviewcontroller (except static methods) can only be called after the web component is bound to the WebviewController.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-webview-class WebviewController--><!--Device-webview-class WebviewController-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## accessBackward

```TypeScript
accessBackward(): boolean
```

Checks whether the web page can go back.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-accessBackward(): boolean--><!--Device-WebviewController-accessBackward(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if the web page can go back else false. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('accessBackward')
        .onClick(() => {
          try {
            let result = this.controller.accessBackward();
            console.info('result:' + result);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## accessForward

```TypeScript
accessForward(): boolean
```

Checks whether the web page can go forward.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-accessForward(): boolean--><!--Device-WebviewController-accessForward(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if the web page can go forward else false. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('accessForward')
        .onClick(() => {
          try {
            let result = this.controller.accessForward();
            console.info('result:' + result);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## accessStep

```TypeScript
accessStep(step: int): boolean
```

Checks whether the web page can go back or forward the given number of steps.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-accessStep(step: int): boolean--><!--Device-WebviewController-accessStep(step: int): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| step | int | Yes | The number of steps. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if the web page can go back else false. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State steps: number = 2;

  build() {
    Column() {
      Button('accessStep')
        .onClick(() => {
          try {
            let result = this.controller.accessStep(this.steps);
            console.info('result:' + result);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## addIntelligentTrackingPreventionBypassingList

```TypeScript
static addIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void
```

Add bypassing hosts for Intelligent Tracking Prevention.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static addIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void--><!--Device-WebviewController-static addIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hostList | Array&lt;string&gt; | Yes | Hosts that bypass the Intelligent Tracking Prevention. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

**Examples**

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
      Button('addIntelligentTrackingPreventionBypassingList')
        .onClick(() => {
          try {
            let hostList = ["www.test1.com", "www.test2.com", "www.test3.com"];
            webview.WebviewController.addIntelligentTrackingPreventionBypassingList(hostList);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## avoidVisibleViewportBottom

```TypeScript
avoidVisibleViewportBottom(avoidHeight: int): void
```

Sets the bottom avoidance height of the web visible viewport. When setting non-zero height, the position and size of the web component remain unchanged, <br>and the visible viewport upward avoids avoidHeight, as manifested by the web page content raising avoidHeight. <br>This interface is generally used for customizing the bottom avoidance area, and it is not recommended for <br>simultaneous use with clicking the editable area of the web page showing the keyboard. <br>In this case, the keyboardAvoidMode will be OVERLAYS_CONTENT. When setting zero, web page content can be restored and the keyboardAvoidMode will be the value set by keyboardAvoidMode().

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-avoidVisibleViewportBottom(avoidHeight: int): void--><!--Device-WebviewController-avoidVisibleViewportBottom(avoidHeight: int): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| avoidHeight | int | Yes | the height value of the visible viewport avoidance. The valid interval of avoidHeight is [0, the height of web component]. When avoidHeight is out of the valid interval, it takes the boundary value of the interval. <br>Unit: vp. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  avoidHeight: number = 100;

  build() {
    Column() {
      Button('avoid')
        .onClick(() => {
          try {
            this.controller.avoidVisibleViewportBottom(this.avoidHeight);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('reset')
        .onClick(() => {
          try {
            this.controller.avoidVisibleViewportBottom(0);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## backOrForward

```TypeScript
backOrForward(step: int): void
```

Goes forward or back backOrForward in the history of the web page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-backOrForward(step: int): void--><!--Device-WebviewController-backOrForward(step: int): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| step | int | Yes | Steps to go forward or backward. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State step: number = -2;

  build() {
    Column() {
      Button('backOrForward')
        .onClick(() => {
          try {
            this.controller.backOrForward(this.step);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## backward

```TypeScript
backward(): void
```

Goes back in the history of the web page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-backward(): void--><!--Device-WebviewController-backward(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('backward')
        .onClick(() => {
          try {
            this.controller.backward();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## clearBlanklessLoadingCache

```TypeScript
static clearBlanklessLoadingCache(keys?: Array<string>) : void
```

Clears the blankless loading cache of the page with a specified key value.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static clearBlanklessLoadingCache(keys?: Array<string>) : void--><!--Device-WebviewController-static clearBlanklessLoadingCache(keys?: Array<string>) : void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keys | Array&lt;string&gt; | No | The list of key values of pages cached in the blankless loading solution. These key values are specified in getBlanklessInfoKey. The default value is the list of key values of all pages cached in the blankless loading solution. The key length cannot exceed 2048 characters, and the number of keys must be less than or equal to 100. The URL is the same as that input to the Web component during page loading. When the key length exceeds 2048 characters, the key does not take effect. When the number of keys exceeds 100, the first 100 keys are used. If these parameters are left empty, the default values are used. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |  |

**Examples**

```TypeScript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    // If the web page of the application will be greatly changed on June 10, 2025, for example, during product promotion activities, you are advised to clear the frame interpolation to optimize the cache.
    webview.WebviewController.initializeWebEngine();
    let pageUpdateTime: number = Date.UTC(2025, 5, 10, 0, 0, 0, 0);
    let pageUpdateTime1: number = Date.UTC(2025, 5, 11, 0, 0, 0, 0);
    let pageUpdateTimeNow: number = Date.now();
    if (pageUpdateTimeNow > pageUpdateTime && pageUpdateTime < pageUpdateTime1) {
      // Clear the cache of the frame interpolation on the specified page.
      try {
        webview.WebviewController.clearBlanklessLoadingCache(["https://www.example.com", "https://www.example1.com"]);
      } catch (error) {
        console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
      }
    }
    AppStorage.setOrCreate("abilityWant", want);
    console.info("EntryAbility onCreate done");
  }
}
```

## clearClientAuthenticationCache

```TypeScript
clearClientAuthenticationCache(): void
```

Clears the client authentication certificate cache in the Web.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-clearClientAuthenticationCache(): void--><!--Device-WebviewController-clearClientAuthenticationCache(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('clearClientAuthenticationCache')
        .onClick(() => {
          try {
            this.controller.clearClientAuthenticationCache();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## clearHistory

```TypeScript
clearHistory(): void
```

Clears the history in the Web.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-clearHistory(): void--><!--Device-WebviewController-clearHistory(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('clearHistory')
        .onClick(() => {
          try {
            this.controller.clearHistory();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## clearHostIP

```TypeScript
static clearHostIP(hostName: string): void
```

Clear the host name IP address.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static clearHostIP(hostName: string): void--><!--Device-WebviewController-static clearHostIP(hostName: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hostName | string | Yes | Which host name to be cleared. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |

**Examples**

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
      // The setting takes effect before the URL is loaded.
      Button('setHostIP')
        .onClick(() => {
          try {
            webview.WebviewController.setHostIP('www.example.com', '127.0.0.1', 30);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('clearHostIP')
        .onClick(() => {
          try {
            webview.WebviewController.clearHostIP('www.example.com');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## clearIntelligentTrackingPreventionBypassingList

```TypeScript
static clearIntelligentTrackingPreventionBypassingList(): void
```

Clear bypassing hosts for Intelligent Tracking Prevention.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static clearIntelligentTrackingPreventionBypassingList(): void--><!--Device-WebviewController-static clearIntelligentTrackingPreventionBypassingList(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

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
      Button('clearIntelligentTrackingPreventionBypassingList')
        .onClick(() => {
          webview.WebviewController.clearIntelligentTrackingPreventionBypassingList();
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## clearMatches

```TypeScript
clearMatches(): void
```

Clears the highlighting surrounding text matches created by searchAllAsync.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-clearMatches(): void--><!--Device-WebviewController-clearMatches(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('clearMatches')
        .onClick(() => {
          try {
            this.controller.clearMatches();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

## clearPrefetchedResource

```TypeScript
static clearPrefetchedResource(cacheKeyList: Array<string>): void
```

Clears the cache of prefetched resources based on the specified cache key list. The cache key in the input parameter must be the prefetched resource cache key specified by API[prefetchResource](#prefetchresource).

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static clearPrefetchedResource(cacheKeyList: Array<string>): void--><!--Device-WebviewController-static clearPrefetchedResource(cacheKeyList: Array<string>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cacheKeyList | Array&lt;string&gt; | Yes | The keys for memory cache. The key in cacheKeyList only support number and letters. |

**Examples**

```TypeScript
// Index.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: "https://www.example.com/", controller: this.controller })
        .onAppear(() => {
          // Replace "https://www.example1.com/post?e=f&g=h" with a real URL to visit.
          webview.WebviewController.prefetchResource(
            {
              url: "https://www.example1.com/post?e=f&g=h",
              method: "POST",
              formData: "a=x&b=y",
            },
            [{
              headerKey: "c",
              headerValue: "z",
            },],
            "KeyX", 500);
        })
        .onPageEnd(() => {
          // Clear the prefetch cache that is no longer used.
          webview.WebviewController.clearPrefetchedResource(["KeyX",]);
        })
    }
  }
}
```

## clearServiceWorkerWebSchemeHandler

```TypeScript
static clearServiceWorkerWebSchemeHandler(): void
```

Clear all web service worker scheme handlers.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static clearServiceWorkerWebSchemeHandler(): void--><!--Device-WebviewController-static clearServiceWorkerWebSchemeHandler(): void-End-->

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
      Button('clearServiceWorkerWebSchemeHandler')
        .onClick(() => {
          webview.WebviewController.clearServiceWorkerWebSchemeHandler();
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## clearSslCache

```TypeScript
clearSslCache(): void
```

Clears the ssl cache in the Web.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-clearSslCache(): void--><!--Device-WebviewController-clearSslCache(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('clearSslCache')
        .onClick(() => {
          try {
            this.controller.clearSslCache();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## clearWebSchemeHandler

```TypeScript
clearWebSchemeHandler(): void
```

Clear all web scheme handlers for related web component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-clearWebSchemeHandler(): void--><!--Device-WebviewController-clearWebSchemeHandler(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('clearWebSchemeHandler')
        .onClick(() => {
          try {
            this.controller.clearWebSchemeHandler();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## closeAllMediaPresentations

```TypeScript
closeAllMediaPresentations(): void
```

Closes all full-screen videos on a web page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-closeAllMediaPresentations(): void--><!--Device-WebviewController-closeAllMediaPresentations(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('closeAllMediaPresentations')
        .onClick(() => {
          try {
            this.controller.closeAllMediaPresentations();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## closeCamera

```TypeScript
closeCamera(): void
```

Disables the camera capture of the current web page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-closeCamera(): void--><!--Device-WebviewController-closeCamera(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

For the complete sample code, see [startCamera](#startcamera).

## constructor

```TypeScript
constructor(webTag?: string)
```

A constructor used to create a WebviewController object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-constructor(webTag?: string)--><!--Device-WebviewController-constructor(webTag?: string)-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| webTag | string | No | specified the name of the web component, Empty by default. |

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

## createPdf

```TypeScript
createPdf(configuration: PdfConfiguration, callback: AsyncCallback<PdfData>): void
```

Rendering current Web page into Pdf data, return the result in async mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-createPdf(configuration: PdfConfiguration, callback: AsyncCallback<PdfData>): void--><!--Device-WebviewController-createPdf(configuration: PdfConfiguration, callback: AsyncCallback<PdfData>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| configuration | [PdfConfiguration](arkts-webview-pdfconfiguration-i.md) | Yes | configuration for createPdf, including page width and height, etc. {@Link PdfConfiguration} |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PdfData](arkts-webview-pdfdata-c.md)&gt; | Yes | Callbacks execute createPdf results. PdfData is pdf data stream of current web page in Uint8Array {@Link PdfData}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid input parameter. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
import { fileIo as fs } from '@kit.CoreFileKit';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  pdfConfig: webview.PdfConfiguration = {
    width: 8.27,
    height: 11.69,
    marginTop: 0,
    marginBottom: 0,
    marginRight: 0,
    marginLeft: 0,
    shouldPrintBackground: true
  }

  build() {
    Column() {
      Button('SavePDF')
        .onClick(() => {
          this.controller.createPdf(
            this.pdfConfig,
            (error, result: webview.PdfData) => {
              try {
                // Obtain the component context.
                let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                // Obtain the sandbox path and set the PDF file name.
                let filePath = context.filesDir + "/test.pdf";
                let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
                fs.write(file.fd, result.pdfArrayBuffer().buffer).then((writeLen: number) => {
                  console.info("createPDF write data to file succeed and size is:" + writeLen);
                }).catch((err: BusinessError) => {
                  console.error("createPDF write data to file failed with error message: " + err.message +
                    ", error code: " + err.code);
                }).finally(() => {
                  fs.closeSync(file);
                });
              } catch (resError) {
                console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
              }
            });
        })
      Web({ src: "www.example.com", controller: this.controller })
    }
  }
}
```

```TypeScript
import { fileIo as fs } from '@kit.CoreFileKit';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  pdfConfig: webview.PdfConfiguration = {
    width: 8.27,
    height: 11.69,
    marginTop: 0,
    marginBottom: 0,
    marginRight: 0,
    marginLeft: 0,
    shouldPrintBackground: true
  }

  build() {
    Column() {
      Button('SavePDF')
        .onClick(() => {
          this.controller.createPdf(this.pdfConfig)
            .then((result: webview.PdfData) => {
              try {
                // Obtain the component context.
                let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                // Obtain the sandbox path and set the PDF file name.
                let filePath = context.filesDir + "/test.pdf";
                let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
                fs.write(file.fd, result.pdfArrayBuffer().buffer).then((writeLen: number) => {
                  console.info("createPDF write data to file succeed and size is:" + writeLen);
                }).catch((err: BusinessError) => {
                  console.error("createPDF write data to file failed with error message: " + err.message +
                    ", error code: " + err.code);
                }).finally(() => {
                  fs.closeSync(file);
                });
              } catch (resError) {
                console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
              }
            })
        })
      Web({ src: "www.example.com", controller: this.controller })
    }
  }
}
```

## createPdf

```TypeScript
createPdf(configuration: PdfConfiguration): Promise<PdfData>
```

Rendering current Web page into Pdf data, return the result in promise mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-createPdf(configuration: PdfConfiguration): Promise<PdfData>--><!--Device-WebviewController-createPdf(configuration: PdfConfiguration): Promise<PdfData>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| configuration | [PdfConfiguration](arkts-webview-pdfconfiguration-i.md) | Yes | configuration for createPdf, including page width and height, etc. {@Link PdfConfiguration} |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[PdfData](arkts-webview-pdfdata-c.md)&gt; | The promise returned by the function. PdfData is pdf data stream of current web page in Uint8Array { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid input parameter. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

See [createPdf](#createpdf)

## createWebMessagePorts

```TypeScript
createWebMessagePorts(isExtentionType?: boolean): Array<WebMessagePort>
```

Create web message ports

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-createWebMessagePorts(isExtentionType?: boolean): Array<WebMessagePort>--><!--Device-WebviewController-createWebMessagePorts(isExtentionType?: boolean): Array<WebMessagePort>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isExtentionType | boolean | No | Set whether the web message port supports extention type. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[WebMessagePort](arkts-webview-webmessageport-i.md)&gt; | An array represent 2 WebMessagePort, then can use those ports to communication with html pages. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

For details about the sample code, see [onMessageEventExt](./arkts-apis-webview-WebMessagePort.md#onmessageeventext).

## createWebPrintDocumentAdapter

```TypeScript
createWebPrintDocumentAdapter(jobName: string): print.PrintDocumentAdapter
```

Creates a PrintDocumentAdapter instance to provide content for printing.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-createWebPrintDocumentAdapter(jobName: string): print.PrintDocumentAdapter--><!--Device-WebviewController-createWebPrintDocumentAdapter(jobName: string): print.PrintDocumentAdapter-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| jobName | string | Yes | Name of the file to print. |

**Return value:**

| Type | Description |
| --- | --- |
| print.PrintDocumentAdapter | Return PrintDocumentAdapter instance created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError, print } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('createWebPrintDocumentAdapter')
        .onClick(() => {
          try {
            let webPrintDocadapter = this.controller.createWebPrintDocumentAdapter('example.pdf');
            print.print('example_jobid', webPrintDocadapter, null, this.getUIContext().getHostContext());
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## customizeSchemes

```TypeScript
static customizeSchemes(schemes: Array<WebCustomScheme>): void
```

Register Web custom schemes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static customizeSchemes(schemes: Array<WebCustomScheme>): void--><!--Device-WebviewController-static customizeSchemes(schemes: Array<WebCustomScheme>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| schemes | Array&lt;[WebCustomScheme](arkts-webview-webcustomscheme-i.md)&gt; | Yes | Configuration of web custom scheme. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
| [17100020](../../apis-arkweb/errorcode-webview.md#17100020-failed-to-register-custom-schemes) | Failed to register custom schemes. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  responseWeb: WebResourceResponse = new WebResourceResponse();
  scheme1: webview.WebCustomScheme = { schemeName: "name1", isSupportCORS: true, isSupportFetch: true };
  scheme2: webview.WebCustomScheme = { schemeName: "name2", isSupportCORS: true, isSupportFetch: true };
  scheme3: webview.WebCustomScheme = { schemeName: "name3", isSupportCORS: true, isSupportFetch: true };

  aboutToAppear(): void {
    try {
      webview.WebviewController.customizeSchemes([this.scheme1, this.scheme2, this.scheme3]);
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onInterceptRequest((event) => {
          if (event) {
            console.info('url:' + event.request.getRequestUrl());
          }
          return this.responseWeb;
        })
    }
  }
}
```

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  responseWeb: WebResourceResponse = new WebResourceResponse();
  scheme1: webview.WebCustomScheme = { schemeName: "name1", isSupportCORS: true, isSupportFetch: true };
  scheme2: webview.WebCustomScheme = { schemeName: "name2", isSupportCORS: true, isSupportFetch: true };
  scheme3: webview.WebCustomScheme = { schemeName: "name3", isSupportCORS: true, isSupportFetch: true };

  aboutToAppear(): void {
    try {
      webview.WebviewController.customizeSchemes([this.scheme1, this.scheme2, this.scheme3], true);
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## customizeSchemes

```TypeScript
static customizeSchemes(schemes: Array<WebCustomScheme>, lazyInitWebEngine: boolean): void
```

Register Web custom schemes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static customizeSchemes(schemes: Array<WebCustomScheme>, lazyInitWebEngine: boolean): void--><!--Device-WebviewController-static customizeSchemes(schemes: Array<WebCustomScheme>, lazyInitWebEngine: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| schemes | Array&lt;[WebCustomScheme](arkts-webview-webcustomscheme-i.md)&gt; | Yes | Configuration of web custom scheme. |
| lazyInitWebEngine | boolean | Yes | When true: The interface internally skips initializing WebEngine and temporarily stores the registered schemes, which will be passed to WebEngine when it actually initializes. When false: The interface automatically performs WebEngine initialization internally. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100020](../../apis-arkweb/errorcode-webview.md#17100020-failed-to-register-custom-schemes) | Failed to register custom schemes. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. The length of the schemes array is greater than 10. 2. The character length of the scheme is greater than 32. 3. The character in the scheme is not within the allowed range of lowercase English letters, numbers, and the symbols ".", "+", "-". @static |

**Examples**

See [customizeSchemes](#customizeschemes)

## deleteJavaScriptRegister

```TypeScript
deleteJavaScriptRegister(name: string): void
```

Deletes a registered JavaScript object with given name.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-deleteJavaScriptRegister(name: string): void--><!--Device-WebviewController-deleteJavaScriptRegister(name: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | The name of a registered JavaScript object to be deleted. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |
| [17100008](../../apis-arkweb/errorcode-webview.md#17100008-deleting-a-javascriptproxy-that-does-not-exist) | Failed to delete JavaScriptProxy because it does not exist. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class TestObj {
  constructor() {
  }

  test(): string {
    return "ArkUI Web Component";
  }

  toString(): void {
    console.info('Web Component toString');
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State testObjtest: TestObj = new TestObj();
  @State name: string = 'objName';
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
      Button('Register JavaScript To Window')
        .onClick(() => {
          try {
            this.controller.registerJavaScriptProxy(this.testObjtest, this.name, ["test", "toString"]);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('deleteJavaScriptRegister')
        .onClick(() => {
          try {
            this.controller.deleteJavaScriptRegister(this.name);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
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
      <script type="text/javascript">
        function htmlTest() {
          let str=objName.test();
          document.getElementById("demo").innerHTML=str;
          console.info('objName.test result:'+ str)
        }
      </script>
    </body>
</html>
```

## enableAdsBlock

```TypeScript
enableAdsBlock(enable: boolean): void
```

Enable the ability to block Ads, disabled by default.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-enableAdsBlock(enable: boolean): void--><!--Device-WebviewController-enableAdsBlock(enable: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Parameter string is too long. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

**Examples**

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
      Button('enableAdsBlock')
        .onClick(() => {
          try {
            this.controller.enableAdsBlock(true);
            console.info("enableAdsBlock: true")
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## enableAdvancedSecurityMode

```TypeScript
static enableAdvancedSecurityMode(securityParams: SecurityParams): void
```

Enable the application disable some features such as PDFViewer to enhance the security level of web application

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebviewController-static enableAdvancedSecurityMode(securityParams: SecurityParams): void--><!--Device-WebviewController-static enableAdvancedSecurityMode(securityParams: SecurityParams): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| securityParams | [SecurityParams](arkts-webview-securityparams-i.md) | Yes | The options means which supported option or item will be disabled. |

## enableBackForwardCache

```TypeScript
static enableBackForwardCache(features?: BackForwardCacheSupportedFeatures): void
```

Enable the BackForwardCache and indicate features that are allowed to enter BackForwardCache. Default is disabled.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static enableBackForwardCache(features?: BackForwardCacheSupportedFeatures): void--><!--Device-WebviewController-static enableBackForwardCache(features?: BackForwardCacheSupportedFeatures): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| features | [BackForwardCacheSupportedFeatures](arkts-webview-backforwardcachesupportedfeatures-c.md) | No | The features that supports BackForwardCache. @static |

**Examples**

```TypeScript
// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        let features = new webview.BackForwardCacheSupportedFeatures();
        features.nativeEmbed = true;
        features.mediaTakeOver = true;
        // If a page uses the same-layer rendering and takes over media playback at the same time,
        // you need to set the values of nativeEmbed and mediaTakeOver to true to add the page to the back-forward cache.
        webview.WebviewController.enableBackForwardCache(features);
        webview.WebviewController.initializeWebEngine();
        AppStorage.setOrCreate("abilityWant", want);
    }
}
```

## enableIntelligentTrackingPrevention

```TypeScript
enableIntelligentTrackingPrevention(enable: boolean): void
```

Enable the ability to use Intelligent Tracking Prevention; default is disabled.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-enableIntelligentTrackingPrevention(enable: boolean): void--><!--Device-WebviewController-enableIntelligentTrackingPrevention(enable: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

**Examples**

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
      Button('enableIntelligentTrackingPrevention')
        .onClick(() => {
          try {
            this.controller.enableIntelligentTrackingPrevention(true);
            console.info("enableIntelligentTrackingPrevention: true");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## enablePrivateNetworkAccess

```TypeScript
static enablePrivateNetworkAccess(enable: boolean): void
```

After enable PrivateNetworkAccess feature, ArkWeb will send a CORS preflight request before issuing any sub-resource private network requests to request explicit permission from the target server. After disable PrivateNetworkAccess, ArkWeb will no longer check whether the private network request is legitimate.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static enablePrivateNetworkAccess(enable: boolean): void--><!--Device-WebviewController-static enablePrivateNetworkAccess(enable: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | {@code true} enable the private network access check; {@code false} otherwise. @static |

**Examples**

```TypeScript
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onControllerAttached(() => {
          // If the value is set to false, ArkWeb does not check whether the private network request is valid.
          webview.WebviewController.enablePrivateNetworkAccess(false);
        })
    }
  }
}
```

## enableSafeBrowsing

```TypeScript
enableSafeBrowsing(enable: boolean): void
```

Enable the ability to check website security risks. Illegal and fraudulent websites are mandatory enabled and can't be disabled by this function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-enableSafeBrowsing(enable: boolean): void--><!--Device-WebviewController-enableSafeBrowsing(enable: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | {@code true} enable check the website security risks; {@code false} otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |

**Examples**

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
      Button('enableSafeBrowsing')
        .onClick(() => {
          try {
            this.controller.enableSafeBrowsing(true);
            console.info("enableSafeBrowsing: true");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## enableWholeWebPageDrawing

```TypeScript
static enableWholeWebPageDrawing(): void
```

Enables the full drawing capability for the web page. This API works only during Web component initialization.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static enableWholeWebPageDrawing(): void--><!--Device-WebviewController-static enableWholeWebPageDrawing(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    try {
      webview.WebviewController.enableWholeWebPageDrawing();
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## executeAIPageCommand

```TypeScript
executeAIPageCommand(command: string): Promise<string>
```

Asynchronously executes AI page command operations.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebviewController-executeAIPageCommand(command: string): Promise<string>--><!--Device-WebviewController-executeAIPageCommand(command: string): Promise<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| command | string | Yes | JSON-formatted command parameter. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | A promise that resolves after the command is executed. This JSON-formatted value will be the result of command execution. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |
| [17100024](../../apis-arkweb/errorcode-webview.md#17100024-aipagecommand-format-error) | Command format error. The command parameter does not conform to the JSON format requirements. |

## forward

```TypeScript
forward(): void
```

Goes forward in the history of the web page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-forward(): void--><!--Device-WebviewController-forward(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('forward')
        .onClick(() => {
          try {
            this.controller.forward();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## getActiveWebEngineVersion

```TypeScript
static getActiveWebEngineVersion(): ArkWebEngineVersion
```

Obtains the current ArkWeb kernel version.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static getActiveWebEngineVersion(): ArkWebEngineVersion--><!--Device-WebviewController-static getActiveWebEngineVersion(): ArkWebEngineVersion-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [ArkWebEngineVersion](arkts-webview-arkwebengineversion-e.md) | The ArkWeb kernel version defined by [ArkWebEngineVersion]{ |

**Examples**

For details, see [setActiveWebEngineVersion](#setactivewebengineversion).

## getAttachState

```TypeScript
getAttachState(): ControllerAttachState
```

Get whether webviewController is attached to a web component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getAttachState(): ControllerAttachState--><!--Device-WebviewController-getAttachState(): ControllerAttachState-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [ControllerAttachState](arkts-webview-controllerattachstate-e.md) | the attach state of controller |

## getBackForwardEntries

```TypeScript
getBackForwardEntries(): BackForwardList
```

Get back forward stack list from current webview.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getBackForwardEntries(): BackForwardList--><!--Device-WebviewController-getBackForwardEntries(): BackForwardList-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [BackForwardList](arkts-webview-backforwardlist-i.md) | Back forward list for current webview. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('getBackForwardEntries')
        .onClick(() => {
          try {
            let list = this.controller.getBackForwardEntries()
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## getBlanklessInfoWithKey

```TypeScript
getBlanklessInfoWithKey(key: string) : BlanklessInfo
```

Obtains the prediction information about the blankless loading solution and enables the generation of the transition frame for the current loading. The application determines whether to enable the blankless loading solution based on the information.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getBlanklessInfoWithKey(key: string) : BlanklessInfo--><!--Device-WebviewController-getBlanklessInfoWithKey(key: string) : BlanklessInfo-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key value that uniquely identifies the page. Default value: N/A. The value cannot be empty or exceed 2048 characters. When an invalid value is set, this API does not take effect. |

**Return value:**

| Type | Description |
| --- | --- |
| [BlanklessInfo](arkts-webview-blanklessinfo-i.md) | The prediction information about the blankless loading solution. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |  |

**Examples**

```TypeScript
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Web({ src: 'https://www.example.com', controller: this.controller })
       .javaScriptAccess(true)
       .onLoadIntercept((event) => {
            // Enable frame interpolation only when the similarity exceeds 50% and the loading duration is less than 1000 ms.
            try {
              let info = this.controller.getBlanklessInfoWithKey('https://www.example.com/page1');
              if (info.errCode == webview.WebBlanklessErrorCode.SUCCESS) {
                if (info.similarity >= 0.5 && info.loadingTime < 1000) {
                  this.controller.setBlanklessLoadingWithKey('http://www.example.com/page1', true);
                } else {
                  this.controller.setBlanklessLoadingWithKey('http://www.example.com/page1', false);
                }
              } else {
                console.info('getBlankless info err');
              }
            } catch (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
            return false;
        })
    }
  }
}
```

## getCertificate

```TypeScript
getCertificate(): Promise<Array<cert.X509Cert>>
```

Get certificate for the current website.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getCertificate(): Promise<Array<cert.X509Cert>>--><!--Device-WebviewController-getCertificate(): Promise<Array<cert.X509Cert>>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;cert.X509Cert&gt;&gt; | the promise of the current website's certificate. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a web component. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { cert } from '@kit.DeviceCertificateKit';

function Uint8ArrayToString(dataArray: Uint8Array) {
  let dataString = '';
  for (let i = 0; i < dataArray.length; i++) {
    dataString += String.fromCharCode(dataArray[i]);
  }
  return dataString;
}

function ParseX509CertInfo(x509CertArray: Array<cert.X509Cert>) {
  let res: string = 'getCertificate success: len = ' + x509CertArray.length;
  for (let i = 0; i < x509CertArray.length; i++) {
    res += ', index = ' + i + ', issuer name = '
      + Uint8ArrayToString(x509CertArray[i].getIssuerName().data) + ', subject name = '
      + Uint8ArrayToString(x509CertArray[i].getSubjectName().data) + ', valid start = '
      + x509CertArray[i].getNotBeforeTime()
      + ', valid end = ' + x509CertArray[i].getNotAfterTime();
  }
  return res;
}

@Entry
@Component
struct Index {
  // outputStr displays debug information on the UI.
  @State outputStr: string = '';
  webviewCtl: webview.WebviewController = new webview.WebviewController();

  build() {
    Row() {
      Column() {
        List({ space: 20, initialIndex: 0 }) {
          ListItem() {
            Button() {
              Text('load bad ssl')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              // Load an expired certificate website and view the obtained certificate information.
              this.webviewCtl.loadUrl('https://expired.badssl.com');
            })
            .height(50)
          }

          ListItem() {
            Button() {
              Text('load example')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              // Load an HTTPS website and view the certificate information of the website.
              this.webviewCtl.loadUrl('https://www.example.com');
            })
            .height(50)
          }

          ListItem() {
            Button() {
              Text('getCertificate Promise')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              try {
                this.webviewCtl.getCertificate().then((x509CertArray: Array<cert.X509Cert>) => {
                  this.outputStr = ParseX509CertInfo(x509CertArray);
                })
              } catch (error) {
                this.outputStr = 'getCertificate failed: ' + (error as BusinessError).code + ", errMsg: " + (error as BusinessError).message;
              }
            })
            .height(50)
          }

          ListItem() {
            Button() {
              Text('getCertificate AsyncCallback')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              try {
                this.webviewCtl.getCertificate((error: BusinessError, x509CertArray: Array<cert.X509Cert>) => {
                  if (error) {
                    this.outputStr = 'getCertificate failed: ' + error.code + ", errMsg: " + error.message;
                  } else {
                    this.outputStr = ParseX509CertInfo(x509CertArray);
                  }
                })
              } catch (error) {
                this.outputStr = 'getCertificate failed: ' + (error as BusinessError).code + ", errMsg: " + (error as BusinessError).message;
              }
            })
            .height(50)
          }
        }
        .listDirection(Axis.Horizontal)
        .height('10%')

        Text(this.outputStr)
          .width('100%')
          .fontSize(10)

        Web({ src: 'https://www.example.com', controller: this.webviewCtl })
          .fileAccess(true)
          .javaScriptAccess(true)
          .domStorageAccess(true)
          .onlineImageAccess(true)
          .onPageEnd((e) => {
            if (e) {
              this.outputStr = 'onPageEnd : url = ' + e.url;
            }
          })
          .onSslErrorEventReceive((e) => {
            // Ignore SSL certificate errors to test websites whose certificates have expired, for example, https://expired.badssl.com.
            e.handler.handleConfirm();
          })
          .width('100%')
          .height('70%')
      }
      .height('100%')
    }
  }
}
```

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { cert } from '@kit.DeviceCertificateKit';

function Uint8ArrayToString(dataArray: Uint8Array) {
  let dataString = '';
  for (let i = 0; i < dataArray.length; i++) {
    dataString += String.fromCharCode(dataArray[i]);
  }
  return dataString;
}

function ParseX509CertInfo(x509CertArray: Array<cert.X509Cert>) {
  let res: string = 'getCertificate success: len = ' + x509CertArray.length;
  for (let i = 0; i < x509CertArray.length; i++) {
    res += ', index = ' + i + ', issuer name = '
      + Uint8ArrayToString(x509CertArray[i].getIssuerName().data) + ', subject name = '
      + Uint8ArrayToString(x509CertArray[i].getSubjectName().data) + ', valid start = '
      + x509CertArray[i].getNotBeforeTime()
      + ', valid end = ' + x509CertArray[i].getNotAfterTime();
  }
  return res;
}

@Entry
@Component
struct Index {
  // outputStr displays debug information on the UI.
  @State outputStr: string = '';
  webviewCtl: webview.WebviewController = new webview.WebviewController();

  build() {
    Row() {
      Column() {
        List({ space: 20, initialIndex: 0 }) {
          ListItem() {
            Button() {
              Text('load bad ssl')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              // Load an expired certificate website and view the obtained certificate information.
              this.webviewCtl.loadUrl('https://expired.badssl.com');
            })
            .height(50)
          }

          ListItem() {
            Button() {
              Text('load example')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              // Load an HTTPS website and view the certificate information of the website.
              this.webviewCtl.loadUrl('https://www.example.com');
            })
            .height(50)
          }

          ListItem() {
            Button() {
              Text('getCertificate Promise')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              try {
                this.webviewCtl.getCertificate().then((x509CertArray: Array<cert.X509Cert>) => {
                  this.outputStr = ParseX509CertInfo(x509CertArray);
                })
              } catch (error) {
                this.outputStr = 'getCertificate failed: ' + (error as BusinessError).code + ", errMsg: " + (error as BusinessError).message;
              }
            })
            .height(50)
          }

          ListItem() {
            Button() {
              Text('getCertificate AsyncCallback')
                .fontSize(10)
                .fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .onClick(() => {
              try {
                this.webviewCtl.getCertificate((error: BusinessError, x509CertArray: Array<cert.X509Cert>) => {
                  if (error) {
                    this.outputStr = 'getCertificate failed: ' + error.code + ", errMsg: " + error.message;
                  } else {
                    this.outputStr = ParseX509CertInfo(x509CertArray);
                  }
                })
              } catch (error) {
                this.outputStr = 'getCertificate failed: ' + (error as BusinessError).code + ", errMsg: " + (error as BusinessError).message;
              }
            })
            .height(50)
          }
        }
        .listDirection(Axis.Horizontal)
        .height('10%')

        Text(this.outputStr)
          .width('100%')
          .fontSize(10)

        Web({ src: 'https://www.example.com', controller: this.webviewCtl })
          .fileAccess(true)
          .javaScriptAccess(true)
          .domStorageAccess(true)
          .onlineImageAccess(true)
          .onPageEnd((e) => {
            if (e) {
              this.outputStr = 'onPageEnd : url = ' + e.url;
            }
          })
          .onSslErrorEventReceive((e) => {
            // Ignore SSL certificate errors to test websites whose certificates have expired, for example, https://expired.badssl.com.
            e.handler.handleConfirm();
          })
          .width('100%')
          .height('70%')
      }
      .height('100%')
    }
  }
}
```

## getCertificate

```TypeScript
getCertificate(callback: AsyncCallback<Array<cert.X509Cert>>): void
```

Get certificate for the current website.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getCertificate(callback: AsyncCallback<Array<cert.X509Cert>>): void--><!--Device-WebviewController-getCertificate(callback: AsyncCallback<Array<cert.X509Cert>>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;cert.X509Cert&gt;&gt; | Yes | the callback of getCertificate. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a web component. |

**Examples**

See [getCertificate](#getcertificate)

## getCustomUserAgent

```TypeScript
getCustomUserAgent(): string
```

Get custom user agent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getCustomUserAgent(): string--><!--Device-WebviewController-getCustomUserAgent(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Get custom User agent information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State userAgent: string = '';

  build() {
    Column() {
      Button('getCustomUserAgent')
        .onClick(() => {
          try {
            this.userAgent = this.controller.getCustomUserAgent();
            console.info("userAgent: " + this.userAgent);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## getDefaultUserAgent

```TypeScript
static getDefaultUserAgent(): string
```

Get the default user agent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static getDefaultUserAgent(): string--><!--Device-WebviewController-static getDefaultUserAgent(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | The default user agent string. |

**Examples**

```TypeScript
// EntryAbility.ets
import { webview } from '@kit.ArkWeb';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    let defaultUserAgent = webview.WebviewController.getDefaultUserAgent();
    console.info("defaultUserAgent: " + defaultUserAgent);
  }
}
```

## getErrorPageEnabled

```TypeScript
getErrorPageEnabled(): boolean
```

Get whether default error page feature is enabled.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getErrorPageEnabled(): boolean--><!--Device-WebviewController-getErrorPageEnabled(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if enable the default error page feature; else false. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

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
       .onControllerAttached(() => {
            this.controller.setErrorPageEnabled(true);
            if (!this.controller.getErrorPageEnabled()) {
                this.controller.setErrorPageEnabled(true);
            }
        })
    }
  }
}
```

## getFavicon

```TypeScript
getFavicon(): image.PixelMap
```

Gets the favicon of current Web page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getFavicon(): image.PixelMap--><!--Device-WebviewController-getFavicon(): image.PixelMap-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| image.PixelMap | Return the favicon bitmap of the current page. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State pixelmap: image.PixelMap | undefined = undefined;

  build() {
    Column() {
      Button('getFavicon')
        .onClick(() => {
          try {
            this.pixelmap = this.controller.getFavicon();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## getLastHitTest

```TypeScript
getLastHitTest(): HitTestValue
```

Gets the last hit test value of HitTest.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getLastHitTest(): HitTestValue--><!--Device-WebviewController-getLastHitTest(): HitTestValue-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [HitTestValue](arkts-webview-hittestvalue-i.md) | Return the element information of the clicked area. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('getLastHitTest')
        .onClick(() => {
          try {
            let hitValue = this.controller.getLastHitTest();
            console.info("hitType: " + hitValue.type);
            console.info("extra: " + hitValue.extra);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## getLastJavascriptProxyCallingFrameUrl

```TypeScript
getLastJavascriptProxyCallingFrameUrl(): string
```

Get the url of the last frame that calls the JavaScriptProxy. This should be called on the UI thread.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getLastJavascriptProxyCallingFrameUrl(): string--><!--Device-WebviewController-getLastJavascriptProxyCallingFrameUrl(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | The url of the last frame that calls the JavaScriptProxy. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class TestObj {
  mycontroller: webview.WebviewController;

  constructor(controller: webview.WebviewController) {
    this.mycontroller = controller;
  }

  test(testStr: string): string {
    console.info('Web Component str' + testStr + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
    return testStr;
  }

  toString(): void {
    console.info('Web Component toString ' + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
  }

  testNumber(testNum: number): number {
    console.info('Web Component number' + testNum + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
    return testNum;
  }

  testBool(testBol: boolean): boolean {
    console.info('Web Component boolean' + testBol + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
    return testBol;
  }
}

class WebObj {
  mycontroller: webview.WebviewController;

  constructor(controller: webview.WebviewController) {
    this.mycontroller = controller;
  }

  webTest(): string {
    console.info('Web test ' + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
    return "Web test";
  }

  webString(): void {
    console.info('Web test toString ' + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
  }
}

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  @State testObjtest: TestObj = new TestObj(this.controller);
  @State webTestObj: WebObj = new WebObj(this.controller);

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
      Button('Register JavaScript To Window')
        .onClick(() => {
          try {
            this.controller.registerJavaScriptProxy(this.testObjtest, "objName", ["test", "toString", "testNumber", "testBool"]);
            this.controller.registerJavaScriptProxy(this.webTestObj, "objTestName", ["webTest", "webString"]);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('deleteJavaScriptRegister')
        .onClick(() => {
          try {
            this.controller.deleteJavaScriptRegister("objName");
            this.controller.deleteJavaScriptRegister("objTestName");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
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
          // This function call expects to return "ArkUI Web Component"
          let str=objName.test("webtest data");
          objName.testNumber(1);
          objName.testBool(true);
          document.getElementById("demo").innerHTML=str;
          console.info('objName.test result:'+ str)

          // This function call expects to return "Web test"
          let webStr = objTestName.webTest();
          document.getElementById("webDemo").innerHTML=webStr;
          console.info('objTestName.webTest result:'+ webStr)
        }
      </script>
    </body>
</html>
```

## getLastPostMessageURL

```TypeScript
getLastPostMessageURL(): string
```

Gets URL of frame that sent the last postMessage to native application.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebviewController-getLastPostMessageURL(): string--><!--Device-WebviewController-getLastPostMessageURL(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | The URL of frame that last sent a postMessage. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

## getMediaPlaybackState

```TypeScript
getMediaPlaybackState(): MediaPlaybackState
```

Queries the audio and video playback status of the current web page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getMediaPlaybackState(): MediaPlaybackState--><!--Device-WebviewController-getMediaPlaybackState(): MediaPlaybackState-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [MediaPlaybackState](arkts-webview-mediaplaybackstate-e.md) | Playback control status of the current web page. The options are **NONE**, **PLAYING**, **PAUSED**, and **STOPPED**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('getMediaPlaybackState')
        .onClick(() => {
          try {
            console.info("MediaPlaybackState : " + this.controller.getMediaPlaybackState());
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## getOriginalUrl

```TypeScript
getOriginalUrl(): string
```

Gets the original url of current Web page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getOriginalUrl(): string--><!--Device-WebviewController-getOriginalUrl(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Return the original url of the current page. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('getOrgUrl')
        .onClick(() => {
          try {
            let url = this.controller.getOriginalUrl();
            console.info("original url: " + url);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## getPageHeight

```TypeScript
getPageHeight(): int
```

Obtains the height of this web page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getPageHeight(): int--><!--Device-WebviewController-getPageHeight(): int-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| int | Height of the current web page. Unit: vp. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('getPageHeight')
        .onClick(() => {
          try {
            let pageHeight = this.controller.getPageHeight();
            console.info("pageHeight : " + pageHeight);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## getPageOffset

```TypeScript
getPageOffset(): ScrollOffset
```

Get the page offset. And the unit is virtual pixel.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getPageOffset(): ScrollOffset--><!--Device-WebviewController-getPageOffset(): ScrollOffset-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| ScrollOffset | page offset |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |  |

**Examples**

```TypeScript
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onScroll((event) => {
          try {
            console.info("getPageOffset x:" + this.controller.getPageOffset().x + ",y:" +
            this.controller.getPageOffset().y);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
    }
  }
}
```

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .blue {
          background-color: lightblue;
        }
        .green {
          background-color: lightgreen;
        }
        .blue, .green {
         font-size:16px;
         height:200px;
         text-align: center;       /* Horizontally centered */
         line-height: 200px;       /* Vertically centered (the height matches the container height) */
        }
    </style>
</head>
<body>
<div class="blue" >webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
</body>
</html>
```

## getPrintBackground

```TypeScript
getPrintBackground(): boolean
```

Get whether print web page background.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getPrintBackground(): boolean--><!--Device-WebviewController-getPrintBackground(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Get whether print web page background. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('setPrintBackground')
        .onClick(() => {
          try {
            let enable = this.controller.getPrintBackground();
            console.info("getPrintBackground: " + enable);
          } catch (error) {
            console.error(`ErrorCode:${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## getProgress

```TypeScript
getProgress() : int
```

Gets the loading progress for the current page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getProgress() : int--><!--Device-WebviewController-getProgress() : int-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| int | The loading progress for the current page. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

**Examples**

```TypeScript
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onPageBegin(() => {
          let curProgress = this.controller.getProgress();
          console.info("current page loading progress is :" + curProgress);
        })
    }
  }
}
```

## getRenderProcessMode

```TypeScript
static getRenderProcessMode(): RenderProcessMode
```

Get render process mode of the ArkWeb.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static getRenderProcessMode(): RenderProcessMode--><!--Device-WebviewController-static getRenderProcessMode(): RenderProcessMode-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [RenderProcessMode](arkts-webview-renderprocessmode-e.md) | mode - The render process mode of the ArkWeb. Call { |

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
      Button('getRenderProcessMode')
        .onClick(() => {
          let mode = webview.WebviewController.getRenderProcessMode();
          console.info("getRenderProcessMode: " + mode);
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## getScrollable

```TypeScript
getScrollable(): boolean
```

Get whether scrolling is allowed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getScrollable(): boolean--><!--Device-WebviewController-getScrollable(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Get scrolling is allowed information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('getScrollable')
        .onClick(() => {
          try {
            let scrollEnabled = this.controller.getScrollable();
            console.info("scrollEnabled: " + scrollEnabled);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## getScrollOffset

```TypeScript
getScrollOffset(): ScrollOffset
```

Get the scroll offset of the webpage in view port, the coordinates of the top left corner of the view port are X: 0, Y: 0. And the unit is virtual pixel.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getScrollOffset(): ScrollOffset--><!--Device-WebviewController-getScrollOffset(): ScrollOffset-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| ScrollOffset | scroll offset |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  @State testTitle: string = 'webScroll'
  controller: webview.WebviewController = new webview.WebviewController();
  @State controllerX: number =-100;
  @State controllerY: number =-100;
  @State mode: OverScrollMode = OverScrollMode.ALWAYS;

  build() {
    Column() {
      Row() {
        Text(this.testTitle)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .margin(5)
      }
      Column() {
        Text(`controllerX: ${this.controllerX}, controllerY: ${this.controllerY}`)
      }
      .margin({ top: 10, bottom: 10 })
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .key("web_01")
        .overScrollMode(this.mode)
        .onTouch(() => {
          this.controllerX = this.controller.getScrollOffset().x;
          this.controllerY = this.controller.getScrollOffset().y;
          let componentInfo = this.getUIContext().getComponentUtils().getRectangleById("web_01");
          let webHeight = this.getUIContext().px2vp(componentInfo.size.height);
          let pageHeight = this.controller.getPageHeight();
          if (this.controllerY < 0) {
            // Case 1: When a web page is scrolled down, use ScrollOffset.y directly.
            console.info(`get downwards overscroll offsetY = ${this.controllerY}`);
          } else if ((this.controllerY != 0) && (this.controllerY > (pageHeight - webHeight))) {
            // Case 2: When a web page is scrolled up, calculate the offset between the lower boundary of the web page and that of the Web component.
            console.info(`get upwards overscroll offsetY = ${this.controllerY - (pageHeight >= webHeight ? (pageHeight - webHeight) : 0)}`);
          } else {
            // Case 3: If the web page is not scrolled, use ScrollOffset.y directly.
            console.info(`get scroll offsetY = ${this.controllerY}`);
          }
        })
        .height(600)
    }
    .width('100%')
    .height('100%')
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" id="viewport" content="width=device-width,initial-scale=1.0">
    <title>Demo</title>
    <style>
        body {
          width:3000px;
          height:6000px;
          padding-right:170px;
          padding-left:170px;
          border:5px solid blueviolet;
        }
    </style>
</head>
<body>
Scroll Test
</body>
</html>
```

## getSecurityLevel

```TypeScript
getSecurityLevel(): SecurityLevel
```

Get the security level of the current page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getSecurityLevel(): SecurityLevel--><!--Device-WebviewController-getSecurityLevel(): SecurityLevel-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| SecurityLevel | the security level of current page. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onPageEnd((event) => {
          if (event) {
            let securityLevel = this.controller.getSecurityLevel();
            console.info('securityLevel: ', securityLevel);
          }
        })
    }
  }
}
```

## getSiteIsolationMode

```TypeScript
static getSiteIsolationMode(): SiteIsolationMode
```

Get the site isolation mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static getSiteIsolationMode(): SiteIsolationMode--><!--Device-WebviewController-static getSiteIsolationMode(): SiteIsolationMode-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [SiteIsolationMode](arkts-webview-siteisolationmode-e.md) | The site isolation mode of the application. |

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
      Button('getSiteIsolationMode')
        .onClick(() => {
          let mode = webview.WebviewController.getSiteIsolationMode();
          console.info("getSiteIsolationMode: " + mode);
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## getSubframeErrorPageEnabled

```TypeScript
getSubframeErrorPageEnabled(): boolean
```

Get whether default error page feature is enabled for subframes.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebviewController-getSubframeErrorPageEnabled(): boolean--><!--Device-WebviewController-getSubframeErrorPageEnabled(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if the default error page function of the subframe is enabled; Otherwise, the value is false. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

## getSurfaceId

```TypeScript
getSurfaceId(): string
```

Get the ID of the surface created by ArkWeb. This ID can be used for web page screenshots.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getSurfaceId(): string--><!--Device-WebviewController-getSurfaceId(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | The ID of the surface created by ArkWeb. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Example{
  controller: webview.WebviewController = new webview.WebviewController();

  @State imagePixelMap: image.PixelMap | undefined = undefined;

  build(){
    Column(){
      Button("Screenshot")
        .onClick(()=>{
          try {
            let surfaceId = this.controller.getSurfaceId();
            console.info("surfaceId: " + surfaceId);
            if(surfaceId.length != 0) {
              let region:image.Region = { x: 0, y: 0, size: { height: 800, width: 1000}}
              this.imagePixelMap = image.createPixelMapFromSurfaceSync(surfaceId, region)
            }
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Image(this.imagePixelMap)
        .height(100)
      Web({src: 'www.example.com', controller: this.controller})
    }
  }
}
```

## getTitle

```TypeScript
getTitle(): string
```

Gets the title of current Web page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getTitle(): string--><!--Device-WebviewController-getTitle(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Return to File Selector Title. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('getTitle')
        .onClick(() => {
          try {
            let title = this.controller.getTitle();
            console.info("title: " + title);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## getUrl

```TypeScript
getUrl(): string
```

Gets the url of current Web page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getUrl(): string--><!--Device-WebviewController-getUrl(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Return the url of the current page. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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

## getUserAgent

```TypeScript
getUserAgent(): string
```

Gets the default user agent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getUserAgent(): string--><!--Device-WebviewController-getUserAgent(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Return user agent information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('getUserAgent')
        .onClick(() => {
          try {
            let userAgent = this.controller.getUserAgent();
            console.info("userAgent: " + userAgent);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

You can customize User-Agent based on the default User-Agent.

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State ua: string = "";

  aboutToAppear(): void {
    webview.once('webInited', () => {
      try {
        // Customize a User-Agent on the application side.
        this.ua = this.controller.getUserAgent() + 'xxx';
        this.controller.setCustomUserAgent(this.ua);
      } catch (error) {
        console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
      }
    })
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## getUserAgentClientHintsEnabled

```TypeScript
static getUserAgentClientHintsEnabled(): boolean
```

Get if the User-Agent Client Hints enabled.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebviewController-static getUserAgentClientHintsEnabled(): boolean--><!--Device-WebviewController-static getUserAgentClientHintsEnabled(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | If User-Agent Client Hints was enabled. |

**Examples**

For details about the sample code, see [setUserAgentClientHintsEnabled](#setuseragentclienthintsenabled).

## getUserAgentMetadata

```TypeScript
getUserAgentMetadata(userAgent: string): UserAgentMetadata
```

Get the User-Agent metadata corresponding to the User-Agent.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebviewController-getUserAgentMetadata(userAgent: string): UserAgentMetadata--><!--Device-WebviewController-getUserAgentMetadata(userAgent: string): UserAgentMetadata-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userAgent | string | Yes | The User-Agent string. |

**Return value:**

| Type | Description |
| --- | --- |
| [UserAgentMetadata](arkts-webview-useragentmetadata-c.md) | The UserAgentMetadata for the userAgent. |

**Examples**

For details about the sample code, see [setUserAgentClientHintsEnabled](#setuseragentclienthintsenabled).

## getWebId

```TypeScript
getWebId(): int
```

Gets the index value of the current Web component for the management of multiple Web components.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-getWebId(): int--><!--Device-WebviewController-getWebId(): int-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the index value of the current Web component. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('getWebId')
        .onClick(() => {
          try {
            let id = this.controller.getWebId();
            console.info("id: " + id);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## hasImage

```TypeScript
hasImage(): Promise<boolean>
```

Checks whether this page contains images. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-hasImage(): Promise<boolean>--><!--Device-WebviewController-hasImage(): Promise<boolean>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. <br> The value **true** indicates that this page contains images, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('hasImageCb')
        .onClick(() => {
          try {
            this.controller.hasImage((error, data) => {
              if (error) {
                console.error(`hasImage error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                return;
              }
              console.info("hasImage: " + data);
            });
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

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
      Button('hasImagePm')
        .onClick(() => {
          try {
            this.controller.hasImage().then((data) => {
              console.info('hasImage: ' + data);
            }).catch((error: BusinessError) => {
              console.error("error: " + error);
            })
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## hasImage

```TypeScript
hasImage(callback: AsyncCallback<boolean>): void
```

Checks whether this page contains images. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-hasImage(callback: AsyncCallback<boolean>): void--><!--Device-WebviewController-hasImage(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result.<br> The value **true** indicates that this page contains images, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

See [hasImage](#hasimage)

## initializeWebEngine

```TypeScript
static initializeWebEngine(): void
```

Initialize the web engine before loading the Web components. This is a global static API that must be called on the UI thread, and it will have no effect if any Web components are loaded.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static initializeWebEngine(): void--><!--Device-WebviewController-static initializeWebEngine(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Examples**

The following code snippet exemplifies calling this API after the EntryAbility is created.

```TypeScript
// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate")
    webview.WebviewController.initializeWebEngine()
    console.info("EntryAbility onCreate done")
  }
}
```

## injectOfflineResources

```TypeScript
injectOfflineResources(resourceMaps: Array<OfflineResourceMap>): void
```

Inject offline resources into cache.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-injectOfflineResources(resourceMaps: Array<OfflineResourceMap>): void--><!--Device-WebviewController-injectOfflineResources(resourceMaps: Array<OfflineResourceMap>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| resourceMaps | Array&lt;[OfflineResourceMap](arkts-webview-offlineresourcemap-i.md)&gt; | Yes | Array of offline resource info maps. The count of array must between 1 and 30. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-incorrect-url-format) | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2 *1024 *1024. |

**Examples**

Save UIContext to localStorage in EntryAbility.

```TypeScript
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

const localStorage: LocalStorage = new LocalStorage('uiContext');

export default class EntryAbility extends UIAbility {
  storage: LocalStorage = localStorage;

  onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage.loadContent('pages/Index', this.storage, (err, data) => {
      if (err.code) {
        return;
      }

      this.storage.setOrCreate<UIContext>("uiContext", windowStage.getMainWindowSync().getUIContext());
    });
  }
}
```

Write the basic code required by the dynamic component.

```TypeScript
// DynamicComponent.ets
import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

export interface BuilderData {
  url: string;
  controller: WebviewController;
  context: UIContext;
}

let storage : LocalStorage | undefined = undefined;

export class NodeControllerImpl extends NodeController {
  private rootNode: BuilderNode<BuilderData[]> | null = null;
  private wrappedBuilder: WrappedBuilder<BuilderData[]> | null = null;

  constructor(wrappedBuilder: WrappedBuilder<BuilderData[]>, context: UIContext) {
    storage = context.getSharedLocalStorage();
    super();
    this.wrappedBuilder = wrappedBuilder;
  }

  makeNode(): FrameNode | null {
    if (this.rootNode != null) {
      return this.rootNode.getFrameNode();
    }
    return null;
  }

  initWeb(url: string, controller: WebviewController) {
    if(this.rootNode != null) {
      return;
    }

    const uiContext: UIContext = storage!.get<UIContext>("uiContext") as UIContext;
    if (!uiContext) {
      return;
    }
    this.rootNode = new BuilderNode(uiContext);
    this.rootNode.build(this.wrappedBuilder, { url: url, controller: controller });
  }
}

export const createNode = (wrappedBuilder: WrappedBuilder<BuilderData[]>, data: BuilderData) => {
  const baseNode = new NodeControllerImpl(wrappedBuilder, data.context);
  baseNode.initWeb(data.url, data.controller);
  return baseNode;
}
```

Write the component code for injecting resources. In this example, the local resource content reads the local file in the rawfile directory through the file reading API.

```TypeScript
// InjectWebview.ets
import { webview } from '@kit.ArkWeb';
import { resourceConfigs } from "./Resource";
import { BuilderData } from "./DynamicComponent";

@Builder
function WebBuilder(data: BuilderData) {
  Web({ src: data.url, controller: data.controller })
    .onControllerAttached(async () => {
      try {
        data.controller.injectOfflineResources(await getData (data.context));
      } catch (err) {
        console.error("error: " + err.code + " " + err.message);
      }
    })
    .fileAccess(true)
}

export const injectWebview = wrapBuilder<BuilderData[]>(WebBuilder);

export async function getData(context: UIContext) {
  const resourceMapArr: Array<webview.OfflineResourceMap> = [];

  // Read the configuration and read the file content from the rawfile directory.
  for (let config of resourceConfigs) {
    let buf: Uint8Array = new Uint8Array(0);
    if (config.localPath) {
      buf = await readRawFile(config.localPath, context);
    }

    resourceMapArr.push({
      urlList: config.urlList,
      resource: buf,
      responseHeaders: config.responseHeaders,
      type: config.type,
    })
  }

  return resourceMapArr;
}

export async function readRawFile(url: string, context: UIContext) {
  try {
    return await context.getHostContext()!.resourceManager.getRawFileContent(url);
  } catch (err) {
    return new Uint8Array(0);
  }
}
```

Compile the code of the service component.

```TypeScript
// BusinessWebview.ets
import { BuilderData } from "./DynamicComponent";

@Builder
function WebBuilder(data: BuilderData) {
  // The component can be extended based on service requirements.
  Web({ src: data.url, controller: data.controller })
    .cacheMode(CacheMode.Default)
}

export const businessWebview = wrapBuilder<BuilderData[]>(WebBuilder);
```

Write the resource configuration information.

```TypeScript
// Resource.ets
import { webview } from '@kit.ArkWeb';

export interface ResourceConfig {
  urlList: Array<string>,
  type: webview.OfflineResourceType,
  responseHeaders: Array<Header>,
  localPath: string, // Path for storing local resources in the rawfile directory.
}

export const resourceConfigs: Array<ResourceConfig> = [
  {
    localPath: "example.png",
    urlList: [
      "https://www.example.com/",
      "https://www.example.com/path1/example.png",
      "https://www.example.com/path2/example.png",
    ],
    type: webview.OfflineResourceType.IMAGE,
    responseHeaders: [
      { headerKey: "Cache-Control", headerValue: "max-age=1000" },
      { headerKey: "Content-Type", headerValue: "image/png" },
    ]
  },
  {
    localPath: "example.js",
    urlList: [ // Only one URL is provided. This URL is used as both the resource origin and the network request address of the resource.
      "https://www.example.com/example.js",
    ],
    type: webview.OfflineResourceType.CLASSIC_JS,
    responseHeaders: [
      // Used in <script crossorigin="anonymous"/> mode to provide additional response headers.
      { headerKey: "Cross-Origin", headerValue:"anonymous" }
    ]
  },
];
```

Use the component on the page.

```TypeScript
// Index.ets
import { webview } from '@kit.ArkWeb';
import { NodeController } from '@kit.ArkUI';
import { createNode } from "./DynamicComponent"
import { injectWebview } from "./InjectWebview"
import { businessWebview } from "./BusinessWebview"

@Entry
@Component
struct Index {
  @State injectNode: NodeController | undefined = undefined;
  injectController: webview.WebviewController = new webview.WebviewController();

  @State businessNode: NodeController | undefined = undefined;
  businessController: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    // Initialize the Web component used to inject local resources and provide an empty HTML page as the URL.
    this.injectNode = createNode(injectWebview,
        { url: "https://www.example.com/empty.html", controller: this.injectController, context: this.getUIContext()});
  }

  build() {
    Column() {
      // Load the Web component used by the service at a proper time. In this example, the button is clicked.
      Button("Load Page")
        .onClick(() => {
          this.businessNode = createNode(businessWebview, {
            url: "https://www.example.com/business.html",
            controller: this.businessController,
            context: this.getUIContext()
          });
        })
      // The Web component used for the service.
      NodeContainer(this.businessNode);
    }
  }
}
```

Example of a loaded HTML web page:

```TypeScript
<!DOCTYPE html>
<html lang="en">
<head></head>
<body>
  <img src="https://www.example.com/path1/request.png" />
  <img src="https://www.example.com/path2/request.png" />
  <script src="https://www.example.com/example.js" crossorigin="anonymous"></script>
</body>
</html>
```

## isActiveWebEngineEvergreen

```TypeScript
static isActiveWebEngineEvergreen(): boolean
```

Checks whether the system is using the evergreen kernel, that is, the latest kernel.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static isActiveWebEngineEvergreen(): boolean--><!--Device-WebviewController-static isActiveWebEngineEvergreen(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the system is using the evergreen kernel. If the system is using the evergreen kernel, **true** is returned. Otherwise, **false** is returned. |

**Examples**

This example shows how to determine whether the evergreen kernel is used in the EntryAbility creation phase.

```TypeScript
// xxx.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate")
    if (webview.WebviewController.isActiveWebEngineEvergreen()) {
      console.info("Active Web Engine is Evergreen")
    }
    console.info("EntryAbility onCreate done")
  }
}
```

## isAdsBlockEnabled

```TypeScript
isAdsBlockEnabled(): boolean
```

Get whether Ads block is enabled.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-isAdsBlockEnabled(): boolean--><!--Device-WebviewController-isAdsBlockEnabled(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if the ability of AdsBlock is enabled; else false. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

**Examples**

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
      Button('isAdsBlockEnabled')
        .onClick(() => {
          try {
            let isAdsBlockEnabled: boolean = this.controller.isAdsBlockEnabled();
            console.info("isAdsBlockEnabled:", isAdsBlockEnabled);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## isAdsBlockEnabledForCurPage

```TypeScript
isAdsBlockEnabledForCurPage(): boolean
```

Get whether Ads block is enabled for current Webpage.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-isAdsBlockEnabledForCurPage(): boolean--><!--Device-WebviewController-isAdsBlockEnabledForCurPage(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if the ability of AdsBlock is enabled for current Webpage; else false. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

**Examples**

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
      Button('isAdsBlockEnabledForCurPage')
        .onClick(() => {
          try {
            let isAdsBlockEnabledForCurPage: boolean = this.controller.isAdsBlockEnabledForCurPage();
            console.info("isAdsBlockEnabledForCurPage:", isAdsBlockEnabledForCurPage);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## isAutoPreconnectEnabled

```TypeScript
static isAutoPreconnectEnabled(): boolean
```

‌Retrieve whether the automatic pre-connection feature is enabled‌.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static isAutoPreconnectEnabled(): boolean--><!--Device-WebviewController-static isAutoPreconnectEnabled(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Return true if enabled, false if disabled. |

**Examples**

```TypeScript
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  build() {
    Column() {
      Button('isAutoPreconnectEnabled')
        .onClick(() => {
          try {
            let isEnabled: boolean = webview.WebviewController.isAutoPreconnectEnabled();
            console.info("isAutoPreconnectEnabled:", isEnabled);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
    }
  }
}
```

## isIncognitoMode

```TypeScript
isIncognitoMode(): boolean
```

Whether the incognito mode is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-isIncognitoMode(): boolean--><!--Device-WebviewController-isIncognitoMode(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('isIncognitoMode')
        .onClick(() => {
          try {
            let result = this.controller.isIncognitoMode();
            console.info('isIncognitoMode' + result);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## isIntelligentTrackingPreventionEnabled

```TypeScript
isIntelligentTrackingPreventionEnabled(): boolean
```

Get whether Intelligent Tracking Prevention is enabled.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-isIntelligentTrackingPreventionEnabled(): boolean--><!--Device-WebviewController-isIntelligentTrackingPreventionEnabled(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if enable the Intelligent Tracking Prevention; else false. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

**Examples**

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
      Button('isIntelligentTrackingPreventionEnabled')
        .onClick(() => {
          try {
            let result = this.controller.isIntelligentTrackingPreventionEnabled();
            console.info("result: " + result);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## isPrivateNetworkAccessEnabled

```TypeScript
static isPrivateNetworkAccessEnabled(): boolean
```

Get whether PrivateNetworkAccess is enabled.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static isPrivateNetworkAccessEnabled(): boolean--><!--Device-WebviewController-static isPrivateNetworkAccessEnabled(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True is enable the ability to check private network access else false. |

**Examples**

```TypeScript
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('isPrivateNetworkAccessEnabled')
        .onClick(() => {
          try {
            let isEnabled: boolean = webview.WebviewController.isPrivateNetworkAccessEnabled();
            console.info("isPrivateNetworkAccessEnabled:", isEnabled);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .onControllerAttached(() => {
          // If the value is set to false, ArkWeb does not check whether the private network request is valid.
          webview.WebviewController.enablePrivateNetworkAccess(false);
        })
    }
  }
}
```

## isSafeBrowsingEnabled

```TypeScript
isSafeBrowsingEnabled(): boolean
```

Get whether checking website security risks is enabled.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-isSafeBrowsingEnabled(): boolean--><!--Device-WebviewController-isSafeBrowsingEnabled(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if enable the ability to check website security risks else false. |

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
      Button('isSafeBrowsingEnabled')
        .onClick(() => {
          let result = this.controller.isSafeBrowsingEnabled();
          console.info("result: " + result);
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## loadData

```TypeScript
loadData(data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string): void
```

Loads the data or URL.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-loadData(data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string): void--><!--Device-WebviewController-loadData(data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | string | Yes | A string encoded according to "Base64" or "URL". |
| mimeType | string | Yes | Media type. For example: "text/html". |
| encoding | string | Yes | Encoding type. For example: "UTF-8". |
| baseUrl | string | No | A specified URL path ("http"/"https"/"data" protocol), which is assigned to window.origin by the Web component. |
| historyUrl | string | No | History URL. When it is not empty, it can be managed by history records to realize the back and forth function. This property is invalid when baseUrl is empty. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

When both baseUrl and historyUrl are empty:

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
      Button('loadData')
        .onClick(() => {
          try {
            this.controller.loadData(
              "<html><body bgcolor=\"white\">Source:<pre>source</pre></body></html>",
              "text/html",
              // UTF-8 is charset.
              "UTF-8"
            );
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

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
      Button('loadData')
        .onClick(() => {
          try {
            this.controller.loadData(
              // Coding tests: string encoded using base64.
              "Q29kaW5nIHRlc3Rz",
              "text/html",
              "base64"
            );
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

Specify baseURL.

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
      Button('loadData')
        .onClick(() => {
          try {
            this.controller.loadData(
              "<img src=aa/bb.jpg>", // Attempt to load the image from "https: // xxx.com/" + "aa/bb.jpg".
              "text/html",
              "UTF-8",
              "https://xxx.com/",
              "about:blank"
            );
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

Example of loading local resource:

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  updataContent: string = '<body><div><image src="resource://rawfile/xxx.png" alt="image -- end" width="500" height="250"></image></div></body>'

  build() {
    Column() {
      Button('loadData')
        .onClick(() => {
          try {
            // UTF-8 is charset.
            this.controller.loadData(this.updataContent, "text/html", "UTF-8", " ", " ");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

Load the sandbox image.

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
      Button('loadData')
        .onClick(() => {
          try {
            this.controller.loadData(
              "<img src=bb.jpg>", // Try to download the image from "file:///xxx/" + "bb.jpg".
              "text/html",
              "UTF-8",
              // Load the image path in the local application sandbox. Change the path to the actual sandbox path.
              "file:///data/storage/el2/base/haps/entry/files/data/.cache_dir/",
              ""
            );
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .fileAccess(true) // Enable the file access functionality to load images in the application sandbox.
    }
  }
}
```

## loadUrl

```TypeScript
loadUrl(url: string | Resource, headers?: Array<WebHeader>): void
```

Loads the data or URL.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-loadUrl(url: string | Resource, headers?: Array<WebHeader>): void--><!--Device-WebviewController-loadUrl(url: string | Resource, headers?: Array<WebHeader>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes | The URL to load. |
| headers | Array&lt;WebHeader&gt; | No | Additional HTTP request header for URL. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-incorrect-url-format) | URL error. The webpage corresponding to the URL is invalid. |
| [17100003](../../apis-arkweb/errorcode-webview.md#17100003-incorrect-resource-path) | Invalid resource path or file type. |

**Examples**

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
      Button('loadUrl')
        .onClick(() => {
          try {
            // The URL to be loaded is of the string type.
            this.controller.loadUrl('www.example.com');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

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
      Button('loadUrl')
        .onClick(() => {
          try {
            // The headers parameter is passed.
            this.controller.loadUrl('www.example.com', [{ headerKey: "headerKey", headerValue: "headerValue" }]);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

Using $rawfile.

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
      Button('loadUrl')
        .onClick(() => {
          try {
            // Load a local resource file through $rawfile.
            this.controller.loadUrl($rawfile('index.html'));
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

When $rawfile is used to load a URL contains a number sign (#), the content following the number sign is treated as a fragment. To avoid this issue, you can use the resource://rawfile/ protocol prefix instead.

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
      Button('loadUrl')
        .onClick(() => {
          try {
            // Load local resource files through the resource protocol.
            this.controller.loadUrl("resource://rawfile/index.html#home");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

Create an index.html file in src/main/resources/rawfile.

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
<body>
<div id="content"></div>

<script>
  function loadContent() {
    var hash = window.location.hash;
    var contentDiv = document.getElementById('content');

    if (hash === '#home') {
      contentDiv.innerHTML = '<h1>Home Page</h1><p>Welcome to the Home Page!</p>';
    } else {
      contentDiv.innerHTML = '<h1>Default Page</h1><p>This is the default content.</p>';
    }
  }

  // Load the UI.
  window.addEventListener('load', loadContent);

  // Update the UI when the hash changes.
  window.addEventListener('hashchange', loadContent);
</script>
</body>
</html>
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
  <body>
    <p>Hello World</p>
  </body>
</html>
```

## offControllerAttachStateChange

```TypeScript
offControllerAttachStateChange(callback?: Callback<ControllerAttachState>): void
```

Unregister the callback for controller attach state change.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-offControllerAttachStateChange(callback?: Callback<ControllerAttachState>): void--><!--Device-WebviewController-offControllerAttachStateChange(callback?: Callback<ControllerAttachState>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ControllerAttachState](arkts-webview-controllerattachstate-e.md)&gt; | No | Callback used to return the controller attach state. |

## onActive

```TypeScript
onActive(): void
```

Call this interface to notify the Web component to enter the foreground activation state. The activation state is the state in which the application interacts with the user. The application will remain in this state until something happens, such as receiving an incoming call or closing the screen of the device, to shift the focus away from the application.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-onActive(): void--><!--Device-WebviewController-onActive(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('onActive')
        .onClick(() => {
          try {
            this.controller.onActive();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## onControllerAttachStateChange

```TypeScript
onControllerAttachStateChange(callback: Callback<ControllerAttachState>): void
```

Register the callback for controller attach state change.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-onControllerAttachStateChange(callback: Callback<ControllerAttachState>): void--><!--Device-WebviewController-onControllerAttachStateChange(callback: Callback<ControllerAttachState>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ControllerAttachState](arkts-webview-controllerattachstate-e.md)&gt; | Yes | Callback used to return the controller attach state. |

## onCreateNativeMediaPlayer

```TypeScript
onCreateNativeMediaPlayer(callback: CreateNativeMediaPlayerCallback): void
```

Called when the [application takes over media playback of the web page](../../../reference/apis-arkweb/arkts-basic-components-web-attributes.md#enablenativemediaplayer12) and a media file is played on the web page.If the application does not take over media playback on the web page, this callback is not invoked.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-onCreateNativeMediaPlayer(callback: CreateNativeMediaPlayerCallback): void--><!--Device-WebviewController-onCreateNativeMediaPlayer(callback: CreateNativeMediaPlayerCallback): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [CreateNativeMediaPlayerCallback](arkts-webview-createnativemediaplayercallback-t.md) | Yes | Callback when the application takes over media playback on the web page. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

class ActualNativeMediaPlayerListener {
  handler: webview.NativeMediaPlayerHandler;

  constructor(handler: webview.NativeMediaPlayerHandler) {
    this.handler = handler;
  }

  onPlaying() {
    // The native media player starts playback.
    this.handler.handleStatusChanged(webview.PlaybackStatus.PLAYING);
  }
  onPaused() {
    // The native media player pauses the playback.
    this.handler.handleStatusChanged(webview.PlaybackStatus.PAUSED);
  }
  onSeeking() {
    // The local player starts to jump to the target time point.
    this.handler.handleSeeking();
  }
  onSeekDone() {
    // The native media player seeks to the target time point.
    this.handler.handleSeekFinished();
  }
  onEnded() {
    // The playback on the native media player is ended.
    this.handler.handleEnded();
  }
  onVolumeChanged() {
    // Obtain the volume of the local player.
    let volume: number = getVolume();
    this.handler.handleVolumeChanged(volume);
  }
  onCurrentPlayingTimeUpdate() {
    // Update the playback time.
    let currentTime: number = getCurrentPlayingTime();
    // Convert the time unit to second.
    let currentTimeInSeconds = convertToSeconds(currentTime);
    this.handler.handleTimeUpdate(currentTimeInSeconds);
  }
  onBufferedChanged() {
    // The cache is changed.
    // Obtain the cache duration of the native media player.
    let bufferedEndTime: number = getCurrentBufferedTime();
    // Convert the time unit to second.
    let bufferedEndTimeInSeconds = convertToSeconds(bufferedEndTime);
    this.handler.handleBufferedEndTimeChanged(bufferedEndTimeInSeconds);

    // Check the cache status.
    // If the cache status changes, notify the ArkWeb engine of the cache status.
    let lastReadyState: webview.ReadyState = getLastReadyState();
    let currentReadyState:  webview.ReadyState = getCurrentReadyState();
    if (lastReadyState != currentReadyState) {
      this.handler.handleReadyStateChanged(currentReadyState);
    }
  }
  onEnterFullscreen() {
    // The native media player enters the full screen mode.
    let isFullscreen: boolean = true;
    this.handler.handleFullscreenChanged(isFullscreen);
  }
  onExitFullscreen() {
    // The native media player exits the full screen mode.
    let isFullscreen: boolean = false;
    this.handler.handleFullscreenChanged(isFullscreen);
  }
  onUpdateVideoSize(width: number, height: number) {
    // Notify the ArkWeb kernel when the native media player parses the video width and height.
    this.handler.handleVideoSizeChanged(width, height);
  }
  onDurationChanged(duration: number) {
    // Notify the ArkWeb kernel when the native media player parses the video duration.
    this.handler.handleDurationChanged(duration);
  }
  onError(error: webview.MediaError, errorMessage: string) {
    // Notify the ArkWeb kernel that an error occurs in the native media player.
    this.handler.handleError(error, errorMessage);
  }
  onNetworkStateChanged(state: webview.NetworkState) {
    // Notify the ArkWeb kernel that the network state of the native media player changes.
    this.handler.handleNetworkStateChanged(state);
  }
  onPlaybackRateChanged(playbackRate: number) {
    // Notify the ArkWeb kernel that the playback rate of the native media player changes.
    this.handler.handlePlaybackRateChanged(playbackRate);
  }
  onMutedChanged(muted: boolean) {
    // Notify the ArkWeb kernel that the native media player is muted.
    this.handler.handleMutedChanged(muted);
  }

  // Listen for other state of the native media player.
}

class NativeMediaPlayerImpl implements webview.NativeMediaPlayerBridge {
  constructor(handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo) {
    // 1. Create a listener for the native media player.
    let listener: ActualNativeMediaPlayerListener = new ActualNativeMediaPlayerListener(handler);
    // 2. Create a native media player.
    // 3. Listen for the local player.
    // ...
  }

  updateRect(x: number, y: number, width: number, height: number) {
    // The position and size of the <video> tag are changed.
    // Make changes based on the information change.
  }

  play() {
    // Start the native media player for playback.
  }

  pause() {
    //Pause the playback on the local player.
  }

  seek(targetTime: number) {
    // The local player jumps to a specified time point.
  }

  release() {
    // Destroy the local player.
  }

  setVolume(volume: number) {
    // The ArkWeb kernel requires to adjust the volume of the local player.
    // Set the volume of the local player.
  }

  setMuted(muted: boolean) {
    // Mute or unmute the local player.
  }

  setPlaybackRate(playbackRate: number) {
    // Adjust the playback speed of the local player.
  }

  enterFullscreen() {
    // Set the local player to play in full screen mode.
  }

  exitFullscreen() {
    // Set the local player to exit full screen mode.
  }

  resumePlayer() {
    // Create a player again.
    // Resume the status information of the player.
  }

  suspendPlayer(type: webview.SuspendType) {
    // Record the status information of the player.
    // Destroy the player.
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController()
  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .enableNativeMediaPlayer({enable: true, shouldOverlay: false})
        .onPageBegin((event) => {
          this.controller.onCreateNativeMediaPlayer((handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo) => {
            if (!shouldHandle(mediaInfo)) {
              // The local player does not take over the media.
              // The ArkWeb engine will play the media with its own player.
              return null;
            }
            let nativePlayer: webview.NativeMediaPlayerBridge = new NativeMediaPlayerImpl(handler, mediaInfo);
            return nativePlayer;
          });
        })
    }
  }
}

// stub
function getVolume() {
  return 1;
}
function getCurrentPlayingTime() {
  return 1;
}
function getCurrentBufferedTime() {
  return 1;
}
function convertToSeconds(input: number) {
  return input;
}
function getLastReadyState() {
  return webview.ReadyState.HAVE_NOTHING;
}
function getCurrentReadyState() {
  return webview.ReadyState.HAVE_NOTHING;
}
function shouldHandle(mediaInfo: webview.MediaInfo) {
  return true;
}
```

## onInactive

```TypeScript
onInactive(): void
```

Call this interface to notify the Web component to enter the inactive state. In this callback, the developer can realize the appropriate behavior when the application loses focus. In this state, any content that can be safely paused will be paused as much as possible, such as animation and geographical location. However, JavaScript will not be paused. To pause JavaScript globally, please use [pauseAllTimers](#pausealltimers).To reactivate the Web component, call onActive.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-onInactive(): void--><!--Device-WebviewController-onInactive(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('onInactive')
        .onClick(() => {
          try {
            this.controller.onInactive();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## pageDown

```TypeScript
pageDown(bottom: boolean): void
```

Scroll the contents of this Webview down by half the view size.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-pageDown(bottom: boolean): void--><!--Device-WebviewController-pageDown(bottom: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bottom | boolean | Yes | Whether to jump to the bottom of the page, if set to false, the page content will scroll down half the size of the view frame, and when set to true, it will jump to the bottom of the page. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('pageDown')
        .onClick(() => {
          try {
            this.controller.pageDown(false);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile("index.html"), controller: this.controller })
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
    <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .blue {
          background-color: lightblue;
        }
        .green {
          background-color: lightgreen;
        }
        .blue, .green {
         font-size:16px;
         height:200px;
         text-align: center;       /* Horizontally centered */
         line-height: 200px;       /* Vertically centered (the height matches the container height) */
        }
    </style>
</head>
<body>
<div class="blue" >webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
</body>
</html>
```

## pageUp

```TypeScript
pageUp(top: boolean): void
```

Scroll the contents of this Webview up by half the view size.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-pageUp(top: boolean): void--><!--Device-WebviewController-pageUp(top: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| top | boolean | Yes | Whether to jump to the top of the page, if set to false, the page content will scroll up half the size of the view frame, and when set to true, it will jump to the top of the page. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('pageUp')
        .onClick(() => {
          try {
            this.controller.pageUp(false);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile("index.html"), controller: this.controller })
    }
  }
}
```

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .blue {
          background-color: lightblue;
        }
        .green {
          background-color: lightgreen;
        }
        .blue, .green {
         font-size:16px;
         height:200px;
         text-align: center;       /* Horizontally centered */
         line-height: 200px;       /* Vertically centered (the height matches the container height) */
        }
    </style>
</head>
<body>
<div class="blue" >webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
</body>
</html>
```

## pauseAllMedia

```TypeScript
pauseAllMedia(): void
```

Pauses all audio and video on a web page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-pauseAllMedia(): void--><!--Device-WebviewController-pauseAllMedia(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('pauseAllMedia')
        .onClick(() => {
          try {
            this.controller.pauseAllMedia();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## pauseAllTimers

```TypeScript
static pauseAllTimers(): void
```

Pause all WebView timers.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static pauseAllTimers(): void--><!--Device-WebviewController-static pauseAllTimers(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Row() {
        Button('PauseAllTimers')
          .onClick(() => {
            webview.WebviewController.pauseAllTimers();
          })
      }
      Web({ src: $rawfile("index.html"), controller: this.controller })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!DOCTYPE html>
<html>
    <body>
        <button style="width:300px;height:150px;font-size:50px" onclick="startTimer()">start</button>
        <button style="width:300px;height:150px;font-size:50px" onclick="resetTimer()">reset</button>
        <input style="width:300px;height:150px;font-size:50px" value="0" id="show_num">
    </body>
</html>
<script>
    var timer = null;
    var num = 0;

    function startTimer() {
        timer = setInterval(function() {
            document.getElementById("show_num").value = ++num;
        }, 1000);
    }
    
    function resetTimer() {
        clearInterval(timer);
        document.getElementById("show_num").value = 0;
        num = 0;
    }
</script>
```

## pauseMicrophone

```TypeScript
pauseMicrophone(): void
```

Pauses microphone capture on the current web page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-pauseMicrophone(): void--><!--Device-WebviewController-pauseMicrophone(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

For the complete sample code, see [resumeMicrophone](#resumemicrophone).

## postMessage

```TypeScript
postMessage(name: string, ports: Array<WebMessagePort>, uri: string): void
```

Post web message port to html

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-postMessage(name: string, ports: Array<WebMessagePort>, uri: string): void--><!--Device-WebviewController-postMessage(name: string, ports: Array<WebMessagePort>, uri: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Data name information to send. |
| ports | Array&lt;[WebMessagePort](arkts-webview-webmessageport-i.md)&gt; | Yes | Port number array information to send. |
| uri | string | Yes | URI to receive this information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  ports: webview.WebMessagePort[] = [];
  @State sendFromEts: string = 'Send this message from ets to HTML';
  @State receivedFromHtml: string = 'Display received message send from HTML';

  build() {
    Column() {
      // Display the received HTML content.
      Text(this.receivedFromHtml)
      // Send the content in the text box to an HTML window.
      TextInput({ placeholder: 'Send this message from ets to HTML' })
        .onChange((value: string) => {
          this.sendFromEts = value;
        })

      Button('postMessage')
        .onClick(() => {
          try {
            // 1. Create two message ports.
            this.ports = this.controller.createWebMessagePorts();
            // 2. Register a callback on a message port (for example, port 1) on the application side.
            this.ports[1].onMessageEvent((result: webview.WebMessage) => {
              let msg = 'Got msg from HTML:';
              if (typeof (result) == "string") {
                console.info("received string message from html5, string is:" + result);
                msg = msg + result;
              } else if (typeof (result) == "object") {
                if (result instanceof ArrayBuffer) {
                  console.info("received arraybuffer from html5, length is:" + result.byteLength);
                  msg = msg + "length is " + result.byteLength;
                } else {
                  console.info("not support");
                }
              } else {
                console.info("not support");
              }
              this.receivedFromHtml = msg;
            })
            // 3. Send another message port (for example, port 0) to the HTML side, which can then save the port for future use.
            this.controller.postMessage('__init_port__', [this.ports[0]], '*');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })

      // 4. Use the port on the application side to send messages to the port that has been sent to the HTML side.
      Button('SendDataToHTML')
        .onClick(() => {
          try {
            if (this.ports && this.ports[1]) {
              this.ports[1].postMessageEvent(this.sendFromEts);
            } else {
              console.error(`ports is null, Please initialize first`);
            }
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebView Message Port Demo</title>
</head>

  <body>
    <h1>WebView Message Port Demo</h1>
    <div>
        <input type="button" value="SendToEts" onclick="PostMsgToEts(msgFromJS.value);"/><br/>
        <input id="msgFromJS" type="text" value="send this message from HTML to ets"/><br/>
    </div>
    <p class="output">display received message send from ets</p>
  </body>
  <script src="xxx.js"></script>
</html>
```

```TypeScript
// xxx.js
var h5Port;
var output = document.querySelector('.output');
window.addEventListener('message', function (event) {
    if (event.data == '__init_port__') {
        if (event.ports[0] != null) {
            h5Port = event.ports[0]; // 1. Save the port number sent from the eTS side.
            h5Port.onmessage = function (event) {
              // 2. Receive the message sent from the eTS side.
              var msg = 'Got message from ets:';
              var result = event.data;
              if (typeof(result) == "string") {
                console.info("received string message from html5, string is:" + result);
                msg = msg + result;
              } else if (typeof(result) == "object") {
                if (result instanceof ArrayBuffer) {
                  console.info("received arraybuffer from html5, length is:" + result.byteLength);
                  msg = msg + "length is " + result.byteLength;
                } else {
                  console.info("not support");
                }
              } else {
                console.info("not support");
              }
              output.innerHTML = msg;
            }
        }
    }
})

// 3. Use h5Port to send messages to the eTS side.
function PostMsgToEts(data) {
    if (h5Port) {
      h5Port.postMessage(data);
    } else {
      console.error("h5Port is null, Please initialize first");
    }
}
```

## postUrl

```TypeScript
postUrl(url: string, postData: ArrayBuffer): void
```

Loads the URL use "POST" method with post data.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-postUrl(url: string, postData: ArrayBuffer): void--><!--Device-WebviewController-postUrl(url: string, postData: ArrayBuffer): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | Request the URL use "POST" method. |
| postData | ArrayBuffer | Yes | This data will passed to "POST" request. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-incorrect-url-format) | URL error. The webpage corresponding to the URL is invalid. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class TestObj {
  constructor() {
  }

  test(str: string): ArrayBuffer {
    let buf = new ArrayBuffer(str.length);
    let buff = new Uint8Array(buf);

    for (let i = 0; i < str.length; i++) {
      buff[i] = str.charCodeAt(i);
    }
    return buf;
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State testObjtest: TestObj = new TestObj();

  build() {
    Column() {
      Button('postUrl')
        .onClick(() => {
          try {
            // Convert data to the ArrayBuffer type.
            let postData = this.testObjtest.test("Name=test&Password=test");
            this.controller.postUrl('www.example.com', postData);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: '', controller: this.controller })
    }
  }
}
```

## precompileJavaScript

```TypeScript
precompileJavaScript(url: string, script: string | Uint8Array, cacheOptions: CacheOptions): Promise<int>
```

Compile javascript and generate code cache.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-precompileJavaScript(url: string, script: string | Uint8Array, cacheOptions: CacheOptions): Promise<int>--><!--Device-WebviewController-precompileJavaScript(url: string, script: string | Uint8Array, cacheOptions: CacheOptions): Promise<int>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | Url of the javascript. Only support HTTP/HTTPS protocol and length no longer than 2048. |
| script | string \| Uint8Array | Yes | Javascript source code. script must not be empty. |
| cacheOptions | [CacheOptions](arkts-webview-cacheoptions-i.md) | Yes | Generate code cache option. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | The promise returned by the function. 0 means generate code cache successfully, -1 means internal error. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid input parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

Save UIContext to localStorage in EntryAbility.

```TypeScript
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

const localStorage: LocalStorage = new LocalStorage('uiContext');

export default class EntryAbility extends UIAbility {
  storage: LocalStorage = localStorage;

  onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage.loadContent('pages/Index', this.storage, (err, data) => {
      if (err.code) {
        return;
      }

      this.storage.setOrCreate<UIContext>("uiContext", windowStage.getMainWindowSync().getUIContext());
    });
  }
}
```

Write the basic code required by the dynamic component.

```TypeScript
// DynamicComponent.ets
import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

export interface BuilderData {
  url: string;
  controller: WebviewController;
  context: UIContext;
}

let storage : LocalStorage | undefined = undefined;

export class NodeControllerImpl extends NodeController {
  private rootNode: BuilderNode<BuilderData[]> | null = null;
  private wrappedBuilder: WrappedBuilder<BuilderData[]> | null = null;

  constructor(wrappedBuilder: WrappedBuilder<BuilderData[]>, context: UIContext) {
    storage = context.getSharedLocalStorage();
    super();
    this.wrappedBuilder = wrappedBuilder;
  }

  makeNode(): FrameNode | null {
    if (this.rootNode != null) {
      return this.rootNode.getFrameNode();
    }
    return null;
  }

  initWeb(url: string, controller: WebviewController) {
    if(this.rootNode != null) {
      return;
    }

    const uiContext: UIContext = storage!.get<UIContext>("uiContext") as UIContext;
    if (!uiContext) {
      return;
    }
    this.rootNode = new BuilderNode(uiContext);
    this.rootNode.build(this.wrappedBuilder, { url: url, controller: controller });
  }
}

export const createNode = (wrappedBuilder: WrappedBuilder<BuilderData[]>, data: BuilderData) => {
  const baseNode = new NodeControllerImpl(wrappedBuilder, data.context);
  baseNode.initWeb(data.url, data.controller);
  return baseNode;
}
```

Write a component for generating bytecode caches. In this example, the local JavaScript resource content is read through the file reading API from a local file in the rawfile directory.

```TypeScript
// PrecompileWebview.ets
import { BuilderData } from "./DynamicComponent";
import { Config, configs } from "./PrecompileConfig";

@Builder
function WebBuilder(data: BuilderData) {
  Web({ src: data.url, controller: data.controller })
    .onControllerAttached(() => {
      precompile(data.controller, configs, data.context);
    })
    .fileAccess(true)
}

export const precompileWebview = wrapBuilder<BuilderData[]>(WebBuilder);

export const precompile = async (controller: WebviewController, configs: Array<Config>, context: UIContext) => {
  for (const config of configs) {
    let content = await readRawFile(config.localPath, context);

    try {
      controller.precompileJavaScript(config.url, content, config.options)
        .then(errCode => {
          console.error("precompile successfully! " + errCode);
        }).catch((errCode: number) => {
          console.error("precompile failed. " + errCode);
      });
    } catch (err) {
      console.error("precompile failed. " + err.code + " " + err.message);
    }
  }
}

async function readRawFile(path: string, context: UIContext) {
  try {
    return await context.getHostContext()!.resourceManager.getRawFileContent(path);
  } catch (err) {
    return new Uint8Array(0);
  }
}
```

Compile the code of the service component.

```TypeScript
// BusinessWebview.ets
import { BuilderData } from "./DynamicComponent";

@Builder
function WebBuilder(data: BuilderData) {
  // The component can be extended based on service requirements.
  Web({ src: data.url, controller: data.controller })
    .cacheMode(CacheMode.Default)
}

export const businessWebview = wrapBuilder<BuilderData[]>(WebBuilder);
```

Write the resource configuration information.

```TypeScript
// PrecompileConfig.ets
import { webview } from '@kit.ArkWeb'

export interface Config {
  url:  string,
  localPath: string, // Local resource path
  options: webview.CacheOptions
}

export let configs: Array<Config> = [
  {
    url: "https://www.example.com/example.js",
    localPath: "example.js",
    options: {
      responseHeaders: [
        { headerKey: "E-Tag", headerValue: "aWO42N9P9dG/5xqYQCxsx+vDOoU="},
        { headerKey: "Last-Modified", headerValue: "Wed, 21 Mar 2024 10:38:41 GMT"}
      ]
    }
  }
]
```

Use the component on the page.

```TypeScript
// Index.ets
import { webview } from '@kit.ArkWeb';
import { NodeController } from '@kit.ArkUI';
import { createNode } from "./DynamicComponent"
import { precompileWebview } from "./PrecompileWebview"
import { businessWebview } from "./BusinessWebview"

@Entry
@Component
struct Index {
  @State precompileNode: NodeController | undefined = undefined;
  precompileController: webview.WebviewController = new webview.WebviewController();

  @State businessNode: NodeController | undefined = undefined;
  businessController: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    // Initialize the Web component used to inject local resources.
    this.precompileNode = createNode(precompileWebview,
      { url: "https://www.example.com/empty.html", controller: this.precompileController, context: this.getUIContext()});
  }

  build() {
    Column() {
      // Load the Web component used by the service at a proper time. In this example, the button is clicked.
      Button("Load Page")
        .onClick(() => {
          this.businessNode = createNode(businessWebview, {
            url:  "https://www.example.com/business.html",
            controller: this.businessController,
            context: this.getUIContext()
          });
        })
      // The Web component used for the service.
      NodeContainer(this.businessNode);
    }
  }
}
```

## prefetchPage

```TypeScript
prefetchPage(url: string, additionalHeaders?: Array<WebHeader>): void
```

Prefetch the resources required by the page, but will not execute js or render the page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-prefetchPage(url: string, additionalHeaders?: Array<WebHeader>): void--><!--Device-WebviewController-prefetchPage(url: string, additionalHeaders?: Array<WebHeader>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | Which url to preresolve/preconnect. |
| additionalHeaders | Array&lt;WebHeader&gt; | No | Additional HTTP request header of the URL. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-incorrect-url-format) | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2*1024*1024. |

**Examples**

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
      Button('prefetchPopularPage')
        .onClick(() => {
          try {
            // Replace 'https://www.example.com' with a real URL for the API to work.
            let options = new webview.PrefetchOptions();
            options.ignoreCacheControlNoStore = true;
            options.minTimeBetweenPrefetchesMs = 100;
            this.controller.prefetchPage('https://www.example.com', [{ headerKey: "headerKey", headerValue: "headerValue" }], options);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      // Replace ''www.example1.com' with a real URL for the API to work.
      Web({ src: 'www.example1.com', controller: this.controller })
    }
  }
}
```

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
      Button('prefetchPopularPage')
        .onClick(() => {
          try {
            // Replace 'https://www.example.com' with a real URL for the API to work.
            this.controller.prefetchPage('https://www.example.com');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      // Replace ''www.example1.com' with a real URL for the API to work.
      Web({ src: 'www.example1.com', controller: this.controller })
    }
  }
}
```

## prefetchPage

```TypeScript
prefetchPage(url: string, additionalHeaders?: Array<WebHeader>, prefetchOptions?: PrefetchOptions): void
```

Prefetch the resources required by the page, but will not execute js or render the page. <p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> ‌prefetchPage‌ does not cache resources with Cache-Control: no-store by default, and only allows one prefetch within 500ms. Prefetch behavior can be customized via ‌prefetchOptions‌, including ignoring Cache-Control: no-store and adjusting the throttling interval.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-prefetchPage(url: string, additionalHeaders?: Array<WebHeader>, prefetchOptions?: PrefetchOptions): void--><!--Device-WebviewController-prefetchPage(url: string, additionalHeaders?: Array<WebHeader>, prefetchOptions?: PrefetchOptions): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | Which url to preresolve/preconnect. |
| additionalHeaders | Array&lt;WebHeader&gt; | No | Additional HTTP request header of the URL. |
| prefetchOptions | [PrefetchOptions](arkts-webview-prefetchoptions-c.md) | No | Prefetch behavior can be customized via ‌prefetchOptions‌, including ignoring Cache-Control: no-store and adjusting the throttling interval. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-incorrect-url-format) | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2*1024*1024. |

**Examples**

See [prefetchPage](#prefetchpage)

## prefetchResource

```TypeScript
static prefetchResource(request: RequestInfo, additionalHeaders?: Array<WebHeader>, cacheKey?: string,
        cacheValidTime?: int): void
```

Prefetches resource requests based on specified request information and additional HTTP request headers, saves the requests to the memory cache, and specifies the cache key and validity period to accelerate loading. Currently, only POST requests whose Content-Type is application/x-www-form-urlencoded are supported. A maximum of six POST requests can be pre-obtained. To prefetch the seventh post request, call API[clearPrefetchedResource](#clearprefetchedresource) to clear the cache of unnecessary post requests. Otherwise, the cache of the earliest prefetched POST request will be automatically cleared. To use the prefetched resource cache, you need to add the key value ArkWebPostCacheKey to the header of the POST request. The content of the key value is the cacheKey of the corresponding cache.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static prefetchResource(request: RequestInfo, additionalHeaders?: Array<WebHeader>, cacheKey?: string,        cacheValidTime?: int): void--><!--Device-WebviewController-static prefetchResource(request: RequestInfo, additionalHeaders?: Array<WebHeader>, cacheKey?: string,        cacheValidTime?: int): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| request | RequestInfo | Yes | The information of the request. |
| additionalHeaders | Array&lt;WebHeader&gt; | No | Additional HTTP request header of the request. |
| cacheKey | string | No | The key for memory cache. Default value is the url of the request. Only support number and letters. |
| cacheValidTime | int | No | The valid time of the cache for request, ranges greater than 0. The unit is second. Default value is 300s. The value of cacheValidTime must between 1 and 2147483647. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-incorrect-url-format) | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2 *1024 *1024. |

**Examples**

```TypeScript
// EntryAbility.ets
import { webview } from '@kit.ArkWeb';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    // Replace "https://www.example1.com/post?e=f&g=h" with a real URL to visit.
    webview.WebviewController.prefetchResource(
      {
        url: "https://www.example1.com/post?e=f&g=h",
        method: "POST",
        formData: "a=x&b=y",
      },
      [{
        headerKey: "c",
        headerValue: "z",
      },],
      "KeyX", 500);
    AppStorage.setOrCreate("abilityWant", want);
    console.info("EntryAbility onCreate done");
  }
}
```

## prepareForPageLoad

```TypeScript
static prepareForPageLoad(url: string, preconnectable: boolean, numSockets: int): void
```

Preresolve or Preconnect the url. This API can be called before loading the url to make loading faster.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static prepareForPageLoad(url: string, preconnectable: boolean, numSockets: int): void--><!--Device-WebviewController-static prepareForPageLoad(url: string, preconnectable: boolean, numSockets: int): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | Which url to preresolve/preconnect. |
| preconnectable | boolean | Yes | Indicates whether to preconnect. |
| numSockets | int | Yes | If preconnectable is true, this parameter indicates the number of sockets to be preconnected. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-incorrect-url-format) | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2048. |
| [17100013](../../apis-arkweb/errorcode-webview.md#17100013-invalid-number-of-sockets-during-preconnection) | The number of preconnect sockets is invalid. |

**Examples**

```TypeScript
// EntryAbility.ets
import { webview } from '@kit.ArkWeb';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    // Replace 'https://www.example.com' with a real URL for the API to work.
    webview.WebviewController.prepareForPageLoad("https://www.example.com", true, 2);
    AppStorage.setOrCreate("abilityWant", want);
    console.info("EntryAbility onCreate done");
  }
}
```

## refresh

```TypeScript
refresh(): void
```

Refreshes the current URL.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-refresh(): void--><!--Device-WebviewController-refresh(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('refresh')
        .onClick(() => {
          try {
            this.controller.refresh();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

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
      Button('refresh')
        .onClick(() => {
          try {
            this.controller.refresh(true);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## refresh

```TypeScript
refresh(ignoreCache: boolean): void
```

Refreshes the current URL.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebviewController-refresh(ignoreCache: boolean): void--><!--Device-WebviewController-refresh(ignoreCache: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ignoreCache | boolean | Yes | If set to true, it indicates an end-to-end request with "pragma: no-cache"; otherwise, it performs a normal refresh. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

See [refresh](#refresh)

## registerJavaScriptProxy

```TypeScript
registerJavaScriptProxy(jsObject: object, name: string, methodList: Array<string>,
            asyncMethodList?: Array<string>, permission?: string): void
```

Registers the supplied ArkTS object into this Web component. The object is registered into all frames of the web page, including all iframes, using the specified name. This allows the methods of the ArkTS object to be accessed from JavaScript. <p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> Registed objects will not appear in JavaScript until the page is next (re)load. To avoid memory leaks, registerJavaScriptProxy must be used together with deleteJavaScriptProxy. To avoid security risks, it is recommended that registerJavaScriptProxy be used with trusted web components. If the same method is registered repeatedly in both synchronous and asynchronous list, it will default to an asynchronous method. The synchronous function list and asynchronous function list cannot be empty at the same time.<br> otherwise, this registration will fail. <p>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-registerJavaScriptProxy(jsObject: object, name: string, methodList: Array<string>,            asyncMethodList?: Array<string>, permission?: string): void--><!--Device-WebviewController-registerJavaScriptProxy(jsObject: object, name: string, methodList: Array<string>,            asyncMethodList?: Array<string>, permission?: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| jsObject | object | Yes | Application side JavaScript objects participating in registration. |
| name | string | Yes | The name of the registered object, which is consistent with the object name called in the window. |
| methodList | Array&lt;string&gt; | Yes | The method of the application side JavaScript object participating in the registration. |
| asyncMethodList | Array&lt;string&gt; | No | The async method of the application side JavaScript object participating in the registration. |
| permission | string | No | permission configuration defining web page URLs that can access JavaScriptProxy methods. The configuration can be defined at two levels, object level and method level. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class TestObj {
  constructor() {
  }

  test(testStr: string): string {
    console.info('Web Component str' + testStr);
    return testStr;
  }

  toString(): void {
    console.info('Web Component toString');
  }

  testNumber(testNum: number): number {
    console.info('Web Component number' + testNum);
    return testNum;
  }

  asyncTestBool(testBol: boolean): void {
    console.info('Web Component boolean' + testBol);
  }
}

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

class AsyncObj {
  constructor() {
  }

  asyncTest(): void {
    console.info('Async test');
  }

  asyncString(testStr: string): void {
    console.info('Web async string' + testStr);
  }
}

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  @State testObjtest: TestObj = new TestObj();
  @State webTestObj: WebObj = new WebObj();
  @State asyncTestObj: AsyncObj = new AsyncObj();

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
      Button('Register JavaScript To Window')
        .onClick(() => {
          try {
            // Register both synchronous and asynchronous functions.
            this.controller.registerJavaScriptProxy(this.testObjtest, "objName", ["test", "toString", "testNumber"], ["asyncTestBool"]);
            // Register only the synchronous function.
            this.controller.registerJavaScriptProxy(this.webTestObj, "objTestName", ["webTest", "webString"]);
            // Register only the asynchronous function.
            this.controller.registerJavaScriptProxy(this.asyncTestObj, "objAsyncName", [], ["asyncTest", "asyncString"]);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('deleteJavaScriptRegister')
        .onClick(() => {
          try {
            this.controller.deleteJavaScriptRegister("objName");
            this.controller.deleteJavaScriptRegister("objTestName");
            this.controller.deleteJavaScriptRegister("objAsyncName");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
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
      <p id="asyncDemo"></p>
      <script type="text/javascript">
        function htmlTest() {
          // This function call expects to return "ArkUI Web Component"
          let str=objName.test("webtest data");
          objName.testNumber(1);
          objName.asyncTestBool(true);
          document.getElementById("demo").innerHTML=str;
          console.info('objName.test result:'+ str)

          // This function call expects to return "Web test"
          let webStr = objTestName.webTest();
          document.getElementById("webDemo").innerHTML=webStr;
          console.info('objTestName.webTest result:'+ webStr)

          objAsyncName.asyncTest();
          objAsyncName.asyncString("async test data");
        }
      </script>
    </body>
</html>
```

## removeAllCache

```TypeScript
static removeAllCache(clearRom: boolean): void
```

Remove resource cache in application. So this method will remove all cache for all web components in the same application.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static removeAllCache(clearRom: boolean): void--><!--Device-WebviewController-static removeAllCache(clearRom: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clearRom | boolean | Yes | Remove cache in both rom and ram if true. Otherwise only clear cache in ram. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |

**Examples**

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
      Button('removeAllCache')
        .onClick(() => {
          try {
            webview.WebviewController.removeAllCache(false);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## removeCache

```TypeScript
removeCache(clearRom: boolean): void
```

Clears the cache in the application. This API will clear the cache for all webviews in the same application.<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> You can view the Webview cache in the data/storage/el2/base/cache/web/Cache directory. </p>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-removeCache(clearRom: boolean): void--><!--Device-WebviewController-removeCache(clearRom: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clearRom | boolean | Yes | Whether to clear the cache in the ROM and RAM at the same time. {@code true} means to clear the cache in the ROM and RAM at the same time; {@code false} means to only clear the cache in the RAM. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('removeCache')
        .onClick(() => {
          try {
            this.controller.removeCache(false);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## removeIntelligentTrackingPreventionBypassingList

```TypeScript
static removeIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void
```

Remove bypassing hosts for Intelligent Tracking Prevention.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static removeIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void--><!--Device-WebviewController-static removeIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hostList | Array&lt;string&gt; | Yes | Hosts needs to remove from bypass list. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

**Examples**

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
      Button('removeIntelligentTrackingPreventionBypassingList')
        .onClick(() => {
          try {
            let hostList = ["www.test1.com", "www.test2.com"];
            webview.WebviewController.removeIntelligentTrackingPreventionBypassingList(hostList);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## requestFocus

```TypeScript
requestFocus(): void
```

Gets the request focus.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-requestFocus(): void--><!--Device-WebviewController-requestFocus(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('requestFocus')
        .onClick(() => {
          try {
            this.controller.requestFocus();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        });
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## restoreWebState

```TypeScript
restoreWebState(state: Uint8Array): void
```

Restoring the web access stack, that is, the history of access.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-restoreWebState(state: Uint8Array): void--><!--Device-WebviewController-restoreWebState(state: Uint8Array): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | Uint8Array | Yes | Web access stack after serialization. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

To perform operations on files, you must first import the fs module. For details, see File Management.

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('RestoreWebState')
        .onClick(() => {
          try {
            let path: string | undefined = AppStorage.get("cacheDir");
            if (path) {
              path += '/WebState';
              // Synchronously open a file.
              let file = fileIo.openSync(path, fileIo.OpenMode.READ_WRITE);
              let stat = fileIo.statSync(path);
              let size = stat.size;
              let buf = new ArrayBuffer(size);
              fileIo.read(file.fd, buf, (err, readLen) => {
                if (err) {
                  console.error("console error with error message: " + err.message + ", error code: " + err.code);
                } else {
                  console.info("read file data succeed");
                  this.controller.restoreWebState(new Uint8Array(buf.slice(0, readLen)));
                  fileIo.closeSync(file);
                }
              });
            }
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

Obtain the path of the application cache file.

```TypeScript
// xxx.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    // Data synchronization between the UIAbility component and the page can be implemented by binding cacheDir to the AppStorage object.
    AppStorage.setOrCreate("cacheDir", this.context.cacheDir);
  }
}
```

## resumeAllMedia

```TypeScript
resumeAllMedia(): void
```

Resumes the playback of the audio and video that are paused by the pauseAllMedia interface.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-resumeAllMedia(): void--><!--Device-WebviewController-resumeAllMedia(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('resumeAllMedia')
        .onClick(() => {
          try {
            this.controller.resumeAllMedia();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## resumeAllTimers

```TypeScript
static resumeAllTimers(): void
```

Resume all timers suspended from the pauseAllTimers() interface.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static resumeAllTimers(): void--><!--Device-WebviewController-static resumeAllTimers(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Row() {
        Button('ResumeAllTimers')
          .onClick(() => {
            webview.WebviewController.resumeAllTimers();
          })
        Button('PauseAllTimers')
          .onClick(() => {
            webview.WebviewController.pauseAllTimers();
          })
      }
      Web({ src: $rawfile("index.html"), controller: this.controller })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!DOCTYPE html>
<html>
    <body>
        <button style="width:300px;height:150px;font-size:50px" onclick="startTimer()">start</button>
        <button style="width:300px;height:150px;font-size:50px" onclick="resetTimer()">reset</button>
        <input style="width:300px;height:150px;font-size:50px" value="0" id="show_num">
    </body>
</html>
<script>
    var timer = null;
    var num = 0;

    function startTimer() {
        timer = setInterval(function() {
            document.getElementById("show_num").value = ++num;
        }, 1000);
    }

    function resetTimer() {
        clearInterval(timer);
        document.getElementById("show_num").value = 0;
        num = 0;
    }
</script>
```

## resumeMicrophone

```TypeScript
resumeMicrophone(): void
```

Resumes microphone capture on the current web page. Before using the microphone , add the **ohos.permission.MICROPHONE** permission to **module.json5**. For details about how to add the permission, see [Declaring Permissions in the Configuration File](../../../security/AccessToken/declare-permissions.md).

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-resumeMicrophone(): void--><!--Device-WebviewController-resumeMicrophone(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, PermissionRequestResult, common } from '@kit.AbilityKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  aboutToAppear(): void {
    let context: Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
    atManager.requestPermissionsFromUser(context, ['ohos.permission.MICROPHONE'], (err: BusinessError, data: PermissionRequestResult) => {
      console.info('data:' + JSON.stringify(data));
      console.info('data permissions:' + data.permissions);
      console.info('data authResults:' + data.authResults);
    })
  }

  build() {
    Column() {
      Button("resumeMicrophone").onClick(() => {
        try {
          this.controller.resumeMicrophone();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Button("pauseMicrophone").onClick(() => {
        try {
          this.controller.pauseMicrophone();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Button("stopMicrophone").onClick(() => {
        try {
          this.controller.stopMicrophone();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onPermissionRequest((event) => {
          if (event) {
            this.uiContext.showAlertDialog({
              title: 'title',
              message: 'text',
              primaryButton: {
                value: 'deny',
                action: () => {
                  event.request.deny();
                }
              },
              secondaryButton: {
                value: 'onConfirm',
                action: () => {
                  event.request.grant(event.request.getAccessibleResource());
                }
              },
              cancel: () => {
                event.request.deny();
              }
            })
          }
        })
        .onMicrophoneCaptureStateChange((event: MicrophoneCaptureStateChangeInfo) => {
          console.info("MicrophoneCapture from ", event.originalState, " to ", event.newState);
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
   <meta charset="UTF-8">
 </head>
 <body>
   <video id="video" width="400px" height="400px" autoplay="autoplay">
   </video>
   <input type="button" title="HTML5 Microphone" value="Enable Microphone" onclick="getMedia()" />
   <script>
     function getMedia() {
       let constraints = {
         video: {
           width: 500,
           height: 500
         },
         audio: true
       }
       let video = document.getElementById("video");
       let promise = navigator.mediaDevices.getUserMedia(constraints);
       promise.then(function(MediaStream) {
         video.srcObject = MediaStream;
         video.play();
       })
     }
   </script>
 </body>
</html>
```

## runJavaScript

```TypeScript
runJavaScript(script: string): Promise<string>
```

Asynchronously execute JavaScript in the context of the currently displayed page. The result of the script execution will be returned through a via Promise. This method must be used on the UI thread, and the callback will also be invoked on the UI thread. <p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> The state of JavaScript is no longer persisted across navigations like loadUrl. For example, global variables and functions defined before calling loadUrl will not exist in the loaded page.<br> It is recommended that applications use registerJavaScriptProxy to ensure that the JavaScript state can be persisted across page navigations.<br> If you cannot obtain the return value by executing the asynchronous method, you need to determine whether to use synchronous or asynchronous mode based on the specific situation. <p>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-runJavaScript(script: string): Promise<string>--><!--Device-WebviewController-runJavaScript(script: string): Promise<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| script | string | Yes | JavaScript Script. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | A promise is solved after the JavaScript script is executed. This parameter will be the result of JavaScript script execution. If the JavaScript script fails to execute or has no return value, null will be returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |
| [17100003](../../apis-arkweb/errorcode-webview.md#17100003-incorrect-resource-path) | Calling a JS method that returns an empty ArrayBuffer via runJavaScript. |

**Examples**

```TypeScript
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State webResult: string = '';

  build() {
    Column() {
      Text(this.webResult).fontSize(20)
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
        .onPageEnd(e => {
          try {
            this.controller.runJavaScript(
              'test()',
              (error, result) => {
                if (error) {
                  console.error(`run JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                  return;
                }
                if (result) {
                  this.webResult = result;
                  console.info(`The test() return value is: ${result}`);
                }
              });
            if (e) {
              console.info('url: ', e.url);
            }
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
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
    Hello world!
    <script type="text/javascript">
      function test() {
        console.info('Ark WebComponent')
        return "This value is from index.html"
      }
    </script>
  </body>
</html>
```

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
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
        .onPageEnd(e => {
          try {
            this.controller.runJavaScript('test()')
              .then((result) => {
                console.info('result: ' + result);
              })
              .catch((error: BusinessError) => {
                console.error("error: " + error);
              })
            if (e) {
              console.info('url: ', e.url);
            }
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
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
    Hello world!
    <script type="text/javascript">
      function test() {
        console.info('Ark WebComponent')
        return "This value is from index.html"
      }
    </script>
  </body>
</html>
```

## runJavaScript

```TypeScript
runJavaScript(script: string, callback: AsyncCallback<string>): void
```

Asynchronously execute JavaScript in the context of the currently displayed page. The result of the script execution will be returned through an asynchronous callback. This method must be used on the UI thread, and the callback will also be invoked on the UI thread. <p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> The state of JavaScript is no longer persisted across navigations like loadUrl. For example, global variables and functions defined before calling loadUrl will not exist in the loaded page. It is recommended that applications use registerJavaScriptProxy to ensure that the JavaScript state can be persisted across page navigations. <p>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-runJavaScript(script: string, callback: AsyncCallback<string>): void--><!--Device-WebviewController-runJavaScript(script: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| script | string | Yes | JavaScript Script. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | Callbacks execute JavaScript script results. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |
| [17100003](../../apis-arkweb/errorcode-webview.md#17100003-incorrect-resource-path) | Calling a JS method that returns an empty ArrayBuffer via runJavaScript. |

**Examples**

See [runJavaScript](#runjavascript)

## runJavaScriptExt

```TypeScript
runJavaScriptExt(script: string | ArrayBuffer): Promise<JsMessageExt>
```

Execute JavaScript code in the context of the currently displayed page, and return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-runJavaScriptExt(script: string | ArrayBuffer): Promise<JsMessageExt>--><!--Device-WebviewController-runJavaScriptExt(script: string | ArrayBuffer): Promise<JsMessageExt>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| script | string \| ArrayBuffer | Yes | JavaScript Script. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[JsMessageExt](arkts-webview-jsmessageext-c.md)&gt; | A promise is solved after the JavaScript script is executed. This parameter will be the result of JavaScript script execution. If the JavaScript script fails to execute or has no return value, a none type value will be returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State msg1: string = '';
  @State msg2: string = '';

  build() {
    Column() {
      Text(this.msg1).fontSize(20)
      Text(this.msg2).fontSize(20)
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
        .onPageEnd(e => {
          try {
            this.controller.runJavaScriptExt(
              'test()',
              (error, result) => {
                if (error) {
                  console.error(`run JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`)
                  return;
                }
                if (result) {
                  try {
                    if (result.getErrorDescription()) {
                      // If an exception occurs or the return type is not supported, getErrorDescription is not empty.
                      console.info(`runJavaScriptExt getErrorDescription: ${result.getErrorDescription()}`);
                      return;
                    }
                    let type = result.getType();
                    switch (type) {
                      case webview.JsMessageType.STRING: {
                        this.msg1 = "result type:" + typeof (result.getString());
                        this.msg2 = "result getString:" + ((result.getString()));
                        break;
                      }
                      case webview.JsMessageType.NUMBER: {
                        this.msg1 = "result type:" + typeof (result.getNumber());
                        this.msg2 = "result getNumber:" + ((result.getNumber()));
                        break;
                      }
                      case webview.JsMessageType.BOOLEAN: {
                        this.msg1 = "result type:" + typeof (result.getBoolean());
                        this.msg2 = "result getBoolean:" + ((result.getBoolean()));
                        break;
                      }
                      case webview.JsMessageType.ARRAY_BUFFER: {
                        this.msg1 = "result type:" + typeof (result.getArrayBuffer());
                        this.msg2 = "result getArrayBuffer byteLength:" + ((result.getArrayBuffer().byteLength));
                        break;
                      }
                      case webview.JsMessageType.ARRAY: {
                        this.msg1 = "result type:" + typeof (result.getArray());
                        this.msg2 = "result getArray:" + result.getArray();
                        break;
                      }
                      default: {
                        this.msg1 = "default break, type:" + type;
                        break;
                      }
                    }
                  }
                  catch (resError) {
                    console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
                  }
                }
              });
            if (e) {
              console.info('url: ', e.url);
            }
          } catch (resError) {
            console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
          }
        })
    }
  }
}
```

```TypeScript
// Use the ArrayBuffer input parameter to obtain the JavaScript script data from the file.
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State msg1: string = ''
  @State msg2: string = ''

  build() {
    Column() {
      Text(this.msg1).fontSize(20)
      Text(this.msg2).fontSize(20)
      Button('runJavaScriptExt')
        .onClick(() => {
          try {
            let uiContext : UIContext = this.getUIContext();
            let context : Context | undefined = uiContext.getHostContext() as common.UIAbilityContext;
            let filePath = context!.filesDir + 'test.txt';
            // Create a file and open it.
            let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
            // Write data to the file.
            fileIo.writeSync(file.fd, "test()");
            // Read data from the file.
            let arrayBuffer: ArrayBuffer = new ArrayBuffer(6);
            fileIo.readSync(file.fd, arrayBuffer, { offset: 0, length: arrayBuffer.byteLength });
            // Close the file.
            fileIo.closeSync(file);
            this.controller.runJavaScriptExt(
              arrayBuffer,
              (error, result) => {
                if (error) {
                  console.error(`run JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`)
                  return;
                }
                if (result) {
                  try {
                    if (result.getErrorDescription()) {
                      // If an exception occurs or the return type is not supported, getErrorDescription is not empty.
                      console.info(`runJavaScriptExt getErrorDescription: ${result.getErrorDescription()}`);
                      return;
                    }
                    let type = result.getType();
                    switch (type) {
                      case webview.JsMessageType.STRING: {
                        this.msg1 = "result type:" + typeof (result.getString());
                        this.msg2 = "result getString:" + ((result.getString()));
                        break;
                      }
                      case webview.JsMessageType.NUMBER: {
                        this.msg1 = "result type:" + typeof (result.getNumber());
                        this.msg2 = "result getNumber:" + ((result.getNumber()));
                        break;
                      }
                      case webview.JsMessageType.BOOLEAN: {
                        this.msg1 = "result type:" + typeof (result.getBoolean());
                        this.msg2 = "result getBoolean:" + ((result.getBoolean()));
                        break;
                      }
                      case webview.JsMessageType.ARRAY_BUFFER: {
                        this.msg1 = "result type:" + typeof (result.getArrayBuffer());
                        this.msg2 = "result getArrayBuffer byteLength:" + ((result.getArrayBuffer().byteLength));
                        break;
                      }
                      case webview.JsMessageType.ARRAY: {
                        this.msg1 = "result type:" + typeof (result.getArray());
                        this.msg2 = "result getArray:" + result.getArray();
                        break;
                      }
                      default: {
                        this.msg1 = "default break, type:" + type;
                        break;
                      }
                    }
                  }
                  catch (resError) {
                    console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
                  }
                }
              });
          } catch (resError) {
            console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html lang="en-gb">
<body>
<h1>run JavaScript Ext demo</h1>
</body>
<script type="text/javascript">
function test() {
  return "hello, world";
}
</script>
</html>
```

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State webResult: string = '';
  @State msg1: string = '';
  @State msg2: string = '';

  build() {
    Column() {
      Text(this.webResult).fontSize(20)
      Text(this.msg1).fontSize(20)
      Text(this.msg2).fontSize(20)
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
        .onPageEnd(() => {
          this.controller.runJavaScriptExt('test()')
            .then((result) => {
              try {
                if (result.getErrorDescription()) {
                  // If an exception occurs or the return type is not supported, getErrorDescription is not empty.
                  console.info(`runJavaScriptExt getErrorDescription: ${result.getErrorDescription()}`);
                  return;
                }
                let type = result.getType();
                switch (type) {
                  case webview.JsMessageType.STRING: {
                    this.msg1 = "result type:" + typeof (result.getString());
                    this.msg2 = "result getString:" + ((result.getString()));
                    break;
                  }
                  case webview.JsMessageType.NUMBER: {
                    this.msg1 = "result type:" + typeof (result.getNumber());
                    this.msg2 = "result getNumber:" + ((result.getNumber()));
                    break;
                  }
                  case webview.JsMessageType.BOOLEAN: {
                    this.msg1 = "result type:" + typeof (result.getBoolean());
                    this.msg2 = "result getBoolean:" + ((result.getBoolean()));
                    break;
                  }
                  case webview.JsMessageType.ARRAY_BUFFER: {
                    this.msg1 = "result type:" + typeof (result.getArrayBuffer());
                    this.msg2 = "result getArrayBuffer byteLength:" + ((result.getArrayBuffer().byteLength));
                    break;
                  }
                  case webview.JsMessageType.ARRAY: {
                    this.msg1 = "result type:" + typeof (result.getArray());
                    this.msg2 = "result getArray:" + result.getArray();
                    break;
                  }
                  default: {
                    this.msg1 = "default break, type:" + type;
                    break;
                  }
                }
              }
              catch (resError) {
                console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
              }
            }).catch((error: BusinessError) => {
            console.error("error: " + error);
          })
        })
    }
  }
}
```

```TypeScript
// Use the ArrayBuffer input parameter to obtain the JavaScript script data from the file.
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State msg1: string = '';
  @State msg2: string = '';

  build() {
    Column() {
      Text(this.msg1).fontSize(20)
      Text(this.msg2).fontSize(20)
      Button('runJavaScriptExt')
        .onClick(() => {
          try {
            let uiContext : UIContext = this.getUIContext();
            let context : Context | undefined = uiContext.getHostContext() as common.UIAbilityContext;
            let filePath = context!.filesDir + 'test.txt';
            // Create a file and open it.
            let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
            // Write data to the file.
            fileIo.writeSync(file.fd, "test()");
            // Read data from the file.
            let arrayBuffer: ArrayBuffer = new ArrayBuffer(6);
            fileIo.readSync(file.fd, arrayBuffer, { offset: 0, length: arrayBuffer.byteLength });
            // Close the file.
            fileIo.closeSync(file);
            this.controller.runJavaScriptExt(arrayBuffer)
              .then((result) => {
                try {
                  if (result.getErrorDescription()) {
                    // If an exception occurs or the return type is not supported, getErrorDescription is not empty.
                    console.info(`runJavaScriptExt getErrorDescription: ${result.getErrorDescription()}`);
                    return;
                  }
                  let type = result.getType();
                  switch (type) {
                    case webview.JsMessageType.STRING: {
                      this.msg1 = "result type:" + typeof (result.getString());
                      this.msg2 = "result getString:" + ((result.getString()));
                      break;
                    }
                    case webview.JsMessageType.NUMBER: {
                      this.msg1 = "result type:" + typeof (result.getNumber());
                      this.msg2 = "result getNumber:" + ((result.getNumber()));
                      break;
                    }
                    case webview.JsMessageType.BOOLEAN: {
                      this.msg1 = "result type:" + typeof (result.getBoolean());
                      this.msg2 = "result getBoolean:" + ((result.getBoolean()));
                      break;
                    }
                    case webview.JsMessageType.ARRAY_BUFFER: {
                      this.msg1 = "result type:" + typeof (result.getArrayBuffer());
                      this.msg2 = "result getArrayBuffer byteLength:" + ((result.getArrayBuffer().byteLength));
                      break;
                    }
                    case webview.JsMessageType.ARRAY: {
                      this.msg1 = "result type:" + typeof (result.getArray());
                      this.msg2 = "result getArray:" + result.getArray();
                      break;
                    }
                    default: {
                      this.msg1 = "default break, type:" + type;
                      break;
                    }
                  }
                }
                catch (resError) {
                  console.error(`ErrorCode: ${(resError as BusinessError).code},  Message: ${(resError as BusinessError).message}`);
                }
              })
              .catch((error: BusinessError) => {
                console.error("error: " + error);
              })
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html lang="en-gb">
<body>
<h1>run JavaScript Ext demo</h1>
</body>
<script type="text/javascript">
function test() {
  return "hello, world";
}
</script>
</html>
```

## runJavaScriptExt

```TypeScript
runJavaScriptExt(script: string | ArrayBuffer, callback: AsyncCallback<JsMessageExt>): void
```

Execute JavaScript code in the context of the currently displayed page, and return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-runJavaScriptExt(script: string | ArrayBuffer, callback: AsyncCallback<JsMessageExt>): void--><!--Device-WebviewController-runJavaScriptExt(script: string | ArrayBuffer, callback: AsyncCallback<JsMessageExt>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| script | string \| ArrayBuffer | Yes | JavaScript Script. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[JsMessageExt](arkts-webview-jsmessageext-c.md)&gt; | Yes | Callbacks execute JavaScript script results. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

See [runJavaScriptExt](#runjavascriptext)

## scrollBy

```TypeScript
scrollBy(deltaX: double, deltaY: double, duration?: int): void
```

Scroll by the delta position within specified time.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-scrollBy(deltaX: double, deltaY: double, duration?: int): void--><!--Device-WebviewController-scrollBy(deltaX: double, deltaY: double, duration?: int): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deltaX | double | Yes | the delta x of the position <br>Unit: vp. |
| deltaY | double | Yes | the delta y of the position <br>Unit: vp. |
| duration | int | No | the scroll animation duration. <br>Unit: millisecond, The value range is all integers, If the value is not passed, or is negative or 0, there is no animation. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('scrollBy')
        .onClick(() => {
          try {
            this.controller.scrollBy(50, 50, 500);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('stopScroll')
        .onClick(() => {
          try {
            this.controller.scrollBy(0, 0, 1); // To stop the animation generated by the current scroll, you can generate another 1 ms animation to interrupt the animation.
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Demo</title>
    <style>
        body {
            width:2000px;
            height:2000px;
            padding-right:170px;
            padding-left:170px;
            border:5px solid blueviolet;
        }
    </style>
</head>
<body>
Scroll Test
</body>
</html>
```

## scrollByWithResult

```TypeScript
scrollByWithResult(deltaX: double, deltaY: double): boolean
```

Scrolls by the specified delta position and returns a result indicating whether the scrolling operation was successful or not.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-scrollByWithResult(deltaX: double, deltaY: double): boolean--><!--Device-WebviewController-scrollByWithResult(deltaX: double, deltaY: double): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deltaX | double | Yes | the delta x of the position. The unit is vp |
| deltaY | double | Yes | the delta y of the position. The unit is vp |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the scroll operation is successful, otherwise false. Return value scenario: when the Web page is in the touch state, return false, otherwise return true. In the same layer rendering scene, when the same layer rendering area of ??the Web is in the touching state, the return value is true. In a nested scrolling scenario, calling scrollByWithResult will not trigger nested scrolling of the parent component. This interface does not guarantee sliding frame rate performance. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('scrollByWithResult')
        .onClick(() => {
          try {
          let result = this.controller.scrollByWithResult(50, 50);
          console.info("original result: " + result);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Demo</title>
    <style>
        body {
            width:2000px;
            height:2000px;
            padding-right:170px;
            padding-left:170px;
            border:5px solid blueviolet;
        }
    </style>
</head>
<body>
Scroll Test
</body>
</html>
```

## scrollTo

```TypeScript
scrollTo(x: double, y: double, duration?: int): void
```

Scroll to the position within specified time.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-scrollTo(x: double, y: double, duration?: int): void--><!--Device-WebviewController-scrollTo(x: double, y: double, duration?: int): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | the x of the position <br>Unit: vp. |
| y | double | Yes | the y of the position <br>Unit: vp. |
| duration | int | No | the scroll animation duration. <br>Unit: millisecond, The value range is all integers, If the value is not passed, or is negative or 0, there is no animation. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('scrollTo')
        .onClick(() => {
          try {
            this.controller.scrollTo(50, 50, 500);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
        Button('stopScroll')
        .onClick(() => {
          try {
            this.controller.scrollBy(0, 0, 1); // To stop the animation generated by the current scroll, you can generate another 1 ms animation to interrupt the animation.
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Demo</title>
    <style>
        body {
            width:2000px;
            height:2000px;
            padding-right:170px;
            padding-left:170px;
            border:5px solid blueviolet;
        }
    </style>
</head>
<body>
Scroll Test
</body>
</html>
```

## searchAllAsync

```TypeScript
searchAllAsync(searchString: string): void
```

Search all instances of 'searchString' on the page and highlights them, result will be notify through callback onSearchResultReceive.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-searchAllAsync(searchString: string): void--><!--Device-WebviewController-searchAllAsync(searchString: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchString | string | Yes | String to be search. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State searchString: string = "Hello World";

  build() {
    Column() {
      Button('searchString')
        .onClick(() => {
          try {
            this.controller.searchAllAsync(this.searchString);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onSearchResultReceive(ret => {
          if (ret) {
            console.info("on search result receive:" + "[cur]" + ret.activeMatchOrdinal +
              "[total]" + ret.numberOfMatches + "[isDone]" + ret.isDoneCounting);
          }
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
  <body>
    <p>Hello World Highlight Hello World</p>
  </body>
</html>
```

## searchNext

```TypeScript
searchNext(forward: boolean): void
```

Highlights and scrolls to the next match search.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-searchNext(forward: boolean): void--><!--Device-WebviewController-searchNext(forward: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| forward | boolean | Yes | Step of search is back or forward. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('searchNext')
        .onClick(() => {
          try {
            this.controller.searchNext(true);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

## serializeWebState

```TypeScript
serializeWebState(): Uint8Array
```

Serialize the access stack of the web, that is, the history of access.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-serializeWebState(): Uint8Array--><!--Device-WebviewController-serializeWebState(): Uint8Array-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | Web access stack after serialization. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

To perform operations on files, you must first import the fs module. For details, see File Management.

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('serializeWebState')
        .onClick(() => {
          try {
            let state = this.controller.serializeWebState();
            let path:string | undefined = AppStorage.get("cacheDir");
            if (path) {
              path += '/WebState';
              // Synchronously open a file.
              let file = fileIo.openSync(path, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
              fileIo.writeSync(file.fd, state.buffer);
              fileIo.closeSync(file.fd);
            }
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

Obtain the path of the application cache file.

```TypeScript
// xxx.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        // Data synchronization between the UIAbility component and the page can be implemented by binding cacheDir to the AppStorage object.
        AppStorage.setOrCreate("cacheDir", this.context.cacheDir);
    }
}
```

## setActiveWebEngineVersion

```TypeScript
static setActiveWebEngineVersion(engineVersion: ArkWebEngineVersion): void
```

Sets the ArkWeb kernel version. If the system does not support the specified version, the setting is invalid. This API is a global static API and must be called before **initializeWebEngine** is called. If any **Web** component has been loaded, the setting of this API is invalid.

> **NOTE：**&gt;
> - **setActiveWebEngineVersion** cannot be called in an asynchronous thread.

> - **setActiveWebEngineVersion** takes effect globally and needs to be called only once in an application
> lifecycle.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static setActiveWebEngineVersion(engineVersion: ArkWebEngineVersion): void--><!--Device-WebviewController-static setActiveWebEngineVersion(engineVersion: ArkWebEngineVersion): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| engineVersion | [ArkWebEngineVersion](arkts-webview-arkwebengineversion-e.md) | Yes | ArkWeb kernel version. |

**Examples**

This example shows how to set the ArkWeb kernel version in the EntryAbility creation phase.

```TypeScript
// xxx.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate")
    webview.WebviewController.setActiveWebEngineVersion(webview.ArkWebEngineVersion.M114)
    if (webview.WebviewController.getActiveWebEngineVersion() == webview.ArkWebEngineVersion.M114) {
      console.info("Active Web Engine Version set to M114")
    }
    console.info("EntryAbility onCreate done")
  }
}
```

## setAppCustomUserAgent

```TypeScript
static setAppCustomUserAgent(userAgent: string) : void
```

Set the default User-Agent for the application.<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> Unlike setCustomUserAgent, which only takes effect in the current web context, the priority for pages loaded in the web is as follows:
1. The User-Agent set by setCustomUserAgent is used first.
2. If not set, it will check whether a specific User-Agent has been
assigned to the current page via setUserAgentForHosts.
3. If no specific User-Agent is assigned, the application will fall back
to using the User-Agent set by setAppCustomUserAgent.
4. If the app's default User-Agent is also not specified, the web's default
User-Agent will be used as the final fallback. </p>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static setAppCustomUserAgent(userAgent: string) : void--><!--Device-WebviewController-static setAppCustomUserAgent(userAgent: string) : void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userAgent | string | Yes | The User-Agent string. @static |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    try {
      webview.WebviewController.initializeWebEngine();
      let defaultUserAgent = webview.WebviewController.getDefaultUserAgent();
      let appUA = defaultUserAgent + " appUA";
      webview.WebviewController.setAppCustomUserAgent(appUA);
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## setAudioMuted

```TypeScript
setAudioMuted(mute: boolean): void
```

Mutes this web page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-setAudioMuted(mute: boolean): void--><!--Device-WebviewController-setAudioMuted(mute: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mute | boolean | Yes | Whether to mute the web page.<br>The value **true** means to mute the web page, and **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State muted: boolean = false;

  build() {
    Column() {
      Button("Toggle Mute")
        .onClick(event => {
          if (event) {
            this.muted = !this.muted;
            this.controller.setAudioMuted(this.muted);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## setAutoPreconnect

```TypeScript
static setAutoPreconnect(enabled: boolean): void
```

Configure whether to enable automatic pre-connection to high-frequency URLs accessed during the application's previous lifecycle after web initialization.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static setAutoPreconnect(enabled: boolean): void--><!--Device-WebviewController-static setAutoPreconnect(enabled: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Enable if true, disable if false. @static |

**Examples**

```TypeScript
// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        webview.WebviewController.setAutoPreconnect(false);
        webview.WebviewController.initializeWebEngine();
        AppStorage.setOrCreate("abilityWant", want);
    }
}
```

## setBackForwardCacheOptions

```TypeScript
setBackForwardCacheOptions(options?: BackForwardCacheOptions): void
```

Configure the BackForwardCache.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-setBackForwardCacheOptions(options?: BackForwardCacheOptions): void--><!--Device-WebviewController-setBackForwardCacheOptions(options?: BackForwardCacheOptions): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [BackForwardCacheOptions](arkts-webview-backforwardcacheoptions-c.md) | No | The configuration of BackForwardCache. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
// xxx.ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Row() {
        Button("Add options").onClick((event: ClickEvent) => {
          let options = new webview.BackForwardCacheOptions();
          options.size = 3;
          options.timeToLive = 10;
          this.controller.setBackForwardCacheOptions(options);
        })
        Button("Backward").onClick((event: ClickEvent) => {
          this.controller.backward();
        })
        Button("Forward").onClick((event: ClickEvent) => {
          this.controller.forward();
        })
      }
      Web({ src: "https://www.example.com", controller: this.controller })
    }
    .height('100%')
    .width('100%')
  }
}
```

## setBlanklessLoadingCacheCapacity

```TypeScript
static setBlanklessLoadingCacheCapacity(capacity: int) : int
```

Sets the cache capacity of the blankless loading solution and returns the value that takes effect. If this API is not called, the default capacity 30 MB is used. The maximum capacity cannot exceed 100 MB.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static setBlanklessLoadingCacheCapacity(capacity: int) : int--><!--Device-WebviewController-static setBlanklessLoadingCacheCapacity(capacity: int) : int-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| capacity | int | Yes | Cache capacity, in MB. The maximum value is 100 MB. The default value is 30 MB. The value ranges from 0 to 100. If this parameter is set to 0, no cache capacity is available and the functionality is disabled globally. When the value is set to a number smaller than 0, the value 0 takes effect. When the value is set to a number greater than 100, the value 100 takes effect. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The effective value that ranges from 0 MB to 100 MB. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |  |

**Examples**

```TypeScript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    // Set the cache capacity to 10 MB.
    try {
      webview.WebviewController.setBlanklessLoadingCacheCapacity(10);
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }
    AppStorage.setOrCreate("abilityWant", want);
    console.info("EntryAbility onCreate done");
  }
}
```

## setBlanklessLoadingWithKey

```TypeScript
setBlanklessLoadingWithKey(key: string, is_start: boolean) : WebBlanklessErrorCode
```

Sets whether to enable blankless page loading. This API must be used in pair with the getBlanklessInfoWithKey API.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-setBlanklessLoadingWithKey(key: string, is_start: boolean) : WebBlanklessErrorCode--><!--Device-WebviewController-setBlanklessLoadingWithKey(key: string, is_start: boolean) : WebBlanklessErrorCode-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key value that uniquely identifies the current page. It must be the same as the key value of the getBlanklessInfoWithKey API. Default value: N/A. The value cannot be empty or exceed 2048 characters. When an invalid value is set, the error code WebBlanklessErrorCode is returned, and the API does not take effect. |
| is_start | boolean | Yes | Whether to enable frame interpolation. The value true indicates to enable frame interpolation, and the value false indicates the opposite. The default value is false. The value can be true or false. Action for setting an invalid value: N/A. |

**Return value:**

| Type | Description |
| --- | --- |
| [WebBlanklessErrorCode](arkts-webview-webblanklesserrorcode-e.md) | WebBlanklessErrorCode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |  |

**Examples**

```TypeScript
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Web({ src: 'https://www.example.com', controller: this.controller })
       .javaScriptAccess(true)
       .onLoadIntercept((event) => {
            // Enable frame interpolation only when the similarity exceeds 50% and the loading duration is less than 1000 ms.
            try {
              let info = this.controller.getBlanklessInfoWithKey('https://www.example.com/page1');
              if (info.errCode == webview.WebBlanklessErrorCode.SUCCESS) {
                if (info.similarity >= 0.5 && info.loadingTime < 1000) {
                  this.controller.setBlanklessLoadingWithKey('http://www.example.com/page1', true);
                } else {
                  this.controller.setBlanklessLoadingWithKey('http://www.example.com/page1', false);
                }
              } else {
                console.info('getBlankless info err');
              }
            } catch (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
            return false;
        })
    }
  }
}
```

## setBlanklessLoadingWithParams

```TypeScript
setBlanklessLoadingWithParams(key: string,
            param: BlanklessLoadingParam) : WebBlanklessErrorCode
```

Triggers frame interpolation and sets frame interpolation parameters. This API must be used in pair with the getBlanklessInfoWithKey API.Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebviewController-setBlanklessLoadingWithParams(key: string,            param: BlanklessLoadingParam) : WebBlanklessErrorCode--><!--Device-WebviewController-setBlanklessLoadingWithParams(key: string,            param: BlanklessLoadingParam) : WebBlanklessErrorCode-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Key value that uniquely identifies the current page. The key value must be the same as that of getBlanklessInfoWithKey. <br>Value range: (0, 2048] <br>Value range: (0, 2048] <br>which must be the same as the key value in getBlanklessInfoWithKey |
| param | [BlanklessLoadingParam](arkts-webview-blanklessloadingparam-i.md) | Yes | The parameter of blankless. For details see {@Link BlanklessLoadingParam}. <br>na |

**Return value:**

| Type | Description |
| --- | --- |
| [WebBlanklessErrorCode](arkts-webview-webblanklesserrorcode-e.md) | WebBlanklessErrorCode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

**Examples**

```TypeScript
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Web({ src: 'https://www.example.com', controller: this.controller })
       .javaScriptAccess(true)
       .onLoadIntercept((event) => {
            try {
              let info = this.controller.getBlanklessInfoWithKey('https://www.example.com/page1');
              if (info.errCode == webview.WebBlanklessErrorCode.SUCCESS) {
                let data = new Date(2026, 5, 10, 0, 0, 0, 0);
                let param: webview.BlanklessLoadingParam = {
                  enable: info.similarity > 0.4 && info.similarity < 2000,
                  duration: info.loadingTime,
                  expirationTime: data.getTime(),
                  callback: (info: webview.BlanklessFrameInterpolationInfo)=>{
                    // Data monitoring.
                  },
                };
                this.controller.setBlanklessLoadingWithParams('http://www.example.com/page1', param);
              } else {
                console.info('getBlankless info err');
              }
            } catch (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code},
                Message: ${(error as BusinessError).message}`);
            }
            return false;
        })
    }
  }
}
```

## setConnectionTimeout

```TypeScript
static setConnectionTimeout(timeout: int): void
```

Set web engine socket connection timeout. Unit: seconds.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static setConnectionTimeout(timeout: int): void--><!--Device-WebviewController-static setConnectionTimeout(timeout: int): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeout | int | Yes | Socket connection timeout. The value should be an integer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3. Parameter verification failed. |

**Examples**

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
      Button('setConnectionTimeout')
        .onClick(() => {
          try {
            webview.WebviewController.setConnectionTimeout(5);
            console.info("setConnectionTimeout: 5s");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .onErrorReceive((event) => {
          if (event) {
            console.info('getErrorInfo:' + event.error.getErrorInfo());
            console.info('getErrorCode:' + event.error.getErrorCode());
          }
        })
    }
  }
}
```

## setCustomUserAgent

```TypeScript
setCustomUserAgent(userAgent: string): void
```

Set custom user agent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-setCustomUserAgent(userAgent: string): void--><!--Device-WebviewController-setCustomUserAgent(userAgent: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userAgent | string | Yes | User custom agent information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State customUserAgent: string = ' DemoApp';

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
      .onControllerAttached(() => {
        console.info("onControllerAttached");
        try {
          let userAgent = this.controller.getUserAgent() + this.customUserAgent;
          this.controller.setCustomUserAgent(userAgent);
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
    }
  }
}
```

## setDownloadDelegate

```TypeScript
setDownloadDelegate(delegate: WebDownloadDelegate): void
```

Set delegate for download. Used to notify the progress of the download triggered from web.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-setDownloadDelegate(delegate: WebDownloadDelegate): void--><!--Device-WebviewController-setDownloadDelegate(delegate: WebDownloadDelegate): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| delegate | [WebDownloadDelegate](arkts-webview-webdownloaddelegate-c.md) | Yes | Delegate used for download triggered from web. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();

  build() {
    Column() {
      Button('setDownloadDelegate')
        .onClick(() => {
          try {
            this.controller.setDownloadDelegate(this.delegate);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## setErrorPageEnabled

```TypeScript
setErrorPageEnabled(enable: boolean): void
```

Set whether enable the error page. onOverrideErrorPage will be triggered when the page error.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-setErrorPageEnabled(enable: boolean): void--><!--Device-WebviewController-setErrorPageEnabled(enable: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | Whether to enable the default error page feature. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

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
       .onControllerAttached(() => {
            this.controller.setErrorPageEnabled(true);
            if (!this.controller.getErrorPageEnabled()) {
                this.controller.setErrorPageEnabled(true);
            }
        })
    }
  }
}
```

## setErrorPageEnabled

```TypeScript
setErrorPageEnabled(enable: boolean, includeSubframe: boolean): void
```

Set whether to enable error page. onOverrideErrorPage will be triggered when the page error.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebviewController-setErrorPageEnabled(enable: boolean, includeSubframe: boolean): void--><!--Device-WebviewController-setErrorPageEnabled(enable: boolean, includeSubframe: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | Whether enable error page. |
| includeSubframe | boolean | Yes | If true, error page is displayed in iframe when a subframe fails to load. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

See [setErrorPageEnabled](#seterrorpageenabled)

## setHostIP

```TypeScript
static setHostIP(hostName: string, address: string, aliveTime: int): void
```

Set IP address for host name.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static setHostIP(hostName: string, address: string, aliveTime: int): void--><!--Device-WebviewController-static setHostIP(hostName: string, address: string, aliveTime: int): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hostName | string | Yes | Which host name to be resolved. |
| address | string | Yes | Resolved IP address. |
| aliveTime | int | Yes | The validity seconds for resolve cache. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |

**Examples**

For details, see [clearHostIP](#clearhostip).

## setHttpDns

```TypeScript
static setHttpDns(secureDnsMode: SecureDnsMode, secureDnsConfig: string): void
```

Set web engine to use HttpDns server to resolve dns.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static setHttpDns(secureDnsMode: SecureDnsMode, secureDnsConfig: string): void--><!--Device-WebviewController-static setHttpDns(secureDnsMode: SecureDnsMode, secureDnsConfig: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| secureDnsMode | [SecureDnsMode](arkts-webview-securednsmode-e.md) | Yes | using HttpDns. |
| secureDnsConfig | string | Yes | The configuration of the HttpDns server. Must be https protocol and only allow one server to be configured. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3. Parameter verification failed. |

**Examples**

```TypeScript
// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate")
    try {
      webview.WebviewController.setHttpDns(webview.SecureDnsMode.AUTO, "https://example1.test")
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }

    AppStorage.setOrCreate("abilityWant", want);
    console.info("EntryAbility onCreate done")
  }
}
```

## setNetworkAvailable

```TypeScript
setNetworkAvailable(enable: boolean): void
```

Put network state for web. Which is used to set window.navigator.onLine property in JavaScript.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-setNetworkAvailable(enable: boolean): void--><!--Device-WebviewController-setNetworkAvailable(enable: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | Whether enable window.navigator.onLine. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('setNetworkAvailable')
        .onClick(() => {
          try {
            this.controller.setNetworkAvailable(true);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
<body>
<h1>online attribute </h1>
<p id="demo"></p>
<button onclick="func()">click</button>
<script>
    // Check whether the browser is online.
    var online1 = navigator.onLine;
    document.getElementById("demo").innerHTML = "Browser online:" + online1;

    function func(){
      var online2 = navigator.onLine;
      document.getElementById("demo").innerHTML = "Browser online:" + online2;
    }
</script>
</body>
</html>
```

## setPathAllowingUniversalAccess

```TypeScript
setPathAllowingUniversalAccess(pathList: Array<string>): void
```

Sets a path list. When the file protocol accesses resources in the path list, cross-origin access to local files and other online resources is allowed. In addition, when a path list is set, the file protocol can access only the resources in the path list. The behavior of fileAccess will be overwritten by that of this API. The paths in the list must be any of the following:
1. The path of subdirectory of the application file directory.
(The application file directory is obtained using [Context.filesDir](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md#filesdir) in the Ability Kit.) For example:  
* /data/storage/el2/base/files/example * /data/storage/el2/base/haps/entry/files/example
2. The path of application resource directory or its subdirectory.
(The application resource directory is obtained from [Context.resourceDir](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md#resourcedir) in the Ability Kit.) For example:  
* /data/storage/el1/bundle/entry/resources/resfile * /data/storage/el1/bundle/entry/resources/resfile/example
3. Since API version 21, the application cache directory and its subdirectories are also supported.
(The application cache directory is obtained through [Context.cacheDir](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md#cachedir) in Ability Kit). For example:  
* /data/storage/el2/base/cache * /data/storage/el2/base/haps/entry/cache/example * The **cache/web** directory is not allowed. If it is included, an exception with the code **401** will be thrown. If the **cache** directory is set, **cache/web** cannot be accessed.
4. Since API version 21, the temporary application directory and its subdirectories are also supported.
(The temporary application directory is obtained through [Context.tempDir](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md#tempdir) in Ability Kit). For example:  
* /data/storage/el2/base/temp * /data/storage/el2/base/haps/entry/temp/example If a path in the list is not of the preceding paths, error code 401 is reported and the path list fails to be set. When the path list is set to empty, the accessible files for the file protocol are subject to the behavior of the fileAccess.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-setPathAllowingUniversalAccess(pathList: Array<string>): void--><!--Device-WebviewController-setPathAllowingUniversalAccess(pathList: Array<string>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathList | Array&lt;string&gt; | Yes | The path list. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter string is too long. 3. Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Row() {
      Web({ src: "", controller: this.controller })
        .onControllerAttached(() => {
          try {
            // Set the list of paths that can be accessed across domains.
            this.controller.setPathAllowingUniversalAccess([
              this.uiContext.getHostContext()!.resourceDir,
              this.uiContext.getHostContext()!.filesDir + "/example"
            ])
            this.controller.loadUrl("file://" + this.getUIContext().getHostContext()!.resourceDir + "/index.html")
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
        .javaScriptAccess(true)
        .fileAccess(true)
        .domStorageAccess(true)
    }
  }
}
```

Load the HTML file, which is located in the application resource directory resource/resfile/index.html.

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>Demo</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no, viewport-fit=cover">
    <script>
        function getFile() {
            var file = "file:///data/storage/el1/bundle/entry/resources/resfile/js/script.js";
            var xmlHttpReq = new XMLHttpRequest();
            xmlHttpReq.onreadystatechange = function(){
                console.info("readyState:" + xmlHttpReq.readyState);
                console.info("status:" + xmlHttpReq.status);
                if(xmlHttpReq.readyState == 4){
                    if (xmlHttpReq.status == 200) {
                // If the path list is set on the eTS, resources can be obtained.
                        const element = document.getElementById('text');
                        element.textContent = "load " + file + " success";
                    } else {
                // If the path list is not set on the eTS, a CORS error is triggered.
                        const element = document.getElementById('text');
                        element.textContent = "load " + file + " failed";
                    }
                }
            }
            xmlHttpReq.open("GET", file);
            xmlHttpReq.send(null);
        }

    </script>
</head>

<body>
<div class="page">
    <button id="example" onclick="getFile()">stealFile</button>
</div>
<div id="text"></div>
</body>

</html>
```

In the HTML file, use the file protocol to access the local JS file through XMLHttpRequest. The JS file is stored in resource/resfile/js/script.js.

```TypeScript
const body = document.body;
const element = document.createElement('div');
element.textContent = 'success';
body.appendChild(element);
```

## setPrintBackground

```TypeScript
setPrintBackground(enable: boolean): void
```

Set whether print web page background.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-setPrintBackground(enable: boolean): void--><!--Device-WebviewController-setPrintBackground(enable: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | Set whether print web page background |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('setPrintBackground')
        .onClick(() => {
          try {
            this.controller.setPrintBackground(false);
          } catch (error) {
            console.error(`ErrorCode:${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## setRenderProcessMode

```TypeScript
static setRenderProcessMode(mode: RenderProcessMode): void
```

Set render process mode of the ArkWeb.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static setRenderProcessMode(mode: RenderProcessMode): void--><!--Device-WebviewController-static setRenderProcessMode(mode: RenderProcessMode): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [RenderProcessMode](arkts-webview-renderprocessmode-e.md) | Yes | The render process mode for the ArkWeb. Call [getRenderProcessMode](#getrenderprocessmode) to get the ArkWeb rendering subprocess mode of the current device. The enumerated value * *0 * * indicates the single render subprocess mode, and * *1 * * indicates the multi-render subprocess mode. If an invalid number other than the enumerated value of * *RenderProcessMode * * is passed, the multi-render subprocess mode is used by default. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |

**Examples**

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
      Button('setRenderProcessMode')
        .onClick(() => {
          try {
            webview.WebviewController.setRenderProcessMode(webview.RenderProcessMode.MULTIPLE);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## setScrollable

```TypeScript
setScrollable(enable: boolean, type?: ScrollType): void
```

Set whether scroll is allowed; default is true.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-setScrollable(enable: boolean, type?: ScrollType): void--><!--Device-WebviewController-setScrollable(enable: boolean, type?: ScrollType): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | Set whether scrolling is allowed {@code true} means scrolling is allowed. {@code false} means scrolling is disabled. |
| type | [ScrollType](arkts-webview-scrolltype-e.md) | No | Enable scrolling type When the input parameter enable is false, it indicates that scrolling of the ScrollType type is prohibited. When ScrollType is not specified,it indicates that all types of webpage scrolling are prohibited. When the input parameter enable is true, regardless of whether ScrollType is specified, it indicates that all types of webpage scrolling are allowed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('setScrollable')
        .onClick(() => {
          try {
            this.controller.setScrollable(true);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## setScrollbarMode

```TypeScript
static setScrollbarMode(scrollbarMode: ScrollbarMode): void
```

Sets whether to switch web scrollbar mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static setScrollbarMode(scrollbarMode: ScrollbarMode): void--><!--Device-WebviewController-static setScrollbarMode(scrollbarMode: ScrollbarMode): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scrollbarMode | [ScrollbarMode](arkts-webview-scrollbarmode-e.md) | Yes | web scrollbar mode, default OVERLAY_LAYOUT_SCROLLBAR. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  aboutToAppear(): void {
    webview.WebviewController.setScrollbarMode(webview.ScrollbarMode.FORCE_DISPLAY_SCROLLBAR);
  }
  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .height('90%')
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo</title>
    <style>
      body {
        width:2560px;
        height:2560px;
        padding-right:170px;
        padding-left:170px;
        border:5px solid blueviolet;
      }
    </style>
</head>
<body>
Scroll Test
</body>
</html>
```

## setServiceWorkerWebSchemeHandler

```TypeScript
static setServiceWorkerWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void
```

Set web scheme handler for specific scheme. This is used for service worker.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static setServiceWorkerWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void--><!--Device-WebviewController-static setServiceWorkerWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scheme | string | Yes | String value for url scheme. |
| handler | [WebSchemeHandler](arkts-webview-webschemehandler-c.md) | Yes | Web scheme handler. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Incorrect parameter types. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  schemeHandler: webview.WebSchemeHandler = new webview.WebSchemeHandler();

  build() {
    Column() {
      Button('setWebSchemeHandler')
        .onClick(() => {
          try {
            webview.WebviewController.setServiceWorkerWebSchemeHandler('http', this.schemeHandler);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## setSiteIsolationMode

```TypeScript
static setSiteIsolationMode(mode: SiteIsolationMode): void
```

Set the site isolation mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static setSiteIsolationMode(mode: SiteIsolationMode): void--><!--Device-WebviewController-static setSiteIsolationMode(mode: SiteIsolationMode): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [SiteIsolationMode](arkts-webview-siteisolationmode-e.md) | Yes | The site isolation mode of the application, default value depends on different devices type. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. Possible causes: 1. Site Isolation mode is already set by the developer. 2. Site Isolation mode cannot be strict in single-render-process mode. 3. Site Isolation mode cannot be changed while Secure Shield mode is active. @static |

**Examples**

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
      Button('setSiteIsolationMode')
        .onClick(() => {
          try {
            webview.WebviewController.setSiteIsolationMode(webview.SiteIsolationMode.PARTIAL);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## setSocketIdleTimeout

```TypeScript
static setSocketIdleTimeout(timeout: int): void
```

Set web engine socket idle timeout. <p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> Unit: seconds, minimum 30s, maximum 5 minutes. If not set, the default is five minutes. </p>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static setSocketIdleTimeout(timeout: int): void--><!--Device-WebviewController-static setSocketIdleTimeout(timeout: int): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeout | int | Yes | Socket idle timeout. @static |

**Examples**

```TypeScript
// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        webview.WebviewController.setSocketIdleTimeout(200);
        AppStorage.setOrCreate("abilityWant", want);
    }
}
```

## setSoftKeyboardBehaviorMode

```TypeScript
setSoftKeyboardBehaviorMode(mode: WebSoftKeyboardBehaviorMode): void
```

Set the WebSoftKeyboardBehaviorMode to decide whether the keyboard will be shown/hidden automatically in particular situation, for example, when web is inactive or active.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-setSoftKeyboardBehaviorMode(mode: WebSoftKeyboardBehaviorMode): void--><!--Device-WebviewController-setSoftKeyboardBehaviorMode(mode: WebSoftKeyboardBehaviorMode): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [WebSoftKeyboardBehaviorMode](arkts-webview-websoftkeyboardbehaviormode-e.md) | Yes | The WebSoftKeyboardBehaviorMode of this web. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
// index.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('Web InActive').onClick(() => {
        this.controller.setSoftKeyboardBehaviorMode(webview.WebSoftKeyboardBehaviorMode.DISABLE_AUTO_KEYBOARD_ON_ACTIVE);
      })
      Web({ src: 'www.example.com', controller: this.controller })
        .keyboardAvoidMode(WebKeyboardAvoidMode.RETURN_TO_UICONTEXT)
    }
  }
}
```

## setUrlTrustList

```TypeScript
setUrlTrustList(urlTrustList: string, allowOpaqueOrigin: boolean, supportWildcard: boolean): void
```

Sets the URL trust list for the ArkWeb.<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> When the URL trust list is set, only the URLs in the list can be accessed.Example of the urlTrustList:{"UrlPermissionList": [{"scheme": "https","host": "www.example1.com","port": 443,"path": "pathA/pathB"}, {"scheme": "http","host": "*.example2.com","port": 80,"path": "test1/test2/test3"}]} </p>

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

<!--Device-WebviewController-setUrlTrustList(urlTrustList: string, allowOpaqueOrigin: boolean, supportWildcard: boolean): void--><!--Device-WebviewController-setUrlTrustList(urlTrustList: string, allowOpaqueOrigin: boolean, supportWildcard: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| urlTrustList | string | Yes | The URL trust list in JSON format. An empty string means all URLs are allowed. |
| allowOpaqueOrigin | boolean | Yes | If true, loading of opaque origin URLs (e.g., javascript, data) is allowed. If false, it is not allowed. |
| supportWildcard | boolean | Yes | If true, wildcard matching is supported (e.g., *.example.com matches all subdomains). If false, wildcard matching is not supported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Initialization error. The WebviewController must be associated with a Web component. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |  |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  urltrustList: string = "{\"UrlPermissionList\":[{\"scheme\":\"http\", \"host\":\"trust.example.com\", \"port\":80, \"path\":\"test\"}]}"

  build() {
    Column() {
      Button('Setting the trustlist')
        .onClick(() => {
          try {
            // Set a trustlist to allow access only to trust web pages.
            this.controller.setUrlTrustList(this.urltrustList);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Cancel the trustlist.')
        .onClick(() => {
          try {
            // Input an empty string to setUrlTrustList() to disable the trustlist, and all URLs can be accessed.
            this.controller.setUrlTrustList("");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Access the trust web')
        .onClick(() => {
          try {
            // The trustlist is enabled and trust web pages can be accessed.
            this.controller.loadUrl('http://trust.example.com/test');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Access the untrust web')
        .onClick(() => {
          try {
            // The trustlist is enabled that untrust web pages cannot be accessed and an error page is displayed.
            this.controller.loadUrl('http://untrust.example.com/test');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'http://untrust.example.com/test', controller: this.controller }).onControllerAttached(() => {
        try {
          // Set the trustlist using onControllerAttached() to enable the trustlist before the URL starts to be loaded. The untrusted web page cannot be accessed, and an error page is displayed.
          this.controller.setUrlTrustList(this.urltrustList);
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
    }
  }
}
```

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  urltrustList: string = "{\"UrlPermissionList\":[{\"scheme\":\"http\", \"host\":\"trust.example.com\", \"path\":\"test\"}]}"
  urlWildcardList: string = "{\"UrlPermissionList\":[{\"scheme\":\"http\", \"host\":\"*.example.com\", \"path\":\"*\"}]}"

  build() {
    Column() {
      Button('Setting the trustlist')
        .onClick(() => {
          try {
            // Set a trustlist to allow access only to trust web pages.
            this.controller.setUrlTrustList(this.urltrustList);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Setting the wildcardlist')
        .onClick(() => {
          try {
            // Set a wildcard trustlist to allow access to all URLs.
            this.controller.setUrlTrustList(this.urlWildcardList, true, true);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Cancel the trustlist.')
        .onClick(() => {
          try {
            // Input an empty string to setUrlTrustList() to disable the trustlist, and all URLs can be accessed.
            this.controller.setUrlTrustList("");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Access the trust web')
        .onClick(() => {
          try {
            // The trustlist is enabled and trust web pages can be accessed.
            this.controller.loadUrl('http://trust.example.com/test');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Access the untrust web')
        .onClick(() => {
          try {
            // The trustlist is enabled that untrust web pages cannot be accessed and an error page is displayed.
            this.controller.loadUrl('http://untrust.example.com/test');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'http://untrust.example.com/test', controller: this.controller }).onControllerAttached(() => {
        try {
          // Set the trustlist using onControllerAttached() to enable the trustlist before the URL starts to be loaded. The untrusted web page cannot be accessed, and an error page is displayed.
          this.controller.setUrlTrustList(this.urltrustList);
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
    }
  }
}
```

## setUrlTrustList

```TypeScript
setUrlTrustList(urlTrustList: string): void
```

Set the URL trust list for the ArkWeb. When the URL trust list has been set, only the URLs in the list can be accessed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-setUrlTrustList(urlTrustList: string): void--><!--Device-WebviewController-setUrlTrustList(urlTrustList: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| urlTrustList | string | Yes | the URL trust list in JSON format. An empty string means that all URLs are allowed to access. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Parameter string is too long. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

See [setUrlTrustList](#seturltrustlist)

## setUserAgentClientHintsEnabled

```TypeScript
static setUserAgentClientHintsEnabled(enabled: boolean): void
```

Enable the User-Agent Client Hints.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebviewController-static setUserAgentClientHintsEnabled(enabled: boolean): void--><!--Device-WebviewController-static setUserAgentClientHintsEnabled(enabled: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | User-Agent Client Hints will enabled when set true. @static |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State userAgent: string = "";

  build() {
    Column() {
      Button('setUserAgentMetadata').fontSize(20)
        .onClick((e: ClickEvent) => {
          try {
            let arrayVersions: Array<webview.UserAgentBrandVersion> = new Array<webview.UserAgentBrandVersion>;
            let brandVersion:webview.UserAgentBrandVersion = new webview.UserAgentBrandVersion();
            brandVersion.setBrand("brand OpenHarmony");
            brandVersion.setMajorVersion("major version 1.0");
            brandVersion.setFullVersion("blank full version 1.0");
            arrayVersions.push(brandVersion);
            let metadata:webview.UserAgentMetadata = new webview.UserAgentMetadata();
            metadata.setBrandVersionList(arrayVersions);
            metadata.setFormFactors([webview.UserAgentFormFactor.AUTOMOTIVE]);
            metadata.setArchitecture("arch OpenHarmony");
            metadata.setBitness("bitness 64");
            metadata.setFullVersion("full version OpenHarmony");
            metadata.setMobile(true);
            metadata.setModel("model OpenHarmony");
            metadata.setPlatform("platform OpenHarmony");
            metadata.setPlatformVersion("platform version OpenHarmony");
            metadata.setWow64(false);
            this.controller.setUserAgentMetadata(this.userAgent, metadata);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('getUserAgentMetadata').fontSize(20)
        .onClick((e: ClickEvent) => {
          try {
            this.userAgent = this.controller.getUserAgent();
            let metadata = this.controller.getUserAgentMetadata(this.userAgent);
            let versionList = metadata.getBrandVersionList();
            for(let i = 0; i < versionList.length; i++) {
              console.info("Brand:" + versionList[i].getBrand());
              console.info("MajorVersion " + versionList[i].getMajorVersion());
              console.info("FullVersion " + versionList[i].getFullVersion());
            }
            let FormFactors = metadata.getFormFactors();
            for(let j = 0; j < FormFactors.length; j++) {
              console.info("FormFactor:" + FormFactors[j]);
            }
            console.info("Bitness:" + metadata.getBitness());
            console.info("FullVersion:" + metadata.getFullVersion());
            console.info("Mobile:" + metadata.getMobile());
            console.info("Model:" + metadata.getModel());
            console.info("Platform:" + metadata.getPlatform());
            console.info("PlatformVersion:" + metadata.getPlatformVersion());
            console.info("Wow64:" + metadata.getWow64());
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'https://www.example.com', controller: this.controller })
        .onControllerAttached(() => {
          try {
            this.userAgent = this.controller.getUserAgent();
            let metaData: webview.UserAgentMetadata = new webview.UserAgentMetadata();
            metaData.setPlatform("OpenHarmony");
            this.controller.setCustomUserAgent(this.userAgent);
            let enabled: boolean = webview.WebviewController.getUserAgentClientHintsEnabled();
            console.info("isUserAgentClientHintsEnabled:", enabled);
            webview.WebviewController.setUserAgentClientHintsEnabled(true);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
    }
  }
}
```

## setUserAgentForHosts

```TypeScript
static setUserAgentForHosts(userAgent: string, hosts : Array<string>) : void
```

Set the User-Agent to be used for specified hosts, with a maximum of 20,000 hosts. <p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> Setting the same host list multiple times for the same User-Agent will override the previous settings. That is, if you want to cancel certain hosts from using the specified User-Agent, you need to reset the host list for that User-Agent. </p>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static setUserAgentForHosts(userAgent: string, hosts : Array<string>) : void--><!--Device-WebviewController-static setUserAgentForHosts(userAgent: string, hosts : Array<string>) : void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userAgent | string | Yes | The User-Agent string. |
| hosts | Array&lt;string&gt; | Yes | The hosts to which the User-Agent apply. @static |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    try {
      webview.WebviewController.initializeWebEngine();
      let defaultUserAgent = webview.WebviewController.getDefaultUserAgent();
      let appUA = defaultUserAgent + " appUA";
      webview.WebviewController.setUserAgentForHosts(
        appUA,
        [
          "www.example.com",
          "www.baidu.com"
        ]
      );
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## setUserAgentMetadata

```TypeScript
setUserAgentMetadata(userAgent: string, metaData: UserAgentMetadata): void
```

Sets the User-Agent metadata corresponding to the User-Agent.<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> This User-Agent metadata will be used to populate the User-Agent client hints, They can provide the client's branding and version information, the underlying operating system's branding and major version, as well as details about the underlying device.The User-Agent can be set with setCustomUserAgent or setAppCustomUserAgent or setUserAgentForHosts.If the UserAgentMetadata is not found according to the overridden User-Agent and the overridden User-Agent contains the system default User-Agent, the system default value will be used.If the UserAgentMetadata is not found according to the overridden User-Agent but the overridden User-Agent does not contain the system default User-Agent, only the low-entry User-Agent client hints will be generated. </p>

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebviewController-setUserAgentMetadata(userAgent: string, metaData: UserAgentMetadata): void--><!--Device-WebviewController-setUserAgentMetadata(userAgent: string, metaData: UserAgentMetadata): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userAgent | string | Yes | The User-Agent string. |
| metaData | [UserAgentMetadata](arkts-webview-useragentmetadata-c.md) | Yes | The UserAgentMetadata for the userAgent. |

**Examples**

For details about the sample code, see [setUserAgentClientHintsEnabled](#setuseragentclienthintsenabled).

## setWebDebuggingAccess

```TypeScript
static setWebDebuggingAccess(webDebuggingAccess: boolean): void
```

Sets whether to enable web debugging. By default, web debugging is disabled. For details, see Debugging Frontend Pages by Using DevTools.<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> Enabling web debugging allows users to check and modify the internal status of the web page, which poses security risks. Therefore, you are advised not to enable this function in the officially released version of the app. </p>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static setWebDebuggingAccess(webDebuggingAccess: boolean): void--><!--Device-WebviewController-static setWebDebuggingAccess(webDebuggingAccess: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| webDebuggingAccess | boolean | Yes | Sets whether to enable web debugging.{@code true} enable web debugging; {@code false} disable web debugging. The default value is false. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    try {
      webview.WebviewController.setWebDebuggingAccess(true);
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    try {
      webview.WebviewController.setWebDebuggingAccess(true, 8888);
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## setWebDebuggingAccess

```TypeScript
static setWebDebuggingAccess(webDebuggingAccess: boolean, port: int): void
```

Enables debugging of web contents. <p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> The port numbers from 0 to 1024 are prohibited. Ports less than 0 or greater than 65535 are considered invalid. If an attempt is made to set these disabled or invalid ports, an exception will be thrown. </p>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static setWebDebuggingAccess(webDebuggingAccess: boolean, port: int): void--><!--Device-WebviewController-static setWebDebuggingAccess(webDebuggingAccess: boolean, port: int): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| webDebuggingAccess | boolean | Yes | { |
| port | int | Yes | Indicates the port of the devtools server. After the port is specified, a tcp server socket is created instead of a unix domain socket. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100023](../../apis-arkweb/errorcode-webview.md#17100023-port-number-not-allowed) | The port number is not within the allowed range. @static |

**Examples**

See [setWebDebuggingAccess](#setwebdebuggingaccess)

## setWebDestroyMode

```TypeScript
static setWebDestroyMode(mode: WebDestroyMode): void
```

Set web destroy mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static setWebDestroyMode(mode: WebDestroyMode): void--><!--Device-WebviewController-static setWebDestroyMode(mode: WebDestroyMode): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [WebDestroyMode](arkts-webview-webdestroymode-e.md) | Yes | web destroy mode, default NORMAL_MODE. |

**Examples**

```TypeScript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    // Set the fast destroy mode.
    webview.WebviewController.setWebDestroyMode(webview.WebDestroyMode.FAST_MODE);
    AppStorage.setOrCreate("abilityWant", want);
    console.info("EntryAbility onCreate done");
  }
}
```

## setWebSchemeHandler

```TypeScript
setWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void
```

Set web scheme handler for specific scheme. This is only used for related web component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-setWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void--><!--Device-WebviewController-setWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scheme | string | Yes | String value for url scheme. |
| handler | [WebSchemeHandler](arkts-webview-webschemehandler-c.md) | Yes | Web scheme handler. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Incorrect parameter types. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  schemeHandler: webview.WebSchemeHandler = new webview.WebSchemeHandler();

  build() {
    Column() {
      Button('setWebSchemeHandler')
        .onClick(() => {
          try {
            this.controller.setWebSchemeHandler('http', this.schemeHandler);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## slideScroll

```TypeScript
slideScroll(vx: double, vy: double): void
```

Slide by the speed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-slideScroll(vx: double, vy: double): void--><!--Device-WebviewController-slideScroll(vx: double, vy: double): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| vx | double | Yes | the x speed of the speed. The unit is vp/s. |
| vy | double | Yes | the y speed of the speed. The unit is vp/s. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('slideScroll')
        .onClick(() => {
          try {
            this.controller.slideScroll(500, 500);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Demo</title>
    <style>
        body {
            width:3000px;
            height:3000px;
            padding-right:170px;
            padding-left:170px;
            border:5px solid blueviolet;
        }
    </style>
</head>
<body>
Scroll Test
</body>
</html>
```

## startCamera

```TypeScript
startCamera(): void
```

Enables the camera capture of the current web page. Before using the camera, add the **ohos.permission.CAMERA** permission to **module.json5**. For details about how to add the permission, see [Declaring Permissions in the Configuration File](../../../security/AccessToken/declare-permissions.md).

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-startCamera(): void--><!--Device-WebviewController-startCamera(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, PermissionRequestResult, common } from '@kit.AbilityKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  aboutToAppear(): void {
    let context: Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
    atManager.requestPermissionsFromUser(context, ['ohos.permission.CAMERA'], (err: BusinessError, data: PermissionRequestResult) => {
      console.info('data:' + JSON.stringify(data));
      console.info('data permissions:' + data.permissions);
      console.info('data authResults:' + data.authResults);
    })
  }

  build() {
    Column() {
      Button("startCamera").onClick(() => {
        try {
          this.controller.startCamera();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Button("stopCamera").onClick(() => {
        try {
          this.controller.stopCamera();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Button("closeCamera").onClick(() => {
        try {
          this.controller.closeCamera();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onPermissionRequest((event) => {
          if (event) {
            this.uiContext.showAlertDialog({
              title: 'title',
              message: 'text',
              primaryButton: {
                value: 'deny',
                action: () => {
                  event.request.deny();
                }
              },
              secondaryButton: {
                value: 'onConfirm',
                action: () => {
                  event.request.grant(event.request.getAccessibleResource());
                }
              },
              cancel: () => {
                event.request.deny();
              }
            })
          }
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
    <meta charset="UTF-8">
  </head>
  <body>
    <video id="video" width="400px" height="400px" autoplay>
    </video>
    <input type="button" title="HTML5 Camera" value="Enable Camera" onclick="getMedia()" />
    <script>
      function getMedia() {
        let constraints = {
          video: {
            width: 500,
            height: 500
          },
          audio: true
        }
        let video = document.getElementById("video");
        let promise = navigator.mediaDevices.getUserMedia(constraints);
        promise.then(function(mediaStream) {
          video.srcObject = mediaStream;
          video.play();
        })
      }
    </script>
  </body>
</html>
```

## startDownload

```TypeScript
startDownload(url: string): void
```

Start a download.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-startDownload(url: string): void--><!--Device-WebviewController-startDownload(url: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | The download url. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-incorrect-url-format) | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2 *1024 *1024. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();

  build() {
    Column() {
      Button('setDownloadDelegate')
        .onClick(() => {
          try {
            this.controller.setDownloadDelegate(this.delegate);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('startDownload')
        .onClick(() => {
          try {
            this.controller.startDownload('https://www.example.com');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## stop

```TypeScript
stop(): void
```

Stops the current load.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-stop(): void--><!--Device-WebviewController-stop(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('stop')
        .onClick(() => {
          try {
            this.controller.stop();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        });
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## stopAllMedia

```TypeScript
stopAllMedia(): void
```

Stops all audio and video on a web page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-stopAllMedia(): void--><!--Device-WebviewController-stopAllMedia(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

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
      Button('stopAllMedia')
        .onClick(() => {
          try {
            this.controller.stopAllMedia();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## stopCamera

```TypeScript
stopCamera(): void
```

Stops the camera capture of the current web page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-stopCamera(): void--><!--Device-WebviewController-stopCamera(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

For the complete sample code, see [startCamera](#startcamera).

## stopMicrophone

```TypeScript
stopMicrophone(): void
```

Stops microphone capture on the current web page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-stopMicrophone(): void--><!--Device-WebviewController-stopMicrophone(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

**Examples**

For the complete sample code, see [resumeMicrophone](#resumemicrophone).

## storeWebArchive

```TypeScript
storeWebArchive(baseName: string, autoName: boolean): Promise<string>
```

Stores the current page as a web archive.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-storeWebArchive(baseName: string, autoName: boolean): Promise<string>--><!--Device-WebviewController-storeWebArchive(baseName: string, autoName: boolean): Promise<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| baseName | string | Yes | Where the generated offline webpage is stored, This value cannot be null. |
| autoName | boolean | Yes | Decide whether to automatically generate the file name. If false, it is stored by the file name of baseName. If true, the file name is automatically generated based on the current URL and stored in the file directory of baseName. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | a promise resolved after the web archive has been stored. The parameter will either be the filename under which the file was stored, or empty if storing the file failed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3. Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |
| [17100003](../../apis-arkweb/errorcode-webview.md#17100003-incorrect-resource-path) | Invalid resource path or file type. |

**Examples**

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
      Button('storeWebArchive')
        .onClick(() => {
          try {
            this.controller.storeWebArchive("/data/storage/el2/base/", true, (error, filename) => {
              if (error) {
                console.error(`save web archive error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                return;
              }
              if (filename != null) {
                console.info(`save web archive success: ${filename}`);
              }
            });
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

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
      Button('storeWebArchive')
        .onClick(() => {
          try {
            this.controller.storeWebArchive("/data/storage/el2/base/", true)
              .then(filename => {
                if (filename != null) {
                  console.info(`save web archive success: ${filename}`)
                }
              })
              .catch((error: BusinessError) => {
                console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
              })
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## storeWebArchive

```TypeScript
storeWebArchive(baseName: string, autoName: boolean, callback: AsyncCallback<string>): void
```

Stores the current page as a web archive.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-storeWebArchive(baseName: string, autoName: boolean, callback: AsyncCallback<string>): void--><!--Device-WebviewController-storeWebArchive(baseName: string, autoName: boolean, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| baseName | string | Yes | Where the generated offline webpage is stored, This value cannot be null. |
| autoName | boolean | Yes | Decide whether to automatically generate the file name. If false, it is stored by the file name of baseName. If true, the file name is automatically generated based on the current URL and stored in the file directory of baseName. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | called after the web archive has been stored. The parameter will either be the filename under which the file was stored, or empty if storing the file failed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3. Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |
| [17100003](../../apis-arkweb/errorcode-webview.md#17100003-incorrect-resource-path) | Invalid resource path or file type. |

**Examples**

See [storeWebArchive](#storewebarchive)

## terminateRenderProcess

```TypeScript
terminateRenderProcess(): boolean
```

Destroy the rendering process. Calling this interface will actively destroy the associated rendering process. If the rendering process has not been started or destroyed, it has no effect. In addition, destroying the rendering process will also affect all other instances associated with the rendering process.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-terminateRenderProcess(): boolean--><!--Device-WebviewController-terminateRenderProcess(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if it was possible to terminate the render process, otherwise false. Calling this on a not yet started, or an already terminated render will have no effect. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |

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
      Button('terminateRenderProcess')
        .onClick(() => {
          let result = this.controller.terminateRenderProcess();
          console.info("terminateRenderProcess result: " + result);
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## trimMemoryByPressureLevel

```TypeScript
static trimMemoryByPressureLevel(level: PressureLevel): void
```

Clears the cache occupied by **Web** component based on the specified memory pressure level.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static trimMemoryByPressureLevel(level: PressureLevel): void--><!--Device-WebviewController-static trimMemoryByPressureLevel(level: PressureLevel): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| level | [PressureLevel](arkts-webview-pressurelevel-e.md) | Yes | Pressure level of the memory to be cleared. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter string is too long. 3. Parameter verification failed. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Row() {
        Button('trim_Memory')
          .onClick(() => {
            try {
              // Set the current memory pressure level to moderate and release a small amount of memory.
              webview.WebviewController.trimMemoryByPressureLevel(
                webview.PressureLevel.MEMORY_PRESSURE_LEVEL_MODERATE);
            } catch (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
          })
      }.height('10%')
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## waitForAttached

```TypeScript
waitForAttached(timeout: int): Promise<ControllerAttachState>
```

Wait for the controller to attach a web component until timeout.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-waitForAttached(timeout: int): Promise<ControllerAttachState>--><!--Device-WebviewController-waitForAttached(timeout: int): Promise<ControllerAttachState>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeout | int | Yes | the wait timeout, if timeout reach, promise will return, the unit is millisecond. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ControllerAttachState](arkts-webview-controllerattachstate-e.md)&gt; | Promise used to return the state of attach. |

**Examples**

In the initialization phase, set the WebViewController to wait for the attachment to complete. The timeout interval is 1000 ms. If the attachment is complete or times out, the callback is triggered.

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  async aboutToAppear() {
    this.controller.waitForAttached(1000).then((state: webview.ControllerAttachState) => {
      if (state == webview.ControllerAttachState.ATTACHED) {
        // The callback is triggered when the attachment is complete or times out.
        console.info('Controller is attached.');
      }
    })
    try {
      const state = await this.controller.waitForAttached(1000);
      if (state == webview.ControllerAttachState.ATTACHED) {
        console.info('Controller is attached.');
      }
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## warmupServiceWorker

```TypeScript
static warmupServiceWorker(url: string): void
```

Warmup the registered service worker associated the url.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-static warmupServiceWorker(url: string): void--><!--Device-WebviewController-static warmupServiceWorker(url: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | The url. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-incorrect-url-format) | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2048. |

**Examples**

```TypeScript
// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        console.info("EntryAbility onCreate");
        webview.WebviewController.initializeWebEngine();
        webview.WebviewController.warmupServiceWorker("https://www.example.com");
        AppStorage.setOrCreate("abilityWant", want);
    }
}
```

## webPageSnapshot

```TypeScript
webPageSnapshot(info: SnapshotInfo, callback: AsyncCallback<SnapshotResult>): void
```

Web page snapshot.<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> Only screenshots of assets on the rendering process are supported: still images and text. If there is a video on the page, the placeholder image of the video will be displayed when you take a screenshot, and blank if there is no placeholder. </p>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-webPageSnapshot(info: SnapshotInfo, callback: AsyncCallback<SnapshotResult>): void--><!--Device-WebviewController-webPageSnapshot(info: SnapshotInfo, callback: AsyncCallback<SnapshotResult>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [SnapshotInfo](arkts-webview-snapshotinfo-i.md) | Yes | The snapshot info. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SnapshotResult](arkts-webview-snapshotresult-i.md)&gt; | Yes | the callback of snapshot. |

**Examples**

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
      Button('webPageSnapshot')
        .onClick(() => {
          try {
            this.controller.webPageSnapshot({ id: "1234", size: { width: 100, height: 100 } }, (error, result) => {
              if (error) {
                console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                return;
              }
              if (result) {
                console.info(`return value is:${result}`);
                // You can process the returned result as required.
              }
            });
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## zoom

```TypeScript
zoom(factor: double): void
```

Zooms in or out of this web page. This API is effective only when zoomAccess is true.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-zoom(factor: double): void--><!--Device-WebviewController-zoom(factor: double): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factor | double | Yes | Relative zoom ratio. The value must be greater than 0. The value 1 indicates that the page is not zoomed. A value smaller than 1 indicates zoom-out, and a value greater than 1 indicates zoom-in. <br>Value range: (0, 100]. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |
| [17100004](../../apis-arkweb/errorcode-webview.md#17100004-function-not-enabled) | Function not enabled. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State factor: number = 2;

  build() {
    Column() {
      Button('zoom')
        .onClick(() => {
          try {
            this.controller.zoom(this.factor);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .zoomAccess(true)
    }
  }
}
```

## zoomIn

```TypeScript
zoomIn(): void
```

Zooms in on this web page by 25%.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-zoomIn(): void--><!--Device-WebviewController-zoomIn(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |
| [17100004](../../apis-arkweb/errorcode-webview.md#17100004-function-not-enabled) | Function not enabled. |

**Examples**

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
      Button('zoomIn')
        .onClick(() => {
          try {
            this.controller.zoomIn();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## zoomOut

```TypeScript
zoomOut(): void
```

Zooms out of this web page by 20%.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebviewController-zoomOut(): void--><!--Device-WebviewController-zoomOut(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller-not-associated-with-a-web-component) | Init error. The WebviewController must be associated with a Web component. |
| [17100004](../../apis-arkweb/errorcode-webview.md#17100004-function-not-enabled) | Function not enabled. |

**Examples**

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
      Button('zoomOut')
        .onClick(() => {
          try {
            this.controller.zoomOut();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

