# getTimezone

## Modules to Import

```TypeScript
import { systemTime } from '@kit.BasicServicesKit';
```

## getTimezone

```TypeScript
function getTimezone(callback: AsyncCallback<string>): void
```

Obtains the system time zone. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getTimezone](arkts-basicservices-systemdatetime-gettimezone-f.md#getTimezone)(callback: AsyncCallback&lt;string&gt;)

<!--Device-systemTime-function getTimezone(callback: AsyncCallback<string>): void--><!--Device-systemTime-function getTimezone(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.MiscServices.Time

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| -1 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getTimezone((error: BusinessError, data: string) => {
    if (error) {
      console.info(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting timezone : ${data}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
}
```


## getTimezone

```TypeScript
function getTimezone(): Promise<string>
```

Obtains the system time zone. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getTimezone](arkts-basicservices-systemdatetime-gettimezone-f.md#getTimezone)()

<!--Device-systemTime-function getTimezone(): Promise<string>--><!--Device-systemTime-function getTimezone(): Promise<string>-End-->

**System capability:** SystemCapability.MiscServices.Time

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| -1 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getTimezone().then((data: string) => {
    console.info(`Succeeded in getting timezone: ${data}`);
  }).catch((error: BusinessError) => {
    console.info(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
}
```
