# offCellInfoChange (System API)

## Modules to Import

```TypeScript
import { observer } from '@kit.TelephonyKit';
```

## offCellInfoChange

```TypeScript
function offCellInfoChange(callback?: Callback<Array<CellInformation>>): void
```

Cancel callback when the cell information is updated.

**Since:** 23

**Deprecated since:** -1

<!--Device-observer-function offCellInfoChange(callback?: Callback<Array<CellInformation>>): void--><!--Device-observer-function offCellInfoChange(callback?: Callback<Array<CellInformation>>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;CellInformation&gt;&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
