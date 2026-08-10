# AlternateIconInfo

描述应用备用图标信息。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export interface AlternateIconInfo--><!--Device-unnamed-export interface AlternateIconInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## enabled

```TypeScript
readonly enabled: boolean
```

备用图标是否启用。

true：表示当前备用图标启用。

false：表示当前备用图标未启用。

**说明：** 应用最多只能启用一个备用图标。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlternateIconInfo-readonly enabled: boolean--><!--Device-AlternateIconInfo-readonly enabled: boolean-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## iconId

```TypeScript
readonly iconId: long
```

备用图标的资源id，是编译构建时根据应用配置的icon自动生成的资源id。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlternateIconInfo-readonly iconId: long--><!--Device-AlternateIconInfo-readonly iconId: long-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## iconName

```TypeScript
readonly iconName: string
```

备用图标的名称。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlternateIconInfo-readonly iconName: string--><!--Device-AlternateIconInfo-readonly iconName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

