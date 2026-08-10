# TaskBody (System API)

任务数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-update-export interface TaskBody--><!--Device-update-export interface TaskBody-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { update } from 'kits/@kit.BasicServicesKit';
```

## errorMessages

```TypeScript
errorMessages: Array<ErrorMessage>
```

错误信息。

**Type:** Array&lt;ErrorMessage&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-TaskBody-errorMessages: Array<ErrorMessage>--><!--Device-TaskBody-errorMessages: Array<ErrorMessage>-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## installMode

```TypeScript
installMode: int
```

安装模式，取值范围[0, 2]。取值原则：0为正常升级，适用于用户主动触发升级的场景；1为夜间升级，适用于设置夜间时段自动升级的场景；2为自动升级，适用于系统自动检测并执行升级的场景。应根据升级策略和用户体验需求选择。超出范围时抛出异常。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-TaskBody-installMode: int--><!--Device-TaskBody-installMode: int-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## progress

```TypeScript
progress: int
```

进度，单位为%，取值范围[0, 100]，超出范围时抛出异常。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-TaskBody-progress: int--><!--Device-TaskBody-progress: int-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## status

```TypeScript
status: UpgradeStatus
```

升级状态。用于标识升级任务的当前执行阶段。包含下载状态（WAITING_DOWNLOAD到DOWNLOAD_FAIL）、安装状态（WAITING_INSTALL到UPDATING）、生效状态（WAITING_APPLY到APPLYING）和最终结果（UPGRADE_SUCCESS或UPGRADE_FAIL），用于任务状态监控、进度展示和异常处理等场景。

**Type:** [UpgradeStatus](arkts-basicservices-update-upgradestatus-e-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-TaskBody-status: UpgradeStatus--><!--Device-TaskBody-status: UpgradeStatus-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## subStatus

```TypeScript
subStatus: int
```

子状态，取值范围参考[UpgradeStatus](arkts-basicservices-update-upgradestatus-e-sys.md)状态码。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-TaskBody-subStatus: int--><!--Device-TaskBody-subStatus: int-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## versionComponents

```TypeScript
versionComponents: Array<VersionComponent>
```

版本组件。

**Type:** Array&lt;VersionComponent&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-TaskBody-versionComponents: Array<VersionComponent>--><!--Device-TaskBody-versionComponents: Array<VersionComponent>-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## versionDigestInfo

```TypeScript
versionDigestInfo: VersionDigestInfo
```

版本摘要。

**Type:** [VersionDigestInfo](arkts-basicservices-update-versiondigestinfo-i-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-TaskBody-versionDigestInfo: VersionDigestInfo--><!--Device-TaskBody-versionDigestInfo: VersionDigestInfo-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

