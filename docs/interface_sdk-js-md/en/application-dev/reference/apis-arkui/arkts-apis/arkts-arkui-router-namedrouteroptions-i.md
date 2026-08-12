# NamedRouterOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-router-interface NamedRouterOptions--><!--Device-router-interface NamedRouterOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { router } from '@kit.ArkUI';
```

## name

```TypeScript
name: string
```

Name of the destination named route.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NamedRouterOptions-name: string--><!--Device-NamedRouterOptions-name: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## params

```TypeScript
params?: Object
```

Data that needs to be passed to the destination page during navigation.

**Type:** Object

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NamedRouterOptions-params?: Object--><!--Device-NamedRouterOptions-params?: Object-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## recoverable

```TypeScript
recoverable?: boolean
```

Set router page stack can be recovered after application is destroyed. When router page stack is recovered,top page will be recovered, other page recovered when it backs. the default value is 'true'.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NamedRouterOptions-recoverable?: boolean--><!--Device-NamedRouterOptions-recoverable?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

