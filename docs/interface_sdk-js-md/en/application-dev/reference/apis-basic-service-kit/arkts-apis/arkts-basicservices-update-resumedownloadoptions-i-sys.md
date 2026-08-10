# ResumeDownloadOptions (System API)

恢复下载选项，用于指定恢复下载的网络类型。对象包含allowNetwork字段，用于设置允许下载的网络类型。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-update-export interface ResumeDownloadOptions--><!--Device-update-export interface ResumeDownloadOptions-End-->

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

网络类型，允许恢复下载的网络类型。仅当已调用pauseDownload暂停下载后才能设置此参数。设置CELLULAR仅允许数据网络恢复下载，设置WIFI仅允许WIFI网络恢复下载，设置CELLULAR_AND_WIFI允许两者均可恢复下载。建议根据升级包大小和网络环境选择：升级包大小超过100MB建议使用WIFI避免流量消耗和提升下载速度；移动场景或无WIFI环境可使用CELLULAR；不确定网络环境建议使用CELLULAR_AND_WIFI。

**Type:** [NetType](arkts-basicservices-update-nettype-e-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ResumeDownloadOptions-allowNetwork: NetType--><!--Device-ResumeDownloadOptions-allowNetwork: NetType-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

