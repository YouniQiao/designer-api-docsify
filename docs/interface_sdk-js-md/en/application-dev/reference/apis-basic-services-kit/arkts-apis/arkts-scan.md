# @ohos.scan

This module provides JavaScript APIs of the scan framework for discovering and connecting to scanners.

> **NOTE：**
> 
> This topic describes only public APIs provided by the module.

**Since:** 20

**System capability:** SystemCapability.Print.PrintFramework

## Modules to Import

```TypeScript
import { scan } from 'kits/@kit.BasicServicesKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cancelScan](arkts-basicservices-scan-cancelscan-f.md) |
| [closeScanner](arkts-basicservices-scan-closescanner-f.md) |
| [exit](arkts-basicservices-scan-exit-f.md) |
| [getPictureScanProgress](arkts-basicservices-scan-getpicturescanprogress-f.md) |
| [getScannerCurrentSetting](arkts-basicservices-scan-getscannercurrentsetting-f.md) |
| [getScannerParameter](arkts-basicservices-scan-getscannerparameter-f.md) |
| [init](arkts-basicservices-scan-init-f.md) |
| [off](arkts-basicservices-scan-off-f.md#offscandevicefound) |
| [off](arkts-basicservices-scan-off-f.md#offscandevicesync) |
| [on](arkts-basicservices-scan-on-f.md#onscandevicefound) |
| [on](arkts-basicservices-scan-on-f.md#onscandevicesync) |
| [openScanner](arkts-basicservices-scan-openscanner-f.md) |
| [setScanAutoOption](arkts-basicservices-scan-setscanautooption-f.md) |
| [setScannerParameter](arkts-basicservices-scan-setscannerparameter-f.md) |
| [startScan](arkts-basicservices-scan-startscan-f.md) |
| [startScannerDiscovery](arkts-basicservices-scan-startscannerdiscovery-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addScanner](arkts-basicservices-scan-addscanner-f-sys.md) |
| [deleteScanner](arkts-basicservices-scan-deletescanner-f-sys.md) |
| [getAddedScanners](arkts-basicservices-scan-getaddedscanners-f-sys.md) |
| off |
| off |
| on |
| on |
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
