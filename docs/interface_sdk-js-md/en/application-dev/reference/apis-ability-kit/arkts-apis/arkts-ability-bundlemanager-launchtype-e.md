# LaunchType

标识组件的[启动模式](../../../application-models/uiability-launch-type.md)。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-bundleManager-export enum LaunchType--><!--Device-bundleManager-export enum LaunchType-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## SINGLETON

```TypeScript
SINGLETON = 0
```

UIAbility的启动模式，表示单实例。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LaunchType-SINGLETON = 0--><!--Device-LaunchType-SINGLETON = 0-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## MULTITON

```TypeScript
MULTITON = 1
```

UIAbility的启动模式，表示普通多实例。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LaunchType-MULTITON = 1--><!--Device-LaunchType-MULTITON = 1-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## SPECIFIED

```TypeScript
SPECIFIED = 2
```

UIAbility的启动模式，表示该UIAbility内部根据业务自己指定多实例。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LaunchType-SPECIFIED = 2--><!--Device-LaunchType-SPECIFIED = 2-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

