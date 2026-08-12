# updateNtpTime（系统接口）

## updateNtpTime

```TypeScript
function updateNtpTime(): Promise<void>
```

使用异步方式从NTP服务器更新NTP时间。该方法一小时内只会从NTP服务器更新一次NTP时间。

**起始版本：** 14

<!--Device-systemDateTime-function updateNtpTime(): Promise<void>--><!--Device-systemDateTime-function updateNtpTime(): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.Time

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [13000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-time.md#13000001-网络或操作系统异常) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.updateNtpTime().then(() => {
    console.info(`Succeeded in updating ntp time.`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to update ntp time. Code: ${error.code}, message: ${error.message}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to update ntp time. Code: ${error.code}, message: ${error.message}`);
}
```
