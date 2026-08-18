# @ohos.net.eap

The **eap** module provides the extensible authentication mechanism to enable third-party clients to access custom 80 2.1X (a port-based network access control protocol) authentication, such as Extensible Authentication Protocol (EAP) authentication.

**Since:** 20

<!--Device-unnamed-declare namespace eap--><!--Device-unnamed-declare namespace eap-End-->

**System capability:** SystemCapability.Communication.NetManager.Eap

## Modules to Import

```TypeScript
import { eap } from '@kit.NetworkKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [logOffEthEap](arkts-network-eap-logoffetheap-f.md) | Revokes the EAP-authenticated state of an Ethernet NIC. |
| [regCustomEapHandler](arkts-network-eap-regcustomeaphandler-f.md) | Registers a custom handler of Extensible Authentication Protocol (EAP) packets for extensible authentication. This API returns the result asynchronously through a callback. The system will encapsulate the eligible EAP packets into the callback function for enterprise applications to retrieve. |
| [replyCustomEapData](arkts-network-eap-replycustomeapdata-f.md) | Notifies the system of the extensible authentication result. > **NOTE：**> > - If this callback is used to process received EAP data packets, the customized portion added by the server must > be removed from the EAP data transmitted to the system. > > - If this callback is used to process sent EAP data packets, the EAP data transmitted to the system is the EAP > data with the customized portion added by the server. |
| [startEthEap](arkts-network-eap-startetheap-f.md) | Starts EAP authentication on an Ethernet NIC. |
| [unregCustomEapHandler](arkts-network-eap-unregcustomeaphandler-f.md) | Unregisters the custom handler of EAP packets for extensible authentication. This API returns the result asynchronously through a callback. |

### Interfaces

| Name | Description |
| --- | --- |
| [EapData](arkts-network-eap-eapdata-i.md) | Defines the EAP data. ​ |
| [EthEapProfile](arkts-network-eap-etheapprofile-i.md) | Represents the EAP profile information. |

### Enums

| Name | Description |
| --- | --- |
| [CustomResult](arkts-network-eap-customresult-e.md) | Enumerates the EAP authentication results. ​ |
| [EapMethod](arkts-network-eap-eapmethod-e.md) | Enumerates the EAP authentication methods. |
| [Phase2Method](arkts-network-eap-phase2method-e.md) | Enumerates the Phase 2 authentication methods. |

