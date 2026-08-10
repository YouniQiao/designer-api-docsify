# HapModuleInfo

Hap模块信息，未做特殊说明的属性，均通过  
[bundle.getBundleInfo](arkts-ability-bundle-getbundleinfo-f.md#getbundleinfo)获取。

> **说明：**
> 
> 从API version 9开始，该模块不再维护，建议使用[bundleManager-HapModuleInfo](arkts-ability-hapmoduleinfo-hapmoduleinfo-depr-i.md)替代。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [hapModuleInfo:HapModuleInfo](arkts-ability-hapmoduleinfo-hapmoduleinfo-depr-i.md)

<!--Device-unnamed-export interface HapModuleInfo--><!--Device-unnamed-export interface HapModuleInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## abilityInfo

```TypeScript
readonly abilityInfo: Array<AbilityInfo>
```

Ability信息。

**Type:** Array&lt;[AbilityInfo](arkts-ability-abilityinfo-abilityinfo-depr-i.md)&gt;

**Default:** Obtains configuration information about ability

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.HapModuleInfo#abilitiesInfo

<!--Device-HapModuleInfo-readonly abilityInfo: Array<AbilityInfo>--><!--Device-HapModuleInfo-readonly abilityInfo: Array<AbilityInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## backgroundImg

```TypeScript
readonly backgroundImg: string
```

模块背景图片。

**Type:** string

**Default:** Indicates the background img of this hapmodule

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-HapModuleInfo-readonly backgroundImg: string--><!--Device-HapModuleInfo-readonly backgroundImg: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## description

```TypeScript
readonly description: string
```

模块描述信息。

**Type:** string

**Default:** Describes the hapmodule

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.HapModuleInfo#description

<!--Device-HapModuleInfo-readonly description: string--><!--Device-HapModuleInfo-readonly description: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## descriptionId

```TypeScript
readonly descriptionId: number
```

描述信息ID。

**Type:** number

**Default:** Indicates the description of this hapmodule

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.HapModuleInfo#descriptionId

<!--Device-HapModuleInfo-readonly descriptionId: number--><!--Device-HapModuleInfo-readonly descriptionId: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## deviceTypes

```TypeScript
readonly deviceTypes: Array<string>
```

支持运行的设备类型。

**Type:** Array&lt;string&gt;

**Default:** The device types that this hapmodule can run on

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.HapModuleInfo#deviceTypes

<!--Device-HapModuleInfo-readonly deviceTypes: Array<string>--><!--Device-HapModuleInfo-readonly deviceTypes: Array<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## icon

```TypeScript
readonly icon: string
```

模块图标。

**Type:** string

**Default:** Indicates the icon of this hapmodule

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.HapModuleInfo#icon

<!--Device-HapModuleInfo-readonly icon: string--><!--Device-HapModuleInfo-readonly icon: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## iconId

```TypeScript
readonly iconId: number
```

模块图标ID。

**Type:** number

**Default:** Indicates the icon id of this hapmodule

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.HapModuleInfo#iconId

<!--Device-HapModuleInfo-readonly iconId: number--><!--Device-HapModuleInfo-readonly iconId: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## installationFree

```TypeScript
readonly installationFree: boolean
```

是否支持免安装，取值为true表示支持免安装，取值为false表示不支持免安装。

**Type:** boolean

**Default:** Indicates whether free installation of the hapmodule is supported

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.HapModuleInfo#installationFree

<!--Device-HapModuleInfo-readonly installationFree: boolean--><!--Device-HapModuleInfo-readonly installationFree: boolean-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## label

```TypeScript
readonly label: string
```

模块标签。

**Type:** string

**Default:** Indicates the label of this hapmodule

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.HapModuleInfo#label

<!--Device-HapModuleInfo-readonly label: string--><!--Device-HapModuleInfo-readonly label: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## labelId

```TypeScript
readonly labelId: number
```

模块标签ID。

**Type:** number

**Default:** Indicates the label id of this hapmodule

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.HapModuleInfo#labelId

<!--Device-HapModuleInfo-readonly labelId: number--><!--Device-HapModuleInfo-readonly labelId: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## mainAbilityName

```TypeScript
readonly mainAbilityName: string
```

入口Ability名称。

**Type:** string

**Default:** Indicates the main ability name of this hapmodule

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-HapModuleInfo-readonly mainAbilityName: string--><!--Device-HapModuleInfo-readonly mainAbilityName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## moduleName

```TypeScript
readonly moduleName: string
```

模块名。

**Type:** string

**Default:** Indicates the name of the .hap package to which the capability belongs

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.HapModuleInfo#name

<!--Device-HapModuleInfo-readonly moduleName: string--><!--Device-HapModuleInfo-readonly moduleName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## name

```TypeScript
readonly name: string
```

模块名称。

**Type:** string

**Default:** Indicates the name of this hapmodule

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.HapModuleInfo#name

<!--Device-HapModuleInfo-readonly name: string--><!--Device-HapModuleInfo-readonly name: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## reqCapabilities

```TypeScript
readonly reqCapabilities: Array<string>
```

模块运行需要的能力。

**Type:** Array&lt;string&gt;

**Default:** Indicates the req capabilities of this hapmodule

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-HapModuleInfo-readonly reqCapabilities: Array<string>--><!--Device-HapModuleInfo-readonly reqCapabilities: Array<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## supportedModes

```TypeScript
readonly supportedModes: number
```

模块支持的模式。

**Type:** number

**Default:** Indicates the supported modes of this hapmodule

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-HapModuleInfo-readonly supportedModes: number--><!--Device-HapModuleInfo-readonly supportedModes: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

