# queryRecommendDriversById (System API)

## Modules to Import

```TypeScript
```

## queryRecommendDriversById

```TypeScript
function queryRecommendDriversById(printerId: string): Promise<PpdInfo[]>
```

Query recommend printer drivers by printer ID.

**Since:** 24

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function queryRecommendDriversById(printerId: string): Promise<PpdInfo[]>--><!--Device-print-function queryRecommendDriversById(printerId: string): Promise<PpdInfo[]>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| printerId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PpdInfo](arkts-basicservices-print-ppdinfo-i.md)[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [13100005](../../apis-basic-services-kit/errorcode-print.md#13100005-invalid-printer) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
