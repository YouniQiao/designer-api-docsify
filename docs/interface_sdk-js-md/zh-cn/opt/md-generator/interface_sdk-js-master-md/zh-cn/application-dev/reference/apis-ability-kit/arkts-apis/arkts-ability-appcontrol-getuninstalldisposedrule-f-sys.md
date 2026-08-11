# getUninstallDisposedRule（系统接口）

## getUninstallDisposedRule

```TypeScript
function getUninstallDisposedRule(appIdentifier: string, appIndex?: number): UninstallDisposedRule
```

获取指定应用或分身应用已设置的优先级最高的卸载处置规则。

**起始版本：** 15

**需要权限：** ohos.permission.GET_DISPOSED_APP_STATUS or ohos.permission.MANAGE_DISPOSED_APP_STATUS

<!--Device-appControl-function getUninstallDisposedRule(appIdentifier: string, appIndex?: int): UninstallDisposedRule--><!--Device-appControl-function getUninstallDisposedRule(appIdentifier: string, appIndex?: int): UninstallDisposedRule-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.AppControl

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| appIdentifier | string | 是 |
| appIndex | number | 否 |

**返回值：**

| 类型 |
| --- |
| [UninstallDisposedRule](arkts-ability-appcontrol-uninstalldisposedrule-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700061](../errorcode-bundle.md#17700061-指定的应用分身索引无效) |
| [17700074](../errorcode-bundle.md#17700074-传入的appidentifier无效) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { appControl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let appIdentifier = "com.example.myapplication_xxxxx";

try {
  let data = appControl.getUninstallDisposedRule(appIdentifier, 1);
  console.info('getUninstallDisposedRule successfully. Data: ' + JSON.stringify(data));
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('getUninstallDisposedRule failed ' + message);
}
```
