# off（系统接口）

## 导入模块

```TypeScript
import { innerBundleManager, BundleStatusCallback } from 'kits/@kit.AbilityKit';
```

## off('BundleStatusChange')

```TypeScript
function off(type: 'BundleStatusChange', callback: AsyncCallback<string>): void
```

取消注册Callback。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> off
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** off

**需要权限：** ohos.permission.LISTEN_BUNDLE_CHANGE

**系统能力：** SystemCapability.BundleManager.BundleFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'BundleStatusChange' | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |


## off('BundleStatusChange')

```TypeScript
function off(type: 'BundleStatusChange'): Promise<string>
```

取消注册Callback。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> off
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** off

**需要权限：** ohos.permission.LISTEN_BUNDLE_CHANGE

**系统能力：** SystemCapability.BundleManager.BundleFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'BundleStatusChange' | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |
