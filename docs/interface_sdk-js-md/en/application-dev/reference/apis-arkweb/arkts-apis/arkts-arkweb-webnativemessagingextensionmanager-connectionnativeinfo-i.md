# ConnectionNativeInfo

表示Web原生消息连接的连接信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-webNativeMessagingExtensionManager-interface ConnectionNativeInfo--><!--Device-webNativeMessagingExtensionManager-interface ConnectionNativeInfo-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webNativeMessagingExtensionManager } from 'kits/@kit.ArkWeb';
```

## bundleName

```TypeScript
bundleName: string
```

Web原生消息扩展应用的包名。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectionNativeInfo-bundleName: string--><!--Device-ConnectionNativeInfo-bundleName: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## connectionId

```TypeScript
connectionId: int
```

Web原生消息扩展连接的唯一标识，由connectNative方法返回，用于标识和管理连接。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectionNativeInfo-connectionId: int--><!--Device-ConnectionNativeInfo-connectionId: int-End-->

**System capability:** SystemCapability.Web.Webview.Core

## extensionOrigin

```TypeScript
extensionOrigin: string
```

浏览器扩展的源URL。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectionNativeInfo-extensionOrigin: string--><!--Device-ConnectionNativeInfo-extensionOrigin: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## extensionPid

```TypeScript
extensionPid: int
```

Web原生消息扩展的进程ID。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectionNativeInfo-extensionPid: int--><!--Device-ConnectionNativeInfo-extensionPid: int-End-->

**System capability:** SystemCapability.Web.Webview.Core

