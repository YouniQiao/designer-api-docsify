# Package

系统更新包详情。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-systemManager-interface Package--><!--Device-systemManager-interface Package-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## fd

```TypeScript
fd?: number
```

系统更新包文件句柄。当前不支持只传入path参数，需要传入fd。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Package-fd?: number--><!--Device-Package-fd?: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## path

```TypeScript
path: string
```

系统更新包文件路径。若传入fd参数，该参数传入更新包文件名。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Package-path: string--><!--Device-Package-path: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## type

```TypeScript
type: PackageType
```

系统更新包类型。

**Type:** [PackageType](arkts-mdm-systemmanager-packagetype-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Package-type: PackageType--><!--Device-Package-type: PackageType-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

