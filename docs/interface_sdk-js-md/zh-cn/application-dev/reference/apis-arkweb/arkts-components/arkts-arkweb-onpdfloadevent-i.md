# OnPdfLoadEvent

定义PDF加载成功或失败时触发的函数。

**起始版本：** 20

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
import { WebNetErrorList } from '@ohos.@kit.ArkWeb.netErrorList';
import WebNativeMessagingExtensionAbility, { ConnectionInfo } from '@ohos.@kit.ArkWeb.WebNativeMessagingExtensionAbility';
import @kit.ArkWebNativeMessagingExtensionManager from '@ohos.@kit.ArkWeb.@kit.ArkWebNativeMessagingExtensionManager';
```

## result

```TypeScript
result: PdfLoadResult
```

PDF页面加载结果。

**类型：** [PdfLoadResult](arkts-arkweb-pdfloadresult-e.md)

**起始版本：** 20

**系统能力：** SystemCapability.Web.Webview.Core

## url

```TypeScript
url: string
```

页面的URL地址。

**类型：** string

**起始版本：** 20

**系统能力：** SystemCapability.Web.Webview.Core
