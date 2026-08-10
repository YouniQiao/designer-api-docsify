# ElementName

应用组件结构体，包含bundleName、moduleName和abilityName等。通常用于组件启动信息  
[AbilityRunningInfo.ability](arkts-ability-abilityrunninginfo-i.md)和组件启动回调函数  
[connectOptions.onConnect](arkts-ability-connectoptions-connectoptions-i.md#onconnect)中。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface ElementName--><!--Device-unnamed-export interface ElementName-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## abilityName

```TypeScript
abilityName: string
```

Ability名称。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ElementName-abilityName: string--><!--Device-ElementName-abilityName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## bundleName

```TypeScript
bundleName: string
```

应用Bundle名称。

**Type:** string

**Default:** Indicates bundle name

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ElementName-bundleName: string--><!--Device-ElementName-bundleName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## deviceId

```TypeScript
deviceId?: string
```

设备ID。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ElementName-deviceId?: string--><!--Device-ElementName-deviceId?: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## moduleName

```TypeScript
moduleName?: string
```

Ability所属的HAP的模块名称。

**Type:** string

**Default:** Indicates module name

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ElementName-moduleName?: string--><!--Device-ElementName-moduleName?: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## shortName

```TypeScript
shortName?: string
```

Ability短名称，以“.”为开头的字符串。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ElementName-shortName?: string--><!--Device-ElementName-shortName?: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## uri

```TypeScript
uri?: string
```

资源标识符。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ElementName-uri?: string--><!--Device-ElementName-uri?: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

