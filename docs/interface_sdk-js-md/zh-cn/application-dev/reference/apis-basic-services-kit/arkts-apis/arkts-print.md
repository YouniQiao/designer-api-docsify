# @ohos.print

该模块为基本打印的操作API，提供调用基础打印功能的接口。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Print.PrintFramework

## 导入模块

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [addPrinter](arkts-basicservices-print-addprinter-f.md) |
| [addPrinterToDiscovery](arkts-basicservices-print-addprintertodiscovery-f.md) |
| [connectPrinter](arkts-basicservices-print-connectprinter-f.md) |
| [connectPrinter](arkts-basicservices-print-connectprinter-f.md) |
| [getAddedPrinters](arkts-basicservices-print-getaddedprinters-f.md) |
| [getPrinterInformationById](arkts-basicservices-print-getprinterinformationbyid-f.md) |
| [notifyWatermarkComplete](arkts-basicservices-print-notifywatermarkcomplete-f.md) |
| [off](arkts-basicservices-print-off-f.md#offprinterchange) |
| [offPrinterChange](arkts-basicservices-print-offprinterchange-f.md) |
| [on](arkts-basicservices-print-on-f.md#onprinterchange) |
| [onPrinterChange](arkts-basicservices-print-onprinterchange-f.md) |
| [print](arkts-basicservices-print-f.md) |
| [print](arkts-basicservices-print-f.md) |
| [print](arkts-basicservices-print-f.md) |
| [print](arkts-basicservices-print-f.md) |
| [print](arkts-basicservices-print-f.md) |
| [registerWatermarkCallback](arkts-basicservices-print-registerwatermarkcallback-f.md) |
| [removePrinterFromDiscovery](arkts-basicservices-print-removeprinterfromdiscovery-f.md) |
| [startDiscoverPrinter](arkts-basicservices-print-startdiscoverprinter-f.md) |
| [startDiscoverPrinter](arkts-basicservices-print-startdiscoverprinter-f.md) |
| [startPrint](arkts-basicservices-print-startprint-f.md) |
| [stopDiscoverPrinter](arkts-basicservices-print-stopdiscoverprinter-f.md) |
| [stopDiscoverPrinter](arkts-basicservices-print-stopdiscoverprinter-f.md) |
| [unregisterWatermarkCallback](arkts-basicservices-print-unregisterwatermarkcallback-f.md) |
| [updatePrinterInDiscovery](arkts-basicservices-print-updateprinterindiscovery-f.md) |
| [updatePrinterInformation](arkts-basicservices-print-updateprinterinformation-f.md) |
| [updatePrintJobState](arkts-basicservices-print-updateprintjobstate-f.md) |
| [updatePrintJobState](arkts-basicservices-print-updateprintjobstate-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addPrinters](arkts-basicservices-print-addprinters-f-sys.md) |
| [addPrinters](arkts-basicservices-print-addprinters-f-sys.md) |
| [addPrinterToCups](arkts-basicservices-print-addprintertocups-f-sys.md) |
| [analyzePrintEvents](arkts-basicservices-print-analyzeprintevents-f-sys.md) |
| [authPrintJob](arkts-basicservices-print-authprintjob-f-sys.md) |
| [authSmbDeviceAsRegisteredUser](arkts-basicservices-print-authsmbdeviceasregistereduser-f-sys.md) |
| [cancelPrintJob](arkts-basicservices-print-cancelprintjob-f-sys.md) |
| [cancelPrintJob](arkts-basicservices-print-cancelprintjob-f-sys.md) |
| [checkPreferencesConflicts](arkts-basicservices-print-checkpreferencesconflicts-f-sys.md) |
| [connectPrinterByIdAndPpd](arkts-basicservices-print-connectprinterbyidandppd-f-sys.md) |
| [connectPrinterByIpAndPpd](arkts-basicservices-print-connectprinterbyipandppd-f-sys.md) |
| [deletePrinterFromCups](arkts-basicservices-print-deleteprinterfromcups-f-sys.md) |
| [disconnectPrinter](arkts-basicservices-print-disconnectprinter-f-sys.md) |
| [disconnectPrinter](arkts-basicservices-print-disconnectprinter-f-sys.md) |
| [discoverUsbPrinters](arkts-basicservices-print-discoverusbprinters-f-sys.md) |
| [getPrinterDefaultPreferences](arkts-basicservices-print-getprinterdefaultpreferences-f-sys.md) |
| [getPrinterInfoById](arkts-basicservices-print-getprinterinfobyid-f-sys.md) |
| [getSharedHosts](arkts-basicservices-print-getsharedhosts-f-sys.md) |
| [notifyPrintService](arkts-basicservices-print-notifyprintservice-f-sys.md#notifyprintservicespooler_closed_for_cancelled-spooler_closed_for_started) |
| [notifyPrintService](arkts-basicservices-print-notifyprintservice-f-sys.md#notifyprintservicespooler_closed_for_cancelled-spooler_closed_for_started) |
| [notifyPrintServiceEvent](arkts-basicservices-print-notifyprintserviceevent-f-sys.md) |
| [notifyPrintServiceEvent](arkts-basicservices-print-notifyprintserviceevent-f-sys.md) |
| [notifyPrintServiceSpoolerCloseForCancelled](arkts-basicservices-print-notifyprintservicespoolercloseforcancelled-f-sys.md) |
| [notifyPrintServiceSpoolerCloseForCancelled](arkts-basicservices-print-notifyprintservicespoolercloseforcancelled-f-sys.md) |
| [notifyPrintServiceSpoolerCloseForStarted](arkts-basicservices-print-notifyprintservicespoolercloseforstarted-f-sys.md) |
| [notifyPrintServiceSpoolerCloseForStarted](arkts-basicservices-print-notifyprintservicespoolercloseforstarted-f-sys.md) |
| [off](arkts-basicservices-print-off-f-sys.md#offprinterstatechange) |
| [off](arkts-basicservices-print-off-f-sys.md#offjobstatechange) |
| [off](arkts-basicservices-print-off-f-sys.md#offextinfochange) |
| [offExtInfoChange](arkts-basicservices-print-offextinfochange-f-sys.md) |
| [offJobStateChange](arkts-basicservices-print-offjobstatechange-f-sys.md) |
| [offPrinterInfoQuery](arkts-basicservices-print-offprinterinfoquery-f-sys.md) |
| [offPrinterStateChange](arkts-basicservices-print-offprinterstatechange-f-sys.md) |
| [on](arkts-basicservices-print-on-f-sys.md#onprinterstatechange) |
| [on](arkts-basicservices-print-on-f-sys.md#onjobstatechange) |
| [on](arkts-basicservices-print-on-f-sys.md#onextinfochange) |
| [onExtInfoChange](arkts-basicservices-print-onextinfochange-f-sys.md) |
| [onJobStateChange](arkts-basicservices-print-onjobstatechange-f-sys.md) |
| [onPrinterInfoQuery](arkts-basicservices-print-onprinterinfoquery-f-sys.md) |
| [onPrinterStateChange](arkts-basicservices-print-onprinterstatechange-f-sys.md) |
| [queryAllActivePrintJobs](arkts-basicservices-print-queryallactiveprintjobs-f-sys.md) |
| [queryAllPrinterExtensionInfos](arkts-basicservices-print-queryallprinterextensioninfos-f-sys.md) |
| [queryAllPrinterExtensionInfos](arkts-basicservices-print-queryallprinterextensioninfos-f-sys.md) |
| [queryAllPrinterPpds](arkts-basicservices-print-queryallprinterppds-f-sys.md) |
| [queryAllPrintJobs](arkts-basicservices-print-queryallprintjobs-f-sys.md) |
| [queryAllPrintJobs](arkts-basicservices-print-queryallprintjobs-f-sys.md) |
| [queryPrinterCapability](arkts-basicservices-print-queryprintercapability-f-sys.md) |
| [queryPrinterCapability](arkts-basicservices-print-queryprintercapability-f-sys.md) |
| [queryPrinterCapabilityByUri](arkts-basicservices-print-queryprintercapabilitybyuri-f-sys.md) |
| [queryPrinterInfoByIp](arkts-basicservices-print-queryprinterinfobyip-f-sys.md) |
| [queryPrintJobById](arkts-basicservices-print-queryprintjobbyid-f-sys.md) |
| [queryPrintJobById](arkts-basicservices-print-queryprintjobbyid-f-sys.md) |
| [queryPrintJobList](arkts-basicservices-print-queryprintjoblist-f-sys.md) |
| [queryPrintJobList](arkts-basicservices-print-queryprintjoblist-f-sys.md) |
| [queryRecommendDriversById](arkts-basicservices-print-queryrecommenddriversbyid-f-sys.md) |
| [removePrinters](arkts-basicservices-print-removeprinters-f-sys.md) |
| [removePrinters](arkts-basicservices-print-removeprinters-f-sys.md) |
| [requestPrintPreview](arkts-basicservices-print-requestprintpreview-f-sys.md) |
| [requestPrintPreview](arkts-basicservices-print-requestprintpreview-f-sys.md) |
| [restartPrintJob](arkts-basicservices-print-restartprintjob-f-sys.md) |
| [savePdfFileJob](arkts-basicservices-print-savepdffilejob-f-sys.md) |
| [setDefaultPrinter](arkts-basicservices-print-setdefaultprinter-f-sys.md) |
| [setPrinterPreferences](arkts-basicservices-print-setprinterpreferences-f-sys.md) |
| [startGettingPrintFile](arkts-basicservices-print-startgettingprintfile-f-sys.md) |
| [startPrintJob](arkts-basicservices-print-startprintjob-f-sys.md) |
| [startPrintJob](arkts-basicservices-print-startprintjob-f-sys.md) |
| [updateExtensionInfo](arkts-basicservices-print-updateextensioninfo-f-sys.md) |
| [updateExtensionInfo](arkts-basicservices-print-updateextensioninfo-f-sys.md) |
| [updatePrinters](arkts-basicservices-print-updateprinters-f-sys.md) |
| [updatePrinters](arkts-basicservices-print-updateprinters-f-sys.md) |
| [updatePrinterState](arkts-basicservices-print-updateprinterstate-f-sys.md) |
| [updatePrinterState](arkts-basicservices-print-updateprinterstate-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [PpdInfo](arkts-basicservices-print-ppdinfo-i.md) |
| [PreviewAttribute](arkts-basicservices-print-previewattribute-i.md) |
| [PrintAttributes](arkts-basicservices-print-printattributes-i.md) |
| [PrintDocumentAdapter](arkts-basicservices-print-printdocumentadapter-i.md) |
| [PrinterCapabilities](arkts-basicservices-print-printercapabilities-i.md) |
| [PrinterCapability](arkts-basicservices-print-printercapability-i.md) |
| [PrinterInfo](arkts-basicservices-print-printerinfo-i.md) |
| [PrinterInformation](arkts-basicservices-print-printerinformation-i.md) |
| [PrinterPreferences](arkts-basicservices-print-printerpreferences-i.md) |
| [PrinterRange](arkts-basicservices-print-printerrange-i.md) |
| [PrintJob](arkts-basicservices-print-printjob-i.md) |
| [PrintJobData](arkts-basicservices-print-printjobdata-i.md) |
| [PrintMargin](arkts-basicservices-print-printmargin-i.md) |
| [PrintPageRange](arkts-basicservices-print-printpagerange-i.md) |
| [PrintPageSize](arkts-basicservices-print-printpagesize-i.md) |
| [PrintResolution](arkts-basicservices-print-printresolution-i.md) |
| [PrintTask](arkts-basicservices-print-printtask-i.md) |
| [SharedHost](arkts-basicservices-print-sharedhost-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [PrinterExtensionInfo](arkts-basicservices-print-printerextensioninfo-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [ApplicationEvent](arkts-basicservices-print-applicationevent-e.md) |
| [DefaultPrinterType](arkts-basicservices-print-defaultprintertype-e.md) |
| [DocFlavor](arkts-basicservices-print-docflavor-e.md) |
| [PrintColorMode](arkts-basicservices-print-printcolormode-e.md) |
| [PrintDirectionMode](arkts-basicservices-print-printdirectionmode-e.md) |
| [PrintDocumentAdapterState](arkts-basicservices-print-printdocumentadapterstate-e.md) |
| [PrintDocumentFormat](arkts-basicservices-print-printdocumentformat-e.md) |
| [PrintDuplexMode](arkts-basicservices-print-printduplexmode-e.md) |
| [PrinterEvent](arkts-basicservices-print-printerevent-e.md) |
| [PrintErrorCode](arkts-basicservices-print-printerrorcode-e.md) |
| [PrinterState](arkts-basicservices-print-printerstate-e.md) |
| [PrinterStatus](arkts-basicservices-print-printerstatus-e.md) |
| [PrintFileCreationState](arkts-basicservices-print-printfilecreationstate-e.md) |
| [PrintJobState](arkts-basicservices-print-printjobstate-e.md) |
| [PrintJobSubState](arkts-basicservices-print-printjobsubstate-e.md) |
| [PrintOrientationMode](arkts-basicservices-print-printorientationmode-e.md) |
| [PrintPageType](arkts-basicservices-print-printpagetype-e.md) |
| [PrintQuality](arkts-basicservices-print-printquality-e.md) |
| [WatermarkHandleResult](arkts-basicservices-print-watermarkhandleresult-e.md) |

### 类型

| 名称 |
| --- |
| [PrinterChangeCallback](arkts-basicservices-print-printerchangecallback-t.md) |
| [WatermarkCallback](arkts-basicservices-print-watermarkcallback-t.md) |

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [ExtInfoChangeCallback](arkts-basicservices-print-extinfochangecallback-t-sys.md) |
| [PrinterInfoQueryCallback](arkts-basicservices-print-printerinfoquerycallback-t-sys.md) |
| [PrinterStateChangeCallback](arkts-basicservices-print-printerstatechangecallback-t-sys.md) |
| [PrintJobStateChangeCallback](arkts-basicservices-print-printjobstatechangecallback-t-sys.md) |
<!--DelEnd-->
