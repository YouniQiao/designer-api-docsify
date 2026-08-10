# AbilityInfo

Ability信息，未做特殊说明的属性，均通过  
[bundle.getAbilityInfo](arkts-ability-bundle-getabilityinfo-f.md#getabilityinfo)获取。

> **说明：**
> 
> 从API version 9开始，该模块不再维护，建议使用[bundleManager-AbilityInfo](arkts-ability-abilityinfo-abilityinfo-depr-i.md)替代。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [abilityInfo:AbilityInfo](arkts-ability-abilityinfo-abilityinfo-depr-i.md)

<!--Device-unnamed-export interface AbilityInfo--><!--Device-unnamed-export interface AbilityInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## applicationInfo

```TypeScript
readonly applicationInfo: ApplicationInfo
```

应用程序的配置信息。

通过调用[bundle.getAbilityInfo](arkts-ability-bundle-getabilityinfo-f.md#getabilityinfo)接口时，传入GET_ABILITY_INFO_WITH_APPLICATION获取。

**Type:** [ApplicationInfo](arkts-ability-applicationinfo-applicationinfo-depr-i.md)

**Default:** Obtains configuration information about an application

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.AbilityInfo#applicationInfo

<!--Device-AbilityInfo-readonly applicationInfo: ApplicationInfo--><!--Device-AbilityInfo-readonly applicationInfo: ApplicationInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## backgroundModes

```TypeScript
readonly backgroundModes: number
```

表示后台服务的类型。

**模型约束：** 此接口仅可在FA模型下使用。

**Type:** number

**Default:** Indicates the background service addressing a specific usage scenario

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Model restriction:** This API can be used only in the FA model.

<!--Device-AbilityInfo-readonly backgroundModes: number--><!--Device-AbilityInfo-readonly backgroundModes: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## bundleName

```TypeScript
readonly bundleName: string
```

应用Bundle名称。

**Type:** string

**Default:** Indicates the name of the bundle containing the ability

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.AbilityInfo#bundleName

<!--Device-AbilityInfo-readonly bundleName: string--><!--Device-AbilityInfo-readonly bundleName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## description

```TypeScript
readonly description: string
```

Ability的描述。

**Type:** string

**Default:** Describes the ability

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.AbilityInfo#description

<!--Device-AbilityInfo-readonly description: string--><!--Device-AbilityInfo-readonly description: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## descriptionId

```TypeScript
readonly descriptionId: number
```

Ability的描述的资源id值。

**Type:** number

**Default:** Indicates the description id of the ability

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.AbilityInfo#descriptionId

<!--Device-AbilityInfo-readonly descriptionId: number--><!--Device-AbilityInfo-readonly descriptionId: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## deviceCapabilities

```TypeScript
readonly deviceCapabilities: Array<string>
```

Ability需要的设备能力。

**Type:** Array&lt;string&gt;

**Default:** The device capability that this ability needs

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-AbilityInfo-readonly deviceCapabilities: Array<string>--><!--Device-AbilityInfo-readonly deviceCapabilities: Array<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## deviceTypes

```TypeScript
readonly deviceTypes: Array<string>
```

Ability支持的设备类型。

**Type:** Array&lt;string&gt;

**Default:** The device types that this ability can run on

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.AbilityInfo#deviceTypes

<!--Device-AbilityInfo-readonly deviceTypes: Array<string>--><!--Device-AbilityInfo-readonly deviceTypes: Array<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## enabled

```TypeScript
readonly enabled: boolean
```

Ability是否可用，取值为true表示Ability可用，取值为false表示Ability不可用。

**Type:** boolean

**Default:** Indicates whether the ability is enabled

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.AbilityInfo#enabled

<!--Device-AbilityInfo-readonly enabled: boolean--><!--Device-AbilityInfo-readonly enabled: boolean-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## formEnabled

```TypeScript
readonly formEnabled: boolean
```

判断Ability是否提供卡片能力，取值为true表示Ability提供卡片能力，取值为false表示Ability不提供卡片能力。

**模型约束：** 此接口仅可在FA模型下使用。

**Type:** boolean

**Default:** Indicates whether the ability provides the embedded card capability

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Model restriction:** This API can be used only in the FA model.

<!--Device-AbilityInfo-readonly formEnabled: boolean--><!--Device-AbilityInfo-readonly formEnabled: boolean-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## icon

```TypeScript
readonly icon: string
```

Ability的图标资源文件索引。

**Type:** string

**Default:** Indicates the icon of the ability

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.AbilityInfo#icon

<!--Device-AbilityInfo-readonly icon: string--><!--Device-AbilityInfo-readonly icon: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## iconId

```TypeScript
readonly iconId: number
```

Ability的图标的资源id值。

**Type:** number

**Default:** Indicates the icon id of the ability

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.AbilityInfo#iconId

<!--Device-AbilityInfo-readonly iconId: number--><!--Device-AbilityInfo-readonly iconId: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## isVisible

```TypeScript
readonly isVisible: boolean
```

判断Ability是否可以被其他应用调用，取值为true表示Ability可以被其他应用调用，取值为false表示Ability不可以被其他应用调用。

**Type:** boolean

**Default:** Indicates whether an ability can be called by other abilities

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.AbilityInfo#exported

<!--Device-AbilityInfo-readonly isVisible: boolean--><!--Device-AbilityInfo-readonly isVisible: boolean-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## label

```TypeScript
readonly label: string
```

Ability对用户显示的名称。

**Type:** string

**Default:** Indicates the label of the ability

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.AbilityInfo#label

<!--Device-AbilityInfo-readonly label: string--><!--Device-AbilityInfo-readonly label: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## labelId

```TypeScript
readonly labelId: number
```

Ability的标签的资源id值。

**Type:** number

**Default:** Indicates the label id of the ability

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.AbilityInfo#labelId

<!--Device-AbilityInfo-readonly labelId: number--><!--Device-AbilityInfo-readonly labelId: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## launchMode

```TypeScript
readonly launchMode: bundle.LaunchMode
```

Ability的启动模式。

**Type:** bundle.LaunchMode

**Default:** Enumerates ability launch modes

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.AbilityInfo#launchType

<!--Device-AbilityInfo-readonly launchMode: bundle.LaunchMode--><!--Device-AbilityInfo-readonly launchMode: bundle.LaunchMode-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## metaData

```TypeScript
readonly metaData: Array<CustomizeData>
```

Ability的元信息。

通过调用[bundle.getAbilityInfo](arkts-ability-bundle-getabilityinfo-f.md#getabilityinfo)接口时，传入GET_ABILITY_INFO_WITH_METADATA获取。

**Type:** Array&lt;[CustomizeData](arkts-ability-customizedata-customizedata-depr-i.md)&gt;

**Default:** Indicates the metadata of ability

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.AbilityInfo#metadata

<!--Device-AbilityInfo-readonly metaData: Array<CustomizeData>--><!--Device-AbilityInfo-readonly metaData: Array<CustomizeData>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## moduleName

```TypeScript
readonly moduleName: string
```

Ability所属的HAP的名称。

**Type:** string

**Default:** Indicates the name of the .hap package to which the capability belongs

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.AbilityInfo#moduleName

<!--Device-AbilityInfo-readonly moduleName: string--><!--Device-AbilityInfo-readonly moduleName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## name

```TypeScript
readonly name: string
```

Ability名称。

**Type:** string

**Default:** Ability simplified class name

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.AbilityInfo#name

<!--Device-AbilityInfo-readonly name: string--><!--Device-AbilityInfo-readonly name: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## orientation

```TypeScript
readonly orientation: bundle.DisplayOrientation
```

Ability的显示模式。

**Type:** bundle.DisplayOrientation

**Default:** Enumerates ability display orientations

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.AbilityInfo#orientation

<!--Device-AbilityInfo-readonly orientation: bundle.DisplayOrientation--><!--Device-AbilityInfo-readonly orientation: bundle.DisplayOrientation-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## permissions

```TypeScript
readonly permissions: Array<string>
```

被其他应用Ability调用时需要申请的权限集合。

通过调用[bundle.getAbilityInfo](arkts-ability-bundle-getabilityinfo-f.md#getabilityinfo)接口时，传入GET_ABILITY_INFO_WITH_PERMISSION获取。

**Type:** Array&lt;string&gt;

**Default:** The permissions that others need to launch this ability

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.AbilityInfo#permissions

<!--Device-AbilityInfo-readonly permissions: Array<string>--><!--Device-AbilityInfo-readonly permissions: Array<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## process

```TypeScript
readonly process: string
```

Ability的进程名称。

**Type:** string

**Default:** Process of ability, if user do not set it ,the value equal application process

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.AbilityInfo#process

<!--Device-AbilityInfo-readonly process: string--><!--Device-AbilityInfo-readonly process: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## readPermission

```TypeScript
readonly readPermission: string
```

读取Ability数据所需的权限。

**模型约束：** 此接口仅可在FA模型下使用。

**Type:** string

**Default:** Indicates the permission required for reading ability data

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Model restriction:** This API can be used only in the FA model.

<!--Device-AbilityInfo-readonly readPermission: string--><!--Device-AbilityInfo-readonly readPermission: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## subType

```TypeScript
readonly subType: bundle.AbilitySubType
```

Ability中枚举使用的模板的子类型。

**模型约束：** 此接口仅可在FA模型下使用。

**Type:** bundle.AbilitySubType

**Default:** Enumerates the subType of templates used by an ability

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Model restriction:** This API can be used only in the FA model.

<!--Device-AbilityInfo-readonly subType: bundle.AbilitySubType--><!--Device-AbilityInfo-readonly subType: bundle.AbilitySubType-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## targetAbility

```TypeScript
readonly targetAbility: string
```

当前Ability重用的目标Ability。

**模型约束：** 此接口仅可在FA模型下使用。

**Type:** string

**Default:** Info about which ability is this nick point to

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Model restriction:** This API can be used only in the FA model.

<!--Device-AbilityInfo-readonly targetAbility: string--><!--Device-AbilityInfo-readonly targetAbility: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## type

```TypeScript
readonly type: bundle.AbilityType
```

Ability类型。

**模型约束：** 此接口仅可在FA模型下使用。

**Type:** bundle.AbilityType

**Default:** Enumerates types of templates that can be used by an ability

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Model restriction:** This API can be used only in the FA model.

<!--Device-AbilityInfo-readonly type: bundle.AbilityType--><!--Device-AbilityInfo-readonly type: bundle.AbilityType-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## uri

```TypeScript
readonly uri: string
```

获取Ability的统一资源标识符（URI）。

**模型约束：** 此接口仅可在FA模型下使用。

**Type:** string

**Default:** Uri of ability

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Model restriction:** This API can be used only in the FA model.

<!--Device-AbilityInfo-readonly uri: string--><!--Device-AbilityInfo-readonly uri: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## writePermission

```TypeScript
readonly writePermission: string
```

向Ability写数据所需的权限。

**模型约束：** 此接口仅可在FA模型下使用。

**Type:** string

**Default:** Indicates the permission required for writing data to the ability

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Model restriction:** This API can be used only in the FA model.

<!--Device-AbilityInfo-readonly writePermission: string--><!--Device-AbilityInfo-readonly writePermission: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

