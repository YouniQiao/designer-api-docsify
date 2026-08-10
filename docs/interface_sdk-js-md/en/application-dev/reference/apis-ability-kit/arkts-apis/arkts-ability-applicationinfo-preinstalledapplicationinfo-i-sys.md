# PreinstalledApplicationInfo (System API)

预装应用的信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface PreinstalledApplicationInfo--><!--Device-unnamed-export interface PreinstalledApplicationInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## bundleName

```TypeScript
readonly bundleName: string
```

应用包的名称。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-PreinstalledApplicationInfo-readonly bundleName: string--><!--Device-PreinstalledApplicationInfo-readonly bundleName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## descriptionId

```TypeScript
readonly descriptionId?: long
```

应用描述Id。

**模型约束：** 此接口仅可在Stage模型下使用。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PreinstalledApplicationInfo-readonly descriptionId?: long--><!--Device-PreinstalledApplicationInfo-readonly descriptionId?: long-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## iconId

```TypeScript
readonly iconId: long
```

应用图标Id。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-PreinstalledApplicationInfo-readonly iconId: long--><!--Device-PreinstalledApplicationInfo-readonly iconId: long-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## labelId

```TypeScript
readonly labelId: long
```

应用标签Id。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-PreinstalledApplicationInfo-readonly labelId: long--><!--Device-PreinstalledApplicationInfo-readonly labelId: long-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## moduleName

```TypeScript
readonly moduleName: string
```

应用包的模块名，返回entry模块的moduleName。若不存在entry模块则返回feature模块的moduleName。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-PreinstalledApplicationInfo-readonly moduleName: string--><!--Device-PreinstalledApplicationInfo-readonly moduleName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

