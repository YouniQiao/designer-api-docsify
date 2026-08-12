# closeOpenedEnterpriseDlpFiles

## closeOpenedEnterpriseDlpFiles

```TypeScript
function closeOpenedEnterpriseDlpFiles(options?: DlpFileQueryOptions): Promise<void>
```

关闭当前打开的所有符合指定选项的企业DLP文件。使用Promise异步回调。

在需要批量关闭企业DLP文件、清理文件资源或应用退出前释放文件句柄时调用该接口。

> **说明：**
> 
> 该接口仅能关闭调用方应用通过[generateDlpFileForEnterprise](arkts-dataprotection-dlppermission-generatedlpfileforenterprise-f.md#generateDlpFileForEnterprise)生成的企业DLP文件。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-dlpPermission-function closeOpenedEnterpriseDlpFiles(options?: DlpFileQueryOptions): Promise<void>--><!--Device-dlpPermission-function closeOpenedEnterpriseDlpFiles(options?: DlpFileQueryOptions): Promise<void>-End-->

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
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [19100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100001-入参错误) |
| [19100011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-系统服务工作异常) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |

## 示例

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
