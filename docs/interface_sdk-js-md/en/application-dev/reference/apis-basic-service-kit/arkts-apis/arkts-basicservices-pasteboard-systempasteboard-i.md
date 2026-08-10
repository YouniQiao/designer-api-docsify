# SystemPasteboard

系统剪贴板对象。在调用SystemPasteboard的接口前，需要先通过[getSystemPasteboard](arkts-basicservices-pasteboard-getsystempasteboard-f.md#getsystempasteboard)获取系统剪贴板。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-pasteboard-interface SystemPasteboard--><!--Device-pasteboard-interface SystemPasteboard-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## Modules to Import

```TypeScript
import { pasteboard } from 'kits/@kit.BasicServicesKit';
```

## clear

```TypeScript
clear(callback: AsyncCallback<void>): void
```

清空系统剪贴板内容，使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [pasteboard.SystemPasteboard.clearData](arkts-basicservices-pasteboard-systempasteboard-i.md#cleardata)(callback:

<!--Device-SystemPasteboard-clear(callback: AsyncCallback<void>): void--><!--Device-SystemPasteboard-clear(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当成功清空时，err为undefined；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

## Examples

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

清空系统剪贴板内容，使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [pasteboard.SystemPasteboard.clearData](arkts-basicservices-pasteboard-systempasteboard-i.md#cleardata)()

<!--Device-SystemPasteboard-clear(): Promise<void>--><!--Device-SystemPasteboard-clear(): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

## Examples

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

清空系统剪贴板内容，使用callback异步回调。调用此方法后，系统将删除剪贴板中的所有数据，触发已注册的'update'监听回调。清空成功后，剪贴板中将没有任何数据，hasData方法将返回false。适用于需要异步清空剪贴板且不阻塞主线程的场景，如UI响应优先的交互流程。与同步接口[clearDataSync](arkts-basicservices-pasteboard-systempasteboard-i.md#cleardatasync)不同，此接口不会阻塞UI线程，更适合在UI交互中使用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-clearData(callback: AsyncCallback<void>): void--><!--Device-SystemPasteboard-clearData(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当成功清空时，err为undefined；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

## Examples

```TypeScript
// Obtain the SystemPasteboard object.
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
// Clear the system pasteboard content.
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

清空系统剪贴板内容，使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-clearData(): Promise<void>--><!--Device-SystemPasteboard-clearData(): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

## Examples

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

清空系统剪贴板内容，此接口为同步接口。适用于需要在关键业务流程中同步清空剪贴板数据，或需要立即确认清空结果的场景。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-clearDataSync(): void--><!--Device-SystemPasteboard-clearDataSync(): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12900005 | Excessive processing time for internal data. |

## Examples

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    systemPasteboard.clearDataSync();
    console.info('Succeeded in clearing the pasteboard.');
} catch (err) {
    console.error('Failed to clear the pasteboard. Cause: ' + err.message);
};
```

## detectPatterns

```TypeScript
detectPatterns(patterns: Array<Pattern>): Promise<Array<Pattern>>
```

检测**本地**剪贴板中存在的[Pattern](arkts-basicservices-pasteboard-pattern-e.md)模式，使用Promise异步回调。本地剪贴板指当前设备上的剪贴板数据，不包括跨设备传输的远端剪贴板数据。适用于应用在粘贴数据前需要检测剪贴板内容是否包含特定类型的数据(如URL、邮箱、电话号码等)，以便进行相应处理或提供智能提示的场景。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-SystemPasteboard-detectPatterns(patterns: Array<Pattern>): Promise<Array<Pattern>>--><!--Device-SystemPasteboard-detectPatterns(patterns: Array<Pattern>): Promise<Array<Pattern>>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| patterns | Array&lt;Pattern&gt; | Yes | 需要在剪贴板中检测的模式，用于检查剪贴板数据是否符合特定格式。 可选值包括：URL(URL类型)、NUMBER(数字类型)、EMAIL_ADDRESS(邮箱地址类型)等。 取值范围：数组元素数量不限，元素值只能为Pattern枚举值。传入无效值时返回错误码401。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;Pattern&gt;&gt; | Promise对象，返回检测到的模式。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

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

ArkTS-Dyn:
```TypeScript
getChangeCount(): number
```

ArkTS-Sta:
```TypeScript
getChangeCount(): long
```

获取剪贴板内容的变化次数。执行成功时返回剪贴板内容的变化次数，否则返回0。当剪贴板内容过期或调用[clearDataSync](arkts-basicservices-pasteboard-systempasteboard-i.md#cleardatasync)等接口导致剪贴板内容为空时，内容变化次数不会因此改变。系统重启或剪贴板服务异常重启时，剪贴板内容变化次数重新从0开始计数。对同一内容连续多次复制会被记录为多次更改，每次复制均会导致内容变化次数增加。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SystemPasteboard-getChangeCount(): long--><!--Device-SystemPasteboard-getChangeCount(): long-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 返回读取到的剪贴板内容变化次数。 |

## Examples

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

读取系统剪贴板内容，使用callback异步回调。将剪贴板数据封装为PasteData对象返回。调用此方法后，系统将从剪贴板服务读取当前内容，通过callback返回PasteData对象。读取成功后，应用可以通过PasteData对象的方法获取具体的数据内容（如文本、HTML、URI等）。适用于需要异步读取剪贴板内容的场景，如UI响应优先、避免阻塞主线程。与[getDataSync](arkts-basicservices-pasteboard-systempasteboard-i.md#getdatasync)相比，getData不会阻塞UI线程，适合处理大量数据或远端数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 12+: ohos.permission.READ_PASTEBOARD

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-getData(callback: AsyncCallback<PasteData>): void--><!--Device-SystemPasteboard-getData(callback: AsyncCallback<PasteData>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;PasteData&gt; | Yes | 回调函数。当读取成功，err为undefined，data为返回的系统剪贴板数据；否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 27787277 | Another copy or paste operation is in progress. |
| 201 | Permission verification failed. The application does not have the permission required to call the API.<br>**Applicable version:** 12 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the SystemPasteboard object.
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
// Read the system clipboard content.
systemPasteboard.getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
    if (err) {
        console.error('Failed to get PasteData. Cause: ' + err.message);
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

读取系统剪贴板内容，将剪贴板数据封装为PasteData对象返回，使用Promise异步回调。适用于需要异步读取剪贴板内容的场景，如UI响应优先、避免阻塞主线程。适用于应用需要使用标准化数据结构[UnifiedData](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-unifieddata-c.md/arkts-arkdata-unifieddatachannel-unifieddata-c.md)读取剪贴板数据的场景。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 12+: ohos.permission.READ_PASTEBOARD

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-getData(): Promise<PasteData>--><!--Device-SystemPasteboard-getData(): Promise<PasteData>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PasteData&gt; | Promise对象，返回系统剪贴板数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 27787277 | Another copy or paste operation is in progress. |
| 201 | Permission verification failed. The application does not have the permission required to call the API.<br>**Applicable version:** 12 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the SystemPasteboard object.
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
// Read the system clipboard content.
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    // Obtain the plain text content from the pasteboard.
    let text: string = pasteData.getPrimaryText();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});
```

## getDataSource

```TypeScript
getDataSource(): string
```

获取剪贴板数据的来源应用名称。适用于安全审计、数据追踪或向用户提示数据来源等场景。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-getDataSource(): string--><!--Device-SystemPasteboard-getDataSource(): string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| string | 数据来源的应用名称。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12900005 | Excessive processing time for internal data. |

## Examples

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: string = systemPasteboard.getDataSource();
    console.info(`Succeeded in getting DataSource. Result: ${result}`);
} catch (err) { 
    console.error('Failed to get DataSource. Cause: ' + err.message);
};
```

## getDataSync

```TypeScript
getDataSync(): PasteData
```

读取系统剪贴板内容，此接口为同步接口。适用于应用需要在关键业务流程中同步获取剪贴板数据，或需要立即处理剪贴板内容的场景。避免在UI线程调用此接口，以免阻塞界面；处理大量数据或远端数据时，建议使用异步接口[getData](arkts-basicservices-pasteboard-pastedatarecord-i.md#getdata)。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 12+: ohos.permission.READ_PASTEBOARD

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-getDataSync(): PasteData--><!--Device-SystemPasteboard-getDataSync(): PasteData-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | 返回系统剪贴板数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12900005 | Excessive processing time for internal data. |
| 201 | Permission verification failed. The application does not have the permission required to call the API.<br>**Applicable version:** 12 and later |

## Examples

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

获取剪贴板的内容和进度，使用Promise异步回调，不支持对文件夹的拷贝。对于大文件拷贝操作，建议设置进度监听以跟踪拷贝进度，避免在UI线程长时间等待；建议合理设置目标路径以确保有足够的存储空间。适用于大文件粘贴场景。在此场景下，可通过此回调显示拷贝进度，或监听拷贝过程以便在必要时取消操作。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.READ_PASTEBOARD

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-SystemPasteboard-getDataWithProgress(params: GetDataParams): Promise<PasteData>--><!--Device-SystemPasteboard-getDataWithProgress(params: GetDataParams): Promise<PasteData>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [GetDataParams](arkts-basicservices-pasteboard-getdataparams-i.md) | Yes | 应用在使用剪贴板提供的文件拷贝能力的情况下需要的参数，包含目标路径、文件冲突选项、进度条类型等。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PasteData&gt; | Promise对象，返回系统剪贴板数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. |
| 12900007 | Invalid destUri or file system error. |
| 12900003 | Another copy or paste operation is in progress. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 12900008 | Failed to start progress. |
| 12900009 | Progress exits abnormally. |
| 12900010 | System error occurred during paste execution. |

## Examples

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

读取剪贴板中存在的MIME类型，使用Promise异步回调。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-SystemPasteboard-getMimeTypes(): Promise<Array<string>>--><!--Device-SystemPasteboard-getMimeTypes(): Promise<Array<string>>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | Promise对象，返回读取到的MIME类型。 |

## Examples

```TypeScript
import { pasteboard, BusinessError } from '@kit.BasicServicesKit'

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getMimeTypes().then((data: Array<string>) => {
    console.info('Succeeded in getting mimeTypes. mimeTypes: ' + data.sort().join(','));
}).catch((err: BusinessError) => {
    console.error('Failed to get mimeTypes. Cause: ' + err.message);
});
```

## getPasteData

```TypeScript
getPasteData(callback: AsyncCallback<PasteData>): void
```

读取系统剪贴板内容，使用callback异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [pasteboard.SystemPasteboard.getData](arkts-basicservices-pasteboard-systempasteboard-i.md#getdata)(callback:

<!--Device-SystemPasteboard-getPasteData(callback: AsyncCallback<PasteData>): void--><!--Device-SystemPasteboard-getPasteData(callback: AsyncCallback<PasteData>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;PasteData&gt; | Yes | 回调函数。当读取成功，err为undefined，data为返回的系统剪贴板数据；否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the SystemPasteboard object.
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
// Read the system clipboard content.
systemPasteboard.getPasteData((err: BusinessError, pasteData: pasteboard.PasteData) => {
    if (err) {
        console.error('Failed to get PasteData. Cause: ' + err.message);
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

读取系统剪贴板内容，使用Promise异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [pasteboard.SystemPasteboard.getData](arkts-basicservices-pasteboard-systempasteboard-i.md#getdata)()

<!--Device-SystemPasteboard-getPasteData(): Promise<PasteData>--><!--Device-SystemPasteboard-getPasteData(): Promise<PasteData>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PasteData&gt; | Promise对象，返回系统剪贴板数据。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the SystemPasteboard object.
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
// Read the system clipboard content.
systemPasteboard.getPasteData().then((pasteData: pasteboard.PasteData) => {
    // Obtain the plain text content from the pasteboard.
    let text: string = pasteData.getPrimaryText();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});
```

## getUnifiedData

```TypeScript
getUnifiedData(): Promise<unifiedDataChannel.UnifiedData>
```

读取系统剪贴板内容，使用Promise异步回调。适用于需要使用标准化数据结构[UnifiedData](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-unifieddata-c.md/arkts-arkdata-unifieddatachannel-unifieddata-c.md)进行跨应用数据交换的场景。当应用需要与其他支持UnifiedData的应用进行数据共享，或需要处理复杂的多类型数据时，使用本接口。与[getData](arkts-basicservices-pasteboard-systempasteboard-i.md#getdata)相比，getUnifiedData提供了更标准化的数据格式。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.READ_PASTEBOARD

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SystemPasteboard-getUnifiedData(): Promise<unifiedDataChannel.UnifiedData>--><!--Device-SystemPasteboard-getUnifiedData(): Promise<unifiedDataChannel.UnifiedData>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;unifiedDataChannel.UnifiedData&gt; | Promise对象，返回系统剪贴板数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 27787277 | Another copy or paste operation is in progress. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

## Examples

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

读取系统剪贴板内容，此接口为同步接口。适用于需要同步使用标准化数据结构UnifiedData进行跨应用数据交换的场景。当应用需要在关键业务流程中立即获取剪贴板数据，且需要与其他支持UnifiedData的应用进行数据共享时使用。由于获取剪贴板中数据的时延受数据量大小与网络环境的影响，调用此接口可能耗时较长，建议开发者在非UI线程调用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.READ_PASTEBOARD

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SystemPasteboard-getUnifiedDataSync(): unifiedDataChannel.UnifiedData--><!--Device-SystemPasteboard-getUnifiedDataSync(): unifiedDataChannel.UnifiedData-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| unifiedDataChannel.UnifiedData | 返回系统剪贴板数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12900005 | Excessive processing time for internal data. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

## Examples

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

判断系统剪贴板中是否有内容，使用callback异步回调。适用于需要异步判断剪贴板是否有内容且不阻塞主线程的场景，如UI响应优先的交互流程。与同步接口[hasDataSync](arkts-basicservices-pasteboard-systempasteboard-i.md#hasdatasync)不同，此接口不会阻塞UI线程，更适合在UI交互中调用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-hasData(callback: AsyncCallback<boolean>): void--><!--Device-SystemPasteboard-hasData(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | 回调函数，用于接收剪贴板是否有内容的判断结果。返回true表示系统剪贴板中有内容，返回false表示系统剪贴板中没有内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

## Examples

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

判断系统剪贴板中是否有内容，使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-hasData(): Promise<boolean>--><!--Device-SystemPasteboard-hasData(): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | 返回true表示系统剪贴板中有内容，返回false表示系统剪贴板中没有内容。 |

## Examples

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

判断系统剪贴板中是否有内容，此接口为同步接口。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-hasDataSync(): boolean--><!--Device-SystemPasteboard-hasDataSync(): boolean-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回true表示系统剪贴板中有内容，返回false表示系统剪贴板中没有内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12900005 | Excessive processing time for internal data. |

## Examples

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: boolean = systemPasteboard.hasDataSync();
    console.info(`Succeeded in checking the PasteData. Result: ${result}`);
} catch (err) {
    console.error('Failed to check the PasteData. Cause: ' + err.message);
};
```

## hasDataType

```TypeScript
hasDataType(mimeType: string): boolean
```

检查剪贴板内容中是否有指定类型的数据。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-hasDataType(mimeType: string): boolean--><!--Device-SystemPasteboard-hasDataType(mimeType: string): boolean-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mimeType | string | Yes | 数据类型，设置后用于检查剪贴板内容中是否存在该类型的特定数据。其长度不能超过1024字节，超出范围时返回错误码401。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 检查剪贴板内容中是否有指定类型的数据。剪贴板内容中有指定类型的数据返回true；剪贴板内容中没有指定类型的数据返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 12900005 | Excessive processing time for internal data. |

## Examples

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: boolean = systemPasteboard.hasDataType(pasteboard.MIMETYPE_TEXT_PLAIN);
    console.info(`Succeeded in checking the DataType. Result: ${result}`);
} catch (err) {
    console.error('Failed to check the DataType. Cause: ' + err.message);
};
```

## hasPasteData

```TypeScript
hasPasteData(callback: AsyncCallback<boolean>): void
```

判断系统剪贴板中是否有内容，使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [pasteboard.SystemPasteboard.hasData](arkts-basicservices-pasteboard-systempasteboard-i.md#hasdata)(callback:

<!--Device-SystemPasteboard-hasPasteData(callback: AsyncCallback<boolean>): void--><!--Device-SystemPasteboard-hasPasteData(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | 返回true表示系统剪贴板中有内容，返回false表示系统剪贴板中没有内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

## Examples

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

判断系统剪贴板中是否有内容，使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [pasteboard.SystemPasteboard.hasData](arkts-basicservices-pasteboard-systempasteboard-i.md#hasdata)()

<!--Device-SystemPasteboard-hasPasteData(): Promise<boolean>--><!--Device-SystemPasteboard-hasPasteData(): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | 返回true表示系统剪贴板中有内容，返回false表示系统剪贴板中没有内容。 |

## Examples

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

判断剪贴板数据是否在远端设备上。由于数据跨端传输耗时较大，如果剪贴板数据在远端设备上，不建议在UI线程执行检查剪贴板数据中是否包含自定义数据类型，或读取剪贴板数据。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-SystemPasteboard-hasRemoteData(): boolean--><!--Device-SystemPasteboard-hasRemoteData(): boolean-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回指示剪贴板数据是否在远端设备上的结果。true表示剪贴板数据在远端设备上；false表示剪贴板数据不在远端设备上。默认为false。 |

## Examples

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();

let result: boolean = systemPasteboard.hasRemoteData();
console.info(`Succeeded in checking the remote data. Result: ${result}`);
```

## isRemoteData

```TypeScript
isRemoteData(): boolean
```

判断剪贴板中的数据是否来自其他设备。由于数据跨端传输耗时较大，如果剪贴板数据在远端设备上，不建议在UI线程执行检查剪贴板数据中是否包含自定义数据类型，或读取剪贴板数据。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-isRemoteData(): boolean--><!--Device-SystemPasteboard-isRemoteData(): boolean-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 判断剪贴板中的数据是否来自其他设备。剪贴板数据来自其他设备返回true；剪贴板数据来自本设备返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12900005 | Excessive processing time for internal data. |

## Examples

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: boolean = systemPasteboard.isRemoteData();
    console.info(`Succeeded in checking the RemoteData. Result: ${result}`);
} catch (err) {
    console.error('Failed to check the RemoteData. Cause: ' + err.message);
};
```

## off('update')

```TypeScript
off(type: 'update', callback?: () => void): void
```

取消订阅系统剪贴板内容变化事件。

- 与on('update')方法配合使用，取消订阅的是通过on('update')订阅的事件监听。  
- 必须在已订阅的情况下才能调用。  
- 如果callback参数未填，清除本应用的所有监听回调；否则清除指定监听回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-SystemPasteboard-off(type: 'update', callback?: () => void): void--><!--Device-SystemPasteboard-off(type: 'update', callback?: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'update' | Yes | 取值为'update'，表示系统剪贴板内容变化事件。 |
| callback | () =&gt; void | No | 剪贴板中内容变化时触发的用户程序的回调。如果此参数未填，表明清除本应用的所有监听回调，否则表示清除指定监听回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

## Examples

```TypeScript
// Obtain the SystemPasteboard object.
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
// Define a callback to be invoked when the pasteboard content changes.
let listener = () => {
    console.info('The system pasteboard has changed.');
};
// Subscribe to the pasteboard content change event.
systemPasteboard.off('update', listener);
```

## offRemoteUpdate

```TypeScript
offRemoteUpdate(callback?: UpdateCallback): void
```

取消订阅跨设备剪贴板内容变化事件。

- 与onRemoteUpdate()方法配合使用，取消订阅的是通过onRemoteUpdate()订阅的事件监听。  
- 必须在已订阅的情况下才能调用。  
- 如果callback参数未填，清除本应用的所有远端监听回调；否则清除指定远端监听回调。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-SystemPasteboard-offRemoteUpdate(callback?: UpdateCallback): void--><!--Device-SystemPasteboard-offRemoteUpdate(callback?: UpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [UpdateCallback](arkts-basicservices-pasteboard-updatecallback-t.md) | No | 远端设备剪贴板中内容变化时触发的用户程序的回调。如果此参数未填，表明清除本应用的所有远端监听回调，否则表示清除指定远端监听回调。 |

## Examples

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

取消订阅系统剪贴板内容变化事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SystemPasteboard-offUpdate(callback?: UpdateCallback): void--><!--Device-SystemPasteboard-offUpdate(callback?: UpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [UpdateCallback](arkts-basicservices-pasteboard-updatecallback-t.md) | No | 剪贴板中内容变化时触发的用户程序的回调。如果此参数未填，表明清除本应用的所有监听回调，否则表示清除指定监听回调。 |

## on('update')

```TypeScript
on(type: 'update', callback: () => void): void
```

订阅系统剪贴板内容变化事件，当系统剪贴板中内容变化时触发用户程序的回调。调用此方法后，系统将在剪贴板服务中注册监听器，剪贴板内容被写入、清空或修改时触发回调。可注册多个监听器，需在适当时机调用off取消监听以释放资源。当应用需要实时响应剪贴板内容变化时使用，如自动检测剪贴板中的特定格式数据、实现智能粘贴建议等场景。

- 订阅后必须在不再需要监听时调用[off('update')](pasteboard.SystemPasteboard.off(type: 'update', callback?: () => void))取消订阅。  
- 未取消订阅会导致回调函数持续监听剪贴板变化，可能造成内存泄漏或多次回调触发。  
- 建议在组件/页面销毁时取消订阅。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-SystemPasteboard-on(type: 'update', callback: () => void): void--><!--Device-SystemPasteboard-on(type: 'update', callback: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'update' | Yes | 取值为'update'，表示系统剪贴板内容变化事件，其他值无效。 |
| callback | () =&gt; void | Yes | 剪贴板中内容变化时触发的用户程序的回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

## Examples

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

订阅跨设备剪贴板内容变化事件，当远端设备系统剪贴板中内容变化时触发用户程序的回调。

- 订阅后必须在不再需要监听时调用  
[offRemoteUpdate](pasteboard.SystemPasteboard.offRemoteUpdate(callback?: UpdateCallback))取消订阅。  
- 未取消订阅会导致回调函数持续监听远端变化，造成内存泄漏。  
- 建议在组件/页面销毁时取消订阅。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-SystemPasteboard-onRemoteUpdate(callback: UpdateCallback): void--><!--Device-SystemPasteboard-onRemoteUpdate(callback: UpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [UpdateCallback](arkts-basicservices-pasteboard-updatecallback-t.md) | Yes | 剪贴板中内容变化时触发的用户程序的回调，无参数。用于监听跨设备剪贴板内容更新事件，当远端设备剪贴板内容发生变化时触发此回调。 |

## Examples

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

订阅系统剪贴板内容变化事件，当系统剪贴板中内容变化时触发用户程序的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SystemPasteboard-onUpdate(callback: UpdateCallback): void--><!--Device-SystemPasteboard-onUpdate(callback: UpdateCallback): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [UpdateCallback](arkts-basicservices-pasteboard-updatecallback-t.md) | Yes | 剪贴板中内容变化时触发的用户程序的回调。 |

## removeAppShareOptions

```TypeScript
removeAppShareOptions(): void
```

删除应用全局的可粘贴的范围。适用于应用需要取消之前设置的粘贴范围限制，恢复剪贴板数据默认粘贴范围的场景。

- 与setAppShareOptions()方法（应用设置本应用剪贴板数据的可粘贴范围）配合使用。  
- 删除的是通过setAppShareOptions()设置的分享范围。  
- 必须在已设置分享范围的情况下才能调用。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 14+: ohos.permission.MANAGE_PASTEBOARD_APP_SHARE_OPTION

<!--Device-SystemPasteboard-removeAppShareOptions(): void--><!--Device-SystemPasteboard-removeAppShareOptions(): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API.<br>**Applicable version:** 14 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 - 13 |

## Examples

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

应用设置本应用剪贴板数据的可粘贴范围。适用于应用需要全局限制本应用产生的剪贴板数据的粘贴范围，如金融类应用需要保护用户敏感信息的场景。

- 与removeAppShareOptions()方法（删除应用全局的可粘贴的范围）配合使用。  
- 需要删除已设置的分享范围时，调用removeAppShareOptions()。  
- 在何处设置就在何处删除，确保分享范围设置和删除的一致性。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 14+: ohos.permission.MANAGE_PASTEBOARD_APP_SHARE_OPTION

<!--Device-SystemPasteboard-setAppShareOptions(shareOptions: ShareOption): void--><!--Device-SystemPasteboard-setAppShareOptions(shareOptions: ShareOption): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| shareOptions | [ShareOption](arkts-basicservices-pasteboard-shareoption-e.md) | Yes | 可粘贴的范围，参数只允许pasteboard.ShareOption.INAPP。传入其他值时返回错误码401。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12900006 | Settings already exist. |
| 201 | Permission verification failed. The application does not have the permission required to call the API.<br>**Applicable version:** 14 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 - 13 |

## Examples

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

将数据写入系统剪贴板，使用callback异步回调。调用此方法后，系统会将PasteData对象写入到系统剪贴板中。写入成功后，其他应用可以读取该剪贴板数据。写入的数据会替换剪贴板中已有的内容。适用于需要异步写入剪贴板内容的场景，如UI响应优先、避免阻塞主线程。与[setDataSync](arkts-basicservices-pasteboard-systempasteboard-i.md#setdatasync)相比，setData不会阻塞UI线程。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-setData(data: PasteData, callback: AsyncCallback<void>): void--><!--Device-SystemPasteboard-setData(data: PasteData, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Yes | PasteData对象，设置后会将该数据写入系统剪贴板，供应用读取和粘贴使用。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当写入成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 27787277 | Another copy or paste operation is in progress. |
| 27787278 | Replication is prohibited. |

## Examples

```TypeScript
// Create a PasteData object of the plain text type.
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'content');
// Obtain the SystemPasteboard object.
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
// Write data to the system pasteboard.
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

将数据写入系统剪贴板，使用Promise异步回调。适用于需要异步写入剪贴板且不阻塞主线程的场景，如UI响应优先的交互流程。与同步接口[setDataSync](arkts-basicservices-pasteboard-systempasteboard-i.md#setdatasync)不同，此接口不会阻塞UI线程，更适合在UI交互中调用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-setData(data: PasteData): Promise<void>--><!--Device-SystemPasteboard-setData(data: PasteData): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Yes | PasteData对象。调用本接口前，需确保无其他拷贝或粘贴操作正在进行。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 27787277 | Another copy or paste operation is in progress. |
| 27787278 | Replication is prohibited. |

## Examples

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
    console.error('Failed to set PasteData. Cause: ' + err.message);
});
```

## setDataSync

```TypeScript
setDataSync(data: PasteData): void
```

将数据写入系统剪贴板，此接口为同步接口。适用于应用需要在关键业务流程中同步完成剪贴板数据写入，或需要立即确认写入结果的场景。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemPasteboard-setDataSync(data: PasteData): void--><!--Device-SystemPasteboard-setDataSync(data: PasteData): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Yes | 需要写入剪贴板中的数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 12900005 | Excessive processing time for internal data. |

## Examples

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

将数据写入系统剪贴板，使用callback异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [pasteboard.SystemPasteboard.setData](arkts-basicservices-pasteboard-systempasteboard-i.md#setdata)(data:

<!--Device-SystemPasteboard-setPasteData(data: PasteData, callback: AsyncCallback<void>): void--><!--Device-SystemPasteboard-setPasteData(data: PasteData, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Yes | PasteData对象。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当写入成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

## Examples

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

将数据写入系统剪贴板，使用Promise异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [pasteboard.SystemPasteboard.setData](arkts-basicservices-pasteboard-systempasteboard-i.md#setdata)(data:

<!--Device-SystemPasteboard-setPasteData(data: PasteData): Promise<void>--><!--Device-SystemPasteboard-setPasteData(data: PasteData): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | Yes | PasteData对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

## Examples

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

将数据写入系统剪贴板，使用Promise异步回调。适用于需要异步写入剪贴板且不阻塞主线程的场景，如UI响应优先的交互流程。与同步接口[setUnifiedDataSync](arkts-basicservices-pasteboard-systempasteboard-i.md#setunifieddatasync)不同，此接口不会阻塞UI线程，更适合在UI交互中调用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SystemPasteboard-setUnifiedData(data: unifiedDataChannel.UnifiedData): Promise<void>--><!--Device-SystemPasteboard-setUnifiedData(data: unifiedDataChannel.UnifiedData): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | unifiedDataChannel.UnifiedData | Yes | 需要写入剪贴板中的数据。调用本接口前，需确保无其他拷贝或粘贴操作正在进行。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 27787277 | Another copy or paste operation is in progress. |
| 27787278 | Replication is prohibited. |

## Examples

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
    console.error('Failed to setUnifiedData. Cause: ' + err.message);
});
```

## setUnifiedDataSync

```TypeScript
setUnifiedDataSync(data: unifiedDataChannel.UnifiedData): void
```

将数据写入系统剪贴板，此接口为同步接口。适用于需要同步使用标准化数据结构UnifiedData进行跨应用数据交换的场景。当应用需要在关键业务流程中立即写入剪贴板数据，且需要与其他支持[UnifiedData](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-unifieddata-c.md/arkts-arkdata-unifieddatachannel-unifieddata-c.md)的应用进行数据共享时使用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SystemPasteboard-setUnifiedDataSync(data: unifiedDataChannel.UnifiedData): void--><!--Device-SystemPasteboard-setUnifiedDataSync(data: unifiedDataChannel.UnifiedData): void-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | unifiedDataChannel.UnifiedData | Yes | 需要写入剪贴板中的数据内容。支持跨应用数据交换，其他应用可通过统一数据结构读取该内容。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 12900005 | Excessive processing time for internal data. |

## Examples

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
    console.error('Failed to set UnifiedData. Cause:' + err.message);
};
```

