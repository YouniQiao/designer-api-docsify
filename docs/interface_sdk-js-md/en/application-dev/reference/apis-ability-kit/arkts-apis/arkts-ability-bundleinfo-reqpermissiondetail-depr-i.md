# ReqPermissionDetail

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃，建议使用[ReqPermissionDetail](arkts-ability-bundleinfo-reqpermissiondetail-depr-i.md)替代。

应用运行时需向系统申请的权限集合的详细信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [bundleInfo](arkts-ability-bundleinfo-i.md)

<!--Device-unnamed-export interface ReqPermissionDetail--><!--Device-unnamed-export interface ReqPermissionDetail-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## name

```TypeScript
name: string
```

需要使用的权限名称。

**Type:** string

**Default:** Indicates the name of this required permissions

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ReqPermissionDetail#name

<!--Device-ReqPermissionDetail-name: string--><!--Device-ReqPermissionDetail-name: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## reason

```TypeScript
reason: string
```

描述申请权限的原因。

**Type:** string

**Default:** Indicates the reason of this required permissions

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ReqPermissionDetail#reason

<!--Device-ReqPermissionDetail-reason: string--><!--Device-ReqPermissionDetail-reason: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## usedScene

```TypeScript
usedScene: UsedScene
```

权限使用的场景和时机。

**Type:** [UsedScene](arkts-ability-bundlemanager-usedscene-t.md)

**Default:** Indicates the used scene of this required permissions

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ReqPermissionDetail#usedScene

<!--Device-ReqPermissionDetail-usedScene: UsedScene--><!--Device-ReqPermissionDetail-usedScene: UsedScene-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

