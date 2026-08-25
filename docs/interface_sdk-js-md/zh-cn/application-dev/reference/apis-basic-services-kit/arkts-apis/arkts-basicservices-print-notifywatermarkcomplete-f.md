# notifyWatermarkComplete

## 导入模块

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## notifyWatermarkComplete

```TypeScript
function notifyWatermarkComplete(jobId: string, result: WatermarkHandleResult): void
```

通知水印处理完成。

**起始版本：** 24

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_PRINT

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| jobId | string | 是 |
| result | [WatermarkHandleResult](arkts-basicservices-print-watermarkhandleresult-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
