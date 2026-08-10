# AbilityFlag

Ability组件信息标志，指示需要获取的Ability组件信息的内容。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-bundleManager-enum AbilityFlag--><!--Device-bundleManager-enum AbilityFlag-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## GET_ABILITY_INFO_DEFAULT

```TypeScript
GET_ABILITY_INFO_DEFAULT = 0x00000000
```

获取默认[AbilityInfo](arkts-abilityinfo.md)，获取的AbilityInfo不包含permissions、metadata、被禁用Ability对应的AbilityInfo。&lt;!--Del--&gt;通过  
[setAbilityEnabled接口](arkts-ability-bundlemanager-setabilityenabled-f-sys.md#setabilityenabled)可设置Ability禁用状态、通过  
[isAbilityEnabled接口](arkts-ability-bundlemanager-isabilityenabled-f-sys.md#isabilityenabled)可获取Ability禁用状态。&lt;!--DelEnd--&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AbilityFlag-GET_ABILITY_INFO_DEFAULT = 0x00000000--><!--Device-AbilityFlag-GET_ABILITY_INFO_DEFAULT = 0x00000000-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## GET_ABILITY_INFO_WITH_PERMISSION

```TypeScript
GET_ABILITY_INFO_WITH_PERMISSION = 0x00000001
```

获取包含permissions的AbilityInfo。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AbilityFlag-GET_ABILITY_INFO_WITH_PERMISSION = 0x00000001--><!--Device-AbilityFlag-GET_ABILITY_INFO_WITH_PERMISSION = 0x00000001-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## GET_ABILITY_INFO_WITH_APPLICATION

```TypeScript
GET_ABILITY_INFO_WITH_APPLICATION = 0x00000002
```

获取包含applicationInfo的AbilityInfo。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AbilityFlag-GET_ABILITY_INFO_WITH_APPLICATION = 0x00000002--><!--Device-AbilityFlag-GET_ABILITY_INFO_WITH_APPLICATION = 0x00000002-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## GET_ABILITY_INFO_WITH_METADATA

```TypeScript
GET_ABILITY_INFO_WITH_METADATA = 0x00000004
```

获取包含metadata的AbilityInfo。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AbilityFlag-GET_ABILITY_INFO_WITH_METADATA = 0x00000004--><!--Device-AbilityFlag-GET_ABILITY_INFO_WITH_METADATA = 0x00000004-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## GET_ABILITY_INFO_WITH_DISABLE

```TypeScript
GET_ABILITY_INFO_WITH_DISABLE = 0x00000008
```

获取被禁用Ability对应的AbilityInfo。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AbilityFlag-GET_ABILITY_INFO_WITH_DISABLE = 0x00000008--><!--Device-AbilityFlag-GET_ABILITY_INFO_WITH_DISABLE = 0x00000008-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## GET_ABILITY_INFO_ONLY_SYSTEM_APP

```TypeScript
GET_ABILITY_INFO_ONLY_SYSTEM_APP = 0x00000010
```

获取系统应用对应的AbilityInfo。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AbilityFlag-GET_ABILITY_INFO_ONLY_SYSTEM_APP = 0x00000010--><!--Device-AbilityFlag-GET_ABILITY_INFO_ONLY_SYSTEM_APP = 0x00000010-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## GET_ABILITY_INFO_WITH_APP_LINKING

```TypeScript
GET_ABILITY_INFO_WITH_APP_LINKING = 0x00000040
```

获取通过&lt;!--RP3--&gt;[域名校验](../../../application-models/app-linking-startup.md#实现原理)&lt;!--RP3End--&gt;筛选的AbilityInfo。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AbilityFlag-GET_ABILITY_INFO_WITH_APP_LINKING = 0x00000040--><!--Device-AbilityFlag-GET_ABILITY_INFO_WITH_APP_LINKING = 0x00000040-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## GET_ABILITY_INFO_WITH_SKILL

```TypeScript
GET_ABILITY_INFO_WITH_SKILL = 0x00000080
```

获取包含skills的AbilityInfo。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AbilityFlag-GET_ABILITY_INFO_WITH_SKILL = 0x00000080--><!--Device-AbilityFlag-GET_ABILITY_INFO_WITH_SKILL = 0x00000080-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

