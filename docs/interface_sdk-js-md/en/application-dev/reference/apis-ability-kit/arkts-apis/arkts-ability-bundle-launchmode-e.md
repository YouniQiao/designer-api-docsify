# LaunchMode

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃，建议使用
> [bundleManager.LaunchType](arkts-ability-bundlemanager-launchtype-e.md)替代。

Ability组件的启动模式。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.bundle.bundleManager:bundleManager.LaunchType](arkts-ability-bundlemanager-launchtype-e.md)

<!--Device-bundle-export enum LaunchMode--><!--Device-bundle-export enum LaunchMode-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## SINGLETON

```TypeScript
SINGLETON = 0
```

Ability只有一个实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.LaunchType#SINGLETON

<!--Device-LaunchMode-SINGLETON = 0--><!--Device-LaunchMode-SINGLETON = 0-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## STANDARD

```TypeScript
STANDARD = 1
```

Ability有多个实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.LaunchType#MULTITON

<!--Device-LaunchMode-STANDARD = 1--><!--Device-LaunchMode-STANDARD = 1-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

