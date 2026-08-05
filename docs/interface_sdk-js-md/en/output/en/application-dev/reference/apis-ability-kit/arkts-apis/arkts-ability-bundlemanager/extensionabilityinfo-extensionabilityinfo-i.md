# ExtensionAbilityInfo

The module defines the ExtensionAbility information. An application can obtain its own ExtensionAbility information through [bundleManager.getBundleInfoForSelf]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ , with **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE** and **GET\_BUNDLE\_INFO\_WITH\_EXTENSION\_ABILITY** passed in to [bundleFlags]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface ExtensionAbilityInfo--><!--Device-unnamed-export interface ExtensionAbilityInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## appIndex

```TypeScript
readonly appIndex: int
```

Index of an application clone. It takes effect only for cloned applications.

**Type:** int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ExtensionAbilityInfo-readonly appIndex: int--><!--Device-ExtensionAbilityInfo-readonly appIndex: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## applicationInfo

```TypeScript
readonly applicationInfo: ApplicationInfo
```

Application configuration information \_\_\_MD\_COMMENT\_DESC\_USD\_4\_\_\_. The information can be obtained by passing in **GET\_EXTENSION\_ABILITY\_INFO\_WITH\_APPLICATION** to the **extensionAbilityFlags** parameter of [queryExtensionAbilityInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ \_\_\_MD\_COMMENT\_DESC\_USD\_5\_\_\_. This field is not returned when the [getBundleInfoForSelf]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ or [getBundleInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ is used to obtain ExtensionAbilityInfo information. You can obtain the related information by obtaining the [bundleInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_.appInfo object.

**Type:** ApplicationInfo

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ExtensionAbilityInfo-readonly applicationInfo: ApplicationInfo--><!--Device-ExtensionAbilityInfo-readonly applicationInfo: ApplicationInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## bundleName

```TypeScript
readonly bundleName: string
```

Bundle name.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ExtensionAbilityInfo-readonly bundleName: string--><!--Device-ExtensionAbilityInfo-readonly bundleName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## descriptionId

```TypeScript
readonly descriptionId: long
```

ID of the ExtensionAbility description.

**Type:** long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ExtensionAbilityInfo-readonly descriptionId: long--><!--Device-ExtensionAbilityInfo-readonly descriptionId: long-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## enabled

```TypeScript
readonly enabled: boolean
```

Whether the ExtensionAbility is enabled. **true** if enabled, **false** otherwise.

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ExtensionAbilityInfo-readonly enabled: boolean--><!--Device-ExtensionAbilityInfo-readonly enabled: boolean-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## exported

```TypeScript
readonly exported: boolean
```

Whether the ExtensionAbility can be called by other applications. **true** if the ExtensionAbility can be called by other applications, **false** otherwise.

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ExtensionAbilityInfo-readonly exported: boolean--><!--Device-ExtensionAbilityInfo-readonly exported: boolean-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## extensionAbilityType

```TypeScript
readonly extensionAbilityType: bundleManager.ExtensionAbilityType
```

Type of the ExtensionAbility.

**Type:** bundleManager.ExtensionAbilityType

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ExtensionAbilityInfo-readonly extensionAbilityType: bundleManager.ExtensionAbilityType--><!--Device-ExtensionAbilityInfo-readonly extensionAbilityType: bundleManager.ExtensionAbilityType-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## extensionAbilityTypeName

```TypeScript
readonly extensionAbilityTypeName: string
```

Type of the ExtensionAbility. For details about available values, see \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ .

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ExtensionAbilityInfo-readonly extensionAbilityTypeName: string--><!--Device-ExtensionAbilityInfo-readonly extensionAbilityTypeName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## iconId

```TypeScript
readonly iconId: long
```

ID of the ExtensionAbility icon.

**Type:** long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ExtensionAbilityInfo-readonly iconId: long--><!--Device-ExtensionAbilityInfo-readonly iconId: long-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## labelId

```TypeScript
readonly labelId: long
```

ID of the ExtensionAbility label.

**Type:** long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ExtensionAbilityInfo-readonly labelId: long--><!--Device-ExtensionAbilityInfo-readonly labelId: long-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## metadata

```TypeScript
readonly metadata: Array<Metadata>
```

Metadata of the ExtensionAbility. The information can be obtained by passing in **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE** , **GET\_BUNDLE\_INFO\_WITH\_EXTENSION\_ABILITY**, and **GET\_BUNDLE\_INFO\_WITH\_METADATA** to the **bundleFlags** parameter of [getBundleInfoForSelf]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Type:** Array&lt;Metadata&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ExtensionAbilityInfo-readonly metadata: Array<Metadata>--><!--Device-ExtensionAbilityInfo-readonly metadata: Array<Metadata>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## moduleName

```TypeScript
readonly moduleName: string
```

Name of the HAP file to which the ExtensionAbility belongs.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ExtensionAbilityInfo-readonly moduleName: string--><!--Device-ExtensionAbilityInfo-readonly moduleName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## name

```TypeScript
readonly name: string
```

Name of the ExtensionAbility.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ExtensionAbilityInfo-readonly name: string--><!--Device-ExtensionAbilityInfo-readonly name: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## permissions

```TypeScript
readonly permissions: Array<string>
```

Permissions required for other bundles to call the ExtensionAbility.

**Type:** Array&lt;string&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ExtensionAbilityInfo-readonly permissions: Array<string>--><!--Device-ExtensionAbilityInfo-readonly permissions: Array<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## readPermission

```TypeScript
readonly readPermission: string
```

Permission required for reading data from the ExtensionAbility.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ExtensionAbilityInfo-readonly readPermission: string--><!--Device-ExtensionAbilityInfo-readonly readPermission: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## skills

```TypeScript
readonly skills: Array<Skill>
```

Skills of the ExtensionAbility.

**Type:** Array&lt;Skill&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ExtensionAbilityInfo-readonly skills: Array<Skill>--><!--Device-ExtensionAbilityInfo-readonly skills: Array<Skill>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## writePermission

```TypeScript
readonly writePermission: string
```

Permission required for writing data to the ExtensionAbility.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ExtensionAbilityInfo-readonly writePermission: string--><!--Device-ExtensionAbilityInfo-readonly writePermission: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

