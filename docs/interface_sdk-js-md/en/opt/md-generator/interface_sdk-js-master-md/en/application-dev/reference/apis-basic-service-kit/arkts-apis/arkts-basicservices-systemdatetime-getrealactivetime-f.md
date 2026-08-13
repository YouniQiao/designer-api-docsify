# getRealActiveTime

## Modules to Import

```TypeScript
import { systemDateTime } from '@kit.BasicServicesKit';
```

## getRealActiveTime

```TypeScript
function getRealActiveTime(isNano: boolean, callback: AsyncCallback<number>): void
```

Obtains the time elapsed since system startup, excluding the deep sleep time. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [getUptime](arkts-basicservices-systemdatetime-getuptime-f.md#getUptime)

<!--Device-systemDateTime-function getRealActiveTime(isNano: boolean, callback: AsyncCallback<number>): void--><!--Device-systemDateTime-function getRealActiveTime(isNano: boolean, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.MiscServices.Time

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isNano | boolean | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealActiveTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.error(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting real active time : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
}
```


## getRealActiveTime

```TypeScript
function getRealActiveTime(callback: AsyncCallback<number>): void
```

Obtains the time elapsed since system startup, excluding the deep sleep time. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [getUptime](arkts-basicservices-systemdatetime-getuptime-f.md#getUptime)

<!--Device-systemDateTime-function getRealActiveTime(callback: AsyncCallback<number>): void--><!--Device-systemDateTime-function getRealActiveTime(callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.MiscServices.Time

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealActiveTime((error: BusinessError, time: number) => {
    if (error) {
      console.error(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting real active time : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
}
```


## getRealActiveTime

```TypeScript
function getRealActiveTime(isNano?: boolean): Promise<number>
```

Obtains the time elapsed since system startup, excluding the deep sleep time. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [getUptime](arkts-basicservices-systemdatetime-getuptime-f.md#getUptime)

<!--Device-systemDateTime-function getRealActiveTime(isNano?: boolean): Promise<number>--><!--Device-systemDateTime-function getRealActiveTime(isNano?: boolean): Promise<number>-End-->

**System capability:** SystemCapability.MiscServices.Time

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isNano | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealActiveTime().then((time: number) => {
    console.info(`Succeeded in getting real active time : ${time}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
}
```
