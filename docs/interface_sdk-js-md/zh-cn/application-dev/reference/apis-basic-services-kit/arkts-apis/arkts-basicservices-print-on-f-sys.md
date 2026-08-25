# on（系统接口）

## 导入模块

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## on('printerStateChange')

```TypeScript
function on(type: 'printerStateChange', callback: (state: PrinterState, info: PrinterInfo) => void): void
```

注册打印机状态变化事件回调，使用callback回调。

**起始版本：** 10

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'printerStateChange' | 是 |
| callback | (state: PrinterState, info: PrinterInfo) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## on('jobStateChange')

```TypeScript
function on(type: 'jobStateChange', callback: (state: PrintJobState, job: PrintJob) => void): void
```

注册打印任务状态变化事件回调，使用callback回调。

**起始版本：** 10

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'jobStateChange' | 是 |
| callback | (state: PrintJobState, job: PrintJob) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## on('extInfoChange')

```TypeScript
function on(type: 'extInfoChange', callback: (extensionId: string, info: string) => void): void
```

注册打印扩展信息变化事件回调，使用callback回调。

**起始版本：** 10

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'extInfoChange' | 是 |
| callback | (extensionId: string, info: string) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
