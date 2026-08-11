# setDisposedStatusSync（系统接口）

## setDisposedStatusSync

```TypeScript
function setDisposedStatusSync(appId: string, disposedWant: Want): void
```

以同步方法设置应用的处置状态。成功返回null，失败抛出对应异常。

**起始版本：** 10

**需要权限：** ohos.permission.MANAGE_DISPOSED_APP_STATUS

<!--Device-appControl-function setDisposedStatusSync(appId: string, disposedWant: Want): void--><!--Device-appControl-function setDisposedStatusSync(appId: string, disposedWant: Want): void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.AppControl

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| appId | string | 是 |
| disposedWant | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700005](../errorcode-bundle.md#17700005-指定的appid为空字符串) |

## 示例

```TypeScript
import { appControl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';

let appId: string = "com.example.myapplication_xxxxx";
let want: Want = { bundleName: 'com.example.myapplication' };

try {
  appControl.setDisposedStatusSync(appId, want);
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('setDisposedStatusSync failed ' + message);
}
```
