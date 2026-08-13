# getLauncherAbilityResourceInfoList（系统接口）

## getLauncherAbilityResourceInfoList

```TypeScript
function getLauncherAbilityResourceInfoList(optionsList: Array<BundleOptions>, resourceFlags: number): Promise<Array<LauncherAbilityResourceInfo>>
```

根据传入的optionsList获取列表中每个BundleOptions元素对应的应用的LauncherAbilityResourceInfo。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_INSTALLED_BUNDLE_LIST and ohos.permission.GET_BUNDLE_RESOURCES

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-bundleResourceManager-function getLauncherAbilityResourceInfoList(optionsList: Array<BundleOptions>, resourceFlags: int): Promise<Array<LauncherAbilityResourceInfo>>--><!--Device-bundleResourceManager-function getLauncherAbilityResourceInfoList(optionsList: Array<BundleOptions>, resourceFlags: int): Promise<Array<LauncherAbilityResourceInfo>>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Resource

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| optionsList | Array&lt;[BundleOptions](arkts-ability-bundleinfo-bundleoptions-i-sys.md)&gt; | 是 |
| resourceFlags | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;LauncherAbilityResourceInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700061](../errorcode-bundle.md#17700061-指定的应用分身索引无效) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700003](../errorcode-bundle.md#17700003-指定的abilityname不存在) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { bundleManager, bundleResourceManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 请开发者替换为实际要查询的应用的信息
let option: bundleManager.BundleOptions = {
  bundleName: 'com.example.demo',
  moduleName: 'entry',
  abilityName: 'EntryAbility',
  appIndex: 0
};

let optionsList: Array<bundleManager.BundleOptions> = [];
optionsList.push(option);
let resourceFlag = bundleResourceManager.ResourceFlag.GET_RESOURCE_INFO_ALL;
try {
  bundleResourceManager.getLauncherAbilityResourceInfoList(optionsList, resourceFlag).then(data => {
    hilog.info(0x0000, 'testTag', 'getLauncherAbilityResourceInfoList successfully. Data length: %{public}s',
      JSON.stringify(data.length));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getLauncherAbilityResourceInfoList failed. err: %{public}s', err.message);
  })
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getLauncherAbilityResourceInfoList failed: %{public}s', message);
}
```
