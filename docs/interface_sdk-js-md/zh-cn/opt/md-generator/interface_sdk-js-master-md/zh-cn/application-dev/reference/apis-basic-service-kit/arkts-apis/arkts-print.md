# @ohos.print

该模块为基本打印的操作API，提供调用基础打印功能的接口。

**起始版本：** 23

<!--Device-unnamed-declare namespace print--><!--Device-unnamed-declare namespace print-End-->

**系统能力：** SystemCapability.Print.PrintFramework

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [addPrinter](arkts-basicservices-print-addprinter-f.md#addprinter) |
| [addPrinterToDiscovery](arkts-basicservices-print-addprintertodiscovery-f.md#addprintertodiscovery) |
| [getAddedPrinters](arkts-basicservices-print-getaddedprinters-f.md#getaddedprinters) |
| [getPrinterInformationById](arkts-basicservices-print-getprinterinformationbyid-f.md#getprinterinformationbyid) |
| [notifyWatermarkComplete](arkts-basicservices-print-notifywatermarkcomplete-f.md#notifywatermarkcomplete) |
| [offPrinterChange](arkts-basicservices-print-offprinterchange-f.md#offprinterchange) |
| [off_printerChange](arkts-basicservices-print-offprinterchange-f.md#offprinterchange) |
| [onPrinterChange](arkts-basicservices-print-onprinterchange-f.md#onprinterchange) |
| [on_printerChange](arkts-basicservices-print-onprinterchange-f.md#onprinterchange) |
| [print](arkts-basicservices-print-f.md#print) |
| [print](arkts-basicservices-print-f.md#print) |
| [print](arkts-basicservices-print-f.md#print) |
| [print](arkts-basicservices-print-f.md#print) |
| [print](arkts-basicservices-print-f.md#print) |
| [registerWatermarkCallback](arkts-basicservices-print-registerwatermarkcallback-f.md#registerwatermarkcallback) |
| [removePrinterFromDiscovery](arkts-basicservices-print-removeprinterfromdiscovery-f.md#removeprinterfromdiscovery) |
| [startPrint](arkts-basicservices-print-startprint-f.md#startprint) |
| [unregisterWatermarkCallback](arkts-basicservices-print-unregisterwatermarkcallback-f.md#unregisterwatermarkcallback) |
| [updatePrinterInDiscovery](arkts-basicservices-print-updateprinterindiscovery-f.md#updateprinterindiscovery) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addPrinterToCups](arkts-basicservices-print-addprintertocups-f-sys.md#addprintertocups系统接口) |
| [addPrinters](arkts-basicservices-print-addprinters-f-sys.md#addprinters系统接口) |
| [addPrinters](arkts-basicservices-print-addprinters-f-sys.md#addprinters系统接口) |
| [analyzePrintEvents](arkts-basicservices-print-analyzeprintevents-f-sys.md#analyzeprintevents系统接口) |
| [authPrintJob](arkts-basicservices-print-authprintjob-f-sys.md#authprintjob系统接口) |
| [authSmbDeviceAsRegisteredUser](arkts-basicservices-print-authsmbdeviceasregistereduser-f-sys.md#authsmbdeviceasregistereduser系统接口) |
| [cancelPrintJob](arkts-basicservices-print-cancelprintjob-f-sys.md#cancelprintjob系统接口) |
| [cancelPrintJob](arkts-basicservices-print-cancelprintjob-f-sys.md#cancelprintjob系统接口) |
| [checkPreferencesConflicts](arkts-basicservices-print-checkpreferencesconflicts-f-sys.md#checkpreferencesconflicts系统接口) |
| [connectPrinter](arkts-basicservices-print-connectprinter-f-sys.md#connectprinter系统接口) |
| [connectPrinter](arkts-basicservices-print-connectprinter-f-sys.md#connectprinter系统接口) |
| [connectPrinterByIdAndPpd](arkts-basicservices-print-connectprinterbyidandppd-f-sys.md#connectprinterbyidandppd系统接口) |
| [connectPrinterByIpAndPpd](arkts-basicservices-print-connectprinterbyipandppd-f-sys.md#connectprinterbyipandppd系统接口) |
| [deletePrinterFromCups](arkts-basicservices-print-deleteprinterfromcups-f-sys.md#deleteprinterfromcups系统接口) |
| [disconnectPrinter](arkts-basicservices-print-disconnectprinter-f-sys.md#disconnectprinter系统接口) |
| [disconnectPrinter](arkts-basicservices-print-disconnectprinter-f-sys.md#disconnectprinter系统接口) |
| [discoverUsbPrinters](arkts-basicservices-print-discoverusbprinters-f-sys.md#discoverusbprinters系统接口) |
| [getPrinterDefaultPreferences](arkts-basicservices-print-getprinterdefaultpreferences-f-sys.md#getprinterdefaultpreferences系统接口) |
| [getPrinterInfoById](arkts-basicservices-print-getprinterinfobyid-f-sys.md#getprinterinfobyid系统接口) |
| [getSharedHosts](arkts-basicservices-print-getsharedhosts-f-sys.md#getsharedhosts系统接口) |
| [notifyPrintService](arkts-basicservices-print-notifyprintservice-f-sys.md#notifyprintservice系统接口) |
| [notifyPrintService](arkts-basicservices-print-notifyprintservice-f-sys.md#notifyprintservice系统接口) |
| [notifyPrintServiceEvent](arkts-basicservices-print-notifyprintserviceevent-f-sys.md#notifyprintserviceevent系统接口) |
| [notifyPrintServiceEvent](arkts-basicservices-print-notifyprintserviceevent-f-sys.md#notifyprintserviceevent系统接口) |
| [notifyPrintServiceSpoolerCloseForCancelled](arkts-basicservices-print-notifyprintservicespoolercloseforcancelled-f-sys.md#notifyprintservicespoolercloseforcancelled系统接口) |
| [notifyPrintServiceSpoolerCloseForCancelled](arkts-basicservices-print-notifyprintservicespoolercloseforcancelled-f-sys.md#notifyprintservicespoolercloseforcancelled系统接口) |
| [notifyPrintServiceSpoolerCloseForStarted](arkts-basicservices-print-notifyprintservicespoolercloseforstarted-f-sys.md#notifyprintservicespoolercloseforstarted系统接口) |
| [notifyPrintServiceSpoolerCloseForStarted](arkts-basicservices-print-notifyprintservicespoolercloseforstarted-f-sys.md#notifyprintservicespoolercloseforstarted系统接口) |
| [offExtInfoChange](arkts-basicservices-print-offextinfochange-f-sys.md#offextinfochange) |
| [offJobStateChange](arkts-basicservices-print-offjobstatechange-f-sys.md#offjobstatechange) |
| [offPrinterInfoQuery](arkts-basicservices-print-offprinterinfoquery-f-sys.md#offprinterinfoquery系统接口) |
| [offPrinterStateChange](arkts-basicservices-print-offprinterstatechange-f-sys.md#offprinterstatechange) |
| [off_extInfoChange](arkts-basicservices-print-offextinfochange-f-sys.md#offextinfochange) |
| [off_jobStateChange](arkts-basicservices-print-offjobstatechange-f-sys.md#offjobstatechange) |
| [off_printerStateChange](arkts-basicservices-print-offprinterstatechange-f-sys.md#offprinterstatechange) |
| [onExtInfoChange](arkts-basicservices-print-onextinfochange-f-sys.md#onextinfochange) |
| [onJobStateChange](arkts-basicservices-print-onjobstatechange-f-sys.md#onjobstatechange) |
| [onPrinterInfoQuery](arkts-basicservices-print-onprinterinfoquery-f-sys.md#onprinterinfoquery系统接口) |
| [onPrinterStateChange](arkts-basicservices-print-onprinterstatechange-f-sys.md#onprinterstatechange) |
| [on_extInfoChange](arkts-basicservices-print-onextinfochange-f-sys.md#onextinfochange) |
| [on_jobStateChange](arkts-basicservices-print-onjobstatechange-f-sys.md#onjobstatechange) |
| [on_printerStateChange](arkts-basicservices-print-onprinterstatechange-f-sys.md#onprinterstatechange) |
| [queryAllActivePrintJobs](arkts-basicservices-print-queryallactiveprintjobs-f-sys.md#queryallactiveprintjobs系统接口) |
| [queryAllPrintJobs](arkts-basicservices-print-queryallprintjobs-f-sys.md#queryallprintjobs系统接口) |
| [queryAllPrintJobs](arkts-basicservices-print-queryallprintjobs-f-sys.md#queryallprintjobs系统接口) |
| [queryAllPrinterExtensionInfos](arkts-basicservices-print-queryallprinterextensioninfos-f-sys.md#queryallprinterextensioninfos系统接口) |
| [queryAllPrinterExtensionInfos](arkts-basicservices-print-queryallprinterextensioninfos-f-sys.md#queryallprinterextensioninfos系统接口) |
| [queryAllPrinterPpds](arkts-basicservices-print-queryallprinterppds-f-sys.md#queryallprinterppds系统接口) |
| [queryPrintJobById](arkts-basicservices-print-queryprintjobbyid-f-sys.md#queryprintjobbyid系统接口) |
| [queryPrintJobById](arkts-basicservices-print-queryprintjobbyid-f-sys.md#queryprintjobbyid系统接口) |
| [queryPrintJobList](arkts-basicservices-print-queryprintjoblist-f-sys.md#queryprintjoblist系统接口) |
| [queryPrintJobList](arkts-basicservices-print-queryprintjoblist-f-sys.md#queryprintjoblist系统接口) |
| [queryPrinterCapability](arkts-basicservices-print-queryprintercapability-f-sys.md#queryprintercapability系统接口) |
| [queryPrinterCapability](arkts-basicservices-print-queryprintercapability-f-sys.md#queryprintercapability系统接口) |
| [queryPrinterCapabilityByUri](arkts-basicservices-print-queryprintercapabilitybyuri-f-sys.md#queryprintercapabilitybyuri系统接口) |
| [queryPrinterInfoByIp](arkts-basicservices-print-queryprinterinfobyip-f-sys.md#queryprinterinfobyip系统接口) |
| [queryRecommendDriversById](arkts-basicservices-print-queryrecommenddriversbyid-f-sys.md#queryrecommenddriversbyid系统接口) |
| [removePrinters](arkts-basicservices-print-removeprinters-f-sys.md#removeprinters系统接口) |
| [removePrinters](arkts-basicservices-print-removeprinters-f-sys.md#removeprinters系统接口) |
| [requestPrintPreview](arkts-basicservices-print-requestprintpreview-f-sys.md#requestprintpreview系统接口) |
| [requestPrintPreview](arkts-basicservices-print-requestprintpreview-f-sys.md#requestprintpreview系统接口) |
| [restartPrintJob](arkts-basicservices-print-restartprintjob-f-sys.md#restartprintjob系统接口) |
| [savePdfFileJob](arkts-basicservices-print-savepdffilejob-f-sys.md#savepdffilejob系统接口) |
| [setDefaultPrinter](arkts-basicservices-print-setdefaultprinter-f-sys.md#setdefaultprinter系统接口) |
| [setPrinterPreferences](arkts-basicservices-print-setprinterpreferences-f-sys.md#setprinterpreferences系统接口) |
| [startDiscoverPrinter](arkts-basicservices-print-startdiscoverprinter-f-sys.md#startdiscoverprinter系统接口) |
| [startDiscoverPrinter](arkts-basicservices-print-startdiscoverprinter-f-sys.md#startdiscoverprinter系统接口) |
| [startGettingPrintFile](arkts-basicservices-print-startgettingprintfile-f-sys.md#startgettingprintfile系统接口) |
| [startPrintJob](arkts-basicservices-print-startprintjob-f-sys.md#startprintjob系统接口) |
| [startPrintJob](arkts-basicservices-print-startprintjob-f-sys.md#startprintjob系统接口) |
| [stopDiscoverPrinter](arkts-basicservices-print-stopdiscoverprinter-f-sys.md#stopdiscoverprinter系统接口) |
| [stopDiscoverPrinter](arkts-basicservices-print-stopdiscoverprinter-f-sys.md#stopdiscoverprinter系统接口) |
| [updateExtensionInfo](arkts-basicservices-print-updateextensioninfo-f-sys.md#updateextensioninfo系统接口) |
| [updateExtensionInfo](arkts-basicservices-print-updateextensioninfo-f-sys.md#updateextensioninfo系统接口) |
| [updatePrintJobState](arkts-basicservices-print-updateprintjobstate-f-sys.md#updateprintjobstate系统接口) |
| [updatePrintJobState](arkts-basicservices-print-updateprintjobstate-f-sys.md#updateprintjobstate系统接口) |
| [updatePrinterInformation](arkts-basicservices-print-updateprinterinformation-f-sys.md#updateprinterinformation系统接口) |
| [updatePrinterState](arkts-basicservices-print-updateprinterstate-f-sys.md#updateprinterstate系统接口) |
| [updatePrinterState](arkts-basicservices-print-updateprinterstate-f-sys.md#updateprinterstate系统接口) |
| [updatePrinters](arkts-basicservices-print-updateprinters-f-sys.md#updateprinters系统接口) |
| [updatePrinters](arkts-basicservices-print-updateprinters-f-sys.md#updateprinters系统接口) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [PpdInfo](arkts-basicservices-print-ppdinfo-i.md) |
| [PrintAttributes](arkts-basicservices-print-printattributes-i.md) |
| [PrintDocumentAdapter](arkts-basicservices-print-printdocumentadapter-i.md) |
| [PrintJobData](arkts-basicservices-print-printjobdata-i.md) |
| [PrintPageRange](arkts-basicservices-print-printpagerange-i.md) |
| [PrintPageSize](arkts-basicservices-print-printpagesize-i.md) |
| [PrintTask](arkts-basicservices-print-printtask-i.md) |
| [PrinterCapabilities](arkts-basicservices-print-printercapabilities-i.md) |
| [PrinterInformation](arkts-basicservices-print-printerinformation-i.md) |
| [PrinterPreferences](arkts-basicservices-print-printerpreferences-i.md) |
| [SharedHost](arkts-basicservices-print-sharedhost-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [PreviewAttribute](arkts-basicservices-print-previewattribute-i-sys.md) |
| [PrintJob](arkts-basicservices-print-printjob-i-sys.md) |
| [PrintMargin](arkts-basicservices-print-printmargin-i-sys.md) |
| [PrintResolution](arkts-basicservices-print-printresolution-i-sys.md) |
| [PrinterCapability](arkts-basicservices-print-printercapability-i-sys.md) |
| [PrinterExtensionInfo](arkts-basicservices-print-printerextensioninfo-i-sys.md) |
| [PrinterInfo](arkts-basicservices-print-printerinfo-i-sys.md) |
| [PrinterRange](arkts-basicservices-print-printerrange-i-sys.md) |
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
| [PrintErrorCode](arkts-basicservices-print-printerrorcode-e.md) |
| [PrintFileCreationState](arkts-basicservices-print-printfilecreationstate-e.md) |
| [PrintJobState](arkts-basicservices-print-printjobstate-e.md) |
| [PrintJobSubState](arkts-basicservices-print-printjobsubstate-e.md) |
| [PrintOrientationMode](arkts-basicservices-print-printorientationmode-e.md) |
| [PrintPageType](arkts-basicservices-print-printpagetype-e.md) |
| [PrintQuality](arkts-basicservices-print-printquality-e.md) |
| [PrinterEvent](arkts-basicservices-print-printerevent-e.md) |
| [PrinterState](arkts-basicservices-print-printerstate-e.md) |
| [PrinterStatus](arkts-basicservices-print-printerstatus-e.md) |
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
| [PrintJobStateChangeCallback](arkts-basicservices-print-printjobstatechangecallback-t-sys.md) |
| [PrinterInfoQueryCallback](arkts-basicservices-print-printerinfoquerycallback-t-sys.md) |
| [PrinterStateChangeCallback](arkts-basicservices-print-printerstatechangecallback-t-sys.md) |
<!--DelEnd-->
