# OnLoadStartedEvent

定义网页加载开始时触发的回调信息，包括页面URL。适用于需要监控页面加载开始的场景，提升页面生命周期的管理能力。

**起始版本：** 20

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
import { WebNetErrorList } from '@ohos.@kit.ArkWeb.netErrorList';
import WebNativeMessagingExtensionAbility, { ConnectionInfo } from '@ohos.@kit.ArkWeb.WebNativeMessagingExtensionAbility';
import @kit.ArkWebNativeMessagingExtensionManager from '@ohos.@kit.ArkWeb.@kit.ArkWebNativeMessagingExtensionManager';
```

## url

```TypeScript
url: string
```

页面的URL地址。

**类型：** string

**起始版本：** 20

**系统能力：** SystemCapability.Web.Webview.Core
