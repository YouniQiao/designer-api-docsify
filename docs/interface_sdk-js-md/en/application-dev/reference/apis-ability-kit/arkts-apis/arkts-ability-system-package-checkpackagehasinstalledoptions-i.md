# CheckPackageHasInstalledOptions

> **说明：**
> 
> 从API version 3开始支持，从API version 9开始废弃。

指示应用包是否已安装。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

<!--Device-unnamed-export interface CheckPackageHasInstalledOptions--><!--Device-unnamed-export interface CheckPackageHasInstalledOptions-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## Modules to Import

```TypeScript
import { CheckPackageHasInstalledResponse, CheckPackageHasInstalledOptions } from 'kits/@kit.AbilityKit';
```

## complete

```TypeScript
complete?: () => void
```

接口调用结束的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

<!--Device-CheckPackageHasInstalledOptions-complete?: () => void--><!--Device-CheckPackageHasInstalledOptions-complete?: () => void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## fail

```TypeScript
fail?: (data: any, code: number) => void
```

接口调用失败的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

<!--Device-CheckPackageHasInstalledOptions-fail?: (data: any, code: number) => void--><!--Device-CheckPackageHasInstalledOptions-fail?: (data: any, code: number) => void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | any | Yes |  |
| code | number | Yes |  |

## success

```TypeScript
success?: (data: CheckPackageHasInstalledResponse) => void
```

接口调用成功的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

<!--Device-CheckPackageHasInstalledOptions-success?: (data: CheckPackageHasInstalledResponse) => void--><!--Device-CheckPackageHasInstalledOptions-success?: (data: CheckPackageHasInstalledResponse) => void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [CheckPackageHasInstalledResponse](arkts-ability-system-package-checkpackagehasinstalledresponse-i.md) | Yes |  |

## bundleName

```TypeScript
bundleName: string
```

应用Bundle名称。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 9

<!--Device-CheckPackageHasInstalledOptions-bundleName: string--><!--Device-CheckPackageHasInstalledOptions-bundleName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

