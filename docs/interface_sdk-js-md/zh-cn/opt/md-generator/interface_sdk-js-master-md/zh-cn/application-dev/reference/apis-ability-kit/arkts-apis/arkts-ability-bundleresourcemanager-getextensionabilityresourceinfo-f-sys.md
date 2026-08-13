# getExtensionAbilityResourceInfo（系统接口）

## getExtensionAbilityResourceInfo

```TypeScript
function getExtensionAbilityResourceInfo(bundleName: string, extensionAbilityType: bundleManager.ExtensionAbilityType, resourceFlags: number, appIndex?: number): Array<LauncherAbilityResourceInfo>
```

根据应用包名、扩展组件类型、资源信息标志、应用分身ID获取应用的扩展组件资源。使用同步方式返回。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_RESOURCES

<!--Device-bundleResourceManager-function getExtensionAbilityResourceInfo(bundleName: string, extensionAbilityType: bundleManager.ExtensionAbilityType, resourceFlags: int, appIndex?: int): Array<LauncherAbilityResourceInfo>--><!--Device-bundleResourceManager-function getExtensionAbilityResourceInfo(bundleName: string, extensionAbilityType: bundleManager.ExtensionAbilityType, resourceFlags: int, appIndex?: int): Array<LauncherAbilityResourceInfo>-End-->

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
| [17700061](../errorcode-bundle.md#17700061-指定的应用分身索引无效) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { bundleManager, bundleResourceManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = "com.example.myapplication";
let extensionAbilityType = bundleManager.ExtensionAbilityType.INPUT_METHOD;
let resourceFlag = bundleResourceManager.ResourceFlag.GET_RESOURCE_INFO_ALL;
try {
  let resourceInfo =
    bundleResourceManager.getExtensionAbilityResourceInfo(bundleName, extensionAbilityType, resourceFlag);
  hilog.info(0x0000, 'testTag', 'getExtensionAbilityResourceInfo successfully. Data label: %{public}s',
    JSON.stringify(resourceInfo[0].label));
} catch (err) {
  let message = (err as BusinessError).message;
  let code = (err as BusinessError).code;
  hilog.error(0x0000, 'testTag', 'getExtensionAbilityResourceInfo failed: %{public}d %{public}s', code, message);
}
```
