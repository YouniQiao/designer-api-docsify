# @ohos.print

The **print** module provides APIs for basic print operations.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace print--><!--Device-unnamed-declare namespace print-End-->

**System capability:** SystemCapability.Print.PrintFramework

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addPrinterToCups](arkts-basicservices-print-addprintertocups-f-sys.md#addPrinterToCups-(System-API)) |
| [addPrinters](arkts-basicservices-print-addprinters-f-sys.md#addPrinters-(System-API)) |
| [addPrinters](arkts-basicservices-print-addprinters-f-sys.md#addPrinters-(System-API)) |
| [analyzePrintEvents](arkts-basicservices-print-analyzeprintevents-f-sys.md#analyzePrintEvents-(System-API)) |
| [authPrintJob](arkts-basicservices-print-authprintjob-f-sys.md#authPrintJob-(System-API)) |
| [authSmbDeviceAsRegisteredUser](arkts-basicservices-print-authsmbdeviceasregistereduser-f-sys.md#authSmbDeviceAsRegisteredUser-(System-API)) |
| [cancelPrintJob](arkts-basicservices-print-cancelprintjob-f-sys.md#cancelPrintJob-(System-API)) |
| [cancelPrintJob](arkts-basicservices-print-cancelprintjob-f-sys.md#cancelPrintJob-(System-API)) |
| [checkPreferencesConflicts](arkts-basicservices-print-checkpreferencesconflicts-f-sys.md#checkPreferencesConflicts-(System-API)) |
| [connectPrinter](arkts-basicservices-print-connectprinter-f-sys.md#connectPrinter-(System-API)) |
| [connectPrinter](arkts-basicservices-print-connectprinter-f-sys.md#connectPrinter-(System-API)) |
| [connectPrinterByIdAndPpd](arkts-basicservices-print-connectprinterbyidandppd-f-sys.md#connectPrinterByIdAndPpd-(System-API)) |
| [connectPrinterByIpAndPpd](arkts-basicservices-print-connectprinterbyipandppd-f-sys.md#connectPrinterByIpAndPpd-(System-API)) |
| [deletePrinterFromCups](arkts-basicservices-print-deleteprinterfromcups-f-sys.md#deletePrinterFromCups-(System-API)) |
| [disconnectPrinter](arkts-basicservices-print-disconnectprinter-f-sys.md#disconnectPrinter-(System-API)) |
| [disconnectPrinter](arkts-basicservices-print-disconnectprinter-f-sys.md#disconnectPrinter-(System-API)) |
| [discoverUsbPrinters](arkts-basicservices-print-discoverusbprinters-f-sys.md#discoverUsbPrinters-(System-API)) |
| [getPrinterDefaultPreferences](arkts-basicservices-print-getprinterdefaultpreferences-f-sys.md#getPrinterDefaultPreferences-(System-API)) |
| [getPrinterInfoById](arkts-basicservices-print-getprinterinfobyid-f-sys.md#getPrinterInfoById-(System-API)) |
| [getSharedHosts](arkts-basicservices-print-getsharedhosts-f-sys.md#getSharedHosts-(System-API)) |
| [notifyPrintService](arkts-basicservices-print-notifyprintservice-f-sys.md#notifyPrintService-(System-API)) |
| [notifyPrintService](arkts-basicservices-print-notifyprintservice-f-sys.md#notifyPrintService-(System-API)) |
| [notifyPrintServiceEvent](arkts-basicservices-print-notifyprintserviceevent-f-sys.md#notifyPrintServiceEvent-(System-API)) |
| [notifyPrintServiceEvent](arkts-basicservices-print-notifyprintserviceevent-f-sys.md#notifyPrintServiceEvent-(System-API)) |
| [notifyPrintServiceSpoolerCloseForCancelled](arkts-basicservices-print-notifyprintservicespoolercloseforcancelled-f-sys.md#notifyPrintServiceSpoolerCloseForCancelled-(System-API)) |
| [notifyPrintServiceSpoolerCloseForCancelled](arkts-basicservices-print-notifyprintservicespoolercloseforcancelled-f-sys.md#notifyPrintServiceSpoolerCloseForCancelled-(System-API)) |
| [notifyPrintServiceSpoolerCloseForStarted](arkts-basicservices-print-notifyprintservicespoolercloseforstarted-f-sys.md#notifyPrintServiceSpoolerCloseForStarted-(System-API)) |
| [notifyPrintServiceSpoolerCloseForStarted](arkts-basicservices-print-notifyprintservicespoolercloseforstarted-f-sys.md#notifyPrintServiceSpoolerCloseForStarted-(System-API)) |
| [offExtInfoChange](arkts-basicservices-print-offextinfochange-f-sys.md#offExtInfoChange-(System-API)) |
| [offJobStateChange](arkts-basicservices-print-offjobstatechange-f-sys.md#offJobStateChange-(System-API)) |
| [offPrinterInfoQuery](arkts-basicservices-print-offprinterinfoquery-f-sys.md#offPrinterInfoQuery-(System-API)) |
| [offPrinterStateChange](arkts-basicservices-print-offprinterstatechange-f-sys.md#offPrinterStateChange-(System-API)) |
| [off_extInfoChange](arkts-basicservices-print-offextinfochange-f-sys.md) |
| [off_jobStateChange](arkts-basicservices-print-offjobstatechange-f-sys.md) |
| [off_printerStateChange](arkts-basicservices-print-offprinterstatechange-f-sys.md) |
| [onExtInfoChange](arkts-basicservices-print-onextinfochange-f-sys.md#onExtInfoChange-(System-API)) |
| [onJobStateChange](arkts-basicservices-print-onjobstatechange-f-sys.md#onJobStateChange-(System-API)) |
| [onPrinterInfoQuery](arkts-basicservices-print-onprinterinfoquery-f-sys.md#onPrinterInfoQuery-(System-API)) |
| [onPrinterStateChange](arkts-basicservices-print-onprinterstatechange-f-sys.md#onPrinterStateChange-(System-API)) |
| [on_extInfoChange](arkts-basicservices-print-onextinfochange-f-sys.md) |
| [on_jobStateChange](arkts-basicservices-print-onjobstatechange-f-sys.md) |
| [on_printerStateChange](arkts-basicservices-print-onprinterstatechange-f-sys.md) |
| [queryAllActivePrintJobs](arkts-basicservices-print-queryallactiveprintjobs-f-sys.md#queryAllActivePrintJobs-(System-API)) |
| [queryAllPrintJobs](arkts-basicservices-print-queryallprintjobs-f-sys.md#queryAllPrintJobs-(System-API)) |
| [queryAllPrintJobs](arkts-basicservices-print-queryallprintjobs-f-sys.md#queryAllPrintJobs-(System-API)) |
| [queryAllPrinterExtensionInfos](arkts-basicservices-print-queryallprinterextensioninfos-f-sys.md#queryAllPrinterExtensionInfos-(System-API)) |
| [queryAllPrinterExtensionInfos](arkts-basicservices-print-queryallprinterextensioninfos-f-sys.md#queryAllPrinterExtensionInfos-(System-API)) |
| [queryAllPrinterPpds](arkts-basicservices-print-queryallprinterppds-f-sys.md#queryAllPrinterPpds-(System-API)) |
| [queryPrintJobById](arkts-basicservices-print-queryprintjobbyid-f-sys.md#queryPrintJobById-(System-API)) |
| [queryPrintJobById](arkts-basicservices-print-queryprintjobbyid-f-sys.md#queryPrintJobById-(System-API)) |
| [queryPrintJobList](arkts-basicservices-print-queryprintjoblist-f-sys.md#queryPrintJobList-(System-API)) |
| [queryPrintJobList](arkts-basicservices-print-queryprintjoblist-f-sys.md#queryPrintJobList-(System-API)) |
| [queryPrinterCapability](arkts-basicservices-print-queryprintercapability-f-sys.md#queryPrinterCapability-(System-API)) |
| [queryPrinterCapability](arkts-basicservices-print-queryprintercapability-f-sys.md#queryPrinterCapability-(System-API)) |
| [queryPrinterCapabilityByUri](arkts-basicservices-print-queryprintercapabilitybyuri-f-sys.md#queryPrinterCapabilityByUri-(System-API)) |
| [queryPrinterInfoByIp](arkts-basicservices-print-queryprinterinfobyip-f-sys.md#queryPrinterInfoByIp-(System-API)) |
| [queryRecommendDriversById](arkts-basicservices-print-queryrecommenddriversbyid-f-sys.md#queryRecommendDriversById-(System-API)) |
| [removePrinters](arkts-basicservices-print-removeprinters-f-sys.md#removePrinters-(System-API)) |
| [removePrinters](arkts-basicservices-print-removeprinters-f-sys.md#removePrinters-(System-API)) |
| [requestPrintPreview](arkts-basicservices-print-requestprintpreview-f-sys.md#requestPrintPreview-(System-API)) |
| [requestPrintPreview](arkts-basicservices-print-requestprintpreview-f-sys.md#requestPrintPreview-(System-API)) |
| [restartPrintJob](arkts-basicservices-print-restartprintjob-f-sys.md#restartPrintJob-(System-API)) |
| [savePdfFileJob](arkts-basicservices-print-savepdffilejob-f-sys.md#savePdfFileJob-(System-API)) |
| [setDefaultPrinter](arkts-basicservices-print-setdefaultprinter-f-sys.md#setDefaultPrinter-(System-API)) |
| [setPrinterPreferences](arkts-basicservices-print-setprinterpreferences-f-sys.md#setPrinterPreferences-(System-API)) |
| [startDiscoverPrinter](arkts-basicservices-print-startdiscoverprinter-f-sys.md#startDiscoverPrinter-(System-API)) |
| [startDiscoverPrinter](arkts-basicservices-print-startdiscoverprinter-f-sys.md#startDiscoverPrinter-(System-API)) |
| [startGettingPrintFile](arkts-basicservices-print-startgettingprintfile-f-sys.md#startGettingPrintFile-(System-API)) |
| [startPrintJob](arkts-basicservices-print-startprintjob-f-sys.md#startPrintJob-(System-API)) |
| [startPrintJob](arkts-basicservices-print-startprintjob-f-sys.md#startPrintJob-(System-API)) |
| [stopDiscoverPrinter](arkts-basicservices-print-stopdiscoverprinter-f-sys.md#stopDiscoverPrinter-(System-API)) |
| [stopDiscoverPrinter](arkts-basicservices-print-stopdiscoverprinter-f-sys.md#stopDiscoverPrinter-(System-API)) |
| [updateExtensionInfo](arkts-basicservices-print-updateextensioninfo-f-sys.md#updateExtensionInfo-(System-API)) |
| [updateExtensionInfo](arkts-basicservices-print-updateextensioninfo-f-sys.md#updateExtensionInfo-(System-API)) |
| [updatePrintJobState](arkts-basicservices-print-updateprintjobstate-f-sys.md#updatePrintJobState-(System-API)) |
| [updatePrintJobState](arkts-basicservices-print-updateprintjobstate-f-sys.md#updatePrintJobState-(System-API)) |
| [updatePrinterInformation](arkts-basicservices-print-updateprinterinformation-f-sys.md#updatePrinterInformation-(System-API)) |
| [updatePrinterState](arkts-basicservices-print-updateprinterstate-f-sys.md#updatePrinterState-(System-API)) |
| [updatePrinterState](arkts-basicservices-print-updateprinterstate-f-sys.md#updatePrinterState-(System-API)) |
| [updatePrinters](arkts-basicservices-print-updateprinters-f-sys.md#updatePrinters-(System-API)) |
| [updatePrinters](arkts-basicservices-print-updateprinters-f-sys.md#updatePrinters-(System-API)) |
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
