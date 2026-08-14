# Package

Represents the details about a system update package.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-systemManager-interface Package--><!--Device-systemManager-interface Package-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { systemManager } from 'systemManager';
```

## fd

```TypeScript
fd?: number
```

File descriptor (FD) of the system update package. Currently, you cannot pass in **path** only. The **fd** parameter must also be passed in.

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Package-fd?: number--><!--Device-Package-fd?: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## path

```TypeScript
path: string
```

Path of the system update package. If **fd** is specified, pass in the update package name here.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Package-path: string--><!--Device-Package-path: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## type

```TypeScript
type: PackageType
```

Type of the system update package.

**Type:** [PackageType](arkts-mdm-systemmanager-packagetype-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Package-type: PackageType--><!--Device-Package-type: PackageType-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

