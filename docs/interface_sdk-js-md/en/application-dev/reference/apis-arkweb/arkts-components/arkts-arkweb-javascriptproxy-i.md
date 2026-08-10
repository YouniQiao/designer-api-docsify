# JavaScriptProxy

定义要注入的JavaScript对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface JavaScriptProxy--><!--Device-unnamed-declare interface JavaScriptProxy-End-->

**System capability:** SystemCapability.Web.Webview.Core

## asyncMethodList

```TypeScript
asyncMethodList?: Array<string>
```

参与注册的应用侧JavaScript对象的异步方法。异步方法无法获取返回值。

**Type:** Array&lt;string&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-JavaScriptProxy-asyncMethodList?: Array<string>--><!--Device-JavaScriptProxy-asyncMethodList?: Array<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## controller

```TypeScript
controller: WebController | WebviewController
```

Controller.

**Type:** [WebController](arkts-arkweb-webcontroller-c.md) \| WebviewController

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-JavaScriptProxy-controller: WebController | WebviewController--><!--Device-JavaScriptProxy-controller: WebController | WebviewController-End-->

**System capability:** SystemCapability.Web.Webview.Core

## methodList

```TypeScript
methodList: Array<string>
```

参与注册的应用侧JavaScript对象的同步方法。

**Type:** Array&lt;string&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-JavaScriptProxy-methodList: Array<string>--><!--Device-JavaScriptProxy-methodList: Array<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## name

```TypeScript
name: string
```

注册对象的名称，与window中调用的对象名一致。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-JavaScriptProxy-name: string--><!--Device-JavaScriptProxy-name: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## object

```TypeScript
object: object
```

参与注册的对象。

**Type:** object

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-JavaScriptProxy-object: object--><!--Device-JavaScriptProxy-object: object-End-->

**System capability:** SystemCapability.Web.Webview.Core

## permission

```TypeScript
permission?: string
```

permission configuration defining web page URLs that can access JavaScriptProxy methods.The configuration can be defined at two levels, object level and method level.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-JavaScriptProxy-permission?: string--><!--Device-JavaScriptProxy-permission?: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

