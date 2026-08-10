# @ohos.nearlink.cdsm

提供与星闪CDSM（合作设备集合管理）相关的方法。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace cdsm--><!--Device-unnamed-declare namespace cdsm-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { cdsm } from 'kits/@kit.ConnectivityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createCdsmClient](arkts-connectivity-cdsm-createcdsmclient-f.md#createcdsmclient) | 创建CDSM客户端实例。 |

### Interfaces

| Name | Description |
| --- | --- |
| [CdsmClient](arkts-connectivity-cdsm-cdsmclient-i.md) | 管理CDSM客户端实例。在调用任何CDSM客户端方法之前，您必须使用{@link createCdsmClient}来创建CDSM客户端实例。 |
| [CdsmInfo](arkts-connectivity-cdsm-cdsminfo-i.md) | 描述合作设备集信息。 |
| [CdsmMemberInfo](arkts-connectivity-cdsm-cdsmmemberinfo-i.md) | 描述合作设备集的成员信息。 |

### Enums

| Name | Description |
| --- | --- |
| [CdsmConnectionState](arkts-connectivity-cdsm-cdsmconnectionstate-e.md) | 成员连接状态的枚举。 |

