# getNtpTime（系统接口）

## 导入模块

```TypeScript
import { systemDateTime } from '@kit.BasicServicesKit';
```

## getNtpTime

```TypeScript
function getNtpTime(): long
```

使用同步方式获取基于上次更新的NTP时间所计算出的真实时间。

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.Time

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：long |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [13000002](../errorcode-time.md#13000002-未更新ntp时间) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let time: number = systemDateTime.getNtpTime();
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get ntp time. Code: ${error.code}, message: ${error.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@ohos.base';

try {
  let time: long = systemDateTime.getNtpTime();
} catch(error: BusinessError) {
  console.error(`Failed to get ntp time. message: ${error.message}, code: ${error.code}`);
}
```
