# SystemPasteboard

Provides **SystemPasteboard** APIs. Before calling any **SystemPasteboard** API, you must obtain a **SystemPasteboard** object using [getSystemPasteboard](arkts-basicservices-pasteboard-getsystempasteboard-f.md).

**Since:** 23

<!--Device-pasteboard-interface SystemPasteboard--><!--Device-pasteboard-interface SystemPasteboard-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## Modules to Import

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit';
```

## clear

```TypeScript
clear(callback: AsyncCallback<void>): void
```

Clears the system pasteboard. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [clearData](#cleardata)(callback: AsyncCallback&lt;void&gt;)

<!--Device-SystemPasteboard-clear(callback: AsyncCallback<void>): void--><!--Device-SystemPasteboard-clear(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Examples**

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.clear((err, data) => {
    if (err) {
        console.error(`Failed to clear the PasteData. Cause: ${err.message}`);
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
    console.error(`Failed to clear the PasteData. Cause: ${err.message}`);
});
```

## clearData

```TypeScript
clearData(callback: AsyncCallback<void>): void
```

Clears the system pasteboard. This API uses an asynchronous callback to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-clearData(callback: AsyncCallback<void>): void--><!--Device-SystemPasteboard-clearData(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Examples**

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.clearData((err, data) => {
    if (err) {
        console.error(`Failed to clear the pasteboard. Cause: ${err.message}`);
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

**Since:** 23

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
    console.error(`Failed to clear the pasteboard. Cause: ${err.message}`);
});
```

## clearDataSync

```TypeScript
clearDataSync(): void
```

Clears the system pasteboard. This API returns the result synchronously.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

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
    console.error('Failed to clear the pasteboard. Cause:' + err.message);
};
```

## detectPatterns

```TypeScript
detectPatterns(patterns: Array<Pattern>): Promise<Array<Pattern>>
```

Detects [patterns](arkts-basicservices-pasteboard-pattern-e.md) in the system pasteboard. This API uses a promise to return the result.

**Since:** 23

<!--Device-SystemPasteboard-detectPatterns(patterns: Array<Pattern>): Promise<Array<Pattern>>--><!--Device-SystemPasteboard-detectPatterns(patterns: Array<Pattern>): Promise<Array<Pattern>>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| patterns | Array&lt;Pattern&gt; | Yes | Pattern to be detected in the system pasteboard. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;Pattern&gt;&gt; | Promise used to return the detected patterns. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit'

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let patterns: Array<pasteboard.Pattern> = [pasteboard.Pattern.URL, pasteboard.Pattern.EMAIL_ADDRESS];

systemPasteboard.detectPatterns(patterns).then((data: Array<pasteboard.Pattern>) => {
    if (patterns.sort().join('')==data.sort().join('')) {
      console.info('All needed patterns detected, next get data');
      try {
        let result: pasteboard.PasteData = systemPasteboard.getDataSync();
        console.info('Succeeded in getting PasteData.');
      } catch (err) {
        console.error('Failed to get PasteData. Cause:' + err.message);
      };
    } else {
      console.info("Not all needed patterns detected, no need to get data.");
    }
});
```

## getChangeCount

```TypeScript
getChangeCount(): long
```

Obtains the number of pasteboard content changes. Returns the number of pasteboard content changes if this API is called successfully; returns **0** otherwise. Even though the PasteData expires, or the data becomes empty because of the called [clearDataSync](#cleardatasync) API, the number of data changes remains. When the system is restarted, or the pasteboard service is restarted due to an exception, the number of PasteData changes counts from 0. In addition, copying the same data repeatedly is considered to change the data for multiple times. Therefore, each time the data is copied, the number of data changes increases.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SystemPasteboard-getChangeCount(): long--><!--Device-SystemPasteboard-getChangeCount(): long-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| long | The number of pasteboard content changes obtained. |

**Examples**

```TypeScript
import { BusinessError, pasteboard } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result : number = systemPasteboard.getChangeCount();
    console.info(`Succeeded in getting the ChangeCount. Result: ${result}`);
} catch (err) {
    console.error(`Failed to get the ChangeCount. Cause: ${err.message}`);
};
```

## getData

```TypeScript
getData(callback: AsyncCallback<PasteData>): void
```

Obtains a **PasteData** object from the pasteboard. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** 
- API version 12+: ohos.permission.READ_PASTEBOARD

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-getData(callback: AsyncCallback<PasteData>): void--><!--Device-SystemPasteboard-getData(callback: AsyncCallback<PasteData>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-asynccallback-t.md)&lt;[PasteData](arkts-basicservices-pasteboard-pastedata-i.md)&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| [27787277](../errorcode-pasteboard.md#27787277-another-copy-or-paste-operation-in-progress) | Another copy or paste operation is in progress. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
    if (err) {
        console.error('Failed to get PasteData. Cause: ' + err.message);
        return;
    }
    let text: string = pasteData.getPrimaryText();
});
```

## getData

```TypeScript
getData(): Promise<PasteData>
```

Obtains a **PasteData** object from the pasteboard. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** 
- API version 12+: ohos.permission.READ_PASTEBOARD

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-getData(): Promise<PasteData>--><!--Device-SystemPasteboard-getData(): Promise<PasteData>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[PasteData](arkts-basicservices-pasteboard-pastedata-i.md)&gt; | Promise used to return the system PasteData. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [27787277](../errorcode-pasteboard.md#27787277-another-copy-or-paste-operation-in-progress) | Another copy or paste operation is in progress. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    let text: string = pasteData.getPrimaryText();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});
```

## getDataSource

```TypeScript
getDataSource(): string
```

Obtains the name of the application that provides data.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

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
    console.error('Failed to get DataSource. Cause:' + err.message);
};
```

## getDataSync

```TypeScript
getDataSync(): PasteData
```

Obtains a **PasteData** object from the pasteboard. This API returns the result synchronously.

**Since:** 23

**Required permissions:** 
- API version 12+: ohos.permission.READ_PASTEBOARD

**Atomic service API:** This API can be used in atomic services since API version 23.

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
    console.error('Failed to get PasteData. Cause:' + err.message);
};
```

## getDataWithProgress

```TypeScript
getDataWithProgress(params: GetDataParams): Promise<PasteData>
```

Obtains the PasteData from the system pasteboard with system progress. This API uses a promise to return the result. Folders cannot be copied.

**Since:** 23

**Required permissions:** ohos.permission.READ_PASTEBOARD

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SystemPasteboard-getDataWithProgress(params: GetDataParams): Promise<PasteData>--><!--Device-SystemPasteboard-getDataWithProgress(params: GetDataParams): Promise<PasteData>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | GetDataParams | Yes | Parameters required when an application obtains the Data from the system pasteboard, including the destination path, file conflict options, and progress indicator types. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[PasteData](arkts-basicservices-pasteboard-pastedata-i.md)&gt; | Promise used to return the system PasteData. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [12900007](../errorcode-pasteboard.md#12900007-file-copying-failure) | Invalid destUri or file system error. |
| [12900003](../errorcode-pasteboard.md#12900003-another-copy-or-paste-operation-in-progress) | Another copy or paste operation is in progress. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
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
                console.info('progressListener success, progress:' + progress.progress);
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
                console.error('Failed to get PasteData. Cause: ' + err.message);
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

Obtains the types of PasteData in the system pasteboard. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SystemPasteboard-getMimeTypes(): Promise<Array<string>>--><!--Device-SystemPasteboard-getMimeTypes(): Promise<Array<string>>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | Promise used to return the types. |

**Examples**

```TypeScript
import { pasteboard, BusinessError } from '@kit.BasicServicesKit'

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getMimeTypes().then((data: Array<String>) => {
    console.info('Succeeded in getting mimeTypes. mimeTypes: ' + data.sort().join(','));
}).catch((err: BusinessError) => {
    console.error('Failed to get mimeTypes. Cause:' + err.message);
});
```

## getPasteData

```TypeScript
getPasteData(callback: AsyncCallback<PasteData>): void
```

Obtains a **PasteData** object from the pasteboard. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getData](#getdata)(callback: AsyncCallback&lt;PasteData&gt;)

<!--Device-SystemPasteboard-getPasteData(callback: AsyncCallback<PasteData>): void--><!--Device-SystemPasteboard-getPasteData(callback: AsyncCallback<PasteData>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-asynccallback-t.md)&lt;[PasteData](arkts-basicservices-pasteboard-pastedata-i.md)&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getPasteData((err: BusinessError, pasteData: pasteboard.PasteData) => {
    if (err) {
        console.error('Failed to get PasteData. Cause: ' + err.message);
        return;
    }
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
| Promise&lt;[PasteData](arkts-basicservices-pasteboard-pastedata-i.md)&gt; | Promise used to return the system PasteData. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getPasteData().then((pasteData: pasteboard.PasteData) => {
    let text: string = pasteData.getPrimaryText();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});
```

## getUnifiedData

```TypeScript
getUnifiedData(): Promise<unifiedDataChannel.UnifiedData>
```

Obtains a **PasteData** object from the system pasteboard. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.READ_PASTEBOARD

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SystemPasteboard-getUnifiedData(): Promise<unifiedDataChannel.UnifiedData>--><!--Device-SystemPasteboard-getUnifiedData(): Promise<unifiedDataChannel.UnifiedData>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;unifiedDataChannel.UnifiedData&gt; | Promise used to return the system PasteData. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [27787277](../errorcode-pasteboard.md#27787277-another-copy-or-paste-operation-in-progress) | Another copy or paste operation is in progress. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |

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
    console.error('Failed to get UnifiedData. Cause: ' + err.message);
});
```

## getUnifiedDataSync

```TypeScript
getUnifiedDataSync(): unifiedDataChannel.UnifiedData
```

Obtains a **UnifiedData** object from the system pasteboard. This API returns the result synchronously.

**Since:** 23

**Required permissions:** ohos.permission.READ_PASTEBOARD

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SystemPasteboard-getUnifiedDataSync(): unifiedDataChannel.UnifiedData--><!--Device-SystemPasteboard-getUnifiedDataSync(): unifiedDataChannel.UnifiedData-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| unifiedDataChannel.UnifiedData | Data in the system pasteboard. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12900005](../errorcode-pasteboard.md#12900005-request-timeout) | Excessive processing time for internal data. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |

**Examples**

```TypeScript
import { unifiedDataChannel } from '@kit.ArkData';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: unifiedDataChannel.UnifiedData = systemPasteboard.getUnifiedDataSync();
    console.info('Succeeded in getting UnifiedData.');
} catch (err) {
    console.error('Failed to get UnifiedData. Cause:' + err.message);
};
```

## hasData

```TypeScript
hasData(callback: AsyncCallback<boolean>): void
```

Checks whether the system pasteboard contains data. This API uses an asynchronous callback to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-hasData(callback: AsyncCallback<boolean>): void--><!--Device-SystemPasteboard-hasData(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-asynccallback-t.md)&lt;boolean&gt; | Yes | Callback used to return the result. Returns **true** if the system pasteboard contains data; returns **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.hasData((err: BusinessError, data: boolean) => {
    if (err) {
        console.error(`Failed to check the PasteData. Cause: ${err.message}`);
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

**Since:** 23

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
    console.error(`Failed to check the PasteData. Cause: ${err.message}`);
});
```

## hasDataSync

```TypeScript
hasDataSync(): boolean
```

Checks whether the system pasteboard contains data. This API returns the result synchronously.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

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
    console.error('Failed to check the PasteData. Cause:' + err.message);
};
```

## hasDataType

```TypeScript
hasDataType(mimeType: string): boolean
```

Checks whether the pasteboard contains data of the specified type.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SystemPasteboard-hasDataType(mimeType: string): boolean--><!--Device-SystemPasteboard-hasDataType(mimeType: string): boolean-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mimeType | string | Yes | Data type. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the pasteboard contains data of the specified type; returns **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| [12900005](../errorcode-pasteboard.md#12900005-request-timeout) | Excessive processing time for internal data. |

**Examples**

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: boolean = systemPasteboard.hasDataType(pasteboard.MIMETYPE_TEXT_PLAIN);
    console.info(`Succeeded in checking the DataType. Result: ${result}`);
} catch (err) {
    console.error('Failed to check the DataType. Cause:' + err.message);
};
```

## hasPasteData

```TypeScript
hasPasteData(callback: AsyncCallback<boolean>): void
```

Checks whether the system pasteboard contains data. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [hasData](#hasdata)(callback: AsyncCallback&lt;boolean&gt;)

<!--Device-SystemPasteboard-hasPasteData(callback: AsyncCallback<boolean>): void--><!--Device-SystemPasteboard-hasPasteData(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-asynccallback-t.md)&lt;boolean&gt; | Yes | Callback used to return the result. Returns **true** if the system pasteboard contains data; returns **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.hasPasteData((err: BusinessError, data: boolean) => {
    if (err) {
        console.error(`Failed to check the PasteData. Cause: ${err.message}`);
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
    console.error(`Failed to check the PasteData. Cause: ${err.message}`);
});
```

## hasRemoteData

```TypeScript
hasRemoteData(): boolean
```

Checks whether the PasteData is on a remote device. Transferring data across devices takes time. If the PasteData is in a remote device, do not check for custom data types or read the PasteData on the UI thread.

**Since:** 24

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-SystemPasteboard-hasRemoteData(): boolean--><!--Device-SystemPasteboard-hasRemoteData(): boolean-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns the check result. The value **true** indicates that the PasteData is in a remote device, and **false** indicates the opposite. Default value: **false**. |

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

Checks whether the data in the pasteboard is from another device.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SystemPasteboard-isRemoteData(): boolean--><!--Device-SystemPasteboard-isRemoteData(): boolean-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the data in the pasteboard is from another device; returns **false** otherwise. |

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
    console.error('Failed to check the RemoteData. Cause:' + err.message);
};
```

## offRemoteUpdate

```TypeScript
offRemoteUpdate(callback?: UpdateCallback): void
```

Remove a callback invoked when remote pasteboard content changes.

**Since:** 23

<!--Device-SystemPasteboard-offRemoteUpdate(callback?: UpdateCallback): void--><!--Device-SystemPasteboard-offRemoteUpdate(callback?: UpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [UpdateCallback](arkts-basicservices-pasteboard-updatecallback-t.md) | No | the callback to remove. If this parameter is not filled in, it indicates that all callbacks for this application will be cleared. Otherwise, it indicates that the specified callback will be cleared. |

**Examples**

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let listener = () => {
    console.info('The remote pasteboard has changed.');
};
systemPasteboard.offRemoteUpdate(listener);
```

## offUpdate

```TypeScript
offUpdate(callback?: UpdateCallback): void
```

Remove a callback invoked when pasteboard content changes.

**Since:** 23

<!--Device-SystemPasteboard-offUpdate(callback?: UpdateCallback): void--><!--Device-SystemPasteboard-offUpdate(callback?: UpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [UpdateCallback](arkts-basicservices-pasteboard-updatecallback-t.md) | No | the callback to remove. If this parameter is not filled in, it indicates that all callbacks for this application will be cleared. Otherwise, it indicates that the specified callback will be cleared. <br>Default value: Clear all callbacks of this application. |

## off('update')

```TypeScript
off(type: 'update', callback?: () => void): void
```

Unsubscribes the content change event of the system pasteboard.

**Since:** 7

<!--Device-SystemPasteboard-off(type: 'update', callback?: () => void): void--><!--Device-SystemPasteboard-off(type: 'update', callback?: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'update' | Yes | Event type. The value **'update'** indicates changes in the pasteboard content. |
| callback | () =&gt; void | No | the callback to remove. If this parameter is not filled in, it indicates that all callbacks for this application will be cleared. Otherwise, it indicates that the specified callback will be cleared. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Examples**

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let listener = () => {
    console.info('The system pasteboard has changed.');
};
systemPasteboard.off('update', listener);
```

## onRemoteUpdate

```TypeScript
onRemoteUpdate(callback: UpdateCallback): void
```

Add a callback invoked when remote pasteboard content changes.

**Since:** 23

<!--Device-SystemPasteboard-onRemoteUpdate(callback: UpdateCallback): void--><!--Device-SystemPasteboard-onRemoteUpdate(callback: UpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [UpdateCallback](arkts-basicservices-pasteboard-updatecallback-t.md) | Yes | the callback to add. |

**Examples**

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let listener = () => {
    console.info('The remote pasteboard has changed.');
};
systemPasteboard.onRemoteUpdate(listener);
```

## onUpdate

```TypeScript
onUpdate(callback: UpdateCallback): void
```

Add a callback invoked when pasteboard content changes.

**Since:** 23

<!--Device-SystemPasteboard-onUpdate(callback: UpdateCallback): void--><!--Device-SystemPasteboard-onUpdate(callback: UpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [UpdateCallback](arkts-basicservices-pasteboard-updatecallback-t.md) | Yes | the callback to add. |

## on('update')

```TypeScript
on(type: 'update', callback: () => void): void
```

Subscribes the content change event of the system pasteboard.

**Since:** 7

<!--Device-SystemPasteboard-on(type: 'update', callback: () => void): void--><!--Device-SystemPasteboard-on(type: 'update', callback: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'update' | Yes | Event type. The value **'update'** indicates changes in the pasteboard content. |
| callback | () =&gt; void | Yes | Callback invoked when the pasteboard content changes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Examples**

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let listener = () => {
    console.info('The system pasteboard has changed.');
};
systemPasteboard.on('update', listener);
```

## setData

```TypeScript
setData(data: PasteData, callback: AsyncCallback<void>): void
```

Writes a **PasteData** object to the pasteboard. This API uses an asynchronous callback to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-setData(data: PasteData, callback: AsyncCallback<void>): void--><!--Device-SystemPasteboard-setData(data: PasteData, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Yes | PasteData** object. |
| callback | [AsyncCallback](arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| [27787277](../errorcode-pasteboard.md#27787277-another-copy-or-paste-operation-in-progress) | Another copy or paste operation is in progress. |
| [27787278](../errorcode-pasteboard.md#27787278-copy-prohibited) | Replication is prohibited. |

**Examples**

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'content');
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.setData(pasteData, (err, data) => {
    if (err) {
        console.error('Failed to set PasteData. Cause: ' + err.message);
        return;
    }
    console.info('Succeeded in setting PasteData.');
});
```

## setData

```TypeScript
setData(data: PasteData): Promise<void>
```

Writes a **PasteData** object to the system pasteboard. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-setData(data: PasteData): Promise<void>--><!--Device-SystemPasteboard-setData(data: PasteData): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Yes | PasteData** object. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| [27787277](../errorcode-pasteboard.md#27787277-another-copy-or-paste-operation-in-progress) | Another copy or paste operation is in progress. |
| [27787278](../errorcode-pasteboard.md#27787278-copy-prohibited) | Replication is prohibited. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'content');
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.setData(pasteData).then((data: void) => {
    console.info('Succeeded in setting PasteData.');
}).catch((err: BusinessError) => {
    console.error('Failed to set PasteData. Cause: ' + err.message);
});
```

## setDataSync

```TypeScript
setDataSync(data: PasteData): void
```

Writes data to the system system pasteboard. This API returns the result synchronously.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SystemPasteboard-setDataSync(data: PasteData): void--><!--Device-SystemPasteboard-setDataSync(data: PasteData): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Yes | Data to be written to the pasteboard. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| [12900005](../errorcode-pasteboard.md#12900005-request-timeout) | Excessive processing time for internal data. |

**Examples**

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    systemPasteboard.setDataSync(pasteData);
    console.info('Succeeded in setting PasteData.');
} catch (err) {
    console.error('Failed to set PasteData. Cause:' + err.message);
};
```

## setPasteData

```TypeScript
setPasteData(data: PasteData, callback: AsyncCallback<void>): void
```

Writes a **PasteData** object to the system pasteboard. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [setData](#setdata)(data: PasteData, callback: AsyncCallback&lt;void&gt;)

<!--Device-SystemPasteboard-setPasteData(data: PasteData, callback: AsyncCallback<void>): void--><!--Device-SystemPasteboard-setPasteData(data: PasteData, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Yes | PasteData** object. |
| callback | [AsyncCallback](arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Examples**

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('content');
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.setPasteData(pasteData, (err, data) => {
    if (err) {
        console.error('Failed to set PasteData. Cause: ' + err.message);
        return;
    }
    console.info('Succeeded in setting PasteData.');
});
```

## setPasteData

```TypeScript
setPasteData(data: PasteData): Promise<void>
```

Writes a **PasteData** object to the system pasteboard. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [setData](#setdata)(data: PasteData)

<!--Device-SystemPasteboard-setPasteData(data: PasteData): Promise<void>--><!--Device-SystemPasteboard-setPasteData(data: PasteData): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Yes | PasteData** object. |

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
    console.error('Failed to set PasteData. Cause: ' + err.message);
});
```

## setUnifiedData

```TypeScript
setUnifiedData(data: unifiedDataChannel.UnifiedData): Promise<void>
```

Writes a **PasteData** object to the system pasteboard. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SystemPasteboard-setUnifiedData(data: unifiedDataChannel.UnifiedData): Promise<void>--><!--Device-SystemPasteboard-setUnifiedData(data: unifiedDataChannel.UnifiedData): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | unifiedDataChannel.UnifiedData | Yes | Data to be written to the pasteboard. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| [27787277](../errorcode-pasteboard.md#27787277-another-copy-or-paste-operation-in-progress) | Another copy or paste operation is in progress. |
| [27787278](../errorcode-pasteboard.md#27787278-copy-prohibited) | Replication is prohibited. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { unifiedDataChannel, uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let plainText : uniformDataStruct.PlainText = {
    uniformDataType: uniformTypeDescriptor.UniformDataType.PLAIN_TEXT,
    textContent : 'PLAINTEXT_CONTENT',
    abstract : 'PLAINTEXT_ABSTRACT',
}
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
let data = new unifiedDataChannel.UnifiedData();
data.addRecord(record);

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.setUnifiedData(data).then((data: void) => {
    console.info('Succeeded in setting UnifiedData.');
}).catch((err: BusinessError) => {
    console.error('Failed to setUnifiedData. Cause: ' + err.message);
});
```

## setUnifiedDataSync

```TypeScript
setUnifiedDataSync(data: unifiedDataChannel.UnifiedData): void
```

Writes data to the system pasteboard. This API returns the result synchronously.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SystemPasteboard-setUnifiedDataSync(data: unifiedDataChannel.UnifiedData): void--><!--Device-SystemPasteboard-setUnifiedDataSync(data: unifiedDataChannel.UnifiedData): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | unifiedDataChannel.UnifiedData | Yes | Data to be written to the pasteboard. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| [12900005](../errorcode-pasteboard.md#12900005-request-timeout) | Excessive processing time for internal data. |

**Examples**

```TypeScript
import { unifiedDataChannel } from '@kit.ArkData';

let plainTextData = new unifiedDataChannel.UnifiedData();
let plainText = new unifiedDataChannel.PlainText();
plainText.details = {
    Key: 'delayPlaintext',
    Value: 'delayPlaintext',
};
plainText.textContent = 'delayTextContent';
plainText.abstract = 'delayTextContent';
plainTextData.addRecord(plainText);

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    systemPasteboard.setUnifiedDataSync(plainTextData);
    console.info('Succeeded in setting UnifiedData.');
} catch (err) {
    console.error('Failed to set UnifiedData. Cause:' + err.message);
};
```

