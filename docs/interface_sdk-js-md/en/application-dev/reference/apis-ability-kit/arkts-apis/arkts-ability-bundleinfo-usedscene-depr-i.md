# UsedScene

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃，建议使用[UsedScene](arkts-ability-bundleinfo-usedscene-depr-i.md)替代。

描述权限使用的场景和时机。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [bundleInfo:UsedScene](arkts-ability-bundleinfo-usedscene-depr-i.md)

<!--Device-unnamed-export interface UsedScene--><!--Device-unnamed-export interface UsedScene-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## abilities

```TypeScript
abilities: Array<string>
```

使用到该权限的Ability集合。

**Type:** Array&lt;string&gt;

**Default:** Indicates the abilities that need the permission

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.UsedScene#abilities

<!--Device-UsedScene-abilities: Array<string>--><!--Device-UsedScene-abilities: Array<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## when

```TypeScript
when: string
```

使用该权限的时机。

**Type:** string

**Default:** Indicates the time when the permission is used

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.UsedScene#when

<!--Device-UsedScene-when: string--><!--Device-UsedScene-when: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

