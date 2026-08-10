# ReqPermissionDetail

应用运行时需向系统申请的权限集合的详细信息。

> **说明：**
> 
> - 如果应用内多包申请的权限名称一样，但是权限申请理由不一致，系统只会返回一个权限申请理由，优先级从高到低顺序为entry类型HAP、feature类型HAP、应用内HSP。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface ReqPermissionDetail--><!--Device-unnamed-export interface ReqPermissionDetail-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## moduleName

```TypeScript
moduleName: string
```

申请该权限的module名称。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ReqPermissionDetail-moduleName: string--><!--Device-ReqPermissionDetail-moduleName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## name

```TypeScript
name: string
```

需要使用的[权限名称](../../../security/AccessToken/app-permissions.md)。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ReqPermissionDetail-name: string--><!--Device-ReqPermissionDetail-name: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## reason

```TypeScript
reason: string
```

描述申请权限的原因。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ReqPermissionDetail-reason: string--><!--Device-ReqPermissionDetail-reason: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## reasonId

```TypeScript
reasonId: long
```

描述申请权限的原因ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ReqPermissionDetail-reasonId: long--><!--Device-ReqPermissionDetail-reasonId: long-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## usedScene

```TypeScript
usedScene: UsedScene
```

权限使用的场景和时机。

**Type:** [UsedScene](arkts-ability-bundlemanager-usedscene-t.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ReqPermissionDetail-usedScene: UsedScene--><!--Device-ReqPermissionDetail-usedScene: UsedScene-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

