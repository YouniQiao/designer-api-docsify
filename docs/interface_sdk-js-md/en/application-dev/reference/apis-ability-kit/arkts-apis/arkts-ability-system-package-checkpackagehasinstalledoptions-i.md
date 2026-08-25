# CheckPackageHasInstalledOptions


> **NOTE：**&gt;
> This API has been supported since API version 3 and deprecated since API version 9.
Checks whether a bundle has been installed.

**Since:** 3

**Deprecated since:** 9

**System capability:** SystemCapability.BundleManager.BundleFramework

## Modules to Import

```TypeScript
import { Package, CheckPackageHasInstalledOptions, CheckPackageHasInstalledResponse } from 'kits/@kit.AbilityKit';
```

## complete

```TypeScript
complete?: () => void
```

Called when API call is complete.

**Since:** 3

**Deprecated since:** 9

**System capability:** SystemCapability.BundleManager.BundleFramework

## fail

```TypeScript
fail?: (data: any, code: number) => void
```

Called when API call has failed.

**Since:** 3

**Deprecated since:** 9

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | any | Yes |
| code | number | Yes |

## success

```TypeScript
success?: (data: CheckPackageHasInstalledResponse) => void
```

Called when API call is successful.

**Since:** 3

**Deprecated since:** 9

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [CheckPackageHasInstalledResponse](arkts-ability-system-package-checkpackagehasinstalledresponse-i.md) | Yes |

## bundleName

```TypeScript
bundleName: string
```

Bundle name.

**Type:** string

**Since:** 3

**Deprecated since:** 9

**System capability:** SystemCapability.BundleManager.BundleFramework
