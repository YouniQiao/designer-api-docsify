# @ohos.print

The **print** module provides APIs for basic print operations.

**Since:** 23

<!--Device-unnamed-declare namespace print--><!--Device-unnamed-declare namespace print-End-->

**System capability:** SystemCapability.Print.PrintFramework

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addPrinterToCups](arkts-basicservices-print-addprintertocups-f-sys.md#addprintertocups-system-api) |
| [addPrinters](arkts-basicservices-print-addprinters-f-sys.md#addprinters-system-api) |
| [addPrinters](arkts-basicservices-print-addprinters-f-sys.md#addprinters-system-api) |
| [analyzePrintEvents](arkts-basicservices-print-analyzeprintevents-f-sys.md#analyzeprintevents-system-api) |
| [authPrintJob](arkts-basicservices-print-authprintjob-f-sys.md#authprintjob-system-api) |
| [authSmbDeviceAsRegisteredUser](arkts-basicservices-print-authsmbdeviceasregistereduser-f-sys.md#authsmbdeviceasregistereduser-system-api) |
| [cancelPrintJob](arkts-basicservices-print-cancelprintjob-f-sys.md#cancelprintjob-system-api) |
| [cancelPrintJob](arkts-basicservices-print-cancelprintjob-f-sys.md#cancelprintjob-system-api) |
| [checkPreferencesConflicts](arkts-basicservices-print-checkpreferencesconflicts-f-sys.md#checkpreferencesconflicts-system-api) |
| [connectPrinter](arkts-basicservices-print-connectprinter-f-sys.md#connectprinter-system-api) |
| [connectPrinter](arkts-basicservices-print-connectprinter-f-sys.md#connectprinter-system-api) |
| [connectPrinterByIdAndPpd](arkts-basicservices-print-connectprinterbyidandppd-f-sys.md#connectprinterbyidandppd-system-api) |
| [connectPrinterByIpAndPpd](arkts-basicservices-print-connectprinterbyipandppd-f-sys.md#connectprinterbyipandppd-system-api) |
| [deletePrinterFromCups](arkts-basicservices-print-deleteprinterfromcups-f-sys.md#deleteprinterfromcups-system-api) |
| [disconnectPrinter](arkts-basicservices-print-disconnectprinter-f-sys.md#disconnectprinter-system-api) |
| [disconnectPrinter](arkts-basicservices-print-disconnectprinter-f-sys.md#disconnectprinter-system-api) |
| [discoverUsbPrinters](arkts-basicservices-print-discoverusbprinters-f-sys.md#discoverusbprinters-system-api) |
| [getPrinterDefaultPreferences](arkts-basicservices-print-getprinterdefaultpreferences-f-sys.md#getprinterdefaultpreferences-system-api) |
| [getPrinterInfoById](arkts-basicservices-print-getprinterinfobyid-f-sys.md#getprinterinfobyid-system-api) |
| [getSharedHosts](arkts-basicservices-print-getsharedhosts-f-sys.md#getsharedhosts-system-api) |
| [notifyPrintService](arkts-basicservices-print-notifyprintservice-f-sys.md#notifyprintservice-system-api) |
| [notifyPrintService](arkts-basicservices-print-notifyprintservice-f-sys.md#notifyprintservice-system-api) |
| [notifyPrintServiceEvent](arkts-basicservices-print-notifyprintserviceevent-f-sys.md#notifyprintserviceevent-system-api) |
| [notifyPrintServiceEvent](arkts-basicservices-print-notifyprintserviceevent-f-sys.md#notifyprintserviceevent-system-api) |
| [notifyPrintServiceSpoolerCloseForCancelled](arkts-basicservices-print-notifyprintservicespoolercloseforcancelled-f-sys.md#notifyprintservicespoolercloseforcancelled-system-api) |
| [notifyPrintServiceSpoolerCloseForCancelled](arkts-basicservices-print-notifyprintservicespoolercloseforcancelled-f-sys.md#notifyprintservicespoolercloseforcancelled-system-api) |
| [notifyPrintServiceSpoolerCloseForStarted](arkts-basicservices-print-notifyprintservicespoolercloseforstarted-f-sys.md#notifyprintservicespoolercloseforstarted-system-api) |
| [notifyPrintServiceSpoolerCloseForStarted](arkts-basicservices-print-notifyprintservicespoolercloseforstarted-f-sys.md#notifyprintservicespoolercloseforstarted-system-api) |
| [offExtInfoChange](arkts-basicservices-print-offextinfochange-f-sys.md#offextinfochange) |
| [offJobStateChange](arkts-basicservices-print-offjobstatechange-f-sys.md#offjobstatechange) |
| [offPrinterInfoQuery](arkts-basicservices-print-offprinterinfoquery-f-sys.md#offprinterinfoquery-system-api) |
| [offPrinterStateChange](arkts-basicservices-print-offprinterstatechange-f-sys.md#offprinterstatechange) |
| [off_extInfoChange](arkts-basicservices-print-offextinfochange-f-sys.md#offextinfochange) |
| [off_jobStateChange](arkts-basicservices-print-offjobstatechange-f-sys.md#offjobstatechange) |
| [off_printerStateChange](arkts-basicservices-print-offprinterstatechange-f-sys.md#offprinterstatechange) |
| [onExtInfoChange](arkts-basicservices-print-onextinfochange-f-sys.md#onextinfochange) |
| [onJobStateChange](arkts-basicservices-print-onjobstatechange-f-sys.md#onjobstatechange) |
| [onPrinterInfoQuery](arkts-basicservices-print-onprinterinfoquery-f-sys.md#onprinterinfoquery-system-api) |
| [onPrinterStateChange](arkts-basicservices-print-onprinterstatechange-f-sys.md#onprinterstatechange) |
| [on_extInfoChange](arkts-basicservices-print-onextinfochange-f-sys.md#onextinfochange) |
| [on_jobStateChange](arkts-basicservices-print-onjobstatechange-f-sys.md#onjobstatechange) |
| [on_printerStateChange](arkts-basicservices-print-onprinterstatechange-f-sys.md#onprinterstatechange) |
| [queryAllActivePrintJobs](arkts-basicservices-print-queryallactiveprintjobs-f-sys.md#queryallactiveprintjobs-system-api) |
| [queryAllPrintJobs](arkts-basicservices-print-queryallprintjobs-f-sys.md#queryallprintjobs-system-api) |
| [queryAllPrintJobs](arkts-basicservices-print-queryallprintjobs-f-sys.md#queryallprintjobs-system-api) |
| [queryAllPrinterExtensionInfos](arkts-basicservices-print-queryallprinterextensioninfos-f-sys.md#queryallprinterextensioninfos-system-api) |
| [queryAllPrinterExtensionInfos](arkts-basicservices-print-queryallprinterextensioninfos-f-sys.md#queryallprinterextensioninfos-system-api) |
| [queryAllPrinterPpds](arkts-basicservices-print-queryallprinterppds-f-sys.md#queryallprinterppds-system-api) |
| [queryPrintJobById](arkts-basicservices-print-queryprintjobbyid-f-sys.md#queryprintjobbyid-system-api) |
| [queryPrintJobById](arkts-basicservices-print-queryprintjobbyid-f-sys.md#queryprintjobbyid-system-api) |
| [queryPrintJobList](arkts-basicservices-print-queryprintjoblist-f-sys.md#queryprintjoblist-system-api) |
| [queryPrintJobList](arkts-basicservices-print-queryprintjoblist-f-sys.md#queryprintjoblist-system-api) |
| [queryPrinterCapability](arkts-basicservices-print-queryprintercapability-f-sys.md#queryprintercapability-system-api) |
| [queryPrinterCapability](arkts-basicservices-print-queryprintercapability-f-sys.md#queryprintercapability-system-api) |
| [queryPrinterCapabilityByUri](arkts-basicservices-print-queryprintercapabilitybyuri-f-sys.md#queryprintercapabilitybyuri-system-api) |
| [queryPrinterInfoByIp](arkts-basicservices-print-queryprinterinfobyip-f-sys.md#queryprinterinfobyip-system-api) |
| [queryRecommendDriversById](arkts-basicservices-print-queryrecommenddriversbyid-f-sys.md#queryrecommenddriversbyid-system-api) |
| [removePrinters](arkts-basicservices-print-removeprinters-f-sys.md#removeprinters-system-api) |
| [removePrinters](arkts-basicservices-print-removeprinters-f-sys.md#removeprinters-system-api) |
| [requestPrintPreview](arkts-basicservices-print-requestprintpreview-f-sys.md#requestprintpreview-system-api) |
| [requestPrintPreview](arkts-basicservices-print-requestprintpreview-f-sys.md#requestprintpreview-system-api) |
| [restartPrintJob](arkts-basicservices-print-restartprintjob-f-sys.md#restartprintjob-system-api) |
| [savePdfFileJob](arkts-basicservices-print-savepdffilejob-f-sys.md#savepdffilejob-system-api) |
| [setDefaultPrinter](arkts-basicservices-print-setdefaultprinter-f-sys.md#setdefaultprinter-system-api) |
| [setPrinterPreferences](arkts-basicservices-print-setprinterpreferences-f-sys.md#setprinterpreferences-system-api) |
| [startDiscoverPrinter](arkts-basicservices-print-startdiscoverprinter-f-sys.md#startdiscoverprinter-system-api) |
| [startDiscoverPrinter](arkts-basicservices-print-startdiscoverprinter-f-sys.md#startdiscoverprinter-system-api) |
| [startGettingPrintFile](arkts-basicservices-print-startgettingprintfile-f-sys.md#startgettingprintfile-system-api) |
| [startPrintJob](arkts-basicservices-print-startprintjob-f-sys.md#startprintjob-system-api) |
| [startPrintJob](arkts-basicservices-print-startprintjob-f-sys.md#startprintjob-system-api) |
| [stopDiscoverPrinter](arkts-basicservices-print-stopdiscoverprinter-f-sys.md#stopdiscoverprinter-system-api) |
| [stopDiscoverPrinter](arkts-basicservices-print-stopdiscoverprinter-f-sys.md#stopdiscoverprinter-system-api) |
| [updateExtensionInfo](arkts-basicservices-print-updateextensioninfo-f-sys.md#updateextensioninfo-system-api) |
| [updateExtensionInfo](arkts-basicservices-print-updateextensioninfo-f-sys.md#updateextensioninfo-system-api) |
| [updatePrintJobState](arkts-basicservices-print-updateprintjobstate-f-sys.md#updateprintjobstate-system-api) |
| [updatePrintJobState](arkts-basicservices-print-updateprintjobstate-f-sys.md#updateprintjobstate-system-api) |
| [updatePrinterInformation](arkts-basicservices-print-updateprinterinformation-f-sys.md#updateprinterinformation-system-api) |
| [updatePrinterState](arkts-basicservices-print-updateprinterstate-f-sys.md#updateprinterstate-system-api) |
| [updatePrinterState](arkts-basicservices-print-updateprinterstate-f-sys.md#updateprinterstate-system-api) |
| [updatePrinters](arkts-basicservices-print-updateprinters-f-sys.md#updateprinters-system-api) |
| [updatePrinters](arkts-basicservices-print-updateprinters-f-sys.md#updateprinters-system-api) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PpdInfo](arkts-basicservices-print-ppdinfo-i.md) |
| [PrintAttributes](arkts-basicservices-print-printattributes-i.md) |
| [PrintDocumentAdapter](arkts-basicservices-print-printdocumentadapter-i.md) |
| [PrintJob](arkts-basicservices-print-printjob-i.md) |
| [PrintJobData](arkts-basicservices-print-printjobdata-i.md) |
| [PrintPageRange](arkts-basicservices-print-printpagerange-i.md) |
| [PrintPageSize](arkts-basicservices-print-printpagesize-i.md) |
| [PrintTask](arkts-basicservices-print-printtask-i.md) |
| [PrinterCapabilities](arkts-basicservices-print-printercapabilities-i.md) |
| [PrinterInformation](arkts-basicservices-print-printerinformation-i.md) |
| [PrinterPreferences](arkts-basicservices-print-printerpreferences-i.md) |
| [SharedHost](arkts-basicservices-print-sharedhost-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PrinterChangeCallback](arkts-basicservices-print-printerchangecallback-t.md) |
| [WatermarkCallback](arkts-basicservices-print-watermarkcallback-t.md) |

<!--Del-->
### Types（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ExtInfoChangeCallback](arkts-basicservices-print-extinfochangecallback-t-sys.md) |
| [PrintJobStateChangeCallback](arkts-basicservices-print-printjobstatechangecallback-t-sys.md) |
| [PrinterInfoQueryCallback](arkts-basicservices-print-printerinfoquerycallback-t-sys.md) |
| [PrinterStateChangeCallback](arkts-basicservices-print-printerstatechangecallback-t-sys.md) |
<!--DelEnd-->
