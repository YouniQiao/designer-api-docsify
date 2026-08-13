# setUninstallDisposedRule（系统接口）

## setUninstallDisposedRule

```TypeScript
function setUninstallDisposedRule(appIdentifier: string, rule: UninstallDisposedRule, appIndex?: number): void
```

设置指定应用或分身应用的卸载处置规则。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_DISPOSED_APP_STATUS

<!--Device-appControl-function setUninstallDisposedRule(appIdentifier: string, rule: UninstallDisposedRule, appIndex?: int): void--><!--Device-appControl-function setUninstallDisposedRule(appIdentifier: string, rule: UninstallDisposedRule, appIndex?: int): void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.AppControl

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| appIdentifier | string | 是 |
| rule | [UninstallDisposedRule](arkts-ability-appcontrol-uninstalldisposedrule-i-sys.md) | 是 |
| appIndex | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700061](../errorcode-bundle.md#17700061-指定的应用分身索引无效) |
| [17700074](../errorcode-bundle.md#17700074-传入的appidentifier无效) |
| [17700075](../errorcode-bundle.md#17700075-want指定的bundlename与调用方不符) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { appControl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';

let appIdentifier = "com.example.myapplication_xxxxx";
let want: Want = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  abilityName: "EntryAbility"
};
let rule: appControl.UninstallDisposedRule = {
  want: want,
  uninstallComponentType: appControl.UninstallComponentType.EXTENSION,
  priority: 100
};

try {
  appControl.setUninstallDisposedRule(appIdentifier, rule, 1);
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('setUninstallDisposedRule failed ' + message);
}
```
