# SystemPasteboard

```TypeScript
interface SystemPasteboard
```

Provides **SystemPasteboard** APIs.

Before calling any **SystemPasteboard** API, you must obtain a **SystemPasteboard** object using [getSystemPasteboard](arkts-basicservices-pasteboard-getsystempasteboard-f.md).

**Since:** 6

<!--Device-pasteboard-interface SystemPasteboard--><!--Device-pasteboard-interface SystemPasteboard-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## Modules to Import

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit';
```

## clearData

```TypeScript
clearData(callback: AsyncCallback<void>): void
```

Clears the system pasteboard. This API uses an asynchronous callback to return the result. After this API is called, the system deletes all data from the pasteboard and triggers the registered listener callback **'update'**. After the pasteboard is cleared, it will contain no data, and **false** will be returned for **hasData**. This API can be used to clear the pasteboard asynchronously without blocking the main thread, such as the interaction process that requires the UI response. Unlike the synchronous API [clearDataSync](#cleardatasync), this API does not block the UI thread and is more suitable for UI interactions.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-clearData(callback: AsyncCallback<void>): void--><!--Device-SystemPasteboard-clearData(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types. |

**Examples**

```TypeScript
// Obtain the SystemPasteboard object.
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
// Clear the system pasteboard content.
systemPasteboard.clearData((err, data) => {
    if (err) {
        console.error(`Failed to clear the pasteboard. errorCode: ${err.code}, errorMessage: ${err.message}.`);
        return;
    }
    console.info('Succeeded in clearing the pasteboard.');
});
```

## clearData

```TypeScript
clearData(): Promise<void>
```

Clears the system pasteboard. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-clearData(): Promise<void>--><!--Device-SystemPasteboard-clearData(): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.clearData().then((data: void) => {
    console.info('Succeeded in clearing the pasteboard.');
}).catch((err: BusinessError) => {
    console.error(`Failed to clear the pasteboard. errorCode: ${err.code}, errorMessage: ${err.message}.`);
});
```

## clearDataSync

```TypeScript
clearDataSync(): void
```

Clears data in the system pasteboard. This API returns the result synchronously. This API is used to clear the pasteboard data synchronously in a key service process or confirm the clearing result immediately.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-clearDataSync(): void--><!--Device-SystemPasteboard-clearDataSync(): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12900005](../errorcode-pasteboard.md#12900005-request-timeout) | Excessive processing time for internal data. |

**Examples**

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    systemPasteboard.clearDataSync();
    console.info('Succeeded in clearing the pasteboard.');
} catch (err) {
    console.error(`Failed to clear the pasteboard. errorCode: ${err.code}, errorMessage: ${err.message}.`);
};
```

## detectPatterns

```TypeScript
detectPatterns(patterns: Array<Pattern>): Promise<Array<Pattern>>
```

Detects [patterns](../../../reference/apis-basic-services-kit/js-apis-pasteboard.md#pattern13) on the local pasteboard. This API uses a promise to return the result. The local pasteboard data refers to the pasteboard data on the current device, excluding the pasteboard data transferred across devices. This API can be used to check whether the pasteboard contains specific types of data (such as URLs, email addresses, and phone numbers) before pasting, so that the app can perform corresponding processing or provide intelligent prompts.

**Since:** 13

<!--Device-SystemPasteboard-detectPatterns(patterns: Array<Pattern>): Promise<Array<Pattern>>--><!--Device-SystemPasteboard-detectPatterns(patterns: Array<Pattern>): Promise<Array<Pattern>>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| patterns | Array&lt;[Pattern](arkts-basicservices-pasteboard-pattern-e.md)&gt; | Yes | Patterns to be detected in the pasteboard, which is used to check whether the pasteboard data complies with a specific format. The options are **URL**, **NUMBER**, and **EMAIL_ADDRESS**. The number of elements in the array is not limited, and the element value must be an enumerated value of **Pattern**. If an invalid value is passed, error code 401 is returned. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[Pattern](arkts-basicservices-pasteboard-pattern-e.md)&gt;&gt; | Promise used to return the detected pattern. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameter types;         3. Parameter verification failed. |

**Examples**

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit'

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let patterns: Array<pasteboard.Pattern> = [pasteboard.Pattern.URL, pasteboard.Pattern.EMAIL_ADDRESS];

systemPasteboard.detectPatterns(patterns).then((data: Array<pasteboard.Pattern>) => {
    if (patterns.sort().join('') == data.sort().join('')) {
      console.info('All needed patterns detected, next get data');
      try {
        let result: pasteboard.PasteData = systemPasteboard.getDataSync();
        console.info('Succeeded in getting PasteData.');
      } catch (err) {
        console.error(`Failed to get PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
      };
    } else {
      console.info("Not all needed patterns detected, no need to get data.");
    }
});
```

## getChangeCount

```TypeScript
getChangeCount(): number
```

Obtains the number of pasteboard content changes.

Returns the number of pasteboard content changes if this API is called successfully; returns **0** otherwise.

Even though the pasteboard data expires, or the data becomes empty because of the called [clearDataSync](#cleardatasync) API, the number of data changes remains.

When the system is restarted, or the pasteboard service is restarted due to an exception, the number of pasteboard data changes counts from 0. If the same data is copied repeatedly, multiple changes will be recorded.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SystemPasteboard-getChangeCount(): long--><!--Device-SystemPasteboard-getChangeCount(): long-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| number | The number of pasteboard content changes obtained. |

**Examples**

```TypeScript
import { BusinessError, pasteboard } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result : number = systemPasteboard.getChangeCount();
    console.info(`Succeeded in getting the ChangeCount. Result: ${result}`);
} catch (err) {
    console.error(`Failed to get the ChangeCount. errorCode: ${err.code}, errorMessage: ${err.message}.`);
};
```

## getData

```TypeScript
getData(callback: AsyncCallback<PasteData>): void
```

Obtains a **PasteData** object from the pasteboard. This API uses an asynchronous callback to return the result. After this API is called, the system reads the current content from the pasteboard service and returns a **PasteData** object using a callback. After the data is read successfully, the app can obtain the specific data content (such as text, HTML, and URI) using the **PasteData** object. This API can be used to read data from the pasteboard asynchronously, such as when the UI response is required or the main thread should not be blocked. Compared with [getDataSync](#getdatasync), **getData** does not block the UI thread and is suitable for processing a large amount of data or remote data.

To use the custom control to access the pasteboard content, you must [request the permission to access the pasteboard](../../../basic-services/pasteboard/get-pastedata-permission-guidelines.md). Those using [PasteButton](../../../security/AccessToken/pastebutton.md) can access the pasteboard content without permission requests.

**Since:** 9

**Required permissions:** 
- API version 12 and later: ohos.permission.READ_PASTEBOARD
- API versions 9 to 11: N/A

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-getData(callback: AsyncCallback<PasteData>): void--><!--Device-SystemPasteboard-getData(callback: AsyncCallback<PasteData>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[PasteData](arkts-basicservices-pasteboard-pastedata-i.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the system pasteboard data. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types. |
| [27787277](../errorcode-pasteboard.md#27787277-another-copy-or-paste-operation-in-progress) | Another copy or paste operation is in progress. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the SystemPasteboard object.
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
// Read the system clipboard content.
systemPasteboard.getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
    if (err) {
        console.error(`Failed to get PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
        return;
    }
    // Obtain the plain text content from the pasteboard.
    let text: string = pasteData.getPrimaryText();
});
```

## getData

```TypeScript
getData(): Promise<PasteData>
```

Obtains data from the system pasteboard and encapsulates the data into a **PasteData** object. This API uses a promise to return the result. This API can be used to read data from the pasteboard asynchronously, such as when the UI response is required or the main thread should not be blocked.

To use the custom control to access the pasteboard content, you must [request the permission to access the pasteboard](../../../basic-services/pasteboard/get-pastedata-permission-guidelines.md). Those using [PasteButton](../../../security/AccessToken/pastebutton.md) can access the pasteboard content without permission requests.

**Since:** 9

**Required permissions:** 
- API version 12 and later: ohos.permission.READ_PASTEBOARD
- API versions 9 to 11: N/A

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-getData(): Promise<PasteData>--><!--Device-SystemPasteboard-getData(): Promise<PasteData>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[PasteData](arkts-basicservices-pasteboard-pastedata-i.md)&gt; | Promise used to return the system pasteboard data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [27787277](../errorcode-pasteboard.md#27787277-another-copy-or-paste-operation-in-progress) | Another copy or paste operation is in progress. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the SystemPasteboard object.
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
// Read the system clipboard content.
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    // Obtain the plain text content from the pasteboard.
    let text: string = pasteData.getPrimaryText();
}).catch((err: BusinessError) => {
    console.error(`Failed to get PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
});
```

## getDataSource

```TypeScript
getDataSource(): string
```

Obtains the name of the app that provides the pasteboard data. This method is applicable to scenarios such as security audit, data tracking, and notifying users of the data source.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-getDataSource(): string--><!--Device-SystemPasteboard-getDataSource(): string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| string | Application name. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12900005](../errorcode-pasteboard.md#12900005-request-timeout) | Excessive processing time for internal data. |

**Examples**

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: string = systemPasteboard.getDataSource();
    console.info(`Succeeded in getting DataSource. Result: ${result}`);
} catch (err) { 
    console.error(`Failed to get DataSource. errorCode: ${err.code}, errorMessage: ${err.message}.`);
};
```

## getDataSync

```TypeScript
getDataSync(): PasteData
```

Reads data in the system pasteboard. This API returns the result synchronously. This API is used to obtain pasteboard data synchronously in key service processes or process pasteboard data immediately. Do not call this API on the UI thread to prevent blocking the UI. Use the asynchronous API [getData](#getdata-1) to process a large amount of data or remote data.

To use the custom control to access the pasteboard content, you must [request the permission to access the pasteboard](../../../basic-services/pasteboard/get-pastedata-permission-guidelines.md). Those using [PasteButton](../../../security/AccessToken/pastebutton.md) can access the pasteboard content without permission requests.

**Since:** 11

**Required permissions:** 
- API version 12 and later: ohos.permission.READ_PASTEBOARD
- API version 11: N/A

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-getDataSync(): PasteData--><!--Device-SystemPasteboard-getDataSync(): PasteData-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Data in the system pasteboard. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12900005](../errorcode-pasteboard.md#12900005-request-timeout) | Excessive processing time for internal data. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: pasteboard.PasteData = systemPasteboard.getDataSync();
    console.info('Succeeded in getting PasteData.');
} catch (err) {
    console.error(`Failed to get PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
};
```

## getDataWithProgress

```TypeScript
getDataWithProgress(params: GetDataParams): Promise<PasteData>
```

Obtains the pasteboard data and progress. This API uses a promise to return the result. Folders cannot be copied. For the copy operation of large files, you are advised to register a listener to track the copy progress and prevent long waiting time on the UI thread. You are also advised to set a proper destination path to ensure sufficient storage space. This method is applicable to the large file pasting scenario. In this scenario, you can use this callback to display the copy progress or monitor the copy process to cancel the operation when necessary.

To use the custom control to access the pasteboard content, you must [request the permission to access the pasteboard](../../../basic-services/pasteboard/get-pastedata-permission-guidelines.md). Those using [PasteButton](../../../security/AccessToken/pastebutton.md) can access the pasteboard content without permission requests.

**Since:** 15

**Required permissions:** ohos.permission.READ_PASTEBOARD

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-SystemPasteboard-getDataWithProgress(params: GetDataParams): Promise<PasteData>--><!--Device-SystemPasteboard-getDataWithProgress(params: GetDataParams): Promise<PasteData>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [GetDataParams](arkts-basicservices-pasteboard-getdataparams-i.md) | Yes | Parameters required when an application uses the file copy capability provided by the pasteboard, including the destination path, file conflict options, and progress indicator types. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[PasteData](arkts-basicservices-pasteboard-pastedata-i.md)&gt; | Promise used to return the system pasteboard data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [12900003](../errorcode-pasteboard.md#12900003-another-copy-or-paste-operation-in-progress) | Another copy or paste operation is in progress. |
| [12900007](../errorcode-pasteboard.md#12900007-file-copying-failure) | Invalid destUri or file system error. |
| [12900008](../errorcode-pasteboard.md#12900008-progress-startup-failure) | Failed to start progress. |
| [12900009](../errorcode-pasteboard.md#12900009-progress-reporting-exception) | Progress exits abnormally. |
| [12900010](../errorcode-pasteboard.md#12900010-data-obtaining-failure) | System error occurred during paste execution. |

**Examples**

```TypeScript
import { BusinessError, pasteboard } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';
@Entry
@Component
struct PasteboardTest {
 build() {
   RelativeContainer() {
     Column() {
       Column() {
         Button("Copy txt")
           .onClick(async ()=>{
              let text = "test";
              let pasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, text);
              let systemPasteboard = pasteboard.getSystemPasteboard();
              await systemPasteboard.setData(pasteData);
              let progressListenerInfo = (progress: pasteboard.ProgressInfo) => {
                console.info(`progressListener success, progress: ${progress.progress}`);
              };
              let destPath: string = '/data/storage/el2/base/files/';
              let destUri : string = fileUri.getUriFromPath(destPath);
              let params: pasteboard.GetDataParams = {
                destUri: destUri,
                fileConflictOptions: pasteboard.FileConflictOptions.OVERWRITE,
                progressIndicator: pasteboard.ProgressIndicator.DEFAULT,
                progressListener: progressListenerInfo,
              };
              systemPasteboard.getDataWithProgress(params).then((pasteData: pasteboard.PasteData) => {
                console.info('getDataWithProgress success');
              }).catch((err: BusinessError) => {
                console.error(`Failed to get PasteData. CerrorCode: ${err.code}, errorMessage: ${err.message}.`);
              })
          })
        }
      }
    }
  }
}
```

## getMimeTypes

```TypeScript
getMimeTypes(): Promise<Array<string>>
```

Obtains the MIME type from the pasteboard. This API uses a promise to return the result.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-SystemPasteboard-getMimeTypes(): Promise<Array<string>>--><!--Device-SystemPasteboard-getMimeTypes(): Promise<Array<string>>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | Promise used to return the read MIME type. |

**Examples**

```TypeScript
import { pasteboard, BusinessError } from '@kit.BasicServicesKit'

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getMimeTypes().then((data: Array<string>) => {
    console.info('Succeeded in getting mimeTypes. mimeTypes: ' + data.sort().join(','));
}).catch((err: BusinessError) => {
    console.error(`Failed to get mimeTypes. errorCode: ${err.code}, errorMessage: ${err.message}.`);
});
```

## getUnifiedData

```TypeScript
getUnifiedData(): Promise<unifiedDataChannel.UnifiedData>
```

Obtains a **PasteData** object from the pasteboard. This API uses a promise to return the result. This API is used for cross-app data exchange using [UnifiedData](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-unifieddata-c.md). This API can be used to share data with other apps that support **UnifiedData** or process complex data of multiple types. Compared with [getData](#getdata-1), **getUnifiedData** provides more standard data formats.

To use the custom control to access the pasteboard content, you must [request the permission to access the pasteboard](../../../basic-services/pasteboard/get-pastedata-permission-guidelines.md). Those using [PasteButton](../../../security/AccessToken/pastebutton.md) can access the pasteboard content without permission requests.

**Since:** 12

**Required permissions:** ohos.permission.READ_PASTEBOARD

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SystemPasteboard-getUnifiedData(): Promise<unifiedDataChannel.UnifiedData>--><!--Device-SystemPasteboard-getUnifiedData(): Promise<unifiedDataChannel.UnifiedData>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[unifiedDataChannel.UnifiedData](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-unifieddata-c.md)&gt; | Promise used to return the system pasteboard data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [27787277](../errorcode-pasteboard.md#27787277-another-copy-or-paste-operation-in-progress) | Another copy or paste operation is in progress. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { unifiedDataChannel, uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getUnifiedData().then((data) => {
    let records: Array<unifiedDataChannel.UnifiedRecord> = data.getRecords();
    for (let j = 0; j < records.length; j++) {
        if (records[j].getType() === uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) {
            let text = records[j].getValue() as uniformDataStruct.PlainText;
            console.info(`${j + 1}.${text.textContent}`);
        }
    }
}).catch((err: BusinessError) => {
    console.error(`Failed to get UnifiedData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
});
```

## getUnifiedDataSync

```TypeScript
getUnifiedDataSync(): unifiedDataChannel.UnifiedData
```

Reads data in the system pasteboard. This API returns the result synchronously. This API is used for cross-app data exchange using **UnifiedData**. This API can be used to immediately obtain data from the pasteboard in key service processes and share the data with other apps that support **UnifiedData**. The delay in obtaining data from the pasteboard is affected by the data volume and network environment. Therefore, calling this API may take a long time. You are advised to call this API in non-UI threads.

To use the custom control to access the pasteboard content, you must [request the permission to access the pasteboard](../../../basic-services/pasteboard/get-pastedata-permission-guidelines.md). Those using [PasteButton](../../../security/AccessToken/pastebutton.md) can access the pasteboard content without permission requests.

**Since:** 12

**Required permissions:** ohos.permission.READ_PASTEBOARD

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SystemPasteboard-getUnifiedDataSync(): unifiedDataChannel.UnifiedData--><!--Device-SystemPasteboard-getUnifiedDataSync(): unifiedDataChannel.UnifiedData-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| [unifiedDataChannel.UnifiedData](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-unifieddata-c.md) | Data in the system pasteboard. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [12900005](../errorcode-pasteboard.md#12900005-request-timeout) | Excessive processing time for internal data. |

**Examples**

```TypeScript
import { unifiedDataChannel } from '@kit.ArkData';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: unifiedDataChannel.UnifiedData = systemPasteboard.getUnifiedDataSync();
    console.info('Succeeded in getting UnifiedData.');
} catch (err) {
    console.error(`Failed to get UnifiedData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
};
```

## hasData

```TypeScript
hasData(callback: AsyncCallback<boolean>): void
```

Checks whether the system pasteboard contains data. This API uses an asynchronous callback to return the result. This API can be used to check whether the pasteboard contains data asynchronously without blocking the main thread, such as the interaction process that requires the UI response. Unlike the synchronous API [hasDataSync](#hasdatasync), this API does not block the UI thread and is more suitable for UI interactions.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-hasData(callback: AsyncCallback<boolean>): void--><!--Device-SystemPasteboard-hasData(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result of whether pasteboard contains data. Callback used to return the result. Returns **true** if the system pasteboard contains data; returns **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.hasData((err: BusinessError, data: boolean) => {
    if (err) {
        console.error(`Failed to check the PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
        return;
    }
    console.info(`Succeeded in checking the PasteData. Data: ${data}`);
});
```

## hasData

```TypeScript
hasData(): Promise<boolean>
```

Checks whether the system pasteboard contains data. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-hasData(): Promise<boolean>--><!--Device-SystemPasteboard-hasData(): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Callback used to return the result. Returns **true** if the system pasteboard contains data; returns **false** otherwise. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.hasData().then((data: boolean) => {
    console.info(`Succeeded in checking the PasteData. Data: ${data}`);
}).catch((err: BusinessError) => {
    console.error(`Failed to check the PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
});
```

## hasDataSync

```TypeScript
hasDataSync(): boolean
```

Checks whether the system pasteboard contains data. This API returns the result synchronously.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-hasDataSync(): boolean--><!--Device-SystemPasteboard-hasDataSync(): boolean-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Callback used to return the result. Returns **true** if the system pasteboard contains data; returns **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12900005](../errorcode-pasteboard.md#12900005-request-timeout) | Excessive processing time for internal data. |

**Examples**

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: boolean = systemPasteboard.hasDataSync();
    console.info(`Succeeded in checking the PasteData. Result: ${result}`);
} catch (err) {
    console.error(`Failed to check the PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
};
```

## hasDataType

```TypeScript
hasDataType(mimeType: string): boolean
```

Checks whether the pasteboard contains data of the specified type.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-hasDataType(mimeType: string): boolean--><!--Device-SystemPasteboard-hasDataType(mimeType: string): boolean-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mimeType | string | Yes | Data type, which is used to check whether specific data of this type exists in the pasteboard. The length of **mimeType** cannot exceed 1024 bytes. If the length exceeds 1024 bytes, error code 401 is returned. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Checks whether the pasteboard contains data of the specified type. The value **true** indicates the pasteboard contains data of the specified type; the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types. |
| [12900005](../errorcode-pasteboard.md#12900005-request-timeout) | Excessive processing time for internal data. |

**Examples**

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: boolean = systemPasteboard.hasDataType(pasteboard.MIMETYPE_TEXT_PLAIN);
    console.info(`Succeeded in checking the DataType. Result: ${result}`);
} catch (err) {
    console.error(`Failed to check the DataType. errorCode: ${err.code}, errorMessage: ${err.message}.`);
};
```

## hasRemoteData

```TypeScript
hasRemoteData(): boolean
```

Checks whether the pasteboard data is on a remote device. Transferring data across devices takes time. If the pasteboard data is on a remote device, do not check for custom data types or read the pasteboard data on the UI thread.

**Since:** 24

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-SystemPasteboard-hasRemoteData(): boolean--><!--Device-SystemPasteboard-hasRemoteData(): boolean-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns the check result. The value **true** indicates that the pasteboard data is on a remote device, and **false** indicates the opposite. Default value: **false**. |

**Examples**

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();

let result: boolean = systemPasteboard.hasRemoteData();
console.info(`Succeeded in checking the remote data. Result: ${result}`);
```

## isRemoteData

```TypeScript
isRemoteData(): boolean
```

Checks whether the data in the pasteboard is from another device. Transferring data across devices takes time. If the pasteboard data is on a remote device, do not check for custom data types or read the pasteboard data on the UI thread.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-isRemoteData(): boolean--><!--Device-SystemPasteboard-isRemoteData(): boolean-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Checks whether the data in the pasteboard is from another device. The value **true** indicates the data in the pasteboard is from another device; the value **false** indicates the data is from the local device. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12900005](../errorcode-pasteboard.md#12900005-request-timeout) | Excessive processing time for internal data. |

**Examples**

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: boolean = systemPasteboard.isRemoteData();
    console.info(`Succeeded in checking the RemoteData. Result: ${result}`);
} catch (err) {
    console.error(`Failed to check the RemoteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
};
```

## off('update')

```TypeScript
off(type: 'update', callback?: () => void): void
```

Unsubscribes from the system pasteboard content change event.

- This API is used to unsubscribe from the event subscribed to by **on('update')**.  
- This API can be called only after an event has been subscribed to.  
- If the **callback** parameter is not specified, listening will be disabled for all callbacks registered by the  
current application.

**Since:** 7

<!--Device-SystemPasteboard-off(type: 'update', callback?: () => void): void--><!--Device-SystemPasteboard-off(type: 'update', callback?: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'update' | Yes | Event type. The value **'update'** indicates changes in the pasteboard content. |
| callback | () =&gt; void | No | Callback invoked when the pasteboard content changes. If this parameter is not specified, listening will be disabled for all callbacks registered by the current application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types. |

**Examples**

```TypeScript
// Obtain the SystemPasteboard object.
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
// Define a callback to be invoked when the pasteboard content changes.
let listener = () => {
    console.info('The system pasteboard has changed.');
};
// Unsubscribe from the pasteboard content change event.
systemPasteboard.off('update', listener);
```

## offRemoteUpdate

```TypeScript
offRemoteUpdate(callback?: UpdateCallback): void
```

Unsubscribes from the content change events of the pasteboard on a remote device.

**Since:** 22

<!--Device-SystemPasteboard-offRemoteUpdate(callback?: UpdateCallback): void--><!--Device-SystemPasteboard-offRemoteUpdate(callback?: UpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [UpdateCallback](arkts-basicservices-pasteboard-updatecallback-t.md) | No | allback to be invoked when the pasteboard content on the remote device changes. If this parameter is not specified, remote listening will be disabled for all callbacks registered by the current application. |

**Examples**

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let listener = () => {
    console.info('The remote pasteboard has changed.');
};
systemPasteboard.offRemoteUpdate(listener);
```

## on('update')

```TypeScript
on(type: 'update', callback: () => void): void
```

Subscribes to the content change event of the system pasteboard. After this method is called, the system registers a listener in the pasteboard service. The callback is triggered when content is written, cleared, or modified in the pasteboard. Multiple listeners can be registered. You need to call **off('update')** to unsubscribe from the content change event at a proper time to release resources. This API is called when an app needs to respond to pasteboard content changes in real time, for example, to automatically detect data in a specific format or to implement intelligent paste suggestions.

- Call [off('update')](#offupdate) to  
unsubscribe from the content change event of the system pasteboard when it is no longer needed.  
- If the event is not unsubscribed from, the callback function will continuously listen for pasteboard changes,  
which may cause memory leaks or the callback being triggered from multiple times.  
- You are advised to unsubscribe from the event when the component or page is destroyed.

**Since:** 7

<!--Device-SystemPasteboard-on(type: 'update', callback: () => void): void--><!--Device-SystemPasteboard-on(type: 'update', callback: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'update' | Yes | Event type. The value **'update'** indicates changes in the pasteboard content. Other values are invalid. |
| callback | () =&gt; void | Yes | Callback invoked when the pasteboard content changes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types. |

**Examples**

```TypeScript
// Obtain the SystemPasteboard object.
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
// Define a callback to be invoked when the pasteboard content changes.
let listener = () => {
    console.info('The system pasteboard has changed.');
};
// Subscribe to the pasteboard content change event.
systemPasteboard.on('update', listener);
```

## onRemoteUpdate

```TypeScript
onRemoteUpdate(callback: UpdateCallback): void
```

Subscribes to the content change events of the pasteboard on a remote device. This callback is triggered when the pasteboard content on the remote device changes.

- Call [offRemoteUpdate](../../../reference/apis-basic-services-kit/js-apis-pasteboard.md#offremoteupdatecallback-updatecallback22) to unsubscribe from the content change event of the pasteboard when it is no longer needed.  
- If the event is not unsubscribed from, the callback function will continuously listen for remote changes, which  
may cause memory leaks.  
- You are advised to unsubscribe from the event when the component or page is destroyed.

**Since:** 22

<!--Device-SystemPasteboard-onRemoteUpdate(callback: UpdateCallback): void--><!--Device-SystemPasteboard-onRemoteUpdate(callback: UpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [UpdateCallback](arkts-basicservices-pasteboard-updatecallback-t.md) | Yes | Callback invoked when the pasteboard content changes. The listener parameters are not specified. The callback is used to listen for cross-device pasteboard data update events, which is triggered when the pasteboard data on a remote device changes. |

**Examples**

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let listener = () => {
    console.info('The remote pasteboard has changed.');
};
systemPasteboard.onRemoteUpdate(listener);
```

## removeAppShareOptions

```TypeScript
removeAppShareOptions(): void
```

Deletes the global pasteable range of the application. This API can be used to delete the previously set pasteable scope and restore the default pasteable scope for pasteboard data.

- This API must be used together with **setAppShareOptions()**.  
- The sharing scope set by **setAppShareOptions()** is deleted.  
- This API can be called only after the sharing scope has been set.

**Since:** 14

**Required permissions:** 
- API version 14 and later: ohos.permission.MANAGE_PASTEBOARD_APP_SHARE_OPTION
- API versions 12 to 13: N/A

<!--Device-SystemPasteboard-removeAppShareOptions(): void--><!--Device-SystemPasteboard-removeAppShareOptions(): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API.<br>**Applicable version:** 14 and later |

**Examples**

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
  systemPasteboard.removeAppShareOptions();
  console.info('Remove app share options success.');
} catch (error) {
  console.error(`Remove app share options failed, errorCode: ${error.code}, errorMessage: ${error.message}.`);
}
```

## setAppShareOptions

```TypeScript
setAppShareOptions(shareOptions: ShareOption): void
```

Sets pasteable range of pasteboard data for applications. This API can be used to globally restrict the pasteable scope of pasteboard data generated by the app. For example, a financial app needs to protect sensitive user information.

- This API is used together with **removeAppShareOptions()**.  
- To delete the configured sharing scope, call **removeAppShareOptions()**.

**Since:** 14

**Required permissions:** 
- API version 14 and later: ohos.permission.MANAGE_PASTEBOARD_APP_SHARE_OPTION
- API versions 12 to 13: N/A

<!--Device-SystemPasteboard-setAppShareOptions(shareOptions: ShareOption): void--><!--Device-SystemPasteboard-setAppShareOptions(shareOptions: ShareOption): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| shareOptions | [ShareOption](arkts-basicservices-pasteboard-shareoption-e.md) | Yes | Pasteable range. Only the enumeration values ​​defined in **pasteboard.ShareOption** are allowed. If other values are passed, error code 401 is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameter types;         3. Parameter verification failed. |
| [12900006](../errorcode-pasteboard.md#12900006-settings-already-exists) | Settings already exist. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API.<br>**Applicable version:** 14 and later |

**Examples**

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
  systemPasteboard.setAppShareOptions(pasteboard.ShareOption.INAPP);
  console.info('Set app share options success.');
} catch (error) {
  console.error(`Set app share options failed, errorCode: ${error.code}, errorMessage: ${error.message}.`);
}
```

## setData

```TypeScript
setData(data: PasteData, callback: AsyncCallback<void>): void
```

Writes a **PasteData** object to the pasteboard. This API uses an asynchronous callback to return the result. After this API is called, the system writes the data of the **PasteData** object to the pasteboard. After the data is written successfully, other apps can read the data from the pasteboard. The written data will replace the existing data in the pasteboard. This API can be used to write data to the pasteboard asynchronously, such as when the UI response is required or the main thread should not be blocked. Unlike [setDataSync](#setdatasync), **setData** does not block the UI thread.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-setData(data: PasteData, callback: AsyncCallback<void>): void--><!--Device-SystemPasteboard-setData(data: PasteData, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Yes | **PasteData** object. After this parameter is set, the data is written to the system pasteboard for the app to read and paste. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types. |
| [27787277](../errorcode-pasteboard.md#27787277-another-copy-or-paste-operation-in-progress) | Another copy or paste operation is in progress. |
| [27787278](../errorcode-pasteboard.md#27787278-copy-prohibited) | Replication is prohibited. |

**Examples**

```TypeScript
// Create a PasteData object of the plain text type.
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'content');
// Obtain the SystemPasteboard object.
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
// Write data to the system pasteboard.
systemPasteboard.setData(pasteData, (err, data) => {
    if (err) {
        console.error(`Failed to set PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
        return;
    }
    console.info('Succeeded in setting PasteData.');
});
```

## setData

```TypeScript
setData(data: PasteData): Promise<void>
```

Writes a **PasteData** object to the pasteboard. This API uses a promise to return the result. This API can be used to write data to the pasteboard asynchronously without blocking the main thread, such as the interaction process that requires the UI response. Unlike the synchronous API [setDataSync](#setdatasync), this API does not block the UI thread and is more suitable for UI interactions.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-setData(data: PasteData): Promise<void>--><!--Device-SystemPasteboard-setData(data: PasteData): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Yes | **PasteData** object. Before calling this API, ensure that no other copy or paste operation is in progress. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types. |
| [27787277](../errorcode-pasteboard.md#27787277-another-copy-or-paste-operation-in-progress) | Another copy or paste operation is in progress. |
| [27787278](../errorcode-pasteboard.md#27787278-copy-prohibited) | Replication is prohibited. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Create a PasteData object of the plain text type.
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'content');
// Obtain the SystemPasteboard object.
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
// Write data to the system pasteboard.
systemPasteboard.setData(pasteData).then((data: void) => {
    console.info('Succeeded in setting PasteData.');
}).catch((err: BusinessError) => {
    console.error(`Failed to set PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
});
```

## setDataSync

```TypeScript
setDataSync(data: PasteData): void
```

Writes data to the system pasteboard. This API returns the result synchronously. This API can be used to write data to the pasteboard synchronously in key service processes or confirm the write result immediately.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-setDataSync(data: PasteData): void--><!--Device-SystemPasteboard-setDataSync(data: PasteData): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Yes | Data to be written to the pasteboard. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types. |
| [12900005](../errorcode-pasteboard.md#12900005-request-timeout) | Excessive processing time for internal data. |

**Examples**

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    systemPasteboard.setDataSync(pasteData);
    console.info('Succeeded in setting PasteData.');
} catch (err) {
    console.error(`Failed to set PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
};
```

## setUnifiedData

```TypeScript
setUnifiedData(data: unifiedDataChannel.UnifiedData): Promise<void>
```

Writes a **PasteData** object to the pasteboard. This API uses a promise to return the result. This API can be used to write data to the pasteboard asynchronously without blocking the main thread, such as the interaction process that requires the UI response. Unlike the synchronous API [setUnifiedDataSync](#setunifieddatasync), this API does not block the UI thread and is more suitable for UI interactions.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SystemPasteboard-setUnifiedData(data: unifiedDataChannel.UnifiedData): Promise<void>--><!--Device-SystemPasteboard-setUnifiedData(data: unifiedDataChannel.UnifiedData): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [unifiedDataChannel.UnifiedData](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-unifieddata-c.md) | Yes | Data to be written to the pasteboard. Before calling this API, ensure that no other copy or paste operation is in progress. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types. |
| [27787277](../errorcode-pasteboard.md#27787277-another-copy-or-paste-operation-in-progress) | Another copy or paste operation is in progress. |
| [27787278](../errorcode-pasteboard.md#27787278-copy-prohibited) | Replication is prohibited. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { unifiedDataChannel, uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

// Create a data structure object of the plain text type.
let plainText : uniformDataStruct.PlainText = {
    uniformDataType: uniformTypeDescriptor.UniformDataType.PLAIN_TEXT,
    textContent : 'PLAINTEXT_CONTENT',
    abstract : 'PLAINTEXT_ABSTRACT',
}
// Create a UnifiedRecord object.
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
// Create a UnifiedData object.
let data = new unifiedDataChannel.UnifiedData();
// Add the data record to the UnifiedData object.
data.addRecord(record);

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.setUnifiedData(data).then((data: void) => {
    console.info('Succeeded in setting UnifiedData.');
}).catch((err: BusinessError) => {
    console.error(`Failed to setUnifiedData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
});
```

## setUnifiedDataSync

```TypeScript
setUnifiedDataSync(data: unifiedDataChannel.UnifiedData): void
```

Writes data to the system pasteboard. This API returns the result synchronously. This API is used for cross-app data exchange using **UnifiedData**. This API can be used to immediately write data to the pasteboard in key service processes and share the data with other apps that support [UnifiedData](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-unifieddata-c.md).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SystemPasteboard-setUnifiedDataSync(data: unifiedDataChannel.UnifiedData): void--><!--Device-SystemPasteboard-setUnifiedDataSync(data: unifiedDataChannel.UnifiedData): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [unifiedDataChannel.UnifiedData](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-unifieddata-c.md) | Yes | Data to be written to the pasteboard. Cross-app data exchange is supported. Other apps can read the data using **unifiedDataChannel**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types. |
| [12900005](../errorcode-pasteboard.md#12900005-request-timeout) | Excessive processing time for internal data. |

**Examples**

```TypeScript
import { unifiedDataChannel } from '@kit.ArkData';

// Create a UnifiedData object.
let plainTextData = new unifiedDataChannel.UnifiedData();
// Create a data object of the plain text type.
let plainText = new unifiedDataChannel.PlainText();
// Set the detailed information about the plain text.
plainText.details = {
    Key: 'delayPlaintext',
    Value: 'delayPlaintext',
};
// Set the text content.
plainText.textContent = 'delayTextContent';
// Set the abstract content.
plainText.abstract = 'delayTextContent';
// Add the data record to the UnifiedData object.
plainTextData.addRecord(plainText);

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    systemPasteboard.setUnifiedDataSync(plainTextData);
    console.info('Succeeded in setting UnifiedData.');
} catch (err) {
    console.error(`Failed to set UnifiedData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
};
```

## clear

```TypeScript
clear(callback: AsyncCallback<void>): void
```

Clears the system pasteboard. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [clearData](#cleardata-1)(callback: AsyncCallback&lt;void&gt;)

<!--Device-SystemPasteboard-clear(callback: AsyncCallback<void>): void--><!--Device-SystemPasteboard-clear(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types. |

**Examples**

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.clear((err, data) => {
    if (err) {
        console.error(`Failed to clear the PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
        return;
    }
    console.info('Succeeded in clearing the PasteData.');
});
```

## clear

```TypeScript
clear(): Promise<void>
```

Clears the system pasteboard. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [clearData](#cleardata)()

<!--Device-SystemPasteboard-clear(): Promise<void>--><!--Device-SystemPasteboard-clear(): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.clear().then((data) => {
    console.info('Succeeded in clearing the PasteData.');
}).catch((err: BusinessError) => {
    console.error(`Failed to clear the PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
});
```

## getPasteData

```TypeScript
getPasteData(callback: AsyncCallback<PasteData>): void
```

Obtains a **PasteData** object from the pasteboard. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getData](#getdata-1)(callback: AsyncCallback&lt;PasteData&gt;)

<!--Device-SystemPasteboard-getPasteData(callback: AsyncCallback<PasteData>): void--><!--Device-SystemPasteboard-getPasteData(callback: AsyncCallback<PasteData>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[PasteData](arkts-basicservices-pasteboard-pastedata-i.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the system pasteboard data. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the SystemPasteboard object.
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
// Read the system clipboard content.
systemPasteboard.getPasteData((err: BusinessError, pasteData: pasteboard.PasteData) => {
    if (err) {
        console.error(`Failed to get PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
        return;
    }
    // Obtain the plain text content from the pasteboard.
    let text: string = pasteData.getPrimaryText();
});
```

## getPasteData

```TypeScript
getPasteData(): Promise<PasteData>
```

Obtains a **PasteData** object from the pasteboard. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getData](#getdata)()

<!--Device-SystemPasteboard-getPasteData(): Promise<PasteData>--><!--Device-SystemPasteboard-getPasteData(): Promise<PasteData>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[PasteData](arkts-basicservices-pasteboard-pastedata-i.md)&gt; | Promise used to return the system pasteboard data. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the SystemPasteboard object.
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
// Read the system clipboard content.
systemPasteboard.getPasteData().then((pasteData: pasteboard.PasteData) => {
    // Obtain the plain text content from the pasteboard.
    let text: string = pasteData.getPrimaryText();
}).catch((err: BusinessError) => {
    console.error(`Failed to get PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
});
```

## hasPasteData

```TypeScript
hasPasteData(callback: AsyncCallback<boolean>): void
```

Checks whether the system pasteboard contains data. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [hasData](#hasdata-1)(callback: AsyncCallback&lt;boolean&gt;)

<!--Device-SystemPasteboard-hasPasteData(callback: AsyncCallback<boolean>): void--><!--Device-SystemPasteboard-hasPasteData(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. Returns **true** if the system pasteboard contains data; returns **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.hasPasteData((err: BusinessError, data: boolean) => {
    if (err) {
        console.error(`Failed to check the PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
        return;
    }
    console.info(`Succeeded in checking the PasteData. Data: ${data}`);
});
```

## hasPasteData

```TypeScript
hasPasteData(): Promise<boolean>
```

Checks whether the system pasteboard contains data. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [hasData](#hasdata)()

<!--Device-SystemPasteboard-hasPasteData(): Promise<boolean>--><!--Device-SystemPasteboard-hasPasteData(): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Callback used to return the result. Returns **true** if the system pasteboard contains data; returns **false** otherwise. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.hasPasteData().then((data: boolean) => {
    console.info(`Succeeded in checking the PasteData. Data: ${data}`);
}).catch((err: BusinessError) => {
    console.error(`Failed to check the PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
});
```

## setPasteData

```TypeScript
setPasteData(data: PasteData, callback: AsyncCallback<void>): void
```

Writes a **PasteData** object to the pasteboard. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [setData](#setdata-1)(data: PasteData, callback: AsyncCallback&lt;void&gt;)

<!--Device-SystemPasteboard-setPasteData(data: PasteData, callback: AsyncCallback<void>): void--><!--Device-SystemPasteboard-setPasteData(data: PasteData, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Yes | **PasteData** object. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameters types. |

**Examples**

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('content');
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.setPasteData(pasteData, (err, data) => {
    if (err) {
        console.error(`Failed to set PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
        return;
    }
    console.info('Succeeded in setting PasteData.');
});
```

## setPasteData

```TypeScript
setPasteData(data: PasteData): Promise<void>
```

Writes a **PasteData** object to the pasteboard. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [setData](#setdata-2)(data: PasteData)

<!--Device-SystemPasteboard-setPasteData(data: PasteData): Promise<void>--><!--Device-SystemPasteboard-setPasteData(data: PasteData): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Yes | **PasteData** object. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('content');
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.setPasteData(pasteData).then((data: void) => {
    console.info('Succeeded in setting PasteData.');
}).catch((err: BusinessError) => {
    console.error(`Failed to set PasteData. errorCode: ${err.code}, errorMessage: ${err.message}.`);
});
```
