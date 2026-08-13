# setDlpFeature (System API)

## Modules to Import

```TypeScript
import { dlpSetDlpFeature } from '@kit.DataProtectionKit';
```

## setDlpFeature

```TypeScript
function setDlpFeature(status: DlpFeatureStatus): Promise<StatusInfoResult>
```

Sets the DLP status. This API uses a promise to return the result. The system enables or disables the DLP protection function based on the DLP status specified using this API. When this feature is enabled, right-click the file to be encrypted, and the encryption option is displayed in the shortcut menu. Files in .txt, .pdf, .xls, .xlsx, .ppt, .pptx, .doc, and .docx formats can be encrypted. This API is used to enable or disable the DLP function in enterprise policies.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-dlpSetDlpFeature-function setDlpFeature(status: DlpFeatureStatus): Promise<StatusInfoResult>--><!--Device-dlpSetDlpFeature-function setDlpFeature(status: DlpFeatureStatus): Promise<StatusInfoResult>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| status | [DlpFeatureStatus](arkts-dataprotection-dlpsetdlpfeature-dlpfeaturestatus-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[StatusInfoResult](arkts-dataprotection-dlpsetdlpfeature-statusinforesult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { dlpSetDlpFeature } from '@kit.DataProtectionKit';

async function exampleFunction() {
  let statusInfoResult: dlpSetDlpFeature.StatusInfoResult =
    await dlpSetDlpFeature.setDlpFeature(dlpSetDlpFeature.DlpFeatureStatus.ENABLED_FEATURE);
  console.info('setDlpFeature result: ', JSON.stringify(statusInfoResult)); 
} // Set the DLP status.

exampleFunction();
```
