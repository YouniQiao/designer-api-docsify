# @ohos.nearlink.scan(NearLink Scanning Capability)

This module provides the definition of the NearLink scanning mode.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import scan from '@kit.ConnectivityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [offDeviceFound(NearLink Scanning Capability)](arkts-connectivity-scan-offdevicefound-f.md) | Unsubscribes from NearLink scanning results. This API uses an asynchronous callback to return the result. |
| [onDeviceFound(NearLink Scanning Capability)](arkts-connectivity-scan-ondevicefound-f.md) | Subscribes to NearLink scanning results. This API uses an asynchronous callback to return the result.The app must have the **ohos.permission.ACCESS_NEARLINK** permission to receive this event. |
| [startScan(NearLink Scanning Capability)](arkts-connectivity-scan-startscan-f.md) | Starts NearLink scanning. This API uses a promise to return the result. You need to call [scan.onDeviceFound](arkts-connectivity-scan-ondevicefound-f.md) to subscribe to the scanning results. After this API initiates scanning, the scanned device information is reported through the [scan.onDeviceFound](arkts-connectivity-scan-ondevicefound-f.md) callback. After the scanning is complete, you can call [scan.stopScan](arkts-connectivity-scan-stopscan-f.md) to stop scanning. |
| [stopScan(NearLink Scanning Capability)](arkts-connectivity-scan-stopscan-f.md) | Stops NearLink scanning. This API uses a promise to return the result. |

### Interfaces

| Name | Description |
| --- | --- |
| [ScanFilters(NearLink Scanning Capability)](arkts-connectivity-scan-scanfilters-i.md) | Defines the scan filters |
| [ScanOptions(NearLink Scanning Capability)](arkts-connectivity-scan-scanoptions-i.md) | Represents the scan options. |
| [ScanResults(NearLink Scanning Capability)](arkts-connectivity-scan-scanresults-i.md) | Represents the scanning results. |

### Enums

| Name | Description |
| --- | --- |
| [ScanMode(NearLink Scanning Capability)](arkts-connectivity-scan-scanmode-e.md) | Enumerates the scan modes. |

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [ScanMode(NearLink Scanning Capability)](arkts-connectivity-scan-scanmode-e-sys.md) | Enumerates the scan modes. |
<!--DelEnd-->
