# RouterOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-router-interface RouterOptions--><!--Device-router-interface RouterOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

## Modules to Import

```TypeScript
import { router } from '@kit.ArkUI';
```

## params

```TypeScript
params?: Object
```

Data that needs to be passed to the destination page during navigation. After the destination page is displayed, the parameter can be directly used for the page.

**Type:** Object

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RouterOptions-params?: Object--><!--Device-RouterOptions-params?: Object-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

## recoverable

```TypeScript
recoverable?: boolean
```

Set router page stack can be recovered after application is destroyed. When router page stack is recovered, top page will be recovered, other page recovered when it backs. the default value is 'true'.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-RouterOptions-recoverable?: boolean--><!--Device-RouterOptions-recoverable?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

## url

```TypeScript
url: string
```

URI of the destination page, which supports the following formats:
1. Absolute path of the page, which is provided by the pages list in the config.json file.
Example: pages/index/index pages/detail/detail
2. Particular path. If the URI is a slash (/), the home page is displayed.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-RouterOptions-url: string--><!--Device-RouterOptions-url: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

