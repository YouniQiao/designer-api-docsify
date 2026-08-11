# getPermissionDefSync（系统接口）

## getPermissionDefSync

```TypeScript
function getPermissionDefSync(permissionName: string): PermissionDef
```

以同步方法根据给定的permissionName获取权限定义结构体PermissionDef信息。

**起始版本：** 10

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundleManager-function getPermissionDefSync(permissionName: string): PermissionDef--><!--Device-bundleManager-function getPermissionDefSync(permissionName: string): PermissionDef-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| permissionName | string | 是 |

**返回值：**

| 类型 |
| --- |
| [PermissionDef](arkts-ability-permissiondef-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [17700006](../errorcode-bundle.md#17700006-查询的权限不存在) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let permissionName = "ohos.permission.GET_BUNDLE_INFO";
try {
  let permissionDef = bundleManager.getPermissionDefSync(permissionName);
  hilog.info(0x0000, 'testTag', 'getPermissionDefSync successfully. Data: %{public}s', JSON.stringify(permissionDef));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getPermissionDefSync failed. Cause: %{public}s', message);
}
```
