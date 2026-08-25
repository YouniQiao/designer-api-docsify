# closeOpenedEnterpriseDlpFiles

## 导入模块

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
```

## closeOpenedEnterpriseDlpFiles

```TypeScript
function closeOpenedEnterpriseDlpFiles(options?: DlpFileQueryOptions): Promise<void>
```

关闭当前打开的所有符合指定选项的企业DLP文件。使用Promise异步回调。在需要批量关闭企业DLP文件、清理文件资源或应用退出前释放文件句柄时调用该接口。

> **说明：**&gt;
> 该接口仅能关闭调用方应用通过[generateDlpFileForEnterprise](arkts-dataprotection-dlppermission-generatedlpfileforenterprise-f.md)生成的企业DLP文件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**需要权限：** ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DlpFileQueryOptions](arkts-dataprotection-dlppermission-dlpfilequeryoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |

**示例**

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
