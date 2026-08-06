# @ohos.nearlink.scan

Provides methods for scanning and discovering nearby devices.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-declare namespace scan--><!--Device-unnamed-declare namespace scan-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Summary

### Functions

| Name | Description |
| --- | --- |
| [offDeviceFound](arkts-connectivity-scan-offdevicefound-f.md#offdevicefound) | Unsubscribes from NearLink scan results. |
| [onDeviceFound](arkts-connectivity-scan-ondevicefound-f.md#ondevicefound) | Subscribes to NearLink scan results.  This event is accessible only to applications that granted the ohos.permission.NEARLINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_ACCESS permission.If the application is granted the ohos.permission.GET\_\_\_ESCAPED\_UNDERSCORE\_\_\_NEARLINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_PEER\_\_\_ESCAPED\_UNDERSCORE\_\_\_MAC permission,the callback returns the real device address; otherwise, a random device address is returned. |
| [startScan](arkts-connectivity-scan-startscan-f.md#startscan) | Starts scanning for specified NearLink devices with filters.It is allowed to set filter parameter to {@code null} if you do not want to use filter. |
| [stopScan](arkts-connectivity-scan-stopscan-f.md#stopscan) | Stops scanning. |

### Interfaces

| Name | Description |
| --- | --- |
| [ScanFilters](arkts-connectivity-scan-scanfilters-i.md) | Describes the scan filters. |
| [ScanOptions](arkts-connectivity-scan-scanoptions-i.md) | Describes the parameters for scan. |
| [ScanResults](arkts-connectivity-scan-scanresults-i.md) | Describes the contents of the scan results. |

### Enums

| Name | Description |
| --- | --- |
| [ScanMode](arkts-connectivity-scan-scanmode-e.md) | The enum of scan mode. |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [ScanMode](arkts-connectivity-scan-scanmode-e-sys.md) | The enum of scan mode. |
<!--DelEnd-->

