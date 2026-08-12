# setAutoTimeStatus（系统接口）

## setAutoTimeStatus

```TypeScript
function setAutoTimeStatus(status: boolean): Promise<void>
```

设置自动设置时间开关状态，使用Promise异步回调。

**起始版本：** 21

**需要权限：** ohos.permission.SET_TIME

<!--Device-systemDateTime-function setAutoTimeStatus(status: boolean): Promise<void>--><!--Device-systemDateTime-function setAutoTimeStatus(status: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.Time

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| status | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [13000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-time.md#13000001-网络或操作系统异常) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [204](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#204-用户访问控制策略拒绝此访问) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.setAutoTimeStatus(true).then(() => {
    console.info(`Succeeded in setting autotime.`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to set autotime. Code: ${error.code}, message: ${error.message}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to set autotime. Code: ${error.code}, message: ${error.message}`);
}
```
