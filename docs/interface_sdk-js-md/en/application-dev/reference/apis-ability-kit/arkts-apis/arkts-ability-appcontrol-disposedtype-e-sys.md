# DisposedType (System API)

标识拦截应用程序的方式，例如禁用应用的全部能力、禁用应用的指定能力、或者不禁用。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-appControl-export enum DisposedType--><!--Device-appControl-export enum DisposedType-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

## BLOCK_APPLICATION

```TypeScript
BLOCK_APPLICATION = 1
```

应用所有能力都将被禁用。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DisposedType-BLOCK_APPLICATION = 1--><!--Device-DisposedType-BLOCK_APPLICATION = 1-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

## BLOCK_ABILITY

```TypeScript
BLOCK_ABILITY = 2
```

应用指定的能力才会被禁用。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DisposedType-BLOCK_ABILITY = 2--><!--Device-DisposedType-BLOCK_ABILITY = 2-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

## NON_BLOCK

```TypeScript
NON_BLOCK = 3
```

应用所有能力不会被禁用。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DisposedType-NON_BLOCK = 3--><!--Device-DisposedType-NON_BLOCK = 3-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

