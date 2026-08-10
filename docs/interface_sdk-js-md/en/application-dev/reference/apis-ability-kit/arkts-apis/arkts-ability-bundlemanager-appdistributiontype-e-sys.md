# AppDistributionType (System API)

标识应用[HarmonyAppProvision配置文件说明](../../../security/app-provision-structure.md)。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-bundleManager-export enum AppDistributionType--><!--Device-bundleManager-export enum AppDistributionType-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## APP_GALLERY

```TypeScript
APP_GALLERY = 1
```

应用市场安装的应用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AppDistributionType-APP_GALLERY = 1--><!--Device-AppDistributionType-APP_GALLERY = 1-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## ENTERPRISE

```TypeScript
ENTERPRISE = 2
```

企业应用，可以安装到个人设备上。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AppDistributionType-ENTERPRISE = 2--><!--Device-AppDistributionType-ENTERPRISE = 2-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## ENTERPRISE_NORMAL

```TypeScript
ENTERPRISE_NORMAL = 3
```

普通企业应用，只能通过企业MDM应用安装在企业设备上。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AppDistributionType-ENTERPRISE_NORMAL = 3--><!--Device-AppDistributionType-ENTERPRISE_NORMAL = 3-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## ENTERPRISE_MDM

```TypeScript
ENTERPRISE_MDM = 4
```

企业MDM应用，只能安装在企业设备上。需要被激活  
[adminManager.enableAdmin](../../apis-mdm-kit/arkts-apis/arkts-mdm-adminmanager-enableadmin-f.md/arkts-mdm-adminmanager-enableadmin-f.md#enableadmin)后，才能安装普通企业应用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AppDistributionType-ENTERPRISE_MDM = 4--><!--Device-AppDistributionType-ENTERPRISE_MDM = 4-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## OS_INTEGRATION

```TypeScript
OS_INTEGRATION = 5
```

系统预置应用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AppDistributionType-OS_INTEGRATION = 5--><!--Device-AppDistributionType-OS_INTEGRATION = 5-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## CROWDTESTING

```TypeScript
CROWDTESTING = 6
```

众包测试应用，是由应用市场分发给部分用户，有一定的有效期的特定应用，系统检测到应用的有效期到期后，会通知用户到应用市场更新release版本的应用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AppDistributionType-CROWDTESTING = 6--><!--Device-AppDistributionType-CROWDTESTING = 6-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## NONE

```TypeScript
NONE = 7
```

其他。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AppDistributionType-NONE = 7--><!--Device-AppDistributionType-NONE = 7-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

