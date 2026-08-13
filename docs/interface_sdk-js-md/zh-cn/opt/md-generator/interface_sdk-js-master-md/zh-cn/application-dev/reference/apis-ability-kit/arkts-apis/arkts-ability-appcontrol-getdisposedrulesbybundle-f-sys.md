# getDisposedRulesByBundle（系统接口）

## getDisposedRulesByBundle

```TypeScript
function getDisposedRulesByBundle(bundleName: string): Array<DisposedRuleConfiguration>
```

获取指定应用程序包设置的所有拦截规则。

**起始版本：** 24

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_DISPOSED_APP_STATUS or ohos.permission.GET_DISPOSED_APP_STATUS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-appControl-function getDisposedRulesByBundle(bundleName: string): Array<DisposedRuleConfiguration>--><!--Device-appControl-function getDisposedRulesByBundle(bundleName: string): Array<DisposedRuleConfiguration>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.AppControl

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[DisposedRuleConfiguration](arkts-ability-appcontrol-disposedruleconfiguration-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { appControl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = 'com.example.myapplication';

try {
  let data = appControl.getDisposedRulesByBundle(bundleName);
  console.info('getDisposedRulesByBundle successfully. Data: ' + JSON.stringify(data));
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('getDisposedRulesByBundle failed ' + message);
}
```
