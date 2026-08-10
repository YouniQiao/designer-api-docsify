# UpgradeAction (System API)

升级方式。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-update-export enum UpgradeAction--><!--Device-update-export enum UpgradeAction-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## UPGRADE

```TypeScript
UPGRADE = 'upgrade'
```

差分包，仅包含与当前版本的差异部分，适用于已安装基础版本的增量升级场景。详见[术语](../../../basic-services/update/update-kit-term.md)。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-UpgradeAction-UPGRADE = 'upgrade'--><!--Device-UpgradeAction-UPGRADE = 'upgrade'-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## RECOVERY

```TypeScript
RECOVERY = 'recovery'
```

修复包，用于修复系统异常或恢复系统功能的特殊升级包，适用于系统故障修复场景。详见[术语](../../../basic-services/update/update-kit-term.md)。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-UpgradeAction-RECOVERY = 'recovery'--><!--Device-UpgradeAction-RECOVERY = 'recovery'-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

