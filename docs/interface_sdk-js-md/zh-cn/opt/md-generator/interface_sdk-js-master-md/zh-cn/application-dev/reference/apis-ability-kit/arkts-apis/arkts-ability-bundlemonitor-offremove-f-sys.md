# offRemove（系统接口）

## offRemove

```TypeScript
function offRemove(callback?: Callback<BundleChangedInfo>): void
```

注销监听应用的卸载。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.LISTEN_BUNDLE_CHANGE

<!--Device-bundleMonitor-function offRemove(callback?: Callback<BundleChangedInfo>): void--><!--Device-bundleMonitor-function offRemove(callback?: Callback<BundleChangedInfo>): void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[BundleChangedInfo](arkts-ability-bundlemonitor-bundlechangedinfo-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
