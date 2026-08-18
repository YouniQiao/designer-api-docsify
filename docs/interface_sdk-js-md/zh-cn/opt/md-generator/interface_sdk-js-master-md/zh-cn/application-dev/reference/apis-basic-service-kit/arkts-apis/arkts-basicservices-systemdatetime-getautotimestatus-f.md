# getAutoTimeStatus

## 导入模块

```TypeScript
```

## getAutoTimeStatus

```TypeScript
function getAutoTimeStatus(): boolean
```

获取自动设置时间开关状态，使用同步方式。

**起始版本：** 23

<!--Device-systemDateTime-function getAutoTimeStatus(): boolean--><!--Device-systemDateTime-function getAutoTimeStatus(): boolean-End-->

**系统能力：** SystemCapability.MiscServices.Time

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [13000001](../../apis-basic-services-kit/errorcode-time.md#13000001-网络或操作系统异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let status: boolean = systemDateTime.getAutoTimeStatus();
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get autotime status. Code: ${error.code}, message: ${error.message}`);
}
```
