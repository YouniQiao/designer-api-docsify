# closeOpenedEnterpriseDlpFiles

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## closeOpenedEnterpriseDlpFiles

```TypeScript
function closeOpenedEnterpriseDlpFiles(options?: DlpFileQueryOptions): Promise<void>
```

关闭当前打开的所有符合指定选项的企业DLP文件。使用Promise异步回调。

在需要批量关闭企业DLP文件、清理文件资源或应用退出前释放文件句柄时调用该接口。

> **说明：**
> 
> 该接口仅能关闭调用方应用通过[generateDlpFileForEnterprise](arkts-dataprotection-dlppermission-generatedlpfileforenterprise-f.md#generatedlpfileforenterprise)生成的企业DLP文件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

**Model restriction:** This API can be used only in the stage model.

<!--Device-dlpPermission-function closeOpenedEnterpriseDlpFiles(options?: DlpFileQueryOptions): Promise<void>--><!--Device-dlpPermission-function closeOpenedEnterpriseDlpFiles(options?: DlpFileQueryOptions): Promise<void>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DlpFileQueryOptions](arkts-dataprotection-dlppermission-dlpfilequeryoptions-i.md) | No | 企业DLP文件的查询选项。当需要按分类标签筛选关闭特定企业DLP文件时传入此参数，当需要关闭所有企业DLP文件时可不传此参数。不传入或传入空 字符串时，关闭所有企业DLP文件。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |
| 201 | Permission denied. |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

let options: dlpPermission.DlpFileQueryOptions = {
  classificationLabel: 'label1'
};
dlpPermission.closeOpenedEnterpriseDlpFiles(options).then(() => {
  console.info("try to close opened enterprise dlp files");
}).catch((error: BusinessError)=> {
  console.error(error.message);
}).finally(()=> {
  console.info("after closing opened enterprise dlp files");
});
```

