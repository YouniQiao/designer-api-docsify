# getAllLauncherAbilityInfos（系统接口）

## getAllLauncherAbilityInfos

```TypeScript
function getAllLauncherAbilityInfos(userId: number, callback: AsyncCallback<Array<LauncherAbilityInfo>>): void
```

获取所有的LauncherAbilityInfos，使用callback异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [getAllLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getalllauncherabilityinfo-f-sys.md#getAllLauncherAbilityInfo)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getAllLauncherAbilityInfo](@ohos.bundle.launcherBundleManager:launcherBundleManager.getAllLauncherAbilityInfo(userId:)

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-innerBundleManager-function getAllLauncherAbilityInfos(userId: number, callback: AsyncCallback<Array<LauncherAbilityInfo>>): void--><!--Device-innerBundleManager-function getAllLauncherAbilityInfos(userId: number, callback: AsyncCallback<Array<LauncherAbilityInfo>>): void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[LauncherAbilityInfo](arkts-ability-launcherabilityinfo-launcherabilityinfo-depr-i-sys.md)&gt;&gt; | 是 |


## getAllLauncherAbilityInfos

```TypeScript
function getAllLauncherAbilityInfos(userId: number): Promise<Array<LauncherAbilityInfo>>
```

获取LauncherAbilityInfos，使用Promise异步回调。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [getAllLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getalllauncherabilityinfo-f-sys.md#getAllLauncherAbilityInfo)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getAllLauncherAbilityInfo](@ohos.bundle.launcherBundleManager:launcherBundleManager.getAllLauncherAbilityInfo(userId:)

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-innerBundleManager-function getAllLauncherAbilityInfos(userId: number): Promise<Array<LauncherAbilityInfo>>--><!--Device-innerBundleManager-function getAllLauncherAbilityInfos(userId: number): Promise<Array<LauncherAbilityInfo>>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[LauncherAbilityInfo](arkts-ability-launcherabilityinfo-launcherabilityinfo-depr-i-sys.md)&gt;&gt; |
