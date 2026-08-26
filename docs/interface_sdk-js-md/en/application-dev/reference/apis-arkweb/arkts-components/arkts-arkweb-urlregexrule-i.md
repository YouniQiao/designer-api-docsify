# UrlRegexRule

Defines the URL regular expression rule.

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { WebNetErrorList } from '@ohos.@kit.ArkWeb.netErrorList';
import WebNativeMessagingExtensionAbility, { ConnectionInfo } from '@ohos.@kit.ArkWeb.WebNativeMessagingExtensionAbility';
import @kit.ArkWebNativeMessagingExtensionManager from '@ohos.@kit.ArkWeb.@kit.ArkWebNativeMessagingExtensionManager';
```

## rule

```TypeScript
rule : string
```

URL regular expression. URL regular expression matching is performed only after **secondLevelDomain** is matched successfully.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

## secondLevelDomain

```TypeScript
secondLevelDomain : string
```

Exact match of the second-level domain. For example, the second-level domain name of "https://www.example.com" is **example.com**, and that of "https://www.example.com.cn" is **example.com.cn**. If the URL does not have a second- level domain name, the value is empty.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core
