# @ohos.scan

This module provides JavaScript APIs of the scan framework for discovering and connecting to scanners. > **NOTE：**> > This topic describes only public APIs provided by the module.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace scan--><!--Device-unnamed-declare namespace scan-End-->

**System capability:** SystemCapability.Print.PrintFramework

## Modules to Import

```TypeScript
import { scan } from '@kit.BasicServicesKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cancelScan](arkts-basicservices-scan-cancelscan-f.md#cancelScan) |
| [closeScanner](arkts-basicservices-scan-closescanner-f.md#closeScanner) |
| [exit](arkts-basicservices-scan-exit-f.md#exit) |
| [getPictureScanProgress](arkts-basicservices-scan-getpicturescanprogress-f.md#getPictureScanProgress) |
| [getScannerCurrentSetting](arkts-basicservices-scan-getscannercurrentsetting-f.md#getScannerCurrentSetting) |
| [getScannerParameter](arkts-basicservices-scan-getscannerparameter-f.md#getScannerParameter) |
| [init](arkts-basicservices-scan-init-f.md#init) |
| [offScanDeviceFound](arkts-basicservices-scan-offscandevicefound-f.md#offScanDeviceFound) |
| [offScanDeviceSync](arkts-basicservices-scan-offscandevicesync-f.md#offScanDeviceSync) |
| [off_scanDeviceFound](arkts-basicservices-scan-offscandevicefound-f.md) |
| [off_scanDeviceSync](arkts-basicservices-scan-offscandevicesync-f.md) |
| [onScanDeviceFound](arkts-basicservices-scan-onscandevicefound-f.md#onScanDeviceFound) |
| [onScanDeviceSync](arkts-basicservices-scan-onscandevicesync-f.md#onScanDeviceSync) |
| [on_scanDeviceFound](arkts-basicservices-scan-onscandevicefound-f.md) |
| [on_scanDeviceSync](arkts-basicservices-scan-onscandevicesync-f.md) |
| [openScanner](arkts-basicservices-scan-openscanner-f.md#openScanner) |
| [setScanAutoOption](arkts-basicservices-scan-setscanautooption-f.md#setScanAutoOption) |
| [setScannerParameter](arkts-basicservices-scan-setscannerparameter-f.md#setScannerParameter) |
| [startScan](arkts-basicservices-scan-startscan-f.md#startScan) |
| [startScannerDiscovery](arkts-basicservices-scan-startscannerdiscovery-f.md#startScannerDiscovery) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addScanner](arkts-basicservices-scan-addscanner-f-sys.md#addScanner-(System-API)) |
| [deleteScanner](arkts-basicservices-scan-deletescanner-f-sys.md#deleteScanner-(System-API)) |
| [getAddedScanners](arkts-basicservices-scan-getaddedscanners-f-sys.md#getAddedScanners-(System-API)) |
| [offScanDeviceAdd](arkts-basicservices-scan-offscandeviceadd-f-sys.md#offScanDeviceAdd-(System-API)) |
| [offScanDeviceDel](arkts-basicservices-scan-offscandevicedel-f-sys.md#offScanDeviceDel-(System-API)) |
| [off_scanDeviceAdd](arkts-basicservices-scan-offscandeviceadd-f-sys.md) |
| [off_scanDeviceDel](arkts-basicservices-scan-offscandevicedel-f-sys.md) |
| [onScanDeviceAdd](arkts-basicservices-scan-onscandeviceadd-f-sys.md#onScanDeviceAdd-(System-API)) |
| [onScanDeviceDel](arkts-basicservices-scan-onscandevicedel-f-sys.md#onScanDeviceDel-(System-API)) |
| [on_scanDeviceAdd](arkts-basicservices-scan-onscandeviceadd-f-sys.md) |
| [on_scanDeviceDel](arkts-basicservices-scan-onscandevicedel-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PictureScanProgress](arkts-basicservices-scan-picturescanprogress-i.md) |
| [Range](arkts-basicservices-scan-range-i.md) |
| [ScannerDevice](arkts-basicservices-scan-scannerdevice-i.md) |
| [ScannerOptionValue](arkts-basicservices-scan-scanneroptionvalue-i.md) |
| [ScannerParameter](arkts-basicservices-scan-scannerparameter-i.md) |
| [ScannerSyncDevice](arkts-basicservices-scan-scannersyncdevice-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ConstraintType](arkts-basicservices-scan-constrainttype-e.md) |
| [OptionValueType](arkts-basicservices-scan-optionvaluetype-e.md) |
| [PhysicalUnit](arkts-basicservices-scan-physicalunit-e.md) |
| [ScanErrorCode](arkts-basicservices-scan-scanerrorcode-e.md) |
| [ScannerDiscoveryMode](arkts-basicservices-scan-scannerdiscoverymode-e.md) |
| [ScannerSyncMode](arkts-basicservices-scan-scannersyncmode-e.md) |
