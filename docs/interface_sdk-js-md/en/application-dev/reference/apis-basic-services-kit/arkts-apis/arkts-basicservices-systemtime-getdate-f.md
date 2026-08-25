# getDate

## Modules to Import

```TypeScript
import { systemTime } from 'kits/@kit.BasicServicesKit';
```

## getDate

```TypeScript
function getDate(callback: AsyncCallback<Date>): void
```

Obtains the current system date. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setDate](arkts-basicservices-systemdatetime-setdate-f-sys.md)

**System capability:** SystemCapability.MiscServices.Time

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Date&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| -1 |


## getDate

```TypeScript
function getDate(): Promise<Date>
```

Obtains the current system date. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getDate](arkts-basicservices-systemdatetime-getdate-f.md)

**System capability:** SystemCapability.MiscServices.Time

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Date & gt; |

**Error codes:**

| Error Code ID |
| --- |
| -1 |
