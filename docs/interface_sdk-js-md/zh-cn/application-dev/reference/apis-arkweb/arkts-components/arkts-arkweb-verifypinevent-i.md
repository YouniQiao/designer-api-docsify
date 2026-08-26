# VerifyPinEvent

定义当需要用户进行PIN码认证时触发回调。

**起始版本：** 22

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
import { WebNetErrorList } from '@ohos.@kit.ArkWeb.netErrorList';
import WebNativeMessagingExtensionAbility, { ConnectionInfo } from '@ohos.@kit.ArkWeb.WebNativeMessagingExtensionAbility';
import @kit.ArkWebNativeMessagingExtensionManager from '@ohos.@kit.ArkWeb.@kit.ArkWebNativeMessagingExtensionManager';
```

## handler

```TypeScript
handler: VerifyPinHandler
```

通知Web组件用户操作行为。

**类型：** [VerifyPinHandler](arkts-arkweb-verifypinhandler-c.md)

**起始版本：** 22

**系统能力：** SystemCapability.Web.Webview.Core

## identity

```TypeScript
identity: string
```

用于认证的证书凭据标识。

**类型：** string

**起始版本：** 22

**系统能力：** SystemCapability.Web.Webview.Core
