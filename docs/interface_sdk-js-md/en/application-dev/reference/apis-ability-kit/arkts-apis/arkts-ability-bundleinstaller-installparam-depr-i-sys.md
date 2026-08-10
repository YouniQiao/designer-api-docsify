# InstallParam (System API)

安装、恢复或卸载时需要指定的参数。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.bundle.installer:installer.InstallParam](arkts-ability-installer-installparam-i-sys.md)

<!--Device-unnamed-export interface InstallParam--><!--Device-unnamed-export interface InstallParam-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

## installFlag

```TypeScript
installFlag: number
```

指示安装标志, 默认值：1。 &lt;/br&gt;取值范围：&lt;/br&gt;1: 覆盖安装。&lt;/br&gt;16: 免安装。

**Type:** number

**Default:** Indicates the install flag

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.bundle.installer:installer.InstallParam.installFlag](arkts-ability-installer-installparam-i-sys.md#installflag)

<!--Device-InstallParam-installFlag: number--><!--Device-InstallParam-installFlag: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

## isKeepData

```TypeScript
isKeepData: boolean
```

指示应用卸载时是否保留包数据，默认值：false，true表示保留，false表示不保留。

**Type:** boolean

**Default:** Indicates whether the param has data

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.bundle.installer:installer.InstallParam.isKeepData](arkts-ability-installer-installparam-i-sys.md#iskeepdata)

<!--Device-InstallParam-isKeepData: boolean--><!--Device-InstallParam-isKeepData: boolean-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

## userId

```TypeScript
userId: number
```

指示用户id, 默认值：调用方的userId。

**Type:** number

**Default:** Indicates the user id

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.bundle.installer:installer.InstallParam.userId](arkts-ability-installer-installparam-i-sys.md#userid)

<!--Device-InstallParam-userId: number--><!--Device-InstallParam-userId: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

