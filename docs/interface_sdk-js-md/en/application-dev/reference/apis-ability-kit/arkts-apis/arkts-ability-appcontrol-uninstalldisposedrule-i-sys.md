# UninstallDisposedRule (System API)

标识卸载处置规则。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-appControl-export interface UninstallDisposedRule--><!--Device-appControl-export interface UninstallDisposedRule-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { appControl } from 'kits/@kit.AbilityKit';
```

## priority

```TypeScript
priority: int
```

拦截规则的优先级，用于规则列表查询结果排序。取值为整数，数值越小，优先级越高，排序越靠前。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-UninstallDisposedRule-priority: int--><!--Device-UninstallDisposedRule-priority: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

## uninstallComponentType

```TypeScript
uninstallComponentType: UninstallComponentType
```

拦截时将拉起能力的类型。

**Type:** [UninstallComponentType](arkts-ability-appcontrol-uninstallcomponenttype-e-sys.md)

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-UninstallDisposedRule-uninstallComponentType: UninstallComponentType--><!--Device-UninstallDisposedRule-uninstallComponentType: UninstallComponentType-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

## want

```TypeScript
want: Want
```

指定应用被拦截时，跳转到的组件。

**Type:** [Want](arkts-ability-app-ability-want-want-c.md)

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-UninstallDisposedRule-want: Want--><!--Device-UninstallDisposedRule-want: Want-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

