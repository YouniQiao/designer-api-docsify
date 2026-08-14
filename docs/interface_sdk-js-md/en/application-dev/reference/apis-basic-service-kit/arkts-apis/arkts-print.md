# @ohos.print

The **print** module provides APIs for basic print operations.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace print--><!--Device-unnamed-declare namespace print-End-->

**System capability:** SystemCapability.Print.PrintFramework

## Modules to Import

```TypeScript
import { print } from 'print';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [addPrinter](arkts-basicservices-print-addprinter-f.md#addPrinter) | Add a printer to system. |
| [addPrinterToDiscovery](arkts-basicservices-print-addprintertodiscovery-f.md#addPrinterToDiscovery) | Adds a printer to the printer discovery list. This API uses a promise to return the result. |
| [getAddedPrinters](arkts-basicservices-print-getaddedprinters-f.md#getAddedPrinters) | Obtains the list of printers added to the system. This API uses a promise to return the result. |
| [getPrinterInformationById](arkts-basicservices-print-getprinterinformationbyid-f.md#getPrinterInformationById) | Obtains printer information based on the printer ID. This API uses a promise to return the result. |
| [notifyWatermarkComplete](arkts-basicservices-print-notifywatermarkcomplete-f.md#notifyWatermarkComplete) | Notify watermark complete. |
| [offPrinterChange](arkts-basicservices-print-offprinterchange-f.md#offPrinterChange) | Unregister event callback for the change of printer. |
| off_printerChange | Unregisters the listener for printer state change events. This API uses a callback to return the result. |
| [onPrinterChange](arkts-basicservices-print-onprinterchange-f.md#onPrinterChange) | Register event callback for the change of printer. |
| on_printerChange | Registers a listener for the printer change events. This API uses a callback to return the result. |
| [print](arkts-basicservices-print-f.md#print) | Prints files. This API uses an asynchronous callback to return the result. To start the system print preview page, call the [print](arkts-basicservices-print-f.md#print) API and pass in context. |
| [print](arkts-basicservices-print-f.md#print) | Prints files. This API uses a promise to return the result. To start the system print preview page, call the [print](arkts-basicservices-print-f.md#print) API and pass in context. |
| [print](arkts-basicservices-print-f.md#print) | Prints files. This API uses an asynchronous callback to return the result. |
| [print](arkts-basicservices-print-f.md#print) | Prints files. This API uses a promise to return the result. |
| [print](arkts-basicservices-print-f.md#print) | Prints a file. This API uses a promise to return the result. |
| [registerWatermarkCallback](arkts-basicservices-print-registerwatermarkcallback-f.md#registerWatermarkCallback) | Register to listen for watermark handling. |
| [removePrinterFromDiscovery](arkts-basicservices-print-removeprinterfromdiscovery-f.md#removePrinterFromDiscovery) | Removes a printer from the printer discovery list. This API uses a promise to return the result. |
| [startPrint](arkts-basicservices-print-startprint-f.md#startPrint) | Prints a file or binary data. This API uses a promise to return the result. |
| [unregisterWatermarkCallback](arkts-basicservices-print-unregisterwatermarkcallback-f.md#unregisterWatermarkCallback) | Unregister to listen for watermark handling. |
| [updatePrinterInDiscovery](arkts-basicservices-print-updateprinterindiscovery-f.md#updatePrinterInDiscovery) | Updates the printer capabilities to the printer discovery list. This API uses a promise to return the result. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [addPrinterToCups](arkts-basicservices-print-addprintertocups-f-sys.md#addPrinterToCups) | Add a printer to cups. |
| [addPrinters](arkts-basicservices-print-addprinters-f-sys.md#addPrinters) | Adds printers. This API uses an asynchronous callback to return the result. |
| [addPrinters](arkts-basicservices-print-addprinters-f-sys.md#addPrinters-(System-API)) | Adds printers. This API uses a promise to return the result. |
| [analyzePrintEvents](arkts-basicservices-print-analyzeprintevents-f-sys.md#analyzePrintEvents) | Analyze print events. |
| [authPrintJob](arkts-basicservices-print-authprintjob-f-sys.md#authPrintJob) | Authenticate a print job. |
| [authSmbDeviceAsRegisteredUser](arkts-basicservices-print-authsmbdeviceasregistereduser-f-sys.md#authSmbDeviceAsRegisteredUser) | Authenticate SMB device as registered user and get available printers. |
| [cancelPrintJob](arkts-basicservices-print-cancelprintjob-f-sys.md#cancelPrintJob) | Cancels the specified print job, which is on the print queue of the printer. This API uses an asynchronous callback to return the result. |
| [cancelPrintJob](arkts-basicservices-print-cancelprintjob-f-sys.md#cancelPrintJob-(System-API)) | Cancels the specified print job, which is on the print queue of the printer. This API uses a promise to return the result. |
| [checkPreferencesConflicts](arkts-basicservices-print-checkpreferencesconflicts-f-sys.md#checkPreferencesConflicts) | Check preferences conflicts. |
| [connectPrinter](arkts-basicservices-print-connectprinter-f-sys.md#connectPrinter) | Connects to a printer by printer ID. This API uses an asynchronous callback to return the result. |
| [connectPrinter](arkts-basicservices-print-connectprinter-f-sys.md#connectPrinter-(System-API)) | Connects to a printer by printer ID. This API uses a promise to return the result. |
| [connectPrinterByIdAndPpd](arkts-basicservices-print-connectprinterbyidandppd-f-sys.md#connectPrinterByIdAndPpd) | Query recommend printer drivers by printer ID. |
| [connectPrinterByIpAndPpd](arkts-basicservices-print-connectprinterbyipandppd-f-sys.md#connectPrinterByIpAndPpd) | Connect a printer by the printer IP and ppd. |
| [deletePrinterFromCups](arkts-basicservices-print-deleteprinterfromcups-f-sys.md#deletePrinterFromCups) | Delete a printer from cups. |
| [disconnectPrinter](arkts-basicservices-print-disconnectprinter-f-sys.md#disconnectPrinter) | Disconnects from the specified printer. This API uses an asynchronous callback to return the result. |
| [disconnectPrinter](arkts-basicservices-print-disconnectprinter-f-sys.md#disconnectPrinter-(System-API)) | Disconnects from the specified printer. This API uses a promise to return the result. |
| [discoverUsbPrinters](arkts-basicservices-print-discoverusbprinters-f-sys.md#discoverUsbPrinters) | Discovers USB printers. This API uses a promise to return the result. |
| [getPrinterDefaultPreferences](arkts-basicservices-print-getprinterdefaultpreferences-f-sys.md#getPrinterDefaultPreferences) | Get default preferences by printer ID. |
| [getPrinterInfoById](arkts-basicservices-print-getprinterinfobyid-f-sys.md#getPrinterInfoById) | Obtains printer information based on the printer ID. This API uses a promise to return the result. |
| [getSharedHosts](arkts-basicservices-print-getsharedhosts-f-sys.md#getSharedHosts) | Get all available shared hosts. |
| [notifyPrintService](arkts-basicservices-print-notifyprintservice-f-sys.md#notifyPrintService) | Notifies the print service of the spooler shutdown information. This API uses an asynchronous callback to return the result. |
| [notifyPrintService](arkts-basicservices-print-notifyprintservice-f-sys.md#notifyPrintService-(System-API)) | Notifies the print service of the spooler shutdown information. This API uses a promise to return the result. |
| [notifyPrintServiceEvent](arkts-basicservices-print-notifyprintserviceevent-f-sys.md#notifyPrintServiceEvent) | Notifies the print service of the print application events. This API uses a promise to return the result. |
| [notifyPrintServiceEvent](arkts-basicservices-print-notifyprintserviceevent-f-sys.md#notifyPrintServiceEvent-(System-API)) | Notifies the print service of the print application events. This API uses a promise to return the result. |
| [notifyPrintServiceSpoolerCloseForCancelled](arkts-basicservices-print-notifyprintservicespoolercloseforcancelled-f-sys.md#notifyPrintServiceSpoolerCloseForCancelled) | Notify print service the information. |
| [notifyPrintServiceSpoolerCloseForCancelled](arkts-basicservices-print-notifyprintservicespoolercloseforcancelled-f-sys.md#notifyPrintServiceSpoolerCloseForCancelled-(System-API)) | Notify print service the information. |
| [notifyPrintServiceSpoolerCloseForStarted](arkts-basicservices-print-notifyprintservicespoolercloseforstarted-f-sys.md#notifyPrintServiceSpoolerCloseForStarted) | Notify print service the information. |
| [notifyPrintServiceSpoolerCloseForStarted](arkts-basicservices-print-notifyprintservicespoolercloseforstarted-f-sys.md#notifyPrintServiceSpoolerCloseForStarted-(System-API)) | Notify print service the information. |
| [offExtInfoChange](arkts-basicservices-print-offextinfochange-f-sys.md#offExtInfoChange) | Unregister event callback for the information change of print extension. |
| [offJobStateChange](arkts-basicservices-print-offjobstatechange-f-sys.md#offJobStateChange) | Unregister event callback for the state change of print job. |
| [offPrinterInfoQuery](arkts-basicservices-print-offprinterinfoquery-f-sys.md#offPrinterInfoQuery) | Unregister event callback for the printer info queried. |
| [offPrinterStateChange](arkts-basicservices-print-offprinterstatechange-f-sys.md#offPrinterStateChange) | Unregister event callback for the state change of printer. |
| off_extInfoChange | Unregisters the listener for printer extension information change events. This API uses a callback to return the result. |
| off_jobStateChange | Unregisters the listener for print job state change events. This API uses a callback to return the result. |
| off_printerStateChange | Unregisters the listener for printer state change events. This API uses a callback to return the result. |
| [onExtInfoChange](arkts-basicservices-print-onextinfochange-f-sys.md#onExtInfoChange) | Register event callback for the information change of print extension. |
| [onJobStateChange](arkts-basicservices-print-onjobstatechange-f-sys.md#onJobStateChange) | Register event callback for the state change of print job. |
| [onPrinterInfoQuery](arkts-basicservices-print-onprinterinfoquery-f-sys.md#onPrinterInfoQuery) | Register event callback for the printer info queried. |
| [onPrinterStateChange](arkts-basicservices-print-onprinterstatechange-f-sys.md#onPrinterStateChange) | Register event callback for the state change of printer. |
| on_extInfoChange | Registers a listener for printer extension information change events. This API uses a callback to return the result. |
| on_jobStateChange | Registers a listener for print job state change events. This API uses a callback to return the result. |
| on_printerStateChange | Registers a listener for printer state change events. This API uses a callback to return the result. |
| [queryAllActivePrintJobs](arkts-basicservices-print-queryallactiveprintjobs-f-sys.md#queryAllActivePrintJobs) | Queries all active print jobs. This API uses a promise to return the result. |
| [queryAllPrintJobs](arkts-basicservices-print-queryallprintjobs-f-sys.md#queryAllPrintJobs) | Queries all print jobs. This API uses an asynchronous callback to return the result. |
| [queryAllPrintJobs](arkts-basicservices-print-queryallprintjobs-f-sys.md#queryAllPrintJobs-(System-API)) | Queries all print jobs. This API uses a promise to return the result. |
| [queryAllPrinterExtensionInfos](arkts-basicservices-print-queryallprinterextensioninfos-f-sys.md#queryAllPrinterExtensionInfos) | Obtains the information of all installed printer extensions. This API uses an asynchronous callback to return the result. |
| [queryAllPrinterExtensionInfos](arkts-basicservices-print-queryallprinterextensioninfos-f-sys.md#queryAllPrinterExtensionInfos-(System-API)) | Obtains the information of all installed printer extensions. This API uses a promise to return the result. |
| [queryAllPrinterPpds](arkts-basicservices-print-queryallprinterppds-f-sys.md#queryAllPrinterPpds) | Query all printer ppds. |
| [queryPrintJobById](arkts-basicservices-print-queryprintjobbyid-f-sys.md#queryPrintJobById) | Queries a print job by ID. This API uses an asynchronous callback to return the result. |
| [queryPrintJobById](arkts-basicservices-print-queryprintjobbyid-f-sys.md#queryPrintJobById-(System-API)) | Queries a print job by ID. This API uses a promise to return the result. |
| [queryPrintJobList](arkts-basicservices-print-queryprintjoblist-f-sys.md#queryPrintJobList) | Queries all print jobs. This API uses an asynchronous callback to return the result. |
| [queryPrintJobList](arkts-basicservices-print-queryprintjoblist-f-sys.md#queryPrintJobList-(System-API)) | Queries all print jobs. This API uses a promise to return the result. |
| [queryPrinterCapability](arkts-basicservices-print-queryprintercapability-f-sys.md#queryPrinterCapability) | Queries the printer capability. This API uses an asynchronous callback to return the result. |
| [queryPrinterCapability](arkts-basicservices-print-queryprintercapability-f-sys.md#queryPrinterCapability-(System-API)) | Queries the printer capability. This API uses a promise to return the result. |
| [queryPrinterCapabilityByUri](arkts-basicservices-print-queryprintercapabilitybyuri-f-sys.md#queryPrinterCapabilityByUri) | Query printer capabilityies by printer uri. |
| [queryPrinterInfoByIp](arkts-basicservices-print-queryprinterinfobyip-f-sys.md#queryPrinterInfoByIp) | Query printer info by ip. |
| [queryRecommendDriversById](arkts-basicservices-print-queryrecommenddriversbyid-f-sys.md#queryRecommendDriversById) | Query recommend printer drivers by printer ID. |
| [removePrinters](arkts-basicservices-print-removeprinters-f-sys.md#removePrinters) | Removes printers. This API uses an asynchronous callback to return the result. |
| [removePrinters](arkts-basicservices-print-removeprinters-f-sys.md#removePrinters-(System-API)) | Removes printers. This API uses a promise to return the result. |
| [requestPrintPreview](arkts-basicservices-print-requestprintpreview-f-sys.md#requestPrintPreview) | Requests print preview data. This API uses a callback to return the result. |
| [requestPrintPreview](arkts-basicservices-print-requestprintpreview-f-sys.md#requestPrintPreview-(System-API)) | Requests print preview data. This API uses a promise to return the result. |
| [restartPrintJob](arkts-basicservices-print-restartprintjob-f-sys.md#restartPrintJob) | Restarts a print job that has been finished before. This API uses a promise to return the result. |
| [savePdfFileJob](arkts-basicservices-print-savepdffilejob-f-sys.md#savePdfFileJob) | Save the pdf file for a print job. |
| [setDefaultPrinter](arkts-basicservices-print-setdefaultprinter-f-sys.md#setDefaultPrinter) | Sets the default printer. This API uses a promise to return the result. |
| [setPrinterPreferences](arkts-basicservices-print-setprinterpreferences-f-sys.md#setPrinterPreferences) | Sets the printer preferences. This API uses a promise to return the result. |
| [startDiscoverPrinter](arkts-basicservices-print-startdiscoverprinter-f-sys.md#startDiscoverPrinter) | Discovers printers by specifying the extension list. The discovered printers contain the specified print extension abilities. If an empty extension list is specified, all extension abilities are loaded. This API uses an asynchronous callback to return the result. |
| [startDiscoverPrinter](arkts-basicservices-print-startdiscoverprinter-f-sys.md#startDiscoverPrinter-(System-API)) | Discovers printers by specifying the extension list. The discovered printers contain the specified print extension abilities. If an empty extension list is specified, all extension abilities are loaded. This API uses a promise to return the result. |
| [startGettingPrintFile](arkts-basicservices-print-startgettingprintfile-f-sys.md#startGettingPrintFile) | Starts to obtain the print file. This API uses an asynchronous callback to return the result. |
| [startPrintJob](arkts-basicservices-print-startprintjob-f-sys.md#startPrintJob) | Starts the specified print job. This API uses an asynchronous callback to return the result. |
| [startPrintJob](arkts-basicservices-print-startprintjob-f-sys.md#startPrintJob-(System-API)) | Starts the specified print job. This API uses a promise to return the result. |
| [stopDiscoverPrinter](arkts-basicservices-print-stopdiscoverprinter-f-sys.md#stopDiscoverPrinter) | Stops discovering printers. This API uses an asynchronous callback to return the result. |
| [stopDiscoverPrinter](arkts-basicservices-print-stopdiscoverprinter-f-sys.md#stopDiscoverPrinter-(System-API)) | Stops discovering printers. This API uses a promise to return the result. |
| [updateExtensionInfo](arkts-basicservices-print-updateextensioninfo-f-sys.md#updateExtensionInfo) | Updates the printer extension information. This API uses an asynchronous callback to return the result. |
| [updateExtensionInfo](arkts-basicservices-print-updateextensioninfo-f-sys.md#updateExtensionInfo-(System-API)) | Updates the printer extension information. This API uses a promise to return the result. |
| [updatePrintJobState](arkts-basicservices-print-updateprintjobstate-f-sys.md#updatePrintJobState) | Updates the print job state. This API uses an asynchronous callback to return the result. |
| [updatePrintJobState](arkts-basicservices-print-updateprintjobstate-f-sys.md#updatePrintJobState-(System-API)) | Updates the print job state. This API uses a promise to return the result. |
| [updatePrinterInformation](arkts-basicservices-print-updateprinterinformation-f-sys.md#updatePrinterInformation) | Updates the information of a printer in the system. This API uses a promise to return the result. Currently, only the **alias** and **options** fields of [PrinterInformation](arkts-basicservices-print-printerinformation-i.md#PrinterInformation) can be updated. |
| [updatePrinterState](arkts-basicservices-print-updateprinterstate-f-sys.md#updatePrinterState) | Updates the printer state. This API uses an asynchronous callback to return the result. |
| [updatePrinterState](arkts-basicservices-print-updateprinterstate-f-sys.md#updatePrinterState-(System-API)) | Updates the printer state. This API uses a promise to return the result. |
| [updatePrinters](arkts-basicservices-print-updateprinters-f-sys.md#updatePrinters) | Updates information about the specified printers. This API uses an asynchronous callback to return the result. |
| [updatePrinters](arkts-basicservices-print-updateprinters-f-sys.md#updatePrinters-(System-API)) | Updates information about the specified printers. This API uses a promise to return the result. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [PpdInfo](arkts-basicservices-print-ppdinfo-i.md) | defines ppd info. |
| [PrintAttributes](arkts-basicservices-print-printattributes-i.md) | Defines the print attributes. |
| [PrintDocumentAdapter](arkts-basicservices-print-printdocumentadapter-i.md) | Provides information about the document to print. This API must be implemented by a third-party application. |
| [PrintJob](arkts-basicservices-print-printjob-i.md) | Defines a print job. |
| [PrintJobData](arkts-basicservices-print-printjobdata-i.md) | Defines a print job. |
| [PrintPageRange](arkts-basicservices-print-printpagerange-i.md) | Defines the print range. |
| [PrintPageSize](arkts-basicservices-print-printpagesize-i.md) | Defines the size of the printed page. |
| [PrintTask](arkts-basicservices-print-printtask-i.md) | Implements event listeners for print jobs. |
| [PrinterCapabilities](arkts-basicservices-print-printercapabilities-i.md) | Defines the printer capabilities. |
| [PrinterInformation](arkts-basicservices-print-printerinformation-i.md) | Defines the printer information. |
| [PrinterPreferences](arkts-basicservices-print-printerpreferences-i.md) | Defines the printer preferences. |
| [SharedHost](arkts-basicservices-print-sharedhost-i.md) | Interface defining shared device information |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [PreviewAttribute](arkts-basicservices-print-previewattribute-i-sys.md) | Defines the print preview attributes. |
| [PrintJob](arkts-basicservices-print-printjob-i-sys.md) | Defines a print job. |
| [PrintMargin](arkts-basicservices-print-printmargin-i-sys.md) | Defines the page margins for printing. |
| [PrintResolution](arkts-basicservices-print-printresolution-i-sys.md) | Defines the resolution for printing. |
| [PrinterCapability](arkts-basicservices-print-printercapability-i-sys.md) | Defines the printer capabilities. |
| [PrinterExtensionInfo](arkts-basicservices-print-printerextensioninfo-i-sys.md) | Provides the printer extension information. |
| [PrinterInfo](arkts-basicservices-print-printerinfo-i-sys.md) | Provides the printer information. |
| [PrinterRange](arkts-basicservices-print-printerrange-i-sys.md) | Defines the print range. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [ApplicationEvent](arkts-basicservices-print-applicationevent-e.md) | Enumerates print application events. |
| [DefaultPrinterType](arkts-basicservices-print-defaultprintertype-e.md) | Enumerates default printer types. |
| [DocFlavor](arkts-basicservices-print-docflavor-e.md) | Enumerates the data source types for printing. |
| [PrintColorMode](arkts-basicservices-print-printcolormode-e.md) | Enumerates the color modes. |
| [PrintDirectionMode](arkts-basicservices-print-printdirectionmode-e.md) | Enumerates the print direction modes. |
| [PrintDocumentAdapterState](arkts-basicservices-print-printdocumentadapterstate-e.md) | Enumerates the print job states. |
| [PrintDocumentFormat](arkts-basicservices-print-printdocumentformat-e.md) | Enumerates the data formats. |
| [PrintDuplexMode](arkts-basicservices-print-printduplexmode-e.md) | Enumerates the duplex modes. |
| [PrintErrorCode](arkts-basicservices-print-printerrorcode-e.md) | Enumerates the print error codes. |
| [PrintFileCreationState](arkts-basicservices-print-printfilecreationstate-e.md) | Enumerates the print file creation status. |
| [PrintJobState](arkts-basicservices-print-printjobstate-e.md) | Enumerates the print job states. |
| [PrintJobSubState](arkts-basicservices-print-printjobsubstate-e.md) | Enumerates the print job substates. |
| [PrintOrientationMode](arkts-basicservices-print-printorientationmode-e.md) | Enumerates the print directions. |
| [PrintPageType](arkts-basicservices-print-printpagetype-e.md) | Enumerates the print page types. |
| [PrintQuality](arkts-basicservices-print-printquality-e.md) | Enumerates the print qualities. |
| [PrinterEvent](arkts-basicservices-print-printerevent-e.md) | Enumerates printer-related events. |
| [PrinterState](arkts-basicservices-print-printerstate-e.md) | Enumerates the printer states. |
| [PrinterStatus](arkts-basicservices-print-printerstatus-e.md) | Enumerates the printer states. |
| [WatermarkHandleResult](arkts-basicservices-print-watermarkhandleresult-e.md) | Watermark handling result. |

### Types

| Name | Description |
| --- | --- |
| [PrinterChangeCallback](arkts-basicservices-print-printerchangecallback-t.md) | Defines a callback that takes the printer event and printer information as parameters. |
| [WatermarkCallback](arkts-basicservices-print-watermarkcallback-t.md) | Defines the callback type used in registering to listen for watermark handling. The value of jobId indicates the print job ID. The value of fd indicates the fd. |

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [ExtInfoChangeCallback](arkts-basicservices-print-extinfochangecallback-t-sys.md) | Defines the callback type used in registering to listen for extension change. The value of extensionId indicates the print extension id. The value of info indicates the connect info. |
| [PrintJobStateChangeCallback](arkts-basicservices-print-printjobstatechangecallback-t-sys.md) | Defines the callback type used in registering to listen for PrintJobState. The value of state indicates the state of print job. The value of job indicates the latest print job info. |
| [PrinterInfoQueryCallback](arkts-basicservices-print-printerinfoquerycallback-t-sys.md) | Defines the callback type used in registering to listen for printerInfoQuery event. The value of printerInfo indicates the printer info. The value of ppdInfo indicates all the printer ppd info. |
| [PrinterStateChangeCallback](arkts-basicservices-print-printerstatechangecallback-t-sys.md) | Defines the callback type used in registering to listen for PrinterState. The value of state indicates the state of printer. The value of info indicates the latest printer info. |
<!--DelEnd-->

