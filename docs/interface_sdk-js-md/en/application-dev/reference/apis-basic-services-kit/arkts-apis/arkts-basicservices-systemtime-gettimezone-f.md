# getTimezone

## Modules to Import

```TypeScript
import { systemTime } from '@kit.BasicServicesKit';
import { systemTimer } from '@kit.BasicServicesKit';
```

## getTimezone

```TypeScript
function getTimezone(callback: AsyncCallback<string>): void
```

Obtains the system time zone. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getTimezone](arkts-basicservices-systemdatetime-gettimezone-f.md)(callback: AsyncCallback&lt;string&gt;)

<!--Device-systemTime-function getTimezone(callback: AsyncCallback<string>): void--><!--Device-systemTime-function getTimezone(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.MiscServices.Time

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-asynccallback-t.md)&lt;string&gt; | Yes | Callback used to return the system time zone. For details, see Supported System Time Zones . |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**Examples**

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

**Substitutes:** [getTimezone](arkts-basicservices-systemdatetime-gettimezone-f.md)()

<!--Device-systemTime-function getTimezone(): Promise<string>--><!--Device-systemTime-function getTimezone(): Promise<string>-End-->

**System capability:** SystemCapability.MiscServices.Time

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the system time zone. For details, see Supported System Time Zones . |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**Examples**

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

