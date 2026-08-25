# getAppProvisionInfoSync（系统接口）

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getAppProvisionInfoSync

```TypeScript
function getAppProvisionInfoSync(bundleName: string, userId?: number): AppProvisionInfo
```

以同步方法根据bundleName和userId获取应用的provision配置文件信息并返回结果。获取调用方自身的信息时不需要权限。

**起始版本：** 10

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| [AppProvisionInfo](arkts-ability-bundlemanager-appprovisioninfo-t-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
