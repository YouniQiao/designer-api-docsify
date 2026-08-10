# onRemove（系统接口）

## 导入模块

```TypeScript
import { bundleMonitor } from 'kits/@kit.AbilityKit';
```

## onRemove

```TypeScript
function onRemove(callback: Callback<BundleChangedInfo>): void
```

注册监听应用的卸载。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.LISTEN_BUNDLE_CHANGE

<!--Device-bundleMonitor-function onRemove(callback: Callback<BundleChangedInfo>): void--><!--Device-bundleMonitor-function onRemove(callback: Callback<BundleChangedInfo>): void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BundleChangedInfo&gt; | 是 | 注册监听的AsyncCallback |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 202 | Permission denied, non-system app called system api. |

