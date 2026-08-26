# getPermissionDef（系统接口）

## 导入模块

```TypeScript
import appControl from '@kit.AbilityKit.appControl';
import bundleManager from '@kit.AbilityKit.bundleManager';
import bundleMonitor from '@kit.AbilityKit.bundleMonitor';
import bundleResourceManager from '@kit.AbilityKit.bundleResourceManager';
import bundle from '@kit.AbilityKit';
import defaultAppManager from '@kit.AbilityKit.defaultAppManager';
import distributedBundleManager from '@kit.AbilityKit.distributedBundleManager';
import freeInstall from '@kit.AbilityKit.freeInstall';
import innerBundleManager, { BundleStatusCallback } from '@kit.AbilityKit.innerBundleManager';
import installer from '@kit.AbilityKit.installer';
import launcherBundleManager from '@kit.AbilityKit.launcherBundleManager';
import overlay from '@kit.AbilityKit.overlay';
import shortcutManager from '@kit.AbilityKit.shortcutManager';
import skillManager from '@kit.AbilityKit.skillManager';
import appDomainVerify from '@kit.AbilityKit.appDomainVerify';
import pluginBundleManager from '@kit.AbilityKit.pluginBundleManager';
```

## getPermissionDef

```TypeScript
function getPermissionDef(permissionName: string, callback: AsyncCallback<PermissionDef>): void
```

按权限名称获取权限的详细信息，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** null

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：** SystemCapability.BundleManager.BundleFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| permissionName | string | 是 | 需要查询的权限的名称。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PermissionDef](arkts-ability-permissiondef-depr-i-sys.md)&gt; | 是 | 程序启动作为入参的回调函数，返回定义的权限信息。 |

**示例**

```TypeScript
import bundle from '@ohos.bundle';

let permission: string = "ohos.permission.GET_BUNDLE_INFO";
bundle.getPermissionDef(permission, (err, data) => {
  if (err) {
    console.error('getPermissionDef failed:' + err.message);
  } else {
    console.info('getPermissionDef successfully:' + JSON.stringify(data));
  }
});
```

```TypeScript
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let permissionName: string = "ohos.permission.GET_BUNDLE_INFO";
bundle.getPermissionDef(permissionName).then((data) => {
  console.info('getPermissionDef successfully. Data: ' + JSON.stringify(data));
}).catch((error: BusinessError) => {
  console.error('getPermissionDef failed. Cause: ' + error.message);
});
```


## getPermissionDef

```TypeScript
function getPermissionDef(permissionName: string): Promise<PermissionDef>
```

按权限名称获取权限的详细信息，使用promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** null

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：** SystemCapability.BundleManager.BundleFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| permissionName | string | 是 | 需要查询的权限的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[PermissionDef](arkts-ability-permissiondef-depr-i-sys.md)&gt; | Promise对象，获取成功时返回权限详细信息。 |

**示例**

参见 [getPermissionDef](#getpermissiondef)
