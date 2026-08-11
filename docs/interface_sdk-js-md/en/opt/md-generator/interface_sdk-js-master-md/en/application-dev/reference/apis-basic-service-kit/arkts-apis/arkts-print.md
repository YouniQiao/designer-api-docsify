# @ohos.print

The **print** module provides APIs for basic print operations.

**Since:** 10

<!--Device-unnamed-declare namespace print--><!--Device-unnamed-declare namespace print-End-->

**System capability:** SystemCapability.Print.PrintFramework

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addPrinter](arkts-basicservices-print-addprinter-f.md#addprinter) |
| [addPrinterToDiscovery](arkts-basicservices-print-addprintertodiscovery-f.md#addprintertodiscovery) |
| [connectPrinter](arkts-basicservices-print-connectprinter-f.md#connectprinter) |
| [connectPrinter](arkts-basicservices-print-connectprinter-f.md#connectprinter-1) |
| [getAddedPrinters](arkts-basicservices-print-getaddedprinters-f.md#getaddedprinters) |
| [getPrinterInformationById](arkts-basicservices-print-getprinterinformationbyid-f.md#getprinterinformationbyid) |
| [notifyWatermarkComplete](arkts-basicservices-print-notifywatermarkcomplete-f.md#notifywatermarkcomplete) |
| [off](arkts-basicservices-print-off-f.md#off-3) |
| [on](arkts-basicservices-print-on-f.md#on-3) |
| [print](arkts-basicservices-print-f.md#print) |
| [print](arkts-basicservices-print-f.md#print-1) |
| [print](arkts-basicservices-print-f.md#print-2) |
| [print](arkts-basicservices-print-f.md#print-3) |
| [print](arkts-basicservices-print-f.md#print-4) |
| [registerWatermarkCallback](arkts-basicservices-print-registerwatermarkcallback-f.md#registerwatermarkcallback) |
| [removePrinterFromDiscovery](arkts-basicservices-print-removeprinterfromdiscovery-f.md#removeprinterfromdiscovery) |
| [startDiscoverPrinter](arkts-basicservices-print-startdiscoverprinter-f.md#startdiscoverprinter) |
| [startDiscoverPrinter](arkts-basicservices-print-startdiscoverprinter-f.md#startdiscoverprinter-1) |
| [startPrint](arkts-basicservices-print-startprint-f.md#startprint) |
| [stopDiscoverPrinter](arkts-basicservices-print-stopdiscoverprinter-f.md#stopdiscoverprinter) |
| [stopDiscoverPrinter](arkts-basicservices-print-stopdiscoverprinter-f.md#stopdiscoverprinter-1) |
| [unregisterWatermarkCallback](arkts-basicservices-print-unregisterwatermarkcallback-f.md#unregisterwatermarkcallback) |
| [updatePrintJobState](arkts-basicservices-print-updateprintjobstate-f.md#updateprintjobstate) |
| [updatePrintJobState](arkts-basicservices-print-updateprintjobstate-f.md#updateprintjobstate-1) |
| [updatePrinterInDiscovery](arkts-basicservices-print-updateprinterindiscovery-f.md#updateprinterindiscovery) |
| [updatePrinterInformation](arkts-basicservices-print-updateprinterinformation-f.md#updateprinterinformation) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addPrinterToCups](arkts-basicservices-print-addprintertocups-f-sys.md#addprintertocups) |
| [addPrinters](arkts-basicservices-print-addprinters-f-sys.md#addprinters) |
| [addPrinters](arkts-basicservices-print-addprinters-f-sys.md#addprinters-1) |
| [analyzePrintEvents](arkts-basicservices-print-analyzeprintevents-f-sys.md#analyzeprintevents) |
| [authPrintJob](arkts-basicservices-print-authprintjob-f-sys.md#authprintjob) |
| [authSmbDeviceAsRegisteredUser](arkts-basicservices-print-authsmbdeviceasregistereduser-f-sys.md#authsmbdeviceasregistereduser) |
| [cancelPrintJob](arkts-basicservices-print-cancelprintjob-f-sys.md#cancelprintjob) |
| [cancelPrintJob](arkts-basicservices-print-cancelprintjob-f-sys.md#cancelprintjob-1) |
| [checkPreferencesConflicts](arkts-basicservices-print-checkpreferencesconflicts-f-sys.md#checkpreferencesconflicts) |
| [connectPrinterByIdAndPpd](arkts-basicservices-print-connectprinterbyidandppd-f-sys.md#connectprinterbyidandppd) |
| [connectPrinterByIpAndPpd](arkts-basicservices-print-connectprinterbyipandppd-f-sys.md#connectprinterbyipandppd) |
| [deletePrinterFromCups](arkts-basicservices-print-deleteprinterfromcups-f-sys.md#deleteprinterfromcups) |
| [disconnectPrinter](arkts-basicservices-print-disconnectprinter-f-sys.md#disconnectprinter) |
| [disconnectPrinter](arkts-basicservices-print-disconnectprinter-f-sys.md#disconnectprinter-1) |
| [discoverUsbPrinters](arkts-basicservices-print-discoverusbprinters-f-sys.md#discoverusbprinters) |
| [getPrinterDefaultPreferences](arkts-basicservices-print-getprinterdefaultpreferences-f-sys.md#getprinterdefaultpreferences) |
| [getPrinterInfoById](arkts-basicservices-print-getprinterinfobyid-f-sys.md#getprinterinfobyid) |
| [getSharedHosts](arkts-basicservices-print-getsharedhosts-f-sys.md#getsharedhosts) |
| [notifyPrintService](arkts-basicservices-print-notifyprintservice-f-sys.md#notifyprintservice) |
| [notifyPrintService](arkts-basicservices-print-notifyprintservice-f-sys.md#notifyprintservice-1) |
| [notifyPrintServiceEvent](arkts-basicservices-print-notifyprintserviceevent-f-sys.md#notifyprintserviceevent) |
| [notifyPrintServiceEvent](arkts-basicservices-print-notifyprintserviceevent-f-sys.md#notifyprintserviceevent-1) |
| [off](arkts-basicservices-print-off-f-sys.md#off) |
| [off](arkts-basicservices-print-off-f-sys.md#off-1) |
| [off](arkts-basicservices-print-off-f-sys.md#off-2) |
| [offPrinterInfoQuery](arkts-basicservices-print-offprinterinfoquery-f-sys.md#offprinterinfoquery) |
| [on](arkts-basicservices-print-on-f-sys.md#on) |
| [on](arkts-basicservices-print-on-f-sys.md#on-1) |
| [on](arkts-basicservices-print-on-f-sys.md#on-2) |
| [onPrinterInfoQuery](arkts-basicservices-print-onprinterinfoquery-f-sys.md#onprinterinfoquery) |
| [queryAllActivePrintJobs](arkts-basicservices-print-queryallactiveprintjobs-f-sys.md#queryallactiveprintjobs) |
| [queryAllPrintJobs](arkts-basicservices-print-queryallprintjobs-f-sys.md#queryallprintjobs) |
| [queryAllPrintJobs](arkts-basicservices-print-queryallprintjobs-f-sys.md#queryallprintjobs-1) |
| [queryAllPrinterExtensionInfos](arkts-basicservices-print-queryallprinterextensioninfos-f-sys.md#queryallprinterextensioninfos) |
| [queryAllPrinterExtensionInfos](arkts-basicservices-print-queryallprinterextensioninfos-f-sys.md#queryallprinterextensioninfos-1) |
| [queryAllPrinterPpds](arkts-basicservices-print-queryallprinterppds-f-sys.md#queryallprinterppds) |
| [queryPrintJobById](arkts-basicservices-print-queryprintjobbyid-f-sys.md#queryprintjobbyid) |
| [queryPrintJobById](arkts-basicservices-print-queryprintjobbyid-f-sys.md#queryprintjobbyid-1) |
| [queryPrintJobList](arkts-basicservices-print-queryprintjoblist-f-sys.md#queryprintjoblist) |
| [queryPrintJobList](arkts-basicservices-print-queryprintjoblist-f-sys.md#queryprintjoblist-1) |
| [queryPrinterCapability](arkts-basicservices-print-queryprintercapability-f-sys.md#queryprintercapability) |
| [queryPrinterCapability](arkts-basicservices-print-queryprintercapability-f-sys.md#queryprintercapability-1) |
| [queryPrinterCapabilityByUri](arkts-basicservices-print-queryprintercapabilitybyuri-f-sys.md#queryprintercapabilitybyuri) |
| [queryPrinterInfoByIp](arkts-basicservices-print-queryprinterinfobyip-f-sys.md#queryprinterinfobyip) |
| [queryRecommendDriversById](arkts-basicservices-print-queryrecommenddriversbyid-f-sys.md#queryrecommenddriversbyid) |
| [removePrinters](arkts-basicservices-print-removeprinters-f-sys.md#removeprinters) |
| [removePrinters](arkts-basicservices-print-removeprinters-f-sys.md#removeprinters-1) |
| [requestPrintPreview](arkts-basicservices-print-requestprintpreview-f-sys.md#requestprintpreview) |
| [requestPrintPreview](arkts-basicservices-print-requestprintpreview-f-sys.md#requestprintpreview-1) |
| [restartPrintJob](arkts-basicservices-print-restartprintjob-f-sys.md#restartprintjob) |
| [savePdfFileJob](arkts-basicservices-print-savepdffilejob-f-sys.md#savepdffilejob) |
| [setDefaultPrinter](arkts-basicservices-print-setdefaultprinter-f-sys.md#setdefaultprinter) |
| [setPrinterPreferences](arkts-basicservices-print-setprinterpreferences-f-sys.md#setprinterpreferences) |
| [startGettingPrintFile](arkts-basicservices-print-startgettingprintfile-f-sys.md#startgettingprintfile) |
| [startPrintJob](arkts-basicservices-print-startprintjob-f-sys.md#startprintjob) |
| [startPrintJob](arkts-basicservices-print-startprintjob-f-sys.md#startprintjob-1) |
| [updateExtensionInfo](arkts-basicservices-print-updateextensioninfo-f-sys.md#updateextensioninfo) |
| [updateExtensionInfo](arkts-basicservices-print-updateextensioninfo-f-sys.md#updateextensioninfo-1) |
| [updatePrinterState](arkts-basicservices-print-updateprinterstate-f-sys.md#updateprinterstate) |
| [updatePrinterState](arkts-basicservices-print-updateprinterstate-f-sys.md#updateprinterstate-1) |
| [updatePrinters](arkts-basicservices-print-updateprinters-f-sys.md#updateprinters) |
| [updatePrinters](arkts-basicservices-print-updateprinters-f-sys.md#updateprinters-1) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PpdInfo](arkts-basicservices-print-ppdinfo-i.md) |
| [PreviewAttribute](arkts-basicservices-print-previewattribute-i.md) |
| [PrintAttributes](arkts-basicservices-print-printattributes-i.md) |
| [PrintDocumentAdapter](arkts-basicservices-print-printdocumentadapter-i.md) |
| [PrintJob](arkts-basicservices-print-printjob-i.md) |
| [PrintJobData](arkts-basicservices-print-printjobdata-i.md) |
| [PrintMargin](arkts-basicservices-print-printmargin-i.md) |
| [PrintPageRange](arkts-basicservices-print-printpagerange-i.md) |
| [PrintPageSize](arkts-basicservices-print-printpagesize-i.md) |
| [PrintResolution](arkts-basicservices-print-printresolution-i.md) |
| [PrintTask](arkts-basicservices-print-printtask-i.md) |
| [PrinterCapabilities](arkts-basicservices-print-printercapabilities-i.md) |
| [PrinterCapability](arkts-basicservices-print-printercapability-i.md) |
| [PrinterInfo](arkts-basicservices-print-printerinfo-i.md) |
| [PrinterInformation](arkts-basicservices-print-printerinformation-i.md) |
| [PrinterPreferences](arkts-basicservices-print-printerpreferences-i.md) |
| [PrinterRange](arkts-basicservices-print-printerrange-i.md) |
| [SharedHost](arkts-basicservices-print-sharedhost-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PrinterExtensionInfo](arkts-basicservices-print-printerextensioninfo-i-sys.md) |
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
| [PrinterInfoQueryCallback](arkts-basicservices-print-printerinfoquerycallback-t-sys.md) |
<!--DelEnd-->
