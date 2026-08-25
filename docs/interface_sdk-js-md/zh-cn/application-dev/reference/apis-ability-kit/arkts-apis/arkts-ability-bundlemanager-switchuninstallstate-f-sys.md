# switchUninstallState（系统接口）

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## switchUninstallState

```TypeScript
function switchUninstallState(bundleName: string, state: boolean): void
```

切换指定应用的可卸载状态，此接口与EDM应用拦截管控机制不互相影响。

**起始版本：** 12

**需要权限：** ohos.permission.CHANGE_BUNDLE_UNINSTALL_STATE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| state | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700060](../errorcode-bundle.md#17700060-指定的应用不允许被卸载) |
