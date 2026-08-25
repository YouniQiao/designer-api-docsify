# setDate

## Modules to Import

```TypeScript
import { systemTime } from 'kits/@kit.BasicServicesKit';
```

## setDate

```TypeScript
function setDate(date: Date, callback: AsyncCallback<void>): void
```

Sets the system date. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setDate](arkts-basicservices-systemdatetime-setdate-f-sys.md)

**Required permissions:** ohos.permission.SET_TIME

**System capability:** SystemCapability.MiscServices.Time

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| date | Date | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| -1 |


## setDate

```TypeScript
function setDate(date: Date): Promise<void>
```

Sets the system date. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setDate](arkts-basicservices-systemdatetime-setdate-f-sys.md)

**Required permissions:** ohos.permission.SET_TIME

**System capability:** SystemCapability.MiscServices.Time

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| date | Date | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| -1 |
