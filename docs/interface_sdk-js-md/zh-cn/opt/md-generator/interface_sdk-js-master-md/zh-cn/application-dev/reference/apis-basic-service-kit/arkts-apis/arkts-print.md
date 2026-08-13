# @ohos.print

该模块为基本打印的操作API，提供调用基础打印功能的接口。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace print--><!--Device-unnamed-declare namespace print-End-->

**系统能力：** SystemCapability.Print.PrintFramework

## 汇总

### 函数

| 名称 |
| --- |
| [addPrinter](arkts-basicservices-print-addprinter-f.md#addPrinter) |
| [addPrinterToDiscovery](arkts-basicservices-print-addprintertodiscovery-f.md#addPrinterToDiscovery) |
| [getAddedPrinters](arkts-basicservices-print-getaddedprinters-f.md#getAddedPrinters) |
| [getPrinterInformationById](arkts-basicservices-print-getprinterinformationbyid-f.md#getPrinterInformationById) |
| [notifyWatermarkComplete](arkts-basicservices-print-notifywatermarkcomplete-f.md#notifyWatermarkComplete) |
| [offPrinterChange](arkts-basicservices-print-offprinterchange-f.md#offPrinterChange) |
| [off_printerChange](arkts-basicservices-print-offprinterchange-f.md) |
| [onPrinterChange](arkts-basicservices-print-onprinterchange-f.md#onPrinterChange) |
| [on_printerChange](arkts-basicservices-print-onprinterchange-f.md) |
| [print](arkts-basicservices-print-f.md#print) |
| [print](arkts-basicservices-print-f.md#print) |
| [print](arkts-basicservices-print-f.md#print) |
| [print](arkts-basicservices-print-f.md#print) |
| [print](arkts-basicservices-print-f.md#print) |
| [registerWatermarkCallback](arkts-basicservices-print-registerwatermarkcallback-f.md#registerWatermarkCallback) |
| [removePrinterFromDiscovery](arkts-basicservices-print-removeprinterfromdiscovery-f.md#removePrinterFromDiscovery) |
| [startPrint](arkts-basicservices-print-startprint-f.md#startPrint) |
| [unregisterWatermarkCallback](arkts-basicservices-print-unregisterwatermarkcallback-f.md#unregisterWatermarkCallback) |
| [updatePrinterInDiscovery](arkts-basicservices-print-updateprinterindiscovery-f.md#updatePrinterInDiscovery) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addPrinterToCups](arkts-basicservices-print-addprintertocups-f-sys.md#addPrinterToCups（系统接口）) |
| [addPrinters](arkts-basicservices-print-addprinters-f-sys.md#addPrinters（系统接口）) |
| [addPrinters](arkts-basicservices-print-addprinters-f-sys.md#addPrinters（系统接口）) |
| [analyzePrintEvents](arkts-basicservices-print-analyzeprintevents-f-sys.md#analyzePrintEvents（系统接口）) |
| [authPrintJob](arkts-basicservices-print-authprintjob-f-sys.md#authPrintJob（系统接口）) |
| [authSmbDeviceAsRegisteredUser](arkts-basicservices-print-authsmbdeviceasregistereduser-f-sys.md#authSmbDeviceAsRegisteredUser（系统接口）) |
| [cancelPrintJob](arkts-basicservices-print-cancelprintjob-f-sys.md#cancelPrintJob（系统接口）) |
| [cancelPrintJob](arkts-basicservices-print-cancelprintjob-f-sys.md#cancelPrintJob（系统接口）) |
| [checkPreferencesConflicts](arkts-basicservices-print-checkpreferencesconflicts-f-sys.md#checkPreferencesConflicts（系统接口）) |
| [connectPrinter](arkts-basicservices-print-connectprinter-f-sys.md#connectPrinter（系统接口）) |
| [connectPrinter](arkts-basicservices-print-connectprinter-f-sys.md#connectPrinter（系统接口）) |
| [connectPrinterByIdAndPpd](arkts-basicservices-print-connectprinterbyidandppd-f-sys.md#connectPrinterByIdAndPpd（系统接口）) |
| [connectPrinterByIpAndPpd](arkts-basicservices-print-connectprinterbyipandppd-f-sys.md#connectPrinterByIpAndPpd（系统接口）) |
| [deletePrinterFromCups](arkts-basicservices-print-deleteprinterfromcups-f-sys.md#deletePrinterFromCups（系统接口）) |
| [disconnectPrinter](arkts-basicservices-print-disconnectprinter-f-sys.md#disconnectPrinter（系统接口）) |
| [disconnectPrinter](arkts-basicservices-print-disconnectprinter-f-sys.md#disconnectPrinter（系统接口）) |
| [discoverUsbPrinters](arkts-basicservices-print-discoverusbprinters-f-sys.md#discoverUsbPrinters（系统接口）) |
| [getPrinterDefaultPreferences](arkts-basicservices-print-getprinterdefaultpreferences-f-sys.md#getPrinterDefaultPreferences（系统接口）) |
| [getPrinterInfoById](arkts-basicservices-print-getprinterinfobyid-f-sys.md#getPrinterInfoById（系统接口）) |
| [getSharedHosts](arkts-basicservices-print-getsharedhosts-f-sys.md#getSharedHosts（系统接口）) |
| [notifyPrintService](arkts-basicservices-print-notifyprintservice-f-sys.md#notifyPrintService（系统接口）) |
| [notifyPrintService](arkts-basicservices-print-notifyprintservice-f-sys.md#notifyPrintService（系统接口）) |
| [notifyPrintServiceEvent](arkts-basicservices-print-notifyprintserviceevent-f-sys.md#notifyPrintServiceEvent（系统接口）) |
| [notifyPrintServiceEvent](arkts-basicservices-print-notifyprintserviceevent-f-sys.md#notifyPrintServiceEvent（系统接口）) |
| [notifyPrintServiceSpoolerCloseForCancelled](arkts-basicservices-print-notifyprintservicespoolercloseforcancelled-f-sys.md#notifyPrintServiceSpoolerCloseForCancelled（系统接口）) |
| [notifyPrintServiceSpoolerCloseForCancelled](arkts-basicservices-print-notifyprintservicespoolercloseforcancelled-f-sys.md#notifyPrintServiceSpoolerCloseForCancelled（系统接口）) |
| [notifyPrintServiceSpoolerCloseForStarted](arkts-basicservices-print-notifyprintservicespoolercloseforstarted-f-sys.md#notifyPrintServiceSpoolerCloseForStarted（系统接口）) |
| [notifyPrintServiceSpoolerCloseForStarted](arkts-basicservices-print-notifyprintservicespoolercloseforstarted-f-sys.md#notifyPrintServiceSpoolerCloseForStarted（系统接口）) |
| [offExtInfoChange](arkts-basicservices-print-offextinfochange-f-sys.md#offExtInfoChange（系统接口）) |
| [offJobStateChange](arkts-basicservices-print-offjobstatechange-f-sys.md#offJobStateChange（系统接口）) |
| [offPrinterInfoQuery](arkts-basicservices-print-offprinterinfoquery-f-sys.md#offPrinterInfoQuery（系统接口）) |
| [offPrinterStateChange](arkts-basicservices-print-offprinterstatechange-f-sys.md#offPrinterStateChange（系统接口）) |
| [off_extInfoChange](arkts-basicservices-print-offextinfochange-f-sys.md) |
| [off_jobStateChange](arkts-basicservices-print-offjobstatechange-f-sys.md) |
| [off_printerStateChange](arkts-basicservices-print-offprinterstatechange-f-sys.md) |
| [onExtInfoChange](arkts-basicservices-print-onextinfochange-f-sys.md#onExtInfoChange（系统接口）) |
| [onJobStateChange](arkts-basicservices-print-onjobstatechange-f-sys.md#onJobStateChange（系统接口）) |
| [onPrinterInfoQuery](arkts-basicservices-print-onprinterinfoquery-f-sys.md#onPrinterInfoQuery（系统接口）) |
| [onPrinterStateChange](arkts-basicservices-print-onprinterstatechange-f-sys.md#onPrinterStateChange（系统接口）) |
| [on_extInfoChange](arkts-basicservices-print-onextinfochange-f-sys.md) |
| [on_jobStateChange](arkts-basicservices-print-onjobstatechange-f-sys.md) |
| [on_printerStateChange](arkts-basicservices-print-onprinterstatechange-f-sys.md) |
| [queryAllActivePrintJobs](arkts-basicservices-print-queryallactiveprintjobs-f-sys.md#queryAllActivePrintJobs（系统接口）) |
| [queryAllPrintJobs](arkts-basicservices-print-queryallprintjobs-f-sys.md#queryAllPrintJobs（系统接口）) |
| [queryAllPrintJobs](arkts-basicservices-print-queryallprintjobs-f-sys.md#queryAllPrintJobs（系统接口）) |
| [queryAllPrinterExtensionInfos](arkts-basicservices-print-queryallprinterextensioninfos-f-sys.md#queryAllPrinterExtensionInfos（系统接口）) |
| [queryAllPrinterExtensionInfos](arkts-basicservices-print-queryallprinterextensioninfos-f-sys.md#queryAllPrinterExtensionInfos（系统接口）) |
| [queryAllPrinterPpds](arkts-basicservices-print-queryallprinterppds-f-sys.md#queryAllPrinterPpds（系统接口）) |
| [queryPrintJobById](arkts-basicservices-print-queryprintjobbyid-f-sys.md#queryPrintJobById（系统接口）) |
| [queryPrintJobById](arkts-basicservices-print-queryprintjobbyid-f-sys.md#queryPrintJobById（系统接口）) |
| [queryPrintJobList](arkts-basicservices-print-queryprintjoblist-f-sys.md#queryPrintJobList（系统接口）) |
| [queryPrintJobList](arkts-basicservices-print-queryprintjoblist-f-sys.md#queryPrintJobList（系统接口）) |
| [queryPrinterCapability](arkts-basicservices-print-queryprintercapability-f-sys.md#queryPrinterCapability（系统接口）) |
| [queryPrinterCapability](arkts-basicservices-print-queryprintercapability-f-sys.md#queryPrinterCapability（系统接口）) |
| [queryPrinterCapabilityByUri](arkts-basicservices-print-queryprintercapabilitybyuri-f-sys.md#queryPrinterCapabilityByUri（系统接口）) |
| [queryPrinterInfoByIp](arkts-basicservices-print-queryprinterinfobyip-f-sys.md#queryPrinterInfoByIp（系统接口）) |
| [queryRecommendDriversById](arkts-basicservices-print-queryrecommenddriversbyid-f-sys.md#queryRecommendDriversById（系统接口）) |
| [removePrinters](arkts-basicservices-print-removeprinters-f-sys.md#removePrinters（系统接口）) |
| [removePrinters](arkts-basicservices-print-removeprinters-f-sys.md#removePrinters（系统接口）) |
| [requestPrintPreview](arkts-basicservices-print-requestprintpreview-f-sys.md#requestPrintPreview（系统接口）) |
| [requestPrintPreview](arkts-basicservices-print-requestprintpreview-f-sys.md#requestPrintPreview（系统接口）) |
| [restartPrintJob](arkts-basicservices-print-restartprintjob-f-sys.md#restartPrintJob（系统接口）) |
| [savePdfFileJob](arkts-basicservices-print-savepdffilejob-f-sys.md#savePdfFileJob（系统接口）) |
| [setDefaultPrinter](arkts-basicservices-print-setdefaultprinter-f-sys.md#setDefaultPrinter（系统接口）) |
| [setPrinterPreferences](arkts-basicservices-print-setprinterpreferences-f-sys.md#setPrinterPreferences（系统接口）) |
| [startDiscoverPrinter](arkts-basicservices-print-startdiscoverprinter-f-sys.md#startDiscoverPrinter（系统接口）) |
| [startDiscoverPrinter](arkts-basicservices-print-startdiscoverprinter-f-sys.md#startDiscoverPrinter（系统接口）) |
| [startGettingPrintFile](arkts-basicservices-print-startgettingprintfile-f-sys.md#startGettingPrintFile（系统接口）) |
| [startPrintJob](arkts-basicservices-print-startprintjob-f-sys.md#startPrintJob（系统接口）) |
| [startPrintJob](arkts-basicservices-print-startprintjob-f-sys.md#startPrintJob（系统接口）) |
| [stopDiscoverPrinter](arkts-basicservices-print-stopdiscoverprinter-f-sys.md#stopDiscoverPrinter（系统接口）) |
| [stopDiscoverPrinter](arkts-basicservices-print-stopdiscoverprinter-f-sys.md#stopDiscoverPrinter（系统接口）) |
| [updateExtensionInfo](arkts-basicservices-print-updateextensioninfo-f-sys.md#updateExtensionInfo（系统接口）) |
| [updateExtensionInfo](arkts-basicservices-print-updateextensioninfo-f-sys.md#updateExtensionInfo（系统接口）) |
| [updatePrintJobState](arkts-basicservices-print-updateprintjobstate-f-sys.md#updatePrintJobState（系统接口）) |
| [updatePrintJobState](arkts-basicservices-print-updateprintjobstate-f-sys.md#updatePrintJobState（系统接口）) |
| [updatePrinterInformation](arkts-basicservices-print-updateprinterinformation-f-sys.md#updatePrinterInformation（系统接口）) |
| [updatePrinterState](arkts-basicservices-print-updateprinterstate-f-sys.md#updatePrinterState（系统接口）) |
| [updatePrinterState](arkts-basicservices-print-updateprinterstate-f-sys.md#updatePrinterState（系统接口）) |
| [updatePrinters](arkts-basicservices-print-updateprinters-f-sys.md#updatePrinters（系统接口）) |
| [updatePrinters](arkts-basicservices-print-updateprinters-f-sys.md#updatePrinters（系统接口）) |
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
