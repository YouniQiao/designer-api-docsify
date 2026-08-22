# WebviewController

WebviewController can control various behaviors of Web components (including page navigation, declaring cycle state, JavaScript interaction and so on). A WebviewController object can only control one Web component, and methods on the Webviewcontroller (except static methods) can only be called after the web component is bound to the WebviewController.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-webview-class WebviewController--><!--Device-webview-class WebviewController-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
```

## accessBackward

```TypeScript
accessBackward(): boolean
```

Checks whether the web page can go back.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-accessBackward(): boolean--><!--Device-WebviewController-accessBackward(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if the web page can go back else false. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

Ark-Dyn示例：

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-accessForward(): boolean--><!--Device-WebviewController-accessForward(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if the web page can go forward else false. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

Ark-Dyn示例：

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-accessStep(step: int): boolean--><!--Device-WebviewController-accessStep(step: int): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| step | int | 是 | The number of steps. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if the web page can go back else false. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { Button, Web, Column, Component, Entry, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State steps: int = 2

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static addIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void--><!--Device-WebviewController-static addIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hostList | Array&lt;string&gt; | 是 | Hosts that bypass the Intelligent Tracking Prevention. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-该设备不支持此api) | Capability not supported. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-avoidVisibleViewportBottom(avoidHeight: int): void--><!--Device-WebviewController-avoidVisibleViewportBottom(avoidHeight: int): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| avoidHeight | int | 是 | the height value of the visible viewport avoidance. The valid interval of avoidHeight is [0, the height of web component]. When avoidHeight is out of the valid interval, it takes the boundary value of the interval. <br>Unit: vp. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |
| [801](../../errorcode-universal.md#801-该设备不支持此api) | Capability not supported. |

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

ArkTS-Sta示例：

```TypeScript
import { Web, Button, Column, Component, Entry } from '@ohos.arkui.component';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@ohos.base';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  avoidHeight: int = 100;

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-backOrForward(step: int): void--><!--Device-WebviewController-backOrForward(step: int): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| step | int | 是 | Steps to go forward or backward. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State step: int = -2

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-backward(): void--><!--Device-WebviewController-backward(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

Ark-Dyn示例：

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static clearBlanklessLoadingCache(keys?: Array<string>) : void--><!--Device-WebviewController-static clearBlanklessLoadingCache(keys?: Array<string>) : void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keys | Array&lt;string&gt; | 否 | The list of key values of pages cached in the blankless loading solution. These key values are specified in getBlanklessInfoKey. The default value is the list of key values of all pages cached in the blankless loading solution. The key length cannot exceed 2048 characters, and the number of keys must be less than or equal to 100. The URL is the same as that input to the Web component during page loading. When the key length exceeds 2048 characters, the key does not take effect. When the number of keys exceeds 100, the first 100 keys are used. If these parameters are left empty, the default values are used. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |  |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    // 假设应用的Web页面在2025/06/10会进行大幅改动，例如商品促销活动等，该提案清除白屏插帧优化缓存
    webview.WebviewController.initializeWebEngine();
    let pageUpdateTime: number = Date.UTC(2025, 5, 10, 0, 0, 0, 0);
    let pageUpdateTime1: number = Date.UTC(2025, 5, 11, 0, 0, 0, 0);
    let pageUpdateTimeNow: number = Date.now();
    if (pageUpdateTimeNow > pageUpdateTime && pageUpdateTime < pageUpdateTime1) {
      // 清除指定页面的白屏插帧方案缓存
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { AppStorage } from '@ohos.arkui.stateManagement';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    // 假设应用的Web页面在2025/06/10会进行大幅改动，例如商品促销活动等，该提案清除白屏插帧优化缓存
    webview.WebviewController.initializeWebEngine();
    let pageUpdateTime: number = Date.UTC(2025, 5, 10, 0, 0, 0, 0);
    let pageUpdateTime1: number = Date.UTC(2025, 5, 11, 0, 0, 0, 0);
    let pageUpdateTimeNow: number = Date.now();
    if (pageUpdateTimeNow > pageUpdateTime && pageUpdateTime < pageUpdateTime1) {
      // 清除指定页面的白屏插帧方案缓存
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-clearClientAuthenticationCache(): void--><!--Device-WebviewController-clearClientAuthenticationCache(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-clearHistory(): void--><!--Device-WebviewController-clearHistory(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { Web, Column, Component, Entry, Button } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static clearHostIP(hostName: string): void--><!--Device-WebviewController-static clearHostIP(hostName: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hostName | string | 是 | Which host name to be cleared. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |

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
      // URL加载前设置生效.
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      // URL加载前设置生效。
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static clearIntelligentTrackingPreventionBypassingList(): void--><!--Device-WebviewController-static clearIntelligentTrackingPreventionBypassingList(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) | Capability not supported. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-clearMatches(): void--><!--Device-WebviewController-clearMatches(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

Clears the cache of prefetched resources based on the specified cache key list. The cache key in the input parameter must be the prefetched resource cache key specified by API[prefetchResource](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#prefetchresource).

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static clearPrefetchedResource(cacheKeyList: Array<string>): void--><!--Device-WebviewController-static clearPrefetchedResource(cacheKeyList: Array<string>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cacheKeyList | Array&lt;string&gt; | 是 | The keys for memory cache. The key in cacheKeyList only support number and letters. |

**示例**

ArkTS-Dyn示例：

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
          // 预获取时，需要将"https://www.example1.com/post?e=f&g=h"替换成真实要访问的网站地址。
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
          // 清除后续不再使用的预获取缓存。
          webview.WebviewController.clearPrefetchedResource(["KeyX",]);
        })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// Index.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Web, Column, Component, Entry } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: "https://www.example.com/", controller: this.controller })
        .onAppear(() => {
          // 预获取时，需要將"https://www.example1.com/post?e=f&g=h"替换成真实要访问的网站地址。
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
          // 清除后续不再使用的预获取缓存。
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static clearServiceWorkerWebSchemeHandler(): void--><!--Device-WebviewController-static clearServiceWorkerWebSchemeHandler(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-clearSslCache(): void--><!--Device-WebviewController-clearSslCache(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-clearWebSchemeHandler(): void--><!--Device-WebviewController-clearWebSchemeHandler(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { Web, Column, Component, Entry, Button } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

控制网页所有全屏视频关闭。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-closeAllMediaPresentations(): void--><!--Device-WebviewController-closeAllMediaPresentations(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

关闭当前网页摄像头捕获。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-closeCamera(): void--><!--Device-WebviewController-closeCamera(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

完整示例代码参考[startCamera](#startcamera)。

## constructor

```TypeScript
constructor(webTag?: string)
```

A constructor used to create a WebviewController object.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-constructor(webTag?: string)--><!--Device-WebviewController-constructor(webTag?: string)-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| webTag | string | 否 | specified the name of the web component, Empty by default. |

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

## createPdf

```TypeScript
createPdf(configuration: PdfConfiguration, callback: AsyncCallback<PdfData>): void
```

Rendering current Web page into Pdf data, return the result in async mode.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-createPdf(configuration: PdfConfiguration, callback: AsyncCallback<PdfData>): void--><!--Device-WebviewController-createPdf(configuration: PdfConfiguration, callback: AsyncCallback<PdfData>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configuration | [PdfConfiguration](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-pdfconfiguration-i.md) | 是 | configuration for createPdf, including page width and height, etc. {@Link PdfConfiguration} |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PdfData](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-pdfdata-c.md)&gt; | 是 | Callbacks execute createPdf results. PdfData is pdf data stream of current web page in Uint8Array {@Link PdfData}. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Invalid input parameter. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { fileIo } from '@kit.CoreFileKit';
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
                // 获取组件上下文
                let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                // 获取沙箱路径，设置pdf文件名
                let filePath = context.filesDir + "/test.pdf";
                let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
                if (error) {
                  console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                  return;
                }
                fileIo.write(file.fd, result.pdfArrayBuffer().buffer).then((writeLen: number) => {
                  console.info("createPDF write data to file succeeded and size is:" + writeLen);
                }).catch((err: BusinessError) => {
                  console.error("createPDF write data to file failed with error message: " + err.message +
                    ", error code: " + err.code);
                }).finally(() => {
                  fileIo.closeSync(file);
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

ArkTS-Sta示例：

```TypeScript
'use static'
import { fileIo } from '@kit.CoreFileKit';
import { Entry, Column, Component, Button, Web } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError, AsyncCallback } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  pdfConfig: webview.PdfConfiguration = {
    width: 8.27,
    height: 11.69,
    marginTop: 0,
    marginBottom: 0,
    marginRight: 0,
    marginLeft: 0,
    shouldPrintBackground: true
  } as webview.PdfConfiguration

  build() {
    Column() {
      Button('SavePDF')
        .onClick(() => {
          this.controller.createPdf(
            this.pdfConfig,
            (error, result: webview.PdfData | undefined) => {
              try {
                // 获取组件上下文
                let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                // 获取沙箱路径，设置pdf文件名
                let filePath = context.filesDir + "/test.pdf";
                let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
                if (error) {
                  console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                  return;
                }
                let arrayBuffer: Uint8Array = result?.pdfArrayBuffer() as Uint8Array;
                fileIo.write(file.fd, arrayBuffer.buffer).then((writeLen: long) => {
                  console.info("createPDF write data to file succeeded and size is:" + writeLen);
                }).catch((err: Error) => {
                  console.error("createPDF write data to file failed with error message: " + err.message +
                    ", error code: " + err.code);
                }).finally(() => {
                  fileIo.closeSync(file);
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

ArkTS-Dyn示例：

```TypeScript
import { fileIo } from '@kit.CoreFileKit';
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
                // 获取组件上下文
                let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                // 获取沙箱路径，设置pdf文件名
                let filePath = context.filesDir + "/test.pdf";
                let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
                fileIo.write(file.fd, result.pdfArrayBuffer().buffer).then((writeLen: number) => {
                  console.info("createPDF write data to file succeeded and size is:" + writeLen);
                }).catch((err: BusinessError) => {
                  console.error("createPDF write data to file failed with error message: " + err.message +
                    ", error code: " + err.code);
                }).finally(() => {
                  fileIo.closeSync(file);
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

ArkTS-Sta示例：

```TypeScript
'use static'
import { fileIo } from '@kit.CoreFileKit';
import { Entry, Column, Component, Button, Web } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError, AsyncCallback } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  pdfConfig: webview.PdfConfiguration = {
    width: 8.27,
    height: 11.69,
    marginTop: 0,
    marginBottom: 0,
    marginRight: 0,
    marginLeft: 0,
    shouldPrintBackground: true
  } as webview.PdfConfiguration

  build() {
    Column() {
      Button('SavePDF')
        .onClick(() => {
          this.controller.createPdf(this.pdfConfig)
            .then((result: webview.PdfData) => {
              try {
                // 获取组件上下文
                let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                // 获取沙箱路径，设置pdf文件名
                let filePath = context.filesDir + "/test.pdf";
                let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
                fileIo.write(file.fd, result.pdfArrayBuffer().buffer).then((writeLen: long) => {
                  console.info("createPDF write data to file succeeded and size is:" + writeLen);
                }).catch((err: Error) => {
                  console.error("createPDF write data to file failed with error message: " + err.message +
                    ", error code: " + err.code);
                }).finally(() => {
                  fileIo.closeSync(file);
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-createPdf(configuration: PdfConfiguration): Promise<PdfData>--><!--Device-WebviewController-createPdf(configuration: PdfConfiguration): Promise<PdfData>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configuration | [PdfConfiguration](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-pdfconfiguration-i.md) | 是 | configuration for createPdf, including page width and height, etc. {@Link PdfConfiguration} |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[PdfData](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-pdfdata-c.md)&gt; | The promise returned by the function. PdfData is pdf data stream of current web page in Uint8Array { |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Invalid input parameter. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

参见 [createPdf](#createpdf)

## createWebMessagePorts

```TypeScript
createWebMessagePorts(isExtentionType?: boolean): Array<WebMessagePort>
```

Create web message ports

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-createWebMessagePorts(isExtentionType?: boolean): Array<WebMessagePort>--><!--Device-WebviewController-createWebMessagePorts(isExtentionType?: boolean): Array<WebMessagePort>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isExtentionType | boolean | 否 | Set whether the web message port supports extention type. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;[WebMessagePort](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-webmessageport-i.md)&gt; | An array represent 2 WebMessagePort, then can use those ports to communication with html pages. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

完整示例代码参考[onMessageEventExt](./arkts-apis-webview-WebMessagePort.md#onmessageeventext)。

## createWebPrintDocumentAdapter

```TypeScript
createWebPrintDocumentAdapter(jobName: string): print.PrintDocumentAdapter
```

Creates a PrintDocumentAdapter instance to provide content for printing.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-createWebPrintDocumentAdapter(jobName: string): print.PrintDocumentAdapter--><!--Device-WebviewController-createWebPrintDocumentAdapter(jobName: string): print.PrintDocumentAdapter-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| jobName | string | 是 | Name of the file to print. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| print.PrintDocumentAdapter | Return PrintDocumentAdapter instance created. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
import print from '@ohos.print';
import { Entry, Column, Component, Button, Web } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError, AsyncCallback } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

const myPrintAttributes: print.PrintAttributes = {
  copyNumber: 1 as int,
  pageRange: {
    startPage: 1 as int,
    endPage: 1 as int,
    pages: [1] as Array<int>
  },
  pageSize: {
    id: 'PAGE_ISO_A4',
    name: 'A4',
    width: 210 as int,
    height: 297 as int
  },
  directionMode: print.PrintDirectionMode.DIRECTION_MODE_PORTRAIT,
  colorMode: print.PrintColorMode.COLOR_MODE_COLOR,
  duplexMode: print.PrintDuplexMode.DUPLEX_MODE_NONE,
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Button('createWebPrintDocumentAdapter')
        .onClick(() => {
          try {
            let webPrintDocadapter = this.controller.createWebPrintDocumentAdapter('example.pdf');
            print.print('example_jobid', webPrintDocadapter, myPrintAttributes, this.getUIContext().getHostContext() as common.UIAbilityContext);
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static customizeSchemes(schemes: Array<WebCustomScheme>): void--><!--Device-WebviewController-static customizeSchemes(schemes: Array<WebCustomScheme>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| schemes | Array&lt;[WebCustomScheme](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-webcustomscheme-i.md)&gt; | 是 | Configuration of web custom scheme. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
| [17100020](../../apis-arkweb/errorcode-webview.md#17100020-注册自定义协议失败) | Failed to register custom schemes. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { WebResourceResponse, OnInterceptRequestEvent } from '@kit.ArkUI'

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  responseWeb: WebResourceResponse = new WebResourceResponse();
  scheme1: webview.WebCustomScheme =
    { schemeName: "name1", isSupportCORS: true, isSupportFetch: true } as webview.WebCustomScheme;
  scheme2: webview.WebCustomScheme =
    { schemeName: "name2", isSupportCORS: true, isSupportFetch: true } as webview.WebCustomScheme;
  scheme3: webview.WebCustomScheme =
    { schemeName: "name3", isSupportCORS: true, isSupportFetch: true } as webview.WebCustomScheme;

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
        .onInterceptRequest((event: OnInterceptRequestEvent): WebResourceResponse => {
          if (event) {
            console.info('url:' + event.request.getRequestUrl());
          }
          return this.responseWeb;
        })
    }
  }
}
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { WebResourceResponse, OnInterceptRequestEvent } from '@kit.ArkUI'

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  responseWeb: WebResourceResponse = new WebResourceResponse();
  scheme1: webview.WebCustomScheme =
    { schemeName: "name1", isSupportCORS: true, isSupportFetch: true } as webview.WebCustomScheme;
  scheme2: webview.WebCustomScheme =
    { schemeName: "name2", isSupportCORS: true, isSupportFetch: true } as webview.WebCustomScheme;
  scheme3: webview.WebCustomScheme =
    { schemeName: "name3", isSupportCORS: true, isSupportFetch: true } as webview.WebCustomScheme;

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static customizeSchemes(schemes: Array<WebCustomScheme>, lazyInitWebEngine: boolean): void--><!--Device-WebviewController-static customizeSchemes(schemes: Array<WebCustomScheme>, lazyInitWebEngine: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| schemes | Array&lt;[WebCustomScheme](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-webcustomscheme-i.md)&gt; | 是 | Configuration of web custom scheme. |
| lazyInitWebEngine | boolean | 是 | When true: The interface internally skips initializing WebEngine and temporarily stores the registered schemes, which will be passed to WebEngine when it actually initializes. When false: The interface automatically performs WebEngine initialization internally. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100020](../../apis-arkweb/errorcode-webview.md#17100020-注册自定义协议失败) | Failed to register custom schemes. |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. The length of the schemes array is greater than 10. 2. The character length of the scheme is greater than 32. 3. The character in the scheme is not within the allowed range of lowercase English letters, numbers, and the symbols ".", "+", "-". @static |

**示例**

参见 [customizeSchemes](#customizeschemes)

## deleteJavaScriptRegister

```TypeScript
deleteJavaScriptRegister(name: string): void
```

Deletes a registered JavaScript object with given name.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-deleteJavaScriptRegister(name: string): void--><!--Device-WebviewController-deleteJavaScriptRegister(name: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | The name of a registered JavaScript object to be deleted. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |
| [17100008](../../apis-arkweb/errorcode-webview.md#17100008-删除不存在的javascriptproxy) | Failed to delete JavaScriptProxy because it does not exist. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry, $rawfile, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class TestObj {
  constructor() {
  }

  test(): string {
    return "ArkUI Web Component";
  }

  toString(): string {
    console.info('Web Component toString');
    return 'TestObj toString';
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-enableAdsBlock(enable: boolean): void--><!--Device-WebviewController-enableAdsBlock(enable: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | { |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Parameter string is too long. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |
| [801](../../errorcode-universal.md#801-该设备不支持此api) | Capability not supported. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WebviewController-static enableAdvancedSecurityMode(securityParams: SecurityParams): void--><!--Device-WebviewController-static enableAdvancedSecurityMode(securityParams: SecurityParams): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| securityParams | [SecurityParams](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-securityparams-i.md) | 是 | The options means which supported option or item will be disabled. |

**示例**

ArkTS-Dyn示例：

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  aboutToAppear() {
    webview.WebviewController.enableAdvancedSecurityMode({
      disableJITCompilation: true,
      disableWebAssembly: true,
      disableWebGL: true,
      disablePDFViewer: true,
      disableMathML: true,
      disableServiceWorker: true,
      disableNonProxyUDP: true
    });
    webview.WebviewController.initializeWebEngine();
  }

  build() {
    Column() {
      Web({ src: 'https://www.example.com', controller: this.controller })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Column, Component, Entry, Web } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  aboutToAppear() {
    webview.WebviewController.enableAdvancedSecurityMode({
      disableJITCompilation: true,
      disableWebAssembly: true,
      disableWebGL: true,
      disablePDFViewer: true,
      disableMathML: true,
      disableServiceWorker: true,
      disableNonProxyUDP: true
    });
    webview.WebviewController.initializeWebEngine();
  }

  build() {
    Column() {
      Web({ src: "https://www.example.com", controller: this.controller })
    }
  }
}
```

## enableBackForwardCache

```TypeScript
static enableBackForwardCache(features?: BackForwardCacheSupportedFeatures): void
```

Enable the BackForwardCache and indicate features that are allowed to enter BackForwardCache. Default is disabled.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static enableBackForwardCache(features?: BackForwardCacheSupportedFeatures): void--><!--Device-WebviewController-static enableBackForwardCache(features?: BackForwardCacheSupportedFeatures): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| features | [BackForwardCacheSupportedFeatures](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-backforwardcachesupportedfeatures-c.md) | 否 | The features that supports BackForwardCache. @static |

**示例**

ArkTS-Dyn示例：

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
        // 如果一个页面同时使用了同层渲染和视频托管的能力，需要 nativeEmbed 和
        // mediaTakeOver 同时设置为 true，该页面才可以进入前进后退缓存中。
        webview.WebviewController.enableBackForwardCache(features);
        webview.WebviewController.initializeWebEngine();
        AppStorage.setOrCreate("abilityWant", want);
    }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { AppStorage } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let features = new webview.BackForwardCacheSupportedFeatures();
    features.nativeEmbed = true;
    features.mediaTakeOver = true;
    // 如果一个页面同时使用了同层渲染和视频托管的能力，需要 nativeEmbed 和
    // mediaTakeOver 同时设置为 true，该页面才可以进入前进后退缓存中。
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-enableIntelligentTrackingPrevention(enable: boolean): void--><!--Device-WebviewController-enableIntelligentTrackingPrevention(enable: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | { |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-该设备不支持此api) | Capability not supported. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static enablePrivateNetworkAccess(enable: boolean): void--><!--Device-WebviewController-static enablePrivateNetworkAccess(enable: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | {@code true} enable the private network access check; {@code false} otherwise. @static |

**示例**

ArkTS-Dyn示例：

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
          // 设置为false时ArkWeb将不再检查私有网络请求是否合法
          webview.WebviewController.enablePrivateNetworkAccess(false);
        })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { webview } from '@kit.ArkWeb';
import { Entry, Column, Component, Web } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onControllerAttached(() => {
          // 设置为false时ArkWeb将不再检查私有网络请求是否合法
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-enableSafeBrowsing(enable: boolean): void--><!--Device-WebviewController-enableSafeBrowsing(enable: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | {@code true} enable check the website security risks; {@code false} otherwise. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static enableWholeWebPageDrawing(): void--><!--Device-WebviewController-static enableWholeWebPageDrawing(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Column, Component, Button, Web } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

## forward

```TypeScript
forward(): void
```

Goes forward in the history of the web page.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-forward(): void--><!--Device-WebviewController-forward(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

Ark-Dyn示例：

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

获取当前ArkWeb内核版本。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static getActiveWebEngineVersion(): ArkWebEngineVersion--><!--Device-WebviewController-static getActiveWebEngineVersion(): ArkWebEngineVersion-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ArkWebEngineVersion](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-arkwebengineversion-e.md) | 返回由[ArkWebEngineVersion]{ |

**示例**

请参考[setActiveWebEngineVersion](#setactivewebengineversion)。

## getAttachState

```TypeScript
getAttachState(): ControllerAttachState
```

Get whether webviewController is attached to a web component.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getAttachState(): ControllerAttachState--><!--Device-WebviewController-getAttachState(): ControllerAttachState-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ControllerAttachState](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-controllerattachstate-e.md) | the attach state of controller |

## getBackForwardEntries

```TypeScript
getBackForwardEntries(): BackForwardList
```

Get back forward stack list from current webview.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getBackForwardEntries(): BackForwardList--><!--Device-WebviewController-getBackForwardEntries(): BackForwardList-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BackForwardList](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-backforwardlist-i.md) | Back forward list for current webview. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { webview } from '@kit.ArkWeb';
import { Entry, Column, Component, Web, Button } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getBlanklessInfoWithKey(key: string) : BlanklessInfo--><!--Device-WebviewController-getBlanklessInfoWithKey(key: string) : BlanklessInfo-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key value that uniquely identifies the page. Default value: N/A. The value cannot be empty or exceed 2048 characters. When an invalid value is set, this API does not take effect. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BlanklessInfo](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-blanklessinfo-i.md) | The prediction information about the blankless loading solution. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |  |

**示例**

ArkTS-Dyn示例：

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
            // 当相似度超过50%，加载耗时小于1000ms时启用插帧，否则不启用。
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import { Entry, Column, Component, Web } from '@ohos.arkui.component'
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  build() {
    Column() {
      Web({ src: 'https://www.example.com', controller: this.controller })
       .javaScriptAccess(true)
       .onLoadIntercept((event) => {
          // 当相似度超过50%，加载耗时小于1000ms时启用插帧，否则不启用。
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getCertificate(): Promise<Array<cert.X509Cert>>--><!--Device-WebviewController-getCertificate(): Promise<Array<cert.X509Cert>>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;cert.X509Cert&gt;&gt; | the promise of the current website's certificate. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a web component. |

**示例**

ArkTS-Dyn示例：

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
  // outputStr在UI界面显示调试信息
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
              // 加载一个过期的证书网站，查看获取到的证书信息
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
              // 加载一个https网站，查看网站的证书信息
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
            // 忽略ssl证书错误，便于测试一些证书过期的网站，如：https://expired.badssl.com
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

ArkTS-Sta示例：

```TypeScript
'use static'
import { Entry, Text, Column, Component, Button, Web, State, Row, List, ListItem, FontWeight, ButtonType, Axis } from '@kit.ArkUI'
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

function ParseX509CertInfo(x509CertArray: Array<cert.X509Cert>|undefined) {
  if (x509CertArray !== undefined) {
    let res: string = 'getCertificate success: len = ' + x509CertArray.length;
    for (let i = 0; i < x509CertArray.length; i++) {
      res += ', index = ' + i + ', issuer name = '
        + Uint8ArrayToString(x509CertArray[i].getIssuerName().data) + ', subject name = '
        + Uint8ArrayToString(x509CertArray[i].getSubjectName().data) + ', valid start = '
        + x509CertArray[i].getNotBeforeTime()
        + ', valid end = ' + x509CertArray[i].getNotAfterTime();
    }
    return res
  } else {
    console.error("ParseX509CertInfo x509CertArray is undefined");
    return "";
  }
}

@Entry
@Component
struct Index {
  // outputStr在UI界面显示调试信息。
  @State outputStr: string = '';
  webviewCtl: webview.WebviewController = new webview.WebviewController(undefined);

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
              // 加载一个过期的证书网站，查看获取到的证书信息。
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
              // 加载一个https网站，查看网站的证书信息。
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
                this.webviewCtl.getCertificate((error: BusinessError|null, x509CertArray: Array<cert.X509Cert>|undefined):void=> {
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
            // 忽略ssl证书错误，便于测试一些证书过期的网站，如：https://expired.badssl.com。
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

ArkTS-Dyn示例：

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
  // outputStr在UI界面显示调试信息
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
              // 加载一个过期的证书网站，查看获取到的证书信息
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
              // 加载一个https网站，查看网站的证书信息
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
            // 忽略ssl证书错误，便于测试一些证书过期的网站，如：https://expired.badssl.com
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Text, Column, Component, Button, Web, State, Row, List, ListItem, FontWeight, ButtonType, Axis } from '@kit.ArkUI'
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

function ParseX509CertInfo(x509CertArray: Array<cert.X509Cert>|undefined) {
  if (x509CertArray !== undefined) {
    let res: string = 'getCertificate success: len = ' + x509CertArray.length;
    for (let i = 0; i < x509CertArray.length; i++) {
      res += ', index = ' + i + ', issuer name = '
        + Uint8ArrayToString(x509CertArray[i].getIssuerName().data) + ', subject name = '
        + Uint8ArrayToString(x509CertArray[i].getSubjectName().data) + ', valid start = '
        + x509CertArray[i].getNotBeforeTime()
        + ', valid end = ' + x509CertArray[i].getNotAfterTime();
    }
    return res
  } else {
    console.error("ParseX509CertInfo x509CertArray is undefined");
    return "";
  }
}

@Entry
@Component
struct Index {
  // outputStr在UI界面显示调试信息
  @State outputStr: string = '';
  webviewCtl: webview.WebviewController = new webview.WebviewController(undefined);

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
              // 加载一个过期的证书网站，查看获取到的证书信息
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
              // 加载一个https网站，查看网站的证书信息
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
                this.webviewCtl.getCertificate((error: BusinessError|null, x509CertArray: Array<cert.X509Cert>|undefined):void=> {
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
            // 忽略ssl证书错误，便于测试一些证书过期的网站，如：https://expired.badssl.com。
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getCertificate(callback: AsyncCallback<Array<cert.X509Cert>>): void--><!--Device-WebviewController-getCertificate(callback: AsyncCallback<Array<cert.X509Cert>>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;cert.X509Cert&gt;&gt; | 是 | the callback of getCertificate. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a web component. |

**示例**

参见 [getCertificate](#getcertificate)

## getCustomUserAgent

```TypeScript
getCustomUserAgent(): string
```

Get custom user agent.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getCustomUserAgent(): string--><!--Device-WebviewController-getCustomUserAgent(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Get custom User agent information. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Entry, Column, Component, Web, Button, State } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static getDefaultUserAgent(): string--><!--Device-WebviewController-static getDefaultUserAgent(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | The default user agent string. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// EntryAbility.ets
'use static'
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { AppStorage } from '@kit.ArkUI';

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getErrorPageEnabled(): boolean--><!--Device-WebviewController-getErrorPageEnabled(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if enable the default error page feature; else false. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { webview } from '@kit.ArkWeb';
import { Web, Column, Component, Entry } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getFavicon(): image.PixelMap--><!--Device-WebviewController-getFavicon(): image.PixelMap-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| image.PixelMap | Return the favicon bitmap of the current page. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Button, Web, Column, Component, Entry, State } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getLastHitTest(): HitTestValue--><!--Device-WebviewController-getLastHitTest(): HitTestValue-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HitTestValue](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-hittestvalue-i.md) | Return the element information of the clicked area. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, Button } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getLastJavascriptProxyCallingFrameUrl(): string--><!--Device-WebviewController-getLastJavascriptProxyCallingFrameUrl(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | The url of the last frame that calls the JavaScriptProxy. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { Web, Column, Component, Entry, Button, $rawfile, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@ohos.base';


class TestObj {
  mycontroller: webview.WebviewController;

  constructor(controller: webview.WebviewController) {
    this.mycontroller = controller;
  }

  test(testStr: string): string {
    console.info('Web Component str' + testStr + " url " + this.mycontroller.getLastJavascriptProxyCallingFrameUrl());
    return testStr;
  }

  toStringFunc(): void {
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
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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
            this.controller.registerJavaScriptProxy(this.testObjtest, "objName", ["test", "toStringFunc", "testNumber", "testBool"]);
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

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WebviewController-getLastPostMessageURL(): string--><!--Device-WebviewController-getLastPostMessageURL(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | The URL of frame that last sent a postMessage. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

## getMediaPlaybackState

```TypeScript
getMediaPlaybackState(): MediaPlaybackState
```

查询当前网页音视频播放状态。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getMediaPlaybackState(): MediaPlaybackState--><!--Device-WebviewController-getMediaPlaybackState(): MediaPlaybackState-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaPlaybackState](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-mediaplaybackstate-e.md) | 当前网页的播放状态，具体值为NONE、PLAYING、PAUSED、STOPPED。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getOriginalUrl(): string--><!--Device-WebviewController-getOriginalUrl(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Return the original url of the current page. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getPageHeight(): int--><!--Device-WebviewController-getPageHeight(): int-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | Height of the current web page. Unit: vp. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'

import { Web, Button, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getPageOffset(): ScrollOffset--><!--Device-WebviewController-getPageOffset(): ScrollOffset-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScrollOffset](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-scrolloffset-i.md) | page offset |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |  |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'

import { Web, Column, Component, Entry, $rawfile} from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
         text-align: center;       /* 水平居中 */
         line-height: 200px;       /* 垂直居中（值等于容器高度） */
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getPrintBackground(): boolean--><!--Device-WebviewController-getPrintBackground(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Get whether print web page background. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { Entry, Column, Component, Web, Button } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getProgress() : int--><!--Device-WebviewController-getProgress() : int-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The loading progress for the current page. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) | Capability not supported. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { webview } from '@kit.ArkWeb';
import { Entry, Column, Component, Web } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static getRenderProcessMode(): RenderProcessMode--><!--Device-WebviewController-static getRenderProcessMode(): RenderProcessMode-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RenderProcessMode](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-renderprocessmode-e.md) | mode - The render process mode of the ArkWeb. Call { |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Column, Component, Button, Web } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct webViewController {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Button('getRenderProcessMode')
        .onClick(() => {
          let mode = webview.WebviewController.getRenderProcessMode();
          console.info("getRenderProcessMode: " + mode);
        });
      Web({
        src: 'www.example.com', controller: this.controller,
      })
    }
  }
}
```

## getScrollable

```TypeScript
getScrollable(): boolean
```

Get whether scrolling is allowed.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getScrollable(): boolean--><!--Device-WebviewController-getScrollable(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Get scrolling is allowed information. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
'use static'

// xxx.ets
import { Entry, Column, Component, Button, Web } from '@ohos.arkui.component';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@ohos.base';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getScrollOffset(): ScrollOffset--><!--Device-WebviewController-getScrollOffset(): ScrollOffset-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScrollOffset](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-scrolloffset-i.md) | scroll offset |

**示例**

ArkTS-Dyn示例：

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
            // case1：网页向下过滚动时，可直接使用ScrollOffset.y
            console.info(`get downwards overscroll offsetY = ${this.controllerY}`);
          } else if ((this.controllerY != 0) && (this.controllerY > (pageHeight - webHeight))) {
            // case2：网页向上过滚动时，需计算出网页下边界与Web组件下边界的偏移量
            console.info(`get upwards overscroll offsetY = ${this.controllerY - (pageHeight >= webHeight ? (pageHeight - webHeight) : 0)}`);
          } else {
            // case3：网页未发生过滚动时，可直接使用ScrollOffset.y
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'

import { $rawfile, Web, Text, Row, Column, Component, Entry, OverScrollMode, FontWeight, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  @State testTitle: string = 'webScroll'
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State controllerX: double =-100;
  @State controllerY: double =-100;
  @State mode: OverScrollMode = OverScrollMode.ALWAYS;

  build() {
    Column() {
      Row() {
        Text(this.testTitle)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
      }
      Column() {
        Text(`controllerX: ${this.controllerX}, controllerY: ${this.controllerY}`)
      }
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
            // case1：网页向下过滚动时，可直接使用ScrollOffset.y
            console.info(`get downwards overscroll offsetY = ${this.controllerY}`);
          } else if ((this.controllerY != 0) && (this.controllerY > (pageHeight - webHeight))) {
            // case2：网页向上过滚动时，需计算出网页下边界与Web组件下边界的偏移量
            console.info(`get upwards overscroll offsetY = ${this.controllerY - (pageHeight >= webHeight ? (pageHeight - webHeight) : 0)}`);
          } else {
            // case3：网页未发生过滚动时，可直接使用ScrollOffset.y
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

加载的html文件。

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getSecurityLevel(): SecurityLevel--><!--Device-WebviewController-getSecurityLevel(): SecurityLevel-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| SecurityLevel | the security level of current page. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, OnPageEndEvent } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onPageEnd((event: OnPageEndEvent): void => {
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static getSiteIsolationMode(): SiteIsolationMode--><!--Device-WebviewController-static getSiteIsolationMode(): SiteIsolationMode-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SiteIsolationMode](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-siteisolationmode-e.md) | The site isolation mode of the application. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import { Entry, Component, Column, Web, Button } from '@ohos.arkui.component'
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

## getSurfaceId

```TypeScript
getSurfaceId(): string
```

Get the ID of the surface created by ArkWeb. This ID can be used for web page screenshots.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getSurfaceId(): string--><!--Device-WebviewController-getSurfaceId(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | The ID of the surface created by ArkWeb. |

**示例**

ArkTS-Dyn示例：

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
      Button("截图")
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { State, Entry, Column, Component, Button, Web, Image, ImageContent, Resource, DrawableDescriptor } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Example{
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  @State imagePixelMap: image.PixelMap | DrawableDescriptor | ImageContent | String | Resource = '';

  build(){
    Column(){
      Button("截图")
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getTitle(): string--><!--Device-WebviewController-getTitle(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Return to File Selector Title. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getUrl(): string--><!--Device-WebviewController-getUrl(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Return the url of the current page. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

## getUserAgent

```TypeScript
getUserAgent(): string
```

Gets the default user agent.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getUserAgent(): string--><!--Device-WebviewController-getUserAgent(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Return user agent information. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Entry, Column, Component, Web, Button } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

ArkTS-Dyn示例：

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
        // 应用侧用法示例，定制User-Agent。
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Entry, Column, Component, Web, State } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State ua: string = "";

  aboutToAppear(): void {
    webview.once('webInited', () => {
      try {
        // 应用侧用法示例，定制User-Agent。
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

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WebviewController-static getUserAgentClientHintsEnabled(): boolean--><!--Device-WebviewController-static getUserAgentClientHintsEnabled(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | If User-Agent Client Hints was enabled. |

**示例**

完整示例代码参考[setUserAgentClientHintsEnabled](#setuseragentclienthintsenabled)。

完整示例代码参考[setUserAgentClientHintsEnabled](#setuseragentclienthintsenabled)。

## getUserAgentMetadata

```TypeScript
getUserAgentMetadata(userAgent: string): UserAgentMetadata
```

Get the User-Agent metadata corresponding to the User-Agent.

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WebviewController-getUserAgentMetadata(userAgent: string): UserAgentMetadata--><!--Device-WebviewController-getUserAgentMetadata(userAgent: string): UserAgentMetadata-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userAgent | string | 是 | The User-Agent string. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UserAgentMetadata](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-useragentmetadata-c.md) | The UserAgentMetadata for the userAgent. |

**示例**

完整示例代码参考[setUserAgentClientHintsEnabled](#setuseragentclienthintsenabled)。

完整示例代码参考[setUserAgentClientHintsEnabled](#setuseragentclienthintsenabled)。

## getWebId

```TypeScript
getWebId(): int
```

Gets the index value of the current Web component for the management of multiple Web components.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-getWebId(): int--><!--Device-WebviewController-getWebId(): int-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | Returns the index value of the current Web component. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import { Web, Button, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

通过Promise方式异步查找当前页面是否存在图像。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-hasImage(): Promise<boolean>--><!--Device-WebviewController-hasImage(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise实例，返回查找页面是否存在图像。 <br> true表示页面存在图像；false表示页面不存在图像。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Button('hasImageCb')
        .onClick(() => {
          try {
            this.controller.hasImage((error: BusinessError | null, data:  Boolean | undefined): void => {
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Button('hasImagePm')
        .onClick(() => {
          try {
            this.controller.hasImage().then((data: boolean) => {
              console.info('hasImage: ' + data);
            }).catch((error: Error): PromiseLike<void> | undefined => {
              console.error("error: " + error);
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

## hasImage

```TypeScript
hasImage(callback: AsyncCallback<boolean>): void
```

通过Callback方式异步查找当前页面是否存在图像。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-hasImage(callback: AsyncCallback<boolean>): void--><!--Device-WebviewController-hasImage(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 | 返回查找页面是否存在图像。<br> true表示页面存在图像；false表示页面不存在图像。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

参见 [hasImage](#hasimage)

## initializeWebEngine

```TypeScript
static initializeWebEngine(): void
```

Initialize the web engine before loading the Web components. This is a global static API that must be called on the UI thread, and it will have no effect if any Web components are loaded.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static initializeWebEngine(): void--><!--Device-WebviewController-static initializeWebEngine(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**示例**

本示例以EntryAbility为例，描述了在Ability创建阶段完成Web组件动态库加载的功能。

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-injectOfflineResources(resourceMaps: Array<OfflineResourceMap>): void--><!--Device-WebviewController-injectOfflineResources(resourceMaps: Array<OfflineResourceMap>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceMaps | Array&lt;[OfflineResourceMap](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-offlineresourcemap-i.md)&gt; | 是 | Array of offline resource info maps. The count of array must between 1 and 30. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-url格式错误) | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2 *1024 *1024. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
// EntryAbility.ets
import { UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import AbilityConstant from '@ohos.app.ability.AbilityConstant';
import { UIContext, LocalStorage, window } from '@kit.ArkUI';

const localStorage: LocalStorage = new LocalStorage('uiContext');

class EntryAbility extends UIAbility {
  storage: LocalStorage = localStorage;

  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.loadContent('pages/Index', this.storage, (err: BusinessError<void> | null, data): void => {
      if (err && err.code) {
        return;
      }
      this.storage.setOrCreate<UIContext>("uiContext", windowStage.getMainWindowSync().getUIContext());
    });
  }
}
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
// DynamicComponent.ets
import { UIContext, LocalStorage, WrappedBuilder, wrapBuilder, Builder } from '@kit.ArkUI';
import { NodeController, BuilderNode, FrameNode } from '@ohos.arkui.node';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { injectWebview } from "./InjectWebview";

export class BuilderData {
  url: string;
  controller: webview.WebviewController;
  context: UIContext;

  constructor(url: string, controller: webview.WebviewController, context: UIContext) {
    this.url = url;
    this.controller = controller;
    this.context = context;
  }
}

let storage : LocalStorage | undefined = undefined;

type MyBuilder = @Builder (p1: BuilderData) => void;

export class NodeControllerImpl extends NodeController {
  private rootNode: BuilderNode<BuilderData> | null = null;
  private wrappedBuilder: WrappedBuilder<MyBuilder> | null = null;

  constructor(wrappedBuilder: WrappedBuilder<MyBuilder>, context: UIContext) {
    super();
    storage = context.getSharedLocalStorage();
    this.wrappedBuilder = wrappedBuilder;
  }

  makeNode(uiContext: UIContext): FrameNode | null {
    if (this.rootNode != null) {
      return this.rootNode!.getFrameNode();
    }
    return null;
  }

  initWeb(url: string, controller: webview.WebviewController) {
    if(this.rootNode != null) {
      return;
    }

    const uiContext: UIContext = storage!.get<UIContext>("uiContext") as UIContext;
    if (!uiContext) {
      return;
    }
    this.rootNode = new BuilderNode<BuilderData>(uiContext);
    this.rootNode!.build(injectWebview, new BuilderData(url, controller, uiContext));
  }
}

export const createNode = (wrappedBuilder: WrappedBuilder<MyBuilder>, data: BuilderData) => {
  const baseNode = new NodeControllerImpl(wrappedBuilder, data.context);
  baseNode.initWeb(data.url, data.controller);
  return baseNode;
}
```

ArkTS-Dyn示例：

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

  // 读取配置，从rawfile目录中读取文件内容
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

ArkTS-Sta示例：

```TypeScript
'use static'
// InjectWebview.ets
import { UIContext, WrappedBuilder, wrapBuilder, Web, Builder } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { resourceConfigs } from "./Resource";
import { BuilderData } from "./DynamicComponent";

@Builder
export function WebBuilder(data: BuilderData) {
  Web({ src: data.url, controller: data.controller })
    .onControllerAttached(() => {
      (async () => {
        try {
          const result = await getData(data.context);
          data.controller.injectOfflineResources(result);
        } catch (err) {
          console.error("error: " + err.code + " " + err.message);
        }
      })();
    })
    .fileAccess(true)
}

type MyBuilder = @Builder (p1: BuilderData) => void;
export const injectWebview : WrappedBuilder<MyBuilder> = wrapBuilder(WebBuilder);

export async function getData(context: UIContext): Promise<Array<webview.OfflineResourceMap>> {
  const resourceMapArr: Array<webview.OfflineResourceMap> = [];

  // 读取配置，从rawfile目录中读取文件内容。
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

async function readRawFile(path: string, context: UIContext): Promise<Uint8Array> {
  try {
    return await context.getHostContext()!.resourceManager.getRawFileContent(path);
  } catch (err) {
    return new Uint8Array(0);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
// BusinessWebview.ets
import { BuilderData } from "./DynamicComponent";

@Builder
function WebBuilder(data: BuilderData) {
  // 此处组件可根据业务需要自行扩展
  Web({ src: data.url, controller: data.controller })
    .cacheMode(CacheMode.Default)
}

export const businessWebview = wrapBuilder<BuilderData[]>(WebBuilder);
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { BuilderData } from "./DynamicComponent";
import { WrappedBuilder, wrapBuilder, Web, Builder } from '@kit.ArkUI';

@Builder
function WebBuilder(data: BuilderData) {
  // 此处组件可根据业务需要自行扩展。
  Web({ src: data.url, controller: data.controller })
  // .cacheMode(CacheMode.Default)
}
type MyBuilder = @Builder (p1: BuilderData) => void;
export const businessWebview : WrappedBuilder<MyBuilder> = wrapBuilder(WebBuilder);
```

ArkTS-Dyn示例：

```TypeScript
// Resource.ets
import { webview } from '@kit.ArkWeb';

export interface ResourceConfig {
  urlList: Array<string>,
  type: webview.OfflineResourceType,
  responseHeaders: Array<Header>,
  localPath: string, // 本地资源存放在rawfile目录下的路径
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
    urlList: [ // 仅提供一个URL，这个URL既作为资源的源，也作为资源的网络请求地址
      "https://www.example.com/example.js",
    ],
    type: webview.OfflineResourceType.CLASSIC_JS,
    responseHeaders: [
      // 以<script crossorigin="anonymous" />方式使用，提供额外的响应头
      { headerKey: "Cross-Origin", headerValue:"anonymous" }
    ]
  },
];
```

ArkTS-Sta示例：

```TypeScript
'use static'
// Resource.ets
import { webview } from '@kit.ArkWeb';

export interface ResourceConfig {
  urlList: Array<string>,
  type: webview.OfflineResourceType,
  responseHeaders: Array<webview.WebHeader>,
  localPath: string, // 本地资源存放在rawfile目录下的路径。
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
    urlList: [ // 仅提供一个URL，这个URL既作为资源的源，也作为资源的网络请求地址。
      "https://www.example.com/example.js",
    ],
    type: webview.OfflineResourceType.CLASSIC_JS,
    responseHeaders: [
      // 以<script crossorigin="anonymous" />方式使用，提供额外的响应头。
      { headerKey: "Cross-Origin", headerValue:"anonymous" }
    ]
  },
];
```

ArkTS-Dyn示例：

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
    // 初始化用于注入本地资源的Web组件, 提供一个空的html页面作为URL即可
    this.injectNode = createNode(injectWebview,
        { url: "https://www.example.com/empty.html", controller: this.injectController, context: this.getUIContext()});
  }

  build() {
    Column() {
      // 在适当的时机加载业务用Web组件，本例以Button点击触发为例
      Button("加载页面")
        .onClick(() => {
          this.businessNode = createNode(businessWebview, {
            url: "https://www.example.com/business.html",
            controller: this.businessController,
            context: this.getUIContext()
          });
        })
      // 用于业务的Web组件
      NodeContainer(this.businessNode);
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
// Index.ets
import { webview } from '@kit.ArkWeb';
import { Button, Column, Entry, Component, State, NodeContainer } from '@kit.ArkUI';
import { NodeController } from '@ohos.arkui.node';
import { createNode, BuilderData } from "./DynamicComponent";
import { injectWebview } from "./InjectWebview";
import { businessWebview } from "./BusinessWebview";

@Entry
@Component
struct Index {
  @State injectNode: NodeController | undefined = undefined;
  injectController: webview.WebviewController = new webview.WebviewController();

  @State businessNode: NodeController | undefined = undefined;
  businessController: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    // 初始化用于注入本地资源的Web组件, 提供一个空的html页面作为URL即可。
    this.injectNode = createNode(injectWebview,
      new BuilderData( "https://www.example.com/empty.html", this.injectController, this.getUIContext()));
  }

  build() {
    Column() {
      // 在适当的时机加载业务用Web组件，本例以Button点击触发为例。
      Button("加载页面")
        .onClick(() => {
          this.businessNode = createNode(businessWebview, new BuilderData(
            "https://www.example.com/business.html",
            this.businessController,
            this.getUIContext()
          ));
        })
      // 用于业务的Web组件。
      NodeContainer(this.businessNode!);
    }
  }
}
```

加载的HTML网页示例。

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

判断当前系统是否正在使用常青内核，即系统的最新内核。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static isActiveWebEngineEvergreen(): boolean--><!--Device-WebviewController-static isActiveWebEngineEvergreen(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示是否正在使用常青内核。正在使用返回true，否则返回false。 |

**示例**

本示例以EntryAbility为例，实现了在Ability创建阶段判断应用是否正在使用常青内核的功能。

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

本示例以EntryAbility为例，实现了在Ability创建阶段判断应用是否正在使用常青内核的功能。

```TypeScript
// xxx.ets
import UIAbility from '@ohos.app.ability.UIAbility';
import Want from '@ohos.app.ability.Want';
import AbilityConstant from '@ohos.app.ability.AbilityConstant';
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-isAdsBlockEnabled(): boolean--><!--Device-WebviewController-isAdsBlockEnabled(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if the ability of AdsBlock is enabled; else false. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) | Capability not supported. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-isAdsBlockEnabledForCurPage(): boolean--><!--Device-WebviewController-isAdsBlockEnabledForCurPage(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if the ability of AdsBlock is enabled for current Webpage; else false. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) | Capability not supported. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static isAutoPreconnectEnabled(): boolean--><!--Device-WebviewController-static isAutoPreconnectEnabled(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Return true if enabled, false if disabled. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Column, Button } from '@ohos.arkui.component'
import { BusinessError } from '@ohos.base'
import { webview } from '@kit.ArkWeb';

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-isIncognitoMode(): boolean--><!--Device-WebviewController-isIncognitoMode(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | { |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-isIntelligentTrackingPreventionEnabled(): boolean--><!--Device-WebviewController-isIntelligentTrackingPreventionEnabled(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if enable the Intelligent Tracking Prevention; else false. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |
| [801](../../errorcode-universal.md#801-该设备不支持此api) | Capability not supported. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static isPrivateNetworkAccessEnabled(): boolean--><!--Device-WebviewController-static isPrivateNetworkAccessEnabled(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True is enable the ability to check private network access else false. |

**示例**

ArkTS-Dyn示例：

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
          // 设置为false时ArkWeb将不再检查私有网络请求是否合法
          webview.WebviewController.enablePrivateNetworkAccess(false);
        })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { webview } from '@kit.ArkWeb';
import { Entry, Column, Component, Button, Web } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
          // 设置为false时ArkWeb将不再检查私有网络请求是否合法
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-isSafeBrowsingEnabled(): boolean--><!--Device-WebviewController-isSafeBrowsingEnabled(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if enable the ability to check website security risks else false. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-loadData(data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string): void--><!--Device-WebviewController-loadData(data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 | A string encoded according to "Base64" or "URL". |
| mimeType | string | 是 | Media type. For example: "text/html". |
| encoding | string | 是 | Encoding type. For example: "UTF-8". |
| baseUrl | string | 否 | A specified URL path ("http"/"https"/"data" protocol), which is assigned to window.origin by the Web component. |
| historyUrl | string | 否 | History URL. When it is not empty, it can be managed by history records to realize the back and forth function. This property is invalid when baseUrl is empty. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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
      Button('loadData')
        .onClick(() => {
          try {
            this.controller.loadData(
              "<html><body bgcolor=\"white\">Source:<pre>source</pre></body></html>",
              "text/html",
              // UTF-8为charset。
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
      Button('loadData')
        .onClick(() => {
          try {
            this.controller.loadData(
              "<html><body bgcolor=\"white\">Source:<pre>source</pre></body></html>",
              "text/html",
              // UTF-8为charset。
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

Ark-Dyn示例：

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
              // Coding tests通过base64编码后的字符串。
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

Ark-Sta示例：

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
      Button('loadData')
        .onClick(() => {
          try {
            this.controller.loadData(
              // Coding tests通过base64编码后的字符串。
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

Ark-Dyn示例：

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
              "<img src=aa/bb.jpg>", // 会尝试从"https://xxx.com/" + "aa/bb.jpg"加载该图片
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
      Button('loadData')
        .onClick(() => {
          try {
            this.controller.loadData(
              "<img src=aa/bb.jpg>", // 会尝试从"https://xxx.com/" + "aa/bb.jpg"加载该图片
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

Ark-Dyn示例：

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  updateContent: string = '<body><div><image src="resource://rawfile/xxx.png" alt="image -- end" width="500" height="250"></image></div></body>'

  build() {
    Column() {
      Button('loadData')
        .onClick(() => {
          try {
            // UTF-8为charset。
            this.controller.loadData(this.updateContent, "text/html", "UTF-8", " ", " ");
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
  updataContent: string = '<body><div><image src=resource://rawfile/xxx.png alt="image -- end" width="500" height="250"></image></div></body>'

  build() {
    Column() {
      Button('loadData')
        .onClick(() => {
          try {
            // UTF-8为charset。
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

加载沙箱图片。

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
              "<img src=bb.jpg>", // 尝试从"file:///xxx/" + "bb.jpg"加载该图片。
              "text/html",
              "UTF-8",
              // 加载本地应用沙箱内的图片路径，请将路径改为实际使用的沙箱路径。
              "file:///data/storage/el2/base/haps/entry/files/data/.cache_dir/",
              ""
            );
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .fileAccess(true) // 为了加载应用沙箱内的图片，需要启用文件访问功能。 
    }
  }
}
```

## loadUrl

```TypeScript
loadUrl(url: string | Resource, headers?: Array<WebHeader>): void
```

Loads the data or URL.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-loadUrl(url: string | Resource, headers?: Array<WebHeader>): void--><!--Device-WebviewController-loadUrl(url: string | Resource, headers?: Array<WebHeader>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 | The URL to load. |
| headers | Array&lt;WebHeader&gt; | 否 | Additional HTTP request header for URL. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-url格式错误) | URL error. The webpage corresponding to the URL is invalid. |
| [17100003](../../apis-arkweb/errorcode-webview.md#17100003-resource路径错误) | Invalid resource path or file type. |

**示例**

ArkTs-Dyn示例：

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
            // 需要加载的URL是string类型。
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

ArkTs-Sta示例：

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
      Button('loadUrl')
        .onClick(() => {
          try {
            // 需要加载的URL是string类型。
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
      Button('loadUrl')
        .onClick(() => {
          try {
            // 带参数headers。
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

ArkTs-Sta示例：

```TypeScript
// xxx.ets
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
      Button('loadUrl')
        .onClick(() => {
          try {
            // 带参数headers。
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
      Button('loadUrl')
        .onClick(() => {
          try {
            // 通过$rawfile加载本地资源文件。
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

ArkTS-Sta示例：

```TypeScript
'use static'
import { Web, Column, Component, Entry, Button, $rawfile } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@ohos.base';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Button('loadUrl')
        .onClick(() => {
          try {
            // 通过$rawfile加载本地资源文件。
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
      Button('loadUrl')
        .onClick(() => {
          try {
            // 通过resource协议加载本地资源文件。
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
      Button('loadUrl')
        .onClick(() => {
          try {
            // 通过resource协议加载本地资源文件。
            this.controller.loadUrl("resource://rawfile/index.html");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

在“srcmainresourcesrawfile”文件夹下创建index.html：

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

  // 加载界面
  window.addEventListener('load', loadContent);

  // 当hash变化时，更新界面
  window.addEventListener('hashchange', loadContent);
</script>
</body>
</html>
```

加载的html文件。

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-offControllerAttachStateChange(callback?: Callback<ControllerAttachState>): void--><!--Device-WebviewController-offControllerAttachStateChange(callback?: Callback<ControllerAttachState>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ControllerAttachState](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-controllerattachstate-e.md)&gt; | 否 | Callback used to return the controller attach state. |

**示例**

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import { Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  // 构建回调函数。
  handleControllerAttachStateChange: Callback<webview.ControllerAttachState> = (state: webview.ControllerAttachState): void => {
    if (state == webview.ControllerAttachState.UNATTACHED) {
      console.info('handleControllerAttachStateChange: Controller is unattached.');
    } else {
      console.info('handleControllerAttachStateChange: Controller is attached.');
    }
  };
  aboutToAppear() {
    try {
      this.controller.onControllerAttachStateChange(this.handleControllerAttachStateChange);
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }
    try {
      // 注册回调以接收controller绑定状态更改通知。
      this.controller.onControllerAttachStateChange((state: webview.ControllerAttachState) => {
        if (state == webview.ControllerAttachState.UNATTACHED) {
          console.info('Controller is unattached.');
        } else {
          console.info('Controller is attached.');
        }
      })
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }
  }
  aboutToDisappear() {
    // 取消指定注册回调。
    // this.controller.offControllerAttachStateChange(this.handleControllerAttachStateChange);
    // 取消所有注册回调。
    this.controller.offControllerAttachStateChange();
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## onActive

```TypeScript
onActive(): void
```

Call this interface to notify the Web component to enter the foreground activation state. The activation state is the state in which the application interacts with the user. The application will remain in this state until something happens, such as receiving an incoming call or closing the screen of the device, to shift the focus away from the application.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-onActive(): void--><!--Device-WebviewController-onActive(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import { Web, Button, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-onControllerAttachStateChange(callback: Callback<ControllerAttachState>): void--><!--Device-WebviewController-onControllerAttachStateChange(callback: Callback<ControllerAttachState>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ControllerAttachState](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-controllerattachstate-e.md)&gt; | 是 | Callback used to return the controller attach state. |

**示例**

请参考[offControllerAttachStateChange](#offcontrollerattachstatechange)。

## onCreateNativeMediaPlayer

```TypeScript
onCreateNativeMediaPlayer(callback: CreateNativeMediaPlayerCallback): void
```

注册回调函数，开启 [应用接管网页媒体播放功能](../../../reference/apis-arkweb/arkts-basic-components-web-attributes.md#enablenativemediaplayer12) 后，当网页中有播放媒体时，触发注册的回调函数。

如果应用接管网页媒体播放功能未开启，则注册的回调函数不会被触发。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-onCreateNativeMediaPlayer(callback: CreateNativeMediaPlayerCallback): void--><!--Device-WebviewController-onCreateNativeMediaPlayer(callback: CreateNativeMediaPlayerCallback): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [CreateNativeMediaPlayerCallback](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-createnativemediaplayercallback-t.md) | 是 | 接管网页媒体播放的回调函数。 |

**示例**

ArkTS-Dyn示例：

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

class ActualNativeMediaPlayerListener {
  handler: webview.NativeMediaPlayerHandler;

  constructor(handler: webview.NativeMediaPlayerHandler) {
    this.handler = handler;
  }

  onPlaying() {
    // 本地播放器开始播放。
    this.handler.handleStatusChanged(webview.PlaybackStatus.PLAYING);
  }
  onPaused() {
    // 本地播放器暂停播放。
    this.handler.handleStatusChanged(webview.PlaybackStatus.PAUSED);
  }
  onSeeking() {
    // 本地播放器开始执行跳转到目标时间点。
    this.handler.handleSeeking();
  }
  onSeekDone() {
    // 本地播放器 seek 完成。
    this.handler.handleSeekFinished();
  }
  onEnded() {
    // 本地播放器播放完成。
    this.handler.handleEnded();
  }
  onVolumeChanged() {
    // 获取本地播放器的音量。
    let volume: number = getVolume();
    this.handler.handleVolumeChanged(volume);
  }
  onCurrentPlayingTimeUpdate() {
    // 更新播放时间。
    let currentTime: number = getCurrentPlayingTime();
    // 将时间单位换算成秒。
    let currentTimeInSeconds = convertToSeconds(currentTime);
    this.handler.handleTimeUpdate(currentTimeInSeconds);
  }
  onBufferedChanged() {
    // 缓存发生了变化。
    // 获取本地播放器的缓存时长。
    let bufferedEndTime: number = getCurrentBufferedTime();
    // 将时间单位换算成秒。
    let bufferedEndTimeInSeconds = convertToSeconds(bufferedEndTime);
    this.handler.handleBufferedEndTimeChanged(bufferedEndTimeInSeconds);

    // 检查缓存状态。
    // 如果缓存状态发生了变化，则向 ArkWeb 内核通知缓存状态。
    let lastReadyState: webview.ReadyState = getLastReadyState();
    let currentReadyState:  webview.ReadyState = getCurrentReadyState();
    if (lastReadyState != currentReadyState) {
      this.handler.handleReadyStateChanged(currentReadyState);
    }
  }
  onEnterFullscreen() {
    // 本地播放器进入了全屏状态。
    let isFullscreen: boolean = true;
    this.handler.handleFullscreenChanged(isFullscreen);
  }
  onExitFullscreen() {
    // 本地播放器退出了全屏状态。
    let isFullscreen: boolean = false;
    this.handler.handleFullscreenChanged(isFullscreen);
  }
  onUpdateVideoSize(width: number, height: number) {
    // 当本地播放器解析出视频宽高时， 通知 ArkWeb 内核。
    this.handler.handleVideoSizeChanged(width, height);
  }
  onDurationChanged(duration: number) {
    // 本地播放器解析到了新的媒体时长， 通知 ArkWeb 内核。
    this.handler.handleDurationChanged(duration);
  }
  onError(error: webview.MediaError, errorMessage: string) {
    // 本地播放器出错了，通知 ArkWeb 内核。
    this.handler.handleError(error, errorMessage);
  }
  onNetworkStateChanged(state: webview.NetworkState) {
    // 本地播放器的网络状态发生了变化， 通知 ArkWeb 内核。
    this.handler.handleNetworkStateChanged(state);
  }
  onPlaybackRateChanged(playbackRate: number) {
    // 本地播放器的播放速率发生了变化， 通知 ArkWeb 内核。
    this.handler.handlePlaybackRateChanged(playbackRate);
  }
  onMutedChanged(muted: boolean) {
    // 本地播放器的静音状态发生了变化， 通知 ArkWeb 内核。
    this.handler.handleMutedChanged(muted);
  }

  // ... 监听本地播放器其他的状态 ...
}

class NativeMediaPlayerImpl implements webview.NativeMediaPlayerBridge {
  constructor(handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo) {
    // 1. 创建一个本地播放器的状态监听。
    let listener: ActualNativeMediaPlayerListener = new ActualNativeMediaPlayerListener(handler);
    // 2. 创建一个本地播放器。
    // 3. 监听该本地播放器。
    // ...
  }

  updateRect(x: number, y: number, width: number, height: number) {
    // <video> 标签的位置和大小发生了变化。
    // 根据该信息变化，作出相应的改变。
  }

  play() {
    // 启动本地播放器播放。
  }

  pause() {
    // 暂停本地播放器播放。
  }

  seek(targetTime: number) {
    // 本地播放器跳转到指定的时间点。
  }

  release() {
    // 销毁本地播放器。
  }

  setVolume(volume: number) {
    // ArkWeb 内核要求调整本地播放器的音量。
    // 设置本地播放器的音量。
  }

  setMuted(muted: boolean) {
    // 将本地播放器静音或取消静音。
  }

  setPlaybackRate(playbackRate: number) {
    // 调整本地播放器的播放速度。
  }

  enterFullscreen() {
    // 将本地播放器设置为全屏播放。
  }

  exitFullscreen() {
    // 将本地播放器退出全屏播放。
  }

  resumePlayer() {
    // 重新创建应用内播放器。
    // 恢复应用内播放器的状态信息。
  }

  suspendPlayer(type: webview.SuspendType) {
    // 记录应用内播放器的状态信息。
    // 销毁应用内播放器。
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
              // 本地播放器不接管该媒体。
              // ArkWeb 内核将用自己的播放器来播放该媒体。
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Observed, State, AppStorage, ObjectLink } from '@kit.ArkUI';
import { XComponent, XComponentType, XComponentController, Text, Alignment, Resource, ForEach, Area, XComponentOptions,
  TouchEvent, Stack, Entry, Color, Component, Column, Row, Button, VideoController, Builder, Web, wrapBuilder,
  FrameNode, NodeContainer, FlexAlign } from '@kit.ArkUI';
import { NodeController, NodeRenderType, BuilderNode } from '@ohos.arkui.node';
import { webview } from '@kit.ArkWeb';
import { UIContext } from '@kit.ArkUI';

class ActualNativeMediaPlayerListener {
  handler: webview.NativeMediaPlayerHandler;

  constructor(handler: webview.NativeMediaPlayerHandler) {
    this.handler = handler;
  }

  onPlaying() {
    // 本地播放器开始播放。
    this.handler.handleStatusChanged(webview.PlaybackStatus.PLAYING);
  }
  onPaused() {
    // 本地播放器暂停播放。
    this.handler.handleStatusChanged(webview.PlaybackStatus.PAUSED);
  }
  onSeeking() {
    // 本地播放器开始执行跳转到目标时间点。
    this.handler.handleSeeking();
  }
  onSeekDone() {
    // 本地播放器 seek 完成。
    this.handler.handleSeekFinished();
  }
  onEnded() {
    // 本地播放器播放完成。
    this.handler.handleEnded();
  }
  onVolumeChanged() {
    // 获取本地播放器的音量。
    let volume: number = getVolume();
    this.handler.handleVolumeChanged(volume);
  }
  onCurrentPlayingTimeUpdate() {
    // 更新播放时间。
    let currentTime: number = getCurrentPlayingTime();
    // 将时间单位换算成秒。
    let currentTimeInSeconds = convertToSeconds(currentTime);
    this.handler.handleTimeUpdate(currentTimeInSeconds);
  }
  onBufferedChanged() {
    // 缓存发生了变化。
    // 获取本地播放器的缓存时长。
    let bufferedEndTime: number = getCurrentBufferedTime();
    // 将时间单位换算成秒。
    let bufferedEndTimeInSeconds = convertToSeconds(bufferedEndTime);
    this.handler.handleBufferedEndTimeChanged(bufferedEndTimeInSeconds);

    // 检查缓存状态。
    // 如果缓存状态发生了变化，则向 ArkWeb 内核通知缓存状态。
    let lastReadyState: webview.ReadyState = getLastReadyState();
    let currentReadyState:  webview.ReadyState = getCurrentReadyState();
    if (lastReadyState != currentReadyState) {
      this.handler.handleReadyStateChanged(currentReadyState);
    }
  }
  onEnterFullscreen() {
    // 本地播放器进入了全屏状态。
    let isFullscreen: boolean = true;
    this.handler.handleFullscreenChanged(isFullscreen);
  }
  onExitFullscreen() {
    // 本地播放器退出了全屏状态。
    let isFullscreen: boolean = false;
    this.handler.handleFullscreenChanged(isFullscreen);
  }
  onUpdateVideoSize(width: number, height: number) {
    // 当本地播放器解析出视频宽高时， 通知 ArkWeb 内核。
    this.handler.handleVideoSizeChanged(width, height);
  }
  onDurationChanged(duration: number) {
    // 本地播放器解析到了新的媒体时长， 通知 ArkWeb 内核。
    this.handler.handleDurationChanged(duration);
  }
  onError(error: webview.MediaError, errorMessage: string) {
    // 本地播放器出错了，通知 ArkWeb 内核。
    this.handler.handleError(error, errorMessage);
  }
  onNetworkStateChanged(state: webview.NetworkState) {
    // 本地播放器的网络状态发生了变化， 通知 ArkWeb 内核。
    this.handler.handleNetworkStateChanged(state);
  }
  onPlaybackRateChanged(playbackRate: number) {
    // 本地播放器的播放速率发生了变化， 通知 ArkWeb 内核。
    this.handler.handlePlaybackRateChanged(playbackRate);
  }
  onMutedChanged(muted: boolean) {
    // 本地播放器的静音状态发生了变化， 通知 ArkWeb 内核。
    this.handler.handleMutedChanged(muted);
  }

  // ... 监听本地播放器其他的状态 ...
}

class NativeMediaPlayerImpl implements webview.NativeMediaPlayerBridge {
  constructor(handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo) {
    // 1. 创建一个本地播放器的状态监听。
    let listener: ActualNativeMediaPlayerListener = new ActualNativeMediaPlayerListener(handler);
    // 2. 创建一个本地播放器。
    // 3. 监听该本地播放器。
    // ...
  }

  updateRect: webview.UpdateRectFn = (x: double, y: double, width: double, height: double) : void=> {
    // <video> 标签的位置和大小发生了变化。
    // 根据该信息变化，作出相应的改变。
  }

  play: webview.ZeroParamFn = () : void=> {
    // 启动本地播放器播放。
  }

  pause: webview.ZeroParamFn = () : void=> {
    // 暂停本地播放器播放。
  }

  seek: webview.OneParamFn<double> = (targetTime: double) : void=> {
    // 本地播放器跳转到指定的时间点。
  }

  release: webview.ZeroParamFn = () : void=> {
    // 销毁本地播放器。
  }

  setVolume: webview.OneParamFn<double> = (volume: double) : void=> {
    // ArkWeb 内核要求调整本地播放器的音量。
    // 设置本地播放器的音量。
  }

  setMuted: webview.OneParamFn<boolean> = (muted: boolean) : void=> {
    // 将本地播放器静音或取消静音。
  }

  setPlaybackRate: webview.OneParamFn<double> = (playbackRate: double) : void=> {
    // 调整本地播放器的播放速度。
  }

  enterFullscreen: webview.ZeroParamFn = () : void=> {
    // 将本地播放器设置为全屏播放。
  }

  exitFullscreen: webview.ZeroParamFn = () : void=> {
    // 将本地播放器退出全屏播放。
  }

  resumePlayer?: webview.ResumePlayerFn = () : void=> {
    // 重新创建应用内播放器。
    // 恢复应用内播放器的状态信息。
  }

  suspendPlayer?: webview.SuspendPlayerFn = (type: webview.SuspendType) : void=> {
    // 记录应用内播放器的状态信息。
    // 销毁应用内播放器。
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined)
  build() {
    Column(undefined) {
      Web({ src: 'www.example.com', controller: this.controller })
        .enableNativeMediaPlayer({enable: true, shouldOverlay: false})
        .onControllerAttached((): void => {
          this.controller.onCreateNativeMediaPlayer((handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo): webview.NativeMediaPlayerBridge => {
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

Call this interface to notify the Web component to enter the inactive state. In this callback, the developer can realize the appropriate behavior when the application loses focus. In this state, any content that can be safely paused will be paused as much as possible, such as animation and geographical location. However, JavaScript will not be paused. To pause JavaScript globally, please use [pauseAllTimers](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#pausealltimers).To reactivate the Web component, call onActive.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-onInactive(): void--><!--Device-WebviewController-onInactive(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import { Web, Button, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-pageDown(bottom: boolean): void--><!--Device-WebviewController-pageDown(bottom: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bottom | boolean | 是 | Whether to jump to the bottom of the page, if set to false, the page content will scroll down half the size of the view frame, and when set to true, it will jump to the bottom of the page. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, Button, $rawfile } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

加载的html文件。

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
         text-align: center;       /* 水平居中 */
         line-height: 200px;       /* 垂直居中（值等于容器高度） */
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-pageUp(top: boolean): void--><!--Device-WebviewController-pageUp(top: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| top | boolean | 是 | Whether to jump to the top of the page, if set to false, the page content will scroll up half the size of the view frame, and when set to true, it will jump to the top of the page. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, Button, $rawfile } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
         text-align: center;       /* 水平居中 */
         line-height: 200px;       /* 垂直居中（值等于容器高度） */
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

控制网页所有音视频暂停。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-pauseAllMedia(): void--><!--Device-WebviewController-pauseAllMedia(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static pauseAllTimers(): void--><!--Device-WebviewController-static pauseAllTimers(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Entry, Column, Row, Component, Button, Web } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

加载的html文件。

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

暂停当前网页麦克风捕获。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-pauseMicrophone(): void--><!--Device-WebviewController-pauseMicrophone(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

完整示例代码参考[resumeMicrophone](#resumemicrophone)。

## postMessage

```TypeScript
postMessage(name: string, ports: Array<WebMessagePort>, uri: string): void
```

Post web message port to html

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-postMessage(name: string, ports: Array<WebMessagePort>, uri: string): void--><!--Device-WebviewController-postMessage(name: string, ports: Array<WebMessagePort>, uri: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | Data name information to send. |
| ports | Array&lt;[WebMessagePort](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-webmessageport-i.md)&gt; | 是 | Port number array information to send. |
| uri | string | 是 | URI to receive this information. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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
  ports: webview.WebMessagePort[] = [];
  @State sendFromEts: string = 'Send this message from ets to HTML';
  @State receivedFromHtml: string = 'Display received message send from HTML';

  build() {
    Column() {
      // 展示接收到的来自HTML的内容
      Text(this.receivedFromHtml)
      // 输入框的内容发送到html
      TextInput({ placeholder: 'Send this message from ets to HTML' })
        .onChange((value: string) => {
          this.sendFromEts = value;
        })

      Button('postMessage')
        .onClick(() => {
          try {
            // 1、创建两个消息端口。
            this.ports = this.controller.createWebMessagePorts();
            // 2、在应用侧的消息端口(如端口1)上注册回调事件。
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
            // 3、将另一个消息端口(如端口0)发送到HTML侧，由HTML侧保存并使用。
            this.controller.postMessage('__init_port__', [this.ports[0]], '*');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })

      // 4、使用应用侧的端口给另一个已经发送到html的端口发送消息。
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { Web, Column, Component, Entry, State, Text, Button, $rawfile, TextInput } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  ports: webview.WebMessagePort[] =[] as webview.WebMessagePort[];
  @State sendFromEts: string = 'Send this message from ets to HTML';
  @State receivedFromHtml: string = 'Display received message send from HTML';

  build() {
    Column() {
      // 展示接收到的来自HTML的内容。
      Text(this.receivedFromHtml)
      // 输入框的内容发送到html。
      TextInput({ placeholder: 'Send this message from ets to HTML' })
        .onChange((value: string) => {
          this.sendFromEts = value;
        })

      Button('postMessage')
        .onClick(() => {
          try {
            // 1、创建两个消息端口。
            this.ports = this.controller.createWebMessagePorts();
            // 2、在应用侧的消息端口(如端口1)上注册回调事件。
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
            // 3、将另一个消息端口(如端口0)发送到HTML侧，由HTML侧保存并使用。
            this.controller.postMessage('__init_port__', [this.ports[0]], '*');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })

      // 4、使用应用侧的端口给另一个已经发送到html的端口发送消息。
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

加载的html文件。

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
            h5Port = event.ports[0]; // 1. 保存从ets侧发送过来的端口
            h5Port.onmessage = function (event) {
              // 2. 接收ets侧发送过来的消息.
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

// 3. 使用h5Port往ets侧发送消息.
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-postUrl(url: string, postData: ArrayBuffer): void--><!--Device-WebviewController-postUrl(url: string, postData: ArrayBuffer): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | Request the URL use "POST" method. |
| postData | ArrayBuffer | 是 | This data will passed to "POST" request. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-url格式错误) | URL error. The webpage corresponding to the URL is invalid. |

**示例**

ArkTS-Dyn示例：

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
            // 数据转化为ArrayBuffer类型。
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

ArkTS-Sta示例：

```TypeScript
'use static'
import { Web, Column, Component, Entry, Button, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@ohos.base';


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
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State testObjtest: TestObj = new TestObj();

  build() {
    Column() {
      Button('postUrl')
        .onClick(() => {
          try {
            // 数据转化为ArrayBuffer类型。
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-precompileJavaScript(url: string, script: string | Uint8Array, cacheOptions: CacheOptions): Promise<int>--><!--Device-WebviewController-precompileJavaScript(url: string, script: string | Uint8Array, cacheOptions: CacheOptions): Promise<int>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | Url of the javascript. Only support HTTP/HTTPS protocol and length no longer than 2048. |
| script | string \| Uint8Array | 是 | Javascript source code. script must not be empty. |
| cacheOptions | [CacheOptions](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-cacheoptions-i.md) | 是 | Generate code cache option. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;int&gt; | The promise returned by the function. 0 means generate code cache successfully, -1 means internal error. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Invalid input parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
// EntryAbility.ets
import { UIAbility, Want, AbilityConstant} from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { UIContext, LocalStorage, window } from '@kit.ArkUI';

const localStorage: LocalStorage = new LocalStorage('uiContext');

class EntryAbility extends UIAbility {
  storage: LocalStorage = localStorage;

  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.loadContent('pages/Index', this.storage, (err: BusinessError<void> | null, data): void => {
      if (err && err.code) {
        return;
      }
      this.storage.setOrCreate<UIContext>("uiContext", windowStage.getMainWindowSync().getUIContext());
    });
  }
}
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
// DynamicComponent.ets
import { UIContext, LocalStorage, WrappedBuilder, wrapBuilder, Builder } from '@kit.ArkUI';
import { NodeController, BuilderNode, FrameNode } from '@ohos.arkui.node';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { WebBuilder } from "./PrecompileWebview";
let storage : LocalStorage | undefined = undefined;

export class BuilderData {
  url: string;
  controller: webview.WebviewController;
  context: UIContext;

  constructor(url: string, controller: webview.WebviewController, context: UIContext) {
    this.url = url;
    this.controller = controller;
    this.context = context;
  }
}

type MyBuilder = @Builder (p1: BuilderData) => void;

export class NodeControllerImpl extends NodeController {
  private rootNode: BuilderNode<BuilderData> | null = null;
  // private wrappedBuilder: WrappedBuilder<@Builder ((p1: BuilderData) => void)> | null = null;

  private wrappedBuilder: WrappedBuilder<MyBuilder> | null = null;
  constructor(wrappedBuilder: WrappedBuilder<MyBuilder>, context: UIContext) {
    super();
    storage = context.getSharedLocalStorage();
    this.wrappedBuilder = wrappedBuilder;
  }

  makeNode(uiContext: UIContext): FrameNode | null {
    if (this.rootNode != null) {
      return this.rootNode!.getFrameNode();
    }
    return null;
  }

  initWeb(url: string, controller: webview.WebviewController) {
    if(this.rootNode != null) {
      return;
    }

    const uiContext: UIContext = storage!.get<UIContext>("uiContext") as UIContext;
    if (!uiContext) {
      return;
    }
    this.rootNode = new BuilderNode<BuilderData>(uiContext);
    this.rootNode!.build(wrapBuilder(WebBuilder), new BuilderData(url, controller, uiContext));
  }
}

export const createNode = (wrappedBuilder: WrappedBuilder<MyBuilder>, data: BuilderData) => {
  const baseNode = new NodeControllerImpl(wrappedBuilder, data.context);
  baseNode.initWeb(data.url, data.controller);
  return baseNode;
}
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
// PrecompileWebview.ets
import { UIContext, WrappedBuilder, wrapBuilder, Web, Builder } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BuilderData } from "./DynamicComponent";
import { Config, configs } from "./PrecompileConfig";
import { BusinessError } from '@kit.BasicServicesKit';

@Builder
export function WebBuilder(data: BuilderData) {
  Web({ src: data.url, controller: data.controller })
    .onControllerAttached(() => {
      precompile(data.controller, configs, data.context);
    })
    .fileAccess(true)
}
type MyBuilder = @Builder (p1: BuilderData) => void;
export const precompileWebview : WrappedBuilder<MyBuilder> = wrapBuilder(WebBuilder);

export const precompile = async (controller: webview.WebviewController, configs: Array<Config>, context: UIContext) => {
  for (const config of configs) {
    let content = await readRawFile(config.localPath, context);

    try {
      controller.precompileJavaScript(config.url, content, config.options)
        .then(errCode => {
          console.error("precompile successfully! " + errCode);
        }).catch((errCode: Error) => {
        console.error("precompile failed. " + errCode);
      });
    } catch (err:BusinessError) {
      console.error("precompile failed. " + err.code + " " + err.message);
    }
  }
}

async function readRawFile(path: string, context: UIContext): Promise<Uint8Array> {
  try {
    return await context.getHostContext()!.resourceManager.getRawFileContent(path);
  } catch (err) {
    return new Uint8Array(0);
  }
}
```

ArkTS-Dyn示例：

```TypeScript
// BusinessWebview.ets
import { BuilderData } from "./DynamicComponent";

@Builder
function WebBuilder(data: BuilderData) {
  // 此处组件可根据业务需要自行扩展
  Web({ src: data.url, controller: data.controller })
    .cacheMode(CacheMode.Default)
}

export const businessWebview = wrapBuilder<BuilderData[]>(WebBuilder);
```

ArkTS-Sta示例：

```TypeScript
'use static'
// BusinessWebview.ets
import { BuilderData } from "./DynamicComponent";
import { WrappedBuilder, wrapBuilder, Web, Builder } from '@kit.ArkUI';

@Builder
function WebBuilder(data: BuilderData) {
  // 此处组件可根据业务需要自行扩展。
  Web({ src: data.url, controller: data.controller })
    // .cacheMode(CacheMode.Default)
}
type MyBuilder = @Builder (p1: BuilderData) => void;
export const businessWebview : WrappedBuilder<MyBuilder> = wrapBuilder(WebBuilder);
```

ArkTS-Dyn示例：

```TypeScript
// PrecompileConfig.ets
import { webview } from '@kit.ArkWeb'

export interface Config {
  url:  string,
  localPath: string, // 本地资源路径
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

ArkTS-Sta示例：

```TypeScript
'use static'
// PrecompileConfig.ets
import { webview } from '@kit.ArkWeb'

export interface Config {
  url:  string,
  localPath: string, // 本地资源路径。
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

ArkTS-Dyn示例：

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
    // 初始化用于注入本地资源的Web组件
    this.precompileNode = createNode(precompileWebview,
      { url: "https://www.example.com/empty.html", controller: this.precompileController, context: this.getUIContext()});
  }

  build() {
    Column() {
      // 在适当的时机加载业务用Web组件，本例以Button点击触发为例
      Button("加载页面")
        .onClick(() => {
          this.businessNode = createNode(businessWebview, {
            url:  "https://www.example.com/business.html",
            controller: this.businessController,
            context: this.getUIContext()
          });
        })
      // 用于业务的Web组件
      NodeContainer(this.businessNode);
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
// Index.ets
import { Button, Column, Entry, Component, State, NodeContainer } from '@kit.ArkUI';
import { NodeController } from '@ohos.arkui.node';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { createNode, BuilderData } from "./DynamicComponent";
import { businessWebview } from "./BusinessWebview";
import { precompileWebview } from "./PrecompileWebview";
@Entry
@Component
struct Index {
  @State precompileNode: NodeController | undefined = undefined;
  precompileController: webview.WebviewController = new webview.WebviewController();

  @State businessNode: NodeController | undefined = undefined;
  businessController: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    // 初始化用于注入本地资源的Web组件。
    this.precompileNode = createNode(precompileWebview,
      new BuilderData( "https://www.example.com/empty.html", this.precompileController, this.getUIContext()));
  }

  build() {
    Column() {
      // 在适当的时机加载业务用Web组件，本例以Button点击触发为例。
      Button("加载页面")
        .onClick(() => {
          this.businessNode = createNode(businessWebview, new BuilderData(
            "https://www.example.com/business.html",
            this.businessController,
            this.getUIContext()
          ));
        })
      // 用于业务的Web组件。
      NodeContainer(this.businessNode!);
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

const url: "https://www.example.com/example.js";
const scripts = "console.info('test')";

const options: { responseHeaders: [
        { headerKey: "E-Tag", headerValue: "aWO42N9P9dG/5xqYQCxsx+vDOoU="},
        { headerKey: "Last-Modified", headerValue: "Wed, 21 Mar 2024 10:38:41 GMT"}
      ] } as webview.CacheOptions;

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('PrecompileJavaScript')
        .onClick(() => {
          try {
            this.controller.precompileJavaScript(url, scripts, options);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## prefetchPage

```TypeScript
prefetchPage(url: string, additionalHeaders?: Array<WebHeader>): void
```

Prefetch the resources required by the page, but will not execute js or render the page.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-prefetchPage(url: string, additionalHeaders?: Array<WebHeader>): void--><!--Device-WebviewController-prefetchPage(url: string, additionalHeaders?: Array<WebHeader>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | Which url to preresolve/preconnect. |
| additionalHeaders | Array&lt;WebHeader&gt; | 否 | Additional HTTP request header of the URL. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-url格式错误) | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2*1024*1024. |

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
      Button('prefetchPopularPage')
        .onClick(() => {
          try {
            // 预加载时，需要将'https://www.example.com'替换成一个真实的网站地址。
            let options = new webview.PrefetchOptions();
            options.ignoreCacheControlNoStore = true;
            options.minTimeBetweenPrefetchesMs = 100;
            this.controller.prefetchPage('https://www.example.com', [{ headerKey: "headerKey", headerValue: "headerValue" }], options);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      // 需要将'www.example1.com'替换成一个真实的网站地址。
      Web({ src: 'www.example1.com', controller: this.controller })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Column, Button, Web } from '@ohos.arkui.component'
import { BusinessError } from '@ohos.base'
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  build() {
    Column() {
      Button('prefetchPopularPage')
        .onClick(() => {
          try {
            let options = new webview.PrefetchOptions();
            options.ignoreCacheControlNoStore = true;
            options.minTimeBetweenPrefetchesMs = 100;
            // 预加载时，需要将'https://www.example.com'替换成一个真实的网站地址。
            this.controller.prefetchPage('https://www.example.com', [{ headerKey: "headerKey", headerValue: "headerValue" }], options);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      // 需要将'www.example1.com'替换成一个真实的网站地址。
      Web({ src: 'https://www.example1.com', controller: this.controller })
    }
  }
}
```

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
      Button('prefetchPopularPage')
        .onClick(() => {
          try {
            // 预加载时，需要将'https://www.example.com'替换成一个真实的网站地址。
            this.controller.prefetchPage('https://www.example.com');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      // 需要将'www.example1.com'替换成一个真实的网站地址。
      Web({ src: 'www.example1.com', controller: this.controller })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Button('prefetchPopularPage')
        .onClick(() => {
          try {
            // 预加载时，需要将'https://www.example.com'替换成一个真实的网站地址。
            this.controller.prefetchPage('https://www.example.com');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      // 需要将'www.example1.com'替换成一个真实的网站地址。
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-prefetchPage(url: string, additionalHeaders?: Array<WebHeader>, prefetchOptions?: PrefetchOptions): void--><!--Device-WebviewController-prefetchPage(url: string, additionalHeaders?: Array<WebHeader>, prefetchOptions?: PrefetchOptions): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | Which url to preresolve/preconnect. |
| additionalHeaders | Array&lt;WebHeader&gt; | 否 | Additional HTTP request header of the URL. |
| prefetchOptions | [PrefetchOptions](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-prefetchoptions-c.md) | 否 | Prefetch behavior can be customized via ‌prefetchOptions‌, including ignoring Cache-Control: no-store and adjusting the throttling interval. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-url格式错误) | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2*1024*1024. |

**示例**

参见 [prefetchPage](#prefetchpage)

## prefetchResource

```TypeScript
static prefetchResource(request: RequestInfo, additionalHeaders?: Array<WebHeader>, cacheKey?: string,
        cacheValidTime?: int): void
```

Prefetches resource requests based on specified request information and additional HTTP request headers, saves the requests to the memory cache, and specifies the cache key and validity period to accelerate loading. Currently, only POST requests whose Content-Type is application/x-www-form-urlencoded are supported. A maximum of six POST requests can be pre-obtained. To prefetch the seventh post request, call API[clearPrefetchedResource](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#clearprefetchedresource) to clear the cache of unnecessary post requests. Otherwise, the cache of the earliest prefetched POST request will be automatically cleared. To use the prefetched resource cache, you need to add the key value ArkWebPostCacheKey to the header of the POST request. The content of the key value is the cacheKey of the corresponding cache.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static prefetchResource(request: RequestInfo, additionalHeaders?: Array<WebHeader>, cacheKey?: string,        cacheValidTime?: int): void--><!--Device-WebviewController-static prefetchResource(request: RequestInfo, additionalHeaders?: Array<WebHeader>, cacheKey?: string,        cacheValidTime?: int): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | RequestInfo | 是 | The information of the request. |
| additionalHeaders | Array&lt;WebHeader&gt; | 否 | Additional HTTP request header of the request. |
| cacheKey | string | 否 | The key for memory cache. Default value is the url of the request. Only support number and letters. |
| cacheValidTime | int | 否 | The valid time of the cache for request, ranges greater than 0. The unit is second. Default value is 300s. The value of cacheValidTime must between 1 and 2147483647. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-url格式错误) | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2 *1024 *1024. |

**示例**

ArkTS-Dyn示例：

```TypeScript
// EntryAbility.ets
import { webview } from '@kit.ArkWeb';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    // 预获取时，需要將"https://www.example1.com/post?e=f&g=h"替换成真实要访问的网站地址。
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

ArkTS-Sta示例：

```TypeScript
// EntryAbility.ets
'use static'
import { UIAbility, Want, AbilityConstant } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';
import { AppStorage } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    webview.WebviewController.initializeWebEngine();
    // 预获取时，需要将"https://www.example1.com/post?e=f&g=h"替换成真实要访问的网站地址。
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static prepareForPageLoad(url: string, preconnectable: boolean, numSockets: int): void--><!--Device-WebviewController-static prepareForPageLoad(url: string, preconnectable: boolean, numSockets: int): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | Which url to preresolve/preconnect. |
| preconnectable | boolean | 是 | Indicates whether to preconnect. |
| numSockets | int | 是 | If preconnectable is true, this parameter indicates the number of sockets to be preconnected. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-url格式错误) | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2048. |
| [17100013](../../apis-arkweb/errorcode-webview.md#17100013-预连接时输入socket数目无效) | The number of preconnect sockets is invalid. |

**示例**

ArkTS-Dyn示例：

```TypeScript
// EntryAbility.ets
import { webview } from '@kit.ArkWeb';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    // 预连接时，需要将'https://www.example.com'替换成一个真实的网站地址。
    webview.WebviewController.prepareForPageLoad("https://www.example.com", true, 2);
    AppStorage.setOrCreate("abilityWant", want);
    console.info("EntryAbility onCreate done");
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { AppStorage } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    // 预连接时，需要將'https://www.example.com'替换成一个真实的网站地址。
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-refresh(): void--><!--Device-WebviewController-refresh(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WebviewController-refresh(ignoreCache: boolean): void--><!--Device-WebviewController-refresh(ignoreCache: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ignoreCache | boolean | 是 | If set to true, it indicates an end-to-end request with "pragma: no-cache"; otherwise, it performs a normal refresh. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

参见 [refresh](#refresh)

## registerJavaScriptProxy

```TypeScript
registerJavaScriptProxy(jsObject: object, name: string, methodList: Array<string>,
            asyncMethodList?: Array<string>, permission?: string): void
```

Registers the supplied ArkTS object into this Web component. The object is registered into all frames of the web page, including all iframes, using the specified name. This allows the methods of the ArkTS object to be accessed from JavaScript. <p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> Registed objects will not appear in JavaScript until the page is next (re)load. To avoid memory leaks, registerJavaScriptProxy must be used together with deleteJavaScriptProxy. To avoid security risks, it is recommended that registerJavaScriptProxy be used with trusted web components. If the same method is registered repeatedly in both synchronous and asynchronous list, it will default to an asynchronous method. The synchronous function list and asynchronous function list cannot be empty at the same time.<br> otherwise, this registration will fail. <p>

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-registerJavaScriptProxy(jsObject: object, name: string, methodList: Array<string>,            asyncMethodList?: Array<string>, permission?: string): void--><!--Device-WebviewController-registerJavaScriptProxy(jsObject: object, name: string, methodList: Array<string>,            asyncMethodList?: Array<string>, permission?: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| jsObject | object | 是 | Application side JavaScript objects participating in registration. |
| name | string | 是 | The name of the registered object, which is consistent with the object name called in the window. |
| methodList | Array&lt;string&gt; | 是 | The method of the application side JavaScript object participating in the registration. |
| asyncMethodList | Array&lt;string&gt; | 否 | The async method of the application side JavaScript object participating in the registration. |
| permission | string | 否 | permission configuration defining web page URLs that can access JavaScriptProxy methods. The configuration can be defined at two levels, object level and method level. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

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
            // 同时注册同步和异步函数
            this.controller.registerJavaScriptProxy(this.testObjtest, "objName", ["test", "toString", "testNumber"], ["asyncTestBool"]);
            // 仅注册同步函数
            this.controller.registerJavaScriptProxy(this.webTestObj, "objTestName", ["webTest", "webString"]);
            // 仅注册异步函数
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry, $rawfile, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class TestObj {
  constructor() {
  }

  test(testStr: string): string {
    console.info('Web Component str' + testStr);
    return testStr;
  }

  toString(): string {
    console.info('Web Component toString');
    return 'TestObj toString';
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
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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
            // 同时注册同步和异步函数
            this.controller.registerJavaScriptProxy(this.testObjtest, "objName", ["test", "toString", "testNumber"],
              ["asyncTestBool"]);
            // 仅注册同步函数
            this.controller.registerJavaScriptProxy(this.webTestObj, "objTestName", ["webTest", "webString"]);
            // 仅注册异步函数
            this.controller.registerJavaScriptProxy(this.asyncTestObj, "objAsyncName", [],
              ["asyncTest", "asyncString"]);
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static removeAllCache(clearRom: boolean): void--><!--Device-WebviewController-static removeAllCache(clearRom: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clearRom | boolean | 是 | Remove cache in both rom and ram if true. Otherwise only clear cache in ram. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

Clears the cache in the application. This API will clear the cache for all webviews in the same application.

<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> You can view the Webview cache in the data/storage/el2/base/cache/web/Cache directory. </p>

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-removeCache(clearRom: boolean): void--><!--Device-WebviewController-removeCache(clearRom: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clearRom | boolean | 是 | Whether to clear the cache in the ROM and RAM at the same time. {@code true} means to clear the cache in the ROM and RAM at the same time; {@code false} means to only clear the cache in the RAM. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static removeIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void--><!--Device-WebviewController-static removeIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hostList | Array&lt;string&gt; | 是 | Hosts needs to remove from bypass list. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-该设备不支持此api) | Capability not supported. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-requestFocus(): void--><!--Device-WebviewController-requestFocus(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
'use static'

// xxx.ets
import { Entry, Column, Component, Button, Web } from '@ohos.arkui.component';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@ohos.base';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-restoreWebState(state: Uint8Array): void--><!--Device-WebviewController-restoreWebState(state: Uint8Array): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | Uint8Array | 是 | Web access stack after serialization. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

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
              // 以同步方法打开文件。
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

ArkTS-Sta示例：

```TypeScript
'use static'
import { Entry, Text, Column, Component, Button, Web, AppStorage} from '@kit.ArkUI'
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Button('RestoreWebState')
        .onClick(() => {
          try {
            let path: string | undefined = AppStorage.get<string>("cacheDir") as string;
            if (path !== undefined) {
              let pathTemp: string = path + '/WebState';
              // 以同步方法打开文件。
              let file = fileIo.openSync(pathTemp, fileIo.OpenMode.READ_WRITE);
              let stat = fileIo.statSync(pathTemp);
              let size = stat.size;
              let buf = new ArrayBuffer(size);
              fileIo.read(file.fd, buf, (err, readLen) => {
                if (err) {
                  console.error("console error with error message: " + err.message + ", error code: " + err.code);
                } else {
                  if (readLen) {
                    let readLenTemp = readLen as Int;
                    console.info("read file data succeed");
                    this.controller.restoreWebState(new Uint8Array(buf.slice(0, readLen)));
                    fileIo.closeSync(file);
                  }
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

ArkTS-Dyn示例：

```TypeScript
// xxx.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    // 通过在AppStorage对象上绑定cacheDir，可以实现UIAbility组件与Page之间的数据同步。
    AppStorage.setOrCreate("cacheDir", this.context.cacheDir);
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { AppStorage} from '@kit.ArkUI'

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    // 通过在AppStorage对象上绑定cacheDir，可以实现UIAbility组件与Page之间的数据同步。
    AppStorage.setOrCreate("cacheDir", this.context.cacheDir);
  }
}
```

## resumeAllMedia

```TypeScript
resumeAllMedia(): void
```

控制网页被pauseAllMedia接口暂停的音视频继续播放。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-resumeAllMedia(): void--><!--Device-WebviewController-resumeAllMedia(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static resumeAllTimers(): void--><!--Device-WebviewController-static resumeAllTimers(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Entry, Column, Row, Component, Button, Web } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Row() {
        Button('PauseAllTimers')
          .onClick(() => {
            webview.WebviewController.pauseAllTimers();
          })
        Button('ResumeAllTimers')
          .onClick(() => {
            webview.WebviewController.resumeAllTimers();
          })
      }
      Web({ src: $rawfile("index.html"), controller: this.controller })
    }
  }
}
```

加载的html文件。

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

恢复当前网页麦克风捕获。使用麦克风功能前请在module.json5中添加权限: ohos.permission.MICROPHONE，具体权限的添加方法请参考 [在配置文件中声明权限](../../../security/AccessToken/declare-permissions.md#在配置文件中声明权限)。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-resumeMicrophone(): void--><!--Device-WebviewController-resumeMicrophone(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

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
      if (err) {
        console.error(`ErrorCode: ${err.code}, Message: ${err.message}`);
        return;
      }
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import { $rawfile, Web, Column, Component, Entry, Button, OnPermissionRequestEvent, Context } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { UIContext } from "@kit.ArkUI";
import { AlertDialogParamWithButtons, AlertDialogButtonBaseOptions } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { PermissionRequestResult, common } from '@kit.AbilityKit';
import abilityAccessCtrl from '@ohos.abilityAccessCtrl'
import { MicrophoneCaptureStateChangeInfo } from '@ohos.arkui.component'
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  uiContext: UIContext = this.getUIContext();

  aboutToAppear(): void {
    let context: Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionsFromUser(context, ['ohos.permission.MICROPHONE'],
      (err: BusinessError | null, data?: PermissionRequestResult) => {
        if (err) {
          console.error(`ErrorCode: ${err.code}, Message: ${err.message}`);
          return;
        }
        if (data) {
          console.info('data:' + JSON.stringify(data));
          console.info('data permissions:' + data.permissions);
          console.info('data authResults:' + data.authResults);
        }
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
        .onPermissionRequest((event: OnPermissionRequestEvent): void => {
          if (event) {
            const dialogOptions: AlertDialogParamWithButtons = {
              title: 'title',
              message: 'text',
              primaryButton: {
                value: 'deny',
                action: () => {
                  event.request.deny();
                },
              } as AlertDialogButtonBaseOptions,
              secondaryButton: {
                value: 'onConfirm',
                action: () => {
                  event.request.grant(event.request.getAccessibleResource());
                },
              } as AlertDialogButtonBaseOptions,
              cancel: () => {
                event.request.deny();
              }
            };
            this.uiContext.showAlertDialog(dialogOptions);
          }
        })
        .onMicrophoneCaptureStateChange((event: MicrophoneCaptureStateChangeInfo | undefined): void => {
          if (event) {
            console.info("Microphone from ", event.originalState, " to ", event.newState);
          }
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
   <meta charset="UTF-8">
 </head>
 <body>
   <video id="video" width="400px" height="400px" autoplay="autoplay">
   </video>
   <input type="button" title="HTML5麦克风" value="开启麦克风" onclick="getMedia()" />
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-runJavaScript(script: string): Promise<string>--><!--Device-WebviewController-runJavaScript(script: string): Promise<string>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| script | string | 是 | JavaScript Script. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | A promise is solved after the JavaScript script is executed. This parameter will be the result of JavaScript script execution. If the JavaScript script fails to execute or has no return value, null will be returned. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |
| [17100003](../../apis-arkweb/errorcode-webview.md#17100003-resource路径错误) | Calling a JS method that returns an empty ArrayBuffer via runJavaScript. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, State, $rawfile, Text } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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

加载的html文件。

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, $rawfile } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
              .catch((error: Error) => {
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

加载的html文件。

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-runJavaScript(script: string, callback: AsyncCallback<string>): void--><!--Device-WebviewController-runJavaScript(script: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| script | string | 是 | JavaScript Script. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 | Callbacks execute JavaScript script results. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |
| [17100003](../../apis-arkweb/errorcode-webview.md#17100003-resource路径错误) | Calling a JS method that returns an empty ArrayBuffer via runJavaScript. |

**示例**

参见 [runJavaScript](#runjavascript)

## runJavaScriptExt

```TypeScript
runJavaScriptExt(script: string | ArrayBuffer): Promise<JsMessageExt>
```

Execute JavaScript code in the context of the currently displayed page, and return the result.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-runJavaScriptExt(script: string | ArrayBuffer): Promise<JsMessageExt>--><!--Device-WebviewController-runJavaScriptExt(script: string | ArrayBuffer): Promise<JsMessageExt>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| script | string \| ArrayBuffer | 是 | JavaScript Script. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[JsMessageExt](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-jsmessageext-c.md)&gt; | A promise is solved after the JavaScript script is executed. This parameter will be the result of JavaScript script execution. If the JavaScript script fails to execute or has no return value, a none type value will be returned. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

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
                      // 若发生异常或返回类型不支持时，getErrorDescription不为空
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

ArkTS-Sta示例：

```TypeScript
'use static'
import { Entry, Text, Column, Component, Button, Web, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State msg1: string = '';
  @State msg2: string = '';

  build() {
    Column() {
      Text(this.msg1).fontSize(20)
      Text(this.msg2).fontSize(20)
      Web({src:"resource://rawfile/index.html", controller:this.controller})
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
                      // 若发生异常或返回类型不支持时，getErrorDescription不为空
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

ArkTS-Dyn示例：

```TypeScript
// 使用ArrayBuffer入参，从文件中获取JavaScript脚本数据。
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
            let filePath = context!.filesDir + '/test.txt';
            // 新建并打开文件。
            let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
            // 写入一段内容至文件。
            fileIo.writeSync(file.fd, "test()");
            // 从文件中读取内容。
            let arrayBuffer: ArrayBuffer = new ArrayBuffer(6);
            fileIo.readSync(file.fd, arrayBuffer, { offset: 0, length: arrayBuffer.byteLength });
            // 关闭文件。
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
                      // 若发生异常或返回类型不支持时，getErrorDescription不为空
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

ArkTS-Sta示例：

```TypeScript
'use static'
// 使用ArrayBuffer入参，从文件中获取JavaScript脚本数据
import { Entry, Text, Column, Component, Button, Web, UIContext, Context, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State msg1: string = ''
  @State msg2: string = ''
  uiContext:UIContext = this.getUIContext();
  build() {
    Column() {
      Text(this.msg1).fontSize(20)
      Text(this.msg2).fontSize(20)
      Button('runJavaScriptExt')
        .onClick(() => {
          try {
            let context:Context|undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
            let filePath = context!.filesDir + 'test.txt';
            // 新建并打开文件
            let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
            // 写入一段内容至文件
            fileIo.writeSync(file.fd, "test()");
            // 从文件中读取内容
            let arrayBuffer: ArrayBuffer = new ArrayBuffer(6);
            fileIo.readSync(file.fd, arrayBuffer, { offset: 0, length: arrayBuffer.byteLength });
            // 关闭文件
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
                      // 若发生异常或返回类型不支持时，getErrorDescription不为空
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

加载的html文件。

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

ArkTS-Dyn示例：

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
                  // 若发生异常或返回类型不支持时，getErrorDescription不为空
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

ArkTS-Sta示例：

```TypeScript
'use static'
import { Entry, Text, Column, Component, Button, Web, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State webResult: string = '';
  @State msg1: string = '';
  @State msg2: string = '';

  build() {
    Column() {
      Text(this.webResult).fontSize(20)
      Text(this.msg1).fontSize(20)
      Text(this.msg2).fontSize(20)
      Web({src:"resource://rawfile/index.html", controller:this.controller})
        .javaScriptAccess(true)
        .onPageEnd(() => {
          this.controller.runJavaScriptExt('test()')
            .then((result:webview.JsMessageExt) => {
              try {
                if (result.getErrorDescription()) {
                  // 若发生异常或返回类型不支持时，getErrorDescription不为空
                  console.info(`runJavaScriptExt getErrorDescription: ${result.getErrorDescription()}`);
                  return null;
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
            }).catch((error) => {
            console.error("error: " + error);
          })
        })
    }
  }
}
```

ArkTS-Dyn示例：

```TypeScript
// 使用ArrayBuffer入参，从文件中获取JavaScript脚本数据。
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
            let filePath = context!.filesDir + '/test.txt';
            // 新建并打开文件。
            let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
            // 写入一段内容至文件。
            fileIo.writeSync(file.fd, "test()");
            // 从文件中读取内容。
            let arrayBuffer: ArrayBuffer = new ArrayBuffer(6);
            fileIo.readSync(file.fd, arrayBuffer, { offset: 0, length: arrayBuffer.byteLength });
            // 关闭文件。
            fileIo.closeSync(file);
            this.controller.runJavaScriptExt(arrayBuffer)
              .then((result) => {
                try {
                  if (result.getErrorDescription()) {
                    // 若发生异常或返回类型不支持时，getErrorDescription不为空
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

ArkTS-Sta示例：

```TypeScript
'use static'
// 使用ArrayBuffer入参，从文件中获取JavaScript脚本数据
import { Entry, Text, Column, Component, Button, Web, UIContext, Context, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State msg1: string = '';
  @State msg2: string = '';
  uiContext:UIContext = this.getUIContext();
  build() {
    Column() {
      Text(this.msg1).fontSize(20)
      Text(this.msg2).fontSize(20)
      Button('runJavaScriptExt')
        .onClick(() => {
          try {
            let context:Context|undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
            let filePath = context!.filesDir + 'test.txt';
            // 新建并打开文件。
            let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
            // 写入一段内容至文件。
            fileIo.writeSync(file.fd, "test()");
            // 从文件中读取内容。
            let arrayBuffer: ArrayBuffer = new ArrayBuffer(6);
            fileIo.readSync(file.fd, arrayBuffer, { offset: 0, length: arrayBuffer.byteLength });
            // 关闭文件。
            fileIo.closeSync(file);
            this.controller.runJavaScriptExt(arrayBuffer)
              .then((result:webview.JsMessageExt) => {
                try {
                  if (result.getErrorDescription()) {
                    // 若发生异常或返回类型不支持时，getErrorDescription不为空
                    console.info(`runJavaScriptExt getErrorDescription: ${result.getErrorDescription()}`);
                    return null;
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
              .catch((error) => {
                console.error("error: " + error);
              })
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({src:"resource://rawfile/index.html", controller:this.controller})
        .javaScriptAccess(true)
    }
  }
}
```

加载的html文件。

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-runJavaScriptExt(script: string | ArrayBuffer, callback: AsyncCallback<JsMessageExt>): void--><!--Device-WebviewController-runJavaScriptExt(script: string | ArrayBuffer, callback: AsyncCallback<JsMessageExt>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| script | string \| ArrayBuffer | 是 | JavaScript Script. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[JsMessageExt](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-jsmessageext-c.md)&gt; | 是 | Callbacks execute JavaScript script results. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

参见 [runJavaScriptExt](#runjavascriptext)

## scrollBy

```TypeScript
scrollBy(deltaX: double, deltaY: double, duration?: int): void
```

Scroll by the delta position within specified time.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-scrollBy(deltaX: double, deltaY: double, duration?: int): void--><!--Device-WebviewController-scrollBy(deltaX: double, deltaY: double, duration?: int): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deltaX | double | 是 | the delta x of the position <br>Unit: vp. |
| deltaY | double | 是 | the delta y of the position <br>Unit: vp. |
| duration | int | 否 | the scroll animation duration. <br>Unit: millisecond, The value range is all integers, If the value is not passed, or is negative or 0, there is no animation. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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
            this.controller.scrollBy(0, 0, 1); // 如果想停止当前scroll产生的动画，可再次生成一个1ms的动画去打断该动画。
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Web, Column, Component, Entry, Button } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
            this.controller.scrollBy(0, 0, 1); // 如果想停止当前scroll产生的动画，可再次生成一个1ms的动画去打断该动画。
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

加载的html文件。

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-scrollByWithResult(deltaX: double, deltaY: double): boolean--><!--Device-WebviewController-scrollByWithResult(deltaX: double, deltaY: double): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deltaX | double | 是 | the delta x of the position. The unit is vp |
| deltaY | double | 是 | the delta y of the position. The unit is vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the scroll operation is successful, otherwise false. Return value scenario: when the Web page is in the touch state, return false, otherwise return true. In the same layer rendering scene, when the same layer rendering area of ??the Web is in the touching state, the return value is true. In a nested scrolling scenario, calling scrollByWithResult will not trigger nested scrolling of the parent component. This interface does not guarantee sliding frame rate performance. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, Button, $rawfile } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

加载的html文件。

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-scrollTo(x: double, y: double, duration?: int): void--><!--Device-WebviewController-scrollTo(x: double, y: double, duration?: int): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | double | 是 | the x of the position <br>Unit: vp. |
| y | double | 是 | the y of the position <br>Unit: vp. |
| duration | int | 否 | the scroll animation duration. <br>Unit: millisecond, The value range is all integers, If the value is not passed, or is negative or 0, there is no animation. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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
            this.controller.scrollBy(0, 0, 1); // 如果想停止当前scroll产生的动画，可再次生成一个1ms的动画去打断该动画。
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Web, Column, Component, Entry, Button } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
            this.controller.scrollBy(0, 0, 1); // 如果想停止当前scroll产生的动画，可再次生成一个1ms的动画去打断该动画。
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

加载的html文件。

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-searchAllAsync(searchString: string): void--><!--Device-WebviewController-searchAllAsync(searchString: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchString | string | 是 | String to be search. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry, $rawfile, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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

加载的html文件。

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-searchNext(forward: boolean): void--><!--Device-WebviewController-searchNext(forward: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| forward | boolean | 是 | Step of search is back or forward. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-serializeWebState(): Uint8Array--><!--Device-WebviewController-serializeWebState(): Uint8Array-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | Web access stack after serialization. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

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
              // 以同步方法打开文件。
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Column, Component, Button, Web, AppStorage } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Button('serializeWebState')
        .onClick(() => {
          try {
            let state = this.controller.serializeWebState();
            let path:string | undefined = AppStorage.get<string>("cacheDir") as string;
            if (path) {
              path += '/WebState';
              // 以同步方法打开文件。
              let file = fileIo.openSync(path as string, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
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

ArkTS-Dyn示例：

```TypeScript
// xxx.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        // 通过在AppStorage对象上绑定cacheDir，可以实现UIAbility组件与Page之间的数据同步。
        AppStorage.setOrCreate("cacheDir", this.context.cacheDir);
    }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { AppStorage } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        // 通过在AppStorage对象上绑定cacheDir，可以实现UIAbility组件与Page之间的数据同步。
        AppStorage.setOrCreate("cacheDir", this.context.cacheDir);
    }
}
```

## setActiveWebEngineVersion

```TypeScript
static setActiveWebEngineVersion(engineVersion: ArkWebEngineVersion): void
```

设置ArkWeb内核版本。若系统不支持指定版本，则设置无效。该接口为全局静态API，须在调用initializeWebEngine前执行，若已加载任何Web组件，则该设置无效。

> **说明：**
> 
> - setActiveWebEngineVersion不支持在异步线程中调用。
> 
> - setActiveWebEngineVersion全局生效，在整个APP生命周期中调用一次即可，不需要重复调用。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static setActiveWebEngineVersion(engineVersion: ArkWebEngineVersion): void--><!--Device-WebviewController-static setActiveWebEngineVersion(engineVersion: ArkWebEngineVersion): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| engineVersion | [ArkWebEngineVersion](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-arkwebengineversion-e.md) | 是 | ArkWeb内核版本。 |

**示例**

本示例以EntryAbility为例，实现了在Ability创建阶段设置ArkWeb内核版本的功能。

```TypeScript
// xxx.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate")
    webview.WebviewController.setActiveWebEngineVersion(webview.ArkWebEngineVersion.M132)
    if (webview.WebviewController.getActiveWebEngineVersion() == webview.ArkWebEngineVersion.M132) {
      console.info("Active Web Engine Version set to M132")
    }
    console.info("EntryAbility onCreate done")
  }
}
```

本示例以EntryAbility为例，实现了在Ability创建阶段设置ArkWeb内核版本的功能。

```TypeScript
// xxx.ets
import UIAbility from '@ohos.app.ability.UIAbility';
import Want from '@ohos.app.ability.Want';
import AbilityConstant from '@ohos.app.ability.AbilityConstant';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate")
    webview.WebviewController.setActiveWebEngineVersion(webview.ArkWebEngineVersion.M132)
    if (webview.WebviewController.getActiveWebEngineVersion() == webview.ArkWebEngineVersion.M132) {
      console.info("Active Web Engine Version set to M132")
    }
    console.info("EntryAbility onCreate done")
  }
}
```

## setAppCustomUserAgent

```TypeScript
static setAppCustomUserAgent(userAgent: string) : void
```

Set the default User-Agent for the application.

<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> Unlike setCustomUserAgent, which only takes effect in the current web context, the priority for pages loaded in the web is as follows: 1. The User-Agent set by setCustomUserAgent is used first. 2. If not set, it will check whether a specific User-Agent has been assigned to the current page via setUserAgentForHosts. 3. If no specific User-Agent is assigned, the application will fall back to using the User-Agent set by setAppCustomUserAgent. 4. If the app's default User-Agent is also not specified, the web's default User-Agent will be used as the final fallback. </p>

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static setAppCustomUserAgent(userAgent: string) : void--><!--Device-WebviewController-static setAppCustomUserAgent(userAgent: string) : void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userAgent | string | 是 | The User-Agent string. @static |

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { webview } from '@kit.ArkWeb';
import { Entry, Column, Component, Web, Button, State } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

设置网页静音。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-setAudioMuted(mute: boolean): void--><!--Device-WebviewController-setAudioMuted(mute: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mute | boolean | 是 | 表示是否将网页设置为静音状态。<br>true表示将网页设置为静音状态，false表示将网页取消静音状态。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State muted: boolean = false;

  build() {
    Column() {
      Button("Toggle Mute")
        .onClick(e => {
          if (e) {
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static setAutoPreconnect(enabled: boolean): void--><!--Device-WebviewController-static setAutoPreconnect(enabled: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | Enable if true, disable if false. @static |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// EntryAbility.ets
'use static'
import AbilityConstant from '@ohos.app.ability.AbilityConstant';
import UIAbility from '@ohos.app.ability.UIAbility';
import Want from '@ohos.app.ability.Want';
import { AppStorage } from 'arkui.stateManagement.storage.appStorage'
import window from '@ohos.window';
import { BusinessError } from '@ohos.base';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) : void {
    webview.WebviewController.setAutoPreconnect(false);
    webview.WebviewController.initializeWebEngine();
    AppStorage.setOrCreate("abilityWant", want);
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // 在使用时将'xxx'替换成一个真实的ets文件名。
    windowStage.loadContent('pages/xxx', (err: BusinessError<void> | null): void => {
      if (err?.code) {
        return;
      }
    });
  }
}
```

## setBackForwardCacheOptions

```TypeScript
setBackForwardCacheOptions(options?: BackForwardCacheOptions): void
```

Configure the BackForwardCache.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-setBackForwardCacheOptions(options?: BackForwardCacheOptions): void--><!--Device-WebviewController-setBackForwardCacheOptions(options?: BackForwardCacheOptions): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [BackForwardCacheOptions](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-backforwardcacheoptions-c.md) | 否 | The configuration of BackForwardCache. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ts
'use static'
import { Entry, Component, Column, Row, Button, Web } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Row() {
        Button("Add options").onClick(() => {
          let options = new webview.BackForwardCacheOptions();
          options.size = 3;
          options.timeToLive = 60;
          this.controller.setBackForwardCacheOptions(options);
        })
        Button("Backward").onClick(() => {
          this.controller.backward();
        })
        Button("Forward").onClick(() => {
          this.controller.forward();
        })
      }
      // 使用时需要將"https://www.example.com"替换成真实要访问的网站地址。
      Web({ src: "https://example.com", controller: this.controller })
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static setBlanklessLoadingCacheCapacity(capacity: int) : int--><!--Device-WebviewController-static setBlanklessLoadingCacheCapacity(capacity: int) : int-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| capacity | int | 是 | Cache capacity, in MB. The maximum value is 100 MB. The default value is 30 MB. The value ranges from 0 to 100. If this parameter is set to 0, no cache capacity is available and the functionality is disabled globally. When the value is set to a number smaller than 0, the value 0 takes effect. When the value is set to a number greater than 100, the value 100 takes effect. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The effective value that ranges from 0 MB to 100 MB. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |  |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    // 设置缓存容量为10MB
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import UIAbility from '@ohos.app.ability.UIAbility';
import AbilityConstant from '@ohos.app.ability.AbilityConstant';
import Want from '@ohos.app.ability.Want';
import { webview } from '@kit.ArkWeb';
import { AppStorage } from '@ohos.arkui.stateManagement';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    // 设置缓存容量为10MB
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-setBlanklessLoadingWithKey(key: string, is_start: boolean) : WebBlanklessErrorCode--><!--Device-WebviewController-setBlanklessLoadingWithKey(key: string, is_start: boolean) : WebBlanklessErrorCode-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key value that uniquely identifies the current page. It must be the same as the key value of the getBlanklessInfoWithKey API. Default value: N/A. The value cannot be empty or exceed 2048 characters. When an invalid value is set, the error code WebBlanklessErrorCode is returned, and the API does not take effect. |
| is_start | boolean | 是 | Whether to enable frame interpolation. The value true indicates to enable frame interpolation, and the value false indicates the opposite. The default value is false. The value can be true or false. Action for setting an invalid value: N/A. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WebBlanklessErrorCode](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-webblanklesserrorcode-e.md) | WebBlanklessErrorCode. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |  |

**示例**

ArkTS-Dyn示例：

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
            // 当相似度超过50%，加载耗时小于1000ms时启用插帧，否则不启用。
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import { Entry, Column, Component, Web } from '@ohos.arkui.component'
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  build() {
    Column() {
      Web({ src: 'https://www.example.com', controller: this.controller })
       .javaScriptAccess(true)
       .onLoadIntercept((event) => {
            // 当相似度超过50%，加载耗时小于1000ms时启用插帧，否则不启用。
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

Triggers frame interpolation and sets frame interpolation parameters. This API must be used in pair with the getBlanklessInfoWithKey API.

Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WebviewController-setBlanklessLoadingWithParams(key: string,            param: BlanklessLoadingParam) : WebBlanklessErrorCode--><!--Device-WebviewController-setBlanklessLoadingWithParams(key: string,            param: BlanklessLoadingParam) : WebBlanklessErrorCode-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | Key value that uniquely identifies the current page. The key value must be the same as that of getBlanklessInfoWithKey. <br>Value range: (0, 2048] <br>Value range: (0, 2048] <br>which must be the same as the key value in getBlanklessInfoWithKey |
| param | [BlanklessLoadingParam](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-blanklessloadingparam-i.md) | 是 | The parameter of blankless. For details see {@Link BlanklessLoadingParam}. <br>na |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WebBlanklessErrorCode](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-webblanklesserrorcode-e.md) | WebBlanklessErrorCode. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) | Capability not supported. |

**示例**

ArkTS-Dyn示例：

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
                    // 数据监控
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import { Entry, Column, Component, Web } from '@ohos.arkui.component'
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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
                  expirationTime: data.getTime() as Int,
                  callback: (info: webview.BlanklessFrameInterpolationInfo)=>{
                    // 数据监控
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static setConnectionTimeout(timeout: int): void--><!--Device-WebviewController-static setConnectionTimeout(timeout: int): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeout | int | 是 | Socket connection timeout. The value should be an integer. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3. Parameter verification failed. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry, OnErrorReceiveEvent } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
        .onErrorReceive((event: OnErrorReceiveEvent): void => {
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-setCustomUserAgent(userAgent: string): void--><!--Device-WebviewController-setCustomUserAgent(userAgent: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userAgent | string | 是 | User custom agent information. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-setDownloadDelegate(delegate: WebDownloadDelegate): void--><!--Device-WebviewController-setDownloadDelegate(delegate: WebDownloadDelegate): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| delegate | [WebDownloadDelegate](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-webdownloaddelegate-c.md) | 是 | Delegate used for download triggered from web. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-setErrorPageEnabled(enable: boolean): void--><!--Device-WebviewController-setErrorPageEnabled(enable: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | Whether to enable the default error page feature. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { webview } from '@kit.ArkWeb';
import { Entry, Column, Component, Web } from '@kit.ArkUI';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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

ArkTS-Dyn示例：

```TypeScript
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile("iframe_error.html"), controller: this.controller })
        .onControllerAttached(() => {
          // 启用mainframe和subframe错误页功能
          this.controller.setErrorPageEnabled(true, true);
          // 查询subframe错误页功能是否已启用
          let isSubframeEnabled: boolean = this.controller.getSubframeErrorPageEnabled();
          console.info("Subframe error page enabled: " + isSubframeEnabled);
        })
        .onOverrideErrorPage((event) => {
          if (event.request.isMainFrame()) {
            return "<html><body><h1>主页面加载失败</h1><p>错误码：" + event.error.getErrorCode() + "</p></body></html>";
          }
          return "<html><body><h1>子页面加载失败</h1><p>错误码：" + event.error.getErrorCode() + "</p></body></html>";
        })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { webview } from '@kit.ArkWeb';
import { Entry, Column, Component, Web, $rawfile } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: $rawfile("iframe_error.html"), controller: this.controller })
        .onControllerAttached(() => {
          // 启用mainframe和subframe错误页功能
          this.controller.setErrorPageEnabled(true, true);
          // 查询subframe错误页功能是否已启用
          let isSubframeEnabled: boolean = this.controller.getSubframeErrorPageEnabled();
          console.info("Subframe error page enabled: " + isSubframeEnabled);
        })
        .onOverrideErrorPage((event) => {
          if (event.request.isMainFrame()) {
            return "<html><body><h1>主页面加载失败</h1><p>错误码：" + event.error.getErrorCode() + "</p></body></html>";
          }
          return "<html><body><h1>子页面加载失败</h1><p>错误码：" + event.error.getErrorCode() + "</p></body></html>";
        })
    }
  }
}
```

```TypeScript
<!-- resources/rawfile/iframe_error.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>iframe</title>
</head>
<body>
<iframe src="https://error-test.com/" title="iframe_error.html" loading="lazy" referrerpolicy="no-referrer" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture"></iframe>
</body>
</html>
```

## setHostIP

```TypeScript
static setHostIP(hostName: string, address: string, aliveTime: int): void
```

Set IP address for host name.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static setHostIP(hostName: string, address: string, aliveTime: int): void--><!--Device-WebviewController-static setHostIP(hostName: string, address: string, aliveTime: int): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hostName | string | 是 | Which host name to be resolved. |
| address | string | 是 | Resolved IP address. |
| aliveTime | int | 是 | The validity seconds for resolve cache. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |

**示例**

请参考[clearHostIP](#clearhostip)。

## setHttpDns

```TypeScript
static setHttpDns(secureDnsMode: SecureDnsMode, secureDnsConfig: string): void
```

Set web engine to use HttpDns server to resolve dns.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static setHttpDns(secureDnsMode: SecureDnsMode, secureDnsConfig: string): void--><!--Device-WebviewController-static setHttpDns(secureDnsMode: SecureDnsMode, secureDnsConfig: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| secureDnsMode | [SecureDnsMode](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-securednsmode-e.md) | 是 | using HttpDns. |
| secureDnsConfig | string | 是 | The configuration of the HttpDns server. Must be https protocol and only allow one server to be configured. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3. Parameter verification failed. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// EntryAbility.ets
'use static'
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { AppStorage } from '@kit.ArkUI';

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-setNetworkAvailable(enable: boolean): void--><!--Device-WebviewController-setNetworkAvailable(enable: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | Whether enable window.navigator.onLine. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry, $rawfile } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

加载的html文件。

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
<body>
<h1>online 属性</h1>
<p id="demo"></p>
<button onclick="func()">click</button>
<script>
    // 检测浏览器是否在线。
    var online1 = navigator.onLine;
    document.getElementById("demo").innerHTML = "浏览器在线：" + online1;

    function func(){
      var online2 = navigator.onLine;
      document.getElementById("demo").innerHTML = "浏览器在线：" + online2;
    }
</script>
</body>
</html>
```

## setPathAllowingUniversalAccess

```TypeScript
setPathAllowingUniversalAccess(pathList: Array<string>): void
```

Sets a path list. When a file protocol accesses resources in the path list, it can access the local files across domains. In addition, when a path list is set, the file protocol can access only the resources in the path list. The behavior of fileAccess will be overwritten by that of this API.

The paths in the list must be any of the following(sub path and module name must be provided):

1. The path of subdirectory of the application file directory, like "/data/storage/el2/base/files/example" or "/data/storage/el2/base/haps/entry/files/example". The application file directory is obtained using Context.filesDir in the Ability Kit. 2. The path of application resource directory or its subdirectory, like "/data/storage/el1/bundle/entry/resource/resfile" or "/data/storage/el1/bundle/entry/resource/resfile/example". The application resource directory is obtained from Context.resourceDir in the Ability Kit.

If a path in the list is not of the preceding paths, error code 401 is reported and the path list fails to be set. When the path list is set to empty, the accessible files for the file protocol are subject to the behavior of the fileAccess.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-setPathAllowingUniversalAccess(pathList: Array<string>): void--><!--Device-WebviewController-setPathAllowingUniversalAccess(pathList: Array<string>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pathList | Array&lt;string&gt; | 是 | The path list allow universal access. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Parameter string is too long. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

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
            // 设置允许可以跨域访问的路径列表
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, UIContext, Row } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  uiContext: UIContext = this.getUIContext();

  build() {
    Row() {
      Web({ src: "", controller: this.controller })
        .onControllerAttached(() => {
          try {
            // 设置允许可以跨域访问的路径列表。
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

加载的html文件，位于应用资源目录resource/resfile/index.html。

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
                // 如果ets侧正确设置路径列表，则此处能正常获取资源
                        const element = document.getElementById('text');
                        element.textContent = "load " + file + " success";
                    } else {
                // 如果ets侧不设置路径列表，则此处会触发CORS跨域检查错误
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

html中使用file协议通过XMLHttpRequest跨域访问本地js文件，js文件位于resource/resfile/js/script.js。

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-setPrintBackground(enable: boolean): void--><!--Device-WebviewController-setPrintBackground(enable: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | Set whether print web page background |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { Entry, Column, Component, Web, Button } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static setRenderProcessMode(mode: RenderProcessMode): void--><!--Device-WebviewController-static setRenderProcessMode(mode: RenderProcessMode): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [RenderProcessMode](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-renderprocessmode-e.md) | 是 | The render process mode for the ArkWeb. Call [getRenderProcessMode](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#getrenderprocessmode) to get the ArkWeb rendering subprocess mode of the current device. The enumerated value *0 indicates the single render subprocess mode, and *1 indicates the multi-render subprocess mode. If an invalid number other than the enumerated value of *RenderProcessMode is passed, the multi-render subprocess mode is used by default. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Column, Component, Button, Web } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct webViewController {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Button('setRenderProcessMode')
        .onClick(() => {
          try {
            webview.WebviewController.setRenderProcessMode(webview.RenderProcessMode.MULTIPLE);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        });
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-setScrollable(enable: boolean, type?: ScrollType): void--><!--Device-WebviewController-setScrollable(enable: boolean, type?: ScrollType): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | Set whether scrolling is allowed {@code true} means scrolling is allowed. {@code false} means scrolling is disabled. |
| type | [ScrollType](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-scrolltype-e.md) | 否 | Enable scrolling type When the input parameter enable is false, it indicates that scrolling of the ScrollType type is prohibited. When ScrollType is not specified,it indicates that all types of webpage scrolling are prohibited. When the input parameter enable is true, regardless of whether ScrollType is specified, it indicates that all types of webpage scrolling are allowed. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, Button } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Button('setScrollable')
        .onClick(() => {
          try {
            this.controller.setScrollable(true, webview.ScrollType.EVENT);
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static setScrollbarMode(scrollbarMode: ScrollbarMode): void--><!--Device-WebviewController-static setScrollbarMode(scrollbarMode: ScrollbarMode): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scrollbarMode | [ScrollbarMode](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-scrollbarmode-e.md) | 是 | web scrollbar mode, default OVERLAY_LAYOUT_SCROLLBAR. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// setScrollbarMode.ets
import { Web, Column, Component, Entry, $rawfile} from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  aboutToAppear(): void {
    try {
      webview.WebviewController.setScrollbarMode(webview.ScrollbarMode.FORCE_DISPLAY_SCROLLBAR);
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }
  }

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

加载的html文件。

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static setServiceWorkerWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void--><!--Device-WebviewController-static setServiceWorkerWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scheme | string | 是 | String value for url scheme. |
| handler | [WebSchemeHandler](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-webschemehandler-c.md) | 是 | Web scheme handler. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Incorrect parameter types. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static setSiteIsolationMode(mode: SiteIsolationMode): void--><!--Device-WebviewController-static setSiteIsolationMode(mode: SiteIsolationMode): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [SiteIsolationMode](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-siteisolationmode-e.md) | 是 | The site isolation mode of the application, default value depends on different devices type. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. Possible causes: 1. Site Isolation mode is already set by the developer. 2. Site Isolation mode cannot be strict in single-render-process mode. 3. Site Isolation mode cannot be changed while Secure Shield mode is active. @static |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import { Entry, Component, Column, Web, Button } from '@ohos.arkui.component'
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static setSocketIdleTimeout(timeout: int): void--><!--Device-WebviewController-static setSocketIdleTimeout(timeout: int): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeout | int | 是 | Socket idle timeout. @static |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// EntryAbility.ets
'use static'
import AbilityConstant from '@ohos.app.ability.AbilityConstant';
import UIAbility from '@ohos.app.ability.UIAbility';
import Want from '@ohos.app.ability.Want';
import window from '@ohos.window';
import { BusinessError } from '@ohos.base';
import hilog from '@ohos.hilog';
import { webview } from '@kit.ArkWeb';
import { AppStorage } from 'arkui.stateManagement.storage.appStorage';

class EntryAbility extends UIAbility {
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-setSoftKeyboardBehaviorMode(mode: WebSoftKeyboardBehaviorMode): void--><!--Device-WebviewController-setSoftKeyboardBehaviorMode(mode: WebSoftKeyboardBehaviorMode): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [WebSoftKeyboardBehaviorMode](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-websoftkeyboardbehaviormode-e.md) | 是 | The WebSoftKeyboardBehaviorMode of this web. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import { Entry, Component, Column, Web, Button, WebKeyboardAvoidMode, $rawfile } from '@ohos.arkui.component'
import { BusinessError } from '@ohos.base'
import webview from '@ohos.web.webview';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

Sets the URL trust list for the ArkWeb.

<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> When the URL trust list is set, only the URLs in the list can be accessed.

Example of the urlTrustList:

{ "UrlPermissionList": [ { "scheme": "https", "host": "www.example1.com", "port": 443, "path": "pathA/pathB" }, { "scheme": "http", "host": "*.example2.com", "port": 80, "path": "test1/test2/test3" } ] } </p>

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

<!--Device-WebviewController-setUrlTrustList(urlTrustList: string, allowOpaqueOrigin: boolean, supportWildcard: boolean): void--><!--Device-WebviewController-setUrlTrustList(urlTrustList: string, allowOpaqueOrigin: boolean, supportWildcard: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| urlTrustList | string | 是 | The URL trust list in JSON format. An empty string means all URLs are allowed. |
| allowOpaqueOrigin | boolean | 是 | If true, loading of opaque origin URLs (e.g., javascript, data) is allowed. If false, it is not allowed. |
| supportWildcard | boolean | 是 | If true, wildcard matching is supported (e.g., *.example.com matches all subdomains). If false, wildcard matching is not supported. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Initialization error. The WebviewController must be associated with a Web component. |
| [401](../../errorcode-universal.md#401-参数检查失败) |  |

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
  urltrustList: string = "{\"UrlPermissionList\":[{\"scheme\":\"http\", \"host\":\"trust.example.com\", \"port\":80, \"path\":\"test\"}]}"

  build() {
    Column() {
      Button('Setting the trustlist')
        .onClick(() => {
          try {
            // 设置白名单，只允许访问trust网页
            this.controller.setUrlTrustList(this.urltrustList);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Cancel the trustlist.')
        .onClick(() => {
          try {
            // 白名单传入空字符串表示关闭白名单机制，所有URL都可以允许访问
            this.controller.setUrlTrustList("");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Access the trust web')
        .onClick(() => {
          try {
            // 白名单生效，可以访问trust网页
            this.controller.loadUrl('http://trust.example.com/test');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Access the untrust web')
        .onClick(() => {
          try {
            // 白名单生效，此时不可以访问untrust网页，并弹出错误页
            this.controller.loadUrl('http://untrust.example.com/test');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'http://untrust.example.com/test', controller: this.controller }).onControllerAttached(() => {
        try {
          // onControllerAttached回调中设置白名单，可以保证在加载URL之前生效，此时不可以访问untrust网页，并弹出错误页
          this.controller.setUrlTrustList(this.urltrustList);
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  urltrustList: string = "{\"UrlPermissionList\":[{\"scheme\":\"http\", \"host\":\"trust.example.com\", \"port\":80, \"path\":\"test\"}]}"

  build() {
    Column() {
      Button('Setting the trustlist')
        .onClick(() => {
          try {
            // 设置白名单，只允许访问trust网页。
            this.controller.setUrlTrustList(this.urltrustList);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Cancel the trustlist.')
        .onClick(() => {
          try {
            // 白名单传入空字符串表示关闭白名单机制，所有URL都可以允许访问。
            this.controller.setUrlTrustList("");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Access the trust web')
        .onClick(() => {
          try {
            // 白名单生效，可以访问trust网页。
            this.controller.loadUrl('http://trust.example.com/test');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Access the untrust web')
        .onClick(() => {
          try {
            // 白名单生效，此时不可以访问untrust网页，并弹出错误页。
            this.controller.loadUrl('http://untrust.example.com/test');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'http://untrust.example.com/test', controller: this.controller }).onControllerAttached(() => {
        try {
          // onControllerAttached回调中设置白名单，可以保证在加载URL之前生效，此时不可以访问untrust网页，并弹出错误页。
          this.controller.setUrlTrustList(this.urltrustList);
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
    }
  }
}
```

ArkTS-Dyn示例：

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
            // 设置白名单，只允许访问trust网页
            this.controller.setUrlTrustList(this.urltrustList);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Setting the wildcardlist')
        .onClick(() => {
          try {
            // 设置通配符白名单，所有URL都可以允许访问
            this.controller.setUrlTrustList(this.urlWildcardList, true, true);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Cancel the trustlist.')
        .onClick(() => {
          try {
            // 白名单传入空字符串表示关闭白名单机制，所有URL都可以允许访问
            this.controller.setUrlTrustList("");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Access the trust web')
        .onClick(() => {
          try {
            // 白名单生效，可以访问trust网页
            this.controller.loadUrl('http://trust.example.com/test');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Access the untrust web')
        .onClick(() => {
          try {
            // 白名单生效，此时不可以访问untrust网页，并弹出错误页
            this.controller.loadUrl('http://untrust.example.com/test');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'http://untrust.example.com/test', controller: this.controller }).onControllerAttached(() => {
        try {
          // onControllerAttached回调中设置白名单，可以保证在加载URL之前生效，此时不可以访问untrust网页，并弹出错误页
          this.controller.setUrlTrustList(this.urltrustList);
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  urltrustList: string = "{\"UrlPermissionList\":[{\"scheme\":\"http\", \"host\":\"trust.example.com\", \"path\":\"test\"}]}"
  urlWildcardList: string = "{\"UrlPermissionList\":[{\"scheme\":\"http\", \"host\":\"*.example.com\", \"path\":\"*\"]}]}"

  build() {
    Column() {
      Button('Setting trustlist')
        .onClick(() => {
          try {
            // 设置白名单，只允许访问trust网页
            this.controller.setUrlTrustList(this.urltrustList);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Setting wildcardlist')
        .onClick(() => {
          try {
            // 设置通配符白名单，所有URL都可以允许访问
            this.controller.setUrlTrustList(this.urlWildcardList, true, true);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Cancel trustlist.')
        .onClick(() => {
          try {
            // 白名单传入空字符串表示关闭白名单机制，所有URL都可以允许访问
            this.controller.setUrlTrustList("");
          } catcharing (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Access trust web')
        .onClick(() => {
          try {
            // 白名单生效，可以访问trust网页
            this.controller.loadUrl('http://trust.example.com/test');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Access untrust web')
        .onClick(() => {
          try {
            // 白名单生效，此时不可以访问untrust网页，并弹出错误页
            this.controller.loadUrl('http://untrust.example.com/test');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'http://untrust.example.com/test', controller: this.controller }).onControllerAttached(() => {
        try {
          // onControllerAttached回调中设置白名单，可以保证在加载URL之前生效，此时不可以访问untrust网页，并弹出错误页
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-setUrlTrustList(urlTrustList: string): void--><!--Device-WebviewController-setUrlTrustList(urlTrustList: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| urlTrustList | string | 是 | the URL trust list in JSON format. An empty string means that all URLs are allowed to access. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Parameter string is too long. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

参见 [setUrlTrustList](#seturltrustlist)

## setUserAgentClientHintsEnabled

```TypeScript
static setUserAgentClientHintsEnabled(enabled: boolean): void
```

Enable the User-Agent Client Hints.

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WebviewController-static setUserAgentClientHintsEnabled(enabled: boolean): void--><!--Device-WebviewController-static setUserAgentClientHintsEnabled(enabled: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | User-Agent Client Hints will enabled when set true. @static |

**示例**

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

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Entry, Column, Component, Button, ClickEvent, Web } from '@kit.ArkUI';
import { State } from '@ohos.arkui.stateManagement'
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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
              console.info("MajorVersion:" + versionList[i].getMajorVersion());
              console.info("FullVersion:" + versionList[i].getFullVersion());
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static setUserAgentForHosts(userAgent: string, hosts : Array<string>) : void--><!--Device-WebviewController-static setUserAgentForHosts(userAgent: string, hosts : Array<string>) : void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userAgent | string | 是 | The User-Agent string. |
| hosts | Array&lt;string&gt; | 是 | The hosts to which the User-Agent apply. @static |

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { webview } from '@kit.ArkWeb';
import { Entry, Column, Component, Web, Button, State } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

Sets the User-Agent metadata corresponding to the User-Agent.

<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> This User-Agent metadata will be used to populate the User-Agent client hints, They can provide the client's branding and version information, the underlying operating system's branding and major version, as well as details about the underlying device.

The User-Agent can be set with setCustomUserAgent or setAppCustomUserAgent or setUserAgentForHosts.

If the UserAgentMetadata is not found according to the overridden User-Agent and the overridden User-Agent contains the system default User-Agent, the system default value will be used.

If the UserAgentMetadata is not found according to the overridden User-Agent but the overridden User-Agent does not contain the system default User-Agent, only the low-entry User-Agent client hints will be generated. </p>

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WebviewController-setUserAgentMetadata(userAgent: string, metaData: UserAgentMetadata): void--><!--Device-WebviewController-setUserAgentMetadata(userAgent: string, metaData: UserAgentMetadata): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userAgent | string | 是 | The User-Agent string. |
| metaData | [UserAgentMetadata](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-useragentmetadata-c.md) | 是 | The UserAgentMetadata for the userAgent. |

**示例**

完整示例代码参考[setUserAgentClientHintsEnabled](#setuseragentclienthintsenabled)。

完整示例代码参考[setUserAgentClientHintsEnabled](#setuseragentclienthintsenabled)。

## setWebDebuggingAccess

```TypeScript
static setWebDebuggingAccess(webDebuggingAccess: boolean): void
```

Sets whether to enable web debugging. By default, web debugging is disabled. For details, see Debugging Frontend Pages by Using DevTools.

<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> Enabling web debugging allows users to check and modify the internal status of the web page, which poses security risks. Therefore, you are advised not to enable this function in the officially released version of the app. </p>

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static setWebDebuggingAccess(webDebuggingAccess: boolean): void--><!--Device-WebviewController-static setWebDebuggingAccess(webDebuggingAccess: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| webDebuggingAccess | boolean | 是 | Sets whether to enable web debugging.{@code true} enable web debugging;{@code false} disable web debugging. The default value is false. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static setWebDebuggingAccess(webDebuggingAccess: boolean, port: int): void--><!--Device-WebviewController-static setWebDebuggingAccess(webDebuggingAccess: boolean, port: int): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| webDebuggingAccess | boolean | 是 | { |
| port | int | 是 | Indicates the port of the devtools server. After the port is specified, a tcp server socket is created instead of a unix domain socket. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100023](../../apis-arkweb/errorcode-webview.md#17100023-使用了不被允许的端口号) | The port number is not within the allowed range. @static |

**示例**

参见 [setWebDebuggingAccess](#setwebdebuggingaccess)

## setWebDestroyMode

```TypeScript
static setWebDestroyMode(mode: WebDestroyMode): void
```

Set web destroy mode.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static setWebDestroyMode(mode: WebDestroyMode): void--><!--Device-WebviewController-static setWebDestroyMode(mode: WebDestroyMode): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [WebDestroyMode](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-webdestroymode-e.md) | 是 | web destroy mode, default NORMAL_MODE. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    // 设置快速销毁模式
    webview.WebviewController.setWebDestroyMode(webview.WebDestroyMode.FAST_MODE);
    AppStorage.setOrCreate("abilityWant", want);
    console.info("EntryAbility onCreate done");
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import UIAbility from '@ohos.app.ability.UIAbility';
import AbilityConstant from '@ohos.app.ability.AbilityConstant';
import Want from '@ohos.app.ability.Want';
import { AppStorage } from 'arkui.stateManagement.storage.appStorage';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    // 设置快速销毁模式
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-setWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void--><!--Device-WebviewController-setWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scheme | string | 是 | String value for url scheme. |
| handler | [WebSchemeHandler](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-webschemehandler-c.md) | 是 | Web scheme handler. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Incorrect parameter types. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-slideScroll(vx: double, vy: double): void--><!--Device-WebviewController-slideScroll(vx: double, vy: double): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vx | double | 是 | the x speed of the speed. The unit is vp/s. |
| vy | double | 是 | the y speed of the speed. The unit is vp/s. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Web, Column, Component, Entry, Button } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

加载的html文件。

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

开启当前网页摄像头捕获。使用摄像头功能前请在module.json5中添加权限: ohos.permission.CAMERA，具体权限的添加方法请参考 [在配置文件中声明权限](../../../security/AccessToken/declare-permissions.md#在配置文件中声明权限)。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-startCamera(): void--><!--Device-WebviewController-startCamera(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

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
      if (err) {
        console.error(`ErrorCode: ${err.code}, Message: ${err.message}`);
        return;
      }
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Web, Column, Component, Entry, Button, OnPermissionRequestEvent, Context } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { UIContext } from "@kit.ArkUI";
import { AlertDialogParamWithButtons, AlertDialogButtonBaseOptions } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { PermissionRequestResult, common, abilityAccessCtrl } from '@kit.AbilityKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  uiContext: UIContext = this.getUIContext();

  aboutToAppear(): void {
    let context: Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionsFromUser(context, ['ohos.permission.CAMERA'],
      (err: BusinessError | null, data?: PermissionRequestResult) => {
        if (err) {
          console.error(`ErrorCode: ${err.code}, Message: ${err.message}`);
          return;
        }
        if (data) {
          console.info('data:' + JSON.stringify(data));
          console.info('data permissions:' + data.permissions);
          console.info('data authResults:' + data.authResults);
        }
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
        .onPermissionRequest((event: OnPermissionRequestEvent): void => {
          if (event) {
            const dialogOptions: AlertDialogParamWithButtons = {
              title: 'title',
              message: 'text',
              primaryButton: {
                value: 'deny',
                action: () => {
                  event.request.deny();
                },
              } as AlertDialogButtonBaseOptions,
              secondaryButton: {
                value: 'onConfirm',
                action: () => {
                  event.request.grant(event.request.getAccessibleResource());
                },
              } as AlertDialogButtonBaseOptions,
              cancel: () => {
                event.request.deny();
              }
            };
            this.uiContext.showAlertDialog(dialogOptions);
          }
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
    <meta charset="UTF-8">
  </head>
  <body>
    <video id="video" width="400px" height="400px" autoplay>
    </video>
    <input type="button" title="HTML5摄像头" value="开启摄像头" onclick="getMedia()" />
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-startDownload(url: string): void--><!--Device-WebviewController-startDownload(url: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | The download url. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-url格式错误) | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2 *1024 *1024. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-stop(): void--><!--Device-WebviewController-stop(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

控制网页所有音视频停止。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-stopAllMedia(): void--><!--Device-WebviewController-stopAllMedia(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

停止当前网页摄像头捕获。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-stopCamera(): void--><!--Device-WebviewController-stopCamera(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

完整示例代码参考[startCamera](#startcamera)。

## stopMicrophone

```TypeScript
stopMicrophone(): void
```

停止当前网页麦克风捕获。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-stopMicrophone(): void--><!--Device-WebviewController-stopMicrophone(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

完整示例代码参考[resumeMicrophone](#resumemicrophone)。

## storeWebArchive

```TypeScript
storeWebArchive(baseName: string, autoName: boolean): Promise<string>
```

Stores the current page as a web archive.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-storeWebArchive(baseName: string, autoName: boolean): Promise<string>--><!--Device-WebviewController-storeWebArchive(baseName: string, autoName: boolean): Promise<string>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| baseName | string | 是 | Where the generated offline webpage is stored, This value cannot be null. |
| autoName | boolean | 是 | Decide whether to automatically generate the file name. If false, it is stored by the file name of baseName. If true, the file name is automatically generated based on the current URL and stored in the file directory of baseName. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | a promise resolved after the web archive has been stored. The parameter will either be the filename under which the file was stored, or empty if storing the file failed. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3. Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |
| [17100003](../../apis-arkweb/errorcode-webview.md#17100003-resource路径错误) | Invalid resource path or file type. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Button('storeWebArchive')
        .onClick(() => {
          try {
            this.controller.storeWebArchive("/data/storage/el2/base/", true,
              (error: BusinessError<void> | null | undefined, filename: String | undefined) => {
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
              .catch((error: Error) => {
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-storeWebArchive(baseName: string, autoName: boolean, callback: AsyncCallback<string>): void--><!--Device-WebviewController-storeWebArchive(baseName: string, autoName: boolean, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| baseName | string | 是 | Where the generated offline webpage is stored, This value cannot be null. |
| autoName | boolean | 是 | Decide whether to automatically generate the file name. If false, it is stored by the file name of baseName. If true, the file name is automatically generated based on the current URL and stored in the file directory of baseName. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 | called after the web archive has been stored. The parameter will either be the filename under which the file was stored, or empty if storing the file failed. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3. Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |
| [17100003](../../apis-arkweb/errorcode-webview.md#17100003-resource路径错误) | Invalid resource path or file type. |

**示例**

参见 [storeWebArchive](#storewebarchive)

## terminateRenderProcess

```TypeScript
terminateRenderProcess(): boolean
```

Destroy the rendering process. Calling this interface will actively destroy the associated rendering process. If the rendering process has not been started or destroyed, it has no effect. In addition, destroying the rendering process will also affect all other instances associated with the rendering process.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-terminateRenderProcess(): boolean--><!--Device-WebviewController-terminateRenderProcess(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if it was possible to terminate the render process, otherwise false. Calling this on a not yet started, or an already terminated render will have no effect. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Column, Component, Button, Web } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct webViewController {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Button('terminateRenderProcess')
        .onClick(() => {
          const result: boolean = this.controller.terminateRenderProcess();
          console.info("terminateRenderProcess result: " + result);
        });
      Web({
        src: 'www.example.com', controller: this.controller,
      })
    }
  }
}
```

## trimMemoryByPressureLevel

```TypeScript
static trimMemoryByPressureLevel(level: PressureLevel): void
```

Trim memory by different memory pressure level.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static trimMemoryByPressureLevel(level: PressureLevel): void--><!--Device-WebviewController-static trimMemoryByPressureLevel(level: PressureLevel): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| level | [PressureLevel](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-pressurelevel-e.md) | 是 | The memory pressure level for the ArkWeb. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Parameter string is too long. 3.Parameter verification failed. |

**示例**

ArkTS-Dyn示例：

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
              // 设置当前内存压力等级为适中，释放少量内存
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column, Row, Button } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  build() {
    Column() {
      Row() {
        Button('trim_Memory')
          .onClick(() => {
            try {
              // 设置当前内存压力等级为适中，释放少量内存。
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-waitForAttached(timeout: int): Promise<ControllerAttachState>--><!--Device-WebviewController-waitForAttached(timeout: int): Promise<ControllerAttachState>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeout | int | 是 | the wait timeout, if timeout reach, promise will return, the unit is millisecond. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[ControllerAttachState](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-controllerattachstate-e.md)&gt; | Promise used to return the state of attach. |

**示例**

ArkTS-Dyn示例:

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
        // 绑定完成或者超时都会触发回调
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

ArkTS-Sta示例:

```TypeScript
// xxx.ets
import { Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  aboutToAppear() {
    this.controller.waitForAttached(1000).then((state: webview.ControllerAttachState) => {
      if (state == webview.ControllerAttachState.ATTACHED) {
        // 绑定完成或者超时都会触发回调。
        console.info('Controller is attached.');
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

## warmupServiceWorker

```TypeScript
static warmupServiceWorker(url: string): void
```

Warmup the registered service worker associated the url.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-static warmupServiceWorker(url: string): void--><!--Device-WebviewController-static warmupServiceWorker(url: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | The url. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-url格式错误) | URL error. The webpage corresponding to the URL is invalid, or the URL length exceeds 2048. |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// EntryAbility.ets
'use static'
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { AppStorage } from '@kit.ArkUI';

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

Web page snapshot.

<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> Only screenshots of assets on the rendering process are supported: still images and text. If there is a video on the page, the placeholder image of the video will be displayed when you take a screenshot, and blank if there is no placeholder. </p>

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-webPageSnapshot(info: SnapshotInfo, callback: AsyncCallback<SnapshotResult>): void--><!--Device-WebviewController-webPageSnapshot(info: SnapshotInfo, callback: AsyncCallback<SnapshotResult>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [SnapshotInfo](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-snapshotinfo-i.md) | 是 | The snapshot info. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SnapshotResult](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-snapshotresult-i.md)&gt; | 是 | the callback of snapshot. |

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
                // 开发者可以根据需要处理返回结果
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Column, Component, Button, Web } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
                // 开发者可以根据需要处理返回结果
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-zoom(factor: double): void--><!--Device-WebviewController-zoom(factor: double): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| factor | double | 是 | Relative zoom ratio. The value must be greater than 0. The value 1 indicates that the page is not zoomed. A value smaller than 1 indicates zoom-out, and a value greater than 1 indicates zoom-in. <br>Value range: (0, 100]. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |
| [17100004](../../apis-arkweb/errorcode-webview.md#17100004-功能开关未打开) | Function not enabled. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'

import { Web, Column, Component, Entry, Button, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-zoomIn(): void--><!--Device-WebviewController-zoomIn(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |
| [17100004](../../apis-arkweb/errorcode-webview.md#17100004-功能开关未打开) | Function not enabled. |

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, Button } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebviewController-zoomOut(): void--><!--Device-WebviewController-zoomOut(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) | Init error. The WebviewController must be associated with a Web component. |
| [17100004](../../apis-arkweb/errorcode-webview.md#17100004-功能开关未打开) | Function not enabled. |

**示例**

ArkTS-Dyn示例

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, Button } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

