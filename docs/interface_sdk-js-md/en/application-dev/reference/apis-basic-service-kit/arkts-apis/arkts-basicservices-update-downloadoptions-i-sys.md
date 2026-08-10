# DownloadOptions (System API)

下载选项，包含allowNetwork(允许下载的网络类型)和order(升级指令)字段，用于控制下载行为。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-update-export interface DownloadOptions--><!--Device-update-export interface DownloadOptions-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { update } from 'kits/@kit.BasicServicesKit';
```

## allowNetwork

```TypeScript
allowNetwork: NetType
```

网络类型，允许下载的网络类型。设置CELLULAR仅允许数据网络下载，设置WIFI仅允许WIFI下载，设置CELLULAR_AND_WIFI允许两者均可下载。建议根据升级包大小和网络环境选择：大文件升级包建议使用WIFI避免流量消耗和提升下载速度；移动场景或无WIFI环境可使用CELLULAR；不确定网络环境建议使用CELLULAR_AND_WIFI。

**Type:** [NetType](arkts-basicservices-update-nettype-e-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-DownloadOptions-allowNetwork: NetType--><!--Device-DownloadOptions-allowNetwork: NetType-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## order

```TypeScript
order: Order
```

取值原则：DOWNLOAD仅下载，适用于先下载后手动安装场景；INSTALL仅安装，适用于直接安装已下载的升级包场景；DOWNLOAD_AND_INSTALL下载并安装，适用于完整升级流程；APPLY仅生效，适用于已安装需重启生效场景；INSTALL_AND_APPLY安装并生效，适用于安装后立即重启生效场景。

**Type:** [Order](arkts-basicservices-update-order-e-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-DownloadOptions-order: Order--><!--Device-DownloadOptions-order: Order-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

