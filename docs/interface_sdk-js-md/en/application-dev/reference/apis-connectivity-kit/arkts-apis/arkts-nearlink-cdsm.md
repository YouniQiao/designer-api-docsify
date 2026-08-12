# @ohos.nearlink.cdsm

Provides methods related to nearlink CDSM(Coordinated Devices Set Management).

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace cdsm--><!--Device-unnamed-declare namespace cdsm-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { cdsm } from '@kit.ConnectivityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createCdsmClient](arkts-connectivity-cdsm-createcdsmclient-f.md#createcdsmclient) | Creates a CDSM client instance. |

### Interfaces

| Name | Description |
| --- | --- |
| [CdsmClient](arkts-connectivity-cdsm-cdsmclient-i.md) | Manages a CDSM client instance. Before invoking any CDSM client method,you must use [createCdsmClient](arkts-connectivity-cdsm-createcdsmclient-f.md#createCdsmClient) to create a CDSM client instance. |
| [CdsmInfo](arkts-connectivity-cdsm-cdsminfo-i.md) | Describes the coordinated devices set information. |
| [CdsmMemberInfo](arkts-connectivity-cdsm-cdsmmemberinfo-i.md) | Describes the member information of coordinated devices set. |

### Enums

| Name | Description |
| --- | --- |
| [CdsmConnectionState](arkts-connectivity-cdsm-cdsmconnectionstate-e.md) | The enum of member's connection state. |

