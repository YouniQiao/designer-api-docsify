# getDate

## Modules to Import

```TypeScript
```

## getDate

```TypeScript
function getDate(callback: AsyncCallback<Date>): void
```

Obtains the current system date. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setDate](arkts-basicservices-systemdatetime-setdate-f-sys.md#setdate-system-api)

<!--Device-systemTime-function getDate(callback: AsyncCallback<Date>): void--><!--Device-systemTime-function getDate(callback: AsyncCallback<Date>): void-End-->

**System capability:** SystemCapability.MiscServices.Time

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Date&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| -1 |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getDate((error: BusinessError, date: Date) => {
    if (error) {
      console.info(`Failed to get date. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting date : ${date}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get date. message: ${error.message}, code: ${error.code}`);
}
```


## getDate

```TypeScript
function getDate(): Promise<Date>
```

Obtains the current system date. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getDate](arkts-basicservices-systemdatetime-getdate-f.md#getdate)

<!--Device-systemTime-function getDate(): Promise<Date>--><!--Device-systemTime-function getDate(): Promise<Date>-End-->

**System capability:** SystemCapability.MiscServices.Time

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Date & gt; |

**Error codes:**

| Error Code ID |
| --- |
| -1 |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getDate().then((date: Date) => {
    console.info(`Succeeded in getting date : ${date}`);
  }).catch((error: BusinessError) => {
    console.info(`Failed to get date. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get date. message: ${error.message}, code: ${error.code}`);
}
```
