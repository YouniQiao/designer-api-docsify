# KeepAliveBundleInfo (System API)

定义应用保活信息，可以通过[getKeepAliveBundles](arkts-ability-appmanager-getkeepalivebundles-f-sys.md#getkeepalivebundles)或  
[getKeepAliveAppServiceExtensions](arkts-ability-appmanager-getkeepaliveappserviceextensions-f-sys.md#getkeepaliveappserviceextensions)获取。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-appManager-export interface KeepAliveBundleInfo--><!--Device-appManager-export interface KeepAliveBundleInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## allowUserToCancel

```TypeScript
allowUserToCancel?: boolean
```

表示是否允许用户取消保活。true表示允许，false表示不允许。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-KeepAliveBundleInfo-allowUserToCancel?: boolean--><!--Device-KeepAliveBundleInfo-allowUserToCancel?: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName: string
```

Bundle名称。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-KeepAliveBundleInfo-bundleName: string--><!--Device-KeepAliveBundleInfo-bundleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## setter

```TypeScript
setter: KeepAliveSetter
```

表示应用保活设置者类型。

**Type:** [KeepAliveSetter](arkts-ability-appmanager-keepalivesetter-e-sys.md)

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-KeepAliveBundleInfo-setter: KeepAliveSetter--><!--Device-KeepAliveBundleInfo-setter: KeepAliveSetter-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## setterUserId

```TypeScript
setterUserId?: int
```

应用保活设置者的用户ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-KeepAliveBundleInfo-setterUserId?: int--><!--Device-KeepAliveBundleInfo-setterUserId?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## type

```TypeScript
type: KeepAliveAppType
```

表示被保活应用的应用类型。

**Type:** [KeepAliveAppType](arkts-ability-appmanager-keepaliveapptype-e-sys.md)

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-KeepAliveBundleInfo-type: KeepAliveAppType--><!--Device-KeepAliveBundleInfo-type: KeepAliveAppType-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

