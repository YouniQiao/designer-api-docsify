# setHapModuleUpgradeFlag（系统接口）

## setHapModuleUpgradeFlag

```TypeScript
function setHapModuleUpgradeFlag(bundleName: string, 
    moduleName: string, upgradeFlag: UpgradeFlag, callback: AsyncCallback<void>): void
```

设置指定模块是否升级。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.INSTALL_BUNDLE

<!--Device-freeInstall-function setHapModuleUpgradeFlag(bundleName: string,     moduleName: string, upgradeFlag: UpgradeFlag, callback: AsyncCallback<void>): void--><!--Device-freeInstall-function setHapModuleUpgradeFlag(bundleName: string,     moduleName: string, upgradeFlag: UpgradeFlag, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.FreeInstall

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| moduleName | string | 是 |
| upgradeFlag | [UpgradeFlag](arkts-ability-freeinstall-upgradeflag-e-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |


## setHapModuleUpgradeFlag

```TypeScript
function setHapModuleUpgradeFlag(bundleName: string, moduleName: string, upgradeFlag: UpgradeFlag): Promise<void>
```

设置指定模块是否升级。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.INSTALL_BUNDLE

<!--Device-freeInstall-function setHapModuleUpgradeFlag(bundleName: string, moduleName: string, upgradeFlag: UpgradeFlag): Promise<void>--><!--Device-freeInstall-function setHapModuleUpgradeFlag(bundleName: string, moduleName: string, upgradeFlag: UpgradeFlag): Promise<void>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.FreeInstall

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| moduleName | string | 是 |
| upgradeFlag | [UpgradeFlag](arkts-ability-freeinstall-upgradeflag-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
