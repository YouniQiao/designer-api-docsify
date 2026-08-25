# updateNtpTime（系统接口）

## 导入模块

```TypeScript
import { systemDateTime } from 'kits/@kit.BasicServicesKit';
```

## updateNtpTime

```TypeScript
function updateNtpTime(): Promise<void>
```

使用异步方式从NTP服务器更新NTP时间。该方法一小时内只会从NTP服务器更新一次NTP时间。

**起始版本：** 14

**系统能力：** SystemCapability.MiscServices.Time

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [13000001](../errorcode-time.md#13000001-网络或操作系统异常) |
