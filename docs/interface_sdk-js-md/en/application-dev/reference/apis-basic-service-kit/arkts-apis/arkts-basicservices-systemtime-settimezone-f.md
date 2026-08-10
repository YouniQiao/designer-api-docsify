# setTimezone

## Modules to Import

```TypeScript
import { systemTime } from 'kits/@kit.BasicServicesKit';
```

## setTimezone

```TypeScript
function setTimezone(timezone: string, callback: AsyncCallback<void>): void
```

设置系统时区，使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.systemDateTime:systemDateTime.setTimezone](arkts-basicservices-systemdatetime-settimezone-f-sys.md#settimezone)

**Required permissions:** ohos.permission.SET_TIME_ZONE

<!--Device-systemTime-function setTimezone(timezone: string, callback: AsyncCallback<void>): void--><!--Device-systemTime-function setTimezone(timezone: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.Time

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timezone | string | Yes | 系统时区。具体可见 [支持的系统时区](../../../reference/apis-basic-services-kit/js-apis-system-time.md#支持的系统时区) 。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

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

使用Promise异步回调设置系统时区。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.systemDateTime:systemDateTime.setTimezone](arkts-basicservices-systemdatetime-settimezone-f-sys.md#settimezone)

**Required permissions:** ohos.permission.SET_TIME_ZONE

<!--Device-systemTime-function setTimezone(timezone: string): Promise<void>--><!--Device-systemTime-function setTimezone(timezone: string): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Time

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timezone | string | Yes | 系统时区。具体可见 [支持的系统时区](../../../reference/apis-basic-services-kit/js-apis-system-time.md#支持的系统时区) 。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

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

