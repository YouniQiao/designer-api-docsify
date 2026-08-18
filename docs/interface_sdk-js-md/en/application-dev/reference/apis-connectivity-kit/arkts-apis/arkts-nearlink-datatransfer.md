# @ohos.nearlink.dataTransfer

Provides methods to operate and manage data transfer of NearLink.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace dataTransfer--><!--Device-unnamed-declare namespace dataTransfer-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { dataTransfer } from '@kit.ConnectivityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [connect](arkts-connectivity-datatransfer-connect-f.md) | Connects to a server. If the connection is successful, data can be sent to the server. |
| [createPort](arkts-connectivity-datatransfer-createport-f.md) | Creates a NearLink listening port that can receive data by UUID. |
| [destroyPort](arkts-connectivity-datatransfer-destroyport-f.md) | Destroys a listen port and releases related resources by UUID. |
| [disconnect](arkts-connectivity-datatransfer-disconnect-f.md) | Disconnects or stops an ongoing connection to a server. |
| [getConnectionState](arkts-connectivity-datatransfer-getconnectionstate-f.md) | Obtains the connection status for data transfer. |
| [offConnectionStateChanged](arkts-connectivity-datatransfer-offconnectionstatechanged-f.md) | Unsubscribes from the connection state change event. |
| [offReadData](arkts-connectivity-datatransfer-offreaddata-f.md) | Unsubscribes from the event reported when data is read from the port. |
| [onConnectionStateChanged](arkts-connectivity-datatransfer-onconnectionstatechanged-f.md) | Subscribes to the connection state change event. This event is accessible only to applications that granted the ohos.permission.NEARLINK_ACCESS permission. |
| [onReadData](arkts-connectivity-datatransfer-onreaddata-f.md) | Subscribes to the event reported when data is read from the port. This event is accessible only to applications that granted the ohos.permission.NEARLINK_ACCESS permission. |
| [writeData](arkts-connectivity-datatransfer-writedata-f.md) | Writes data by address and UUID. |

### Interfaces

| Name | Description |
| --- | --- |
| [ConnectionParams](arkts-connectivity-datatransfer-connectionparams-i.md) | Describes the parameters for connection. |
| [ConnectionResult](arkts-connectivity-datatransfer-connectionresult-i.md) | Describes the parameters for connection result. |
| [ConnectionStateParams](arkts-connectivity-datatransfer-connectionstateparams-i.md) | Describes the parameters required for obtaining the connection status. |
| [DataParams](arkts-connectivity-datatransfer-dataparams-i.md) | Describes the parameters for Data. |

### Enums

| Name | Description |
| --- | --- |
| [TransferMode](arkts-connectivity-datatransfer-transfermode-e.md) | Indicates the data transfer mode. |

### Types

| Name | Description |
| --- | --- |
| [ConnectionState](arkts-connectivity-datatransfer-connectionstate-t.md) | Indicates the connection state. |

