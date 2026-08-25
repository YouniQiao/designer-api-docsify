# JavaScriptProxy

Defines the JavaScript object to be injected.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## asyncMethodList

```TypeScript
asyncMethodList?: Array<string>
```

The async method of the application side JavaScript object participating in the registration.

**Type:** Array&lt;string&gt;

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## controller

```TypeScript
controller: WebviewController
```

Controller.

**Type:** [WebviewController](arkts-arkweb-webviewcontroller-t.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## jsObject

```TypeScript
jsObject: object
```

Objects participating in registration.

**Type:** object

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## methodList

```TypeScript
methodList: Array<string>
```

The method of the application side JavaScript object participating in the registration.

**Type:** Array&lt;string&gt;

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## name

```TypeScript
name: string
```

The name of the registered object, which is consistent with the object name called in the window.

**Type:** string

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## permission

```TypeScript
permission?: string
```

permission configuration defining web page URLs that can access JavaScriptProxy methods. The configuration can be defined at two levels, object level and method level.

**Type:** string

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core
