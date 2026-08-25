# @ohos.scan

该模块为扫描框架的js-api接口文档，提供发现和连接扫描仪的能力。

> **说明：**
> 
> 当前界面仅包含本模块的公开接口。

**起始版本：** 20

**系统能力：** SystemCapability.Print.PrintFramework

## 导入模块

```TypeScript
import { scan } from 'kits/@kit.BasicServicesKit';
```

## 汇总

### 函数

| 名称 |
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
### 函数（系统接口）

| 名称 |
| --- |
| [addScanner](arkts-basicservices-scan-addscanner-f-sys.md) |
| [deleteScanner](arkts-basicservices-scan-deletescanner-f-sys.md) |
| [getAddedScanners](arkts-basicservices-scan-getaddedscanners-f-sys.md) |
| off |
| off |
| on |
| on |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [PictureScanProgress](arkts-basicservices-scan-picturescanprogress-i.md) |
| [Range](arkts-basicservices-scan-range-i.md) |
| [ScannerDevice](arkts-basicservices-scan-scannerdevice-i.md) |
| [ScannerOptionValue](arkts-basicservices-scan-scanneroptionvalue-i.md) |
| [ScannerParameter](arkts-basicservices-scan-scannerparameter-i.md) |
| [ScannerSyncDevice](arkts-basicservices-scan-scannersyncdevice-i.md) |

### 枚举

| 名称 |
| --- |
| [ConstraintType](arkts-basicservices-scan-constrainttype-e.md) |
| [OptionValueType](arkts-basicservices-scan-optionvaluetype-e.md) |
| [PhysicalUnit](arkts-basicservices-scan-physicalunit-e.md) |
| [ScanErrorCode](arkts-basicservices-scan-scanerrorcode-e.md) |
| [ScannerDiscoveryMode](arkts-basicservices-scan-scannerdiscoverymode-e.md) |
| [ScannerSyncMode](arkts-basicservices-scan-scannersyncmode-e.md) |
