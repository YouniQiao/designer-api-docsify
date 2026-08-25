# checkPreferencesConflicts（系统接口）

## 导入模块

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## checkPreferencesConflicts

```TypeScript
function checkPreferencesConflicts(printerId: string, changedType: string, preferences: PrinterPreferences): Promise<string[]>
```

检查首选项冲突。

**起始版本：** 24

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| printerId | string | 是 |
| changedType | string | 是 |
| preferences | [PrinterPreferences](arkts-basicservices-print-printerpreferences-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [13100005](../errorcode-print.md#13100005-无效的打印机) |
