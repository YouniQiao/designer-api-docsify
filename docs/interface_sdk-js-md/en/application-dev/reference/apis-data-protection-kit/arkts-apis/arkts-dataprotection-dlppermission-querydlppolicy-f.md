# queryDlpPolicy

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## queryDlpPolicy

```TypeScript
function queryDlpPolicy(dlpFd: number): Promise<string>
```

在DLP文件中解析文件头，获取DLP明文策略。返回的策略JSON字符串包含[DLPProperty](arkts-dataprotection-dlppermission-dlpproperty-i.md)和  
[CustomProperty](arkts-dataprotection-dlppermission-customproperty-i.md)信息。使用Promise异步回调。

该接口可用于在查看DLP文件权限配置等场景中，获取文件的策略信息以便进行分析。

> **说明：**
> 
> 该接口仅支持企业账号调用。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Required permissions:** ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

<!--Device-dlpPermission-function queryDlpPolicy(dlpFd: number): Promise<string>--><!--Device-dlpPermission-function queryDlpPolicy(dlpFd: number): Promise<string>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dlpFd | number | Yes | 待查询策略的DLP文件的fd。取值范围为[0, 2&lt;sup&gt;31&lt;/sup&gt;-1]。当fd小于0时，打印错误日志，函数停止运行；当fd大于2&lt;sup&gt;31&lt;/sup&gt;-1时， fd的值被截断。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回当前DLP策略的JSON字符串。长度不超过4194304字节。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19100003 | Credential task time out. |
| 19100002 | Credential service busy due to too many tasks or duplicate tasks. |
| 19100001 | Invalid parameter value. |
| 19100005 | Credential authentication server error. |
| 19100004 | Credential service error. |
| 19100011 | The system ability works abnormally. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs.<br>**Applicable version:** 20 and later |
| 19100009 | Failed to operate the DLP file. |
| 19100008 | The file is not a DLP file. |
| 19100013 | The user does not have the permission. |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';

let dlpFd : number | undefined = undefined; // FD of the DLP file to be queried.
let dlpFilePath: string = "file://docs/storage/Users/currentUser/Documents/test.txt.dlp"; // Specify the DLP file path.
dlpFd = fileIo.openSync(dlpFilePath, fileIo.OpenMode.READ_ONLY).fd; // Open the DLP file to obtain the descriptor.
dlpPermission.queryDlpPolicy(dlpFd).then((policy) => {
  console.info('DLP policy:' + policy);
}).catch((error: BusinessError)=> {
  console.error(JSON.stringify(error));
}).finally(()=>{
  if (dlpFd) {
    fileIo.closeSync(dlpFd);
  }
});
```

