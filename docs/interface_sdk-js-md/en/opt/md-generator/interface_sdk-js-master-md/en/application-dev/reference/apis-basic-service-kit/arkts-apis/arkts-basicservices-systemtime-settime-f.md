# setTime

## Modules to Import

```TypeScript
import { systemTime } from '@kit.BasicServicesKit';
```

## setTime

```TypeScript
function setTime(time: number, callback: AsyncCallback<void>): void
```

Sets the system time. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setTime](arkts-basicservices-systemdatetime-settime-f-sys.md#setTime-(System-API))

**Required permissions:** ohos.permission.SET_TIME

<!--Device-systemTime-function setTime(time: number, callback: AsyncCallback<void>): void--><!--Device-systemTime-function setTime(time: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.Time

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| time | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| -1 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Set the system time to 2021-01-20 02:36:25.
let time = 1611081385000;
try {
  systemTime.setTime(time, (error: BusinessError) => {
    if (error) {
      console.info(`Failed to set time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in setting time`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to set time. message: ${error.message}, code: ${error.code}`);
}
```


## setTime

```TypeScript
function setTime(time: number): Promise<void>
```

Sets the system time. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setTime](arkts-basicservices-systemdatetime-settime-f-sys.md#setTime-(System-API))

**Required permissions:** ohos.permission.SET_TIME

<!--Device-systemTime-function setTime(time: number): Promise<void>--><!--Device-systemTime-function setTime(time: number): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Time

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| time | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| -1 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Set the system time to 2021-01-20 02:36:25.
let time = 1611081385000;
try {
  systemTime.setTime(time).then(() => {
    console.info(`Succeeded in setting time.`);
  }).catch((error: BusinessError) => {
    console.info(`Failed to set time. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to set time. message: ${error.message}, code: ${error.code}`);
}
```
