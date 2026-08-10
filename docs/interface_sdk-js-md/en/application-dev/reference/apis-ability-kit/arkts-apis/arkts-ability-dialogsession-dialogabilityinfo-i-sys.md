# DialogAbilityInfo (System API)

提供会话组件信息，包括包名、模块名、组件名等信息。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-dialogSession-export interface DialogAbilityInfo--><!--Device-dialogSession-export interface DialogAbilityInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { dialogSession } from 'kits/@kit.AbilityKit';
```

## abilityIconId

```TypeScript
abilityIconId: int
```

表示Ability图标ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogAbilityInfo-abilityIconId: int--><!--Device-DialogAbilityInfo-abilityIconId: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## abilityLabelId

```TypeScript
abilityLabelId: int
```

表示Ability标签ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogAbilityInfo-abilityLabelId: int--><!--Device-DialogAbilityInfo-abilityLabelId: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## abilityName

```TypeScript
abilityName: string
```

表示组件名。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogAbilityInfo-abilityName: string--><!--Device-DialogAbilityInfo-abilityName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## appIndex

```TypeScript
appIndex: int
```

表示应用的分身索引。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogAbilityInfo-appIndex: int--><!--Device-DialogAbilityInfo-appIndex: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## bundleIconId

```TypeScript
bundleIconId: int
```

表示Bundle图标ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogAbilityInfo-bundleIconId: int--><!--Device-DialogAbilityInfo-bundleIconId: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## bundleLabelId

```TypeScript
bundleLabelId: int
```

表示Bundle标签ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogAbilityInfo-bundleLabelId: int--><!--Device-DialogAbilityInfo-bundleLabelId: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName: string
```

表示包名。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogAbilityInfo-bundleName: string--><!--Device-DialogAbilityInfo-bundleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## codePath

```TypeScript
codePath?: string
```

表示应用程序的安装目录。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogAbilityInfo-codePath?: string--><!--Device-DialogAbilityInfo-codePath?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## installSource

```TypeScript
installSource?: string
```

表示应用程序的安装来源，支持的取值如下：

- pre-installed：表示首次开机时安装的预置应用。  
- ota：表示系统升级时新增的预置应用。  
- recovery：表示用户卸载后又手动恢复的预置应用。  
- bundleName：表示由此包名对应的应用安装。该bundleName代表变量，以实际值为准。  
- unknown：表示应用安装来源未知。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogAbilityInfo-installSource?: string--><!--Device-DialogAbilityInfo-installSource?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## moduleName

```TypeScript
moduleName: string
```

表示模块名。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogAbilityInfo-moduleName: string--><!--Device-DialogAbilityInfo-moduleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## multiAppMode

```TypeScript
multiAppMode: MultiAppMode
```

表示应用的多开模式。

**Type:** [MultiAppMode](arkts-ability-applicationinfo-multiappmode-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogAbilityInfo-multiAppMode: MultiAppMode--><!--Device-DialogAbilityInfo-multiAppMode: MultiAppMode-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## visible

```TypeScript
visible: boolean
```

表示Ability是否可见。true表示Ability可见，false表示Ability不可见。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogAbilityInfo-visible: boolean--><!--Device-DialogAbilityInfo-visible: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

