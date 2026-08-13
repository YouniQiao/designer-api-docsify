# getDisposedRule（系统接口）

## getDisposedRule

```TypeScript
function getDisposedRule(appId: string, appIndex?: number): DisposedRule
```

获取指定应用或分身应用已设置的拦截规则。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_DISPOSED_APP_STATUS or ohos.permission.GET_DISPOSED_APP_STATUS

<!--Device-appControl-function getDisposedRule(appId: string, appIndex?: int): DisposedRule--><!--Device-appControl-function getDisposedRule(appId: string, appIndex?: int): DisposedRule-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.AppControl

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| appId | string | 是 |
| appIndex | number | 否 |

**返回值：**

| 类型 |
| --- |
| [DisposedRule](arkts-ability-appcontrol-disposedrule-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700061](../errorcode-bundle.md#17700061-指定的应用分身索引无效) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700005](../errorcode-bundle.md#17700005-指定的appid为空字符串) |

## 示例

```TypeScript
import { appControl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let appId = "com.example.myapplication_xxxxx";

try {
  let data = appControl.getDisposedRule(appId, 1);
  console.info('getDisposedRule successfully. Data: ' + JSON.stringify(data));
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('getDisposedRule failed ' + message);
}
```
