# ApplicationInfo

The module provides application information. Unless otherwise specified, the information is obtained through [bundle.getApplicationInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ . > **NOTE** > > The APIs of this module have been deprecated since API version 9. You are advised to use > [bundleManager-ApplicationInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ instead.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [applicationInfo:ApplicationInfo](../arkts-ability-bundlemanager/applicationinfo-applicationinfo-i.md)

<!--Device-unnamed-export interface ApplicationInfo--><!--Device-unnamed-export interface ApplicationInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## accessTokenId

```TypeScript
readonly accessTokenId: number
```

Access token ID of the application.

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

Installation directory of the application. Do not access resource files using concatenated paths. Use [@ohos.resourceManager]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ instead.

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

Application description.

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

ID of the application description.

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

Whether the application is enabled. **true** if enabled, **false** otherwise.

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

Type of the application, for example, gaming, social networking, movies, and news.

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

Path for storing application files. Do not access resource files using concatenated paths. Use [@ohos.resourceManager]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ instead.

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

Application icon.

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

ID of the application icon.

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

Application label.

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

ID of the application label.

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

Custom metadata of the application. The value is obtained by passing in GET\_APPLICATION\_INFO\_WITH\_METADATA to [bundle.getApplicationInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ .

**Type:** Map&lt;string, Array&lt;CustomizeData&gt;&gt;

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

Application module information.

**Type:** Array&lt;ModuleInfo&gt;

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

Relative paths for storing application resources. Do not access resource files using concatenated paths. Use [@ohos.resourceManager]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ instead.

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

Application name.

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

Permissions required for accessing the application. The value is obtained by passing in GET\_APPLICATION\_INFO\_WITH\_PERMISSION to [bundle.getApplicationInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ .

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

Process name.

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

Whether the application is removable. **true** if removable, **false** otherwise.

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

Modes supported by the application. Currently, only the **drive** mode is defined. This attribute applies only to telematics devices.

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

Whether the application is a system application. **true** if yes, **false** otherwise.

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

UID of the application.

**Type:** number

**Default:** Indicates the uid of the application

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ApplicationInfo#uid

<!--Device-ApplicationInfo-readonly uid: number--><!--Device-ApplicationInfo-readonly uid: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

