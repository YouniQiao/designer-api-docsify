# UpgradeOptions (System API)

升级选项，包含升级指令等配置，用于指定升级操作类型。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-update-export interface UpgradeOptions--><!--Device-update-export interface UpgradeOptions-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { update } from 'kits/@kit.BasicServicesKit';
```

## order

```TypeScript
order: Order
```

升级指令。用于指定升级操作的执行方式。取值原则：DOWNLOAD仅下载升级包，适用于需要先下载后手动安装的场景；INSTALL仅安装已下载的升级包，适用于已下载完成需直接安装的场景；DOWNLOAD_AND_INSTALL下载并安装，适用于完整升级流程；APPLY仅生效，适用于已安装需重启生效的场景；INSTALL_AND_APPLY安装并生效，适用于安装后立即重启生效的场景。应根据当前升级状态和业务需求选择合适的指令。

**Type:** [Order](arkts-basicservices-update-order-e-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-UpgradeOptions-order: Order--><!--Device-UpgradeOptions-order: Order-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

