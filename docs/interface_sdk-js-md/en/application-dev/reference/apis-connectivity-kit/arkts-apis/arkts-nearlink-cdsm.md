# @ohos.nearlink.cdsm

This module provides the coordinated devices set management (CDSM) capability for NearLink, including querying and subscribing to the coordinated devices set information of NearLink.

**Since:** 26.0.0

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
| [createCdsmClient](arkts-connectivity-cdsm-createcdsmclient-f.md) | Creates a CDSM client instance. |

### Interfaces

| Name | Description |
| --- | --- |
| [CdsmClient](arkts-connectivity-cdsm-cdsmclient-i.md) | Defines a CDSM client class, which provides APIs for obtaining the CDSM information of a remote device.  - Before using the methods of this class, call [cdsm.createCdsmClient](arkts-connectivity-cdsm-createcdsmclient-f.md) to construct an instance of this class.  This class is applicable to scenarios where you need to obtain the member devices and connection status changes of a group of NearLink devices (CDSM) and perform service coordination accordingly. For example, after a phone is paired with earphones, the phone can use the CDSM to query the left and right earphones and detect their connection status changes.An app only needs to create one [CdsmClient](arkts-connectivity-cdsm-cdsmclient-i.md) instance for a remote device. Repeated creation will increase unnecessary resource overhead. |
| [CdsmInfo](arkts-connectivity-cdsm-cdsminfo-i.md) | Represents the CDSM information. |
| [CdsmMemberInfo](arkts-connectivity-cdsm-cdsmmemberinfo-i.md) | Represents the information about member devices in the coordinated devices set. |

### Enums

| Name | Description |
| --- | --- |
| [CdsmConnectionState](arkts-connectivity-cdsm-cdsmconnectionstate-e.md) | Enumerates the connection states of member devices in a coordinated device set. |

