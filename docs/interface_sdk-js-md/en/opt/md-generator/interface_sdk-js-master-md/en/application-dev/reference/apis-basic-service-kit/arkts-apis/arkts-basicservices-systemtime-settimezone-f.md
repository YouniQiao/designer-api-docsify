# setTimezone

## Modules to Import

```TypeScript
import { systemTime } from 'kits/@kit.BasicServicesKit';
```

## setTimezone

```TypeScript
function setTimezone(timezone: string, callback: AsyncCallback<void>): void
```

Sets the system time zone. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.systemDateTime:systemDateTime.setTimezone](arkts-basicservices-systemdatetime-settimezone-f-sys.md#settimezone)

**Required permissions:** ohos.permission.SET_TIME_ZONE

<!--Device-systemTime-function setTimezone(timezone: string, callback: AsyncCallback<void>): void--><!--Device-systemTime-function setTimezone(timezone: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.Time

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timezone | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| -1 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.setTimezone('Asia/Shanghai', (error: BusinessError) => {
    if (error) {
      console.info(`Failed to set timezone. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in setting timezone.`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to set timezone. message: ${error.message}, code: ${error.code}`);
}
```


## setTimezone

```TypeScript
function setTimezone(timezone: string): Promise<void>
```

Sets the system time zone. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.systemDateTime:systemDateTime.setTimezone](arkts-basicservices-systemdatetime-settimezone-f-sys.md#settimezone)

**Required permissions:** ohos.permission.SET_TIME_ZONE

<!--Device-systemTime-function setTimezone(timezone: string): Promise<void>--><!--Device-systemTime-function setTimezone(timezone: string): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Time

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timezone | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| -1 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.setTimezone('Asia/Shanghai').then(() => {
    console.info(`Succeeded in setting timezone.`);
  }).catch((error: BusinessError) => {
    console.info(`Failed to set timezone. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to set timezone. message: ${error.message}, code: ${error.code}`);
}
```
