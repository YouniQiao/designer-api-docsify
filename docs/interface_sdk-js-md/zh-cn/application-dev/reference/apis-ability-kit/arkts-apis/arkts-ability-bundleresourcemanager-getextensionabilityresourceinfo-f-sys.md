# getExtensionAbilityResourceInfo（系统接口）

## 导入模块

```TypeScript
import { bundleResourceManager } from 'kits/@kit.AbilityKit';
```

## getExtensionAbilityResourceInfo

```TypeScript
function getExtensionAbilityResourceInfo(bundleName: string, extensionAbilityType: bundleManager.ExtensionAbilityType, resourceFlags: number, appIndex?: number): Array<LauncherAbilityResourceInfo>
```

根据应用包名、扩展组件类型、资源信息标志、应用分身ID获取应用的扩展组件资源。使用同步方式返回。

**起始版本：** 20

**需要权限：** ohos.permission.GET_BUNDLE_RESOURCES

**系统能力：** SystemCapability.BundleManager.BundleFramework.Resource

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| [extensionAbilityType](arkts-ability-extensionabilityinfo-i.md) | bundleManager.ExtensionAbilityType | 是 |
| resourceFlags | number | 是 |
| appIndex | number | 否 |

**返回值：**

| 类型 |
| --- |
| Array & lt;LauncherAbilityResourceInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700061](../errorcode-bundle.md#17700061-指定的应用分身索引无效) |
