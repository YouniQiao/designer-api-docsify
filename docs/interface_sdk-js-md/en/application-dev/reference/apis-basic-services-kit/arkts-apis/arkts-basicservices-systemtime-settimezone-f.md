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

**Substitutes:** [setTimezone](arkts-basicservices-systemdatetime-settimezone-f-sys.md)

**Required permissions:** ohos.permission.SET_TIME_ZONE

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


## setTimezone

```TypeScript
function setTimezone(timezone: string): Promise<void>
```

Sets the system time zone. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setTimezone](arkts-basicservices-systemdatetime-settimezone-f-sys.md)

**Required permissions:** ohos.permission.SET_TIME_ZONE

**System capability:** SystemCapability.MiscServices.Time

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timezone | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| -1 |
