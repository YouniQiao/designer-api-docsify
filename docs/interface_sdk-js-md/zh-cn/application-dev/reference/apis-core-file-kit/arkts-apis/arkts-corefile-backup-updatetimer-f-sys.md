# updateTimer（系统接口）

## updateTimer

```TypeScript
function updateTimer(bundleName: string, timeout: int): boolean
```

设置应用备份或恢复的时长。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.BACKUP

<!--Device-backup-function updateTimer(bundleName: string, timeout: int): boolean--><!--Device-backup-function updateTimer(bundleName: string, timeout: int): boolean-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 需要设置备份或恢复时长的应用名称。 |
| timeout | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 备份或恢复的限制时长，单位为毫秒，取值范围为0至14400000。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 设置结果，true表示成功，false表示失败。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. 3.Parameter verification failed. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) | Permission verification failed, usually the result returned by VerifyAccessToken. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Permission verification failed, application which is not a system application uses system API. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { backup } from '@kit.CoreFileKit';

function updateTimer() {
  try {
    let timeout = 30000;
    let bundleName = 'com.example.hiworld';
    let result = backup.updateTimer(bundleName, timeout);
    if (result) {
      console.info('updateTimer success');
    } else {
      console.info('updateTimer fail');
    }
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`updateTimer failed. Code: ${err.code}, message: ${err.message}`);
  }
}
```

