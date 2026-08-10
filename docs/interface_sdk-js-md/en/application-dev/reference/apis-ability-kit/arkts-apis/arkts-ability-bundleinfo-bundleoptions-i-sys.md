# BundleOptions (System API)

应用包选项，用于设置或查询应用相关信息。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface BundleOptions--><!--Device-unnamed-export interface BundleOptions-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## abilityName

```TypeScript
abilityName?: string
```

Ability名称。默认值为空字符串。  
**模型约束：** 此接口仅可在Stage模型下使用。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BundleOptions-abilityName?: string--><!--Device-BundleOptions-abilityName?: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## appIndex

```TypeScript
appIndex?: int
```

应用分身ID。默认为0，表示主应用。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-BundleOptions-appIndex?: int--><!--Device-BundleOptions-appIndex?: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName?: string
```

应用包名。默认值为空字符串。  
**模型约束：** 此接口仅可在Stage模型下使用。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BundleOptions-bundleName?: string--><!--Device-BundleOptions-bundleName?: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## moduleName

```TypeScript
moduleName?: string
```

Ability所属的模块名称。默认值为空字符串。  
**模型约束：** 此接口仅可在Stage模型下使用。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BundleOptions-moduleName?: string--><!--Device-BundleOptions-moduleName?: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## userId

```TypeScript
userId?: int
```

用户ID。默认为当前调用方所在的用户。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-BundleOptions-userId?: int--><!--Device-BundleOptions-userId?: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

