# Package

> **NOTE：**
> 
> This API has been supported since API version 3 and deprecated since API version 9.

Checks whether a bundle has been installed.

**Since:** 3

**Deprecated since:** 9

<!--Device-unnamed-export default class Package--><!--Device-unnamed-export default class Package-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## Modules to Import

```TypeScript
import { CheckPackageHasInstalledResponse, CheckPackageHasInstalledOptions } from 'kits/@kit.AbilityKit';
```

## hasInstalled

```TypeScript
static hasInstalled(options: CheckPackageHasInstalledOptions): void
```

Checks whether an application exists, or whether a native application has been installed.

**Since:** 3

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager#canOpenLink

<!--Device-Package-static hasInstalled(options: CheckPackageHasInstalledOptions): void--><!--Device-Package-static hasInstalled(options: CheckPackageHasInstalledOptions): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [CheckPackageHasInstalledOptions](arkts-ability-system-package-checkpackagehasinstalledoptions-i.md) | Yes |
