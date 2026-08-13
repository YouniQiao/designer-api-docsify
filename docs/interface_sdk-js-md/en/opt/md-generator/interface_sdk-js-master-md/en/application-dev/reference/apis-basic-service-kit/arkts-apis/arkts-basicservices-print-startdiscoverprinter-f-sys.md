# startDiscoverPrinter (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## startDiscoverPrinter

```TypeScript
function startDiscoverPrinter(extensionList: Array<string>, callback: AsyncCallback<void>): void
```

Discovers printers by specifying the extension list. The discovered printers contain the specified print extension abilities. If an empty extension list is specified, all extension abilities are loaded. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** 
- API version 20+: ohos.permission.MANAGE_PRINT_JOB or ohos.permission.PRINT
- API version 10 - 19: ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function startDiscoverPrinter(extensionList: Array<string>, callback: AsyncCallback<void>): void--><!--Device-print-function startDiscoverPrinter(extensionList: Array<string>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| extensionList | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Load all print extension abilities.
let extensionList: string[] = [];
// Specify the bundle name of your applications to load required print extension abilities during printer discovery.
// let extensionList: string[] = ['com.myapplication.test'];
print.startDiscoverPrinter(extensionList, (err: BusinessError) => {
    if (err) {
        console.error('failed to start Discover Printer because : ' + JSON.stringify(err));
    } else {
        console.info('start Discover Printer success');
    }
})
```


## startDiscoverPrinter

```TypeScript
function startDiscoverPrinter(extensionList: Array<string>): Promise<void>
```

Discovers printers by specifying the extension list. The discovered printers contain the specified print extension abilities. If an empty extension list is specified, all extension abilities are loaded. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** 
- API version 20+: ohos.permission.MANAGE_PRINT_JOB or ohos.permission.PRINT
- API version 10 - 19: ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function startDiscoverPrinter(extensionList: Array<string>): Promise<void>--><!--Device-print-function startDiscoverPrinter(extensionList: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| extensionList | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Load all print extension abilities.
let extensionList: string[] = [];
// Specify the bundle name of your applications to load required print extension abilities during printer discovery.
// let extensionList: string[] = ['com.myapplication.test'];
print.startDiscoverPrinter(extensionList).then(() => {
    console.info('start Discovery success');
}).catch((error: BusinessError) => {
    console.error('failed to start Discovery because : ' + JSON.stringify(error));
})
```
