# @ohos.distributedHardware.hardwareManager

分布式硬件管理模块提供控制分布式硬件的能力，包括暂停、恢复和停止被控端分布式硬件业务。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace hardwareManager--><!--Device-unnamed-declare namespace hardwareManager-End-->

**System capability:** SystemCapability.DistributedHardware.DistributedHardwareFWK

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { hardwareManager } from 'kits/@kit.DistributedServiceKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [pauseDistributedHardware](arkts-distributedservice-hardwaremanager-pausedistributedhardware-f-sys.md#pausedistributedhardware) | 暂停被控端分布式硬件业务。使用promise异步回调。 |
| [resumeDistributedHardware](arkts-distributedservice-hardwaremanager-resumedistributedhardware-f-sys.md#resumedistributedhardware) | 恢复被控端分布式硬件业务。使用promise异步回调。 |
| [stopDistributedHardware](arkts-distributedservice-hardwaremanager-stopdistributedhardware-f-sys.md#stopdistributedhardware) | 停止被控端分布式硬件业务。使用promise异步回调。 |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [HardwareDescriptor](arkts-distributedservice-hardwaremanager-hardwaredescriptor-i-sys.md) | 表示分布式硬件的描述信息。 |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [DistributedHardwareErrorCode](arkts-distributedservice-hardwaremanager-distributedhardwareerrorcode-e-sys.md) | 分布式硬件错误码的枚举。 |
| [DistributedHardwareType](arkts-distributedservice-hardwaremanager-distributedhardwaretype-e-sys.md) | 表示分布式硬件类型。 |
<!--DelEnd-->

