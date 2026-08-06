# Metadata

The module defines a metadata object. An application can obtain the metadata through  
[bundleManager.getBundleInfoForSelf]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_, with **GET\_BUNDLE\_INFO\_WITH\_METADATA** passed in for  
[bundleFlags]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_. This object is contained in  
[ApplicationInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, [HapModuleInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_, [AbilityInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_, and  
[ExtensionAbilityInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_.

The module provides the configuration about the module, UIAbility, and ExtensionAbility. The value is of the array type. The configuration is valid only for the current module, UIAbility, or ExtensionAbility.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface Metadata--><!--Device-unnamed-export interface Metadata-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## name

```TypeScript
name: string
```

Indicates the metadata name

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Metadata-name: string--><!--Device-Metadata-name: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## resource

```TypeScript
resource: string
```

Indicates the metadata resource

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Metadata-resource: string--><!--Device-Metadata-resource: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## value

```TypeScript
value: string
```

Indicates the metadata value

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Metadata-value: string--><!--Device-Metadata-value: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## valueId

```TypeScript
readonly valueId?: long
```

Indicates the value id of the metadata

**Type:** long

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Metadata-readonly valueId?: long--><!--Device-Metadata-readonly valueId?: long-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

