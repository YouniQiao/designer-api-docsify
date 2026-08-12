# @ohos.scan

This module provides JavaScript APIs of the scan framework for discovering and connecting to scanners.

> **NOTE：**
> > This topic describes only public APIs provided by the module.

**Since:** 20

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
| [cancelScan](arkts-basicservices-scan-cancelscan-f.md#cancelscan) |
| [closeScanner](arkts-basicservices-scan-closescanner-f.md#closescanner) |
| [exit](arkts-basicservices-scan-exit-f.md#exit) |
| [getPictureScanProgress](arkts-basicservices-scan-getpicturescanprogress-f.md#getpicturescanprogress) |
| [getScannerCurrentSetting](arkts-basicservices-scan-getscannercurrentsetting-f.md#getscannercurrentsetting) |
| [getScannerParameter](arkts-basicservices-scan-getscannerparameter-f.md#getscannerparameter) |
| [init](arkts-basicservices-scan-init-f.md#init) |
| [off](arkts-basicservices-scan-off-f.md#off) |
| [off](arkts-basicservices-scan-off-f.md#off-1) |
| [on](arkts-basicservices-scan-on-f.md#on) |
| [on](arkts-basicservices-scan-on-f.md#on-1) |
| [openScanner](arkts-basicservices-scan-openscanner-f.md#openscanner) |
| [setScanAutoOption](arkts-basicservices-scan-setscanautooption-f.md#setscanautooption) |
| [setScannerParameter](arkts-basicservices-scan-setscannerparameter-f.md#setscannerparameter) |
| [startScan](arkts-basicservices-scan-startscan-f.md#startscan) |
| [startScannerDiscovery](arkts-basicservices-scan-startscannerdiscovery-f.md#startscannerdiscovery) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addScanner](arkts-basicservices-scan-addscanner-f-sys.md#addscanner) |
| [deleteScanner](arkts-basicservices-scan-deletescanner-f-sys.md#deletescanner) |
| [getAddedScanners](arkts-basicservices-scan-getaddedscanners-f-sys.md#getaddedscanners) |
| [off](arkts-basicservices-scan-off-f-sys.md#off-2) |
| [off](arkts-basicservices-scan-off-f-sys.md#off-3) |
| [on](arkts-basicservices-scan-on-f-sys.md#on-2) |
| [on](arkts-basicservices-scan-on-f-sys.md#on-3) |
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
