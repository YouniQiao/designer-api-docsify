# hasMatchedCallLog

## Modules to Import

```TypeScript
import { contact } from '@kit.ContactsKit';
```

## hasMatchedCallLog

```TypeScript
function hasMatchedCallLog(context: Context, phoneNumber: string, minDuration: int): Promise<boolean>
```

Checks whether there are call records that meet the specified conditions. By default, call records within the last 6 hours are queried. This API applies only to carrier calls. This API uses a promise to return the result.

**Since:** 24

**Required permissions:** ohos.permission.CHECK_CALL_LOG

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-contact-function hasMatchedCallLog(context: Context, phoneNumber: string, minDuration: int): Promise<boolean>--><!--Device-contact-function hasMatchedCallLog(context: Context, phoneNumber: string, minDuration: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Indicates the context of the application or capability. |
| phoneNumber | string | Yes | Phone number of the contacts. |
| minDuration | int | Yes | Minimum call duration, in seconds. The value must be greater than 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result of whether there are call records that meet the specified conditions. The value **true** indicates that there are such records, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [16700002](../errorcode-contacts.md#16700002-parameter-check-failed) | Invalid parameter value. |
| [16700001](../errorcode-contacts.md#16700001-system-internal-error) | General error. |


## hasMatchedCallLog

```TypeScript
function hasMatchedCallLog(context: Context, phoneNumber: string, minDuration: int, withinTime: int): Promise<boolean>
```

Checks whether there are call records that meet the specified conditions. This API applies only to carrier calls. This API uses a promise to return the result.

**Since:** 24

**Required permissions:** ohos.permission.CHECK_CALL_LOG

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-contact-function hasMatchedCallLog(context: Context, phoneNumber: string, minDuration: int, withinTime: int): Promise<boolean>--><!--Device-contact-function hasMatchedCallLog(context: Context, phoneNumber: string, minDuration: int, withinTime: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Indicates the context of the application or capability. |
| phoneNumber | string | Yes | Phone number of the contacts. |
| minDuration | int | Yes | Minimum call duration, in seconds. The value must be greater than 0. |
| withinTime | int | Yes | Period of time that the start time and end time of calls should be within, in seconds. This period starts from the current time. A maximum of six hours can be set. If the query duration exceeds six hours, the query duration is six hours by default. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result of whether there are call records that meet the specified conditions. The value **true** indicates that there are such records, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [16700002](../errorcode-contacts.md#16700002-parameter-check-failed) | Invalid parameter value. |
| [16700001](../errorcode-contacts.md#16700001-system-internal-error) | General error. |

