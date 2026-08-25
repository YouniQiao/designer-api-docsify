# SystemPasteboard

Provides **SystemPasteboard** APIs. Before calling any **SystemPasteboard** API, you must obtain a **SystemPasteboard** object using [getSystemPasteboard](arkts-basicservices-pasteboard-getsystempasteboard-f.md).

**Since:** 6

**System capability:** SystemCapability.MiscServices.Pasteboard

## Modules to Import

```TypeScript
import { pasteboard } from 'kits/@kit.BasicServicesKit';
```

## clear

```TypeScript
clear(callback: AsyncCallback<void>): void
```

Clears the system pasteboard. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [clearData](#cleardata)(callback: AsyncCallback&lt;void&gt;)

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## clear

```TypeScript
clear(): Promise<void>
```

Clears the system pasteboard. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [clearData](#cleardata)()

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## clearData

```TypeScript
clearData(callback: AsyncCallback<void>): void
```

Clears the system pasteboard. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## clearData

```TypeScript
clearData(): Promise<void>
```

Clears the system pasteboard. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## clearDataSync

```TypeScript
clearDataSync(): void
```

Clears the system pasteboard. This API returns the result synchronously.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Error codes:**

| Error Code ID |
| --- |
| [12900005](../errorcode-pasteboard.md#12900005-request-timeout) |

## detectPatterns

```TypeScript
detectPatterns(patterns: Array<Pattern>): Promise<Array<Pattern>>
```

Detects [patterns](arkts-basicservices-pasteboard-pattern-e.md) in the system pasteboard. This API uses a promise to return the result.

**Since:** 13

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [patterns](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodlist-patternoptions-i.md) | Array & lt;Pattern & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;Pattern & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getChangeCount

```TypeScript
getChangeCount(): number
```

Obtains the number of pasteboard content changes. Returns the number of pasteboard content changes if this API is called successfully; returns **0** otherwise. Even though the PasteData expires, or the data becomes empty because of the called [clearDataSync](#cleardatasync) API, the number of data changes remains. When the system is restarted, or the pasteboard service is restarted due to an exception, the number of PasteData changes counts from 0. In addition, copying the same data repeatedly is considered to change the data for multiple times. Therefore, each time the data is copied, the number of data changes increases.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getData

```TypeScript
getData(callback: AsyncCallback<PasteData>): void
```

Obtains a **PasteData** object from the pasteboard. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** 
- API version 12+: ohos.permission.READ_PASTEBOARD

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[PasteData](arkts-basicservices-pasteboard-pastedata-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [27787277](../errorcode-pasteboard.md#27787277-another-copy-or-paste-operation-in-progress) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## getData

```TypeScript
getData(): Promise<PasteData>
```

Obtains a **PasteData** object from the pasteboard. This API uses a promise to return the result.

**Since:** 9

**Required permissions:** 
- API version 12+: ohos.permission.READ_PASTEBOARD

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PasteData](arkts-basicservices-pasteboard-pastedata-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [27787277](../errorcode-pasteboard.md#27787277-another-copy-or-paste-operation-in-progress) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## getDataSource

```TypeScript
getDataSource(): string
```

Obtains the name of the application that provides data.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [12900005](../errorcode-pasteboard.md#12900005-request-timeout) |

## getDataSync

```TypeScript
getDataSync(): PasteData
```

Obtains a **PasteData** object from the pasteboard. This API returns the result synchronously.

**Since:** 11

**Required permissions:** 
- API version 12+: ohos.permission.READ_PASTEBOARD

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [12900005](../errorcode-pasteboard.md#12900005-request-timeout) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## getDataWithProgress

```TypeScript
getDataWithProgress(params: GetDataParams): Promise<PasteData>
```

Obtains the PasteData from the system pasteboard with system progress. This API uses a promise to return the result. Folders cannot be copied.

**Since:** 15

**Required permissions:** ohos.permission.READ_PASTEBOARD

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| params | [GetDataParams](arkts-basicservices-pasteboard-getdataparams-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PasteData](arkts-basicservices-pasteboard-pastedata-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12900003](../errorcode-pasteboard.md#12900003-another-copy-or-paste-operation-in-progress) |
| [12900007](../errorcode-pasteboard.md#12900007-file-copying-failure) |
| [12900008](../errorcode-pasteboard.md#12900008-progress-startup-failure) |
| [12900009](../errorcode-pasteboard.md#12900009-progress-reporting-exception) |
| [12900010](../errorcode-pasteboard.md#12900010-data-obtaining-failure) |

## getMimeTypes

```TypeScript
getMimeTypes(): Promise<Array<string>>
```

Obtains the types of PasteData in the system pasteboard. This API uses a promise to return the result.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

## getPasteData

```TypeScript
getPasteData(callback: AsyncCallback<PasteData>): void
```

Obtains a **PasteData** object from the pasteboard. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getData](#getdata)(callback: AsyncCallback&lt;PasteData&gt;)

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[PasteData](arkts-basicservices-pasteboard-pastedata-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getPasteData

```TypeScript
getPasteData(): Promise<PasteData>
```

Obtains a **PasteData** object from the pasteboard. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getData](#getdata)()

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PasteData](arkts-basicservices-pasteboard-pastedata-i.md)&gt; |

## getUnifiedData

```TypeScript
getUnifiedData(): Promise<unifiedDataChannel.UnifiedData>
```

Obtains a **PasteData** object from the system pasteboard. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.READ_PASTEBOARD

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;unifiedDataChannel.UnifiedData & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [27787277](../errorcode-pasteboard.md#27787277-another-copy-or-paste-operation-in-progress) |

## getUnifiedDataSync

```TypeScript
getUnifiedDataSync(): unifiedDataChannel.UnifiedData
```

Obtains a **UnifiedData** object from the system pasteboard. This API returns the result synchronously.

**Since:** 12

**Required permissions:** ohos.permission.READ_PASTEBOARD

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| unifiedDataChannel.UnifiedData |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12900005](../errorcode-pasteboard.md#12900005-request-timeout) |

## hasData

```TypeScript
hasData(callback: AsyncCallback<boolean>): void
```

Checks whether the system pasteboard contains data. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## hasData

```TypeScript
hasData(): Promise<boolean>
```

Checks whether the system pasteboard contains data. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## hasDataSync

```TypeScript
hasDataSync(): boolean
```

Checks whether the system pasteboard contains data. This API returns the result synchronously.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [12900005](../errorcode-pasteboard.md#12900005-request-timeout) |

## hasDataType

```TypeScript
hasDataType(mimeType: string): boolean
```

Checks whether the pasteboard contains data of the specified type.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mimeType | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12900005](../errorcode-pasteboard.md#12900005-request-timeout) |

## hasPasteData

```TypeScript
hasPasteData(callback: AsyncCallback<boolean>): void
```

Checks whether the system pasteboard contains data. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [hasData](#hasdata)(callback: AsyncCallback&lt;boolean&gt;)

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## hasPasteData

```TypeScript
hasPasteData(): Promise<boolean>
```

Checks whether the system pasteboard contains data. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [hasData](#hasdata)()

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## hasRemoteData

```TypeScript
hasRemoteData(): boolean
```

Checks whether the PasteData is on a remote device. Transferring data across devices takes time. If the PasteData is in a remote device, do not check for custom data types or read the PasteData on the UI thread.

**Since:** 24

**Atomic service API:** This API can be used in atomic services since API version 24.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isRemoteData

```TypeScript
isRemoteData(): boolean
```

Checks whether the data in the pasteboard is from another device.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [12900005](../errorcode-pasteboard.md#12900005-request-timeout) |

## off('update')

```TypeScript
off(type: 'update', callback?: () => void): void
```

Unsubscribes the content change event of the system pasteboard.

**Since:** 7

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'update' | Yes |
| callback | () = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## offRemoteUpdate

```TypeScript
offRemoteUpdate(callback?: UpdateCallback): void
```

Remove a callback invoked when remote pasteboard content changes.

**Since:** 22

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [UpdateCallback](arkts-basicservices-pasteboard-updatecallback-t.md) | No |

## on('update')

```TypeScript
on(type: 'update', callback: () => void): void
```

Subscribes the content change event of the system pasteboard.

**Since:** 7

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'update' | Yes |
| callback | () = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## onRemoteUpdate

```TypeScript
onRemoteUpdate(callback: UpdateCallback): void
```

Add a callback invoked when remote pasteboard content changes.

**Since:** 22

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [UpdateCallback](arkts-basicservices-pasteboard-updatecallback-t.md) | Yes |

## removeAppShareOptions

```TypeScript
removeAppShareOptions(): void
```

Deletes the global pasteable range of the application.

**Since:** 14

**Required permissions:** 
- API version 14+: ohos.permission.MANAGE_PASTEBOARD_APP_SHARE_OPTION

**System capability:** SystemCapability.MiscServices.Pasteboard

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## setAppShareOptions

```TypeScript
setAppShareOptions(shareOptions: ShareOption): void
```

Sets pasteable range of PasteData for application.

**Since:** 14

**Required permissions:** 
- API version 14+: ohos.permission.MANAGE_PASTEBOARD_APP_SHARE_OPTION

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [shareOptions](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-unifieddataproperties-c.md) | [ShareOption](arkts-basicservices-pasteboard-shareoption-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12900006](../errorcode-pasteboard.md#12900006-settings-already-exists) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## setData

```TypeScript
setData(data: PasteData, callback: AsyncCallback<void>): void
```

Writes a **PasteData** object to the pasteboard. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [27787277](../errorcode-pasteboard.md#27787277-another-copy-or-paste-operation-in-progress) |
| [27787278](../errorcode-pasteboard.md#27787278-copy-prohibited) |

## setData

```TypeScript
setData(data: PasteData): Promise<void>
```

Writes a **PasteData** object to the system pasteboard. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [27787277](../errorcode-pasteboard.md#27787277-another-copy-or-paste-operation-in-progress) |
| [27787278](../errorcode-pasteboard.md#27787278-copy-prohibited) |

## setDataSync

```TypeScript
setDataSync(data: PasteData): void
```

Writes data to the system system pasteboard. This API returns the result synchronously.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12900005](../errorcode-pasteboard.md#12900005-request-timeout) |

## setPasteData

```TypeScript
setPasteData(data: PasteData, callback: AsyncCallback<void>): void
```

Writes a **PasteData** object to the system pasteboard. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [setData](#setdata)(data: PasteData, callback: AsyncCallback&lt;void&gt;)

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setPasteData

```TypeScript
setPasteData(data: PasteData): Promise<void>
```

Writes a **PasteData** object to the system pasteboard. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [setData](#setdata)(data: PasteData)

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setUnifiedData

```TypeScript
setUnifiedData(data: unifiedDataChannel.UnifiedData): Promise<void>
```

Writes a **PasteData** object to the system pasteboard. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | unifiedDataChannel.UnifiedData | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [27787277](../errorcode-pasteboard.md#27787277-another-copy-or-paste-operation-in-progress) |
| [27787278](../errorcode-pasteboard.md#27787278-copy-prohibited) |

## setUnifiedDataSync

```TypeScript
setUnifiedDataSync(data: unifiedDataChannel.UnifiedData): void
```

Writes data to the system pasteboard. This API returns the result synchronously.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | unifiedDataChannel.UnifiedData | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12900005](../errorcode-pasteboard.md#12900005-request-timeout) |
