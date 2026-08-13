# getLauncherAbilityResourceInfo（系统接口）

## getLauncherAbilityResourceInfo

```TypeScript
function getLauncherAbilityResourceInfo(bundleName: string, resourceFlags?: number): Array<LauncherAbilityResourceInfo>
```

以同步方法根据给定的bundleName和resourceFlags获取当前应用的LauncherAbilityResourceInfo。

**起始版本：** 11

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_RESOURCES

<!--Device-bundleResourceManager-function getLauncherAbilityResourceInfo(bundleName: string, resourceFlags?: int): Array<LauncherAbilityResourceInfo>--><!--Device-bundleResourceManager-function getLauncherAbilityResourceInfo(bundleName: string, resourceFlags?: int): Array<LauncherAbilityResourceInfo>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Resource

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| resourceFlags | number | 否 |

**返回值：**

| 类型 |
| --- |
| Array & lt;LauncherAbilityResourceInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |


## getLauncherAbilityResourceInfo

```TypeScript
function getLauncherAbilityResourceInfo(bundleName: string, resourceFlags?: number, appIndex?: number): Array<LauncherAbilityResourceInfo>
```

以同步方法根据给定的bundleName、resourceFlags和appIndex获取当前应用或分身应用的LauncherAbilityResourceInfo。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_RESOURCES

<!--Device-bundleResourceManager-function getLauncherAbilityResourceInfo(bundleName: string, resourceFlags?: int, appIndex?: int): Array<LauncherAbilityResourceInfo>--><!--Device-bundleResourceManager-function getLauncherAbilityResourceInfo(bundleName: string, resourceFlags?: int, appIndex?: int): Array<LauncherAbilityResourceInfo>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Resource

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| resourceFlags | number | 否 |
| appIndex | number | 否 |

**返回值：**

| 类型 |
| --- |
| Array & lt;LauncherAbilityResourceInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700061](../errorcode-bundle.md#17700061-指定的应用分身索引无效) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
