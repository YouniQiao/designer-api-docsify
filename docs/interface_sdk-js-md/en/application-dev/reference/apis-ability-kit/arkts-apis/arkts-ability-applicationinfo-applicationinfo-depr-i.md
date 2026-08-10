# ApplicationInfo

应用程序信息，未做特殊说明的属性，均通过  
[bundle.getApplicationInfo](arkts-ability-bundle-getapplicationinfo-f.md#getapplicationinfo)获取。

> **说明：**
> 
> 从API version 9开始，该模块不再维护，建议使用[bundleManager-ApplicationInfo](arkts-ability-applicationinfo-applicationinfo-depr-i.md)替代。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [applicationInfo:ApplicationInfo](arkts-ability-applicationinfo-applicationinfo-depr-i.md)

<!--Device-unnamed-export interface ApplicationInfo--><!--Device-unnamed-export interface ApplicationInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## accessTokenId

```TypeScript
readonly accessTokenId: number
```

应用程序的accessTokenId。

**Type:** number

**Default:** Indicates the access token of the application

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ApplicationInfo#accessTokenId

<!--Device-ApplicationInfo-readonly accessTokenId: number--><!--Device-ApplicationInfo-readonly accessTokenId: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## codePath

```TypeScript
readonly codePath: string
```

应用程序的安装目录。不能拼接路径访问资源文件，请使用[资源管理接口](../../apis-localization-kit/arkts-apis/arkts-resourcemanager.md/arkts-resourcemanager.md)访问资源。

**Type:** string

**Default:** Indicates the application source code path

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ApplicationInfo#codePath

<!--Device-ApplicationInfo-readonly codePath: string--><!--Device-ApplicationInfo-readonly codePath: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## description

```TypeScript
readonly description: string
```

应用程序的描述信息。

**Type:** string

**Default:** Description of application

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ApplicationInfo#description

<!--Device-ApplicationInfo-readonly description: string--><!--Device-ApplicationInfo-readonly description: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## descriptionId

```TypeScript
readonly descriptionId: number
```

应用程序的描述信息的资源ID。

**Type:** number

**Default:** Indicates the description id of the application

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ApplicationInfo#descriptionId

<!--Device-ApplicationInfo-readonly descriptionId: number--><!--Device-ApplicationInfo-readonly descriptionId: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## enabled

```TypeScript
readonly enabled: boolean
```

判断应用程序是否可以使用，取值为true表示可以使用，取值为false表示不可使用。

**Type:** boolean

**Default:** Indicates whether or not this application may be instantiated

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ApplicationInfo#enabled

<!--Device-ApplicationInfo-readonly enabled: boolean--><!--Device-ApplicationInfo-readonly enabled: boolean-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## entityType

```TypeScript
readonly entityType: string
```

应用程序的类别，例如游戏、社交、影视、新闻。

**Type:** string

**Default:** Indicates entity type of the application

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

<!--Device-ApplicationInfo-readonly entityType: string--><!--Device-ApplicationInfo-readonly entityType: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## entryDir

```TypeScript
readonly entryDir: string
```

应用程序的文件保存路径。不能拼接路径访问资源文件，请使用[资源管理接口](../../apis-localization-kit/arkts-apis/arkts-resourcemanager.md/arkts-resourcemanager.md)访问资源。

**Type:** string

**Default:** Indicates the path where the {@code Entry.hap} file of the application is saved

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-ApplicationInfo-readonly entryDir: string--><!--Device-ApplicationInfo-readonly entryDir: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## icon

```TypeScript
readonly icon: string
```

应用程序的图标。

**Type:** string

**Default:** Indicates the icon of the application

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ApplicationInfo#icon

<!--Device-ApplicationInfo-readonly icon: string--><!--Device-ApplicationInfo-readonly icon: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## iconId

```TypeScript
readonly iconId: string
```

应用程序图标的资源ID值。

**Type:** string

**Default:** Indicates the icon id of the application

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ApplicationInfo#iconId

<!--Device-ApplicationInfo-readonly iconId: string--><!--Device-ApplicationInfo-readonly iconId: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## label

```TypeScript
readonly label: string
```

应用程序显示的标签。

**Type:** string

**Default:** Indicates the label of the application

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ApplicationInfo#label

<!--Device-ApplicationInfo-readonly label: string--><!--Device-ApplicationInfo-readonly label: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## labelId

```TypeScript
readonly labelId: string
```

应用程序的标签的资源ID值。

**Type:** string

**Default:** Indicates the label id of the application

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ApplicationInfo#labelId

<!--Device-ApplicationInfo-readonly labelId: string--><!--Device-ApplicationInfo-readonly labelId: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## metaData

```TypeScript
readonly metaData: Map<string, Array<CustomizeData>>
```

应用程序的自定义元信息。

通过调用  
[bundle.getApplicationInfo](arkts-ability-bundle-getapplicationinfo-f.md#getapplicationinfo)接口时，传入GET_APPLICATION_INFO_WITH_METADATA获取。

**Type:** Map&lt;string, Array&lt;[CustomizeData](arkts-ability-customizedata-customizedata-depr-i.md)&gt;&gt;

**Default:** Indicates the metadata of module

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ApplicationInfo#metadataArray

<!--Device-ApplicationInfo-readonly metaData: Map<string, Array<CustomizeData>>--><!--Device-ApplicationInfo-readonly metaData: Map<string, Array<CustomizeData>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## moduleInfos

```TypeScript
readonly moduleInfos: Array<ModuleInfo>
```

应用程序的模块信息。

**Type:** Array&lt;[ModuleInfo](arkts-ability-moduleinfo-moduleinfo-depr-i.md)&gt;

**Default:** Indicates module information about an application

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.BundleInfo#hapModulesInfo

<!--Device-ApplicationInfo-readonly moduleInfos: Array<ModuleInfo>--><!--Device-ApplicationInfo-readonly moduleInfos: Array<ModuleInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## moduleSourceDirs

```TypeScript
readonly moduleSourceDirs: Array<string>
```

应用程序的资源存放的相对路径。不能拼接路径访问资源文件，请使用[资源管理接口](../../apis-localization-kit/arkts-apis/arkts-resourcemanager.md/arkts-resourcemanager.md)访问资源。

**Type:** Array&lt;string&gt;

**Default:** Indicates the path storing the module resources of the application

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-ApplicationInfo-readonly moduleSourceDirs: Array<string>--><!--Device-ApplicationInfo-readonly moduleSourceDirs: Array<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## name

```TypeScript
readonly name: string
```

应用程序的名称。

**Type:** string

**Default:** Indicates the application name, which is the same as {@code bundleName}

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ApplicationInfo#name

<!--Device-ApplicationInfo-readonly name: string--><!--Device-ApplicationInfo-readonly name: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## permissions

```TypeScript
readonly permissions: Array<string>
```

访问应用程序所需的权限。

通过调用  
[bundle.getApplicationInfo](arkts-ability-bundle-getapplicationinfo-f.md#getapplicationinfo)接口时，传入GET_APPLICATION_INFO_WITH_PERMISSION获取。

**Type:** Array&lt;string&gt;

**Default:** Indicates the permissions required for accessing the application.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ApplicationInfo#permissions

<!--Device-ApplicationInfo-readonly permissions: Array<string>--><!--Device-ApplicationInfo-readonly permissions: Array<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## process

```TypeScript
readonly process: string
```

应用程序的进程名称。

**Type:** string

**Default:** Process of application, if user do not set it ,the value equal bundleName

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ApplicationInfo#process

<!--Device-ApplicationInfo-readonly process: string--><!--Device-ApplicationInfo-readonly process: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## removable

```TypeScript
readonly removable: boolean
```

应用程序是否可以被移除，取值为true表示可以被移除，取值为false表示不可以被移除。

**Type:** boolean

**Default:** Indicates whether or not this application may be removable

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ApplicationInfo#removable

<!--Device-ApplicationInfo-readonly removable: boolean--><!--Device-ApplicationInfo-readonly removable: boolean-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## supportedModes

```TypeScript
readonly supportedModes: number
```

标识应用支持的运行模式，当前只定义了驾驶模式（drive）。该标签只适用于车机。

**Type:** number

**Default:** Indicates the running mode supported by the application

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-ApplicationInfo-readonly supportedModes: number--><!--Device-ApplicationInfo-readonly supportedModes: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## systemApp

```TypeScript
readonly systemApp: boolean
```

判断是否为系统应用程序，取值为true表示系统应用，取值为false表示非系统应用。

**Type:** boolean

**Default:** Indicates whether the application is a system application

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ApplicationInfo#systemApp

<!--Device-ApplicationInfo-readonly systemApp: boolean--><!--Device-ApplicationInfo-readonly systemApp: boolean-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## uid

```TypeScript
readonly uid: number
```

应用程序的uid。

**Type:** number

**Default:** Indicates the uid of the application

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ApplicationInfo#uid

<!--Device-ApplicationInfo-readonly uid: number--><!--Device-ApplicationInfo-readonly uid: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

